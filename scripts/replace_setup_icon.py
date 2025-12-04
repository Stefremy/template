#!/usr/bin/env python3
import re
from pathlib import Path
import shutil

root = Path('/workspaces/template')
file_path = root / 'linke' / 'solucoes.html'
backup = file_path.with_suffix('.setupicon.bak')
text = file_path.read_text(encoding='utf-8')

# Pattern matches the <i ... class="lnr lnr-chart-bars"></i> including possible whitespace
pattern = re.compile(r"<i\s+aria-hidden=[\"']true[\"']\s+class=[\"']lnr\s+lnr-chart-bars[\"']\s*></i>")

replacement = (
    '<div style="width:56px;height:56px;background:#fff;border-radius:12px;display:flex;align-items:center;justify-content:center;box-shadow:0 6px 18px rgba(0,0,0,0.08);">'
    '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" aria-hidden="true" focusable="false" style="display:block;color:#111">'
    '<path d="M12 15.5A3.5 3.5 0 1 0 12 8.5a3.5 3.5 0 0 0 0 7z" stroke="currentColor" stroke-width="1.2" fill="none" stroke-linejoin="round"/>'
    '<path d="M19.4 15a1 1 0 0 0 .2 1.1l.7.7a1 1 0 0 1 0 1.4l-1.4 1.4a1 1 0 0 1-1.4 0l-.7-.7a1 1 0 0 0-1.1-.2 6.5 6.5 0 0 1-2.8.6 6.5 6.5 0 0 1-2.8-.6 1 1 0 0 0-1.1.2l-.7.7a1 1 0 0 1-1.4 0L3.7 18.2a1 1 0 0 1 0-1.4l.7-.7a1 1 0 0 0 .2-1.1 6.5 6.5 0 0 1-.6-2.8c0-1 .2-2 .6-2.8a1 1 0 0 0-.2-1.1l-.7-.7a1 1 0 0 1 0-1.4L5.3 3.3A1 1 0 0 1 6.7 3.3l.7.7a1 1 0 0 0 1.1.2c.8-.4 1.7-.6 2.8-.6.9 0 1.9.2 2.8.6a1 1 0 0 0 1.1-.2l.7-.7a1 1 0 0 1 1.4 0l1.4 1.4a1 1 0 0 1 0 1.4l-.7.7a1 1 0 0 0-.2 1.1c.4.8.6 1.7.6 2.8 0 .9-.2 1.9-.6 2.8z" stroke="currentColor" stroke-width="0.9" fill="none" stroke-linejoin="round"/>'
    '</svg>'
    '</div>'
)

if not pattern.search(text):
    print('No matching chart-bars icon found; nothing changed.')
else:
    shutil.copy2(file_path, backup)
    new_text = pattern.sub(replacement, text, count=1)
    file_path.write_text(new_text, encoding='utf-8')
    print(f'Replaced chart-bars icon with gear SVG box. Backup: {backup}')
