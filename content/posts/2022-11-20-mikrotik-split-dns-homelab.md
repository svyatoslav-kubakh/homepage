Title: Setting up MikroTik Split-DNS for homelab
Date: 2022-11-20
Slug: mikrotik-split-dns-homelab
Summary: How to access home services using the same domain inside and outside your local network without Hairpin NAT overhead.

When you run a home server, like a [Synology NAS](https://www.synology.com/) or a mini-PC with [Docker](https://www.docker.com/), you usually want to access your services using a proper domain name and valid SSL certificates, both from home WiFi and from the outside.

The common way people solve this is Hairpin NAT (NAT loopback). It works, but it routes all local traffic through the router NAT firewall, which adds unnecessary load on the CPU and can limit throughput.

A much cleaner way is Split-DNS.

How it works:

- When you are away from home, your domain resolves to your public WAN IP through external DNS.
- When you are connected to your home WiFi, [MikroTik](https://mikrotik.com/) DNS answers the query and gives the local LAN IP (like 192.168.88.2) directly.

How to set this up in [RouterOS](https://help.mikrotik.com/docs/spaces/ROS/overview):

1. In [Winbox](https://help.mikrotik.com/docs/spaces/ROS/pages/53706857/Winbox), go to IP -> DNS -> Static.
2. Add a new static DNS entry:
   - Name: your service domain (e.g. `service.mydomain.me`)
   - Address: your local server IP (e.g. `192.168.88.2`)
   - TTL: `1d`

Now all local clients talk directly to the server over LAN at full gigabit speed, without touching the NAT engine, and SSL certificates work without any browser warnings.
