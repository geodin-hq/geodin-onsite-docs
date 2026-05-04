# Managing labels

Onsite prints barcoded labels that tie physical samples to digital records. Labels are typically printed from inside a G1 Drilling Report as you collect samples, but Onsite's **Tools menu** also offers utility operations for labelling work outside of a form.

This page covers the label-printing workflow. For printer setup and template customisation, see [Label printing](../configuration/label-printing.md).

## Before you start

Label printing requires a ZPL-compatible thermal printer configured in Configuration → Labels — see [Label printing](../configuration/label-printing.md) for setup. Without a physical printer configured, Onsite offers a **Preview** mode that shows what the label would look like without actually printing.

## Print a sample label from a form

When you've logged a sample on a G1 Drilling Report's Sampling Log page, click the **three-line menu** next to the sample and select **Print Label**. Onsite generates a QR code containing the sample's unique ID combined with project, location, and depth information.

<figure><img src="../.gitbook/assets/image (23).png" alt=""><figcaption></figcaption></figure>

Onsite displays a preview of the label before printing:

<figure><img src="../.gitbook/assets/image (24).png" alt=""><figcaption></figcaption></figure>

From the preview, you can choose:

* **Print** — send the label to the configured main printer using the main label layout
* **Use alternative printer** — print to the secondary printer (useful for hazardous-sample labels or alternative label stock)
* **Use alternative label layout** — use the second configured template (for example, a hazard-marked version)

Affix the printed label to the physical sample container.

{% hint style="info" %}
The button names "alternative printer" and "alternative label layout" are customisable — you can rename them to match your actual setup (e.g. "red labels", "hazardous layout"). See [Label printing → Custom button labels](../configuration/label-printing.md).
{% endhint %}

## Tools menu — label utilities

The Tools menu offers label operations that don't require a form to be open:

### Sample labels

Print a single sample label directly — without going through a form. Useful when you need to pre-print labels ahead of a field trip, or re-print a label that was damaged in transit.

### Label duplicator

Scan an existing printed label with your device's camera, specify how many copies you want, and Onsite reprints them. Useful when a sample needs to go into multiple containers, each needing its own label.

### Crate labels

Create labels for sample crates or boxes — the containers that hold multiple samples. Crate labels are typically larger than individual sample labels and can include summary information for the crate's contents.

### Shelf labels

Create labels for warehouse shelves where samples are stored. Useful for sample-storage organisation in a lab facility.

## Label design

The visual design of every label — layout, logo, font size, QR code placement — is defined by a ZPL template file. Default templates ship with Onsite; custom templates can be created in **Zebra Designer** (a free tool from Zebra) or any ZPL-capable editor. See [Label printing → Label templates](../configuration/label-printing.md) for customisation details.

***

**See also**

* [Label printing](../configuration/label-printing.md) — printer setup, label templates, logo customisation
* [Soil sampling](soil-sampling.md) — defining samples inside G1 drilling reports
* [Sample picture log](sample-picture-log.md) — photographing samples
