#!/usr/bin/env python3
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
md_files = [p for p in ROOT.rglob('*.md') if '.git' not in p.parts and 'md_backups' not in p.parts]

common_typos = ['teh', 'adn', 'recieve', 'occurence', 'adress', 'enviroment']
report = []
fix_count = 0

for p in md_files:
    text = p.read_text(encoding='utf-8')
    orig = text
    # remove trailing spaces
    new_text = re.sub(r"[ \t]+$", "", text, flags=re.M)
    if new_text != text:
        p.write_text(new_text, encoding='utf-8')
        fix_count += 1
    # find long lines
    long_lines = []
    for i, line in enumerate(new_text.splitlines(), start=1):
        if len(line) > 200:
            long_lines.append((i, len(line), line[:120]))
    # find common typos
    typos_found = []
    low = new_text.lower()
    for t in common_typos:
        if t in low:
            typos_found.append(t)
    if long_lines or typos_found:
        report.append({'file': str(p.relative_to(ROOT)), 'long_lines': long_lines[:5], 'typos': typos_found})

report_path = ROOT / 'md_lint_report.txt'
with report_path.open('w', encoding='utf-8') as f:
    f.write(f'Fixed trailing whitespace in {fix_count} files\n\n')
    for r in report:
        f.write(f"File: {r['file']}\n")
        if r['typos']:
            f.write('  Possible typos: ' + ', '.join(r['typos']) + '\n')
        if r['long_lines']:
            f.write('  Long lines (line, length, excerpt):\n')
            for ln, l, ex in r['long_lines']:
                f.write(f'    - {ln}: {l} chars - "{ex}..."\n')
        f.write('\n')

print('Lint pass complete. Report written to', report_path)
