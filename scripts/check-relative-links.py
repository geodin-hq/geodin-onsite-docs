#!/usr/bin/env python3
"""Check that relative links and image references in markdown pages resolve.

Catches the move-a-block-break-a-path failure mode: GitBook URLs survive
SUMMARY regrouping (the platform redirects old URLs), but relative *file*
references inside page bodies break silently when content moves between
folder depths — e.g. a section relocated from a two-level-deep page into a
one-level-deep page keeps its `../../.gitbook/...` image path and points
above the content root.

Checks markdown link targets `](...)` and raw `src="..."` attributes whose
target has a known file extension. External URLs, mailto:, absolute paths,
and bare anchors are ignored. GitBook asset names containing parentheses
("image (42).png") are handled.

Exits 1 if any reference is broken, 0 otherwise — safe to wire into CI.

Usage:
    python3 scripts/check-relative-links.py            # defaults to public/
    python3 scripts/check-relative-links.py public/en  # narrow scope
"""
import os
import re
import sys
import urllib.parse

CHECKED_EXTENSIONS = ('.md', '.png', '.jpg', '.jpeg', '.gif', '.svg', '.webp', '.pdf')

# ](target) allowing one level of nested parentheses, since GitBook asset
# filenames look like "image (42) (1).png" — a plain [^)]+ under-matches them.
MD_TARGET = re.compile(r'\]\(\s*<?([^()<>\s][^()<>]*(?:\([^()]*\)[^()<>]*)*)>?\s*\)')
SRC_TARGET = re.compile(r'src="([^"]+)"')


def iter_targets(text):
    for match in MD_TARGET.finditer(text):
        yield match.group(1)
    for match in SRC_TARGET.finditer(text):
        yield match.group(1)


def main():
    root = sys.argv[1] if len(sys.argv) > 1 else 'public'
    if not os.path.isdir(root):
        print(f'error: no such directory: {root}', file=sys.stderr)
        return 2
    broken = []
    pages = 0
    for dirpath, _dirnames, filenames in os.walk(root):
        for name in sorted(filenames):
            if not name.endswith('.md'):
                continue
            pages += 1
            page = os.path.join(dirpath, name)
            with open(page, encoding='utf-8') as fh:
                text = fh.read()
            for raw in iter_targets(text):
                target = urllib.parse.unquote(raw.split('#', 1)[0].strip())
                if not target or target.startswith(('http://', 'https://', 'mailto:', '/')):
                    continue
                if not target.lower().endswith(CHECKED_EXTENSIONS):
                    continue
                resolved = os.path.normpath(os.path.join(dirpath, target))
                if not os.path.exists(resolved):
                    broken.append((page, raw))
    if broken:
        print(f'FAIL: {len(broken)} broken relative reference(s) across {pages} pages:')
        for page, raw in broken:
            print(f'  {page} -> {raw}')
        return 1
    print(f'OK: all relative links and image references resolve ({pages} pages).')
    return 0


if __name__ == '__main__':
    sys.exit(main())
