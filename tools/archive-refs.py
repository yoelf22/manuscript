#!/usr/bin/env python3
"""
archive-refs.py — Find Wayback Machine snapshots for all URLs in references.yaml

Usage:
    python3 tools/archive-refs.py [--input references.yaml] [--output references.yaml]
                                   [--timeout 15] [--parallel 3] [--save-only]

For each URL in the registry, queries the Wayback Machine Availability API
to find the closest existing snapshot. Updates archive_url and archive_date
fields in-place.

Uses the Availability API (read-only, no snapshots created):
    https://archive.org/wayback/available?url=URL

To actually *create* new snapshots, use --save mode which hits:
    https://web.archive.org/save/URL
(Rate-limited; use sparingly)
"""

import argparse
import concurrent.futures
import json
import os
import re
import sys
import time
import urllib.request
import urllib.error
import urllib.parse
import ssl
from datetime import datetime
from pathlib import Path


# ---------------------------------------------------------------------------
# YAML I/O (no PyYAML dependency)
# ---------------------------------------------------------------------------

def load_references_raw(filepath: str) -> str:
    """Load the raw YAML text."""
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()


def parse_entries(content: str) -> list:
    """Minimal YAML parser for references.yaml — returns list of dicts."""
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
            val = stripped[len('- id:'):].strip().strip('"')
            current['id'] = val
        elif ':' in stripped and current is not None:
            key, _, val = stripped.partition(':')
            key = key.strip()
            val = val.strip()
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


def update_yaml_field(content: str, ref_id: str, field: str, value) -> str:
    """Update a single field for a given ref ID in the raw YAML text."""
    # Find the entry block
    id_pattern = re.compile(
        r'(  - id: ' + re.escape(ref_id) + r'\n(?:    \w.*\n)*?)'
        r'(    ' + re.escape(field) + r': )(.*)(\n)',
        re.MULTILINE
    )

    if value is None:
        replacement_val = 'null'
    elif isinstance(value, bool):
        replacement_val = 'true' if value else 'false'
    elif isinstance(value, str):
        if any(c in value for c in ':{}[]&*?|>!%@`#,\'"\\') or value.startswith(('-', ' ')):
            escaped = value.replace('\\', '\\\\').replace('"', '\\"')
            replacement_val = f'"{escaped}"'
        else:
            replacement_val = f'"{value}"'
    else:
        replacement_val = str(value)

    def replacer(m):
        return m.group(1) + m.group(2) + replacement_val + m.group(4)

    new_content, count = id_pattern.subn(replacer, content)
    if count == 0:
        # Try simpler pattern (field might not be in the expected block position)
        simple = re.compile(
            r'(- id: ' + re.escape(ref_id) + r'\n(?:.*\n)*?'
            r'    ' + re.escape(field) + r': )(.*)(\n)'
        )
        new_content, count = simple.subn(
            lambda m: m.group(1) + replacement_val + m.group(3),
            content
        )

    return new_content


# ---------------------------------------------------------------------------
# Wayback Machine API
# ---------------------------------------------------------------------------

def check_wayback_availability(url: str, timeout: int = 15) -> dict:
    """Query Wayback Machine Availability API for existing snapshots."""
    result = {
        'url': url,
        'available': False,
        'archive_url': None,
        'archive_date': None,
        'error': None,
    }

    api_url = f"https://archive.org/wayback/available?url={urllib.parse.quote(url, safe='')}"

    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    headers = {
        'User-Agent': 'SmartTangiblesBookRefChecker/1.0 (book manuscript reference preservation)',
        'Accept': 'application/json',
    }

    try:
        req = urllib.request.Request(api_url, headers=headers)
        with urllib.request.urlopen(req, timeout=timeout, context=ctx) as resp:
            data = json.loads(resp.read().decode('utf-8'))

        snapshots = data.get('archived_snapshots', {})
        closest = snapshots.get('closest', {})

        if closest.get('available'):
            result['available'] = True
            result['archive_url'] = closest.get('url', '')
            # Parse timestamp: 20231215123456 -> 2023-12-15
            ts = closest.get('timestamp', '')
            if len(ts) >= 8:
                result['archive_date'] = f"{ts[:4]}-{ts[4:6]}-{ts[6:8]}"

    except urllib.error.HTTPError as e:
        result['error'] = f'HTTP {e.code}'
    except urllib.error.URLError as e:
        result['error'] = str(e.reason)[:100]
    except TimeoutError:
        result['error'] = f'Timeout after {timeout}s'
    except Exception as e:
        result['error'] = str(e)[:100]

    return result


