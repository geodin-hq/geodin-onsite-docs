#!/usr/bin/env python3
"""check-structure.py - mechanizable checks for the GeoDin docs house structure.

Checks (per content root, default public/en):
  1. Every SUMMARY.md entry resolves to an existing file.
  2. Every .md page under the root is referenced in SUMMARY.md (no orphans).
  3. SUMMARY nesting depth: at most two levels of subpages (GitBook guidance;
     see the repo CLAUDE.md, section "Index and SUMMARY.md structure").
  4. Every <figure> block contains a <figcaption> (caption rule: what the
     image shows and what to notice in it).
  5. Heading hygiene per page: at most one H1, no skipped heading levels.

Informational in CI at first (continue-on-error) - promote to required once
pre-existing findings are triaged.

Usage:
    python3 scripts/check-structure.py            # defaults to public/en
    python3 scripts/check-structure.py public
"""
import os
import re
import sys

SUMMARY_ENTRY = re.compile(r'^(\s*)\*\s+\[[^\]]*\]\(([^)]+)\)')
HEADING = re.compile(r'^(#{1,6})\s')
FIGURE = re.compile(r'<figure\b.*?</figure>', re.DOTALL)
MAX_SUBPAGE_DEPTH = 2  # levels of indentation under a top-level page


def main():
    root = sys.argv[1] if len(sys.argv) > 1 else 'public/en'
    summary_path = os.path.join(root, 'SUMMARY.md')
    if not os.path.isfile(summary_path):
        print(f'error: {summary_path} not found', file=sys.stderr)
        return 2

    problems = []

    # --- SUMMARY checks ---
    referenced = set()
    with open(summary_path, encoding='utf-8') as fh:
        for lineno, line in enumerate(fh, 1):
            m = SUMMARY_ENTRY.match(line)
            if not m:
                continue
            indent, target = m.groups()
            depth = len(indent) // 2
            target = target.split('#', 1)[0].strip()
            if not target or target.startswith(('http://', 'https://')):
                continue
            path = os.path.normpath(os.path.join(root, target))
            if not os.path.isfile(path):
                problems.append(f'SUMMARY.md:{lineno}: entry does not resolve: {target}')
            if path in referenced:
                problems.append(f'SUMMARY.md:{lineno}: page listed twice: {target}')
            referenced.add(path)
            if depth > MAX_SUBPAGE_DEPTH:
                problems.append(
                    f'SUMMARY.md:{lineno}: nesting deeper than {MAX_SUBPAGE_DEPTH} '
                    f'subpage levels: {target}')

    # --- orphan pages ---
    for dirpath, _dirs, files in os.walk(root):
        for name in sorted(files):
            if not name.endswith('.md') or name == 'SUMMARY.md':
                continue
            path = os.path.normpath(os.path.join(dirpath, name))
            if path not in referenced:
                problems.append(f'{path}: not referenced in SUMMARY.md (orphan)')

    # --- per-page checks ---
    for dirpath, _dirs, files in os.walk(root):
        for name in sorted(files):
            if not name.endswith('.md') or name == 'SUMMARY.md':
                continue
            path = os.path.join(dirpath, name)
            with open(path, encoding='utf-8') as fh:
                text = fh.read()

            for i, fig in enumerate(FIGURE.findall(text), 1):
                if '<figcaption' not in fig or re.search(
                        r'<figcaption>\s*</figcaption>', fig):
                    problems.append(
                        f'{path}: figure #{i} missing a non-empty <figcaption>')

            h1_count = 0
            prev_level = 0
            in_fence = False
            for lineno, line in enumerate(text.splitlines(), 1):
                if line.lstrip().startswith('```'):
                    in_fence = not in_fence
                    continue
                if in_fence:
                    continue
                m = HEADING.match(line)
                if not m:
                    continue
                level = len(m.group(1))
                if level == 1:
                    h1_count += 1
                    if h1_count > 1:
                        problems.append(f'{path}:{lineno}: more than one H1')
                if prev_level and level > prev_level + 1:
                    problems.append(
                        f'{path}:{lineno}: heading level skips from '
                        f'H{prev_level} to H{level}')
                prev_level = level

    if problems:
        print(f'{len(problems)} structure finding(s) under {root}:')
        for p in problems:
            print(f'  {p}')
        return 1
    print(f'OK: structure checks passed under {root}.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
