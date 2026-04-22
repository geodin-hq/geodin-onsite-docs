---
description: Publish Retrieve Revoke
---

<!--
**Content status:** Auto-assembled from product documentation
**Source quality:** B (Moderate (single source type))
**Needs:** editorial review
-->

# Publish Retrieve Revoke

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
