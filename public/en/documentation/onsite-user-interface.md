# The Onsite user interface

This page is an orientation tour - where menus live, what each button does, where to find things. Pair it with [First steps](first-steps.md) to actually create a form; this page just gives you the map.

## The main menu

The main menu is your workspace hub. The buttons you'll use most:

| Action | What it does |
|---|---|
| **New Form** | Start a new form. Opens a dialog where you choose the form type (G1 Drilling Report, Sample Picture Log, Picture Log, and others). |
| **Load Local** | Reopen a form you've saved but not yet published. See [Forms & projects](../core-concepts/forms-and-projects.md) for where saved forms live. |
| **Retrieve** | Take a form back from the shared folder onto your device. Only visible once [file delivery is configured](../configuration/file-delivery-setup.md). |
| **Save** | Save the current form. Forms also save automatically when closed or when Onsite exits - you don't have to press Save routinely. |
| **Validate** | Check the current form for errors. Mandatory fields are highlighted in red; any missing fields are listed in the Invalidation window. |
| **Export** | Export the current form as a PDF, a GeoDinML file, or other supported formats. See [Exporting to GeoDin](../guides/exporting-to-geodin.md). |
| **Publish** | Send the current form to the shared folder. Only visible once file delivery is configured. See [File delivery & ownership](../core-concepts/file-delivery-and-ownership.md). |

## The Configuration menu

Configuration is organised into tabs, each controlling a related group of settings:

| Tab | What it controls |
|---|---|
| **Project** | Project metadata - project number, client name, client number. Two modes: manual entry, or driven by a GeoDinML file. [Details](../configuration/project-setup.md) |
| **Integration** | Geo-data delivery standards + file delivery mode. [Standards](../configuration/geo-data-standards.md), [File delivery](../configuration/file-delivery-setup.md) |
| **Defaults** | Default values that auto-fill into new forms - foreman, rig number, unit system, coordinate system, and more. [Details](../configuration/form-defaults.md) |
| **Backups** | Automatic backup frequency and retention. [Details](../configuration/backups.md) |
| **Labels** | Label printer selection, label templates, logo customisation. [Details](../configuration/label-printing.md) |
| **Camera** | Camera source and resolution for photo capture. [Details](../configuration/camera.md) |
| **GPS** | GPS source - built-in, Bluetooth, manual entry, or Windows-based. [Details](../configuration/gps-and-coordinates.md) |
| **Folders** | Default export folder path and a shortcut button to **Open local folder** (your [working folder](../core-concepts/folder-structure.md)). |
| **Language & UI** | UI language (English, German, and others) and the on-screen keyboard toggle for tablets. |

## The Tools menu

The Tools menu holds utility operations - actions you run occasionally rather than during regular form filling:

* **Sample labels** - print a single sample label directly, without going through a form
* **Label duplicator** - scan an existing printed label and reprint N copies of it
* **Crate labels** - create labels for sample crates or boxes
* **Shelf labels** - create labels for warehouse shelves
* **Restore backups** - open the backup browser to restore a previous version of a form

See [Managing labels](../guides/managing-labels.md) for the label tools and [Backups](../configuration/backups.md) for restore.

## The question-mark menu

Click the **?** icon in the menu bar for:

* **About** - version information
* **Licensing** - reopen the license manager to enter a new key or check licence status
* **Open log files** - open the `logs/` folder in Windows Explorer, useful when [contacting support](../support/troubleshooting.md)
* **Contact support** - opens the GeoDin support site in your browser
* **Online help** - opens this documentation site

## The on-screen keyboard

If you're using a tablet without a physical keyboard, enable the on-screen keyboard via Configuration > Language & UI. The keyboard appears whenever a text field gains focus and is designed to keep out of the way during field-form data entry.

***

**See also**

* [First steps](first-steps.md) - walk through your first form
* [Forms & projects](../core-concepts/forms-and-projects.md) - how Onsite organises your work
