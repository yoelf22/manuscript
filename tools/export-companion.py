#!/usr/bin/env python3
"""
export-companion.py — Generate companion site reference pages from references.yaml

Usage:
    python3 tools/export-companion.py [--input references.yaml] [--output-dir companionSite/references]
                                       [--base-url https://smarttangibles.com/references]
                                       [--repo-url https://github.com/yoelf22/manuscript]

Generates:
  1. index.html — master reference directory
  2. ch{NN}.html — per-chapter reference pages
  3. refs.json — JSON API for client-side search/filter
"""

import argparse
import json
import re
import sys
from datetime import datetime
from html import escape as html_escape
from pathlib import Path


# ---------------------------------------------------------------------------
# YAML parser (no PyYAML dependency)
# ---------------------------------------------------------------------------

def parse_references(filepath: str) -> list:
    """Parse references.yaml into a list of dicts."""
    content = Path(filepath).read_text(encoding='utf-8')
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


# ---------------------------------------------------------------------------
# Chapter title mapping
# ---------------------------------------------------------------------------

CHAPTER_TITLES = {
    '0': 'Introduction',
    '1': 'Platform Economics',
    '2': 'Absorption Patterns',
    '3': 'When Gadgets Dissolve Into Features',
    '4': 'Evolving Competition',
    '5': 'Digital Interfaces',
    '6': 'Connectivity & IoT',
}


def get_chapter_title(chapter: str) -> str:
    """Get a display title for a chapter."""
    if chapter in CHAPTER_TITLES:
        return CHAPTER_TITLES[chapter]
    if chapter.isdigit():
        return f'Chapter {chapter}'
    return chapter.replace('-', ' ').title()


# ---------------------------------------------------------------------------
# Status helpers
# ---------------------------------------------------------------------------

def get_status_indicator(ref: dict) -> tuple:
    """Return (emoji, label, css_class) for a reference's status."""
    status = ref.get('status', 'active')
    if status == 'removed':
        return ('&#x26AA;', 'Removed', 'status-removed')

    archive_url = ref.get('archive_url')
    has_archive = archive_url and archive_url != 'null' and archive_url != ''

    # We don't do a live check here — just indicate archive availability
    if has_archive:
        return ('&#x1F7E2;', 'Archived', 'status-archived')
    return ('&#x1F7E1;', 'No archive', 'status-noarchive')


# ---------------------------------------------------------------------------
# HTML templates
# ---------------------------------------------------------------------------

