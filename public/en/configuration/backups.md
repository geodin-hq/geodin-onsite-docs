# Backups

Onsite includes an **automatic backup feature** that protects your work against mistakes, crashes, and accidental deletion. When enabled, Onsite takes timed snapshots of your active form at regular intervals and keeps a fixed number of previous versions. You can restore any saved version via the Tools menu.

## Enable backups

Backups are off by default. To turn them on:

1. Open **Configuration > Backups**.
2. Tick **Do timed backups**.
3. Set the interval, backup folder, and retention count (see below).

## Backup settings

| Setting | What it controls | Example |
|---|---|---|
| **Interval** | How often to take a snapshot, as HH:MM:SS | `00:00:30` = every 30 seconds; `00:02:00` = every 2 minutes |
| **Backup folder** | Where the snapshots are stored | Default: `[AppData]\GeoDin.Onsite\backups` |
| **Versions to keep** | How many snapshots to retain before overwriting the oldest | `10` (the default) |

<figure><img src="../.gitbook/assets/image (31).png" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
**Notes:**

* Backups run automatically - you don't need to press Save.
* Forms are also saved automatically when closed or when Onsite exits.
* Backup files are named with a combination of location name, form code, and date.
* Older forms remain accessible via **Load Local**, allowing you to retrieve previous work.
{% endhint %}

## Choosing your backup frequency

More frequent backups = better protection, but more disk usage. For a typical project:

* **Every 30 seconds** - suitable for fast-moving, high-stakes work (field drilling with complex forms)
* **Every 2-5 minutes** - fine for office-based work on stable data
* **Longer intervals** (15+ minutes) - leave you exposed if a crash happens; not recommended while actively editing

## Restore a backup

To restore a previous version of a form:

1. From the main menu, open **Tools > Restore backups**. The backup browser shows your recent forms - pick the form you want to restore.

<figure><img src="../.gitbook/assets/image (1).png" alt=""><figcaption></figcaption></figure>

2. Browse the saved versions for that form. Each entry is a snapshot; select one to preview it in read-only mode.

3. When you've found the version you want, click **Restore**. Onsite asks for confirmation before overwriting the current form with the selected version.

<figure><img src="../.gitbook/assets/image (2).png" alt=""><figcaption></figcaption></figure>

{% hint style="danger" %}
Restoring overwrites the current version of the form - the action cannot be undone. Make sure you really want to discard the current state before confirming.
{% endhint %}

***

**See also**

* [Folder structure](../core-concepts/folder-structure.md) - where the `backups/` folder lives
* [Forms & projects](../core-concepts/forms-and-projects.md) - how forms are saved automatically
