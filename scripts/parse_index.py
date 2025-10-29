from bs4 import BeautifulSoup
from pathlib import Path
import sys


# Resolve repo root and nordicus/index relative to it
repo_root = Path(__file__).resolve().parents[1]
IN = repo_root / "nordicus" / "index"
if not IN.exists():
    print("File not found:", IN)
    sys.exit(1)

html = IN.read_text(encoding="utf-8", errors="replace")

# Use html5lib for best tolerance of malformed markup
soup = BeautifulSoup(html, "html5lib")

# Write prettified output
OUT = IN.with_name(IN.name + ".formatted.html")
OUT.write_text(soup.prettify(formatter="html"), encoding="utf-8")

# Produce small summary
def text_list(tag):
    return [t.get_text(strip=True) for t in soup.find_all(tag)]

links = [a.get("href") or "" for a in soup.find_all("a")]
images = [img.get("src") or "" for img in soup.find_all("img")]
scripts = [s.get("src") or "" for s in soup.find_all("script") if s.get("src")]
styles = [l.get("href") or "" for l in soup.find_all("link") if l.get("rel") and "stylesheet" in l.get("rel")]

summary = {
    "title": (soup.title.string.strip() if soup.title and soup.title.string else ""),
    "h1": text_list("h1")[:10],
    "h2": text_list("h2")[:10],
    "h3": text_list("h3")[:10],
    "link_count": len(links),
    "image_count": len(images),
    "script_count": len(scripts),
    "stylesheet_count": len(styles),
    "output_file": str(OUT)
}

import json
print(json.dumps(summary, indent=2))
print("Prettified HTML written to:", OUT)