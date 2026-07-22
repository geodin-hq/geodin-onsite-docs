#!/usr/bin/env bash
# check-typography.sh
# Fails if any .md page contains AI smart-typography characters. House rule
# (2026-07-21): docs prose is ASCII-typography only - em/en dashes -> "-",
# curly quotes -> straight, ellipsis char -> "...", arrows -> ">"/"->",
# middle dots -> "|" or ",", non-breaking/narrow spaces -> regular space.
# Accented characters, the registered-trademark symbol, and callout emoji are
# NOT flagged - only the specific characters below.
#
# Pre-existing violations are grandfathered in scripts/typography-allowlist.txt
# (one path per line, relative to the repo root). Remove entries as pages are
# cleaned up; never add new ones for new content.
#
# Usage:
#   scripts/check-typography.sh            # defaults to public/en (see ROOT)
#   scripts/check-typography.sh public/en  # explicit scope
#
# Uses perl for the Unicode character class (portable: macOS grep lacks -P).

set -euo pipefail

ROOT="${1:-public/en}"
ALLOWLIST_FILE="$(dirname "$0")/typography-allowlist.txt"

# em dash, en dash, curly single/double quotes, ellipsis, right arrow,
# middle dot, no-break space, narrow no-break space
PATTERN='[\x{2014}\x{2013}\x{2018}\x{2019}\x{201C}\x{201D}\x{2026}\x{2192}\x{00B7}\x{00A0}\x{202F}]'

violations=""
allowlisted=0

while IFS= read -r -d '' f; do
  hits=$(perl -CSD -ne 'print "$.: $_" if /'"$PATTERN"'/' "$f" || true)
  [ -z "$hits" ] && continue
  if [ -f "$ALLOWLIST_FILE" ] && grep -Fxq "$f" "$ALLOWLIST_FILE"; then
    allowlisted=$((allowlisted + 1))
    continue
  fi
  violations="${violations}${f}:
$(echo "$hits" | sed 's/^/  /')
"
done < <(find "$ROOT" -name '*.md' -print0)

if [ "$allowlisted" -gt 0 ]; then
  echo "note: $allowlisted allowlisted page(s) still contain smart typography (see typography-allowlist.txt - clean up and remove entries)."
fi

if [ -n "$violations" ]; then
  echo "Smart-typography characters found (docs are ASCII-typography only):"
  echo
  echo "$violations"
  echo "Replace: em/en dash -> '-', curly quotes -> straight, ellipsis -> '...', arrow -> '>' or '->', middot -> '|' or ',', nbsp -> space."
  exit 1
fi

echo "OK: no smart-typography characters outside the allowlist."
