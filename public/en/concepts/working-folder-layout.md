---
description: Working Folder Layout
---

<!--
**Content status:** Auto-assembled from product documentation
**Source quality:** B (Moderate (single source type))
**Needs:** editorial review
-->

# Working Folder Layout

## Working Folder / AppData Layout

Two installation modes: `All users` (requires local admin, installs to `C:\Program Files\GeoDin.Onsite\`) and `Local` (per-user, no admin, default `%LOCALAPPDATA%\Programs\GeoDin.Onsite\`). <!-- src: transcript/field-data-collection#working-folder-appdata-layout -->

The runtime working folder is always `%APPDATA%\Roaming\GeoDin.Onsite\` — hard-coded and cannot be relocated (unlike Gaia Forms, which allowed custom working-folder locations). <!-- src: transcript/field-data-collection#working-folder-appdata-layout -->

`%APPDATA%` is invisible by default in Windows; users can unhide via View > Show hidden items, or navigate via the address bar by typing `%appdata%`. <!-- src: transcript/field-data-collection#working-folder-appdata-layout -->

Working folder contents after use: <!-- src: transcript/field-data-collection#working-folder-appdata-layout -->

The installation folder contains DLLs and default versions of configuration/asset files (ZPL templates, default logo). These are read-only — customization is done by copying files into the working folder and editing the copies. <!-- src: transcript/field-data-collection#working-folder-appdata-layout -->

Never edit files directly in the installation folder — always copy to `%APPDATA%\Roaming\GeoDin.Onsite\` first. <!-- src: transcript/field-data-collection#working-folder-appdata-layout -->

A customized set of files (`config.xml`, custom `logo.png`, custom ZPL files) can be distributed to other users as a one-time copy to pre-configure installations. `config.xml` must not be pointed at a shared network location — each user needs their own copy. The `[my documents]` placeholder keeps `config.xml` shareable because it does not hardcode the user name. <!-- src: transcript/field-data-collection#working-folder-appdata-layout -->

To customize the logo printed on forms, place a custom `logo.png` in `%APPDATA%\Roaming\GeoDin.Onsite\`. The file must match the default aspect ratio (478 × 376 px) and have a white background. <!-- src: transcript/field-data-collection#working-folder-appdata-layout -->

The working folder can be opened quickly via Configuration > Folders > Open local folder. <!-- src: transcript/field-data-collection#working-folder-appdata-layout -->
