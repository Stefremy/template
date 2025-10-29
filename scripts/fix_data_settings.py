#!/usr/bin/env python3
"""Normalize broken `data - settings = "..."` attributes.

This script finds attribute patterns like `data - settings = "{...}"` where
the JSON may contain unescaped angle brackets or quotes. It converts them to
`data-settings='...json...'` (single-quoted) and ensures braces are balanced.
It makes a timestamped backup before writing.
"""
from pathlib import Path
from datetime import datetime
import re


# Resolve repo root and nordicus/index relative to it
repo_root = Path(__file__).resolve().parents[1]
IN_PATH = repo_root / "nordicus" / "index"
if not IN_PATH.exists():
    raise SystemExit(f'File not found: {IN_PATH}')

orig = IN_PATH.read_text(encoding='utf-8', errors='replace')
bak = IN_PATH.with_name(IN_PATH.name + '.datasettings.bak.' + datetime.utcnow().strftime('%Y%m%dT%H%M%SZ'))
bak.write_text(orig, encoding='utf-8')
print('Backup written to:', bak)

text = orig

# Find occurrences of data - settings = " starting positions
pattern = re.compile(r'data\s*-\s*settings\s*=\s*"', re.IGNORECASE)
pos = 0
replacements = 0
out = []
last = 0
while True:
    m = pattern.search(text, pos)
    if not m:
        break
    start_attr = m.start()
    # find opening quote index
    quote_idx = m.end() - 1  # position of the double quote
    # find first '{' after the quote
    brace_idx = text.find('{', quote_idx)
    if brace_idx == -1:
        pos = m.end()
        continue
    # scan forward to find matching closing brace
    i = brace_idx
    depth = 0
    end_idx = None
    while i < len(text):
        c = text[i]
        if c == '{':
            depth += 1
        elif c == '}':
            depth -= 1
            if depth == 0:
                end_idx = i
                break
        i += 1
    if end_idx is None:
        # can't balance braces, skip
        pos = m.end()
        continue
    # find closing double-quote after end_idx
    closing_quote = text.find('"', end_idx)
    if closing_quote == -1:
        pos = end_idx + 1
        continue

    json_text = text[brace_idx:end_idx+1]

    # Build replacement: data-settings='json_text'
    # Ensure any single quotes in json_text are escaped (rare)
    safe_json = json_text.replace("'", "&#39;")
    replacement = "data-settings='" + safe_json + "'"

    # Append segment before match
    out.append(text[last:start_attr])
    out.append(replacement)
    last = closing_quote + 1
    pos = last
    replacements += 1

# append remainder
out.append(text[last:])
new_text = ''.join(out)

IN_PATH.write_text(new_text, encoding='utf-8')
print('Rewrote', IN_PATH, 'with', replacements, 'replacements')

# Quick verification: ensure no remaining 'data - settings' patterns
if re.search(r'data\s*-\s*settings\s*=\s*"', new_text, re.IGNORECASE):
    print('Warning: some "data - settings = \"...\"" patterns remain')
else:
    print('All data - settings attributes normalized.')
