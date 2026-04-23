# Forms & projects

Every piece of work in GeoDin Onsite lives inside a **project**, and every deliverable inside a project is a **form**. Understanding this two-level model makes the rest of the product self-explanatory.

## Projects

A project represents the geotechnical or environmental investigation you're working on. It's identified by a **project number** (for example `P123`, `Delft001`, `F123456`) that you set in Configuration → Project.

Project numbers have strict formatting rules — letters, numbers, hyphens, and underscores only — because they double as folder names on disk and may appear in URLs. See [Project setup](../configuration/project-setup.md) for the full rules and the two ways to enter a project number (manual or from a GeoDinML file).

All forms you create while a given project is active are tied to that project automatically. You never file a form or pick a save location; Onsite handles that for you. On disk, every project gets its own subfolder under your [working folder](folder-structure.md).

## Forms

A form is a structured digital record of something you're collecting in the field — a drilling log, a sample picture, a groundwater reading. GeoDin Onsite ships with a set of form layouts. The two most commonly used are:

* **G1 Drilling Report** — a multi-page drilling log (see [G1 drilling report](../guides/g1-drilling-report.md))
* **ISO 22475 SEP 3** — a drilling report in the EN ISO 22475 standard

Other forms include the Picture Log, the Sample Picture Log, and bundled variants. See [Guides](../guides/g1-drilling-report.md) for form-specific walkthroughs.

### Form files: `.gdof` and `.gdob`

Forms are stored as files on disk in one of two formats:

* `.gdof` — a **single form** (for example, one drilling report)
* `.gdob` — a **form bundle** (a group of forms that travel together, for example a G1 Drilling Report plus a Sample Picture Log)

Both formats are XML under the hood. You shouldn't normally need to open them directly, but if you ever do, the contents are human-readable. The file includes the project number, the location identifier, validation state, and a history of every edit (who, when, which machine, which Onsite version).

### No "Save As" — Onsite names and files forms for you

Unlike a traditional desktop application, Onsite does not let you choose where a form is saved or what to name it. This is deliberate.

Every form is saved automatically in its project's folder with a standardised filename:

```
<Location>_<FormCode>_<Date>.<extension>
```

For example, `B1_G1DR_20260423.gdof` is a G1 Drilling Report for location `B1`, created on 23 April 2026.

This convention means:

* Files are always where Onsite expects them
* Filenames tell you at a glance what a form is
* Two people working in the same project can't pick conflicting filenames
* You cannot accidentally lose work by closing without saving — Onsite saves automatically when a form is closed or when the application exits

{% hint style="info" %}
**Tip:** A Save button exists for convenience, but you don't need to press it routinely. The form is automatically saved whenever you close it or exit Onsite.
{% endhint %}

### Form bundles

A **form bundle** is two or more forms stapled together so they travel as one unit. The most common bundle is **G1 Drilling Report + Sample Picture Log**: the drilling data and its accompanying sample photos stay joined as a single `.gdob` file.

You choose whether to create a single form or a bundle from the New Form dialog. Once a bundle is created, the pieces cannot be split apart later.

Within a bundled form, the Sample Picture Log section automatically pulls the list of samples from the drilling report — you don't re-enter them.

### Customising pages within a form

Some forms — notably the G1 Drilling Report — let you **show or hide pages** depending on what's relevant to your project. If you don't collect SPT readings, hide the SPT page. If you don't log rock layers, hide the rock page.

Pages can also be reordered. Both are done once per project from the page management controls inside the form.

***

**See also**

* [Folder structure](folder-structure.md) — where projects and forms live on disk
* [File delivery & ownership](file-delivery-and-ownership.md) — how forms move between team members
