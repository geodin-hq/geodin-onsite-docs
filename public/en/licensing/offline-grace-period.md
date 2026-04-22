---
description: Offline Grace Period
---

<!--
**Content status:** Auto-assembled from product documentation
**Source quality:** C (Thin (limited source material))
**Needs:** editorial review
-->

# Offline Grace Period

## Offline Grace Period

Onsite validates its license on every startup by contacting the licensing server. <!-- src: transcript/deployment-infrastructure#offline-grace-period -->

If no internet is available (e.g., tablet in the field), Onsite falls back to running offline for up to 30 days. <!-- src: transcript/deployment-infrastructure#offline-grace-period -->

After 30 days offline, the license must re-validate online before Onsite will continue to run. <!-- src: transcript/deployment-infrastructure#offline-grace-period -->

Internet/cloud connectivity is required only at the time of publish/retrieve; the tablet does not need to be online while filling out forms. <!-- src: transcript/deployment-infrastructure#offline-grace-period -->
