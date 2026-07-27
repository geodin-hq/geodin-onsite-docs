# First steps

You've installed GeoDin Onsite and activated your license. This page walks through creating your first form end-to-end - just enough to see the full workflow from start to finish in about ten minutes. For deeper coverage of any step, follow the links.

## Before you start

Open Onsite. The first thing you'll see is the **project number confirmation box** - Onsite configures itself for one project at a time, and every form you create belongs to that project.

If a project number is already filled in from a previous session or from [Configuration > Project](../configuration/project-setup.md), click OK. Otherwise enter one now. Project numbers can contain letters, numbers, hyphens (`-`), and underscores (`_`) - no spaces or special characters.

## 1. Start a new form

From the main menu, click **New Form**. In the dialog, choose **G1 Drilling Report** - it's the most common form type and the one we'll use as an example here.

## 2. Enter the basics

The G1 Drilling Report is a multi-page form. Start with the first page and fill in:

* **Location identifier** (for example, `BH-1`)
* **Drilling method** - choose from the dropdown
* At least one row on the **borehole design** page (from-to depth, method)

Fields highlighted in **red** are mandatory. Fields shown in black are optional - you can leave them for now.

{% hint style="info" %}
If your device has a GPS chip or an external Bluetooth GPS receiver, you can use **Record position** to capture coordinates automatically. See [GPS & coordinates](../configuration/gps-and-coordinates.md) to configure your GPS source.
{% endhint %}

## 3. Validate

Click the **Validate** button (the ticks icon, top-left of the form). Onsite checks that every mandatory field is complete and shows the results:

* If the form is valid, the Invalidation window closes cleanly and you can move on.
* If something is missing, Onsite lists the errors. Fix them and validate again.

## 4. Export to GeoDin

From the main menu, click **Export** > **GeoDin** and choose where to save the file.

Onsite creates a **GeoDinML file** - a structured XML file ready to import into GeoDin. The filename follows the standard pattern, for example `BH-1_G1DR_20260423.geodinml`.

{% hint style="info" %}
If you have [file delivery](../core-concepts/file-delivery-and-ownership.md) configured, use **Publish** instead of Export. Publish sends the file to your team's shared folder automatically and generates a PDF alongside the GeoDinML.
{% endhint %}

## 5. Import into GeoDin (optional)

Open GeoDin and use its GeoDinML import feature to bring the file into your database. The full GeoDin workflow is covered in the [GeoDin documentation](https://docs.geodin.com).

***

That's it - you've completed the core loop: **configure > create > validate > export**.

## What's next

Now that you've seen the shape of the workflow, dig into the details:

* [G1 drilling report](../guides/g1-drilling-report.md) - comprehensive coverage of every page and option in the G1 form
* [Exporting to GeoDin](../guides/exporting-to-geodin.md) - all the export formats Onsite supports
* [Core concepts](../core-concepts/forms-and-projects.md) - the mental model behind forms, projects, and file delivery
