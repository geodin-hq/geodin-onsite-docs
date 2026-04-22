# Configuration

### 1. Changing Standards

To change the standard used in GeoDin Onsite:

1. Navigate to **Configuration**.
2. Select **Integration** from the menu.
3. Under **Geo-data delivery** section, select the ⚙️ button
4.  In this section, you can choose which **standard** to apply.

    * This version includes five available standards.
    * You can also select the relevant **description types** associated with each standard.

    <figure><img src="../.gitbook/assets/image (28).png" alt=""><figcaption></figcaption></figure>

{% hint style="danger" %}
**Important:** Once a standard is applied and the project is active, it cannot be changed retroactively. Ensure you select the correct standard before proceeding with data entry.


{% endhint %}

{% hint style="info" %}
**Tip:** If the tab is locked, you will receive the below error. Check for any open forms and close them before proceeding.

<p align="center"><img src="../.gitbook/assets/image (30).png" alt=""></p>
{% endhint %}

### 2. Defaults

The **Defaults** tab in the **Configuration** menu allows you to define values that will automatically populate forms during data entry. This helps save time and ensures consistency across projects.

You can set the following default values:

* **Foreman/Leader/Logger** – Name of the person supervising or logging the drilling.
* **Assistant/Enabler 1 & 2** – Names of assistants involved in the drilling process.
* **Rig Number / Pit Method** – Identifier for the drilling rig or pit method used.
* **Vehicle/Vessel** – Name or ID of the vehicle or vessel associated with the project.
* **Unit System** – The available options are:
  * **Metric**
  * **US Customary**
  * **US with Decimal Feet**
* **Local Coordinate System** – Select the code for your local coordinate system as per the project.

<figure><img src="../.gitbook/assets/image.png" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
**Tip:** Setting these defaults ensures that forms are pre-filled with standard values, reducing manual input and minimizing errors.
{% endhint %}

### 3. Backups

GeoDin Onsite includes an **automatic backup feature** to protect your work and minimize data loss. This feature can be enabled in the **Backups** tab of the Configuration menu.

#### **3.1 How Backups Work**

* When enabled, the system creates timed backups of your active form at regular intervals (e.g., every 30 seconds or every 2 minutes).
* Each backup is stored in a designated folder and up to **10 versions** are retained by default.
* This ensures that if you make a mistake or need to revert to an earlier version, you can easily restore your work.

#### **3.2 Enable Backups**

1. Go to **Configuration** → **Backups**.
2. Check **Do timed backups** to enable the feature.

#### **3.3 Configure Backup Settings**

* **Interval**: Set how often backups occur (e.g., `00:05:00` for every 5 minutes).
* **Backup Folder**: Choose where backups are stored (default: `[AppData]\GeoDin.Onsite\`).
* **Versions to Keep**: Define how many backup versions to retain (e.g., 6).

<figure><img src="../.gitbook/assets/image (31).png" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
#### **Notes:**

* Backups run automatically; no need to press **Save**.
* Forms are saved when closed or when the program exits.
* Naming convention: **Location Name + Form Code + Date**.
* Older forms remain accessible via **Load Local**, allowing you to retrieve previous work.
{% endhint %}

#### **3.4 Accessing Backups**

To restore a previous version of your data:

1. Navigate to **Tools** in the main menu.
2. Select **Restore**.
3. Browse the list of available backup files and choose the specific project.
4. Inside the project, you’ll see **all saved versions.**
5. Select the version you want to restore and **confirm the action**.

<figure><img src="../.gitbook/assets/image (1).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (2).png" alt=""><figcaption></figcaption></figure>

###

### &#x20;

























































