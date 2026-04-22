---
description: Getting started (Onsite)
---

<!--
**Content status:** Auto-assembled from product documentation
**Source quality:** C (Thin (limited source material))
**Needs:** editorial review
-->

# Getting started (Onsite)

To begin your journey with **GeoDin Onsite**, follow these simple steps:

1. **Download the Installer**
   Visit the [GeoDin Onsite official pagearrow-up-right](https://www.GeoDin.com/pages/GeoDin-onsite) to download the latest version of the software.
2. **Install the Application**
   Run the installer and follow the on-screen instructions to complete the setup.
3. **Activate Your License**
   Use the provided serial key to activate GeoDin Onsite and select the preferred language.

1. **Configure Default Settings**
   Open the Settings menu to customize language preferences, measurement units, and form templates according to your project needs.

Once installed, you're ready to start collecting validated field data with ease.
If you have questions or need help with access, feel free to contact

## **Licensing and Offline Use**

GeoDin Onsite performs a license validation check each time the application is launched. This ensures that the software is being used under a valid license agreement.

## Offline Mode

If you're working in the field without internet access (such as on a tablet or field computer), GeoDin Onsite will automatically switch to offline mode. In this mode, the software can continue to operate for up to 30 consecutive days without revalidating the license.

After 30 days offline, the application requires an internet connection to revalidate the license.

circle-info

**Note:** The 30-day offline period is separate from the actual license expiration date. Users must ensure that their license remains valid and reconnect periodically to maintain access.

---

## Additional content from product documentation

## Onsite Purpose & Core Workflow

GeoDin Onsite is the field/tablet/mobile companion app for digital form filling, designed to replace paper drilling logs. <!-- src: transcript/field-data-collection#onsite-purpose-core-workflow -->

Onsite is fundamentally a "form filler" — a digital form-filling application optimized for on-site geotechnical data capture. <!-- src: transcript/field-data-collection#onsite-purpose-core-workflow -->

Intended workflow is "fire and forget": capture data on-site, publish to the office, then move the tablet on to the next task without further involvement. <!-- src: transcript/field-data-collection#onsite-purpose-core-workflow -->

Onsite has no server front-end — it cannot talk directly to a GeoDin server; all project metadata and data exchange goes via GeoDin ML files and shared folders. <!-- src: transcript/field-data-collection#onsite-purpose-core-workflow -->

Onsite is configured per project: each install is tied to a specific project number (also called project identifier), with defaults like client, client number, driller name, and rig name stored at project level and auto-populated into new forms. <!-- src: transcript/field-data-collection#onsite-purpose-core-workflow -->

On every startup Onsite shows a project confirmation dialog asking the user to verify they are still working on the currently configured project. <!-- src: transcript/field-data-collection#onsite-purpose-core-workflow -->

First-run initialization shows a welcome dialog prompting the user to go to Configuration and choose their language. <!-- src: transcript/field-data-collection#onsite-purpose-core-workflow -->

## Runtime & Platform

Onsite is a Windows desktop application (tablet or PC), built on Microsoft .NET 8 — requires the .NET 8 runtime. <!-- src: transcript/field-data-collection#runtime-platform -->

On first launch, if the .NET 8 runtime is missing, Onsite redirects the user to Microsoft to download and install it. <!-- src: transcript/field-data-collection#runtime-platform -->

On-screen keyboard: a setting activates a built-in on-screen keyboard for tablets without a physical keyboard. It takes up significant screen space but is necessary for some hardware. <!-- src: transcript/field-data-collection#runtime-platform -->

UI language is switchable between English, German, Portuguese, and others under general settings. English is fully translated; other languages may have gaps where messages, warnings, or form pages revert to English. <!-- src: transcript/field-data-collection#runtime-platform -->
