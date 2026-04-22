---
description: GPS and Location Capture
---

<!--
**Content status:** Auto-assembled from product documentation
**Source quality:** B (Moderate (single source type))
**Needs:** editorial review
-->

# GPS and Location Capture

## GPS & Location Capture

Onsite supports GPS location capture via a "Record position" button on forms, using the device's built-in GPS chip to write coordinates directly into the form. <!-- src: transcript/field-data-collection#gps-location-capture -->

GPS source options (Configuration > GPS tab): <!-- src: transcript/field-data-collection#gps-location-capture -->

Local coordinate system is configured via EPSG code in the project settings. <!-- src: transcript/field-data-collection#gps-location-capture -->

Pictures captured via the camera are automatically embedded with a GPS location map showing where the picture was taken. <!-- src: transcript/field-data-collection#gps-location-capture -->

## Camera & Photo Capture

Onsite uses the device's embedded camera for photos on forms like the picture log. Camera settings (Configuration > Camera tab) include camera selection, resolution, and image rotation. <!-- src: transcript/field-data-collection#camera-photo-capture -->

External DSLR integration: Configuration > Camera > "Enable command line interface capture" lets Onsite delegate photo capture to an external command-line tool. <!-- src: transcript/field-data-collection#camera-photo-capture -->

The recommended CLI capture tool is Digicamcontrol (free, downloadable from the Digicamcontrol website). It lets Onsite trigger Nikon DSLRs and similar cameras to capture photos and save them to a specified path and filename. <!-- src: transcript/field-data-collection#camera-photo-capture -->

Digital Camera Capture mode supports configurable image quality, bits, and other high-end parameters for connected external cameras. <!-- src: transcript/field-data-collection#camera-photo-capture -->

One laboratory installation uses Onsite on a tablet/touchscreen PC with a Nikon DSLR mounted on an overhead frame with calibrated lighting, capturing core/sample photographs via Digicamcontrol. <!-- src: transcript/field-data-collection#camera-photo-capture -->

Sample Picture Log (`SPL`) form supports two capture modes: (1) scan an existing sample label's QR code to auto-link the picture to that sample, or (2) create a sample manually from a sample page in G1 drilling, then take a photo and assign it. <!-- src: transcript/field-data-collection#camera-photo-capture -->

Pictures can be rotated, cropped, and annotated/drawn on from within the form. <!-- src: transcript/field-data-collection#camera-photo-capture -->

Multiple pictures can be attached to the same sample. <!-- src: transcript/field-data-collection#camera-photo-capture -->

Picture files are named after project number + location + reference + depth, so they remain uniquely identifiable outside the form. <!-- src: transcript/field-data-collection#camera-photo-capture -->

Picture log output is a PDF with embedded small images plus the original source JPEGs/PNGs placed in the delivery folder; no GeoDin ML is produced. <!-- src: transcript/field-data-collection#camera-photo-capture -->
