---
description: Camera and GPS
---

<!--
**Content status:** Auto-assembled from product documentation
**Source quality:** C (Thin (limited source material))
**Needs:** editorial review
-->

# Camera and GPS

## Camera & DSLR Integration

Onsite uses the device's embedded camera for photos on forms like the picture log. Camera settings (`Configuration > Camera`) include: camera selection, resolution, image rotation. <!-- src: transcript/api-integrations#camera-dslr-integration -->

"Digital Camera Capture" mode supports connected high-resolution external cameras (e.g., DSLR mounted on a rig for laboratory photography of liners). Extra parameters: image quality, bits, etc. <!-- src: transcript/api-integrations#camera-dslr-integration -->

External DSLR integration via command line: `Configuration > Camera > Enable command line interface capture` lets Onsite delegate photo capture to an external CLI tool — the user provides the command and Onsite runs it instead of the built-in camera. <!-- src: transcript/api-integrations#camera-dslr-integration -->

The recommended CLI capture tool is **Digicamcontrol** (free, downloadable from the Digicamcontrol website), which lets Onsite trigger Nikon DSLRs (and similar) to capture a photo and save it to a specified path/filename. <!-- src: transcript/api-integrations#camera-dslr-integration -->

A laboratory installation uses Onsite on a tablet/touchscreen PC with a Nikon DSLR mounted on an overhead frame with calibrated lighting, capturing core/sample photographs via Digicamcontrol. <!-- src: transcript/api-integrations#camera-dslr-integration -->

Pictures captured via the device camera are automatically embedded with a GPS location map showing where the picture was taken. <!-- src: transcript/api-integrations#camera-dslr-integration -->

## GPS Hardware Integration

Onsite supports GPS location capture via a "Record position" button on forms, writing coordinates directly into the form. <!-- src: transcript/api-integrations#gps-hardware-integration -->

GPS source options (`Configuration > GPS`): (1) built-in tablet GPS chip, (2) Windows location service (IP/Wi-Fi based — accuracy described as "terrible", within a few kilometres), (3) external high-accuracy GPS device via Bluetooth, (4) manual latitude/longitude entry, (5) manual local X/Y entry. <!-- src: transcript/api-integrations#gps-hardware-integration -->

Local coordinate system is configured via EPSG code in the project settings. <!-- src: transcript/api-integrations#gps-hardware-integration -->
