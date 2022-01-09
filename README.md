# magpie

magpie is a simple homelab setup - a bunch of Docker services
deployed on a single
[Raspberry Pi 4 model B (rev 1.1)](https://www.raspberrypi.com/products/raspberry-pi-4-model-b/) running Raspberry Pi OS Lite.

![Architecture diagram](assets/architecture.png)

## Notes

Using the `.local` TLD can be problematic due to an
[Avahi bug](https://wiki.archlinux.org/title/Avahi#Hostname_changes_with_appending_incrementing_numbers);
this makes resolving `magpie.local` unreliable on systems with mDNS resolvers.
See [[1]](https://www.howtogeek.com/167190/how-and-why-to-assign-the-.local-domain-to-your-raspberry-pi/),
and [[2]](https://www.ctrl.blog/entry/homenet-domain-name.html).
Might be a good excuse to move to back to Pi-hole's DHCP server solution.
