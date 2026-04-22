---
description: Keygen Licensing
---

<!--
**Content status:** Auto-assembled from product documentation
**Source quality:** C (Thin (limited source material))
**Needs:** editorial review
-->

# Keygen Licensing

## Keygen Licensing Integration

GeoDin uses Keygen (keygen.sh) as the licensing backend. Support staff manage licenses via the Keygen dashboard — suspend, renew, revoke, view customer info. <!-- src: transcript/api-integrations#keygen-licensing-integration -->

Licensing is seat-based via a 30-character uppercase alphanumeric license key; a single key can cover multiple seats (multi-seat license). <!-- src: transcript/api-integrations#keygen-licensing-integration -->

Each activation is bound to a machine via a hardware ID fingerprint derived from hardware characteristics — cannot be spoofed or tampered with. <!-- src: transcript/api-integrations#keygen-licensing-integration -->

If the hardware ID changes (disk/memory swap), the license becomes unlinked and an admin must remove the old machine link in the Keygen dashboard so the license can be re-activated on the new hardware. <!-- src: transcript/api-integrations#keygen-licensing-integration -->

Offline license validation: Onsite normally validates its license on every startup via the licensing server; if offline, Onsite falls back to running offline for up to 30 days before requiring online re-validation. <!-- src: transcript/api-integrations#keygen-licensing-integration -->

The License Manager UI shows: license key, license name (customer name), expiry date, maximum GeoDin version allowed (e.g., "up to 3.99"), offline grace period, multi-seat count, machine name, and hardware ID. <!-- src: transcript/api-integrations#keygen-licensing-integration -->

License Manager is available in English and German. <!-- src: transcript/api-integrations#keygen-licensing-integration -->

The Keygen licensing manager is NOT a CRM — it does not handle transactions, money, addresses, or CRM data; it only handles keys and machine bindings. <!-- src: transcript/api-integrations#keygen-licensing-integration -->

Fallback when the first licensing problem occurs: contact the internal support/licensing owner before assuming a Shopify-Keygen logic bug. <!-- src: transcript/api-integrations#keygen-licensing-integration -->