def page_head(title: str, depth: int = 0) -> str:
    """Generate HTML head section. depth=0 for files in references/, depth=1 for nested."""
    css_path = '../assets/css/style.css' if depth == 0 else '../../assets/css/style.css'
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="{html_escape(title)} — Smart Tangibles Reference Directory">
    <title>{html_escape(title)} | Smart Tangibles</title>
    <link rel="stylesheet" href="{css_path}">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <style>
        .ref-page {{ max-width: 960px; margin: 0 auto; padding: 2rem 1.5rem; padding-top: 5rem; }}
        .ref-page h1 {{ margin-bottom: 0.5rem; }}
        .ref-page .subtitle {{ color: var(--color-text-light); margin-bottom: 2rem; }}
        .ref-table {{ width: 100%; border-collapse: collapse; margin: 1.5rem 0; }}
        .ref-table th {{ text-align: left; padding: 0.75rem; border-bottom: 2px solid var(--color-border);
                        font-size: var(--font-size-sm); color: var(--color-text-light);
                        text-transform: uppercase; letter-spacing: 0.5px; }}
        .ref-table td {{ padding: 0.75rem; border-bottom: 1px solid var(--color-border-light);
                        font-size: var(--font-size-sm); vertical-align: top; }}
        .ref-table tr:hover {{ background-color: var(--color-bg-alt); }}
        .ref-num {{ color: var(--color-text-muted); font-weight: 600; white-space: nowrap; }}
        .ref-title {{ font-weight: 500; color: var(--color-text); }}
        .ref-source {{ color: var(--color-text-muted); font-size: var(--font-size-xs); }}
        .ref-links {{ display: flex; gap: 0.5rem; flex-wrap: wrap; }}
        .ref-links a {{ display: inline-flex; align-items: center; padding: 0.25rem 0.5rem;
                       border-radius: 4px; font-size: var(--font-size-xs); font-weight: 500;
                       border: 1px solid var(--color-border); color: var(--color-text); }}
        .ref-links a:hover {{ background-color: var(--color-primary); color: white;
                             border-color: var(--color-primary); }}
        .ref-links .archive-link {{ color: var(--color-accent); border-color: var(--color-accent); }}
        .ref-links .archive-link:hover {{ background-color: var(--color-accent); color: white; }}
        .status-archived {{ color: var(--color-success); }}
        .status-noarchive {{ color: var(--color-warning); }}
        .status-removed {{ color: var(--color-text-muted); }}
        .chapter-grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
                        gap: 1rem; margin: 2rem 0; }}
        .chapter-link {{ display: block; padding: 1.25rem; border: 1px solid var(--color-border);
                        border-radius: var(--border-radius-lg); transition: all 0.2s ease; }}
        .chapter-link:hover {{ border-color: var(--color-primary); box-shadow: var(--shadow-md);
                              transform: translateY(-2px); }}
        .chapter-link .ch-num {{ font-size: var(--font-size-sm); font-weight: 700;
                                color: var(--color-primary); }}
        .chapter-link h3 {{ font-size: var(--font-size-base); margin: 0.25rem 0; color: var(--color-text); }}
        .chapter-link .ch-count {{ font-size: var(--font-size-sm); color: var(--color-text-muted); }}
        .feedback-bar {{ margin-top: 2rem; padding: 1rem 1.5rem; background: var(--color-bg-alt);
                        border-radius: var(--border-radius); display: flex; align-items: center;
                        justify-content: space-between; flex-wrap: wrap; gap: 1rem; }}
        .feedback-bar p {{ color: var(--color-text-light); font-size: var(--font-size-sm); margin: 0; }}
        .feedback-bar a {{ font-size: var(--font-size-sm); font-weight: 500; }}
        .back-link {{ display: inline-flex; align-items: center; gap: 0.25rem;
                     font-size: var(--font-size-sm); margin-bottom: 1rem; }}
        .generated-note {{ text-align: center; color: var(--color-text-muted);
                          font-size: var(--font-size-xs); margin-top: 3rem;
                          padding-top: 1.5rem; border-top: 1px solid var(--color-border-light); }}
    </style>
</head>
"""


def page_nav(home_path: str = '../') -> str:
    """Generate simplified navigation bar."""
    return f"""<body>
    <nav class="navbar">
        <div class="nav-container">
            <a href="{home_path}index.html" class="nav-logo">
                <span class="logo-smart">Smart</span><span class="logo-tangibles">Tangibles</span>
            </a>
            <ul class="nav-menu">
                <li><a href="{home_path}index.html#tools">Tools</a></li>
                <li><a href="{home_path}references/">References</a></li>
                <li><a href="{home_path}index.html#book">The Book</a></li>
            </ul>
        </div>
    </nav>
"""


def page_footer(generated_date: str) -> str:
    return f"""
    <p class="generated-note">
        Reference directory generated on {html_escape(generated_date)} by
        <a href="https://github.com/yoelf22/manuscript">Smart Tangibles reference tools</a>.
    </p>
</body>
</html>
"""


def feedback_bar(chapter: str, repo_url: str) -> str:
    """Generate feedback section with GitHub Issues and general feedback links."""
    issue_title = f"Broken+link+in+Chapter+{chapter}"
    issue_url = f"{repo_url}/issues/new?title={issue_title}&labels=broken-link"

    return f"""    <div class="feedback-bar">
        <p>Found a broken link or outdated source?</p>
        <div>
            <a href="{html_escape(issue_url)}" target="_blank" rel="noopener">Report on GitHub</a>
            &nbsp;&bull;&nbsp;
            <a href="mailto:yoel@theroad.co.il?subject=Broken%20link%20report%20-%20Chapter%20{chapter}">Email report</a>
        </div>
    </div>
