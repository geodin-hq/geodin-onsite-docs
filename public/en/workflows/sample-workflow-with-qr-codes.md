---
description: Sample Workflow with Qr Codes
---

<!--
**Content status:** Auto-assembled from product documentation
**Source quality:** B (Moderate (single source type))
**Needs:** editorial review
-->

# Sample Workflow with Qr Codes

## Onsite Purpose & Core Workflow

GeoDin Onsite is the field/tablet/mobile companion app for digital form filling, designed to replace paper drilling logs. <!-- src: transcript/field-data-collection#onsite-purpose-core-workflow -->

Onsite is fundamentally a "form filler" — a digital form-filling application optimized for on-site geotechnical data capture. <!-- src: transcript/field-data-collection#onsite-purpose-core-workflow -->

Intended workflow is "fire and forget": capture data on-site, publish to the office, then move the tablet on to the next task without further involvement. <!-- src: transcript/field-data-collection#onsite-purpose-core-workflow -->

Onsite has no server front-end — it cannot talk directly to a GeoDin server; all project metadata and data exchange goes via GeoDin ML files and shared folders. <!-- src: transcript/field-data-collection#onsite-purpose-core-workflow -->

Onsite is configured per project: each install is tied to a specific project number (also called project identifier), with defaults like client, client number, driller name, and rig name stored at project level and auto-populated into new forms. <!-- src: transcript/field-data-collection#onsite-purpose-core-workflow -->

On every startup Onsite shows a project confirmation dialog asking the user to verify they are still working on the currently configured project. <!-- src: transcript/field-data-collection#onsite-purpose-core-workflow -->

First-run initialization shows a welcome dialog prompting the user to go to Configuration and choose their language. <!-- src: transcript/field-data-collection#onsite-purpose-core-workflow -->

## Publish / Retrieve / Revoke / Shelf Workflow

"Save Local" stores a form locally in the project folder without changing its ownership status. <!-- src: transcript/field-data-collection#publish-retrieve-revoke-shelf-workflow -->

"Publish" moves the form into the file-delivery system ("the shelf") with a status. <!-- src: transcript/field-data-collection#publish-retrieve-revoke-shelf-workflow -->

Three publish states exist: `Incomplete`, `Final/Complete`, and `Partial` (Partial is an advanced mode). <!-- src: transcript/field-data-collection#publish-retrieve-revoke-shelf-workflow -->

Publishing as Complete requires all form validation to pass. Publishing as Incomplete is allowed even with validation errors. <!-- src: transcript/field-data-collection#publish-retrieve-revoke-shelf-workflow -->

Publish as Incomplete places only the `.GDOF` file on the shelf — no PDF or GeoDin ML is generated yet; other colleagues can retrieve it via the Retrieve button. <!-- src: transcript/field-data-collection#publish-retrieve-revoke-shelf-workflow -->

Publish as Final/Complete generates the full deliverable set (`.GDOF` + PDF + GeoDin ML + AGS where applicable) into the shared delivery folder. <!-- src: transcript/field-data-collection#publish-retrieve-revoke-shelf-workflow -->

Two conceptual shelves exist: incomplete (can be retrieved back) and final/complete (belongs to office staff; normal users cannot retrieve from it). <!-- src: transcript/field-data-collection#publish-retrieve-revoke-shelf-workflow -->

When published, the original `.GDOF` "leaves" the local `projects` folder — Load Local will no longer find it on the tablet. <!-- src: transcript/field-data-collection#publish-retrieve-revoke-shelf-workflow -->

A local photocopy of any published form is always kept locally (marked internally as a copy, not the "live" version) for disaster recovery — protects against cloud sync folder failures (Google Drive, Dropbox, etc.). <!-- src: transcript/field-data-collection#publish-retrieve-revoke-shelf-workflow -->

"Retrieve" is the reverse of Publish — it reads a form from the shared delivery folder back onto the tablet and transfers ownership to the local user. After retrieve, a "photocopy" remains on the shelf, marked as not-owned. <!-- src: transcript/field-data-collection#publish-retrieve-revoke-shelf-workflow -->

The Retrieve button only appears when a file delivery option is configured. <!-- src: transcript/field-data-collection#publish-retrieve-revoke-shelf-workflow -->

"Revoke": if a form was published as Complete but a mistake is discovered, the user can load the local photocopy and press Revoke to reactivate it as the live copy and allow re-submission. Revoke is flagged as dangerous because it can overwrite data already processed downstream. <!-- src: transcript/field-data-collection#publish-retrieve-revoke-shelf-workflow -->

PDFs exported from forms always include a "DRAFT" watermark unless the form was saved via Publish as Complete. GeoDin ML exports never have a draft watermark. <!-- src: transcript/field-data-collection#publish-retrieve-revoke-shelf-workflow -->

`Send embedded pictures` option (in delivery config) controls whether raw full-resolution image files are uploaded separately when publishing: `Always`, `Ask every time`, or `Never`. PDFs always contain reduced/compressed embedded versions regardless. <!-- src: transcript/field-data-collection#publish-retrieve-revoke-shelf-workflow -->

## Sample Workflow & QR Codes

Sample workflow on a drilling form: select sampling method (e.g., liner tube 4-inch), condition (e.g., undisturbed), recovery percentage (e.g., 95%+), sample type, depth reference, then print a QR-coded label that can be stuck on the physical sample. <!-- src: transcript/field-data-collection#sample-workflow-qr-codes -->

Each soil sample is given a unique ID with the structure: 1 fixed prefix letter (configurable) + 6 characters encoding a timestamp + 4 random characters. <!-- src: transcript/field-data-collection#sample-workflow-qr-codes -->

Prefix length is adjustable: if extended to 2 or 3 characters, the random section shrinks to 3 or 2 characters respectively (prefix + random is always 5 characters total). <!-- src: transcript/field-data-collection#sample-workflow-qr-codes -->

The timestamp portion of the sample ID changes every second, so collisions only happen if more than ~20–100 samples are generated in the exact same second. <!-- src: transcript/field-data-collection#sample-workflow-qr-codes -->

QR code label scanning: when attaching a picture to a sample in a standalone Sample Picture Log form, the user first scans the sample's printed QR label; Onsite then knows all sample details and lets the user add pictures. <!-- src: transcript/field-data-collection#sample-workflow-qr-codes -->