def save_to_wayback(url: str, timeout: int = 30) -> dict:
    """Request Wayback Machine to create a new snapshot via Save Page Now."""
    result = {
        'url': url,
        'saved': False,
        'archive_url': None,
        'error': None,
    }

    save_url = f"https://web.archive.org/save/{url}"

    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    headers = {
        'User-Agent': 'SmartTangiblesBookRefChecker/1.0 (book manuscript reference preservation)',
    }

    try:
        req = urllib.request.Request(save_url, headers=headers)
        with urllib.request.urlopen(req, timeout=timeout, context=ctx) as resp:
            final_url = resp.geturl()
            if 'web.archive.org' in final_url:
                result['saved'] = True
                result['archive_url'] = final_url
    except urllib.error.HTTPError as e:
        # 302 redirect to the archived page is actually success
        if e.code in (301, 302) and e.headers.get('Location'):
            loc = e.headers['Location']
            if 'web.archive.org' in loc:
                result['saved'] = True
                result['archive_url'] = loc
            else:
                result['error'] = f'Redirect to {loc[:80]}'
        else:
            result['error'] = f'HTTP {e.code}'
    except Exception as e:
        result['error'] = str(e)[:100]

    return result


def lookup_all(refs: list, timeout: int = 15, max_workers: int = 3,
               delay: float = 0, progress: bool = True) -> list:
    """Check Wayback availability for all URLs.

    When delay > 0, runs sequentially to respect rate limits.
    When delay == 0 and max_workers > 1, runs in parallel.
    """
    total = len(refs)
    results = [None] * total

    if progress:
        mode = "sequential" if delay > 0 else f"parallel (workers={max_workers})"
        print(f"Checking Wayback availability for {total} URLs "
              f"(timeout={timeout}s, {mode})...")

    if delay > 0:
        # Sequential with delay — for rate-limit-safe retries
        for i, ref in enumerate(refs):
            url = ref.get('clean_url') or ref.get('url', '')
            if not url:
                results[i] = {'url': '', 'available': False, 'archive_url': None,
                              'archive_date': None, 'error': 'No URL'}
                continue
            results[i] = check_wayback_availability(url, timeout)
            if progress and (i + 1) % 10 == 0:
                print(f"  {i+1}/{total} checked...")
            if i < total - 1:
                time.sleep(delay)
    else:
        # Parallel
        with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
            future_to_idx = {}
            for i, ref in enumerate(refs):
                url = ref.get('clean_url') or ref.get('url', '')
                if not url:
                    results[i] = {'url': '', 'available': False, 'archive_url': None,
                                  'archive_date': None, 'error': 'No URL'}
                    continue
                future = executor.submit(check_wayback_availability, url, timeout)
                future_to_idx[future] = i

            done_count = 0
            for future in concurrent.futures.as_completed(future_to_idx):
                idx = future_to_idx[future]
                try:
                    results[idx] = future.result()
                except Exception as e:
                    results[idx] = {'url': refs[idx].get('url', ''), 'available': False,
                                    'archive_url': None, 'archive_date': None,
                                    'error': str(e)[:100]}
                done_count += 1
                if progress and done_count % 20 == 0:
                    print(f"  {done_count}/{total} checked...")

    if progress:
        print(f"  {total}/{total} done.")

    return results


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description='Find Wayback Machine snapshots for references.yaml URLs')
    parser.add_argument('--input', default='references.yaml',
                        help='Path to references.yaml')
    parser.add_argument('--output', default=None,
                        help='Output path (default: same as input, in-place update)')
    parser.add_argument('--timeout', type=int, default=15,
                        help='HTTP request timeout in seconds')
    parser.add_argument('--parallel', type=int, default=3,
                        help='Number of parallel requests (keep low to respect rate limits)')
    parser.add_argument('--delay', type=float, default=0,
                        help='Delay in seconds between requests (enables sequential mode)')
    parser.add_argument('--skip-existing', action='store_true',
                        help='Skip entries that already have archive_url set')
    parser.add_argument('--save', action='store_true',
                        help='Also trigger Save Page Now for URLs without snapshots')
    parser.add_argument('--report', default='reports/wayback-report.md',
                        help='Output report path')
    args = parser.parse_args()

    if args.output is None:
        args.output = args.input

    # Load
    raw_content = load_references_raw(args.input)
    refs = parse_entries(raw_content)
    if not refs:
        print("No references found.", file=sys.stderr)
        sys.exit(1)

    print(f"Loaded {len(refs)} references from {args.input}")

    # Filter to only entries needing lookup
    if args.skip_existing:
        lookup_refs = [r for r in refs if not r.get('archive_url') or r['archive_url'] == 'null']
        skipped = len(refs) - len(lookup_refs)
        print(f"Skipping {skipped} entries with existing archive_url")
    else:
        lookup_refs = refs

    # Check availability
    results = lookup_all(lookup_refs, timeout=args.timeout,
                         max_workers=args.parallel, delay=args.delay)

    # Stats
    available = sum(1 for r in results if r and r.get('available'))
    missing = sum(1 for r in results if r and not r.get('available') and not r.get('error'))
    errors = sum(1 for r in results if r and r.get('error'))

    print(f"\nWayback availability (this run):")
    print(f"  Snapshot found: {available}")
    print(f"  No snapshot:    {missing}")
    print(f"  Errors:         {errors}")

    # Update YAML
    updated_content = raw_content
    update_count = 0
    for ref, res in zip(lookup_refs, results):
        if res and res.get('available') and res.get('archive_url'):
            updated_content = update_yaml_field(
                updated_content, ref['id'], 'archive_url', res['archive_url'])
            updated_content = update_yaml_field(
                updated_content, ref['id'], 'archive_date', res.get('archive_date'))
            update_count += 1

    # Write updated YAML
    Path(args.output).write_text(updated_content, encoding='utf-8')
    print(f"\nUpdated {update_count} entries in {args.output}")

    # Generate report
    checked = len(lookup_refs)
    report_lines = []
    report_lines.append("# Wayback Machine Snapshot Report")
    report_lines.append("")
    report_lines.append(f"**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    report_lines.append(f"**Total URLs in registry:** {len(refs)}")
    report_lines.append(f"**Checked this run:** {checked}")
    if args.skip_existing:
        report_lines.append(f"**Skipped (already archived):** {len(refs) - checked}")
    report_lines.append("")
    report_lines.append("## Summary")
    report_lines.append("")
    report_lines.append(f"| Status | Count | % |")
    report_lines.append(f"|--------|------:|----:|")
    pct = lambda n: f"{n*100//checked}%" if checked else "0%"
    report_lines.append(f"| Snapshot found | {available} | {pct(available)} |")
    report_lines.append(f"| No snapshot | {missing} | {pct(missing)} |")
    report_lines.append(f"| API error | {errors} | {pct(errors)} |")
    report_lines.append("")

    # URLs without snapshots
    no_snapshot = [(ref, res) for ref, res in zip(lookup_refs, results)
                   if res and not res.get('available') and not res.get('error')]
    if no_snapshot:
        report_lines.append(f"## URLs Without Snapshots ({len(no_snapshot)})")
        report_lines.append("")
        report_lines.append("These URLs have no Wayback Machine archive. Consider using "
                          "`--save` to trigger archival.")
        report_lines.append("")
        for ref, res in no_snapshot:
            ch = ref.get('chapter', '?')
            url = ref.get('clean_url') or ref.get('url', '')
            report_lines.append(f"- `{ref['id']}` (Ch. {ch}): {url[:90]}")
        report_lines.append("")

    # Errors
    error_refs = [(ref, res) for ref, res in zip(lookup_refs, results)
                  if res and res.get('error')]
    if error_refs:
        report_lines.append(f"## API Errors ({len(error_refs)})")
        report_lines.append("")
        for ref, res in error_refs:
            ch = ref.get('chapter', '?')
            report_lines.append(f"- `{ref['id']}` (Ch. {ch}): {res['error']}")
        report_lines.append("")

    report_lines.append("---")
    report_lines.append("*Report generated by `tools/archive-refs.py`*")

    report_path = Path(args.report)
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text('\n'.join(report_lines) + '\n', encoding='utf-8')
    print(f"Report written to {report_path}")

    # Optionally trigger Save Page Now for missing snapshots
    if args.save and no_snapshot:
        print(f"\n--- Save Page Now ---")
        print(f"Requesting snapshots for {len(no_snapshot)} URLs without archives...")
        print(f"(This is rate-limited; may take a while)")

        save_count = 0
        for i, (ref, _) in enumerate(no_snapshot):
            url = ref.get('clean_url') or ref.get('url', '')
            if not url:
                continue

            res = save_to_wayback(url, timeout=30)
            if res.get('saved'):
                save_count += 1
                print(f"  [{i+1}/{len(no_snapshot)}] Saved: {ref['id']}")
                # Update YAML
                updated_content = update_yaml_field(
                    updated_content, ref['id'], 'archive_url', res['archive_url'])
                updated_content = update_yaml_field(
                    updated_content, ref['id'], 'archive_date',
                    datetime.now().strftime('%Y-%m-%d'))
            else:
                print(f"  [{i+1}/{len(no_snapshot)}] Failed: {ref['id']} — {res.get('error', 'unknown')}")

            # Rate limit: wait between saves
            time.sleep(5)

        Path(args.output).write_text(updated_content, encoding='utf-8')
        print(f"\nSaved {save_count}/{len(no_snapshot)} new snapshots")


if __name__ == '__main__':
    main()
