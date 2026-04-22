---
description: Label Template Design
---

<!--
**Content status:** Auto-assembled from product documentation
**Source quality:** B (Moderate (single source type))
**Needs:** editorial review
-->

# Label Template Design

## Label Printing & ZPL Templates

Default label templates ship in the installation folder under `assets/labels/` (ZPL label templates). <!-- src: transcript/forms-templates-customization#label-printing-zpl-templates -->

The default label template is `QR.zpl`; a hazardous variant (`QR` for hazard) shows a warning `!` symbol in place of the logo. <!-- src: transcript/forms-templates-customization#label-printing-zpl-templates -->

Default label template ships at 2 inches x 2 inches (50.8 mm / 5 cm square). Label printers are typically available in 2-inch, 3-inch, or 4-inch (10 cm) widths. Labels can be rectangular, not just square. <!-- src: transcript/forms-templates-customization#label-printing-zpl-templates -->

To customize a label template: copy the default ZPL file from `assets/labels/`, rename it (e.g., `myQR.zpl`), place it loose in `%APPDATA%\Roaming\GeoDin.Onsite\`, and set its name in `Configuration > Labels`. <!-- src: transcript/forms-templates-customization#label-printing-zpl-templates -->

ZPL templates use placeholder fields in square brackets that Onsite replaces at print time: contract number, project number, location number, sample type, sample number, depths, barcode text, and others. <!-- src: transcript/forms-templates-customization#label-printing-zpl-templates -->

Label templates can be designed using the Zebra Designer application and exported as `.ZPL`. <!-- src: transcript/forms-templates-customization#label-printing-zpl-templates -->

Onsite supports two label templates at the same time: a **main** template and an **alternative** template (originally intended for hazardous samples). The printed label can use either template per print action via a checkbox in the print dialog. <!-- src: transcript/forms-templates-customization#label-printing-zpl-templates -->

Onsite drives label printers via the ZPL (Zebra Printer Language) protocol. Zebra and Toshiba are the main ZPL label-printer manufacturers; cheaper brands such as Pixelon also advertise as "ZPL compatible". <!-- src: transcript/forms-templates-customization#label-printing-zpl-templates -->

Two printers can be configured simultaneously: a "main printer" and an "alternative printer". Use cases: white vs red labels (red for contaminated/dangerous samples), or small vs large label sizes. <!-- src: transcript/forms-templates-customization#label-printing-zpl-templates -->

Windows printers (e.g., "Microsoft Print to PDF") will appear in the printer list but will not work for label printing — Windows does not expose ZPL compatibility to Onsite; users must select a truly ZPL-capable printer. <!-- src: transcript/forms-templates-customization#label-printing-zpl-templates -->

Onsite supports a "Preview" mode for labels that renders the label on screen instead of sending it to a printer. <!-- src: transcript/forms-templates-customization#label-printing-zpl-templates -->

The main/alternative template checkbox labels in the print dialog can be customized in `Configuration > Labels` (e.g., rename "use alternative printer" to "use printer next door", or "use alternative label layout" to "use hazardous layout"). <!-- src: transcript/forms-templates-customization#label-printing-zpl-templates -->

Sample labels are printed via `Print label` on the samples page; users can choose per-print which label template (main/alternative) and which printer (main/alternative) to use. <!-- src: transcript/forms-templates-customization#label-printing-zpl-templates -->

Standalone label tools: (1) sample labels (print a label for a sample not tied to a form), (2) label duplicator (scan an existing label, specify how many copies to reprint), (3) crate labels (for boxes containing multiple samples), (4) shelf labels (for warehouse storage shelves). <!-- src: transcript/forms-templates-customization#label-printing-zpl-templates -->

If a location ID or depth is missing, some fields on the printed label will be blank (e.g., depth prints as `00`); missing location ID may suppress the location ID entirely. <!-- src: transcript/forms-templates-customization#label-printing-zpl-templates -->
