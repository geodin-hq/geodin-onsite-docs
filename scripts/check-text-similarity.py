#!/usr/bin/env python3
"""
check-text-similarity.py — find near-duplicate pages and repeated paragraph
blocks in the GeoDin desktop docs.

Informational tool: emits a markdown audit report; never fails CI.
Stdlib only (Python 3).

Usage:
    python3 scripts/check-text-similarity.py public/en \
        [--page-threshold 0.55] [--block-threshold 0.75] \
        [--min-block-tokens 40] [--top-pairs 50] \
        [--output PATH] [--quiet]

Algorithm:
- Page-level: 5-word shingles + Jaccard, verified with
  difflib.SequenceMatcher.ratio() on top candidates above 0.40.
- Block-level: same shingling on paragraph blocks (>= --min-block-tokens),
  then cluster blocks that share Jaccard >= --block-threshold. Block
  matches whose two pages are already in a page-level pair are dropped
  to avoid noise (otherwise the gINT-style "same paragraph in 4 pages"
  pattern blows up the report).

Normalization (before tokenizing): strip frontmatter, HTML comments
(incl. `<!-- src: -->` markers), GitBook `{% hint %}..{% endhint %}`
blocks, `<figure>` blocks, fenced code, inline code, markdown image
syntax, URLs, HTML entities, table separators, list markers, headings,
markdown emphasis chars; lowercase; collapse whitespace; drop
~25 stopwords; drop tokens < 2 chars.

Pages with fewer than 60 normalized tokens are skipped entirely
(stubs are a separate concern — see check-stubs.sh).

This tool is intentionally NOT wired into CI. Text similarity is not a
binary pass/fail; the report surfaces candidates for human review.
"""

import argparse
import difflib
import re
import sys
from collections import defaultdict
from pathlib import Path

# ---------- normalization config ----------

STOPWORDS = {
    "the", "a", "an", "of", "to", "in", "on", "for", "and", "or",
    "is", "are", "this", "that", "with", "as", "by", "it", "be", "can",
    "will", "you", "we", "if", "then", "but", "not", "at",
}

SHINGLE_SIZE = 5

RE_FRONTMATTER  = re.compile(r"\A---\n.*?\n---\n", re.DOTALL)
RE_HTML_COMMENT = re.compile(r"<!--.*?-->", re.DOTALL)
RE_HINT_BLOCK   = re.compile(r"\{%\s*hint[^%]*%\}.*?\{%\s*endhint\s*%\}", re.DOTALL)
RE_OTHER_TAG    = re.compile(r"\{%[^%]+%\}")
RE_FIGURE       = re.compile(r"<figure[^>]*>.*?</figure>", re.DOTALL)
RE_DIV_FIGURE   = re.compile(r"<div[^>]*>\s*<figure.*?</figure>\s*</div>", re.DOTALL)
RE_CODE_FENCED  = re.compile(r"```.*?```", re.DOTALL)
RE_CODE_INLINE  = re.compile(r"`[^`\n]+`")
RE_MD_IMAGE     = re.compile(r"!\[[^\]]*\]\([^)]*\)")
RE_URL          = re.compile(r"https?://\S+")
RE_HTML_ENTITY  = re.compile(r"&#?\w+;")
RE_TABLE_SEP    = re.compile(r"^\s*\|[\s\-:|]+\|\s*$", re.MULTILINE)
RE_LIST_MARKER  = re.compile(r"^\s*(?:[-*+]|\d+\.|\d+\\\.)\s+", re.MULTILINE)
RE_HEADING      = re.compile(r"^\s*#+\s*", re.MULTILINE)
RE_EMPHASIS     = re.compile(r"[*_`\\]+")
RE_WHITESPACE   = re.compile(r"\s+")


def _strip_structure(text):
    """Strip composite structures while preserving paragraph boundaries."""
    text = RE_FRONTMATTER.sub("", text)
    text = RE_HTML_COMMENT.sub("", text)
    text = RE_HINT_BLOCK.sub("", text)
    text = RE_DIV_FIGURE.sub("", text)
    text = RE_FIGURE.sub("", text)
    text = RE_CODE_FENCED.sub("", text)
    text = RE_MD_IMAGE.sub("", text)
    text = RE_URL.sub("", text)
    text = RE_HTML_ENTITY.sub("", text)
    return text


