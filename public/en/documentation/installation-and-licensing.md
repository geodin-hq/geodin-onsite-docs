# Installation & licensing

This page covers what you need to install GeoDin Onsite and activate your license. For an orientation of the app once you have it running, see [The Onsite user interface](onsite-user-interface.md). To create your first form, see [First steps](first-steps.md).

## System requirements

* Windows tablet, laptop, or desktop
* **.NET 8 runtime** - if missing, Onsite will prompt you and redirect to Microsoft's download page on first launch
* An internet connection for licence activation and periodic validation

## Download the installer

Purchase GeoDin Onsite from the [GeoDin pricing page](https://www.geodin.com/pricing). After purchase you will receive a welcome email containing:

* A link to the installer
* A licence key (a string of letters and numbers, around 30 characters long)

## Install

Run the installer. It's a standard Windows setup wizard - click through **Next** until it finishes.

The installer asks which install mode to use:

* **Install for all users** (requires admin rights) - installs to `C:\Program Files\GeoDin.Onsite`. Use this when multiple Windows accounts on the same machine need access.
* **Install for your user only** (the default, no admin rights needed) - installs to a location under `%LOCALAPPDATA%\Programs\GeoDin.Onsite`.

Both modes work identically for daily use.

## Activate your license

The first time you start Onsite, the license manager opens automatically and asks for your license key.

1. Copy the key from your welcome email.
2. Paste it into the license manager (use **Ctrl+V** or the paste icon).
3. Click **Save the license key**.

If the key is valid, the manager confirms activation and Onsite opens.

<figure><img src="../.gitbook/assets/image (18).png" alt=""><figcaption></figcaption></figure>

4. **Configure default settings**\
   Open the Configuration menu to set your language preference, measurement units, and form defaults. See [The Onsite user interface](onsite-user-interface.md) for a tour of the menu.

{% hint style="info" %}
Your license is bound to your machine's hardware. If you move Onsite to a different computer or significantly change the hardware (for example, swap the disk or memory), the binding may break. In that case, [contact support](../support/get-support.md) to re-bind your licence to the new hardware.
{% endhint %}

## Subscription & free trial

GeoDin Onsite is available as an annual subscription, priced per device. A free trial with full functionality is also available for teams evaluating the product.

For current pricing and plan options, see the [GeoDin pricing page](https://www.geodin.com/pricing).

## Validation and offline use

Onsite validates your license online at every launch. After successful validation, you can use Onsite **offline for up to 30 consecutive days** - useful on tablets in the field without connectivity. Only licence validation and publish/retrieve require internet; filling out forms offline is fully supported throughout this window.

After 30 days offline, reconnect to the internet so Onsite can revalidate. The 30-day offline window resets each time a successful online validation occurs, and is **separate** from your subscription's expiry date.

## What's next

* [The Onsite user interface](onsite-user-interface.md) - a tour of what you'll see
* [First steps](first-steps.md) - create your first form end-to-end
