# GeoDin Onsite Docs — Project Summary

**Branch:** `feature/onsite-docs-augmentation`
**Started:** 2026-04-23
**Authors:** Nuno + Claude
**Status:** Plan approved — content drafting in progress

This document is the living plan for the refreshed GeoDin Onsite docs. It records (1) the current state of the `main` branch, (2) the target structure, (3) a diff matrix classifying every page, (4) a coverage map tying each page to its source material, and (5) the execution plan.

It lives at the repo root (outside `public/en/`) so it is **not** synced to GitBook. It stays in the branch as a reference for reviewers, and survives merge as ongoing project documentation — matching the `PROJECT-SUMMARY.md` pattern already used in `geodin-desktop-docs`.

---

## 1. Current state (on `main`)

10 markdown files, ~2,400 words total. Single live source serving docs.geodin.com for Onsite.

| # | Path | Words | Purpose today |
|---|---|---|---|
| 1 | `README.md` (Introduction) | 189 | Product pitch, 4 key features, external embed |
| 2 | `SUMMARY.md` | 34 | Table of contents (3 sections: Documentation / Guides / Support) |
| 3 | `documentation/getting-started.md` | 246 | Install, activate, offline licensing |
| 4 | `documentation/updates-and-version-compatibility.md` | 172 | Auto-update, backward compat |
| 5 | `guides/the-first-steps.md` | 662 | G1 Drilling Report tutorial (filename misleading) |
| 6 | `guides/soil-sampling.md` | 321 | Soil sampling + QR codes + printer setup (mixed) |
| 7 | `guides/configuration.md` | 580 | Standards, Defaults, Backups (everything dumped into one page) |
| 8 | `support/changelog.md` | 17 | Hidden placeholder ("Work in Progress") |
| 9 | `support/get-support.md` | 126 | Support portal + email |
| 10 | `.gitbook/includes/untitled.md` | 9 | Stray asset, not referenced from SUMMARY |

**Strengths of current docs:** concise, task-oriented, covers the happy path for G1 reports.

**Gaps identified:**
- No explanation of the **mental model** (forms as single-owner files, publish/retrieve, ownership transfer)
- No coverage of the **file system** (where data lives, how projects map to folders)
- No **forms inventory** beyond G1 and Soil Sampling
- Single "Configuration" page mashes six distinct topic areas
- Label printing, camera, GPS configuration not documented
- No publishing/collaboration workflow documentation
- Photography / Sample Picture Log not documented
- Filename bug: `the-first-steps.md` contains G1 content
- `.gitbook/includes/untitled.md` is dead weight

---

## 2. Guiding principles

These shape every decision in Section 3 below.

1. **GitBook-consistent structure.** Match the SUMMARY.md patterns already used on `geodin-desktop-docs` (`##` for groups, clean hierarchy), so users moving between docs sites feel continuity.
2. **Distinguish mechanics from forms.** The trainer's explicit ask: separate "how Onsite works" (framework) from "how to fill out this specific form" (domain). This drives the split between *Core Concepts* and *Guides*.
3. **Mirror the app's UI where it aids navigation.** Configuration sub-pages match the tabs a user actually sees in the app's Configuration menu (Project / Integration / Defaults / Backups / Labels / Camera / GPS). Searchability ↑.
4. **Accuracy over completeness.** If a topic can't be verified from the main docs or the two training transcripts, it does NOT get a page. Uncertain items are tracked in a separate internal notes file at the end of the project (see Section 6).
5. **No versioning claims.** Docs describe "current Onsite behavior," never "as of v1.2."
6. **No internal-only content.** Keygen/Shopify/hardware-fingerprinting internals stay out of public docs. Licensing coverage is intentionally thin and user-facing only.
7. **No legacy references.** "Gaia Forms" = GeoDin Onsite (just a prior internal name). Public docs make no mention of the legacy brand or Fugro-specific lineage.

---

## 3. Proposed structure

### 3.1 SUMMARY.md (proposed)

Deliberately **not** mirroring the desktop-docs shape (which has a loose `Introduction` outside any group plus a redundant "Getting Started > Getting Started" entry). The pattern below is the modern-documentation-portal convention: `README.md` doubles as the landing page and the first sidebar item of Getting Started. Intent is that this shape gets applied back to desktop-docs for consistency.

