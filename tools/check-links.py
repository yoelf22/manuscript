#!/usr/bin/env python3
"""
check-links.py — Check HTTP status of all URLs in references.yaml

Usage:
    python3 tools/check-links.py [--input references.yaml] [--report reports/link-health.md]
                                  [--timeout 15] [--parallel 5]

Outputs a Markdown report with:
  - Summary statistics (alive / redirected / dead / timeout / error)
  - Per-chapter breakdown
  - Detailed table of all URLs with status
  - List of dead URLs needing attention

Designed to run periodically (monthly/quarterly) as a maintenance tool.
"""

import argparse
import concurrent.futures
import os
import re
import ssl
import sys
import time
import urllib.request
import urllib.error
from datetime import datetime
from pathlib import Path

# Try to import yaml; fall back to a simple parser if unavailable
try:
    import yaml
    HAS_YAML = True
except ImportError:
    HAS_YAML = False


def parse_yaml_simple(filepath: str) -> list:
    """Minimal YAML list-of-dicts parser for references.yaml when PyYAML unavailable."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find the references: block
    match = re.search(r'^references:\s*\n', content, re.MULTILINE)
    if not match:
        return []

    refs_text = content[match.end():]
    entries = []
    current = {}

    for line in refs_text.split('\n'):
        stripped = line.strip()
        if not stripped or stripped.startswith('#'):
            continue

        if stripped.startswith('- id:'):
            if current:
                entries.append(current)
            current = {}
            val = stripped[len('- id:'):].strip()
            current['id'] = val.strip('"')
        elif ':' in stripped and current is not None:
            key, _, val = stripped.partition(':')
            key = key.strip()
            val = val.strip()
            # Handle null
            if val == 'null':
                val = None
            elif val == 'false':
                val = False
            elif val == 'true':
                val = True
            else:
                val = val.strip('"')
            current[key] = val

    if current:
        entries.append(current)

    return entries


def load_references(filepath: str) -> list:
    """Load references from YAML file."""
    if HAS_YAML:
        with open(filepath, 'r', encoding='utf-8') as f:
            data = yaml.safe_load(f)
        return data.get('references', [])
    else:
        return parse_yaml_simple(filepath)


def check_url(url: str, timeout: int = 15) -> dict:
    """Check a single URL and return status info."""
    result = {
        'url': url,
        'status': 'unknown',
        'http_code': None,
        'redirect_url': None,
        'error': None,
        'response_time_ms': None,
    }

    # Create SSL context that doesn't verify (some sites have cert issues)
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) '
                       'AppleWebKit/537.36 (KHTML, like Gecko) '
                       'Chrome/120.0.0.0 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    }

    try:
        req = urllib.request.Request(url, headers=headers, method='HEAD')
        start = time.time()
        with urllib.request.urlopen(req, timeout=timeout, context=ctx) as resp:
            elapsed = (time.time() - start) * 1000
            result['http_code'] = resp.getcode()
            result['response_time_ms'] = round(elapsed)
            final_url = resp.geturl()
            if final_url != url:
                result['status'] = 'redirected'
                result['redirect_url'] = final_url
            else:
                result['status'] = 'alive'
    except urllib.error.HTTPError as e:
        result['http_code'] = e.code
        if e.code in (403, 405):
            # Some servers block HEAD; retry with GET
            try:
                req2 = urllib.request.Request(url, headers=headers, method='GET')
                start = time.time()
                with urllib.request.urlopen(req2, timeout=timeout, context=ctx) as resp2:
                    elapsed = (time.time() - start) * 1000
                    result['http_code'] = resp2.getcode()
                    result['response_time_ms'] = round(elapsed)
                    result['status'] = 'alive'
                    final_url = resp2.geturl()
                    if final_url != url:
                        result['status'] = 'redirected'
                        result['redirect_url'] = final_url
            except Exception as e2:
                result['status'] = 'dead'
                result['error'] = str(e2)[:120]
        elif e.code == 429:
            result['status'] = 'rate-limited'
            result['error'] = 'Too many requests'
        elif e.code >= 400:
            result['status'] = 'dead'
            result['error'] = f'HTTP {e.code}'
    except urllib.error.URLError as e:
        result['status'] = 'dead'
        result['error'] = str(e.reason)[:120]
    except TimeoutError:
        result['status'] = 'timeout'
        result['error'] = f'Timed out after {timeout}s'
    except Exception as e:
        result['status'] = 'error'
        result['error'] = str(e)[:120]

    return result


def check_all_urls(refs: list, timeout: int = 15, max_workers: int = 5,
                   progress: bool = True) -> list:
    """Check all URLs with parallel requests, respecting rate limits."""
    total = len(refs)
    results = [None] * total

    # Group by domain to avoid hammering a single host
    if progress:
        print(f"Checking {total} URLs (timeout={timeout}s, workers={max_workers})...")

    with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
        future_to_idx = {}
        for i, ref in enumerate(refs):
            url = ref.get('clean_url') or ref.get('url', '')
            if not url:
                results[i] = {'url': '', 'status': 'skipped', 'http_code': None,
                              'redirect_url': None, 'error': 'No URL', 'response_time_ms': None}
                continue
            future = executor.submit(check_url, url, timeout)
            future_to_idx[future] = i

        done_count = 0
        for future in concurrent.futures.as_completed(future_to_idx):
            idx = future_to_idx[future]
            try:
                results[idx] = future.result()
            except Exception as e:
                results[idx] = {'url': refs[idx].get('url', ''), 'status': 'error',
                                'http_code': None, 'redirect_url': None,
                                'error': str(e)[:120], 'response_time_ms': None}
            done_count += 1
            if progress and done_count % 10 == 0:
                print(f"  {done_count}/{total} checked...")

    if progress:
        print(f"  {total}/{total} done.")

    return results


def generate_report(refs: list, results: list, report_date: str) -> str:
    """Generate a Markdown health report."""
    # Compute stats
    status_counts = {}
    chapter_stats = {}

    for ref, res in zip(refs, results):
        st = res['status']
        status_counts[st] = status_counts.get(st, 0) + 1

        ch = ref.get('chapter', '?')
        if ch not in chapter_stats:
            chapter_stats[ch] = {'alive': 0, 'redirected': 0, 'dead': 0,
                                 'timeout': 0, 'error': 0, 'rate-limited': 0,
                                 'skipped': 0, 'unknown': 0}
        chapter_stats[ch][st] = chapter_stats[ch].get(st, 0) + 1

    total = len(refs)
    alive = status_counts.get('alive', 0) + status_counts.get('redirected', 0)
    dead = status_counts.get('dead', 0)
    timeout = status_counts.get('timeout', 0)
    rate_limited = status_counts.get('rate-limited', 0)
    errors = status_counts.get('error', 0) + status_counts.get('unknown', 0)

    lines = []
    lines.append(f"# Link Health Report")
    lines.append(f"")
    lines.append(f"**Generated:** {report_date}")
    lines.append(f"**Total URLs checked:** {total}")
    lines.append(f"")
    lines.append(f"## Summary")
    lines.append(f"")
    lines.append(f"| Status | Count | % |")
    lines.append(f"|--------|------:|----:|")
    lines.append(f"| Alive | {alive} | {alive*100//total}% |")
    lines.append(f"| Dead (4xx/5xx/unreachable) | {dead} | {dead*100//total}% |")
    lines.append(f"| Timeout | {timeout} | {timeout*100//total}% |")
    lines.append(f"| Rate-limited (429) | {rate_limited} | {rate_limited*100//total}% |")
    lines.append(f"| Error/Unknown | {errors} | {errors*100//total}% |")
    lines.append(f"")

    # Per-chapter summary
    lines.append(f"## Per-Chapter Breakdown")
    lines.append(f"")
    lines.append(f"| Chapter | Total | Alive | Dead | Timeout | Other |")
    lines.append(f"|---------|------:|------:|-----:|--------:|------:|")
    for ch in sorted(chapter_stats.keys(),
                     key=lambda x: (not x.isdigit(), int(x) if x.isdigit() else 0, x)):
        s = chapter_stats[ch]
        ch_total = sum(s.values())
        ch_alive = s.get('alive', 0) + s.get('redirected', 0)
        ch_dead = s.get('dead', 0)
        ch_timeout = s.get('timeout', 0)
        ch_other = ch_total - ch_alive - ch_dead - ch_timeout
        label = f"Ch. {ch}" if ch.isdigit() else ch
        lines.append(f"| {label} | {ch_total} | {ch_alive} | {ch_dead} | {ch_timeout} | {ch_other} |")
    lines.append(f"")

    # Dead URLs detail
    dead_refs = [(ref, res) for ref, res in zip(refs, results) if res['status'] == 'dead']
    if dead_refs:
        lines.append(f"## Dead URLs ({len(dead_refs)})")
        lines.append(f"")
        lines.append(f"These URLs returned errors and need attention:")
        lines.append(f"")
        lines.append(f"| ID | Chapter | HTTP | URL | Error |")
        lines.append(f"|----|---------|-----:|-----|-------|")
        for ref, res in dead_refs:
            ch = ref.get('chapter', '?')
            http = res.get('http_code', '-') or '-'
            url = ref.get('url', '')
            # Truncate URL for display
            url_display = url[:80] + '...' if len(url) > 80 else url
            error = (res.get('error', '') or '')[:60]
            has_archive = 'Yes' if ref.get('archive_url') else 'No'
            lines.append(f"| {ref.get('id', '')} | {ch} | {http} | {url_display} | {error} |")
        lines.append(f"")

    # Timeout URLs
    timeout_refs = [(ref, res) for ref, res in zip(refs, results) if res['status'] == 'timeout']
    if timeout_refs:
        lines.append(f"## Timed Out URLs ({len(timeout_refs)})")
        lines.append(f"")
        lines.append(f"These URLs timed out and may need manual verification:")
        lines.append(f"")
        for ref, res in timeout_refs:
            lines.append(f"- `{ref.get('id', '')}` (Ch. {ref.get('chapter', '?')}): {ref.get('url', '')}")
        lines.append(f"")

    # Redirected URLs
    redir_refs = [(ref, res) for ref, res in zip(refs, results) if res['status'] == 'redirected']
    if redir_refs:
        lines.append(f"## Redirected URLs ({len(redir_refs)})")
        lines.append(f"")
        lines.append(f"These URLs redirect. Consider updating to the final destination:")
        lines.append(f"")
        for ref, res in redir_refs:
            lines.append(f"- `{ref.get('id', '')}` (Ch. {ref.get('chapter', '?')}): {ref.get('url', '')[:70]}")
            lines.append(f"  -> {res.get('redirect_url', '')[:90]}")
        lines.append(f"")

    # Rate-limited
    rl_refs = [(ref, res) for ref, res in zip(refs, results) if res['status'] == 'rate-limited']
    if rl_refs:
        lines.append(f"## Rate-Limited URLs ({len(rl_refs)})")
        lines.append(f"")
        lines.append(f"These URLs returned 429 (too many requests). Re-check manually:")
        lines.append(f"")
        for ref, res in rl_refs:
            lines.append(f"- `{ref.get('id', '')}` (Ch. {ref.get('chapter', '?')}): {ref.get('url', '')}")
        lines.append(f"")

    lines.append(f"---")
    lines.append(f"*Report generated by `tools/check-links.py`*")
    return '\n'.join(lines) + '\n'


def main():
    parser = argparse.ArgumentParser(description='Check health of all URLs in references.yaml')
    parser.add_argument('--input', default='references.yaml',
                        help='Path to references.yaml')
    parser.add_argument('--report', default='reports/link-health.md',
                        help='Output report path')
    parser.add_argument('--timeout', type=int, default=15,
                        help='HTTP request timeout in seconds')
    parser.add_argument('--parallel', type=int, default=5,
                        help='Number of parallel requests')
    args = parser.parse_args()

    # Load references
    refs = load_references(args.input)
    if not refs:
        print("No references found.", file=sys.stderr)
        sys.exit(1)

    print(f"Loaded {len(refs)} references from {args.input}")

    # Check all URLs
    results = check_all_urls(refs, timeout=args.timeout, max_workers=args.parallel)

    # Generate report
    report_date = datetime.now().strftime('%Y-%m-%d %H:%M')
    report = generate_report(refs, results, report_date)

    # Write report
    report_path = Path(args.report)
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(report, encoding='utf-8')
    print(f"\nReport written to {report_path}")

    # Quick summary to stdout
    status_counts = {}
    for res in results:
        st = res['status']
        status_counts[st] = status_counts.get(st, 0) + 1

    print(f"\nQuick summary:")
    for st in ['alive', 'redirected', 'dead', 'timeout', 'rate-limited', 'error', 'unknown']:
        if st in status_counts:
            print(f"  {st}: {status_counts[st]}")


if __name__ == '__main__':
    main()
