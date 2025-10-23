#!/usr/bin/env python3
"""Repair the nordicus index by unescaping HTML entities that were double-escaped,
ensuring a valid <head> with charset/title/viewport, and writing a clean HTML file.
Backs up the current file before changing.

This script is conservative: it tries to preserve the original content, only
fixing surrounding broken markup (unescaped tags, missing head content).
"""
from pathlib import Path
from datetime import datetime
import html
import re
from bs4 import BeautifulSoup

IN_PATH = Path("/workspaces/template/nordicus/index")
if not IN_PATH.exists():
    raise SystemExit(f"File not found: {IN_PATH}")

orig = IN_PATH.read_text(encoding="utf-8", errors="replace")
# Backup
bak = IN_PATH.with_name(IN_PATH.name + ".repair.bak." + datetime.utcnow().strftime('%Y%m%dT%H%M%SZ'))
bak.write_text(orig, encoding="utf-8")
print("Backup written to:", bak)

# The file appears to contain lots of escaped angle brackets like "&lt;" and "&gt;"
# Some parts are real HTML already; to avoid double-unescaping normal parts,
# we'll try to detect large blocks that are escaped and unescape them.

content = orig
# Heuristic: unescape sequences where we see '&lt;' followed soon by '&gt;'
# and where there are many &lt; occurrences.
if content.count('&lt;') > 20:
    content = html.unescape(content)

# Now parse with html5lib to get a DOM
soup = BeautifulSoup(content, 'html5lib')

# Ensure proper head: add charset and viewport and a sensible title if missing
head = soup.head
if not head:
    head = soup.new_tag('head')
    soup.html.insert(0, head)

# charset
if not head.find('meta', charset=True):
    meta = soup.new_tag('meta', charset='utf-8')
    head.insert(0, meta)

# viewport
if not head.find('meta', attrs={'name': 'viewport'}):
    mv = soup.new_tag('meta', attrs={'name': 'viewport', 'content': 'width=device-width, initial-scale=1'})
    head.append(mv)

# title
if not head.title or not (head.title.string and head.title.string.strip()):
    t = soup.new_tag('title')
    t.string = 'Nordicus Architects — Template'
    head.append(t)

# Remove stray text outside html/body tags (like leftover backticks)
# Move any top-level text nodes into body
if soup.body is None:
    body = soup.new_tag('body')
    soup.html.append(body)
else:
    body = soup.body

for top in list(soup.contents):
    if getattr(top, 'name', None) is None and str(top).strip():
        # move into body
        body.insert(0, top.extract())

# Pretty output
fixed = soup.prettify(formatter='html')
IN_PATH.write_text(fixed, encoding='utf-8')
print('Fixed file written to:', IN_PATH)

# Print short summary
links = [a.get('href') or '' for a in soup.find_all('a')]
print('links:', len(links))
print('images:', len(soup.find_all('img')))
print('scripts:', len([s for s in soup.find_all('script') if s.get('src')]))
print('stylesheets:', len([l for l in soup.find_all('link') if l.get('rel') and 'stylesheet' in l.get('rel')]))
