# Folder structure

GeoDin Onsite keeps everything it writes - your forms, your settings, your logs - in a single **working folder** on your computer. Knowing where this folder is and what's in it will save you time whenever you need to back up your work, share a configuration with a colleague, or troubleshoot an issue.

## The working folder

Your working folder lives at:

```
%APPDATA%\GeoDin.Onsite\
```

On a typical Windows machine, `%APPDATA%` resolves to `C:\Users\<your username>\AppData\Roaming`, so the full path looks something like `C:\Users\John\AppData\Roaming\GeoDin.Onsite`.

{% hint style="info" %}
The `AppData` folder is **hidden by default** in Windows Explorer. Two easy ways to get to the working folder:

* **Inside Onsite** - open Configuration → Folders and click **Open local folder**
* **From Windows Explorer** - click the address bar, type `%appdata%\GeoDin.Onsite`, and press Enter
{% endhint %}

## What's inside

Your working folder starts almost empty. As you use Onsite, it gradually populates with subfolders and files.

### Subfolders

| Folder | Purpose |
|---|---|
| `projects/` | One subfolder per project you've worked on, containing its forms. Created automatically the first time you save a form under a given project number. |
| `logs/` | One log file per day, created automatically. Useful when [contacting support](../support/troubleshooting.md). |
| `installers/` | Cached copies of Onsite installers downloaded during automatic updates. Handy if you need to install Onsite on another machine on a slow connection - you can share the cached installer instead of re-downloading. |
| `backups/` | Automatic backup copies of your forms, kept according to your [backup settings](../configuration/backups.md). |

### Loose files

These files appear directly in the root of the working folder:

* **`config.xml`** - your Configuration settings. Created the first time you click OK in the Configuration menu.
* **`logo.png`** - your custom logo, if you've added one. See [Label printing](../configuration/label-printing.md).
* **Custom `.zpl` files** - custom label templates, if you've created any.

## Sharing configuration with colleagues

Everything in the working folder is yours alone - Onsite doesn't share it automatically. If your team needs consistent settings (same label layout, same logo, same defaults), a reasonable workflow is:

1. One person configures Onsite the way the team wants it
2. They share their `config.xml`, `logo.png`, and any custom `.zpl` templates
3. Each colleague copies those files into their own working folder

{% hint style="danger" %}
Each person should have their **own individual copy** of the files. Do not point multiple installations at a single shared `config.xml` - that will cause conflicts.
{% endhint %}

## The installation folder (read-only)

Separate from the working folder is the **installation folder**, where the Onsite program itself and its default assets live. The exact location depends on how you installed Onsite:

* **Installed for all users** (requires admin rights) - `C:\Program Files\GeoDin.Onsite`
* **Installed for your user only** (the default) - under `%LOCALAPPDATA%\Programs\GeoDin.Onsite`

{% hint style="danger" %}
Never edit files in the installation folder directly. They're read-only by design, and updating Onsite will overwrite them.
{% endhint %}

Default label templates, the default logo, and other customisable assets all live in `<installation folder>\assets\`. To customise any of them, **copy the file to your working folder** and edit it there. Onsite uses your working-folder version in preference to the default.

***

**See also**

* [Forms & projects](forms-and-projects.md) - how Onsite organises what you create
* [Backups](../configuration/backups.md) - configuring and restoring automatic backups
* [Troubleshooting](../support/troubleshooting.md) - finding log files
