---
description: Custom Form Layouts
---

<!--
**Content status:** Auto-assembled from product documentation
**Source quality:** B (Moderate (single source type))
**Needs:** editorial review
-->

# Custom Form Layouts

## Custom Data Types & Validation

Users can create their own custom data types via `System > Data Types > New Data Type`; these live in the user's syslib and are shared across users on the same syslib. <!-- src: transcript/forms-templates-customization#custom-data-types-validation -->

Custom data types require a unique 3-character short name that doesn't conflict with existing system data types; the GeoDin team can provide the list of reserved short names. <!-- src: transcript/forms-templates-customization#custom-data-types-validation -->

Custom data types support: parameter names, formulas with their own syntax, validations (possibility checks). <!-- src: transcript/forms-templates-customization#custom-data-types-validation -->

Custom data types can be used in batch import of values and called in templates like any built-in type. <!-- src: transcript/forms-templates-customization#custom-data-types-validation -->

Custom tables should use parameter names that do not collide with existing parameters in other tables (best practice). <!-- src: transcript/forms-templates-customization#custom-data-types-validation -->

Custom tables remain local to the user and are NOT overwritten by GeoDin distribution updates. <!-- src: transcript/forms-templates-customization#custom-data-types-validation -->

Central GeoDin-distributed tables cannot be edited by users (must remain consistent across installations). <!-- src: transcript/forms-templates-customization#custom-data-types-validation -->

Data types contain built-in formulas (e.g., the water content table auto-calculates W from tin mass, wet mass, dry mass inputs); formula cells are displayed in darker blue to indicate auto-populated calculated fields. <!-- src: transcript/forms-templates-customization#custom-data-types-validation -->

Each measurement table parameter has both a long name (human-readable) and a short/database field name (used in macros, queries, formulas) — toggle via right-click "short field name". <!-- src: transcript/forms-templates-customization#custom-data-types-validation -->

Data type tables are inspectable via `System > Data Types > [table name]` — shows parameter list, long name, database field name, active formulas. <!-- src: transcript/forms-templates-customization#custom-data-types-validation -->

**Compulsory fields** appear in a darker purple color in the form — e.g., the `Method` field in general data. <!-- src: transcript/forms-templates-customization#custom-data-types-validation -->

Saving a record without a compulsory field triggers an error telling the user which field is required. <!-- src: transcript/forms-templates-customization#custom-data-types-validation -->

External users may not have permission to modify system data types (Data Types under System Configuration is read-only for external users). <!-- src: transcript/forms-templates-customization#custom-data-types-validation -->

## GeoDin Onsite Form Layouts

Onsite is fundamentally "a form filler" / digital form-filling application. <!-- src: transcript/forms-templates-customization#geodin-onsite-form-layouts -->

Onsite currently ships with 10 form layouts, selected from the 150+ layouts that exist in Gaia Forms (the predecessor tool). <!-- src: transcript/forms-templates-customization#geodin-onsite-form-layouts -->

Form types: **G1 drilling form** (code `G1D`), **Step 3 form** (ISO standard), **picture log**, **standalone Sample Picture Log** (code `SPL`), and a combined **Drilling Report + SPL bundle** (`Dr+SPL`). <!-- src: transcript/forms-templates-customization#geodin-onsite-form-layouts -->

The G1 drilling form has 8 pages by default, but pages are switchable via "Show/hide pages" (menu under the logo). Users can turn pages on/off based on need (e.g., switch off SPT, discontinuities, sub-samples; switch on water levels). Example: turning off SPT/discontinuities/sub-samples and turning on water levels yields 5 pages. <!-- src: transcript/forms-templates-customization#geodin-onsite-form-layouts -->

Page order inside a form can be rearranged using up/down arrows (no drag-and-drop; legacy-style reordering). <!-- src: transcript/forms-templates-customization#geodin-onsite-form-layouts -->

**Form bundles** concept: a bundle is two forms chained together as one (e.g., G1 drilling form immediately followed by a sample picture log page). To the user it looks like a single form type selectable from the new form list. Once created, a bundle cannot be split. <!-- src: transcript/forms-templates-customization#geodin-onsite-form-layouts -->

In a Drilling Report + SPL bundle, when adding a new sample picture, Onsite does NOT require scanning a QR label — instead it shows the samples already defined on the drilling pages so the user selects an existing sample and attaches a picture to it. <!-- src: transcript/forms-templates-customization#geodin-onsite-form-layouts -->

Forms are validated via a Validate button (also appears as a tick icon); validation lists all missing/invalid fields. <!-- src: transcript/forms-templates-customization#geodin-onsite-form-layouts -->

