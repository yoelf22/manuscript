#!/usr/bin/env python3
"""
extract-refs.py — Extract all external URLs from book manuscript chapters
and generate a draft references.yaml registry.

Usage:
    python3 tools/extract-refs.py [--chapters-dir chapters/] [--output references.yaml]

Handles these citation patterns found in the manuscript:
  1. Inline markdown links: [text](url)
  2. Bare URLs (http/https) not inside markdown link syntax
  3. HTML-commented URLs: <!--url-->
  4. URLs inside <u><span> wrappers
  5. Figure caption attributions
  6. Endnote sections
  7. Patent links, YouTube links, etc.
"""

import re
import sys
import os
import argparse
from pathlib import Path
from collections import OrderedDict
from urllib.parse import urlparse

# ---------------------------------------------------------------------------
# URL extraction patterns
# ---------------------------------------------------------------------------

# Markdown link: [text](url)
# Handles balanced parentheses in URLs (e.g., Wikimedia File:Name_(part).JPG)
MARKDOWN_LINK_RE = re.compile(
    r'\[([^\]]*)\]\((https?://(?:[^\s\(\)]|\([^\s\)]*\))+)\)'
)

# Bare URL not already captured by markdown link syntax.
# Matches http(s) URLs that are NOT preceded by ]( (which would be a markdown link)
BARE_URL_RE = re.compile(
    r'(?<!\]\()(?<!\()(https?://[^\s\)\]>"\'`,;]+)'
)

# HTML comment with URL
COMMENT_URL_RE = re.compile(
    r'<!--\s*(https?://[^\s>]+?)\s*-->'
)


def extract_chapter_number(filename: str) -> str:
    """Extract chapter number from filename, or return a descriptive label."""
    m = re.search(r'Chapter-(\d+)', filename)
    if m:
        return m.group(1)
    # Arc files, front/end matter, etc.
    name = Path(filename).stem
    return name


def classify_url_type(url: str, context: str) -> str:
    """Guess the reference type based on URL and surrounding context."""
    url_lower = url.lower()
    ctx_lower = context.lower()

    if 'youtu.be' in url_lower or 'youtube.com' in url_lower:
        return 'video'
    if 'doi.org' in url_lower:
        return 'journal-article'
    if 'patents.google.com' in url_lower:
        return 'patent'
    if any(ext in url_lower for ext in ['.pdf']):
        return 'report'
    if any(ext in url_lower for ext in ['.jpg', '.jpeg', '.png', '.gif', '.svg']):
        return 'image'
    if 'flickr.com' in url_lower or 'unsplash.com' in url_lower or 'commons.wikimedia' in url_lower:
        return 'image'
    if 'github.com' in url_lower:
        return 'software'
    if 'web.archive.org' in url_lower:
        return 'web-archive'

    # Context-based heuristics
    if re.search(r'figure\s+\d+', ctx_lower):
        return 'image'
    if 'report' in ctx_lower or 'study' in ctx_lower:
        return 'report'

    return 'web-article'


def classify_context(context: str) -> str:
    """Determine where in the chapter this URL appears."""
    ctx_lower = context.lower()
    if re.search(r'\*\*figure\s+\d+', ctx_lower):
        return 'figure-caption'
    if '## endnotes' in ctx_lower or re.match(r'\s*\*\*[¹²³⁴⁵⁶⁷⁸⁹⁰]+', context):
        return 'endnote'
    if 'further reading' in ctx_lower or 'read more' in ctx_lower:
        return 'further-reading'
    if '<!--' in context:
        return 'html-comment'
    return 'inline'


def get_context_lines(lines: list, line_idx: int, window: int = 2) -> str:
    """Get surrounding lines for context."""
    start = max(0, line_idx - window)
    end = min(len(lines), line_idx + window + 1)
    return '\n'.join(lines[start:end])


