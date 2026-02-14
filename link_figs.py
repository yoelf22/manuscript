#!/usr/bin/env python3
"""Add hyperlinks to image filenames in fig_names.md, linking back to their chapter files."""

import re
import os

CHAPTERS_DIR = os.path.join(os.path.dirname(__file__), "chapters")
FIG_NAMES = os.path.join(CHAPTERS_DIR, "fig_names.md")

# Map chapter numbers to filenames
CH_MAP = {}
for f in os.listdir(CHAPTERS_DIR):
    m = re.match(r"Chapter-(\d+)-(.+)\.md$", f)
    if m:
        CH_MAP[int(m.group(1))] = f

print("Chapter mapping:")
for k in sorted(CH_MAP):
    print(f"  {k} -> {CH_MAP[k]}")

with open(FIG_NAMES, "r") as fh:
    lines = fh.readlines()


def strip_links(text):
    """Remove existing markdown links, keeping just the display text."""
    return re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)


new_lines = []
for line in lines:
    # Detect table rows (start with |, contain data)
    if not line.startswith("|") or line.startswith("|--") or line.startswith("| Fig. No."):
        new_lines.append(line)
        continue

    # Parse table row
    cols = [c.strip() for c in line.split("|")]
    # cols: ['', 'Fig. No.', 'Ch', 'Image Filename(s)', 'Caption', 'Attribution', '']
    if len(cols) < 6:
        new_lines.append(line)
        continue

    fig_no = cols[1]
    ch_str = cols[2].strip()
    filenames_raw = strip_links(cols[3])  # strip any previous links
    caption = cols[4]
    attribution = cols[5]

    try:
        ch_num = int(ch_str)
    except ValueError:
        new_lines.append(line)
        continue

    ch_file = CH_MAP.get(ch_num)
    if not ch_file:
        new_lines.append(line)
        continue

    # Split filenames by comma, make each a hyperlink to ../chapters/ChapterFile.md
    parts = [p.strip() for p in filenames_raw.split(",")]
    linked_parts = []
    for p in parts:
        if p:
            linked_parts.append(f"[{p}](../chapters/{ch_file})")

    new_filenames = ", ".join(linked_parts)
    new_line = f"| {fig_no} | {ch_str} | {new_filenames} | {caption} | {attribution} |\n"
    new_lines.append(new_line)

with open(FIG_NAMES, "w") as fh:
    fh.writelines(new_lines)

print(f"\nDone. Updated {FIG_NAMES}")
