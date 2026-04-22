---
description: Keygen and Hardware Binding
---

<!--
**Content status:** Auto-assembled from product documentation
**Source quality:** B (Moderate (single source type))
**Needs:** editorial review
-->

# Keygen and Hardware Binding

## Product Architecture Overview

GeoDin is a Windows client application, installed per-machine or as a central network installation. <!-- src: transcript/deployment-infrastructure#product-architecture-overview -->

GeoDin Onsite is a Windows desktop application (tablet or PC), distributed as a single `setup.exe` installer. <!-- src: transcript/deployment-infrastructure#product-architecture-overview -->

Onsite has no server front-end — it cannot talk directly to a GeoDin server; all project metadata and data exchange happens via GeoDin ML files. <!-- src: transcript/deployment-infrastructure#product-architecture-overview -->

Customers can install GeoDin in a locked-down corporate environment with no Internet access. <!-- src: transcript/deployment-infrastructure#product-architecture-overview -->

## System Requirements & Runtime

Onsite is a .NET 8 program and requires the Microsoft .NET 8 runtime. <!-- src: transcript/deployment-infrastructure#system-requirements-runtime -->

On first launch, if the .NET 8 runtime is missing, Onsite redirects the user to Microsoft to download and install it. <!-- src: transcript/deployment-infrastructure#system-requirements-runtime -->

Tablets or PCs running Windows are the supported platform; no separate mobile OS build. <!-- src: transcript/deployment-infrastructure#system-requirements-runtime -->

## Backend Database Options (Desktop)

Backend database options are Microsoft Access (local or network share) or SQL Server (client-server, requires IT-managed connection string). <!-- src: transcript/deployment-infrastructure#backend-database-options-desktop -->

Microsoft Access files have a 2 GB size limit; one Access file per database is recommended. <!-- src: transcript/deployment-infrastructure#backend-database-options-desktop -->

SQL Server client-server databases support multiple concurrent projects with no project-count constraint. <!-- src: transcript/deployment-infrastructure#backend-database-options-desktop -->

Databases can be stored locally, on a company network, or on a shared network drive. <!-- src: transcript/deployment-infrastructure#backend-database-options-desktop -->

Database maintenance operations (Close Database, Maintain, Optimize) are available via right-click on the database connection. <!-- src: transcript/deployment-infrastructure#backend-database-options-desktop -->

Some corporate IT policies prevent the use of Access and require SQL Server only. <!-- src: transcript/deployment-infrastructure#backend-database-options-desktop -->

## Installation Modes (Desktop)

GeoDin can be installed per-machine (each user has their own configuration) or as a central network installation (shared configuration folders on a network drive). <!-- src: transcript/deployment-infrastructure#installation-modes-desktop -->

In central installations, all users share the same syslib, dictionaries, custom data types, and configuration. <!-- src: transcript/deployment-infrastructure#installation-modes-desktop -->

In per-machine installations, each user has their own copy of these folders. <!-- src: transcript/deployment-infrastructure#installation-modes-desktop -->

