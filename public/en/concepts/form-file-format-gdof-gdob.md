---
description: Form File Format GDOF GDOB
---

<!--
**Content status:** Auto-assembled from product documentation
**Source quality:** B (Moderate (single source type))
**Needs:** editorial review
-->

# Form File Format GDOF GDOB

## GeoDin Onsite — Form File Format (GDOF / GDOB)

Inside a project folder, Onsite forms are saved as individual files with extensions `.GDOF` or `.GDOB` (GeoDin Onsite Form / GeoDin Onsite Bundle). <!-- src: transcript/data-model-architecture#geodin-onsite-form-file-format-gdof-gdob -->

`.GDOF` and `.GDOB` files are XML internally — they can be opened in a text editor (e.g. Notepad). <!-- src: transcript/data-model-architecture#geodin-onsite-form-file-format-gdof-gdob -->

Each form file contains the contract number, the location GUID, and other identifiers that tie the form to a specific project/location. <!-- src: transcript/data-model-architecture#geodin-onsite-form-file-format-gdof-gdob -->

Each form file contains a `history` section that logs every event on the form: timestamp, user name, computer name, Onsite version, and action (created, saved, published as incomplete, retrieved, published as complete, etc.). <!-- src: transcript/data-model-architecture#geodin-onsite-form-file-format-gdof-gdob -->

Fixing wrong project/location assignments requires editing the internal XML (contract number, location GUID) manually. <!-- src: transcript/data-model-architecture#geodin-onsite-form-file-format-gdof-gdob -->

Form file names follow a fixed auto-generated pattern determined by the form type: `<locationName>_<formCode>_<date>...` (e.g. the G1 drilling form uses code `G1D`, the Sample Picture Log uses `SPL`). <!-- src: transcript/data-model-architecture#geodin-onsite-form-file-format-gdof-gdob -->

Picture files are named after project number + location + reference + depth, so they remain uniquely identifiable outside the form. <!-- src: transcript/data-model-architecture#geodin-onsite-form-file-format-gdof-gdob -->

Backward compatibility is guaranteed: newer Onsite versions can always read data created by older versions. <!-- src: transcript/data-model-architecture#geodin-onsite-form-file-format-gdof-gdob -->

Cross-version compatibility: a form published by an older version can be retrieved by a newer version without issue; a newer-version form opened in an older version may drop fields from new tables/pages on save. <!-- src: transcript/data-model-architecture#geodin-onsite-form-file-format-gdof-gdob -->

There is currently no warning when a user opens a form created by a newer version than their local installation. <!-- src: transcript/data-model-architecture#geodin-onsite-form-file-format-gdof-gdob -->

## GeoDin Onsite — Form Ownership & Lifecycle

Form ownership model: only one copy of a form exists at any time. A form belongs to either the user's local "briefcase" (Load Local / Save Local) or is published to a shared location (Publish / Retrieve). <!-- src: transcript/data-model-architecture#geodin-onsite-form-ownership-lifecycle -->

Analogy: a piece of paper physically on a shelf — prevents two users from editing the same form simultaneously. <!-- src: transcript/data-model-architecture#geodin-onsite-form-ownership-lifecycle -->

Only one user can own and edit a form at a time (digital equivalent of "single existence"); the ownership model is strictly exclusive, never concurrent. <!-- src: transcript/data-model-architecture#geodin-onsite-form-ownership-lifecycle -->

Ownership of a form is a file-level concept, not a user concept — whoever currently holds the live `.GDOF` owns it, regardless of user identity. <!-- src: transcript/data-model-architecture#geodin-onsite-form-ownership-lifecycle -->

Form ownership is user-bound in practice: when a user publishes an incomplete form, only another Onsite user with access to the shared folder can retrieve it; the original user loses the ability to `Load Local` that form until they retrieve it again. <!-- src: transcript/data-model-architecture#geodin-onsite-form-ownership-lifecycle -->

"Save Local" stores a form locally in the project folder without changing its ownership status. <!-- src: transcript/data-model-architecture#geodin-onsite-form-ownership-lifecycle -->

"Publish" moves the form into the file-delivery system with a status and transfers it to the "shelf". <!-- src: transcript/data-model-architecture#geodin-onsite-form-ownership-lifecycle -->

Three publish states exist: `Incomplete`, `Final/Complete`, and `Partial` (Partial is more advanced). <!-- src: transcript/data-model-architecture#geodin-onsite-form-ownership-lifecycle -->

Publishing as `Complete` requires all form validation to pass; publishing as `Incomplete` is allowed even with validation errors, and only the `.GDOF` file is placed on the shelf (no PDF or GeoDin ML generated yet). <!-- src: transcript/data-model-architecture#geodin-onsite-form-ownership-lifecycle -->

When a form is published, the `.GDOF` file is moved to the shared delivery folder ("the shelf"). On `Publish as Complete`, a PDF, GeoDin ML, and AGS file are generated and placed there simultaneously. The original file "leaves" the local `projects` folder — `Load Local` will no longer find it. <!-- src: transcript/data-model-architecture#geodin-onsite-form-ownership-lifecycle -->

Two "shelves" exist when publishing: incomplete (can be retrieved back by colleagues) and final/complete (goes to a shelf the user cannot retrieve from; belongs to the office staff). <!-- src: transcript/data-model-architecture#geodin-onsite-form-ownership-lifecycle -->

A local "photocopy" of any published form is always kept locally (marked internally as a copy, not the "live" version) for disaster recovery, so data is not lost if the cloud sync folder fails (e.g. closed Google Drive account, Dropbox issue). <!-- src: transcript/data-model-architecture#geodin-onsite-form-ownership-lifecycle -->

`Retrieve` is the reverse of `Publish` — it reads a form from the shared delivery folder back onto the tablet and transfers ownership to the local user; a photocopy remains on the shelf, marked as not-owned. <!-- src: transcript/data-model-architecture#geodin-onsite-form-ownership-lifecycle -->

`Retrieve` only appears in the UI when a file delivery option is configured. <!-- src: transcript/data-model-architecture#geodin-onsite-form-ownership-lifecycle -->

`Revoke`: if a form has been published as complete but the user later realises there was a mistake, they can load the local photocopy and press `Revoke`, which reactivates it as the live copy and allows re-submission. Revoke is marked as dangerous because it can overwrite data already processed downstream. <!-- src: transcript/data-model-architecture#geodin-onsite-form-ownership-lifecycle -->

Forms are auto-saved when closed or when the program is closed; an explicit Save button exists but is rarely needed. <!-- src: transcript/data-model-architecture#geodin-onsite-form-ownership-lifecycle -->

## GeoDin Onsite — Backups & Form History

Onsite takes snapshots every 30 seconds or every 2 minutes and retains up to 10 versions (~5 minutes of work history); the interval is configurable in settings. <!-- src: transcript/data-model-architecture#geodin-onsite-backups-form-history -->

Backups are accessed via `Tools > Restore backups`, which lists recent forms and lets the user pick a version to restore. <!-- src: transcript/data-model-architecture#geodin-onsite-backups-form-history -->

Restore overwrites the active live copy and cannot be undone. <!-- src: transcript/data-model-architecture#geodin-onsite-backups-form-history -->

Backups are stored in a hidden local folder inside the Onsite working folder; users normally access them via `Tools > Restore backups` rather than browsing the folder directly. <!-- src: transcript/data-model-architecture#geodin-onsite-backups-form-history -->

Every form carries an internal `history` log capturing timestamp, user name, computer name, Onsite version, and action for each event (created, saved, published, retrieved, etc.). <!-- src: transcript/data-model-architecture#geodin-onsite-backups-form-history -->
