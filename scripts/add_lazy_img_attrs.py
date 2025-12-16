#!/usr/bin/env python3

import argparse
import re
from pathlib import Path


IMG_TAG_RE = re.compile(r"<img\b[^>]*>", re.IGNORECASE)


def should_skip_img_tag(tag: str) -> bool:
    # If author already set a strategy, respect it.
    if re.search(r"\bloading\s*=", tag, flags=re.IGNORECASE):
        return True
    # Keep high-priority images eager (typically logo / hero / LCP).
    if re.search(r"\bfetchpriority\s*=\s*(['\"]?)high\1", tag, flags=re.IGNORECASE):
        return True
    return False


def add_attrs_to_img_tag(tag: str) -> str:
    if should_skip_img_tag(tag):
        return tag

    attrs_to_insert = []
    if not re.search(r"\bdecoding\s*=", tag, flags=re.IGNORECASE):
        attrs_to_insert.append('decoding="async"')

    attrs_to_insert.append('loading="lazy"')

    insertion = " " + " ".join(attrs_to_insert)

    # Insert immediately after '<img'
    return re.sub(r"^<img\b", lambda m: m.group(0) + insertion, tag, count=1, flags=re.IGNORECASE)


def process_file(path: Path) -> int:
    original = path.read_text(encoding="utf-8", errors="replace")

    changed = 0

    def repl(match: re.Match) -> str:
        nonlocal changed
        before = match.group(0)
        after = add_attrs_to_img_tag(before)
        if after != before:
            changed += 1
        return after

    updated = IMG_TAG_RE.sub(repl, original)

    if updated != original:
        path.write_text(updated, encoding="utf-8")

    return changed


def main() -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Add loading=lazy (and decoding=async when missing) to <img> tags, "
            "skipping tags that already set loading= or fetchpriority=high."
        )
    )
    parser.add_argument("files", nargs="+", help="HTML files to update")
    args = parser.parse_args()

    total_changed = 0
    for file_str in args.files:
        path = Path(file_str)
        if not path.exists():
            raise SystemExit(f"File not found: {path}")
        changed = process_file(path)
        total_changed += changed
        print(f"{path}: updated {changed} <img> tag(s)")

    print(f"Done. Updated {total_changed} <img> tag(s) total.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
