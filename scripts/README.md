# Docs Lint Scripts

Hygiene checks for the docs repo. Run locally before opening a PR; CI runs them on every PR.

## `check-duplication.sh`

Fails if the same `<!-- src: transcript/... -->` attribution appears in more than one `.md` file.

Each transcript section is a single source of truth. Duplicates mean auto-assembled content was copy-pasted into multiple destinations - the bug that produced the original `data-collection/import/` mess.

```bash
./scripts/check-duplication.sh           # defaults to public/
./scripts/check-duplication.sh public/en # narrow scope
```

## `check-stubs.sh`

Fails if any `.md` page has fewer than 10 lines of real content (frontmatter, blank lines, and HTML comments excluded). Intentional landing pages can be allowlisted in `stub-allowlist.txt`.

```bash
./scripts/check-stubs.sh
MIN_LINES=20 ./scripts/check-stubs.sh   # raise the bar
```

## `check-asset-integrity.sh`

Fails if an existing `.gitbook/assets/` image's **content** changes, or a pinned asset disappears - the silent-swap failure mode. GitBook keeps every image in one flat folder with generic names (`image (N).png`, `N_Screen.jpg`); a GitBook→git sync can re-point an existing filename at different bytes while leaving the page markdown untouched (commit `ce308ef` / "GITBOOK-86" did exactly this to 20 screenshots, unnoticed for ~2 months). Every asset is pinned by sha256 in `asset-manifest.sha256`. New uploads are allowed and only reported; mutating an existing file is what fails.

```bash
./scripts/check-asset-integrity.sh           # verify against the manifest (CI)
./scripts/check-asset-integrity.sh --update   # regenerate after an intended change
ROOT=public/en ./scripts/check-asset-integrity.sh   # narrow scope
```

On a legitimate change (new screenshot for a step, GitBook re-export): review the flagged files, then run `--update` and commit the refreshed `asset-manifest.sha256` in the same PR. Because GitBook syncs *into* this repo, the `push: main` trigger (no path filter) is what surfaces a sync-introduced swap - it can't block an already-pushed commit, but it turns a months-long silent corruption into a red check within minutes.

## `check-text-similarity.py`

Informational audit: finds **near-duplicate pages** and **repeated paragraph blocks** that don't share a `<!-- src: -->` marker (so the marker-based linter can't catch them). 5-word word-shingles + Jaccard, page-level AND block-level, with `difflib.SequenceMatcher.ratio()` as a secondary verify on top candidates. Stdlib only.

Writes a markdown report - defaults to stdout, point `--output` at a path to capture it (the convention is `~/GitHub/geodin-docs-internal/insights/AUDIT-text-similarity.md`, alongside the existing `AUDIT-import-duplication.md`).

```bash
python3 scripts/check-text-similarity.py public/en
python3 scripts/check-text-similarity.py public/en --output ~/GitHub/geodin-docs-internal/insights/AUDIT-text-similarity.md
python3 scripts/check-text-similarity.py public/en --page-threshold 0.70 --block-threshold 0.85 --quiet
```

Defaults: page Jaccard ≥ 0.55, block Jaccard ≥ 0.75 with ≥ 40 normalized tokens. Skips pages with fewer than 60 normalized tokens (those are stubs - `check-stubs.sh`'s job).

**Not wired into CI** - text similarity isn't a binary defect; a 0.62 page-level score isn't *wrong*, it's a candidate for human review. Run on-demand when you suspect duplication has crept in, or after a bulk content addition.

## `check-relative-links.py`

Fails if a relative link or image reference in any `.md` page points at a file that doesn't exist. This is the move-a-block-break-a-path failure mode: GitBook redirects page *URLs* when SUMMARY regroups, but relative *file* references inside page bodies break silently when content moves between folder depths - a section relocated from a two-level-deep page keeps its `../../.gitbook/...` prefix and points above the content root. Handles GitBook asset names containing parentheses (`image (42).png`), which naive `[^)]+` link regexes silently skip.

```bash
python3 scripts/check-relative-links.py            # defaults to public/
python3 scripts/check-relative-links.py public/en  # narrow scope
```

Checks markdown `](...)` targets and raw `src="..."` attributes with a known file extension; external URLs, mailto:, absolute paths, and bare anchors are ignored. Exits 1 on any broken reference - CI-ready as a required check, not wired in yet.

## CI

`check-asset-integrity.sh`, `check-duplication.sh`, and `check-stubs.sh` run via `.github/workflows/docs-lint.yml`. `check-asset-integrity.sh` and `check-duplication.sh` are required; `check-stubs.sh` is informational. The asset check also runs on every push to `main` (no path filter) so GitBook sync commits are caught. `check-text-similarity.py` is not in CI - it's a local audit tool.

## `check-typography.sh`

Fails if any `.md` page contains AI smart-typography characters (em/en dashes, curly quotes, ellipsis char, arrows, middle dots, non-breaking spaces). House rule (2026-07-21): docs prose is ASCII-typography only - see `CLAUDE.md` section 1 for the replacement map. Pre-existing violations are grandfathered in `typography-allowlist.txt`; clean pages up and remove their entries - never allowlist new content.

```bash
./scripts/check-typography.sh public/en
```

## `check-structure.py`

Mechanizable house-structure checks: every SUMMARY.md entry resolves, every page is referenced in SUMMARY.md (no orphans), nesting stays within two subpage levels, every `<figure>` has a non-empty `<figcaption>`, one H1 per page, no skipped heading levels. See `CLAUDE.md` sections 2-6 for the rules these enforce. Informational in CI until the pre-existing findings are triaged.

```bash
python3 scripts/check-structure.py public/en
```
