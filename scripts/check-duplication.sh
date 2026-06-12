#!/usr/bin/env bash
# check-duplication.sh
# Fails if any `src: <ref>#<section>` attribution comment appears in more than
# one .md file. Each transcript section is a single source of truth — duplicates
# indicate auto-assembled content was placed in multiple destinations.
#
# Top-level transcript citations without a #section anchor (e.g.
# `src: transcript/2026-04-15-in-person-workshop`) are NOT flagged — those are
# legitimate provenance markers and can appear on multiple curated pages.

set -euo pipefail

ROOT="${1:-public}"

# A repo with no src: refs at all is clean — exit before the pipeline, which
# would otherwise abort under pipefail on the empty grep.
files=$(grep -rE 'src: [^ ]+#' "$ROOT" --include='*.md' -l || true)
if [ -z "$files" ]; then
  echo "OK: no src: references present yet."
  exit 0
fi

dupes=$(
  echo "$files" \
    | xargs -I{} sh -c 'grep -oE "src: [^ ]+#[^ ]+" "$1" | sort -u | sed "s|^|$1\t|"' _ {} \
    | awk -F'\t' '{print $2"\t"$1}' \
    | sort \
    | awk -F'\t' '{ key=$1; if (key==prev) { print prev"\t"prev_file; print key"\t"$2; dup=1 } prev=key; prev_file=$2 }' \
    | sort -u
)

if [ -n "$dupes" ]; then
  echo "Duplicate src: references found (each ref must appear in exactly one file):"
  echo
  echo "$dupes" | awk -F'\t' '{print "  "$1"  ->  "$2}'
  echo
  count=$(echo "$dupes" | awk -F'\t' '{print $1}' | sort -u | wc -l | tr -d ' ')
  echo "Total duplicated refs: $count"
  exit 1
fi

echo "OK: no duplicate src: references."