def _tokenize_snippet(snippet):
    snippet = RE_OTHER_TAG.sub(" ", snippet)
    snippet = RE_CODE_INLINE.sub(" ", snippet)
    snippet = RE_TABLE_SEP.sub(" ", snippet)
    snippet = RE_LIST_MARKER.sub(" ", snippet)
    snippet = RE_HEADING.sub(" ", snippet)
    snippet = RE_EMPHASIS.sub(" ", snippet)
    snippet = snippet.lower()
    snippet = RE_WHITESPACE.sub(" ", snippet).strip()
    return [t for t in snippet.split() if len(t) >= 2 and t not in STOPWORDS]


def normalize(text):
    """Return list of normalized tokens for whole-page comparison."""
    return _tokenize_snippet(_strip_structure(text))


def split_blocks(text):
    """Return list of (raw_block, normalized_tokens) for paragraph-level comparison."""
    stripped = _strip_structure(text)
    out = []
    for raw in re.split(r"\n\s*\n", stripped):
        raw = raw.strip()
        if not raw:
            continue
        tokens = _tokenize_snippet(raw)
        if tokens:
            out.append((raw, tokens))
    return out


def shingle_set(tokens, n=SHINGLE_SIZE):
    if len(tokens) < n:
        return set()
    return {" ".join(tokens[i:i + n]) for i in range(len(tokens) - n + 1)}


def jaccard(a, b):
    if not a or not b:
        return 0.0
    return len(a & b) / len(a | b)


# ---------- main ----------

