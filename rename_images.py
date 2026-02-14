#!/usr/bin/env python3
"""
rename_images.py - Rename book images to human-readable fig-style names.

Parses all markdown files in the chapters/ directory for image references,
generates new filenames following the convention fig{CC}-{NN}-{slug}.{ext},
and optionally applies the changes.

Usage:
    python rename_images.py              # Dry run (default)
    python rename_images.py --dry-run    # Explicit dry run
    python rename_images.py --apply      # Apply changes
"""

from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import sys
from collections import OrderedDict
from pathlib import Path
from typing import Dict, List, Optional, Tuple

# ── Paths ────────────────────────────────────────────────────────────────────
BASE_DIR = Path(__file__).resolve().parent
CHAPTERS_DIR = BASE_DIR / "chapters"
IMAGES_DIR = BASE_DIR / "images"
MAPPING_FILE = BASE_DIR / "rename_mapping.json"
FIG_NAMES_FILE = CHAPTERS_DIR / "fig_names.md"

# ── Constants ────────────────────────────────────────────────────────────────
SKIP_ARTICLES = {"the", "a", "an", "of", "in", "on", "at", "to", "for", "and",
                 "or", "by", "is", "its", "with", "from", "vs", "via", "as"}

# Files to skip entirely (reference files, old_ prefixed files, copy-of- files)
SKIP_FILE_PREFIXES = ("markdwon_reference", "old_", "copy-of-")

# The special banner image that appears across multiple chapters
BANNER_IMAGE = "73dd11_0b92f228f82c496483131707d652d041~mv2.jpg"
BANNER_NEW_NAME = "fig00-00-capabilities-revenue.jpg"

# Regex to detect already-renamed fig-style filenames
FIG_PATTERN = re.compile(r"^fig\d{2}-\d{2}-")

# Max slug length
MAX_SLUG_LENGTH = 30


def extract_chapter_number(filename: str) -> Optional[int]:
    """
    Extract chapter number from a markdown filename.
    Handles patterns like:
        Chapter-0-Hardware-Needs-To-Get-Smart-Now.md  -> 0
        Chapter-25-Reviving-iRobot.md                -> 25
        old_Chapter-4-Evolving-Competition.md         -> 4  (but skipped)
        Arc-0-About-This-Book.md                     -> None (not a chapter)
    """
    m = re.search(r"Chapter-(\d+)-", filename)
    if m:
        return int(m.group(1))
    return None


def should_skip_file(filename: str) -> bool:
    """Determine if a markdown file should be skipped."""
    for prefix in SKIP_FILE_PREFIXES:
        if filename.startswith(prefix):
            return True
    return False


def generate_slug(alt_text: str) -> str:
    """
    Generate a 2-4 word kebab-case slug from alt text.

    - Lowercases
    - Strips nested markdown image references (malformed alt text)
    - Removes special characters
    - Skips articles and short filler words
    - Takes first 2-4 meaningful words
    - Truncates to MAX_SLUG_LENGTH chars
    """
    if not alt_text or not alt_text.strip():
        return "untitled"

    text = alt_text.strip()

    # Remove any nested markdown image syntax  ![...](...)
    text = re.sub(r"!\[.*?\]\(.*?\)", "", text)

    # Remove URLs
    text = re.sub(r"https?://\S+", "", text)

    # Remove Wix-style hash fragments (73dd11_xxxx...)
    text = re.sub(r"73dd11_[a-f0-9~]+mv2", "", text)
    text = re.sub(r"73dd11_[a-f0-9~]+", "", text)

    # Remove image file paths that leaked into alt text
    text = re.sub(r"\.\./images/[^\s]+", "", text)

    # Lowercase
    text = text.lower()

    # Remove special characters, keep alphanumeric and spaces
    text = re.sub(r"[^a-z0-9\s]", " ", text)

    # Collapse whitespace
    text = re.sub(r"\s+", " ", text).strip()

    if not text:
        return "untitled"

    words = text.split()

    # Filter out articles and filler words
    meaningful = [w for w in words if w not in SKIP_ARTICLES]

    # If filtering removed everything, fall back to unfiltered
    if not meaningful:
        meaningful = words

    # Take 2-4 words
    selected = meaningful[:4]

    # If we have more than 4 and the slug would be too long, trim further
    slug = "-".join(selected)
    if len(slug) > MAX_SLUG_LENGTH:
        # Try with fewer words
        for count in range(3, 0, -1):
            slug = "-".join(selected[:count])
            if len(slug) <= MAX_SLUG_LENGTH:
                break

    # Final truncation safety net
    if len(slug) > MAX_SLUG_LENGTH:
        slug = slug[:MAX_SLUG_LENGTH].rstrip("-")

    return slug if slug else "untitled"


