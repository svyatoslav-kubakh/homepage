Title: My own gpodder2 compatible sync server
Date: 2026-08-12
Slug: why-i-built-podhound
Summary: The story of building a lightweight gPodder sync server after getting tired of broken self-hosted alternatives.

<img src="/images/podhound-logo.png" alt="Podhound Logo" width="120" style="float: right; margin: 4px 0 15px 20px; max-width: 30%;">

I listen to podcasts daily on my phone using AntennaPod and wanted to keep playback progress and subscriptions in sync across devices.

The official gpodder.net service has been unreliable and slow for years. So I started looking for self-hosted alternatives to run on my Synology NAS in Docker.

What I found was frustrating:

- Heavy suites: Running a full Nextcloud instance just to sync podcast playback state is way too bloated.
- Incomplete implementations: I tried gpodder2go, but it had annoying limitations. It did not handle device registration properly. Every time you added a new device, it returned HTTP 500 until you opened SQLite in the terminal and manually inserted SQL rows into sync tables.

I just wanted a small, rock-solid service that you start once with Docker and forget about. Once I decided to write it for my own setup, the immediate next thought was to polish it and share it with the open source community so others dealing with the same sync issues could use it too.

So I built and released Podhound.

What Podhound is:

- A clean, lightweight implementation of the gPodder API v2.
- Built with Bun and TypeScript using native SQLite and prepared statements.
- Fully automated: connects new devices and creates sync groups out of the box with zero manual database tweaking.
- Ultra-low memory footprint: around 11 MB on startup, staying around 20 MB in daily use.
- Packaged as a multi-stage Alpine Docker image.

Project resources:

- Official website and config generator: [podhound.github.io](https://podhound.github.io)
- GitHub repository: [github.com/podhound/podhound](https://github.com/podhound/podhound)
- Docker image: [hub.docker.com/r/skubakh/podhound](https://hub.docker.com/r/skubakh/podhound)