def main(argv=None):
    p = argparse.ArgumentParser(
        description="Find near-duplicate pages and repeated blocks in markdown docs (informational)."
    )
    p.add_argument("root", help="Root directory to scan (e.g. public/en)")
    p.add_argument("--page-threshold", type=float, default=0.55,
                   help="Page-level Jaccard threshold (default 0.55)")
    p.add_argument("--block-threshold", type=float, default=0.75,
                   help="Block-level Jaccard threshold (default 0.75)")
    p.add_argument("--min-block-tokens", type=int, default=40,
                   help="Minimum normalized tokens for a block to be considered (default 40)")
    p.add_argument("--top-pairs", type=int, default=50,
                   help="Max page pairs to list in the report (default 50)")
    p.add_argument("--output", default=None,
                   help="Markdown report output path (default: stdout)")
    p.add_argument("--quiet", action="store_true",
                   help="Suppress progress messages on stderr")
    args = p.parse_args(argv)

    root = Path(args.root)
    if not root.is_dir():
        print(f"error: not a directory: {root}", file=sys.stderr)
        return 1

    paths = sorted(pth for pth in root.rglob("*.md") if pth.name != "SUMMARY.md")

    files = []
    skipped_stubs = 0
    for path in paths:
        text = path.read_text(encoding="utf-8", errors="replace")
        page_tokens = normalize(text)
        if len(page_tokens) < 60:
            skipped_stubs += 1
            continue
        files.append({
            "rel": str(path.relative_to(root)),
            "tokens": page_tokens,
            "shingles": shingle_set(page_tokens),
            "blocks": split_blocks(text),
        })

    if not args.quiet:
        print(f"scanned {len(files)} pages; skipped {skipped_stubs} stubs (<60 tokens)",
              file=sys.stderr)

    # ----- Pass A: page-level -----
    page_results = []
    for i in range(len(files)):
        for j in range(i + 1, len(files)):
            jac = jaccard(files[i]["shingles"], files[j]["shingles"])
            if jac < args.page_threshold:
                continue
            sm = difflib.SequenceMatcher(None, files[i]["tokens"], files[j]["tokens"],
                                         autojunk=False)
            qr = sm.quick_ratio()
            dif = sm.ratio() if qr >= 0.40 else qr
            page_results.append((jac, dif, files[i]["rel"], files[j]["rel"]))

    page_results.sort(key=lambda x: -x[0])

    if not args.quiet:
        print(f"page-level pairs >= {args.page_threshold}: {len(page_results)}",
              file=sys.stderr)

    flagged_pairs = {frozenset([a, b]) for _, _, a, b in page_results}

    # ----- Pass B: block-level (shingle-index optimization) -----
    block_data = []
    shingle_index = defaultdict(list)
    for fi, f in enumerate(files):
        for raw, tokens in f["blocks"]:
            if len(tokens) < args.min_block_tokens:
                continue
            shingles = shingle_set(tokens)
            if not shingles:
                continue
            idx = len(block_data)
            block_data.append({
                "fi": fi,
                "rel": f["rel"],
                "tokens": tokens,
                "shingles": shingles,
                "raw": raw,
            })
            for s in shingles:
                shingle_index[s].append(idx)

    candidate_pairs = set()
    for indices in shingle_index.values():
        if len(indices) < 2:
            continue
        for i in range(len(indices)):
            for j in range(i + 1, len(indices)):
                a, b = indices[i], indices[j]
                if block_data[a]["fi"] == block_data[b]["fi"]:
                    continue
                pair = (a, b) if a < b else (b, a)
                candidate_pairs.add(pair)

    adj = defaultdict(set)
    for a, b in candidate_pairs:
        jac = jaccard(block_data[a]["shingles"], block_data[b]["shingles"])
        if jac < args.block_threshold:
            continue
        if frozenset([block_data[a]["rel"], block_data[b]["rel"]]) in flagged_pairs:
            continue
        adj[a].add(b)
        adj[b].add(a)

    visited = set()
    clusters = []
    for start in list(adj.keys()):
        if start in visited:
            continue
        cluster = set()
        stack = [start]
        while stack:
            cur = stack.pop()
            if cur in visited:
                continue
            visited.add(cur)
            cluster.add(cur)
            for n in adj.get(cur, ()):
                if n not in visited:
                    stack.append(n)
        if len(cluster) >= 2:
            pages = sorted({block_data[idx]["rel"] for idx in cluster})
            rep_idx = max(cluster, key=lambda x: len(block_data[x]["tokens"]))
            rep = block_data[rep_idx]
            clusters.append({
                "pages": pages,
                "preview": rep["raw"][:200].replace("\n", " "),
                "tokens": len(rep["tokens"]),
            })

    clusters.sort(key=lambda c: (-len(c["pages"]), -c["tokens"]))

    if not args.quiet:
        print(f"block-level clusters (>= 2 pages, after de-noise): {len(clusters)}",
              file=sys.stderr)

    # ----- Render markdown report -----
    lines = []
    lines.append("# Audit — Text-level near-duplicates in geodin-desktop-docs")
    lines.append("")
    lines.append("**Tool:** `scripts/check-text-similarity.py`")
    lines.append(f"**Corpus:** {len(files)} pages under `{root}` ({skipped_stubs} stubs skipped)")
    lines.append(f"**Thresholds:** page Jaccard ≥ {args.page_threshold} | "
                 f"block Jaccard ≥ {args.block_threshold}, ≥ {args.min_block_tokens} tokens")
    lines.append("**Status:** For review. No files changed.")
    lines.append("")

    lines.append(f"## 1. Page-level near-duplicates ({len(page_results)} pairs)")
    lines.append("")
    if not page_results:
        lines.append("_None above threshold._")
    else:
        lines.append("| Jaccard | difflib | Page A | Page B |")
        lines.append("|--:|--:|---|---|")
        for jac, dif, a, b in page_results[:args.top_pairs]:
            lines.append(f"| {jac:.3f} | {dif:.3f} | `{a}` | `{b}` |")
        if len(page_results) > args.top_pairs:
            lines.append("")
            lines.append(f"_(and {len(page_results) - args.top_pairs} more pairs — "
                         "raise `--top-pairs` to list all)_")
    lines.append("")

    lines.append(f"## 2. Cross-page duplicated blocks ({len(clusters)} clusters)")
    lines.append("")
    if not clusters:
        lines.append("_None above threshold (after de-noising against page-level pairs)._")
    else:
        for i, c in enumerate(clusters, 1):
            lines.append(f"### Cluster {i} — {c['tokens']} tokens, {len(c['pages'])} pages")
            for pg in c["pages"][:8]:
                lines.append(f"- `{pg}`")
            if len(c["pages"]) > 8:
                lines.append(f"- _(and {len(c['pages']) - 8} more)_")
            lines.append("")
            lines.append(f"First 120 chars: _{c['preview'][:120]}…_")
            lines.append("")

    report = "\n".join(lines)

    if args.output:
        out_path = Path(args.output).expanduser()
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(report, encoding="utf-8")
        if not args.quiet:
            print(f"report written: {out_path}", file=sys.stderr)
    else:
        print(report)

    return 0


if __name__ == "__main__":
    sys.exit(main())