```
# Table of contents

## Getting Started

* [Introduction](README.md)
* [Installation & licensing](documentation/installation-and-licensing.md)
* [The Onsite user interface](documentation/onsite-user-interface.md)
* [First steps](documentation/first-steps.md)

## Core Concepts

* [Forms & projects](core-concepts/forms-and-projects.md)
* [Folder structure](core-concepts/folder-structure.md)
* [File delivery & ownership](core-concepts/file-delivery-and-ownership.md)

## Guides

* [G1 drilling report](guides/g1-drilling-report.md)
* [Soil sampling](guides/soil-sampling.md)
* [Sample picture log](guides/sample-picture-log.md)
* [Publishing & retrieving forms](guides/publishing-and-retrieving.md)
* [Exporting to GeoDin](guides/exporting-to-geodin.md)
* [Managing labels](guides/managing-labels.md)

## Configuration

* [Project setup](configuration/project-setup.md)
* [Geo-data standards](configuration/geo-data-standards.md)
* [File delivery setup](configuration/file-delivery-setup.md)
* [Form defaults](configuration/form-defaults.md)
* [Backups](configuration/backups.md)
* [Label printing](configuration/label-printing.md)
* [Camera](configuration/camera.md)
* [GPS & coordinates](configuration/gps-and-coordinates.md)

## Support

* [Troubleshooting](support/troubleshooting.md)
* [Updates & version compatibility](support/updates-and-version-compatibility.md)
* [Get support](support/get-support.md)
* [Changelog](support/changelog.md)
```

### 3.2 Section-by-section rationale

**Getting Started** (4 pages) — Canonical new-user onboarding shape. The `README.md` file serves double duty: it's the landing page when someone arrives at docs.geodin.com/onsite *and* the first sidebar item inside Getting Started. No loose "Introduction" outside the group, no redundant "Getting Started > Getting Started" entry.

1. **Introduction** (README.md) — product overview, key features, link to marketing page
2. **Installation & licensing** — install, .NET 8 prerequisite, licence activation, offline grace
3. **The Onsite user interface** — orientation tour: menu actions, Configuration tabs, Tools menu, question-mark menu, on-screen keyboard
4. **First steps** — 5-step happy-path walkthrough to create your first G1 form end-to-end. Links out to the G1 drilling report guide for deeper coverage.

**Core Concepts** (3 pages) — The mental model. Read once, applies everywhere. Separated from Guides because reading concepts before acting is a different user intent than following a tutorial. This is where the paper/shelf/letterbox analogy lives.

**Guides** (6 pages) — Task-oriented "how do I do X" content. Each guide points back to relevant Core Concepts when the underlying model matters.

**Configuration** (8 pages) — One page per Configuration tab in the app UI. A user looking for "how do I set up my printer" finds the Label Printing page; they don't have to scroll through a mega-page.

