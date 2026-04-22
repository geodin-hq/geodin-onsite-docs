---
description: Cloud Sync
---

<!--
**Content status:** Auto-assembled from product documentation
**Source quality:** C (Thin (limited source material))
**Needs:** editorial review
-->

# Cloud Sync

## Cloud Sync / Shared Folder Integrations

File delivery integration is folder-based. Options include `None` (local-only), `Shared network folder`, and `Folder plus equal IDs` (the last two behave nearly identically). <!-- src: transcript/api-integrations#cloud-sync-shared-folder-integrations -->

Synchronization of the shared delivery folder is explicitly out of scope for Onsite — it does not know or care whether the folder is a mapped network drive, OneDrive, Google Drive, Dropbox, SharePoint, or any other sync target; it simply reads/writes files to the configured path and relies on the external sync client. <!-- src: transcript/api-integrations#cloud-sync-shared-folder-integrations -->

File delivery works with any cloud or network target: Dropbox, Google Drive, OneDrive, mapped drives (P:, X:), corporate network shares. <!-- src: transcript/api-integrations#cloud-sync-shared-folder-integrations -->

The shared delivery folder must not point to the `%APPDATA%` working folder or the local-photocopy folder — Onsite may warn but should not be configured that way. <!-- src: transcript/api-integrations#cloud-sync-shared-folder-integrations -->

A `Make a local copy of delivered` option in shared-folder delivery preserves a local backup of every published form (GDOF, PDF, GeoDin ML) for disaster recovery — so data is not lost if the cloud-sync folder fails (e.g., Google Drive account closed, Dropbox issue). <!-- src: transcript/api-integrations#cloud-sync-shared-folder-integrations -->

`Send embedded pictures` option in delivery config controls whether raw full-resolution image files are uploaded separately when publishing: `Always`, `Ask every time`, or `Never`. PDFs always contain compressed embedded versions regardless. <!-- src: transcript/api-integrations#cloud-sync-shared-folder-integrations -->

Internet/cloud connectivity is required only at publish/retrieve time; the tablet does not need to be online while filling out forms. <!-- src: transcript/api-integrations#cloud-sync-shared-folder-integrations -->

Gaia Forms (the predecessor/sibling product) has additional delivery mechanisms — direct SharePoint integration and direct upload to Amazon AWS S3 buckets — which Onsite does not have. <!-- src: transcript/api-integrations#cloud-sync-shared-folder-integrations -->
