#!/usr/bin/env python3
"""Convert heavy project card background images to WebP.

This repo serves static assets from linke/PUBLIC/projects. The project cards on the
homepage use these images as CSS backgrounds via shared/lazy-bg.js.

WebP is typically much smaller than PNG and loads faster on Vercel/CDNs.

- Converts *.png and *.jpg in linke/PUBLIC/projects to *.webp (same basename)
- Skips conversion if the .webp already exists
"""

from __future__ import annotations

from pathlib import Path


from PIL import Image  # type: ignore


ROOT = Path(__file__).resolve().parents[1]
PROJECTS_DIR = ROOT / "linke" / "PUBLIC" / "projects"


def convert_to_webp(src: Path, dst: Path) -> None:
    with Image.open(src) as im:
        # Normalize mode for WebP
        if im.mode not in {"RGB", "RGBA"}:
            im = im.convert("RGBA" if "A" in im.getbands() else "RGB")

        dst.parent.mkdir(parents=True, exist_ok=True)
        im.save(
            dst,
            format="WEBP",
            quality=82,
            method=6,
            optimize=True,
        )


def main() -> int:
    if not PROJECTS_DIR.exists():
        raise SystemExit(f"Missing directory: {PROJECTS_DIR}")

    sources = sorted(list(PROJECTS_DIR.glob("*.png")) + list(PROJECTS_DIR.glob("*.jpg")) + list(PROJECTS_DIR.glob("*.jpeg")))
    if not sources:
        print("No project images found to convert.")
        return 0

    converted = 0
    skipped = 0
    for src in sources:
        dst = src.with_suffix(".webp")
        if dst.exists():
            skipped += 1
            continue
        convert_to_webp(src, dst)
        converted += 1

    print(f"Converted: {converted} | Skipped (already existed): {skipped}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
