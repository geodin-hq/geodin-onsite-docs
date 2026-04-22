---
description: Single Ownership Model
---

<!--
**Content status:** Auto-assembled from product documentation
**Source quality:** B (Moderate (single source type))
**Needs:** editorial review
-->

# Single Ownership Model

## Single-Ownership Model (Onsite "One Piece of Paper")

Form ownership in Onsite follows a strict single-copy model: only one copy of a form exists at any time. A form is either in the user's local "briefcase" or on a shared "shelf" — never both as live copies. <!-- src: transcript/user-management-permissions#single-ownership-model-onsite-one-piece-of-paper -->

Analogy: a physical piece of paper on a shelf — prevents two users editing the same form simultaneously and is positioned as a conscious simplicity choice over conflict-merging. <!-- src: transcript/user-management-permissions#single-ownership-model-onsite-one-piece-of-paper -->

Ownership is file-level, not user-level: whoever currently holds the live `.GDOF` owns it, regardless of user identity. <!-- src: transcript/user-management-permissions#single-ownership-model-onsite-one-piece-of-paper -->

Ownership is strictly exclusive, never concurrent — the digital equivalent of "single existence". <!-- src: transcript/user-management-permissions#single-ownership-model-onsite-one-piece-of-paper -->

"Save local" keeps a form in the local project folder without changing ownership. "Publish" moves the form into the file-delivery system with a status. <!-- src: transcript/user-management-permissions#single-ownership-model-onsite-one-piece-of-paper -->

Three publish states: `Incomplete`, `Final/Complete`, and `Partial` (Partial is more advanced). <!-- src: transcript/user-management-permissions#single-ownership-model-onsite-one-piece-of-paper -->

Two "shelves" exist when publishing: `Incomplete` (can be retrieved back by any user with access) and `Final/Complete` (goes to a shelf the original user cannot retrieve from; belongs to office staff). <!-- src: transcript/user-management-permissions#single-ownership-model-onsite-one-piece-of-paper -->

Publishing as `Complete` requires full form validation to pass; publishing as `Incomplete` is allowed with validation errors and places only the `.GDOF` on the shelf (no PDF or GeoDin ML generated yet). <!-- src: transcript/user-management-permissions#single-ownership-model-onsite-one-piece-of-paper -->

When a form is published, the `.GDOF` file is moved to the shared delivery folder and the original file "leaves" the local `projects` folder — `Load local` will no longer find it. <!-- src: transcript/user-management-permissions#single-ownership-model-onsite-one-piece-of-paper -->

A local photocopy of every published form is kept locally (marked internally as a copy, not the "live" version) for disaster recovery in case the cloud sync folder fails. <!-- src: transcript/user-management-permissions#single-ownership-model-onsite-one-piece-of-paper -->

`Retrieve` is the reverse of `Publish`: it reads a form back from the shared delivery folder onto the tablet and transfers ownership to the local user. After retrieve, a photocopy remains on the shelf marked as not-owned. <!-- src: transcript/user-management-permissions#single-ownership-model-onsite-one-piece-of-paper -->

When a user publishes an incomplete form, only another Onsite user with access to the shared folder can retrieve it; the original user loses the ability to `Load Local` that form until they retrieve it back. <!-- src: transcript/user-management-permissions#single-ownership-model-onsite-one-piece-of-paper -->

`Revoke`: if a form has been published as complete but was a mistake, the user can load the local photocopy and press `Revoke`, which reactivates it as the live copy for re-submission. Revoke is flagged as dangerous because it can overwrite data already processed downstream. <!-- src: transcript/user-management-permissions#single-ownership-model-onsite-one-piece-of-paper -->

Fire-and-forget workflow: field users publish from the tablet, the form disappears locally, and office staff pick it up — positioned as the intended clean separation between field and office work. <!-- src: transcript/user-management-permissions#single-ownership-model-onsite-one-piece-of-paper -->

## Data Privacy & Ownership

GeoDin does not access customer data; data ownership and privacy are core principles. <!-- src: transcript/user-management-permissions#data-privacy-ownership -->

The customer controls where data is stored (local, on-premises server, or cloud) and who has access. <!-- src: transcript/user-management-permissions#data-privacy-ownership -->

Data put into GeoDin is not visible to the parent company or to other clients; the platform operates independently. <!-- src: transcript/user-management-permissions#data-privacy-ownership -->

GeoDin does not anonymize or sell customer data. <!-- src: transcript/user-management-permissions#data-privacy-ownership -->

NDA arrangements are available for clients who need to share sensitive project data during configuration or API development; standard NDA templates are provided, or clients can use their own. <!-- src: transcript/user-management-permissions#data-privacy-ownership -->

Customers can run GeoDin in a locked-down corporate environment with no internet access — runtime telemetry or file transfer from GeoDin staff into the customer network is blocked in such setups. <!-- src: transcript/user-management-permissions#data-privacy-ownership -->

## GeoDin Licensing Model

Two license types exist: <!-- src: transcript/user-management-permissions#geodin-licensing-model -->

With a Professional license, the number of seats determines how many users can use GeoDin simultaneously (e.g., 3 licenses = up to 3 concurrent users out of a 15-person team). <!-- src: transcript/user-management-permissions#geodin-licensing-model -->

Any machine can act as the license server — no separate license server product is required. <!-- src: transcript/user-management-permissions#geodin-licensing-model -->

Licenses are hardware-bound; hardware changes (new laptop, Windows 10 to 11 upgrade) require license reactivation by GeoDin support. <!-- src: transcript/user-management-permissions#geodin-licensing-model -->

An educational package is available for colleges and students. <!-- src: transcript/user-management-permissions#geodin-licensing-model -->

Civil 3D plugin (GeoDin Ground) users do not need a GeoDin license; only people who manage and curate the database need paid licenses. <!-- src: transcript/user-management-permissions#geodin-licensing-model -->

GeoDin Onsite is included with a GeoDin subscription at no additional cost. <!-- src: transcript/user-management-permissions#geodin-licensing-model -->

GeoDin Onsite licenses can be bundled for contractors; pricing is custom/negotiated per bundle. <!-- src: transcript/user-management-permissions#geodin-licensing-model -->