Fields are color-coded: red = compulsory, black = optional. <!-- src: transcript/forms-templates-customization#geodin-onsite-form-layouts -->

Forms contain standard GeoDin tables (same layout as in GeoDin) for layer identification, samples, etc. <!-- src: transcript/forms-templates-customization#geodin-onsite-form-layouts -->

Layer identification uses Munsell color chart, minor constituents, stratification, bed thickness, spacing, etc. — producing standard GeoDin codes with brackets and attributes. <!-- src: transcript/forms-templates-customization#geodin-onsite-form-layouts -->

Standard selection: `Configuration > Integration > GeoDin` lets the user select which drilling/description standard to use. The current Onsite version includes 5 standards with their relevant description types. Once a form is started, the standard cannot be changed for that form. <!-- src: transcript/forms-templates-customization#geodin-onsite-form-layouts -->

Default form values (driller name, driller assistants, rig name, view name, unit system, local coordinate system EPSG code) are configured once and auto-filled into new forms. <!-- src: transcript/forms-templates-customization#geodin-onsite-form-layouts -->

Forms have a validation state — incomplete forms (missing required fields) cannot be published as complete. <!-- src: transcript/forms-templates-customization#geodin-onsite-form-layouts -->

Documentation gap: there is no proper Onsite manual yet; two layers of documentation are recommended in the future — (1) general mechanics (publish vs export, incomplete vs complete, file delivery, shelves analogy), (2) per-form domain documentation (what each field means on the drilling form, how to do layer identification, GeoDin code system). A first-steps tutorial is also planned. <!-- src: transcript/forms-templates-customization#geodin-onsite-form-layouts -->

## Custom Branding (Logo & Watermark)

Default logo ships in the Onsite installation folder as `assets/logo.png`. <!-- src: transcript/forms-templates-customization#custom-branding-logo-watermark -->

To customize the logo printed on forms: place a custom `logo.png` in `%APPDATA%\Roaming\GeoDin.Onsite\`. Onsite reads the user copy over the default. <!-- src: transcript/forms-templates-customization#custom-branding-logo-watermark -->

The custom logo file must maintain the default aspect ratio (default is 478 x 376 px) and should have a white background. <!-- src: transcript/forms-templates-customization#custom-branding-logo-watermark -->

PDF exports always include the watermark "DRAFT" across the page unless the form was saved via `Publish as Complete`. <!-- src: transcript/forms-templates-customization#custom-branding-logo-watermark -->

`Publish as Complete` generates a PDF without the draft watermark (and a GeoDin ML file simultaneously). <!-- src: transcript/forms-templates-customization#custom-branding-logo-watermark -->

The draft watermark does not apply to GeoDin ML exports. <!-- src: transcript/forms-templates-customization#custom-branding-logo-watermark -->

Files in the Onsite installation folder (including default config/template files) are read-only — users must never edit them directly; customization is done by copying the file into the working folder (`%APPDATA%\Roaming\GeoDin.Onsite\`) and editing there. <!-- src: transcript/forms-templates-customization#custom-branding-logo-watermark -->

A customized set of files (`config.xml`, custom `logo.png`, custom ZPL files) can be distributed to other users as a one-time copy to pre-configure installations, but `config.xml` must not be pointed at a shared network location — each user needs their own copy. <!-- src: transcript/forms-templates-customization#custom-branding-logo-watermark -->

The `[my documents]` placeholder in paths keeps `config.xml` shareable because it does not hardcode the user name. <!-- src: transcript/forms-templates-customization#custom-branding-logo-watermark -->

## Cross-Section Layouts

Cross-section creation workflow (All Objects branch > Cross Section method): <!-- src: transcript/forms-templates-customization#cross-section-layouts -->

Cross-section depth scale divisions can be changed (e.g., 1 m > 5 m main division). <!-- src: transcript/forms-templates-customization#cross-section-layouts -->

Cross-sections can be saved as either GLO (template) or GGF (with connected data). <!-- src: transcript/forms-templates-customization#cross-section-layouts -->

GGF cross-sections are stored as graphic files and can be opened later with their data intact. <!-- src: transcript/forms-templates-customization#cross-section-layouts -->

Cross-sections can be stored in the project's Documents area (New Folder > New Document > choose GGF file > save in database OR link to external file). <!-- src: transcript/forms-templates-customization#cross-section-layouts -->

Cross-section method has a "from the top" map view for selecting boreholes spatially. <!-- src: transcript/forms-templates-customization#cross-section-layouts -->
