# magpie

magpie is a ~~simple~~ homelab setup.

| Hostname  | Host           | OS                         | Storage                          |
| --------- | -------------- | -------------------------- | -------------------------------- |
| pica      | Raspberry Pi 4 | Raspberry Pi OS - Bullseye | 64GB microSD + 1TB SATA 2.5″ SSD |
| urocissa  | ROCK 4 A+      | Armbian 22.08 - Bullseye   | 32GB on-board eMMC               |
| cissa     | ROCK 4 A+      | Armbian 22.08 - Bullseye   | 32GB on-board eMMC               |
| cyanopica | ROCK 4 A+      | Armbian 22.08 - Bullseye   | 32GB on-board eMMC               |

## Setup

This will cover the process of geeting a decent base system on the boards;
It boils down to the downloading of images, flashing microSD cards, manual
patching of the images, any other preliminary steps required on the boards,
and finally running an Ansible bootstrap playbook.

### Operating system choice

It would be preferable to have an uniform OS layer, but it seems
Armbian doesn't reliabily boot on the Raspberry Pi.
The ROCK 4 A+ boards go with Armbian and the Raspberry Pi uses the stock
Raspberry Pi OS Lite image.
Using Debian Bullseye flavor for both.

Some notes on the stock images:

- Random number generation: Armbian uses `haveged`, RPi OS uses `rng-tools-debian`
- NTP / SNTP: Armbian uses `chrony`, RPi OS uses `systemd-timesyncd`
- RPi OS has a number of unrequired services running by default:
  `avahi-daemon`, `triggerhappy`, `hciuart`, ...
  I'm not touching these for now.

### OS image patching

Other than writing the image to the on-board eMMC module, the setup for the
ROCK boards is pretty straightforward.
On the flipside, enabling
[remote access](https://www.raspberrypi.com/documentation/computers/remote-access.html)
on the Raspberry Pi, requires some doing (on the `boot` partition):

1. Add an empty `ssh` file
2. Add a `userconf.txt` file containing a single line: `username:encryptedpassword`
   (see [here](https://www.raspberrypi.com/documentation/computers/configuration.html#configuring-a-user)).
   Set the historically default user `pi` with `raspberry` as password.
   It will be deleted and replaced as part of the bootstrapping process.

The boards should boot and be reachable by SSH.
I recommend setting a static IP for each board.

### Writing the image to the on-board eMMC (ROCK 4 A+)

Use `armbian-install` and pick 'Boot from eMMC - system on eMMC'.

If that doesn't work, follow the directions in
[Radxa's wiki](https://wiki.radxa.com/Rockpi4/install/eMMC):

1. `wget $ARMBIAN_IMG_URL`
2. `xzcat $ARMBIAN_IMG | dd of=/dev/mmcblk1 bs=1M`

### Bootstrap hosts using Ansible

1. Create an SSH key-pair, `ssh-keygen -t ed25519 -f ~/.ssh/magpie_ed25519`
2. Run `ansible-playbook bootstrap.yaml -t first-run`
3. Run `ansible-playbook k3s.yaml`

### Notes

The [ROCK Pi 23 PoE HAT](https://wiki.radxa.com/ROCKPI_23W_PoE_HAT)
has a PWM controllable fan "supported" by Radxa.
It's not straighforward to set it up using Armbian so I didn't.
Here's a related
[thread on the Armbian forums](https://forum.armbian.com/topic/20101-open-pwm-on-rockpi4-to-control-fan-on-poe-hat/)
that should be a decent starting point.
