<!-- GENERATED FILE - do not edit here.
     Canonical source: geodin-docs-internal/rules/docs-style-rules.md
     Regenerate with:  geodin-docs-internal/scripts/sync-rules.sh -->

# GeoDin docs - contribution style rules

These rules apply to every change in this repo, whoever (or whatever) authors it:
AI agents, pipeline PRs, and hand edits alike. They are the operative distillation
of the GeoDin docs house style. CI enforces the mechanical parts
(`.github/workflows/docs-lint.yml`); the rest is checked at review.

## 1. Typography - ASCII only

No smart typography in any docs prose. Replace before committing:

| Never | Use instead |
|---|---|
| em dash / en dash | `-` |
| curly quotes / apostrophes | straight `"` and `'` |
| ellipsis character | `...` |
| arrow characters | `>` for UI paths, `->` otherwise |
| middle-dot separators | `\|` or `,` |
| non-breaking / narrow spaces | regular space |

Keep: `(R)`-style registered marks as the real symbol, accented characters in
names, and house-style callout emoji inside hints. CI runs
`scripts/check-typography.sh` on every PR.

## 2. Page structure - five progressive tiers

A reader should be able to stop at any point and have gotten value: the first
screen gets a beginner to a working result; the bottom answers the power user's
last question. Nothing above may require knowledge introduced below.

Tiers, in this order (omit tiers that do not apply; never reorder):

1. **Requirements** (`## Requirements`) - only when the page has real
   prerequisites: formats, object types, licenses, prior setup. Short bullets,
   links to setup pages. Never manufacture an empty Requirements section.
2. **Task walkthrough** - one outcome, end-to-end. The only always-present tier
   on a how-to page. Prefer GitBook's Stepper block; `### Step 1: ...` headings
   are acceptable. Each step: what to do, where to click (**bold UI names**),
   and its screenshot at the step it illustrates - never pooled at the end.
   A beginner who stops after the last step has a working result.
3. **Optional settings** (`## Optional ...`) - bullet list of option -> effect.
   No procedures here.
4. **Working with [topic]** - after a `***` divider: intermediate prose on how
   the pieces behave and interact. Paragraphs, not steps.
5. **Reference: [element]** - after a `***` divider: the exhaustive layer,
   subsections per option family, tables for enumerable modes.

`***` dividers only at audience shifts (max 2 per page). When the Reference tier
grows past roughly half the page, promote it to a subpage and leave a pointer.

Adaptation by page type:

| Page type | Tiers |
|---|---|
| How-to / workflow page | Tier 2 mandatory; 1 and 3 when they apply; 4-5 as content exists |
| Reference page | Tier 5 dominates; still open with 2-3 orientation sentences |
| Concept page | Prose only; order simple -> nuanced |
| Landing page / section README | Exempt: short orientation + links |
| Troubleshooting / contact | Exempt: short by nature |

## 3. Tutorial-grade sources (Looms, SOPs)

A step-by-step workflow source becomes **one tutorial page per workflow**:
numbered steps, one figure per step, a "Next step" link chaining to the next
tutorial, and a hub page ordering the series beginner -> advanced. Never
compress a tutorial source into bullet summaries under an existing page.

## 4. GitBook blocks - match the block to the intent

| Need | Block |
|---|---|
| Sequential procedure | Stepper (`{% stepper %}` / `{% step %}`) |
| Platform / variant alternatives | Tabs |
| Optional detail that would bloat the flow | Expandable (`<details>`) |
| Tip / caution / warning | Hint - match severity (`info`, `success`, `warning`, `danger`), do not default everything to `info` |
| Code / config / file contents | Code block, with `title=` and `lineNumbers` when useful |
| Screenshot | `<figure>` + `<figcaption>` |

You cannot nest an Expandable or another Stepper inside a Stepper.

**Caption rule:** every screenshot gets a visible `<figcaption>` stating what
the image shows and what to notice in it. Alt text alone is not a substitute.
Key facts live in the text, not only in screenshots - the step's words must
convey what to do without the image.

## 5. Formatting idioms

- **Bold** for UI elements and button names; `code` for identifiers.
- `##` (H2) for tier sections - GitBook's page outline shows only H1/H2.
  `###`/`####` inside tiers (steps may stay `###`). One H1 per page.
- Tables only for enumerable facts; explanations stay in prose.
- No process flags (HTML comments about status/verification) in page source -
  the repo is public and comments are readable in the GitHub source.

## 6. Index and SUMMARY.md structure

- Page groups (`##` in SUMMARY.md) exist only at the top level.
- At most two levels of subpages (three levels total including the page).
- One markdown file = one URL: a page appears exactly once in SUMMARY.md.
- Every content page is reachable from SUMMARY.md - no orphans.
- Each group gets a short landing page (section README) that orients the reader.
- Order by user journey, top to bottom: arrive and set up -> understand the
  model -> daily work in workflow order (in -> manage -> find -> visualize ->
  out) -> power use -> connect and extend -> administer -> troubleshooting last.
  The same principle applies inside each section: reading top-to-bottom never
  requires knowledge introduced further down.
- One topic per page; cross-link instead of repeating a concept across pages.

## 7. Content preservation

- **Additive only.** Re-ordering within a page is allowed; deleting content is
  not. No "delete and relocate" edits.
- **Every image survives**, attached to the step or section it illustrates.
- Hardware names and vendor links are content, not marketing - keep them.

***

*For local agents with access to the private companion repo: the full editorial
policy (content policy, frozen pages, workflow) is at
`~/GitHub/geodin-docs-internal/rules/docs-editorial-policy.md` - read it before
editing if the path exists.*
