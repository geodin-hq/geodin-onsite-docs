#!/usr/bin/env bash
#
# check-asset-integrity.sh — detect silent GitBook asset swaps.
#
# Background: GitBook stores every image in a single flat `.gitbook/assets/`
# folder with auto-generated generic names (`image (N).png`, `N_Screen.jpg`).
# A GitBook->git sync can silently re-point an existing filename at DIFFERENT
# image bytes while leaving the page markdown untouched (see commit ce308ef,
# "GITBOOK-86", which swapped 20 screenshots and went unnoticed for ~2 months).
#
# This check pins every committed asset to a sha256 in
# scripts/asset-manifest.sha256 and fails when an EXISTING filename's content
# changes (the swap signature) or a pinned asset disappears. Brand-new uploads
# are allowed and only reported — uploading images is normal; silently
# mutating existing ones is not.
#
# Usage:
#   scripts/check-asset-integrity.sh           # verify against manifest (CI)
#   scripts/check-asset-integrity.sh --update   # regenerate manifest after an
#                                               # intended/reviewed asset change
#
# On a legitimate change (new screenshot for an existing step, GitBook
# re-export, etc.): eyeball the flagged files, then run with --update and
# commit the refreshed manifest in the same PR.
#
set -euo pipefail

ROOT="${ROOT:-public}"
MANIFEST="scripts/asset-manifest.sha256"

# Portable sha256: sha256sum on Linux/CI, shasum -a 256 on macOS.
# Resolved to a real command (not a shell function) so it works under xargs.
if command -v sha256sum >/dev/null 2>&1; then
  HASHER=(sha256sum)
else
  HASHER=(shasum -a 256)
fi

# Emit "<sha256>\t<path>" for every asset, TAB-separated (paths contain
# spaces, e.g. "image (28).png"), sorted by path for stable diffs.
generate() {
  find "$ROOT" -path '*/.gitbook/assets/*' -type f -print0 \
    | xargs -0 "${HASHER[@]}" \
    | sed -E 's/^([0-9a-f]{64}) [ *]/\1\t/' \
    | sort -t"$(printf '\t')" -k2
}

if [[ "${1:-}" == "--update" ]]; then
  generate > "$MANIFEST"
  echo "Updated $MANIFEST ($(wc -l < "$MANIFEST" | tr -d ' ') assets)."
  exit 0
fi

if [[ ! -f "$MANIFEST" ]]; then
  echo "::error::$MANIFEST not found. Generate it with: scripts/check-asset-integrity.sh --update"
  exit 1
fi

CURRENT="$(generate)"

# Compare manifest (committed, known-good) vs current tree, keyed by path.
# CHANGED or MISSING -> fail (the dangerous swap/loss case). NEW -> report only.
echo "$CURRENT" | awk -v manifest="$MANIFEST" '
  BEGIN { FS = "\t" }
  # First pass: the committed manifest (read via getline so stdin stays "current").
  {
    cur[$2] = $1
  }
  END {
    while ((getline line < manifest) > 0) {
      i = index(line, "\t")
      h = substr(line, 1, i - 1)
      p = substr(line, i + 1)
      old[p] = h
    }
    for (p in old) {
      if (!(p in cur))            { print "CHANGED-or-MISSING: pinned asset gone -> " p; bad++ }
      else if (cur[p] != old[p])  { print "CONTENT CHANGED (swap?): " p; bad++ }
    }
    n = 0
    for (p in cur) if (!(p in old)) { print "new (ok): " p; n++ }
    printf("\n%d new asset(s), %d changed/missing.\n", n, bad) > "/dev/stderr"
    if (bad > 0) {
      print "::error::Existing asset content changed or a pinned asset vanished — possible silent GitBook swap. If intentional, review the files above, then run scripts/check-asset-integrity.sh --update and commit the manifest." > "/dev/stderr"
      exit 1
    }
    print "Asset integrity OK." > "/dev/stderr"
  }
'
