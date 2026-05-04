# Publishing & retrieving forms

When your team uses a [shared folder for file delivery](../configuration/file-delivery-setup.md), forms flow between colleagues using **Publish** and **Retrieve**. This page covers the day-to-day mechanics. For the mental model — why the buttons work the way they do — see [File delivery & ownership](../core-concepts/file-delivery-and-ownership.md).

## Before you start

The Publish and Retrieve buttons only appear in Onsite if file delivery is configured. If you don't see them, open Configuration → Integration → File delivery and choose **Shared network folder**. See [File delivery setup](../configuration/file-delivery-setup.md) for the full setup steps.

## Publish an incomplete form

Use **Publish as incomplete** when you've filled in part of a form and need a colleague to finish it — for example, a field crew completing the borehole data and an office engineer adding interpretation.

1. With the form open, click **Publish** from the menu.
2. Choose **Publish as incomplete**.
3. Onsite sends the form's `.gdof` file to your shared folder. No PDF or GeoDinML is produced yet — those only appear on final publish.
4. The form closes and is no longer editable on your device — it's now "on the shelf" for any colleague to retrieve.

{% hint style="info" %}
Your local copy remains on the device as a read-only photocopy — a safety net in case the shared folder becomes unreachable. See [File delivery & ownership](../core-concepts/file-delivery-and-ownership.md).
{% endhint %}

## Retrieve a form from the shared folder

When it's your turn to work on a published-incomplete form:

1. From the main menu, click **Retrieve**.
2. Onsite shows forms currently on the shared folder that are marked incomplete.
3. Pick the form you want. Onsite copies it from the shared folder to your device and clears the shared-folder copy.
4. The form is now yours to edit.

{% hint style="danger" %}
**Update Onsite before retrieving.** If a colleague on a newer version published a form that uses a new field or table, and you retrieve it on an older version, the new data may be silently dropped when you save. Keep everyone on the latest version — see [Updates & version compatibility](../support/updates-and-version-compatibility.md).
{% endhint %}

## Publish a final form

When a form is complete and ready for the office to process:

1. **Validate the form first.** Final publish requires the form to pass validation — see the [G1 drilling report](g1-drilling-report.md) page for validation details.
2. Click **Publish → Publish as final**.
3. Onsite generates all deliverables: the `.gdof`, a final PDF (without the "draft" watermark), a GeoDinML export if the form supports it, and any other configured outputs.
4. All deliverables are pushed to the shared folder.
5. The form on your device becomes read-only. You can view it via **Load Local**, but you cannot edit it.

Once a form is published as final, the office typically imports its GeoDinML into GeoDin Desktop and processes the data further. Your part of the workflow is done.

## Revoke a published form (careful)

Sometimes you realise after publishing that you need to fix something. Onsite offers a **Revoke** button that un-publishes a final form — but this is dangerous.

1. Open the read-only photocopy of the form via **Load Local**.
2. Click **Revoke**. The form becomes editable again and ownership transfers back to you.
3. Make your corrections and publish again.

{% hint style="danger" %}
**Before revoking:**

* **Communicate with whoever receives your forms.** The office may have already imported the GeoDinML and started processing. Revoking doesn't recall that downstream work — you rely on the next person noticing the new version.
* **Don't revoke forms published more than a few hours ago.** Assume they've already been processed.
* Use Revoke as a rare escape hatch, not a routine workflow step.
{% endhint %}

***

**See also**

* [File delivery & ownership](../core-concepts/file-delivery-and-ownership.md) — the mental model behind these buttons
* [File delivery setup](../configuration/file-delivery-setup.md) — shared folder configuration
* [Exporting to GeoDin](exporting-to-geodin.md) — the Export button as an alternative when file delivery isn't used
