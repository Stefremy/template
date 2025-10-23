#!/usr/bin/env python3
"""Conservative head merge:

Find a large escaped HTML chunk (lots of &lt;), unescape it, parse it,
merge any head elements (meta, link, script, style, title) into the
document's real <head> (deduplicate charset/viewport/title), remove the
escaped chunk from the body, and write the file. Makes a timestamped
backup before writing.
"""
from pathlib import Path
from datetime import datetime
import html
from bs4 import BeautifulSoup

IN_PATH = Path("/workspaces/template/nordicus/index")
if not IN_PATH.exists():
    raise SystemExit(f"File not found: {IN_PATH}")

orig = IN_PATH.read_text(encoding='utf-8', errors='replace')
bak = IN_PATH.with_name(IN_PATH.name + '.mergehead.bak.' + datetime.utcnow().strftime('%Y%m%dT%H%M%SZ'))
bak.write_text(orig, encoding='utf-8')
print('Backup written to:', bak)

# Heuristic: find the first region with many &lt; occurrences
if orig.count('&lt;') < 10:
    print('No large escaped block detected; aborting.')
    raise SystemExit(0)

# We'll unescape the entire file, parse it, then try to find the
# first 'html' that was inside the escaped content by looking for
# a <head> that contains many typical head tags.
content_unescaped = html.unescape(orig)
doc = BeautifulSoup(content_unescaped, 'html5lib')

main = BeautifulSoup(orig, 'html5lib')

# Find candidate head in unescaped content
cand_head = doc.head
if not cand_head:
    print('No head found in unescaped content; aborting.')
    raise SystemExit(0)

main_head = main.head
if main_head is None:
    main_head = main.new_tag('head')
    main.html.insert(0, main_head)

# Helper: add if missing
def add_if_missing(tag):
    # dedupe by tag type: charset, viewport, title
    if tag.name == 'meta' and tag.get('charset'):
        if not main_head.find('meta', charset=True):
            main_head.insert(0, tag)
        return
    if tag.name == 'meta' and tag.get('name') == 'viewport':
        if not main_head.find('meta', attrs={'name': 'viewport'}):
            main_head.append(tag)
        return
    if tag.name == 'title':
        if not main_head.title or not (main_head.title.string and main_head.title.string.strip()):
            main_head.append(tag)
        return
    # For link/script/style and other metas, avoid exact duplicates by string
    s = str(tag)
    for existing in main_head.find_all(tag.name):
        if str(existing) == s:
            return
    main_head.append(tag)

# Merge elements
for el in cand_head.find_all(['meta','link','script','style','title']):
    add_if_missing(el)

# Now remove the escaped chunk from the body's text nodes: look for the first
# occurrence of the unescaped <head> start string in the original file as escaped
escaped_head_snippet = html.escape(str(cand_head))[:200]
if escaped_head_snippet and escaped_head_snippet in orig:
    new_body = orig.replace(escaped_head_snippet, '')
    # fallback: remove a broader escaped block between &lt; html and &lt; /head &gt;
    import re
    pattern = re.compile(r'&lt;\/?html[\s\S]*?&lt;\/head&gt;?', re.IGNORECASE)
    new_body2 = pattern.sub('', orig, count=1)
    if new_body2 != orig:
        # parse main again and replace body contents with cleaned version
        main = BeautifulSoup(new_body2, 'html5lib')
    else:
        main = BeautifulSoup(orig, 'html5lib')
else:
    # fallback regex remove
    import re
    pattern = re.compile(r'&lt;\/?html[\s\S]*?&lt;\/head&gt;?', re.IGNORECASE)
    new_body2 = pattern.sub('', orig, count=1)
    if new_body2 != orig:
        main = BeautifulSoup(new_body2, 'html5lib')

# Ensure charset and viewport exist (safety)
if not main.head.find('meta', charset=True):
    main.head.insert(0, main.new_tag('meta', charset='utf-8'))
if not main.head.find('meta', attrs={'name':'viewport'}):
    main.head.append(main.new_tag('meta', attrs={'name':'viewport','content':'width=device-width, initial-scale=1'}))
if not main.head.title or not (main.head.title.string and main.head.title.string.strip()):
    t = main.new_tag('title')
    t.string = 'Nordicus Architects — Template'
    main.head.append(t)

# Write back
main_fixed = main.prettify(formatter='html')
IN_PATH.write_text(main_fixed, encoding='utf-8')
print('Merged head and wrote file:', IN_PATH)
print('Backup kept at:', bak)
