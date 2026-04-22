---
description: Label Printing ZPL
---

<!--
**Content status:** Auto-assembled from product documentation
**Source quality:** B (Moderate (single source type))
**Needs:** editorial review
-->

# Label Printing ZPL

## Label Printer Integration (ZPL)

Onsite drives label printers using the ZPL (Zebra Printer Language) protocol — an industry-standard language. <!-- src: transcript/api-integrations#label-printer-integration-zpl -->

Zebra and Toshiba are the main ZPL label-printer manufacturers; cheaper brands such as Pixelon also advertise as "ZPL compatible". <!-- src: transcript/api-integrations#label-printer-integration-zpl -->

Non-Zebra printers that support ZPL also work, though most users will use Zebra hardware. <!-- src: transcript/api-integrations#label-printer-integration-zpl -->

Windows printers (e.g., "Microsoft Print to PDF") appear in the printer list but do NOT work for label printing — Windows does not expose ZPL compatibility to Onsite, so users must pick a truly ZPL-capable printer. <!-- src: transcript/api-integrations#label-printer-integration-zpl -->

Two printers can be configured simultaneously: a "main printer" and an "alternative printer" (use cases: white labels vs red labels for hazardous/contaminated samples, or small vs large label sizes). <!-- src: transcript/api-integrations#label-printer-integration-zpl -->

Onsite supports two label templates at the same time: the main template and an alternative template; per-print dialog lets the user choose which template and which printer to use. <!-- src: transcript/api-integrations#label-printer-integration-zpl -->

Label templates are ZPL files stored in the Onsite configuration; fully customizable by the user (size, logo, data placement, QR code position and size). <!-- src: transcript/api-integrations#label-printer-integration-zpl -->

Default label template ships at 2 inches × 2 inches (50.8 mm / 5 cm square); label printers are typically available in 2", 3", or 4" (10 cm) widths; labels can be rectangular as well as square. <!-- src: transcript/api-integrations#label-printer-integration-zpl -->

Default templates ship in the installation folder under `assets/labels/` (e.g., `QR.zpl` and a hazardous variant showing a warning `!` symbol in place of the logo). <!-- src: transcript/api-integrations#label-printer-integration-zpl -->

Customization workflow: copy the default ZPL file, rename it (e.g., `myQR.zpl`), place it loose in `%APPDATA%\Roaming\GeoDin.Onsite\`, and set its name in `Configuration > Labels`. <!-- src: transcript/api-integrations#label-printer-integration-zpl -->

ZPL templates use placeholder fields in square brackets that Onsite replaces at print time: contract number, project number, location number, sample type, sample number, depths, barcode text, and others. <!-- src: transcript/api-integrations#label-printer-integration-zpl -->

Label templates can be designed using the Zebra Designer application and exported as `.ZPL`. <!-- src: transcript/api-integrations#label-printer-integration-zpl -->

The labels for main/alternative template checkboxes in the print dialog can be customized in `Configuration > Labels` (e.g., rename to "use printer next door" or "use hazardous layout"). <!-- src: transcript/api-integrations#label-printer-integration-zpl -->

Onsite supports a "Preview" mode that renders the label on screen instead of sending it to a printer. <!-- src: transcript/api-integrations#label-printer-integration-zpl -->

If a location ID or depth is missing, some fields on the printed label will be blank (e.g., depth prints as `00`). <!-- src: transcript/api-integrations#label-printer-integration-zpl -->