def extract_urls_from_file(filepath: str) -> list:
    """Extract all URLs from a markdown file with context."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    lines = content.split('\n')

    found = []  # list of (url, link_text, line_number, context_snippet, context_type)
    seen_urls_in_file = set()

    for i, line in enumerate(lines):
        # 1) Markdown links
        for match in MARKDOWN_LINK_RE.finditer(line):
            link_text = match.group(1)
            url = match.group(2)
            # Strip trailing punctuation that got captured
            url = url.rstrip('.,;:')
            if url not in seen_urls_in_file:
                ctx = get_context_lines(lines, i)
                found.append((url, link_text, i + 1, ctx, classify_context(ctx)))
                seen_urls_in_file.add(url)

        # 2) HTML comment URLs
        for match in COMMENT_URL_RE.finditer(line):
            url = match.group(1).rstrip('.,;:')
            if url not in seen_urls_in_file:
                ctx = get_context_lines(lines, i)
                found.append((url, '', i + 1, ctx, 'html-comment'))
                seen_urls_in_file.add(url)

        # 3) Bare URLs (not already found as part of markdown links)
        for match in BARE_URL_RE.finditer(line):
            url = match.group(1).rstrip('.,;:*')
            if url not in seen_urls_in_file:
                # Verify it's not part of a markdown link we already captured
                # by checking if it appears inside (url) pattern
                pre = line[:match.start()]
                if not pre.endswith(']('):
                    ctx = get_context_lines(lines, i)
                    found.append((url, '', i + 1, ctx, classify_context(ctx)))
                    seen_urls_in_file.add(url)

    return found


def is_excluded_url(url: str) -> bool:
    """Filter out non-external URLs and excluded domains."""
    parsed = urlparse(url)
    if not parsed.scheme or not parsed.netloc:
        return True
    # Filter out localhost, example.com, etc.
    if parsed.netloc in ('localhost', '127.0.0.1', 'example.com'):
        return True
    # Unsplash: image attribution handled separately, not tracked as references
    if 'unsplash.com' in parsed.netloc:
        return True
    return False


def clean_url(url: str) -> str:
    """Clean tracking parameters and trailing artifacts from URLs."""
    # Remove common tracking params
    url = re.sub(r'[?&]utm_source=[^&\s]*', '', url)
    url = re.sub(r'[?&]utm_medium=[^&\s]*', '', url)
    url = re.sub(r'[?&]utm_campaign=[^&\s]*', '', url)
    # Clean up orphaned ? or &
    url = re.sub(r'\?&', '?', url)
    url = url.rstrip('?&')
    return url


def extract_domain(url: str) -> str:
    """Extract readable source name from URL."""
    parsed = urlparse(url)
    domain = parsed.netloc.replace('www.', '')
    return domain


def yaml_escape(s: str) -> str:
    """Escape a string for safe YAML output."""
    if not s:
        return '""'
    # If it contains special chars, quote it
    if any(c in s for c in ':{}[]&*?|>!%@`#,\'"\\'):
        escaped = s.replace('\\', '\\\\').replace('"', '\\"')
        return f'"{escaped}"'
    if s.startswith(('-', ' ')) or s.endswith(' '):
        return f'"{s}"'
    return f'"{s}"'


def generate_yaml(all_refs: list) -> str:
    """Generate references.yaml content."""
    header = """# references.yaml — Master Reference Registry
# Smart Tangibles: Strategic Product Management for Connected Hardware
#
# Generated by tools/extract-refs.py
# Each entry is keyed by a unique ID: ref-ch{chapter}-{sequence}
#
# Fields:
#   id:             Unique reference identifier
#   chapter:        Chapter number or section name
#   type:           web-article | report | image | video | patent | software | journal-article | web-archive
#   authors:        Author(s) — empty string if unknown, fill in manually
#   date:           Publication year — empty string if unknown
#   title:          Page/article title — auto-filled from link text or empty
#   source:         Publication/site name (domain-derived)
#   url:            Original URL
#   clean_url:      URL with tracking params removed
#   doi:            DOI if available (replaces URL per APA 7)
#   archive_url:    Wayback Machine snapshot URL (fill in Step 2)
#   archive_date:   Date snapshot was taken (fill in Step 2)
#   access_date:    Date author last verified URL
#   license:        For images: CC license string
#   context:        Where in chapter: inline | figure-caption | endnote | further-reading | html-comment
#   line:           Line number in source file
#   companion_site: Whether linked from companion site
#   notes:          Additional context
#
# STATUS: Draft — auto-extracted, needs manual enrichment
# ---------------------------------------------------------

