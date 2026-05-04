# Troubleshooting

This page covers the quick things you can check yourself before contacting support — and how to gather the information our support team needs when you do reach out.

## Find your log files

GeoDin Onsite automatically creates a log file for every day you use it. These files record what the program was doing and surface any errors. They're the first thing our support team will ask for when investigating a crash or unexpected behaviour.

To open the log folder:

* Click the **?** icon in the main menu, then choose **Open log files** — this takes you straight to the `logs/` folder.
* Or navigate manually to `%APPDATA%\GeoDin.Onsite\logs`.

Each file is named by date. Pick the file for the day the issue happened and attach it to your support request — plain-text editors like Notepad can open it.

## When you contact support

To help us investigate faster, include:

* A description of **what you were doing** when the issue occurred
* The **log file** for that day (attached to your support request)
* **What you expected to happen** vs. what actually happened
* **Screenshots** of any error dialogs, if possible

Contact support by emailing [support@geodin.com](mailto:support@geodin.com). See [Get support](get-support.md).

## Common issues

### My license won't activate after a hardware change

Your license is bound to your machine's hardware. Swapping the hard disk, upgrading memory, or moving to a new computer can break the binding.

If activation fails after a hardware change, contact support — we can unlink your license from the old hardware so you can re-register it on the new machine. Keep your original license key handy.

### The Geo-data standards tab is locked

The Integration → Geo-data delivery tab is locked while forms are open. If you see a "locked" error when trying to change the standard, close any open forms and try again. See [Geo-data standards](../configuration/geo-data-standards.md).

### Offline mode isn't working

Onsite can run offline for up to 30 consecutive days after a successful license validation. If Onsite is asking you to go online and it's been fewer than 30 days, try:

1. Quit Onsite completely.
2. Confirm your system clock is correct — large clock skew can break validation.
3. Reopen Onsite.

If the issue persists, contact support.

### Sample labels won't print

Onsite prints labels in ZPL, a language supported by Zebra and compatible thermal printers. If your printer appears in the dropdown but labels don't print:

* Confirm the printer is **ZPL-compatible** — most Windows printers (including "Microsoft Print to PDF") are not.
* Try the **Preview** mode in Configuration → Labels to see whether the label renders at all.
* Check the printer's own status — offline, out of paper, disconnected from USB, etc.

See [Label printing](../configuration/label-printing.md) for full printer configuration.

### My teammate's published forms aren't appearing

If you've set up [file delivery](../configuration/file-delivery-setup.md) with a shared folder and forms aren't syncing between teammates:

1. **Check sync service** — open the shared folder directly in Windows Explorer. Are files appearing on both your and your teammate's machines? If not, the file-sync service (OneDrive, Dropbox, Google Drive, etc.) has a problem — not Onsite.
2. **Check cloud account status** — out-of-space or suspended accounts halt syncing silently.
3. **Check the folder path** — both users must point at the *same* synchronised folder, not independent folders with the same name.

### I need to go back to an older Onsite version

In general, **newer is better** — we recommend always running the latest Onsite version and never downgrading. Forms created in a newer version may have fields or tables that don't exist in an older version, and opening them in the older version will silently drop that data on save.

If you genuinely need to downgrade, contact support so we can walk you through safely handling your working folder.

***

**See also**

* [Get support](get-support.md) — how to reach our team
* [Updates & version compatibility](updates-and-version-compatibility.md) — version handling rules
* [Folder structure](../core-concepts/folder-structure.md) — where the logs folder lives
