# Docs Lint Scripts

Hygiene checks for the docs repo. Run locally before opening a PR; CI runs them on every PR.

## `check-duplication.sh`

Fails if the same `<!-- src: transcript/... -->` attribution appears in more than one `.md` file.

Each transcript section is a single source of truth. Duplicates mean auto-assembled content was copy-pasted into multiple destinations — the bug that produced the original `data-collection/import/` mess.

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

## CI

Both scripts run via `.github/workflows/docs-lint.yml` on every PR. Currently informational; will be promoted to required checks once the existing duplication backlog is cleared.