def parse_image_references(md_content: str):
    """
    Parse all image references from markdown content.
    Yields (alt_text, image_path) tuples.

    Pattern: ![alt text](path/to/image)

    Handles:
    - Normal: ![alt](../images/file.png)
    - Spaces in paths: ![alt](../images/my file.png)
    - Nested/malformed alt text: ![![inner](path)](../images/file.png)
    """
    # We need a robust regex that handles:
    # 1. Nested brackets in alt text (malformed markdown)
    # 2. Parentheses in filenames like Flashlight_(Wuzur).jpg
    #
    # Strategy: match balanced parens in the path by looking for the closing
    # paren that follows a file extension or the last paren on the line.
    pattern = re.compile(
        r"!\[([^\]]*(?:\[[^\]]*\][^\]]*)*)\]"       # alt text with possible nested []
        r"\(([^()]*(?:\([^()]*\)[^()]*)*)\)"         # image path allowing balanced parens
    )

    for match in pattern.finditer(md_content):
        alt_text = match.group(1)
        image_path = match.group(2).strip()
        yield alt_text, image_path


def is_images_path(image_path: str) -> bool:
    """Check if the image path references ../images/ directory."""
    return image_path.startswith("../images/")


def get_relative_image_name(image_path: str) -> str:
    """
    Extract the image filename (possibly with subdirectory) from the path.
    ../images/foo.png           -> foo.png
    ../images/poc2prod/bar.png  -> poc2prod/bar.png
    """
    prefix = "../images/"
    if image_path.startswith(prefix):
        return image_path[len(prefix):]
    return image_path


def build_image_mapping(chapters_dir: Path) -> dict:
    """
    Scan all chapter markdown files and build a mapping of
    old_image_name -> (new_image_name, chapter_num, figure_num, alt_text).

    Returns an OrderedDict: {old_filename: new_filename}
    """
    # First pass: collect all image references with chapter info
    # Structure: {image_name: [(chapter_num, alt_text, md_filename), ...]}
    image_refs: Dict[str, List[Tuple[Optional[int], str, str]]] = {}

    # Get all markdown files, sorted by chapter number (non-chapter files last)
    all_md_files = list(chapters_dir.glob("*.md"))

    def sort_key(p: Path) -> Tuple[int, str]:
        ch = extract_chapter_number(p.name)
        if ch is not None:
            return (0, f"{ch:04d}")
        return (1, p.name)

    md_files = sorted(all_md_files, key=sort_key)

    for md_file in md_files:
        filename = md_file.name

        # Skip reference files, old_ prefixed, copy-of- prefixed
        if should_skip_file(filename):
            continue

        chapter_num = extract_chapter_number(filename)

        try:
            content = md_file.read_text(encoding="utf-8")
        except (UnicodeDecodeError, IOError):
            print(f"WARNING: Could not read {filename}, skipping.", file=sys.stderr)
            continue

        for alt_text, image_path in parse_image_references(content):
            # Skip images that don't reference ../images/
            if not is_images_path(image_path):
                continue

            image_name = get_relative_image_name(image_path)

            if image_name not in image_refs:
                image_refs[image_name] = []

            image_refs[image_name].append((chapter_num, alt_text, filename))

    # Second pass: assign figure numbers per chapter and generate new names
    # Group images by chapter (use FIRST chapter they appear in)
    # chapter_figures: {chapter_num: [(image_name, alt_text), ...]} in order
    chapter_figures: Dict[int, List[Tuple[str, str]]] = {}
    image_to_chapter: Dict[str, int] = {}  # track first chapter assignment

    # Process all images, assign each to its first chapter
    for image_name, refs in image_refs.items():
        # Handle the special banner image
        if image_name == BANNER_IMAGE:
            image_to_chapter[image_name] = 0  # Special: chapter 00, figure 00
            continue

        # Find the first chapter reference (prefer actual chapter numbers)
        first_chapter = None
        first_alt = ""

        for ch_num, alt_text, md_filename in refs:
            if ch_num is not None:
                if first_chapter is None:
                    first_chapter = ch_num
                    first_alt = alt_text
                    break

        # If no chapter number found (e.g., from Arc files, Preface, etc.),
        # try to assign based on a non-chapter file
        if first_chapter is None:
            # Use the first reference's alt text
            first_alt = refs[0][1] if refs else ""
            # Assign to chapter 99 for non-chapter images
            first_chapter = 99

        image_to_chapter[image_name] = first_chapter

        if first_chapter not in chapter_figures:
            chapter_figures[first_chapter] = []

        chapter_figures[first_chapter].append((image_name, first_alt))

    # Third pass: generate the mapping
    mapping = OrderedDict()

    # Handle the special banner image first
    if BANNER_IMAGE in image_to_chapter:
        mapping[BANNER_IMAGE] = BANNER_NEW_NAME

    # Process each chapter in order
    for chapter_num in sorted(chapter_figures.keys()):
        figures = chapter_figures[chapter_num]

        for fig_idx, (image_name, alt_text) in enumerate(figures, start=1):
            # Skip if already has a fig-style name (idempotency)
            basename = os.path.basename(image_name)
            if FIG_PATTERN.match(basename):
                continue

            # Determine subdirectory prefix (e.g., "poc2prod/")
            subdir = ""
            if "/" in image_name:
                subdir = image_name.rsplit("/", 1)[0] + "/"
                basename = image_name.rsplit("/", 1)[1]

            # Get extension
            _, ext = os.path.splitext(basename)
            ext = ext.lower()

            # Generate slug
            slug = generate_slug(alt_text)

            # Format chapter and figure numbers
            cc = f"{chapter_num:02d}"
            nn = f"{fig_idx:02d}"

            new_name = f"{subdir}fig{cc}-{nn}-{slug}{ext}"

            # Ensure uniqueness: if new_name already assigned, append a suffix
            existing_new_names = set(mapping.values())
            if new_name in existing_new_names:
                suffix = 2
                while f"{subdir}fig{cc}-{nn}-{slug}-{suffix}{ext}" in existing_new_names:
                    suffix += 1
                new_name = f"{subdir}fig{cc}-{nn}-{slug}-{suffix}{ext}"

            mapping[image_name] = new_name

    return mapping


