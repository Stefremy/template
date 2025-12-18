#!/usr/bin/env python3
"""Check local asset references in exported HTML.

Scans HTML files under linke/ and extracts common asset references:
- <script src=...>
- <link href=...> (stylesheets, preloads)
- <img src=...>, <source src/srcset>

It then resolves workspace-local paths and reports missing files.

Notes:
- External URLs (http/https) are ignored.
- Query strings and fragments are stripped.
- Absolute paths like /PUBLIC/foo.png are resolved under linke/.
"""

from __future__ import annotations

import os
import re
import sys
from dataclasses import dataclass
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlparse


WORKSPACE = Path(__file__).resolve().parents[1]
LINKE_DIR = WORKSPACE / "linke"


def _strip_qs(url: str) -> str:
    return url.split("#", 1)[0].split("?", 1)[0]


def _is_external(url: str) -> bool:
    u = url.strip()
    if not u:
        return True
    if u.startswith("//"):
        return True
    parsed = urlparse(u)
    return parsed.scheme in {"http", "https", "data", "mailto", "tel"}


def _normalize(url: str) -> str:
    u = _strip_qs(url.strip())
    # Remove surrounding quotes if any
    u = u.strip('"\'')
    return u


def _resolve_to_file(html_file: Path, ref: str) -> Path | None:
    ref = _normalize(ref)
    if not ref or _is_external(ref):
        return None

    # Decode percent-encoding so '/PUBLIC/foo%20bar.png' maps to 'foo bar.png'
    ref = unquote(ref)

    # Ignore javascript pseudo-URLs
    if ref.lower().startswith("javascript:"):
        return None

    # Ignore anchors
    if ref.startswith("#"):
        return None

    # Absolute site paths (/PUBLIC/..., /wp-content/..., /wp-includes/...)
    if ref.startswith("/"):
        return LINKE_DIR / ref.lstrip("/")

    # Otherwise resolve relative to HTML file location
    return (html_file.parent / ref).resolve()


@dataclass(frozen=True)
class Ref:
    html: Path
    tag: str
    attr: str
    value: str


class _RefParser(HTMLParser):
    def __init__(self, html_path: Path):
        super().__init__(convert_charrefs=True)
        self.html_path = html_path
        self.refs: list[Ref] = []

    def handle_starttag(self, tag: str, attrs):
        attrs_dict = {k: v for k, v in attrs if k}

        # script src
        if tag == "script" and "src" in attrs_dict:
            self.refs.append(Ref(self.html_path, tag, "src", attrs_dict["src"] or ""))

        # link href
        if tag == "link" and "href" in attrs_dict:
            self.refs.append(Ref(self.html_path, tag, "href", attrs_dict["href"] or ""))

        # img src
        if tag == "img" and "src" in attrs_dict:
            self.refs.append(Ref(self.html_path, tag, "src", attrs_dict["src"] or ""))

        # source src / srcset
        if tag == "source":
            if "src" in attrs_dict:
                self.refs.append(Ref(self.html_path, tag, "src", attrs_dict["src"] or ""))
            if "srcset" in attrs_dict:
                self.refs.append(Ref(self.html_path, tag, "srcset", attrs_dict["srcset"] or ""))

        # a href (optional, can catch missing html pages too)
        if tag == "a" and "href" in attrs_dict:
            self.refs.append(Ref(self.html_path, tag, "href", attrs_dict["href"] or ""))


_SRCSET_SPLIT_RE = re.compile(r"\s*,\s*")


def _expand_srcset(value: str) -> list[str]:
    parts = _SRCSET_SPLIT_RE.split(value.strip())
    urls: list[str] = []
    for part in parts:
        if not part:
            continue
        # Each entry is: url [descriptor]
        url = part.strip().split()[0]
        if url:
            urls.append(url)
    return urls


def main() -> int:
    if not LINKE_DIR.exists():
        print(f"ERROR: linke/ directory not found at {LINKE_DIR}")
        return 2

    html_files = sorted(LINKE_DIR.glob("*.html"))
    if not html_files:
        print("No HTML files found under linke/")
        return 0

    missing: dict[Path, list[Ref]] = {}

    for html in html_files:
        parser = _RefParser(html)
        try:
            parser.feed(html.read_text(encoding="utf-8", errors="replace"))
        except Exception as e:
            print(f"WARN: failed to parse {html.relative_to(WORKSPACE)}: {e}")
            continue

        for ref in parser.refs:
            values = [ref.value]
            if ref.tag == "source" and ref.attr == "srcset":
                values = _expand_srcset(ref.value)

            for v in values:
                resolved = _resolve_to_file(ref.html, v)
                if resolved is None:
                    continue

                # Only consider refs that point within linke/ workspace
                try:
                    resolved.relative_to(LINKE_DIR)
                except ValueError:
                    # Points outside linke/; treat as external to this export
                    continue

                if not resolved.exists():
                    missing.setdefault(resolved, []).append(Ref(ref.html, ref.tag, ref.attr, v))

    if not missing:
        print("OK: no missing local asset references found in linke/*.html")
        return 0

    print("Missing local files referenced by HTML:\n")
    for path in sorted(missing.keys()):
        rel = path.relative_to(WORKSPACE)
        print(f"- {rel}")
        for ref in missing[path][:10]:
            print(
                f"  referenced from {ref.html.relative_to(WORKSPACE)} <{ref.tag} {ref.attr}='{ref.value}'>"
            )
        if len(missing[path]) > 10:
            print(f"  ... +{len(missing[path]) - 10} more")
        print()

    print(f"Total missing paths: {len(missing)}")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
