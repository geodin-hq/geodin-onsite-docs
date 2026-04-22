---
description: Picture Log Form
---

<!--
**Content status:** Auto-assembled from product documentation
**Source quality:** B (Moderate (single source type))
**Needs:** editorial review
-->

# Picture Log Form

## Onsite Form Layouts

Onsite currently ships with 10 form layouts, curated from the 150+ layouts that exist in the [COMPANY_A]-branded predecessor (Gaia Forms). <!-- src: transcript/field-data-collection#onsite-form-layouts -->

Form types include: G1 drilling form (code `G1D`), Step 3 form (ISO standard), picture log, standalone Sample Picture Log (code `SPL`), and combined drilling + SPL bundle (`Dr+SPL`). <!-- src: transcript/field-data-collection#onsite-form-layouts -->

The G1 drilling form has 8 pages by default; pages are switchable via "Show/hide pages" (menu under the logo). Users can enable/disable pages such as SPT, discontinuities, sub-samples, and water levels based on project needs. <!-- src: transcript/field-data-collection#onsite-form-layouts -->

Example page configuration: turning off SPT, discontinuities, and sub-samples and turning on water levels yields a 5-page drilling form. <!-- src: transcript/field-data-collection#onsite-form-layouts -->

Page order inside a form can be rearranged using up/down arrows (no drag-and-drop; legacy-style reordering). <!-- src: transcript/field-data-collection#onsite-form-layouts -->

Form bundles concept: a bundle is two forms chained together as one (e.g., "Drilling Report + SPL" = G1 drilling form immediately followed by a sample picture log page). To the user it looks like a single form type selectable from the new form list. Once created, a bundle cannot be split. <!-- src: transcript/field-data-collection#onsite-form-layouts -->

In a drilling report + SPL bundle, when adding a new sample picture, Onsite does NOT require scanning a QR label — instead it shows the samples already defined on the drilling pages, so the user selects an existing sample and attaches a picture. <!-- src: transcript/field-data-collection#onsite-form-layouts -->

Forms are validated via a Validate button (tick icon). Validation lists all missing/invalid fields. Fields are color-coded: red = compulsory, black = optional. <!-- src: transcript/field-data-collection#onsite-form-layouts -->

Forms contain standard GeoDin tables (same layout as GeoDin) for layer identification, samples, etc. <!-- src: transcript/field-data-collection#onsite-form-layouts -->

Layer identification uses Munsell color chart, minor constituents, stratification, bed thickness, spacing, etc. — producing standard GeoDin codes with brackets and attributes. <!-- src: transcript/field-data-collection#onsite-form-layouts -->

Standard selection lives under Configuration > Integration > GeoDin; the current version ships 5 standards with their relevant description types. Once a form is started, the standard cannot be changed for that form. <!-- src: transcript/field-data-collection#onsite-form-layouts -->

Default form values (driller name, driller assistants, rig name, view name, unit system metric vs other, local coordinate EPSG) are configured once and auto-filled into new forms. <!-- src: transcript/field-data-collection#onsite-form-layouts -->

EN ISO E2 standard is currently disabled because of a bug in the GeoDin GeoDin ML importer for E2-flavoured GeoDin ML; re-activation takes ~5 minutes once the Desktop importer is fixed. <!-- src: transcript/field-data-collection#onsite-form-layouts -->

## Form Ownership Model (Single-Ownership)

Only one copy of a form exists at any time — the digital equivalent of "one piece of paper" physically on a shelf. Prevents two users from editing the same form simultaneously. <!-- src: transcript/field-data-collection#form-ownership-model-single-ownership -->

A form belongs to either the user's local "briefcase" (load local / save) or is published to a shared location (publish / retrieve). <!-- src: transcript/field-data-collection#form-ownership-model-single-ownership -->

Ownership is file-level, not role-level: whoever currently holds the live `.GDOF` owns it, regardless of user identity. <!-- src: transcript/field-data-collection#form-ownership-model-single-ownership -->

When a user publishes an incomplete form, only another Onsite user with access to the shared folder can retrieve it; the original user loses the ability to "Load Local" that form until they retrieve it again. <!-- src: transcript/field-data-collection#form-ownership-model-single-ownership -->

The ownership model is strictly exclusive, never concurrent. <!-- src: transcript/field-data-collection#form-ownership-model-single-ownership -->

## Cross-Version Form Compatibility

Backward compatibility is guaranteed: newer Onsite versions can always read data created by older versions. <!-- src: transcript/field-data-collection#cross-version-form-compatibility -->

Forward compatibility: a form created by a newer version can be opened by an older version, but fields from new tables/pages will be dropped on save. <!-- src: transcript/field-data-collection#cross-version-form-compatibility -->

A form published by an older version can be retrieved by a newer version without issue. <!-- src: transcript/field-data-collection#cross-version-form-compatibility -->

Recommendation: in collaborative setups, all team members should upgrade Onsite as soon as an upgrade becomes available, and a user should not retrieve a form if they know an update is pending. <!-- src: transcript/field-data-collection#cross-version-form-compatibility -->