"""


# ---------------------------------------------------------------------------
# Page generators
# ---------------------------------------------------------------------------

def generate_index_page(refs_by_chapter: dict, generated_date: str, repo_url: str) -> str:
    """Generate the master index.html reference directory."""
    total_refs = sum(len(refs) for refs in refs_by_chapter.values())
    archived = sum(
        1 for refs in refs_by_chapter.values()
        for r in refs
        if r.get('archive_url') and r['archive_url'] != 'null'
    )

    html = page_head('Reference Directory')
    html += page_nav('../')
    html += f"""
    <div class="ref-page">
        <h1>Reference Directory</h1>
        <p class="subtitle">
            All sources cited in <em>Smart Tangibles</em> — {total_refs} references across
            {len(refs_by_chapter)} chapters. {archived} sources archived via the Wayback Machine.
        </p>

        <div class="chapter-grid">
"""

    for ch in sorted(refs_by_chapter.keys(),
                     key=lambda x: (not x.isdigit(), int(x) if x.isdigit() else 0, x)):
        refs = refs_by_chapter[ch]
        active_refs = [r for r in refs if r.get('status', 'active') != 'removed']
        ch_display = ch.zfill(2) if ch.isdigit() else ch
        title = get_chapter_title(ch)
        html += f"""            <a href="ch{ch_display}.html" class="chapter-link">
                <span class="ch-num">Chapter {ch_display}</span>
                <h3>{html_escape(title)}</h3>
                <span class="ch-count">{len(active_refs)} references</span>
            </a>
"""

    html += """        </div>
"""
    html += feedback_bar('all', repo_url)
    html += f"""    </div>
"""
    html += page_footer(generated_date)
    return html


def generate_chapter_page(chapter: str, refs: list, generated_date: str,
                          base_url: str, repo_url: str) -> str:
    """Generate a per-chapter reference page."""
    ch_display = chapter.zfill(2) if chapter.isdigit() else chapter
    title = get_chapter_title(chapter)
    active_refs = [r for r in refs if r.get('status', 'active') != 'removed']

    html = page_head(f'Chapter {ch_display} — {title}: References')
    html += page_nav('../')
    html += f"""
    <div class="ref-page">
        <a href="index.html" class="back-link">&larr; All chapters</a>
        <h1>Chapter {html_escape(ch_display)} — {html_escape(title)}</h1>
        <p class="subtitle">{len(active_refs)} references</p>

        <table class="ref-table">
            <thead>
                <tr>
                    <th>#</th>
                    <th>Reference</th>
                    <th>Links</th>
                    <th>Status</th>
                </tr>
            </thead>
            <tbody>
"""

    for i, ref in enumerate(active_refs, 1):
        ref_title = ref.get('title', '') or ref.get('source', '') or 'Untitled'
        ref_url = ref.get('url', '')
        clean_url = ref.get('clean_url', '') or ref_url
        archive_url = ref.get('archive_url')
        has_archive = archive_url and archive_url != 'null' and archive_url != ''
        source = ref.get('source', '')
        authors = ref.get('authors', '')
        date = ref.get('date', '')

        # Build citation line
        citation_parts = []
        if authors:
            citation_parts.append(html_escape(str(authors)))
        if date:
            citation_parts.append(f'({html_escape(str(date))})')
        citation_parts.append(f'<span class="ref-title">{html_escape(str(ref_title))}</span>')
        if source:
            citation_parts.append(f'<span class="ref-source">{html_escape(str(source))}</span>')
        citation = ' '.join(citation_parts)

        # Status indicator
        emoji, status_label, css_class = get_status_indicator(ref)

        # Links
        links_html = f'<a href="{html_escape(str(clean_url))}" target="_blank" rel="noopener">Source</a>'
        if has_archive:
            links_html += f' <a href="{html_escape(str(archive_url))}" target="_blank" rel="noopener" class="archive-link">Archive</a>'

        html += f"""                <tr>
                    <td class="ref-num">{i}</td>
                    <td>{citation}</td>
                    <td class="ref-links">{links_html}</td>
                    <td><span class="{css_class}">{emoji} {html_escape(status_label)}</span></td>
                </tr>
