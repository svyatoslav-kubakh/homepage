Title: Self-hosted Obsidian LiveSync with CouchDB
Date: 2024-03-25
Slug: self-hosted-obsidian-livesync
Summary: How I set up end-to-end encrypted Obsidian sync across desktop and mobile without third-party cloud services.

[Obsidian](https://obsidian.md/) has been my primary tool for daily engineering notes, project specs, and personal knowledge base.

Standard file sync solutions like Google Drive or [Syncthing](https://syncthing.net/) can cause file conflicts on mobile when editing rapidly.

To get instant, conflict-free sync with full data ownership, I configured the [Self-hosted LiveSync plugin](https://github.com/vrtmrz/obsidian-livesync) for Obsidian backed by [Apache CouchDB](https://couchdb.apache.org/) running on my [Synology NAS](https://www.synology.com/).

Why this setup works well:

- Fast real-time sync: Changes on PC appear on the phone almost immediately.
- End-to-end encryption: All vault contents stored in CouchDB are encrypted with a client-side password before transmission.
- Clean conflict handling: CouchDB revision history prevents silent data overwrites.
- Automated Git backup: In addition to CouchDB replication, a background cron job commits the entire vault to a private Git repository once a day.

Combined with MikroTik Split-DNS, synchronization runs directly over local network when at home and securely over mobile internet when away.
