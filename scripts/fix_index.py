#!/usr/bin/env python3
"""Fix and prettify nordicus index HTML.

Backs up the original to the same directory with a timestamped suffix,
parses with html5lib via BeautifulSoup, performs light cleanups, and
writes a prettified replacement.
"""
from bs4 import BeautifulSoup
from pathlib import Path
from datetime import datetime
import sys


# Resolve repo root and nordicus/index relative to it
repo_root = Path(__file__).resolve().parents[1]
IN_PATH = repo_root / "nordicus" / "index"
if not IN_PATH.exists():
    print("File not found:", IN_PATH)
    sys.exit(1)

html = IN_PATH.read_text(encoding="utf-8", errors="replace")

# Backup original
bak = IN_PATH.with_name(IN_PATH.name + ".bak." + datetime.utcnow().strftime('%Y%m%dT%H%M%SZ'))
bak.write_text(html, encoding="utf-8")
print("Backup written to:", bak)

# Parse with html5lib
soup = BeautifulSoup(html, "html5lib")

# Remove empty comments and strange orphan strings
for s in list(soup.find_all(string=True)):
    if isinstance(s, str) and s.strip() == "":
        try:
            s.extract()
        except Exception:
            pass

# Optionally remove duplicate meta/charset declarations if they exist
# (keep first occurrence)
charsets = soup.find_all('meta', attrs={'charset': True})
if len(charsets) > 1:
    for m in charsets[1:]:
        m.extract()

# Write cleaned, prettified HTML (overwrite original)
fixed = soup.prettify(formatter="html")
IN_PATH.write_text(fixed, encoding="utf-8")
print("Fixed file written to:", IN_PATH)

# Print a small summary
links = [a.get('href') or '' for a in soup.find_all('a')]
images = [img.get('src') or '' for img in soup.find_all('img')]
scripts = [s.get('src') or '' for s in soup.find_all('script') if s.get('src')]
styles = [l.get('href') or '' for l in soup.find_all('link') if l.get('rel') and ('stylesheet' in l.get('rel') or 'Stylesheet' in l.get('rel'))]

summary = {
    'title': (soup.title.string.strip() if soup.title and soup.title.string else ''),
    'h1': [t.get_text(strip=True) for t in soup.find_all('h1')][:10],
    'link_count': len(links),
    'image_count': len(images),
    'script_count': len(scripts),
    'stylesheet_count': len(styles),
    'backup': str(bak),
}

import json
print(json.dumps(summary, indent=2))
