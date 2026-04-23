# Label printing

GeoDin Onsite can print barcoded sample labels directly from your field forms, giving every sample a unique traceable ID. This page covers the Labels tab in Configuration — printer setup and label customisation. For the actual label-printing workflow, see [Managing labels](../guides/managing-labels.md).

## Printer technology

Onsite prints labels in **ZPL** (Zebra Programming Language), an industry-standard language for thermal label printers. The Zebra brand is the market leader, but any printer advertising ZPL compatibility should work.

{% hint style="danger" %}
Windows print queues — including "Microsoft Print to PDF" — are **not** ZPL compatible and will not print labels correctly, even though they may appear in Onsite's printer dropdown. You need an actual ZPL-compatible thermal printer.
{% endhint %}

## Configuring printers

Onsite lets you configure **two printers** — a main printer and an alternative printer. This covers common field and lab use cases:

* A laboratory with white labels on one printer and red labels (for hazardous samples) on another
* Different label sizes — small labels for vials, large labels for containers
* A backup printer for when the main one is busy

Set them in Configuration → Labels:

* **Main printer** — the default printer for regular labels
* **Alternative printer** — a secondary printer, selected per-label when needed
* **No printer** — disables printing
* **Preview** — shows the label on screen without actually printing; useful for testing label templates

## Custom button labels

If "Alternative printer" and "Alternative label layout" don't describe your setup meaningfully, rename them. Onsite lets you replace the default text on the printer toggle and label-layout toggle buttons. For example:

* "Use alternative printer" → "Use printer next door"
* "Use alternative label layout" → "Use hazardous layout"

Custom names live in the Labels tab settings. A clearer button label saves confusion in the field.

## Label templates

Onsite ships with default label templates stored in the installation folder at `<install>\assets\labels\` (read-only). The defaults produce a 2″ × 2″ label (approximately 50 × 50 mm) with the GeoDin logo and standard sample identification fields.

### Two template slots

You can configure two templates — main and alternative — matching the two-printer setup. The main is for everyday labels; the alternative covers a second use case like hazardous-sample labelling.

### Customising a template

To use a custom label design:

1. Copy the default `.zpl` file from the installation folder to your [working folder](../core-concepts/folder-structure.md). Rename it, for example `my-qr.zpl`.
2. Edit the file to match your design. The template uses `{field}` placeholders for sample data — project number, location, depth, barcode text, and other values Onsite fills in at print time.
3. In Configuration → Labels, set the label template filename to your custom file (`my-qr.zpl`).

Onsite uses the file from your working folder in preference to the default.

{% hint style="info" %}
**Zebra Designer** is a free visual tool from Zebra for designing labels. Design the layout graphically, then save it as a `.zpl` file ready to use with Onsite.
{% endhint %}

## Logo customisation

The default label template includes the GeoDin logo. To replace it with your organisation's logo:

1. Prepare a PNG image of your logo. The default logo is 478 × 376 pixels — match the aspect ratio closely for best results. Use a white background.
2. Save the file as `logo.png` in your [working folder](../core-concepts/folder-structure.md).
3. The logo applies immediately — no restart needed.

The same `logo.png` is also used on exported PDFs of forms, keeping your branding consistent across labels and reports.

## Sample ID format

Every sample gets an automatic unique identifier consisting of a prefix, a timestamp-encoded section, and a random suffix. By default the prefix is a single letter, but you can customise it to 1–3 letters to match your organisation's sample-identifier convention.

***

**See also**

* [Managing labels](../guides/managing-labels.md) — the label tools in the Tools menu
* [Soil sampling](../guides/soil-sampling.md) — taking samples in G1 forms
* [Folder structure](../core-concepts/folder-structure.md) — where logo and template files live
