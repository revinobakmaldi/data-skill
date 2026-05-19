#!/usr/bin/env python3
"""
html_to_pdf.py — Convert an HTML file or URL to PDF using Playwright.

Usage:
    python html_to_pdf.py report.html                    # → report.pdf
    python html_to_pdf.py report.html -o output.pdf      # custom output path
    python html_to_pdf.py https://example.com -o out.pdf # from URL
    python html_to_pdf.py report.html --landscape        # landscape orientation

Requirements:
    pip install playwright
    playwright install chromium
"""

import argparse
import os
import sys
from pathlib import Path


def convert(source: str, output: str, landscape: bool = False, wait_ms: int = 500):
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        print("Error: playwright not installed. Run: pip install playwright && playwright install chromium", file=sys.stderr)
        sys.exit(1)

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        # Determine if source is a URL or file path
        if source.startswith("http://") or source.startswith("https://"):
            page.goto(source, wait_until="networkidle")
        else:
            abs_path = Path(source).resolve()
            if not abs_path.exists():
                print(f"Error: File not found: {source}", file=sys.stderr)
                sys.exit(1)
            page.goto(f"file://{abs_path}", wait_until="networkidle")

        # Wait for any JS rendering to complete
        if wait_ms > 0:
            page.wait_for_timeout(wait_ms)

        page.pdf(
            path=output,
            format="A4",
            landscape=landscape,
            print_background=True,
            margin={
                "top": "20mm",
                "right": "15mm",
                "bottom": "20mm",
                "left": "15mm"
            }
        )

        browser.close()
        print(f"[ok] PDF saved: {output}")


def main():
    parser = argparse.ArgumentParser(description="Convert HTML to PDF using Playwright/Chromium")
    parser.add_argument("source", help="HTML file path or URL")
    parser.add_argument("--output", "-o", help="Output PDF path (default: same name as input with .pdf)")
    parser.add_argument("--landscape", action="store_true", help="Landscape orientation")
    parser.add_argument("--wait", type=int, default=500, help="Extra wait time in ms after page load (default: 500)")
    args = parser.parse_args()

    # Auto-generate output path
    if args.output:
        output = args.output
    elif args.source.startswith("http"):
        output = "output.pdf"
    else:
        output = str(Path(args.source).with_suffix(".pdf"))

    convert(args.source, output, landscape=args.landscape, wait_ms=args.wait)


if __name__ == "__main__":
    main()
