# Project setup

The **Project** tab in Configuration is where you tell Onsite which project you're currently working on. Onsite configures itself for one project at a time, and every form you create is automatically tied to that project.

See [Forms & projects](../core-concepts/forms-and-projects.md) for the conceptual background on why Onsite works this way.

## Project number rules

Project numbers are restrictive because they double as folder names on disk and may appear in URLs in future online features. Allowed characters:

* Letters (A-Z, a-z)
* Numbers (0-9)
* Hyphens (`-`)
* Underscores (`_`)

Spaces and special characters (`*`, `@`, `#`, `/`, and similar) are not allowed. If you type a disallowed character, Onsite automatically replaces it with an underscore.

{% hint style="danger" %}
**Be careful reusing a project number.** Onsite saves forms into a folder named after the project number. If you reuse an old project number for a new investigation, new forms mix into the old project's folder, and sorting them out afterwards is painful. Use a fresh project number for every new investigation.
{% endhint %}

## Two modes: manual vs GeoDinML-driven

You can choose how Onsite gets project details (project number, client name, location list). Set this in Configuration → Integration → Project metadata.

### Manual mode (default)

You type the project number and metadata directly into the Project tab. Fast and simple, but:

* No validation — you can mistype a project number
* No list of past projects — you have to remember what you used
* No cross-check against a master list

### GeoDinML-driven mode

In this mode, you provide a GeoDinML file containing a list of projects. Onsite reads the file and populates the Project tab with a dropdown of project numbers, each pre-populated with its associated client name and locations.

This is useful for teams with a central project database. One person exports a GeoDinML file from GeoDin Desktop containing the current list of active projects — just the project and location headers, no sample or measurement data, so the file stays small. The file is shared to the team; each person loads it in Onsite, and the dropdown keeps everyone consistent.

When the list of active projects changes, export a fresh GeoDinML and reload it.

{% hint style="info" %}
Onsite does not connect directly to a GeoDin database — it only reads GeoDinML files. This is by design: Onsite is built to work offline in the field.
{% endhint %}

## Project settings

Within the Project tab you also set:

* Project number (as above)
* Client name
* Client number
* Project description

These values auto-fill into every form you create under this project, saving repeated data entry. For additional auto-fill fields (crew names, rig, units), see [Form defaults](form-defaults.md).

***

**See also**

* [Forms & projects](../core-concepts/forms-and-projects.md) — the conceptual background
* [Form defaults](form-defaults.md) — other fields that auto-fill into forms
