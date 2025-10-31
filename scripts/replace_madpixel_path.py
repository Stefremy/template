#!/usr/bin/env python3
import shutil
from pathlib import Path

root = Path('/workspaces/template')
file_path = root / 'nordicus' / 'solucoes.html'
backup = file_path.with_suffix('.madpixel.bak')

old = '/workspaces/template/nordicus/PUBLIC/madpixel-logo.png'
new = 'PUBLIC/madpixel-logo.png'

print(f'Reading {file_path}')
text = file_path.read_text(encoding='utf-8')
if old not in text:
    print('No occurrences found; nothing to do.')
else:
    shutil.copy2(file_path, backup)
    new_text = text.replace(old, new)
    file_path.write_text(new_text, encoding='utf-8')
    print(f'Replaced occurrences of {old} with {new}. Backup at {backup}')
