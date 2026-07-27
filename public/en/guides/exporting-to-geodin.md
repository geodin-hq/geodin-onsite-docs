# Exporting to GeoDin

Every form you create in GeoDin Onsite eventually needs to reach your team - either for further processing in GeoDin or as a deliverable for a client. Onsite offers two ways of handing data off:

* **Export** - save deliverables to a folder you choose, then transfer manually (email, USB drive, etc.)
* **Publish** - push deliverables automatically to a [shared folder](../configuration/file-delivery-setup.md) your team already syncs

This page covers Export. For Publish, see [Publishing & retrieving forms](publishing-and-retrieving.md).

## When to use Export vs Publish

Export is the simplest mode - it doesn't require any setup. Use it when:

* You don't have a shared folder configured
* You want to send a form ad-hoc by email or USB drive
* You need a one-off PDF for a client

Publish is for teams who work with field-to-office workflows routinely - see the [File delivery & ownership](../core-concepts/file-delivery-and-ownership.md) concept page for why you might want it.

## Export formats

From the Export menu, Onsite offers:

* **GeoDinML** - a structured XML file ready to import into GeoDin. Produced for drilling and sampling forms.
* **PDF** - a printable document. Every exported PDF is watermarked "draft" unless it was produced via **Publish as final** (see below).

Which forms produce GeoDinML:

| Form | GeoDinML | PDF | Original image files |
|---|---|---|---|
| G1 Drilling Report | ✓ | ✓ | - |
| ISO 22475 SEP 3 | ✓ | ✓ | - |
| Picture Log | - | ✓ | ✓ |
| Sample Picture Log | - | ✓ | ✓ |
| G1 + SPL bundle | ✓ (drilling part) | ✓ (combined) | ✓ (photos) |

## Export to GeoDin

1. With the form open and validated, click **Export > GeoDin** from the menu.
2. Choose where to save the file.
3. Onsite generates a `.geodinml` file using the standard naming convention: `<Location>_<FormCode>_<Date>.geodinml` - for example, `BH-1_G1DR_20260423.geodinml`.

## Export to PDF

1. Click **Export > PDF**.
2. Choose a save location.
3. Onsite generates the PDF.

{% hint style="info" %}
**Why does the PDF say "draft"?**

Every PDF exported via the Export button carries a "draft" watermark. This is deliberate - PDFs are easy to share, and a watermark prevents an in-progress form from being mistaken for a final deliverable.

The only way to get an un-watermarked PDF is through [Publish as final](publishing-and-retrieving.md), which requires the form to pass validation first.
{% endhint %}

## Import into GeoDin

Once you have a `.geodinml` file, open GeoDin and use its GeoDinML import feature to bring the file into your database. Full GeoDin instructions - including specific import workflows for different data types - live in the [GeoDin documentation](https://docs.geodin.com).

From an ecosystem perspective, importing your Onsite forms into Desktop is where the data becomes reusable - layered into your database, combined with data from other forms and other projects, and used as the basis for plates, cross-sections, and reports.

***

**See also**

* [Publishing & retrieving forms](publishing-and-retrieving.md) - the shared-folder alternative to manual export
* [G1 drilling report](g1-drilling-report.md) - the form producing most of your GeoDinML output
* [Sample picture log](sample-picture-log.md) - photo-form outputs
