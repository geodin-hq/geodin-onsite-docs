---
description: Label Printing
---

<!--
**Content status:** Auto-assembled from product documentation
**Source quality:** B (Moderate (single source type))
**Needs:** editorial review
-->

# Label Printing

## Label Printing (ZPL / Zebra)

Onsite drives label printers using the ZPL (Zebra Printing Language) protocol. Zebra and Toshiba are the main ZPL label-printer manufacturers; cheaper brands (e.g., Pixelon) also advertise as ZPL-compatible. <!-- src: transcript/field-data-collection#label-printing-zpl-zebra -->

Windows printers (e.g., "Microsoft Print to PDF") appear in the printer list but will not work for label printing — the user must select a truly ZPL-capable printer. <!-- src: transcript/field-data-collection#label-printing-zpl-zebra -->

Two printers can be configured simultaneously: a "main printer" and an "alternative printer". Use cases: white labels vs red labels (red for contaminated/dangerous samples), or small vs large label sizes. <!-- src: transcript/field-data-collection#label-printing-zpl-zebra -->

Onsite supports two label templates at the same time: main + alternative (originally intended for hazardous samples). The printed label can use either template per print action via a checkbox in the print dialog. <!-- src: transcript/field-data-collection#label-printing-zpl-zebra -->

Label checkbox labels in the print dialog can be renamed via Configuration > Labels (e.g., "use alternative printer" → "use printer next door", "use alternative label layout" → "use hazardous layout"). <!-- src: transcript/field-data-collection#label-printing-zpl-zebra -->

Default label template is `QR.zpl`, 2 inches × 2 inches (50.8 mm / 5 cm square). Label printers are available in 2-, 3-, or 4-inch widths; labels can be rectangular, not just square. <!-- src: transcript/field-data-collection#label-printing-zpl-zebra -->

A hazardous label variant shows a warning `!` symbol in place of the logo. <!-- src: transcript/field-data-collection#label-printing-zpl-zebra -->

ZPL templates use placeholder fields in square brackets that Onsite replaces at print time: contract number, project number, location number, sample type, sample number, depths, barcode text, and others. <!-- src: transcript/field-data-collection#label-printing-zpl-zebra -->

Label templates can be designed using the Zebra Designer application and exported as `.ZPL`. <!-- src: transcript/field-data-collection#label-printing-zpl-zebra -->

To customize a label template: copy the default ZPL file from `assets/labels/`, rename it (e.g., `myQR.zpl`), place it loose in the `%APPDATA%\Roaming\GeoDin.Onsite\` folder, and set its name in Configuration > Labels. <!-- src: transcript/field-data-collection#label-printing-zpl-zebra -->

Onsite supports a "Preview" mode that renders the label on screen instead of sending it to a printer. <!-- src: transcript/field-data-collection#label-printing-zpl-zebra -->

Standalone label tools available: (1) sample labels (not tied to a form), (2) label duplicator (scan an existing label, specify copy count), (3) crate labels (for boxes containing multiple samples), (4) shelf labels (for warehouse storage shelves). <!-- src: transcript/field-data-collection#label-printing-zpl-zebra -->

Sample labels are printed via Print Label on the samples page; users choose per-print which label template (main/alternative) and which printer (main/alternative) to use. <!-- src: transcript/field-data-collection#label-printing-zpl-zebra -->

If a location ID or depth is missing, some fields on the printed label will be blank (e.g., depth prints as `00`); a missing location ID may suppress the location ID entirely. <!-- src: transcript/field-data-collection#label-printing-zpl-zebra -->
