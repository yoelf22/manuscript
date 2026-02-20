#!/usr/bin/env python3
"""
Process book chapters to:
1. Strip bare URLs from endnote entries (chapters with ## Endnotes)
2. Add companion site link at end of endnotes
3. Append References & Sources block with QR code

Idempotent: skips chapters that already have a References & Sources block.
"""

import re
import glob
import os

CHAPTERS_DIR = "/Users/yoel/Desktop/smart-tangibles-book/manuscript/chapters"

# Chapters that have references (from QR generation)
CHAPTERS_WITH_REFS = {0, 1, 3, 4, 5, 6, 7, 8, 10, 11, 12, 13, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25}

# Chapters with existing ## Endnotes sections
CHAPTERS_WITH_ENDNOTES = {3, 4, 25}


def extract_chapter_number(filename):
    """Extract chapter number from filename like Chapter-4-Evolving-Competition.md"""
    m = re.match(r'Chapter-(\d+)-', os.path.basename(filename))
    if m:
        return int(m.group(1))
    return None


def strip_urls_from_endnotes(text, endnotes_start):
    """Strip bare URLs from endnote entries.

    Handles:
    - Lines ending with ` https://...` or ` http://...` (space before URL)
    - Lines ending with `, https://...` or `, http://...` (comma+space before URL)
    - Lines that are just a bare URL → remove entire line
    """
    lines = text.split('\n')
    endnote_line = None

    # Find the line number where ## Endnotes starts
    for i, line in enumerate(lines):
        if line.strip() == '## Endnotes':
            endnote_line = i
            break

    if endnote_line is None:
        return text

    new_lines = []
    for i, line in enumerate(lines):
        if i <= endnote_line:
            new_lines.append(line)
            continue

        stripped = line.strip()

        # Line is just a bare URL → remove entirely
        if re.match(r'^https?://\S+$', stripped):
            continue

        # Line ends with a URL preceded by comma+space or just space
        # Pattern: `, https://...` or ` https://...` at end of line
        modified = re.sub(r',?\s+https?://\S+\s*$', '', line)

        # If we stripped a URL and the line now ends with trailing punctuation cleanup
        # e.g., `- Source, "Title,"` → keep as is (the comma inside quotes is fine)
        modified = modified.rstrip()

        new_lines.append(modified)

    return '\n'.join(new_lines)


def build_reference_block(chapter_num):
    """Build the References & Sources block."""
    nn = f"{chapter_num:02d}"
    return f"""---

**References & Sources**
All references for this chapter — with live links and archived snapshots — are available at the companion site.

[View Chapter {chapter_num} References →](https://yoelf22.github.io/manuscript/references/ch{nn}.html)

[![Scan for chapter references](../images/qr/ch{nn}-refs.png)](https://yoelf22.github.io/manuscript/references/ch{nn}.html)"""


def build_companion_link(chapter_num):
    """Build the companion site link to insert at end of endnotes."""
    nn = f"{chapter_num:02d}"
    return f"\n[View all Chapter {chapter_num} references with live links and archived snapshots →](https://yoelf22.github.io/manuscript/references/ch{nn}.html)"


def process_chapter(filepath, chapter_num):
    """Process a single chapter file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Idempotency check
    if '**References & Sources**' in content:
        print(f"  Chapter {chapter_num}: SKIPPED (already has References & Sources)")
        return False

    has_endnotes = chapter_num in CHAPTERS_WITH_ENDNOTES

    if has_endnotes:
        # Strip URLs from endnotes
        content = strip_urls_from_endnotes(content, '## Endnotes')

        # Ensure content ends with single newline before appending
        content = content.rstrip('\n')

        # Add companion link + reference block at the end
        companion_link = build_companion_link(chapter_num)
        ref_block = build_reference_block(chapter_num)

        content = content + '\n' + companion_link + '\n\n' + ref_block + '\n'

        print(f"  Chapter {chapter_num}: Stripped endnote URLs, added companion link and References & Sources block")
    else:
        # No endnotes — just append reference block at end
        content = content.rstrip('\n')
        ref_block = build_reference_block(chapter_num)
        content = content + '\n\n' + ref_block + '\n'

        print(f"  Chapter {chapter_num}: Added References & Sources block (no endnotes)")

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

    return True


def main():
    # Find all chapter files
    pattern = os.path.join(CHAPTERS_DIR, "Chapter-*-*.md")
    files = sorted(glob.glob(pattern))

    print(f"Found {len(files)} chapter files")
    print(f"Chapters with references: {sorted(CHAPTERS_WITH_REFS)}")
    print(f"Chapters with endnotes: {sorted(CHAPTERS_WITH_ENDNOTES)}")
    print()

    processed = 0
    skipped = 0

    for filepath in files:
        chapter_num = extract_chapter_number(filepath)
        if chapter_num is None:
            print(f"  Could not parse chapter number from: {os.path.basename(filepath)}")
            continue

        if chapter_num not in CHAPTERS_WITH_REFS:
            print(f"  Chapter {chapter_num}: SKIPPED (no references)")
            skipped += 1
            continue

        if process_chapter(filepath, chapter_num):
            processed += 1
        else:
            skipped += 1

    print(f"\nDone. Processed: {processed}, Skipped: {skipped}")


if __name__ == '__main__':
    main()
