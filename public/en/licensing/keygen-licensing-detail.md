---
description: Keygen Licensing Detail
---

<!--
**Content status:** Auto-assembled from product documentation
**Source quality:** B (Moderate (single source type))
**Needs:** editorial review
-->

# Keygen Licensing Detail

## GeoDin Licensing Model

Two license types exist: <!-- src: transcript/user-management-permissions#geodin-licensing-model -->

With a Professional license, the number of seats determines how many users can use GeoDin simultaneously (e.g., 3 licenses = up to 3 concurrent users out of a 15-person team). <!-- src: transcript/user-management-permissions#geodin-licensing-model -->

Any machine can act as the license server — no separate license server product is required. <!-- src: transcript/user-management-permissions#geodin-licensing-model -->

Licenses are hardware-bound; hardware changes (new laptop, Windows 10 to 11 upgrade) require license reactivation by GeoDin support. <!-- src: transcript/user-management-permissions#geodin-licensing-model -->

An educational package is available for colleges and students. <!-- src: transcript/user-management-permissions#geodin-licensing-model -->

Civil 3D plugin (GeoDin Ground) users do not need a GeoDin license; only people who manage and curate the database need paid licenses. <!-- src: transcript/user-management-permissions#geodin-licensing-model -->

GeoDin Onsite is included with a GeoDin subscription at no additional cost. <!-- src: transcript/user-management-permissions#geodin-licensing-model -->

GeoDin Onsite licenses can be bundled for contractors; pricing is custom/negotiated per bundle. <!-- src: transcript/user-management-permissions#geodin-licensing-model -->

## GeoDin Onsite Licensing (Keygen + Hardware Binding)

Licensing is seat-based via a license key — a 30-character uppercase alphanumeric string. A single key can cover multiple seats ("multi-seat license"). <!-- src: transcript/user-management-permissions#geodin-onsite-licensing-keygen-hardware-binding -->

Example configuration: a 20-seat support license valid until a fixed expiry date, named after the customer as entered in Shopify. <!-- src: transcript/user-management-permissions#geodin-onsite-licensing-keygen-hardware-binding -->

The licensing backend is Keygen (keygen.sh or equivalent). Support staff manage licenses via the Keygen dashboard — suspend, renew, revoke, view customer info. <!-- src: transcript/user-management-permissions#geodin-onsite-licensing-keygen-hardware-binding -->

Keygen is integrated with Shopify: a Shopify purchase triggers license automation, and customer IDs shown in Keygen are Shopify customer IDs (e.g., "customer ID 3656"). <!-- src: transcript/user-management-permissions#geodin-onsite-licensing-keygen-hardware-binding -->

The licensing backend is not a CRM — Keygen only handles keys and machine bindings, not transactions, money, or addresses. <!-- src: transcript/user-management-permissions#geodin-onsite-licensing-keygen-hardware-binding -->

Each activation is bound to a machine via a hardware ID fingerprint derived from hardware; it cannot be spoofed or tampered with. <!-- src: transcript/user-management-permissions#geodin-onsite-licensing-keygen-hardware-binding -->

The hardware ID may change if the disk or memory is swapped — in that case the license becomes unlinked and an admin must remove the old machine link in the Keygen dashboard so the license can re-activate on new hardware. <!-- src: transcript/user-management-permissions#geodin-onsite-licensing-keygen-hardware-binding -->

License Manager UI shows: license key, license name (customer name), expiry date, maximum GeoDin version allowed (e.g., "up to 3.99"), offline grace period (30 days), multi-seat count, machine name, and hardware ID. <!-- src: transcript/user-management-permissions#geodin-onsite-licensing-keygen-hardware-binding -->

License Manager is available in English and German. <!-- src: transcript/user-management-permissions#geodin-onsite-licensing-keygen-hardware-binding -->

Offline license validation: Onsite normally validates its license on every startup against the licensing server. If no internet is available (e.g., tablet in the field), Onsite falls back to offline mode for up to 30 days; after 30 days offline, the license must re-validate online. <!-- src: transcript/user-management-permissions#geodin-onsite-licensing-keygen-hardware-binding -->

Anti-abuse check on purchase: only existing GeoDin customers can self-serve Onsite; unknown emails trigger a manual approval step by sales. <!-- src: transcript/user-management-permissions#geodin-onsite-licensing-keygen-hardware-binding -->

Post-purchase the customer receives an email with the installer URL and a license key. First launch runs the License Wizard, which accepts the key via paste or clipboard and binds the license to the machine hardware ID. <!-- src: transcript/user-management-permissions#geodin-onsite-licensing-keygen-hardware-binding -->

Fallback when a licensing problem occurs: contact the internal support/licensing owner before assuming a Shopify/Keygen logic bug. <!-- src: transcript/user-management-permissions#geodin-onsite-licensing-keygen-hardware-binding -->