Installation folder layout is split across a bin folder (executable) and a syslib folder (dictionaries, filters, custom data types, configuration); these can be on `C:\Program Files\GeoDin\` and `C:\ProgramData\GeoDin\` respectively, or combined into a single stack. <!-- src: transcript/deployment-infrastructure#installation-modes-desktop -->

## Desktop Folder Layout

Typical installation path: `C:\ProgramData\GeoDin\`. <!-- src: transcript/deployment-infrastructure#desktop-folder-layout -->

System library (syslib) folder: `C:\ProgramData\GeoDin\System\` — contains all dictionaries and customizations. <!-- src: transcript/deployment-infrastructure#desktop-folder-layout -->

Layouts folder: `C:\ProgramData\GeoDin\Layouts\` — default layouts ship here, organized by object type. <!-- src: transcript/deployment-infrastructure#desktop-folder-layout -->

Bin folder contains the executable to run GeoDin. <!-- src: transcript/deployment-infrastructure#desktop-folder-layout -->

Syslib folder contains dictionaries (GSD files), import filters (e.g., `Sony_Filter.sys`), custom data type configurations, and other user-editable configuration. <!-- src: transcript/deployment-infrastructure#desktop-folder-layout -->

Demos folder contains sample databases shipped with the installation. <!-- src: transcript/deployment-infrastructure#desktop-folder-layout -->

Dictionaries are stored as individual `.GSD` files, one per list (e.g., `G1_EPSG.GSD` holds the EPSG code list). <!-- src: transcript/deployment-infrastructure#desktop-folder-layout -->

## Installation Modes (Onsite)

Two installation modes are offered: `All users` (requires local admin) and `Local` (per-user, no admin required). Most users are expected to choose the local option. <!-- src: transcript/deployment-infrastructure#installation-modes-onsite -->

All-users installation path: `C:\Program Files\GeoDin.Onsite\` (or similar). <!-- src: transcript/deployment-infrastructure#installation-modes-onsite -->

Local (per-user) installation default path: `%LOCALAPPDATA%\Programs\GeoDin.Onsite\` (i.e., under `C:\Users\<user>\AppData\Local\Programs\`); the user can customize this during installation. <!-- src: transcript/deployment-infrastructure#installation-modes-onsite -->

The `setup.exe` installer has no install options beyond the choice of all-users/local mode and whether to create a desktop shortcut. <!-- src: transcript/deployment-infrastructure#installation-modes-onsite -->

The installation mode (`all users` vs. `local user`) is the only user-scoping decision — it controls whether the executable is available to all Windows accounts or only to the installing user. <!-- src: transcript/deployment-infrastructure#installation-modes-onsite -->

## Onsite Working Folder Layout

The working folder (runtime data, configs, projects, logs, backups, installers) is always: `%APPDATA%\Roaming\GeoDin.Onsite\` (i.e., `C:\Users\<user>\AppData\Roaming\GeoDin.Onsite\`). <!-- src: transcript/deployment-infrastructure#onsite-working-folder-layout -->

The working folder location is hard-coded in Onsite and cannot be relocated — unlike the predecessor product, where the working folder location was customizable. This was intentionally locked down. <!-- src: transcript/deployment-infrastructure#onsite-working-folder-layout -->

`%APPDATA%` is an invisible folder by default in Windows — users can unhide via `View > Show hidden items`, or navigate via the address bar by typing `%appdata%` (jumps to Roaming) or `%localappdata%` (jumps to Local). <!-- src: transcript/deployment-infrastructure#onsite-working-folder-layout -->

Typical contents of `%APPDATA%\Roaming\GeoDin.Onsite\` after use: <!-- src: transcript/deployment-infrastructure#onsite-working-folder-layout -->

The working folder itself can be opened via `Configuration > Folders > Open local folder`. <!-- src: transcript/deployment-infrastructure#onsite-working-folder-layout -->

Log files can be opened quickly via `Help (?) > Open log files`, which jumps directly to the `logs` folder. <!-- src: transcript/deployment-infrastructure#onsite-working-folder-layout -->

## Installation Folder vs Working Folder (Onsite)

The installation folder contains the Onsite executable plus many DLLs and "default" versions of configuration/asset files (ZPL templates, default logo). <!-- src: transcript/deployment-infrastructure#installation-folder-vs-working-folder-onsite -->

All files in the installation folder are read-only; users must never edit them directly. <!-- src: transcript/deployment-infrastructure#installation-folder-vs-working-folder-onsite -->

Customization is done by copying the default file from the installation folder into the working folder (`%APPDATA%\Roaming\GeoDin.Onsite\`) and editing the copy there. <!-- src: transcript/deployment-infrastructure#installation-folder-vs-working-folder-onsite -->

Onsite reads the user copy from the working folder in preference to the default in the installation folder. <!-- src: transcript/deployment-infrastructure#installation-folder-vs-working-folder-onsite -->

Default label templates ship in the installation folder under `assets/labels/` (ZPL label templates) and `assets/logo.png` (default logo). <!-- src: transcript/deployment-infrastructure#installation-folder-vs-working-folder-onsite -->

## Configuration Files (config.xml)

`Config.xml` stores all user configuration settings for Onsite and lives in `%APPDATA%\Roaming\GeoDin.Onsite\`. <!-- src: transcript/deployment-infrastructure#configuration-files-configxml -->

`Config.xml` is generated (or regenerated) as soon as Onsite has run once and changes have been saved via `Configuration > OK`. <!-- src: transcript/deployment-infrastructure#configuration-files-configxml -->

A customized set of files (`config.xml`, custom `logo.png`, custom ZPL files) can be distributed to other users as a one-time copy to pre-configure installations. <!-- src: transcript/deployment-infrastructure#configuration-files-configxml -->

`Config.xml` must not be pointed at a shared network location — each user needs their own copy. <!-- src: transcript/deployment-infrastructure#configuration-files-configxml -->

The `[my documents]` placeholder in paths keeps `config.xml` shareable because it does not hardcode the user name. <!-- src: transcript/deployment-infrastructure#configuration-files-configxml -->

Onsite supports shortcut codes in path settings (e.g., `[my documents]`, `[desktop]`); the full list of placeholders is limited. <!-- src: transcript/deployment-infrastructure#configuration-files-configxml -->

## Installer Delivery & Updates (Onsite)

The installer is fetched from `resources.GeoDin.com/onsite/latest-version/...` — the URL structure is auto-generated by the licensing system. <!-- src: transcript/deployment-infrastructure#installer-delivery-updates-onsite -->

The installer URL is emailed to the customer after the Shopify purchase completes. <!-- src: transcript/deployment-infrastructure#installer-delivery-updates-onsite -->

Onsite periodically checks `resources.GeoDin.com` for newer versions; when the project confirmation dialog pops up on startup, an "Update available" notification may appear within ~10 seconds. <!-- src: transcript/deployment-infrastructure#installer-delivery-updates-onsite -->

Clicking update downloads the new installer, auto-uninstalls the old version, and installs the new version. <!-- src: transcript/deployment-infrastructure#installer-delivery-updates-onsite -->

Downloaded installers are cached in the `installers\` subfolder of the working folder, so they can be copied to other machines on low-bandwidth sites. <!-- src: transcript/deployment-infrastructure#installer-delivery-updates-onsite -->

Both upgrade and downgrade are technically supported, but downgrade is not recommended — the preferred recovery for a broken version is to release a fix rather than roll back. <!-- src: transcript/deployment-infrastructure#installer-delivery-updates-onsite -->

Downgrade risk: if the newer version introduced `config.xml` structure changes, the older version may fail to read the config on downgrade. Workaround: rename `%APPDATA%\Roaming\GeoDin.Onsite\` (e.g., append `_X`) after downgrading so the old version starts with a clean config. <!-- src: transcript/deployment-infrastructure#installer-delivery-updates-onsite -->

Official recommendation: always update Onsite — there is no forward-compatibility protection for form data. <!-- src: transcript/deployment-infrastructure#installer-delivery-updates-onsite -->

In collaborative setups, all team members should upgrade Onsite as soon as an upgrade becomes available, and a user should not retrieve a form if they know an update is pending. <!-- src: transcript/deployment-infrastructure#installer-delivery-updates-onsite -->

## Licensing Model (Keygen)

GeoDin uses Keygen (keygen.sh or equivalent) as the licensing system backend. <!-- src: transcript/deployment-infrastructure#licensing-model-keygen -->

Licensing is seat-based via a license key — a 30-character uppercase alphanumeric string. A single license key can cover multiple seats (multi-seat license). Example: a 20-seat "GeoDin support license". <!-- src: transcript/deployment-infrastructure#licensing-model-keygen -->

Each activation is bound to a machine via a hardware ID (fingerprint derived from hardware; cannot be spoofed or tampered with). <!-- src: transcript/deployment-infrastructure#licensing-model-keygen -->

The hardware ID may change if the disk or memory is swapped. In that case the license becomes unlinked and an admin must remove the old machine link in the Keygen dashboard so the license can be re-activated on the new hardware. <!-- src: transcript/deployment-infrastructure#licensing-model-keygen -->

The License Manager UI shows: license key, license name (customer name), expiry date, maximum GeoDin version allowed (e.g., "up to 3.99"), offline grace period (30 days), multi-seat seat count, machine name, hardware ID. <!-- src: transcript/deployment-infrastructure#licensing-model-keygen -->

The License Manager is available in English and German. <!-- src: transcript/deployment-infrastructure#licensing-model-keygen -->

Support staff manage licenses via the Keygen dashboard — suspend, renew, revoke, view customer info. <!-- src: transcript/deployment-infrastructure#licensing-model-keygen -->

Keygen is NOT a CRM — it does not handle transactions, money, or addresses. <!-- src: transcript/deployment-infrastructure#licensing-model-keygen -->

No CRM integration in the licensing backend — it only handles keys and machine bindings. <!-- src: transcript/deployment-infrastructure#licensing-model-keygen -->

Fallback when the first licensing problem occurs: contact the internal support/licensing owner before assuming a Shopify-Keygen logic bug. <!-- src: transcript/deployment-infrastructure#licensing-model-keygen -->

## Offline Grace Period

Onsite validates its license on every startup by contacting the licensing server. <!-- src: transcript/deployment-infrastructure#offline-grace-period -->

If no internet is available (e.g., tablet in the field), Onsite falls back to running offline for up to 30 days. <!-- src: transcript/deployment-infrastructure#offline-grace-period -->

After 30 days offline, the license must re-validate online before Onsite will continue to run. <!-- src: transcript/deployment-infrastructure#offline-grace-period -->

Internet/cloud connectivity is required only at the time of publish/retrieve; the tablet does not need to be online while filling out forms. <!-- src: transcript/deployment-infrastructure#offline-grace-period -->

## First-Run & Activation Flow

Post-purchase, the customer receives an email containing (1) the installer URL and (2) a license key. <!-- src: transcript/deployment-infrastructure#first-run-activation-flow -->

On first launch, Onsite shows a welcome dialog prompting the user to go to Configuration and choose their language. <!-- src: transcript/deployment-infrastructure#first-run-activation-flow -->

First launch runs the License Wizard, which accepts the key via paste or clipboard button; successful activation binds the license to the machine's hardware ID. <!-- src: transcript/deployment-infrastructure#first-run-activation-flow -->

The first-launch flow is designed to be self-explanatory — the user is asked "I don't have a key, do you want to start the wizard?" → paste key from email → activate. <!-- src: transcript/deployment-infrastructure#first-run-activation-flow -->

A project confirmation dialog appears on every startup, asking the user to verify they are still working on the currently configured project number. <!-- src: transcript/deployment-infrastructure#first-run-activation-flow -->

## Shopify Purchase Flow

Onsite has a product page on the GeoDin website; customers add it to cart and check out via Shopify. <!-- src: transcript/deployment-infrastructure#shopify-purchase-flow -->

Shopify purchase triggers the license automation in Keygen; customer IDs visible in Keygen are Shopify customer IDs (e.g., "customer ID 3656"). <!-- src: transcript/deployment-infrastructure#shopify-purchase-flow -->

Current Onsite pricing is €0 / free at the moment (for existing GeoDin customers). <!-- src: transcript/deployment-infrastructure#shopify-purchase-flow -->

Anti-abuse check: to prevent random people with disposable Gmail addresses from getting free Onsite, only existing GeoDin customers can self-serve. Unknown emails trigger an email to sales for manual approval. <!-- src: transcript/deployment-infrastructure#shopify-purchase-flow -->

## File Delivery Configuration (Onsite)

File delivery is configured via `Configuration > Integration > File delivery`. <!-- src: transcript/deployment-infrastructure#file-delivery-configuration-onsite -->

Options: `No delivery` (default, local-only standalone mode), `Shared network folder`, and `Folder plus equal IDs` (behaves nearly identically to shared folder). <!-- src: transcript/deployment-infrastructure#file-delivery-configuration-onsite -->

The `Shared network folder` path is set via `Browse` in the Folders tab and supports the same shortcut codes as other paths (`[my documents]`, etc.). <!-- src: transcript/deployment-infrastructure#file-delivery-configuration-onsite -->

Shared folder can be a local path, mapped network drive, or a cloud-sync folder (Dropbox, Google Drive, OneDrive, SharePoint, P: drive, X: drive). Onsite simply reads/writes files to the configured path and relies on the external sync client. <!-- src: transcript/deployment-infrastructure#file-delivery-configuration-onsite -->

Synchronization of the shared delivery folder is out of scope for Onsite — Onsite does not know or care how the folder is synced. <!-- src: transcript/deployment-infrastructure#file-delivery-configuration-onsite -->

The shared delivery folder must not point to the `%APPDATA%` working folder or to the folder used for the local photocopy of delivered files; Onsite may warn about this but should not be configured that way. <!-- src: transcript/deployment-infrastructure#file-delivery-configuration-onsite -->

A `Make a local copy of delivered` option in shared-folder delivery preserves a local backup of every published form (GDOF, PDF, GeoDin ML) for disaster recovery. <!-- src: transcript/deployment-infrastructure#file-delivery-configuration-onsite -->

A local photocopy of any published form is always kept locally (marked internally as a copy, not the "live" version) so that if the cloud sync folder fails (e.g., Google Drive account closed, Dropbox issue), the data is not lost. <!-- src: transcript/deployment-infrastructure#file-delivery-configuration-onsite -->

## Backups & Snapshots

Onsite can take snapshots every 30 seconds or every 2 minutes and retains up to 10 versions (about 5 minutes of work history). Configurable in settings. <!-- src: transcript/deployment-infrastructure#backups-snapshots -->

Backups are accessed via Tools > Restore backups, which lists recent forms and lets the user pick a version to restore. <!-- src: transcript/deployment-infrastructure#backups-snapshots -->

Restore overwrites the active live copy and cannot be undone. <!-- src: transcript/deployment-infrastructure#backups-snapshots -->

Backups are stored in a hidden local folder (the `backups\` subfolder of the working folder); users normally access them via Tools > Restore backups rather than browsing the folder directly. <!-- src: transcript/deployment-infrastructure#backups-snapshots -->

## Data Compatibility Across Versions

Newer Onsite versions can always read data created by older versions (backward compatibility is guaranteed). <!-- src: transcript/deployment-infrastructure#data-compatibility-across-versions -->

Older versions can read forms created by newer versions in most cases but drop data for any tables/pages that did not exist in the old version. <!-- src: transcript/deployment-infrastructure#data-compatibility-across-versions -->

There is currently no warning to the user if they open a form that was created by a newer version than their own. <!-- src: transcript/deployment-infrastructure#data-compatibility-across-versions -->

The license constrains the maximum Onsite version allowed (e.g., "up to 3.99"); the current Onsite version is 1.2, so customers have significant headroom before hitting the version ceiling. <!-- src: transcript/deployment-infrastructure#data-compatibility-across-versions -->

## Multi-User & Network Deployment

Network installation: one shared installation can serve multiple users — all users share the same layouts and dictionaries. <!-- src: transcript/deployment-infrastructure#multi-user-network-deployment -->

Custom data types, modified dictionaries, and custom layouts all live in the syslib folder and must be copied or shared between installations manually when delivering to an external client. <!-- src: transcript/deployment-infrastructure#multi-user-network-deployment -->

When sending data to a client who does not have the same custom dictionaries, the user must also send the `.GSD` dictionary files or the full syslib folder. <!-- src: transcript/deployment-infrastructure#multi-user-network-deployment -->

Configuration file changes (new dictionaries, new filters, new custom data types) can be shared between users by copying the relevant files (e.g., `Sony_Filter.sys` for import filters) between user syslib folders. <!-- src: transcript/deployment-infrastructure#multi-user-network-deployment -->

Updates: if a dictionary file's date has changed (due to user edits), GeoDin updates will NOT overwrite it, preserving user changes. <!-- src: transcript/deployment-infrastructure#multi-user-network-deployment -->

Updates may push new default layouts — if a user edits defaults in place, they risk being overwritten; recommended workflow is to copy defaults to a client-specific folder first. <!-- src: transcript/deployment-infrastructure#multi-user-network-deployment -->

External users may not have permission to modify system data types; Data Types under System Configuration can be read-only for external users. <!-- src: transcript/deployment-infrastructure#multi-user-network-deployment -->

## Consulting & Support

When customers purchase GeoDin they typically receive included consulting hours — can be used for custom table creation, advanced training, and troubleshooting. <!-- src: transcript/deployment-infrastructure#consulting-support -->

Consulting hours example: 10 hours bundled with a typical customer purchase. <!-- src: transcript/deployment-infrastructure#consulting-support -->

## Planned / Upcoming

[PLANNED] Add a warning when a user opens a form created with a newer version of Onsite than the local installation. <!-- src: transcript/deployment-infrastructure#planned-upcoming -->
