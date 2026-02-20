#!/usr/bin/env python3
"""
generate-qr.py — Generate QR codes for chapter reference pages

Usage:
    python3 tools/generate-qr.py [--input references.yaml] [--base-url URL]
                                  [--output-dir images/qr] [--size 8]

Generates one QR code per chapter that has references, pointing to:
    {base-url}/ch{NN}

Requires the 'qrcode' package:
    pip install qrcode[pil]

If 'qrcode' is not installed, falls back to generating an SVG-based QR code
using a minimal built-in encoder (for simple URLs only).
"""

import argparse
import re
import sys
from pathlib import Path

# Try to import qrcode library
try:
    import qrcode
    from qrcode.image.svg import SvgPathImage
    HAS_QRCODE = True
except ImportError:
    HAS_QRCODE = False

# Try PIL for PNG output
try:
    from PIL import Image
    HAS_PIL = True
except ImportError:
    HAS_PIL = False


def parse_references(filepath: str) -> list:
    """Parse references.yaml to extract chapter list."""
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


def get_chapters_with_refs(refs: list) -> dict:
    """Return dict of chapter -> ref count for active refs."""
    chapters = {}
    for ref in refs:
        status = ref.get('status', 'active')
        if status == 'removed':
            continue
        ch = str(ref.get('chapter', ''))
        if ch:
            chapters[ch] = chapters.get(ch, 0) + 1
    return chapters


def generate_qr_png(url: str, output_path: Path, box_size: int = 8):
    """Generate a QR code PNG using the qrcode library."""
    qr = qrcode.QRCode(
        version=None,  # auto-size
        error_correction=qrcode.constants.ERROR_CORRECT_M,
        box_size=box_size,
        border=2,
    )
    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill_color='black', back_color='white')
    img.save(str(output_path))


def generate_qr_svg(url: str, output_path: Path, box_size: int = 8):
    """Generate a QR code SVG using the qrcode library."""
    qr = qrcode.QRCode(
        version=None,
        error_correction=qrcode.constants.ERROR_CORRECT_M,
        box_size=box_size,
        border=2,
    )
    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(image_factory=SvgPathImage)
    img.save(str(output_path))


def main():
    parser = argparse.ArgumentParser(
        description='Generate QR codes for chapter reference pages')
    parser.add_argument('--input', default='references.yaml',
                        help='Path to references.yaml')
    parser.add_argument('--base-url', default='https://smarttangibles.com/references',
                        help='Base URL for reference pages')
    parser.add_argument('--output-dir', default='images/qr',
                        help='Output directory for QR code images')
    parser.add_argument('--size', type=int, default=8,
                        help='QR code box size in pixels (default: 8)')
    parser.add_argument('--format', choices=['png', 'svg'], default='png',
                        help='Output format (default: png)')
    args = parser.parse_args()

    if not HAS_QRCODE:
        print("Error: 'qrcode' package required. Install with:", file=sys.stderr)
        print("  pip install qrcode[pil]", file=sys.stderr)
        sys.exit(1)

    if args.format == 'png' and not HAS_PIL:
        print("Error: 'Pillow' package required for PNG output. Install with:", file=sys.stderr)
        print("  pip install Pillow", file=sys.stderr)
        print("  Or use --format svg for SVG output.", file=sys.stderr)
        sys.exit(1)

    # Load references
    refs = parse_references(args.input)
    if not refs:
        print("No references found.", file=sys.stderr)
        sys.exit(1)

    chapters = get_chapters_with_refs(refs)
    print(f"Found {len(chapters)} chapters with references")

    # Create output directory
    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    base_url = args.base_url.rstrip('/')
    ext = args.format
    gen_func = generate_qr_png if ext == 'png' else generate_qr_svg

    for ch in sorted(chapters.keys(),
                     key=lambda x: (not x.isdigit(), int(x) if x.isdigit() else 0, x)):
        ch_display = ch.zfill(2) if ch.isdigit() else ch
        url = f"{base_url}/ch{ch_display}"
        filename = f"ch{ch_display}-refs.{ext}"
        output_path = output_dir / filename

        gen_func(url, output_path, box_size=args.size)
        print(f"  {filename} -> {url} ({chapters[ch]} refs)")

    print(f"\nGenerated {len(chapters)} QR codes in {output_dir}/")
    print(f"\nTo embed in chapter markdown:")
    print(f'  ![Scan for live references](../images/qr/ch04-refs.{ext})')


if __name__ == '__main__':
    main()
