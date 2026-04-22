---
description: Working Folder and Config
---

<!--
**Content status:** Auto-assembled from product documentation
**Source quality:** B (Moderate (single source type))
**Needs:** editorial review
-->

# Working Folder and Config

## Desktop Folder Layout

Typical installation path: `C:\ProgramData\GeoDin\`. <!-- src: transcript/deployment-infrastructure#desktop-folder-layout -->

System library (syslib) folder: `C:\ProgramData\GeoDin\System\` — contains all dictionaries and customizations. <!-- src: transcript/deployment-infrastructure#desktop-folder-layout -->

Layouts folder: `C:\ProgramData\GeoDin\Layouts\` — default layouts ship here, organized by object type. <!-- src: transcript/deployment-infrastructure#desktop-folder-layout -->

Bin folder contains the executable to run GeoDin. <!-- src: transcript/deployment-infrastructure#desktop-folder-layout -->

Syslib folder contains dictionaries (GSD files), import filters (e.g., `Sony_Filter.sys`), custom data type configurations, and other user-editable configuration. <!-- src: transcript/deployment-infrastructure#desktop-folder-layout -->

Demos folder contains sample databases shipped with the installation. <!-- src: transcript/deployment-infrastructure#desktop-folder-layout -->

Dictionaries are stored as individual `.GSD` files, one per list (e.g., `G1_EPSG.GSD` holds the EPSG code list). <!-- src: transcript/deployment-infrastructure#desktop-folder-layout -->

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
