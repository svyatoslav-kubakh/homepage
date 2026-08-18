Title: Building an ESP32 blackout power monitor
Date: 2023-08-10
Slug: svitlobot-esp32-blackout-monitor
Summary: Creating a resilient ESP32 client with C++ and PlatformIO to track power availability and WiFi status.

After the winter with frequent power outages, I wanted a simple and reliable device to monitor whether power and home internet are active.

I decided to write custom firmware for an [ESP32](https://www.espressif.com/en/products/socs/esp32) board in C++ using [PlatformIO](https://platformio.org/).

The hardware setup is very simple:

- ESP32 development board plugged into wall power.
- LED indicator for fast visual status checks.

The main challenge with firmware during outages is network instability. When electricity returns, the router takes a couple of minutes to boot, the optical terminal (ONT) might take even longer, and WiFi may connect before WAN is actually reachable.

A few architectural details that made the firmware stable:

- Clean finite state machine: Strict transitions between booting, connecting to WiFi, pinging the gateway, active telemetry, and offline recovery.
- Reconnection backoff: Avoid overloading the router with connection requests while it is still starting up.
- Non-volatile storage (NVS): Saving WiFi settings and configuration directly on flash so they survive reboots.
- Simple LED patterns: Different blink rates indicate whether the device is connecting to WiFi, waiting for IP, or fully online.

The device runs continuously without crashes and gives accurate telemetry on whether our home has electricity and internet.