**Support** (4 pages) — Troubleshooting + Updates & version compatibility (moved here from the top, matching desktop's placement of update-related content near the bottom) + existing Get Support + hidden Changelog.

---

## 4. Diff matrix

Per-page classification. Three outcomes:
- **Keep** — port from main with minimal edits (fix links, ensure conventions)
- **Amend** — port + significant expansion with transcript content
- **New** — entirely new page authored from transcript + main context

### 4.1 Kept pages (4)

| Proposed page | Current source | Changes |
|---|---|---|
| `README.md` (Introduction) | `README.md` | Minor: ensure "Key features" list still reflects what we document in detail. Keep the `{% embed %}` to marketing page. |
| `support/updates-and-version-compatibility.md` | `documentation/updates-and-version-compatibility.md` | **File moves** from `documentation/` to `support/`. Content: minor — ensure wording matches current subscription model (remove any trial-era framing). |
| `support/get-support.md` | same | Minor: no changes expected. |
| `support/changelog.md` | same | Keep hidden placeholder as-is. |

**Deleted:**
- `.gitbook/includes/untitled.md` — dead stray file, not referenced from SUMMARY.
- `guides/configuration.md` — content redistributed across the new `configuration/` pages (Geo-data standards, Form defaults, Backups).

### 4.2 Amended pages (3)

| Proposed page | Current source | What changes |
|---|---|---|
| `documentation/installation-and-licensing.md` | `documentation/getting-started.md` | **Rename file + expand.** Add: install modes (local vs all-users), .NET 8 prerequisite, working folder location (`%APPDATA%\GeoDin.Onsite\`), licence activation flow. Reflect annual subscription model + 6-month free trial (strip any trial-era language). Minimal licensing coverage: purchase via website, activate with key, validation on launch, 30-day offline grace, contact support for hardware changes. |
| `guides/g1-drilling-report.md` | `guides/the-first-steps.md` | **Rename file + expand.** Add: show/hide pages customization, page reordering, form bundle concept (G1 + SPL), explicit pointer to Sample Picture Log guide for bundles. Existing structure (Configure → Project setup → Create → Validate → Export) is solid. |
| `guides/soil-sampling.md` | same | **Amend + trim.** Keep soil logging content. Remove QR/printer-config content (moves to `configuration/label-printing.md` and `guides/managing-labels.md`). Add pointer to label printing config. |

### 4.3 New pages (18)

**Getting Started (2 new)**

| Page | Source material | Content summary |
|---|---|---|
| `documentation/onsite-user-interface.md` | Transcripts + main | Orientation tour of the UI: main menu actions (New Form, Load Local, Retrieve, Tools, Configuration, Export, Publish), the Configuration tabs at a glance, the question-mark icon menu (About, Licensing, Open Log Files, Contact Support, Online Help), on-screen keyboard toggle for tablets. Pure "where things live" page — no deep how-to. |
| `documentation/first-steps.md` | Training transcript | 5-step happy-path walkthrough: (1) confirm project number, (2) New Form → G1 Drilling Report, (3) fill minimum required fields (location, one layer, drilling method), (4) validate, (5) Export → GeoDin → `.geodinml`. Closes with pointer to the full G1 guide. Short (~400–500 words), heavy on screenshots. |

**Core Concepts (3 new)**

| Page | Source material | Content summary |
|---|---|---|
| `core-concepts/forms-and-projects.md` | Transcripts | What is a form (GDOF/GDOB), what is a project, how forms are saved automatically, naming convention (`Location_FormCode_Date`), file format (XML internally), form bundles, page customization inside a form. Introduces terminology used everywhere else. |
| `core-concepts/folder-structure.md` | Transcripts | Working folder location, how to find it (address bar trick, in-app "Open local folder" button), subfolders (`projects/`, `logs/`, `installers/`, `backups/`), loose files (`config.xml`, `logo.png`, custom ZPL), read-only defaults in installation folder. |
| `core-concepts/file-delivery-and-ownership.md` | Transcripts | The paper / shelf / letterbox analogy. File delivery modes. Ownership: one form, one owner at a time. Publish statuses (complete vs incomplete). Retrieve. Revoke (with explicit warning). Local photocopy for disaster recovery. Save vs publish semantics. |

**Guides (4 new)**

| Page | Source material | Content summary |
|---|---|---|
| `guides/sample-picture-log.md` | Transcripts | Standalone SPL form (scan QR to tie photo to sample). Bundled G1+SPL (pick sample from dropdown). Taking/cropping/rotating/annotating photos. Picture file naming convention. |
| `guides/publishing-and-retrieving.md` | Transcripts | Step-by-step: publish incomplete, publish complete, retrieve, revoke. Cross-links to Core Concepts for the "why." Practical how-to. |
| `guides/exporting-to-geodin.md` | Transcripts + main | Export → GeoDin (produces GeoDinML). Which forms produce GeoDinML (G1 + SEP3). Other outputs (PDF, JPEGs for picture logs). Pointer to GeoDin Desktop docs for import. Draft watermark rule. |
| `guides/managing-labels.md` | Transcripts | Tools menu: print individual sample labels, duplicate labels, crate labels, shelf labels. Pairs with `configuration/label-printing.md` for setup. |

**Configuration (8 new)**

All new because the current `guides/configuration.md` is a single mega-page covering only 3 of the 8 topics below.

| Page | Source material | Content summary |
|---|---|---|
| `configuration/project-setup.md` | Transcripts | Project tab: manual mode vs GeoDinML-driven mode. Project number rules (letters, numbers, `-`, `_`) and rationale. Warnings about reusing project numbers. |
| `configuration/geo-data-standards.md` | Main + transcripts | Integration tab → Geo-data delivery. 5 standards. Standards lock once project is active. Tab can lock if forms are open. |
| `configuration/file-delivery-setup.md` | Transcripts | Integration tab → File delivery system. No-delivery (default) vs shared folder. Selecting the folder. Sync is the user's responsibility (OneDrive / Dropbox / X-drive etc.). Embedded picture options. Cross-link to Core Concepts. |
| `configuration/form-defaults.md` | Main | Defaults tab: foreman/leader/logger, assistants, rig/pit method, vehicle/vessel, unit system, local coordinate system. |
| `configuration/backups.md` | Main + transcripts | Backups tab: enable timed backups, interval, folder, versions to keep. Restore via Tools → Restore. No manual save needed. |
| `configuration/label-printing.md` | Transcripts | Labels tab: printer selection (main + alternative), preview mode, ZPL overview, Zebra recommendation + compatible alternatives, label template customization (copying default ZPL, editing fields), logo customization (`logo.png`), relabeling the printer/layout toggle buttons. |
| `configuration/camera.md` | Transcripts | Camera tab: built-in camera config (device / resolution / rotation). External DSLR via command-line interface capture. Default picture path. |
| `configuration/gps-and-coordinates.md` | Transcripts | GPS tab: four sources (built-in chip / Windows-based / external Bluetooth / manual entry). EPSG / local coordinate system selection. |

**Support (1 new)**

| Page | Source material | Content summary |
|---|---|---|
| `support/troubleshooting.md` | Transcripts | Finding log files (question-mark menu → Open log files). Common issues with suggested checks. When to contact support. Hardware changes and license re-binding (user-facing framing only). |

### 4.4 Summary counts

| Category | Count |
|---|---|
| Kept (minimal changes, incl. one file move) | 4 |
| Amended (major expansion, incl. one file rename) | 3 |
| New | 18 |
| Deleted | 2 |
| **Total pages after** | **25** (vs 10 current) |

Word-count projection: ~15,500–17,500 words (vs 2,356 current). Each new page averages 500–900 words; no single page expected to exceed 1,500 words. The First Steps page is intentionally shorter (~400–500 words).

---

## 5. Coverage map — sources feeding each page

How we stay honest that every claim in the docs is traceable.

| Page | Primary source | Secondary source |
|---|---|---|
| Introduction | main README | transcripts (key features list) |
| Installation & licensing | main + training transcript | pricing file (subscription model) |
| The Onsite user interface | both transcripts | main (existing menu references) |
| First steps | training transcript | main (existing G1 walkthrough) |
| Updates & compatibility | main | training transcript |
| Forms & projects | tech demo transcript | training transcript |
| Folder structure | tech demo transcript | — |
| File delivery & ownership | both transcripts | — |
| G1 drilling report | main | training transcript (show/hide, bundles) |
| Soil sampling | main | — |
| Sample picture log | tech demo transcript | training transcript |
| Publishing & retrieving | both transcripts | — |
| Exporting to GeoDin | main + both transcripts | — |
| Managing labels | training transcript | tech demo transcript |
| Project setup | tech demo transcript | training transcript |
| Geo-data standards | main | — |
| File delivery setup | both transcripts | — |
| Form defaults | main | — |
| Backups | main | both transcripts |
| Label printing | tech demo transcript | training transcript |
| Camera | tech demo transcript | training transcript |
| GPS & coordinates | training transcript | — |
| Troubleshooting | both transcripts | — |
| Get support | main | — |

---

## 6. Out of scope / unresolved

To be tracked separately (as a README note at the end of the project) and NOT published in the current docs:

- **Partial publish status** (trainer explicitly skipped explanation)
- **Full 10-form inventory** — only 5 forms confirmed from transcripts (G1 Drilling, SEP3, Picture Log, Sample Picture Log, G1+SPL bundle). Other 4 unknown.
- **EN ISO E2 form status** — disabled at time of training due to Desktop importer bug; current state unknown
- **"Folder + GUIDs" file delivery mode** — mentioned in tech demo, not explained
- **Forward-compat warning feature** — trainer suggested adding, unclear if implemented
- **Complete path shortcut list** — only `[my documents]` confirmed; "desktop" and "one or two others" mentioned but not enumerated
- **Config.xml schema details** — deliberately not documenting internals beyond "it's where your settings live"

---

## 7. Open items requiring Nuno's input

*(None blocking — all previously resolved in planning conversation. This section kept for traceability.)*

---

## 8. Execution plan

Plan approved on 2026-04-23. Drafting proceeds in this order (foundation first, so later pages can reference earlier ones):

1. **Core Concepts** (3 pages) — the mental model, referenced everywhere downstream
2. **Getting Started** (4 pages) — Introduction, Installation & licensing, UI, First steps
3. **Configuration** (8 pages) — reference pages for the Config tabs
4. **Guides** (6 pages) — task tutorials (cross-links to Core Concepts + Config pages)
5. **Support** (4 pages) — Troubleshooting, move Updates here, polish Get Support + keep Changelog
6. **SUMMARY.md rewrite** — flip to the new structure
7. **Cleanup** — delete old `guides/configuration.md` and `.gitbook/includes/untitled.md`
8. **Rescue pass** through the `feature/update-docs` branch for any valuable content we missed
9. **Open PR to `main`** — standard Summary/How-to-verify/Risks/Test-plan body; Rik reviews and merges

This `PROJECT-SUMMARY.md` stays in the repo after merge as persistent project documentation.
