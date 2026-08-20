---
layout: editorial
---

# G1 drilling report

After installing GeoDin Onsite and activating your license, you can create a G1 drilling report. GeoDin Onsite supports multiple standards for G1 drilling reports, as well as the ISO 22475 field standard for the SEP3 Report. In this tutorial, we'll use the G1 standard as an example.

If you haven't completed the basic setup yet, see [Installation & licensing](../documentation/installation-and-licensing.md) and [First steps](../documentation/first-steps.md) for orientation.

## 1. Configure the project standard

To begin, configure the standard for your project:

1. Open the GeoDin Onsite application.
2. Click **Configuration** from the menu to open the configuration window.

<figure><img src="../.gitbook/assets/image (7).png" alt=""><figcaption></figcaption></figure>

3. Navigate to the **Integration** tab.

<figure><img src="../.gitbook/assets/image (1) (1).png" alt=""><figcaption></figcaption></figure>

4. Click the settings button under **Geo-data delivery**. This opens a settings window. GeoDin Onsite supports multiple standards. By default, the standard is set to BS 5930 / Clark and Walker.

<figure><img src="../.gitbook/assets/image (2) (1).png" alt=""><figcaption></figcaption></figure>

5. After selecting the appropriate standard, click **Close** in the Geo-data delivery window, then click **OK** in the configuration window.

See [Geo-data standards](../configuration/geo-data-standards.md) for the full list of supported standards and the consequences of changing a standard later.

## 2. Project setup

1. In the configuration dialog box, select the **Project** tab to enter your project-specific details.

<figure><img src="../.gitbook/assets/image (19).png" alt="" width="563"><figcaption></figcaption></figure>

2. These entries automatically appear on all forms associated with the project, keeping your data consistent.
3. The project number must follow these formatting rules to ensure compatibility with file storage and system operations:

* **Allowed characters**: letters, numbers, hyphens (`-`), and underscores (`_`)
* **Not allowed**: spaces or special characters (e.g. `*`, `@`, `#`)

{% hint style="danger" %}
**Important:** Special characters such as asterisks (`*`) are automatically converted to underscores. GeoDin Onsite stores forms in folders named after the project number, and certain symbols are restricted by the operating system.
{% endhint %}

See [Project setup](../configuration/project-setup.md) for full details on the two project-metadata modes (manual vs. GeoDinML-driven).

## 3. Create a G1 drilling report

1. From the menu, select **New Form**.

<figure><img src="../.gitbook/assets/image (3) (1).png" alt=""><figcaption></figcaption></figure>

2. In the New Form window, choose **G1 Drilling Report**.

<figure><img src="../.gitbook/assets/image (4) (1).png" alt=""><figcaption></figcaption></figure>

3. The G1 report consists of eight default pages. Fill in the required information based on your project needs.

<figure><img src="../.gitbook/assets/image (4).png" alt=""><figcaption></figcaption></figure>

### 3.1 Managing drilling report parameters

1. **Accessing the options menu**

* Click on the second page, **Design**, to start customising the borehole drilling report.
* Click the **three-line menu** (highlighted in red) on the side of the borehole design box to display the available options.

<figure><img src="../.gitbook/assets/image (5).png" alt=""><figcaption></figcaption></figure>

2. **Input methods**

* **Open Builder** - launch the builder to enter borehole design parameters in a structured interface.
* **Direct Entry** - alternatively, input values directly into the respective fields.

<figure><img src="../.gitbook/assets/image (6).png" alt=""><figcaption></figcaption></figure>

3. **Mandatory vs. optional fields**

* Fields highlighted in **red** are **mandatory**.
* All other fields are **optional** - fill them as required by the project.

<figure><img src="../.gitbook/assets/image (3) (2).png" alt=""><figcaption></figcaption></figure>

4. **Row management**

* **Insert row above/below** - add a new row above or below the current one.
* **Delete row** - remove the selected row if no longer needed.

5. **Depth auto-population**\
   After completing a "From" and "To" depth entry, clicking on the next row automatically populates the depth values, ensuring continuity.

6. Once completed, click the validate button <img src="../.gitbook/assets/image (11).png" alt="" data-size="line"> in the upper-left corner, or select **Validate** from the menu.

* If any information is missing or incorrect, the Invalidation window lists the relevant messages.

<figure><img src="../.gitbook/assets/image (6) (1).png" alt=""><figcaption></figcaption></figure>

* If all information is correct, validation completes successfully.

<figure><img src="../.gitbook/assets/image (8).png" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
You can only export the form after it passes validation. However, you can save your progress at any time.
{% endhint %}

### 3.2 Customising which pages appear

The default eight pages of the G1 Drilling Report cover most scenarios, but you can switch pages on and off based on what your project actually needs. Under the form's logo, use **Show/hide pages** to open the page selector.

For example, if you're not collecting SPT readings, hide the SPT page. If you're not logging rock layers, hide the rock page. The selector also lets you **reorder pages** via up/down arrows - useful for matching your preferred data-entry sequence.

These choices are saved with the form; you typically set them once at the start of a project.

## 4. Export the report

1. From the menu, select **Export > GeoDin**.

<figure><img src="../.gitbook/assets/image (17).png" alt=""><figcaption></figcaption></figure>

<div align="center"><figure><img src="../.gitbook/assets/image (10).png" alt=""><figcaption></figcaption></figure></div>

2. Select a location to save the file.
3. GeoDin Onsite generates a GeoDinML file, for example:

&#x20;      `Delft001_G1DR_20260423.geodinml`

If you have [file delivery](../core-concepts/file-delivery-and-ownership.md) configured, use **Publish** instead of Export. Publish pushes the deliverables to your shared folder and handles PDF generation automatically. See [Publishing & retrieving forms](publishing-and-retrieving.md).

## 5. Import into GeoDin

To import the report into GeoDin, use its GeoDinML import feature. Full instructions - including workflows for different data types - live in the [GeoDin documentation](https://docs.geodin.com). Once imported, your drilling data is available for layouts, cross-sections, plates, and reports.

## Form bundles: G1 + Sample Picture Log

Alongside the standalone G1 Drilling Report, Onsite offers **G1 Drilling Report + Sample Picture Log** as a form bundle. The bundle pairs the drilling log with a dedicated page for sample photographs, and the two sections stay linked - the SPL part automatically pulls the sample list from the drilling report, so you don't re-scan or re-enter samples.

Choose the bundle from the New Form dialog when you want drilling data and sample photos to travel together as a single `.gdob` file. See [Sample picture log](sample-picture-log.md) for photo workflow details.

***

**See also**

* [Soil sampling](soil-sampling.md) - logging soil samples within the G1 form
* [Sample picture log](sample-picture-log.md) - photographing samples
* [Exporting to GeoDin](exporting-to-geodin.md) - all export formats
* [Publishing & retrieving forms](publishing-and-retrieving.md) - team workflow
