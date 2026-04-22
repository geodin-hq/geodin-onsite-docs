---
layout: editorial
---

# G1 Drilling Report

After installing GeoDin Onsite and activating it with the correct license key, let’s begin by creating a G1 drilling report.

GeoDin Onsite supports multiple standards for G1 drilling reports and ISO 22475 field standard for the SEP3 Report. In this tutorial, we’ll use the G1 standard as an example.

## 1. Configure the Project Standard

To begin, configure the standard for your project:

1. Open GeoDin Onsite application.
2. Click Configuration from the menu to open the configuration window.

<figure><img src="../.gitbook/assets/image (7).png" alt=""><figcaption></figcaption></figure>

3. Navigate to the Integration tab.

<figure><img src="../.gitbook/assets/image (1) (1).png" alt=""><figcaption></figcaption></figure>

4. Click the Settings button under Geo-data delivery. This will open a settings window. GeoDin Onsite supports multiple standards. By default, the standard is set to BS 5930 / Clark and Walker.

<figure><img src="../.gitbook/assets/image (2) (1).png" alt=""><figcaption></figcaption></figure>

5. After selecting the appropriate standard,click Close in the Geo-data delivery window, then click OK in the configuration window.

## 2. Project setup

1. As mentioned above, in the configuration dialog box, select the **"Project"** tab to enter your project specific details.<br>

<figure><img src="../.gitbook/assets/image (19).png" alt="" width="563"><figcaption></figcaption></figure>

2. These entries will automatically appear on all forms associated with the project and help maintain consistency across your data records.&#x20;
3. To ensure compatibility with file storage and system operations, the project number must follow these formatting rules:

* **Allowed characters**: letters, numbers, hyphens (`-`), and underscores (`_`)
* **Not allowed**: spaces or special characters (e.g., `*`, `@`, `#`, etc.)

{% hint style="danger" %}
**Important:** Special characters such as asterisks (`*`) are automatically converted to underscores. This is because GeoDin Onsite stores forms in folders named after the project number, and certain symbols are restricted by the operating system.
{% endhint %}

## 3. Create a G1 Drilling Report

1. From the menu, select New Form.



<figure><img src="../.gitbook/assets/image (3) (1).png" alt=""><figcaption></figcaption></figure>

2. &#x20;In the New Form window, choose G1 Drilling Report.

<figure><img src="../.gitbook/assets/image (4) (1).png" alt=""><figcaption></figcaption></figure>



3. The G1 report consists of eight different pages. Fill in the required information based on your project needs.

<figure><img src="../.gitbook/assets/image (4).png" alt=""><figcaption></figcaption></figure>

#### 3.1 Managing Drilling Report Parameters

1. **Accessing the Options Menu**

* Click on the second page, **Design,** to start customizing the borehole drilling report.&#x20;
* Click the **three-line menu** (highlighted in red) on the side of the borehole design box to display the available options.

<figure><img src="../.gitbook/assets/image (5).png" alt=""><figcaption></figcaption></figure>

2. **Input Methods**

* &#x20;**Open Builder**: Launch the builder to enter borehole design parameters in a structured interface.
* **Direct Entry**: Alternatively, input values directly into the respective fields.

<figure><img src="../.gitbook/assets/image (6).png" alt=""><figcaption></figcaption></figure>

3. **Mandatory vs. Optional Fields**

* Fields highlighted in **red** are **mandatory**.
* All other fields are **optional** and to be filled as per the requirement of the project

<figure><img src="../.gitbook/assets/image (3) (2).png" alt=""><figcaption></figcaption></figure>

4. **Row Management**

* **Insert Row Above/Below**: Add a new row above or below the current one.
* **Delete Row**: Remove the selected row if no longer needed.

5. **Depth Auto-Population**\
   After completing a “From” and “To” depth entry, clicking on the next row will **automatically populate the depth values**, ensuring continuity.
6. Once completed, click validate button <img src="../.gitbook/assets/image (11).png" alt="" data-size="line"> in the upper-left corner, or select Validate from the menu.

* If any information is missing or incorrect, the Invalidation window will display the relevant messages.

<figure><img src="../.gitbook/assets/image (6) (1).png" alt=""><figcaption></figcaption></figure>

* If all information is correct, validation will be successful

<figure><img src="../.gitbook/assets/image (8).png" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
&#x20;Note: You can only export the form after it passes validation. However, you can save your progress at any time.
{% endhint %}

## 4. Export the Report

1. From the menu, select Export → GeoDin.

<figure><img src="../.gitbook/assets/image (17).png" alt=""><figcaption></figcaption></figure>

<div align="center"><figure><img src="../.gitbook/assets/image (10).png" alt=""><figcaption></figcaption></figure></div>

2. Then, select a location to save the file.
3. GeoDin Onsite will generate a GeoDinML file, for example:

&#x20;      Delft001\_G1DR\_20250528.geodinml

## 5. Import into GeoDin

To import the report into GeoDin, please refer to the video tutorial [Import into GeoDin](https://app.gitbook.com/s/Oh9veY55xgALNVUW8siX/data-collection/import/special-imports/import-geodinml).

<br>

