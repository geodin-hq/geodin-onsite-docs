# File delivery setup

File delivery is how Onsite shares forms between teammates — drilling crews in the field, engineers in the office, and anyone else who needs to see the data. Configuration lives in Configuration → Integration → File delivery.

See [File delivery & ownership](../core-concepts/file-delivery-and-ownership.md) for the conceptual background — what publishing and retrieving mean, why single-ownership matters. This page covers the nuts-and-bolts setup.

## Delivery modes

Pick one mode:

| Mode | When to use |
|---|---|
| **No delivery** (default) | You work alone, or you share `.geodinml` files manually via email, USB drive, etc. No shared folder, no publish/retrieve buttons. |
| **Shared network folder** | Your team has a synchronised folder (OneDrive, Dropbox, Google Drive, a network drive, etc.) and wants forms to flow through it. Enables publish and retrieve. |

## Setting up a shared network folder

1. Decide which folder to use. Any folder your file-sync service keeps synchronised with your teammates will work:
   * A folder inside a shared OneDrive, SharePoint, or Google Drive
   * A shared Dropbox folder
   * A mapped network drive at the office

2. In Configuration → Integration → File delivery system, choose **Shared network folder**.

3. Click **Browse** and select the folder.

{% hint style="info" %}
You can use the `[my documents]` shortcut in the folder path to keep the configuration portable between users and machines. For example, `[my documents]\GeoDin.Onsite.Delivery` resolves to each user's own Documents folder, so you can share a single `config.xml` across a team without path breakage.
{% endhint %}

{% hint style="danger" %}
Do not point the shared folder at:

* Your Onsite **working folder** (`%APPDATA%\GeoDin.Onsite`) — that's for your private local data, not for sharing.
* The same location as your disaster-recovery local copies — keep the shelf and your briefcase physically separate.
{% endhint %}

## Synchronisation is your job, not Onsite's

Onsite reads from and writes to the folder you select. It does **not** synchronise that folder with your colleagues — that's handled by your file-sync service.

If teammates can't see each other's published forms, check the sync service first:

* Is the folder actually syncing? Open it on both machines and verify new files appear on both sides.
* Is anyone's cloud account out of space or suspended?
* Is the network connection stable for all users?

## Embedded picture options

Some forms (like the [Sample Picture Log](../guides/sample-picture-log.md)) include photographs. Photo files can be large — large enough to slow down publication on bandwidth-limited connections.

In File delivery settings, choose how Onsite handles picture files on publish:

* **Always send** — original full-resolution image files are always uploaded alongside the form.
* **Ask every time** — on each publish, Onsite asks whether to send the raw picture files.
* **Never send** — only the compressed version embedded in the PDF is sent; raw images stay on your device.

{% hint style="info" %}
Pictures are always embedded in the exported PDF at reduced resolution — the option above only affects whether the **original** full-resolution files are also transferred.
{% endhint %}

## Local copy of delivered forms

Onsite automatically keeps a read-only local photocopy of every form you publish — a disaster-recovery backup in case the shared folder becomes unreachable. This is always on and cannot be turned off. See [File delivery & ownership](../core-concepts/file-delivery-and-ownership.md) for details.

***

**See also**

* [File delivery & ownership](../core-concepts/file-delivery-and-ownership.md) — the concept model
* [Publishing & retrieving forms](../guides/publishing-and-retrieving.md) — day-to-day workflow
