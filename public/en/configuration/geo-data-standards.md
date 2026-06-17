# Geo-data standards

A **geo-data standard** defines the schema for describing drilling, sampling, and layer data - what columns exist, what values are allowed, what units are used. Different countries and industries use different standards. Onsite supports several of them and lets you choose the right one for each project.

Standards are configured in Configuration → Integration → Geo-data delivery, via the ⚙️ settings button.

## Supported standards

This version of Onsite supports five standards. When you select one, Onsite also asks you to pick the relevant **description types** associated with it - the specific logging conventions your project uses.

<figure><img src="../.gitbook/assets/image (28).png" alt=""><figcaption></figcaption></figure>

## Choose your standard before starting

Decide on the standard **before** you create any forms for a project. Standards affect which fields appear, how data is entered, and what the exported GeoDinML will look like - they need to be correct from day one.

{% hint style="danger" %}
**Once a standard is applied and the project has active forms, it cannot be changed retroactively.** If you realise you've picked the wrong standard after creating forms, you'll need to start a new project with the correct standard.
{% endhint %}

## The standards tab is locked when forms are open

If any forms are currently open in Onsite, the geo-data delivery tab is locked - you cannot change the standard while forms are being edited.

{% hint style="info" %}
If you see this error, close all open forms and try again.

<p align="center"><img src="../.gitbook/assets/image (30).png" alt=""></p>
{% endhint %}

***

**See also**

* [Project setup](project-setup.md) - configure the project this standard applies to
* [Exporting to GeoDin](../guides/exporting-to-geodin.md) - how your standard shapes the GeoDinML export
