---
description: Soil Sampling (Onsite)
---

<!--
**Content status:** Auto-assembled from product documentation
**Source quality:** B (Moderate (single source type))
**Needs:** editorial review
-->

# Soil Sampling (Onsite)

## 1. Managing Soil Parameters

To begin managing soil parameters, select **Option 5** in the **G1 Drilling Report**. This will open the **Sampling Log** page for your project as seen below.

When you click on the **From Depth** field, a builder window will open, allowing you to enter all relevant test details. Calculations for the **To Depth** will be performed automatically once the penetration value is entered in centimeters.

## 2. QR Code

#### **Configuring the Printer:**

* First, navigate to **Configuration** and select **Labels**. Choose the printer you want to use for printing.
* You can configure which printer to use for label printing. The system allows you to select **two printers**:

  + **Main Printer** – The default printer for standard labels.
  + **Alternative Printer** – A backup or specialized printer for specific cases.

  This flexibility is useful for clients who:

  + Operate in laboratories and need different label types (e.g., **white labels** for regular samples and **red labels** for hazardous or contaminated samples).
  + Require different sizes of labels (e.g., **small labels** for vials and **large labels** for containers).

#### Label Generation:

* To print a QR code for a specific sample, click on the **three-line menu** next to the sample and select **Print Label**.
* The system will automatically generate a QR code containing the sample’s unique identifier (ID), which can then be affixed to the sample for easy tracking and scanning.

* As shown below, a **preview of the label** is generated, including the QR code for the selected sample.

#### Recommended Printer

For the smoothest experience, we recommend the **Zebra ZQ600 Series mobile thermal label printer**.

👉 Buy or view details: [Zebra ZQ600 Seriesarrow-up-right](https://www.zebra.com/us/en/products/printers/mobile/zq600-series.html)

Other, equivalent thermal label printers may also work, but this model has been fully tested with GeoDin Onsite.

---

## Additional content from product documentation

## Sample Workflow & QR Codes

Sample workflow on a drilling form: select sampling method (e.g., liner tube 4-inch), condition (e.g., undisturbed), recovery percentage (e.g., 95%+), sample type, depth reference, then print a QR-coded label that can be stuck on the physical sample. <!-- src: transcript/field-data-collection#sample-workflow-qr-codes -->

Each soil sample is given a unique ID with the structure: 1 fixed prefix letter (configurable) + 6 characters encoding a timestamp + 4 random characters. <!-- src: transcript/field-data-collection#sample-workflow-qr-codes -->

Prefix length is adjustable: if extended to 2 or 3 characters, the random section shrinks to 3 or 2 characters respectively (prefix + random is always 5 characters total). <!-- src: transcript/field-data-collection#sample-workflow-qr-codes -->

The timestamp portion of the sample ID changes every second, so collisions only happen if more than ~20–100 samples are generated in the exact same second. <!-- src: transcript/field-data-collection#sample-workflow-qr-codes -->

QR code label scanning: when attaching a picture to a sample in a standalone Sample Picture Log form, the user first scans the sample's printed QR label; Onsite then knows all sample details and lets the user add pictures. <!-- src: transcript/field-data-collection#sample-workflow-qr-codes -->

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