def apply_file_renames(mapping: dict, images_dir: Path) -> list[str]:
    """
    Rename actual image files on disk.
    Returns a list of status messages.
    """
    messages = []

    for old_name, new_name in mapping.items():
        old_path = images_dir / old_name
        new_path = images_dir / new_name

        if not old_path.exists():
            messages.append(f"  SKIP (not found): {old_name}")
            continue

        if old_path == new_path:
            messages.append(f"  SKIP (same name): {old_name}")
            continue

        if new_path.exists():
            messages.append(f"  SKIP (target exists): {new_name}")
            continue

        # Ensure target subdirectory exists
        new_path.parent.mkdir(parents=True, exist_ok=True)

        shutil.move(str(old_path), str(new_path))
        messages.append(f"  RENAMED: {old_name} -> {new_name}")

    return messages


def update_markdown_references(mapping: dict, chapters_dir: Path) -> list[str]:
    """
    Update all image references in .md files in the chapters directory.
    Returns a list of status messages.
    """
    messages = []

    # Build a lookup for old path -> new path (as they appear in markdown)
    path_mapping = {}
    for old_name, new_name in mapping.items():
        old_path = f"../images/{old_name}"
        new_path = f"../images/{new_name}"
        path_mapping[old_path] = new_path

    md_files = sorted(chapters_dir.glob("*.md"))

    for md_file in md_files:
        try:
            content = md_file.read_text(encoding="utf-8")
        except (UnicodeDecodeError, IOError):
            continue

        original = content
        replacements = 0

        for old_path, new_path in path_mapping.items():
            if old_path in content:
                count = content.count(old_path)
                content = content.replace(old_path, new_path)
                replacements += count

        if content != original:
            md_file.write_text(content, encoding="utf-8")
            messages.append(f"  UPDATED: {md_file.name} ({replacements} reference(s))")

    return messages


