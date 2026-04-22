---
description: Configuring standards, defaults, and backups in GeoDin Onsite
---

# Configuration

## 1. Changing Standards

To change the standard used in GeoDin Onsite:

1. Navigate to **Configuration**.
2. Select **Integration** from the menu.
3. Under the **Geo-data delivery** section, select the settings (⚙️) button.
4. Choose which **standard** to apply.
   - This version includes five available standards.
   - You can also select the relevant **description types** associated with each standard.

![Configuration Standards](.gitbook/assets/onsite/config-standards.png)

> **Important:** Once a standard is applied and the project is active, it cannot be changed retroactively. Ensure you select the correct standard before proceeding with data entry.

> **Tip:** If the tab is locked, you will receive the error shown below. Check for any open forms and close them before proceeding.

![Lock Error](.gitbook/assets/onsite/config-lock-error.png)

## 2. Defaults

The **Defaults** tab in the **Configuration** menu lets you define values that automatically populate forms during data entry. This saves time and ensures consistency across projects.

You can set the following default values:

- **Foreman / Leader / Logger** — Name of the person supervising or logging the drilling.
- **Assistant / Enabler 1 & 2** — Names of assistants involved in the drilling process.
- **Rig Number / Pit Method** — Identifier for the drilling rig or pit method used.
- **Vehicle / Vessel** — Name or ID of the vehicle or vessel associated with the project.
- **Unit System** — Metric / US Customary / US with Decimal Feet.
- **Local Coordinate System** — Select the code for your local coordinate system as per the project.

![Defaults Configuration](.gitbook/assets/onsite/config-defaults.png)

> **Tip:** Setting these defaults ensures that forms are pre-filled with standard values, reducing manual input and minimizing errors.

## 3. Backups

GeoDin Onsite includes an **automatic backup feature** to protect your work and minimize data loss.

### 3.1 How Backups Work

- When enabled, the system creates timed backups of your active form at regular intervals.
- Each backup is stored in a designated folder; up to 10 versions are retained by default.
- If you make a mistake or need to revert, you can restore any retained version.

### 3.2 Enable Backups

1. Go to **Configuration** → **Backups**.
2. Check **Do timed backups** to enable the feature.

### 3.3 Configure Backup Settings

- **Interval** — How often backups occur (e.g., `00:05:00`).
- **Backup Folder** — Default: `[AppData]\GeoDin.Onsite\`.
- **Versions to Keep** — Number of backup versions to retain (e.g., 6).

![Backup Configuration](.gitbook/assets/onsite/config-backups.png)

**Notes:**

- Backups run automatically — no need to press **Save**.
- Forms are saved when closed or when the program exits.
- Naming convention: **Location Name + Form Code + Date**.
- Older forms remain accessible via **Load Local**.

### 3.4 Accessing Backups

1. Navigate to **Tools** in the main menu.
2. Select **Restore**.
3. Browse the list of available backup files and choose the relevant project.
4. Inside the project, all saved versions are listed.
5. Select the version you want to restore and confirm.

![Restore Menu](.gitbook/assets/onsite/config-restore-menu.png)

![Backup Selection](.gitbook/assets/onsite/config-backup-selection.png)
