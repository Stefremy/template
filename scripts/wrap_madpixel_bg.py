#!/usr/bin/env python3
import re
from pathlib import Path
import shutil

root = Path('/workspaces/template')
file_path = root / 'nordicus' / 'solucoes.html'
backup = file_path.with_suffix('.madpixel.bg.bak')

text = file_path.read_text(encoding='utf-8')
pattern = re.compile(r'(<img[^>]*src="PUBLIC/madpixel-logo.png"[^>]*?/?>)')

m = pattern.search(text)
if not m:
    print('No matching img tag found; nothing changed.')
else:
    shutil.copy2(file_path, backup)
    img_tag = m.group(1)
    wrapper = ('<div style="background:#333;color:#fff;padding:10px;display:inline-block;border-radius:6px;">'
               + img_tag + '</div>')
    new_text = text[:m.start(1)] + wrapper + text[m.end(1):]
    file_path.write_text(new_text, encoding='utf-8')
    print(f'Wrapped first occurrence of madpixel logo with dark bg. Backup at {backup}')