references:
"""

    entries = []
    for ref in all_refs:
        entry = f"""  - id: {ref['id']}
    chapter: {yaml_escape(ref['chapter'])}
    type: {ref['type']}
    authors: ""
    date: ""
    title: {yaml_escape(ref['title'])}
    source: {yaml_escape(ref['source'])}
    url: {yaml_escape(ref['url'])}
    clean_url: {yaml_escape(ref['clean_url'])}
    doi: null
    archive_url: null
    archive_date: null
    access_date: null
    license: null
    context: {ref['context']}
    line: {ref['line']}
    companion_site: false
    notes: {yaml_escape(ref['notes'])}"""
        entries.append(entry)

    return header + '\n'.join(entries) + '\n'


def main():
    parser = argparse.ArgumentParser(description='Extract URLs from manuscript chapters')
    parser.add_argument('--chapters-dir', default='chapters/',
                        help='Path to chapters directory')
    parser.add_argument('--output', default='references.yaml',
                        help='Output YAML file path')
    parser.add_argument('--stats', action='store_true',
                        help='Print statistics only, do not write file')
    args = parser.parse_args()

    chapters_dir = Path(args.chapters_dir)
    if not chapters_dir.exists():
        print(f"Error: chapters directory '{chapters_dir}' not found", file=sys.stderr)
        sys.exit(1)

    # Collect all .md files, sorted
    md_files = sorted(chapters_dir.glob('*.md'))
    # Exclude scraps subdirectory and support/inventory files that would create duplicates
    EXCLUDE_FILES = {
        'external_links.md', 'fig_names.md', 'video_names.md', 'table_names.md',
        'markdwon_reference.md', 'copy-of-chapter-5-digital-interfaces.md',
        'annotated-toc.md', 'Smart-tangibles_ Chapter feedback.md',
        'TOC_exp_v2.md',
    }
    md_files = [f for f in md_files if 'scraps' not in str(f) and f.name not in EXCLUDE_FILES]

    print(f"Scanning {len(md_files)} markdown files...")

    all_refs = []
    chapter_counts = {}

    for filepath in md_files:
        chapter = extract_chapter_number(filepath.name)
        urls = extract_urls_from_file(str(filepath))

        # Track per-chapter sequence numbers
        if chapter not in chapter_counts:
            chapter_counts[chapter] = 0

        for url, link_text, line_num, context_snippet, ctx_type in urls:
            if is_excluded_url(url):
                continue

            chapter_counts[chapter] += 1
            seq = chapter_counts[chapter]

            # Build the ID
            ch_label = chapter.zfill(2) if chapter.isdigit() else chapter.lower()[:10]
            ref_id = f"ref-ch{ch_label}-{seq:03d}"

            clean = clean_url(url)
            url_type = classify_url_type(url, context_snippet)
            source = extract_domain(url)

            # Build a note from the context
            note = ''
            if ctx_type == 'figure-caption':
                fig_match = re.search(r'[Ff]igure\s+(\d+\.\d+)', context_snippet)
                if fig_match:
                    note = f"Figure {fig_match.group(1)}"
            elif ctx_type == 'endnote':
                note = 'Endnote reference'

            all_refs.append({
                'id': ref_id,
                'chapter': chapter,
                'type': url_type,
                'title': link_text.strip() if link_text else '',
                'source': source,
                'url': url,
                'clean_url': clean,
                'context': ctx_type,
                'line': line_num,
                'notes': note,
            })

    # Print statistics
    print(f"\nExtracted {len(all_refs)} external URLs from {len(chapter_counts)} files")
    print(f"\nPer-chapter breakdown:")
    for ch in sorted(chapter_counts.keys(), key=lambda x: (not x.isdigit(), int(x) if x.isdigit() else 0, x)):
        label = f"Chapter {ch}" if ch.isdigit() else ch
        print(f"  {label}: {chapter_counts[ch]} URLs")

    type_counts = {}
    for ref in all_refs:
        type_counts[ref['type']] = type_counts.get(ref['type'], 0) + 1
    print(f"\nBy type:")
    for t, c in sorted(type_counts.items(), key=lambda x: -x[1]):
        print(f"  {t}: {c}")

    context_counts = {}
    for ref in all_refs:
        context_counts[ref['context']] = context_counts.get(ref['context'], 0) + 1
    print(f"\nBy context:")
    for ctx, c in sorted(context_counts.items(), key=lambda x: -x[1]):
        print(f"  {ctx}: {c}")

    if args.stats:
        return

    # Write YAML
    yaml_content = generate_yaml(all_refs)
    output_path = Path(args.output)
    output_path.write_text(yaml_content, encoding='utf-8')
    print(f"\nWrote {output_path} ({len(all_refs)} entries)")


if __name__ == '__main__':
    main()
