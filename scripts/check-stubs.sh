#!/usr/bin/env bash
# check-stubs.sh
# Fails if any .md page has fewer than MIN_LINES of non-empty, non-frontmatter,
# non-comment content. Allowlist intentional landing pages in scripts/stub-allowlist.txt.

set -euo pipefail

ROOT="${1:-public}"
MIN_LINES="${MIN_LINES:-10}"
ALLOWLIST_FILE="$(dirname "$0")/stub-allowlist.txt"

stubs=()
while IFS= read -r -d '' f; do
  if [ -f "$ALLOWLIST_FILE" ] && grep -Fxq "$f" "$ALLOWLIST_FILE"; then
    continue
  fi
  lines=$(awk '
    /^---$/ { fm = !fm; next }
    fm { next }
    /^<!--/,/-->/ { next }
    /^[[:space:]]*$/ { next }
    { c++ }
    END { print c+0 }
  ' "$f")
  if [ "$lines" -lt "$MIN_LINES" ]; then
    stubs+=("$f ($lines lines)")
  fi
done < <(find "$ROOT" -name '*.md' -print0)

if [ "${#stubs[@]}" -gt 0 ]; then
  echo "Stub pages found (under $MIN_LINES content lines):"
  printf '  %s\n' "${stubs[@]}"
  echo
  echo "Either fill the page, delete it, or add it to scripts/stub-allowlist.txt."
  exit 1
fi

echo "OK: no stub pages."
