# File delivery & ownership

When you work alone on a tablet, Onsite behaves like any ordinary program: you make a form, it saves, it stays on your device. But Onsite is designed for **field-to-office workflows** - drilling crews in the field, engineers in the office, forms moving between them. To make that work safely, Onsite introduces two concepts: **file delivery** and **form ownership**.

Reading this page once will make the Publish / Retrieve / Revoke buttons obvious everywhere else in the product.

## File delivery modes

Onsite offers two ways of handling your data, configured in Configuration → Integration:

* **No delivery** (default) - everything stays on your device. You work alone. When you want to hand data to the office, you [export a `.geodinml` file manually](../guides/exporting-to-geodin.md) and share it by email, USB, or however you like.
* **Shared network folder** - you point Onsite at a folder on your machine that's synchronised with your colleagues (via OneDrive, Dropbox, Google Drive, or any other sync service of your choice). Onsite doesn't care which service you use; it just reads from and writes to that folder.

Once a shared folder is configured, two new buttons appear in the Onsite menu: **Publish** and **Retrieve**. These are the mechanics of handing forms off and picking them up.

{% hint style="info" %}
See [File delivery setup](../configuration/file-delivery-setup.md) for the practical configuration steps. This page covers *why* file delivery works the way it does.
{% endhint %}

## The ownership model: a single piece of paper

The critical idea is that **a form behaves like a single piece of paper**. There is only one of it. It can be in one place at a time, and it belongs to exactly one person at a time.

Picture your team working in an office with:

* **Each person's briefcase** - where the forms they're actively working on live. This is your Onsite installation on your tablet.
* **An "incomplete" shelf** - anyone on the team can put a half-finished form there, and anyone can take it back off.
* **The boss's letterbox** - where finished forms go. Once a form goes through, only the boss can deal with it.

The buttons in Onsite map to this physical analogy:

| Onsite action | Physical analogy |
|---|---|
| **Save** | Put the form in your briefcase |
| **Load local** | Take the form back out of your briefcase |
| **Publish as incomplete** | Put the form on the "incomplete" shelf |
| **Retrieve** | Take a form from the "incomplete" shelf back into your briefcase |
| **Publish as final** | Drop the form through the boss's letterbox |
| **Revoke** | Reach into the letterbox and pull the form back out - see warning below |

At any moment, a form is either in someone's briefcase, on the shelf, or through the letterbox - never in two places. This is how Onsite guarantees that two people can't accidentally overwrite each other's edits.

## Publishing: incomplete vs final

When you publish a form, Onsite asks whether it's **incomplete** or **final**. The choice matters.

**Incomplete** means the form is still being worked on. Only the `.gdof` file itself goes to the shared folder - no PDF, no GeoDinML export is generated yet, because the data isn't final. A colleague can [retrieve](../guides/publishing-and-retrieving.md) the form, fill in the remaining parts, and publish again when they're ready.

**Final** means the form is done. Onsite requires the form to pass validation first. When you publish as final, Onsite generates **all the deliverables** - the `.gdof`, a PDF without the "draft" watermark, a GeoDinML file ready to import into GeoDin Desktop, and any other outputs your project needs. These are pushed to the shared folder, and the office can process them.

After publishing as final, the form on your device is closed and read-only. You can see it in Load Local but cannot edit it - it's the boss's now.

## The disaster-recovery photocopy

Every time you publish a form, Onsite keeps a **local read-only photocopy** in your working folder. This is a safety net for scenarios where the "real" form becomes unreachable - your tablet falls overboard, the shared folder becomes unavailable, the sync service suspends your account - and you still need a record of what you sent.

You can open the photocopy via Load Local. It's clearly marked as a copy, and you cannot edit it directly. But if you genuinely need to undo a published form, there's an escape hatch: **Revoke**.

## Revoke - use with caution

**Revoke** un-publishes a form. It takes your read-only photocopy, makes it editable again, and transfers ownership back to you. You can then edit and publish a new version.

The danger is that the office may have **already processed** the previous version - imported it into GeoDin Desktop, generated a plate, sent a report to the client. Revoking doesn't recall any of that downstream work. If you revoke and republish, you're relying on the next person noticing there's a new version.

{% hint style="danger" %}
**Rules of thumb for Revoke:**

* Avoid it where possible. It's an escape hatch, not a workflow step.
* If you must revoke, **communicate with whoever receives your forms** before you do it. Tell them a new version is coming so they don't process the old one.
* Never revoke a form that was published more than a few hours ago - assume it's already been processed.
{% endhint %}

## Versioning and team discipline

Forms move between team members, and sometimes also between Onsite versions - someone on an older version retrieves a form published by someone on a newer version.

The simplest rule: **keep everyone on the latest version**. Onsite's automatic update check at launch makes this easy. An older version can usually still open a newer form, but any data tied to new tables or new fields introduced in the newer version may be lost on save. For multi-user teams, update discipline matters.

***

**See also**

* [Publishing & retrieving forms](../guides/publishing-and-retrieving.md) - step-by-step how-to
* [File delivery setup](../configuration/file-delivery-setup.md) - configuring the shared folder
* [Forms & projects](forms-and-projects.md) - what a form actually is on disk
