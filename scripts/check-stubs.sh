#!/usr/bin/env bash
# check-stubs.sh
# Fails if any .md page has fewer than MIN_LINES of non-empty, non-frontmatter,
# non-comment content.
#
# Two escape hatches, deliberately kept separate:
#
#   scripts/stub-allowlist.txt   Pages that are SUPPOSED to be short - section
#                                landing pages, troubleshooting/contact pages
#                                (both exempt under style rules section 2), and
#                                canonical-home pointers. Exempt silently: there
#                                is nothing to fix.
#
#   scripts/stub-known-gaps.txt  Real gaps that are already tracked in the HITL
#                                register. Reported on every run but do not fail
#                                the build, so a known gap stays visible instead
#                                of disappearing into the allowlist. Every entry
#                                MUST carry its register ID in a trailing comment
#                                - an untracked entry is an error.
#
# Anything else fails. Both files accept `path  # comment` and full-line comments.

set -euo pipefail

ROOT="${1:-public}"
MIN_LINES="${MIN_LINES:-10}"
HERE="$(dirname "$0")"
ALLOWLIST_FILE="$HERE/stub-allowlist.txt"
KNOWN_GAPS_FILE="$HERE/stub-known-gaps.txt"

# Strip inline comments and blank lines, leaving bare paths.
paths_in() {
  [ -f "$1" ] || return 0
  sed -e 's/[[:space:]]*#.*$//' -e 's/[[:space:]]*$//' -e '/^[[:space:]]*$/d' "$1"
}

allowlist="$(paths_in "$ALLOWLIST_FILE")"
known_gaps="$(paths_in "$KNOWN_GAPS_FILE")"

# A known gap without a register ID is how this list rots into a dumping ground.
if [ -f "$KNOWN_GAPS_FILE" ]; then
  untracked=$(grep -vE '^[[:space:]]*(#|$)' "$KNOWN_GAPS_FILE" | grep -v '#' || true)
  if [ -n "$untracked" ]; then
    echo "ERROR: entries in $KNOWN_GAPS_FILE with no register ID:"
    printf '  %s\n' $untracked
    echo
    echo "Every known gap must name the HITL register item tracking it, e.g."
    echo "  public/en/some/page.md  # A3 - Tushita"
    exit 2
  fi
fi

listed() { printf '%s\n' "$2" | grep -Fxq "$1"; }

stubs=()
gaps=()
while IFS= read -r -d '' f; do
  listed "$f" "$allowlist" && continue
  lines=$(awk '
    /^---$/ { fm = !fm; next }
    fm { next }
    /^<!--/,/-->/ { next }
    /^[[:space:]]*$/ { next }
    { c++ }
    END { print c+0 }
  ' "$f")
  if [ "$lines" -lt "$MIN_LINES" ]; then
    if listed "$f" "$known_gaps"; then
      gaps+=("$f ($lines lines)")
    else
      stubs+=("$f ($lines lines)")
    fi
  fi
done < <(find "$ROOT" -name '*.md' -print0)

if [ "${#gaps[@]}" -gt 0 ]; then
  echo "Known content gaps (tracked in the HITL register, not failing this build):"
  printf '  %s\n' "${gaps[@]}"
  echo
fi

if [ "${#stubs[@]}" -gt 0 ]; then
  echo "Stub pages found (under $MIN_LINES content lines):"
  printf '  %s\n' "${stubs[@]}"
  echo
  echo "Fill the page, delete it, or - if it is short by design - add it to"
  echo "scripts/stub-allowlist.txt. If it is a real gap that a human has to close,"
  echo "open a HITL register item and add it to scripts/stub-known-gaps.txt with"
  echo "that item's ID."
  exit 1
fi

echo "OK: no untracked stub pages."