"""

    html += """            </tbody>
        </table>
"""
    html += feedback_bar(ch_display, repo_url)
    html += """    </div>
"""
    html += page_footer(generated_date)
    return html


def generate_refs_json(refs_by_chapter: dict) -> str:
    """Generate refs.json for client-side use."""
    output = {}
    for ch, refs in refs_by_chapter.items():
        ch_display = ch.zfill(2) if ch.isdigit() else ch
        output[ch_display] = []
        for ref in refs:
            if ref.get('status', 'active') == 'removed':
                continue
            archive_url = ref.get('archive_url')
            has_archive = bool(archive_url and archive_url != 'null' and archive_url != '')
            output[ch_display].append({
                'id': ref.get('id', ''),
                'title': ref.get('title', ''),
                'authors': ref.get('authors', ''),
                'date': ref.get('date', ''),
                'source': ref.get('source', ''),
                'url': ref.get('clean_url') or ref.get('url', ''),
                'archive_url': archive_url if has_archive else None,
                'type': ref.get('type', ''),
                'context': ref.get('context', ''),
            })

    return json.dumps(output, indent=2, ensure_ascii=False)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description='Generate companion site reference pages from references.yaml')
    parser.add_argument('--input', default='references.yaml',
                        help='Path to references.yaml')
    parser.add_argument('--output-dir', default='companionSite/references',
                        help='Output directory for generated pages')
    parser.add_argument('--base-url', default='https://smarttangibles.com/references',
                        help='Base URL for the reference pages (used in QR codes)')
    parser.add_argument('--repo-url', default='https://github.com/yoelf22/manuscript',
                        help='GitHub repository URL for issue reporting')
    args = parser.parse_args()

    # Load references
    refs = parse_references(args.input)
    if not refs:
        print("No references found.", file=sys.stderr)
        sys.exit(1)

    print(f"Loaded {len(refs)} references from {args.input}")

    # Group by chapter
    refs_by_chapter = {}
    for ref in refs:
        ch = str(ref.get('chapter', '?'))
        if ch not in refs_by_chapter:
            refs_by_chapter[ch] = []
        refs_by_chapter[ch].append(ref)

    print(f"Found references for {len(refs_by_chapter)} chapters")

    # Create output directory
    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    generated_date = datetime.now().strftime('%Y-%m-%d')

    # Generate index page
    index_html = generate_index_page(refs_by_chapter, generated_date, args.repo_url)
    (output_dir / 'index.html').write_text(index_html, encoding='utf-8')
    print(f"  Wrote {output_dir / 'index.html'}")

    # Generate per-chapter pages
    for ch, ch_refs in refs_by_chapter.items():
        ch_display = ch.zfill(2) if ch.isdigit() else ch
        filename = f'ch{ch_display}.html'
        page_html = generate_chapter_page(ch, ch_refs, generated_date,
                                          args.base_url, args.repo_url)
        (output_dir / filename).write_text(page_html, encoding='utf-8')
        active = len([r for r in ch_refs if r.get('status', 'active') != 'removed'])
        print(f"  Wrote {output_dir / filename} ({active} refs)")

    # Generate JSON
    refs_json = generate_refs_json(refs_by_chapter)
    (output_dir / 'refs.json').write_text(refs_json, encoding='utf-8')
    print(f"  Wrote {output_dir / 'refs.json'}")

    total_active = sum(
        1 for ch_refs in refs_by_chapter.values()
        for r in ch_refs if r.get('status', 'active') != 'removed'
    )
    print(f"\nDone: {len(refs_by_chapter)} chapter pages + index + JSON ({total_active} active refs)")


if __name__ == '__main__':
    main()
