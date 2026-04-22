---
description: File Formats GDOF GDOB
---

<!--
**Content status:** Auto-assembled from product documentation
**Source quality:** B (Moderate (single source type))
**Needs:** editorial review
-->

# File Formats GDOF GDOB

## File Formats (.GDOF, .GDOB, XML Internals)

Forms are saved as individual files with extensions `.GDOF` (GeoDin Onsite Form) or `.GDOB` (GeoDin Onsite Bundle). <!-- src: transcript/field-data-collection#file-formats-gdof-gdob-xml-internals -->

`.GDOF` and `.GDOB` files are XML internally — they can be opened in a text editor (e.g., Notepad). Each file contains the contract number, the location GUID, and other identifiers that tie the form to a specific project/location. <!-- src: transcript/field-data-collection#file-formats-gdof-gdob-xml-internals -->

Each form file contains a `history` section that logs every event on the form: timestamp, user name, computer name, Onsite version, and action (created, saved, published as incomplete, retrieved, published as complete, etc.). <!-- src: transcript/field-data-collection#file-formats-gdof-gdob-xml-internals -->

The `history` section captures identity information (user name, computer name) for audit purposes even though Onsite has no user accounts or authentication. <!-- src: transcript/field-data-collection#file-formats-gdof-gdob-xml-internals -->

File-name patterns are determined by the form type — e.g., a G1 drilling form uses the pattern `<locationName>_G1D_<date>...`. No manual file naming required. <!-- src: transcript/field-data-collection#file-formats-gdof-gdob-xml-internals -->

Onsite uses a rigid, fixed file-name pattern and fixed storage locations — users cannot choose where forms are saved on the device. <!-- src: transcript/field-data-collection#file-formats-gdof-gdob-xml-internals -->

Project numbers and location short names are automatically sanitized — any character invalid in a Windows file name/path (e.g., `*`, `+`) is replaced with `_` because values are used directly in file names and paths. <!-- src: transcript/field-data-collection#file-formats-gdof-gdob-xml-internals -->

Project number restrictions: letters, numbers, dashes, and underscores only. No spaces, no special characters, no umlauts. <!-- src: transcript/field-data-collection#file-formats-gdof-gdob-xml-internals -->

If a user reuses an existing project number by mistake, Onsite writes into the existing folder; file-name collisions are avoided by appending `_1`, `_2`, `_3` suffixes to older files. Fixing wrong project/location assignments requires editing the internal XML (contract number, location GUID) manually. <!-- src: transcript/field-data-collection#file-formats-gdof-gdob-xml-internals -->

## File Delivery & Cloud Sync

File delivery is configured under Configuration > Integration > File Delivery. Options: `No delivery` (default, local-only standalone mode), `Shared network folder`, and `Folder plus equal IDs` (behaves nearly identically to Shared network folder). <!-- src: transcript/field-data-collection#file-delivery-cloud-sync -->

Synchronization of the shared delivery folder is explicitly out of scope — Onsite does not know or care whether the folder is on a mapped network drive, OneDrive, Google Drive, Dropbox, SharePoint, or any other service. It simply reads/writes files to the configured path and relies on the external sync client. <!-- src: transcript/field-data-collection#file-delivery-cloud-sync -->

Gaia Forms had additional delivery mechanisms (direct SharePoint integration, direct AWS S3 upload) which Onsite does not currently ship. <!-- src: transcript/field-data-collection#file-delivery-cloud-sync -->

A "Make a local copy of delivered" option in shared-folder delivery preserves a local backup of every published form (GDOF, PDF, GeoDin ML) for disaster recovery. <!-- src: transcript/field-data-collection#file-delivery-cloud-sync -->

The shared delivery folder must not point to the `%APPDATA%` working folder or the same folder used for the local photocopy of delivered files — Onsite may warn about this misconfiguration. <!-- src: transcript/field-data-collection#file-delivery-cloud-sync -->

Export folder path is controlled by Configuration > Folders > Export folder path; supports shortcut codes like `[my documents]`, `[desktop]`, etc. (full list limited). Exports are always placed in a project-named subfolder, auto-created by Onsite. <!-- src: transcript/field-data-collection#file-delivery-cloud-sync -->