def update_fig_names_md(mapping: dict, fig_names_file: Path) -> list[str]:
    """
    Update the fig_names.md file, replacing old filenames with new ones
    in the Image Filename(s) column.
    Returns a list of status messages.
    """
    messages = []

    if not fig_names_file.exists():
        messages.append("  SKIP: fig_names.md not found")
        return messages

    try:
        content = fig_names_file.read_text(encoding="utf-8")
    except (UnicodeDecodeError, IOError):
        messages.append("  SKIP: Could not read fig_names.md")
        return messages

    original = content
    replacements = 0

    for old_name, new_name in mapping.items():
        # In fig_names.md, filenames appear without the ../images/ prefix
        # They may include subdirectory prefixes like poc2prod/
        if old_name in content:
            content = content.replace(old_name, new_name)
            replacements += 1

    if content != original:
        fig_names_file.write_text(content, encoding="utf-8")
        messages.append(f"  UPDATED: fig_names.md ({replacements} filename(s) replaced)")
    else:
        messages.append("  NO CHANGES: fig_names.md (no matching filenames found)")

    return messages


def print_mapping(mapping: dict, dry_run: bool = True):
    """Print the proposed or applied mapping."""
    mode = "DRY RUN" if dry_run else "APPLIED"
    print(f"\n{'='*72}")
    print(f"  Image Rename Mapping ({mode})")
    print(f"{'='*72}\n")

    if not mapping:
        print("  No images to rename.\n")
        return

    # Group by chapter for readability
    chapter_groups: Dict[str, List[Tuple[str, str]]] = {}
    for old_name, new_name in mapping.items():
        # Extract chapter from new name
        m = re.match(r"(?:.*/)?fig(\d{2})-", new_name)
        ch = m.group(1) if m else "??"
        key = f"Chapter {int(ch)}" if ch != "??" else "Unknown"
        if key not in chapter_groups:
            chapter_groups[key] = []
        chapter_groups[key].append((old_name, new_name))

    for chapter, items in chapter_groups.items():
        print(f"  --- {chapter} ---")
        for old_name, new_name in items:
            print(f"    {old_name}")
            print(f"      -> {new_name}")
        print()

    print(f"  Total: {len(mapping)} image(s)\n")


def main():
    parser = argparse.ArgumentParser(
        description="Rename book images to human-readable fig-style names."
    )
    group = parser.add_mutually_exclusive_group()
    group.add_argument(
        "--dry-run",
        action="store_true",
        default=True,
        help="Print proposed mapping without making changes (default)"
    )
    group.add_argument(
        "--apply",
        action="store_true",
        help="Apply changes: rename files, update markdown references"
    )

    args = parser.parse_args()

    # --apply overrides --dry-run
    dry_run = not args.apply

    # Validate directories exist
    if not CHAPTERS_DIR.is_dir():
        print(f"ERROR: Chapters directory not found: {CHAPTERS_DIR}", file=sys.stderr)
        sys.exit(1)
    if not IMAGES_DIR.is_dir():
        print(f"ERROR: Images directory not found: {IMAGES_DIR}", file=sys.stderr)
        sys.exit(1)

    print("Scanning chapter files for image references...")
    mapping = build_image_mapping(CHAPTERS_DIR)

    # Always write the JSON mapping file
    with open(MAPPING_FILE, "w", encoding="utf-8") as f:
        json.dump(mapping, f, indent=2, ensure_ascii=False)
    print(f"Mapping written to: {MAPPING_FILE}")

    # Print the mapping
    print_mapping(mapping, dry_run=dry_run)

    if dry_run:
        print("  [DRY RUN] No files were modified.")
        print(f"  Run with --apply to rename files and update references.\n")
    else:
        print("Applying changes...\n")

        # 1. Rename image files
        print("--- Renaming image files ---")
        rename_msgs = apply_file_renames(mapping, IMAGES_DIR)
        for msg in rename_msgs:
            print(msg)

        # 2. Update markdown references in chapter files
        print("\n--- Updating markdown references ---")
        md_msgs = update_markdown_references(mapping, CHAPTERS_DIR)
        for msg in md_msgs:
            print(msg)

        # 3. Update fig_names.md
        print("\n--- Updating fig_names.md ---")
        fig_msgs = update_fig_names_md(mapping, FIG_NAMES_FILE)
        for msg in fig_msgs:
            print(msg)

        print(f"\nDone. {len(mapping)} image(s) processed.\n")


if __name__ == "__main__":
    main()
