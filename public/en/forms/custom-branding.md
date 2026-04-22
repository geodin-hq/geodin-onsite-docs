---
description: Custom Branding
---

<!--
**Content status:** Auto-assembled from product documentation
**Source quality:** B (Moderate (single source type))
**Needs:** editorial review
-->

# Custom Branding

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
