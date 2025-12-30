#!/usr/bin/env python3
import os
import re
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BACKUP_DIR = ROOT / 'md_backups'
BACKUP_DIR.mkdir(exist_ok=True)

# heuristics
SENTENCE_SPLIT_RE = re.compile(r'(?<=[.!?])\s+')
HIGHLIGHT_KEYWORDS = ['event', 'meet', 'deadline', 'important', 'note', 'meeting', 'launch', 'release']


def title_from_filename(p: Path):
    name = p.stem
    name = name.replace('_', ' ').replace('-', ' ')
    # capitalize words
    return ' '.join(w.capitalize() for w in name.split())


def split_sentences(text):
    return [s.strip() for s in SENTENCE_SPLIT_RE.split(text) if s.strip()]


def first_paragraph(lines):
    buf = []
    for l in lines:
        if l.strip() == '':
            if buf:
                break
            else:
                continue
        buf.append(l.rstrip())
    return ' '.join(buf).strip()


def ensure_header_and_sections(path: Path, text: str):
    lines = text.splitlines()
    # find first non-empty line
    i = 0
    while i < len(lines) and lines[i].strip() == '':
        i += 1
    if i >= len(lines) or not lines[i].strip().startswith('#'):
        # no header, create one
        title = title_from_filename(path)
        header = f"# {title}\n"
        lines.insert(i, header)
    # find header index (first line starting with #)
    header_idx = 0
    for idx, l in enumerate(lines):
        if l.strip().startswith('# '):
            header_idx = idx
            break
    # after header, find if Summary exists
    rest = '\n'.join(lines[header_idx+1:]).strip()
    new_sections = []
    # ensure Summary
    if re.search(r'^##+\s*Summary', rest, flags=re.I|re.M) is None:
        # take first paragraph as summary
        fp = first_paragraph(lines[header_idx+1:])
        summary_lines = []
        if fp:
            sents = split_sentences(fp)
            if len(sents) == 1:
                summary_lines = [f"- {fp}"]
            else:
                # take up to 4 sentences as bullets
                for s in sents[:4]:
                    summary_lines.append(f"- {s}")
        else:
            summary_lines = ["- "]
        new_sections.append('\n'.join(['## Summary', ''] + summary_lines + ['']))
    # ensure Highlights
    if re.search(r'^##+\s*Highlights', rest, flags=re.I|re.M) is None:
        # try to find sentences with keywords
        text_for_search = rest[:1000]
        sents = split_sentences(text_for_search)
        highlights = []
        for s in sents:
            low = s.lower()
            if any(k in low for k in HIGHLIGHT_KEYWORDS):
                highlights.append(f"- **{s.strip()}**")
            if len(highlights) >= 3:
                break
        if not highlights and sents:
            for s in sents[:2]:
                highlights.append(f"- **{s.strip()}**")
        if not highlights:
            highlights = ['- ']
        new_sections.append('\n'.join(['## Highlights', ''] + highlights + ['']))
    # ensure Tags
    if re.search(r'^Tags\s*:', rest, flags=re.I|re.M) is None:
        new_sections.append('Tags: #journal')
    # append new sections after header + existing leading blanks
    insert_pos = header_idx + 1
    # skip immediate blank lines
    while insert_pos < len(lines) and lines[insert_pos].strip() == '':
        insert_pos += 1
    # insert the sections
    if new_sections:
        lines[insert_pos:insert_pos] = [''] + new_sections

    return '\n'.join(lines).rstrip() + '\n'


def process_file(path: Path, dry_run=False):
    rel = path.relative_to(ROOT)
    # skip README.md at root (we'll create/update separately)
    if rel == Path('README.md'):
        return None
    with path.open('r', encoding='utf-8') as f:
        text = f.read()
    new_text = ensure_header_and_sections(path, text)
    if new_text != text:
        # backup original
        backup_path = BACKUP_DIR / rel
        backup_path.parent.mkdir(parents=True, exist_ok=True)
        with backup_path.open('w', encoding='utf-8') as b:
            b.write(text)
        if not dry_run:
            with path.open('w', encoding='utf-8') as f:
                f.write(new_text)
        return True
    return False


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--apply', action='store_true', help='Write changes')
    args = parser.parse_args()

    md_files = list(ROOT.rglob('*.md'))
    # exclude git dir and backups
    md_files = [p for p in md_files if '.git' not in p.parts and 'md_backups' not in p.parts]

    changed = []
    for p in md_files:
        res = process_file(p, dry_run=not args.apply)
        if res:
            changed.append(p.relative_to(ROOT))

    # generate README
    total = len(md_files)
    readme_lines = []
    readme_lines.append('# Journal — Organized')
    readme_lines.append('')
    readme_lines.append('A curated and readable view of the personal journal entries and study notes. This README was auto-generated during formatting.')
    readme_lines.append('')
    readme_lines.append('## Quick stats')
    readme_lines.append('')
    readme_lines.append(f'- **Total Markdown files:** {total}')
    readme_lines.append(f'- **Files updated in this run:** {len(changed)}')
    readme_lines.append('')
    readme_lines.append('## Organization')
    readme_lines.append('')

    # list top-level folders
    for child in sorted(ROOT.iterdir()):
        if child.is_dir() and child.name != '.git':
            count = sum(1 for _ in child.rglob('*.md'))
            readme_lines.append(f'- **{child.name}/** — {count} markdown files')
    readme_lines.append('')
    readme_lines.append('## Featured highlights')
    readme_lines.append('')

    # collect up to 10 highlights from files
    highlights = []
    for p in md_files:
        try:
            txt = p.read_text(encoding='utf-8')
        except Exception:
            continue
        m = re.search(r'^##+\s*Highlights\n([\s\S]*?)(?:\n## |\Z)', txt, flags=re.I|re.M)
        if m:
            block = m.group(1).strip()
            for line in block.splitlines():
                line = line.strip()
                if line.startswith('-'):
                    highlights.append((p.relative_to(ROOT).as_posix(), line.lstrip('- ').strip()))
        if len(highlights) >= 10:
            break
    if highlights:
        for f, h in highlights[:10]:
            readme_lines.append(f'- **{h}** — [{f}]({f})')
    else:
        readme_lines.append('- No highlights found yet. Run the formatter to extract them.')

    readme_lines.append('')
    readme_lines.append('## Formatting rules applied')
    readme_lines.append('')
    readme_lines.append('- H1 header added if missing')
    readme_lines.append('- `## Summary` and `## Highlights` sections added')
    readme_lines.append('- `Tags: #journal` appended when missing')
    readme_lines.append('- Original files backed up under `md_backups/`')

    readme_text = '\n'.join(readme_lines).rstrip() + '\n'
    readme_path = ROOT / 'README.md'
    # backup README if exists
    if readme_path.exists():
        shutil.copy2(readme_path, BACKUP_DIR / 'README.md.bak')
    if args.apply:
        readme_path.write_text(readme_text, encoding='utf-8')

    print(f"Processed {len(md_files)} markdown files. Changed: {len(changed)}")
    if changed:
        print('Changed files:')
        for c in changed:
            print('-', c)
    else:
        print('No changes were necessary.')
