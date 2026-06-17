# Camera

The Camera tab in Configuration controls how Onsite captures photographs - in [Sample Picture Logs](../guides/sample-picture-log.md), in G1 drilling form bundles, and in any other form that embeds images.

## Built-in cameras

For tablets and laptops with built-in or USB webcams, Onsite lists the available cameras in a dropdown. Pick the device you want to use.

For each configured camera you can set:

* **Resolution** - the capture resolution. Higher = more detail but larger file sizes.
* **Rotation** - if the image comes in rotated the wrong way, pre-set a rotation correction here. Saves rotating every photo manually.

## External cameras (DSLR and similar)

Onsite supports high-resolution external cameras for lab-grade photography - for example, a DSLR mounted above a calibrated core-photography rig.

To use an external camera, you need a command-line capture tool of your choice - for example, **DigiCamControl** - that can trigger the camera and save the image to a specified file. Such tools support a wide range of DSLRs, run in the background, and expose a command-line interface that Onsite can invoke.

In Configuration → Camera:

1. Tick **Enable command-line interface capture**.
2. Supply the command-line instruction Onsite should run when it needs to take a picture - the capture tool's invocation with whatever parameters your camera requires.

When a form asks for a photo, Onsite runs the command instead of using a webcam, and picks up the resulting image file.

{% hint style="info" %}
External camera setup is more involved than built-in cameras. Refer to your capture tool's own documentation for the correct command-line parameters, and [contact support](../support/get-support.md) if you need help wiring it up to Onsite.
{% endhint %}

## Default picture path

Onsite stores captured photos in a default location determined by the form and project. Some forms let you browse for an already-taken photo instead of capturing a new one - in that case Onsite uses the default picture path as the starting folder for the browse dialog. Set this in Configuration → Camera if you regularly pick photos from the same location.

## Picture file handling

Captured photos are:

* Embedded into the form's PDF export at reduced resolution, so the PDF stays a manageable size.
* Stored as separate original files (JPEG or PNG depending on source) alongside the form.

When you [publish](../core-concepts/file-delivery-and-ownership.md) a form, you can choose whether to also send the original full-resolution files to the shared folder. See [File delivery setup → Embedded picture options](file-delivery-setup.md).

***

**See also**

* [Sample picture log](../guides/sample-picture-log.md) - the main photo-capturing form
* [GPS & coordinates](gps-and-coordinates.md) - also configured per-device
