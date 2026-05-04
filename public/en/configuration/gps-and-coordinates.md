# GPS & coordinates

Onsite can capture location coordinates automatically when you record field data — on a G1 drilling form's **Record position** button, for example. Configuration → GPS lets you choose where coordinates come from; Configuration → Defaults lets you choose what coordinate system they're reported in.

## GPS sources

Onsite supports four ways of getting your current position:

### Built-in GPS chip

Most field tablets have an integrated GPS receiver. If yours does, this is the most accurate and convenient option.

* **Pros:** High accuracy, works offline, no extra hardware
* **Cons:** Only available on devices with a GPS chip — most laptops don't have one

### Windows-based (IP + Wi-Fi)

Windows can estimate your location from your IP address and nearby Wi-Fi networks. Onsite can use this estimate when no better source is available.

* **Pros:** Available on any Windows device
* **Cons:** Accuracy is very low — typically within a few kilometres, sometimes worse

{% hint style="danger" %}
Windows-based location is fine as a fallback but is **not accurate enough for geotechnical fieldwork**. Use a built-in GPS chip or an external receiver when precise location matters.
{% endhint %}

### External Bluetooth GPS

Connect a dedicated GPS receiver to your device via Bluetooth. High-accuracy RTK or differential GPS units typically connect this way.

* **Pros:** Very high accuracy, including survey-grade
* **Cons:** Requires pairing and keeping the receiver charged

### Manual entry

Turn off automatic capture and enter coordinates by hand — as latitude/longitude or local X/Y values.

* **Pros:** Works anywhere, no hardware dependency
* **Cons:** Slow, error-prone, depends on knowing the coordinates ahead of time

## Coordinate systems

Field positions are recorded in a coordinate system appropriate to your region. Onsite uses **EPSG codes** to identify coordinate systems — a standard numeric catalogue covering most coordinate reference systems worldwide.

Configure your project's coordinate system in Configuration → Defaults → Local Coordinate System. Onsite converts captured GPS positions into your chosen system automatically. See [Form defaults](form-defaults.md) for the broader defaults configuration.

{% hint style="info" %}
If you're not sure which EPSG code to use, check with your surveyor or project lead. Common examples:

* **EPSG:4326** — WGS84 lat/long (what GPS chips natively produce)
* **EPSG:28992** — Dutch RD (Rijksdriehoekscoördinaten)
* **EPSG:27700** — British National Grid
* **EPSG:25832** — ETRS89 / UTM zone 32N (central Europe)

Hundreds of other codes exist for regional and national coordinate systems.
{% endhint %}

***

**See also**

* [Form defaults](form-defaults.md) — where the project coordinate system is set
* [Camera](camera.md) — other per-device settings
