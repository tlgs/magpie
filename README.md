# magpie

magpie is a ~~simple~~ homelab setup.

| Hostname  | Host           | OS                         | Storage                       |
| --------- | -------------- | -------------------------- | ----------------------------- |
| pica      | Raspberry Pi 4 | Raspberry Pi OS (Bullseye) | 64GB microSD                  |
| cissa     | ROCK 4 A+      | Armbian 22.08 (Bullseye)   | 32GB eMMC                     |
| cyanopica | ROCK 4 A+      | Armbian 22.08 (Bullseye)   | 32GB eMMC                     |
| urocissa  | ROCK 4 A+      | Armbian 22.08 (Bullseye)   | 32GB eMMC + 1TB SATA 2.5″ SSD |

## Setup

I defer most of the homelab base system setup to a couple Ansible playbooks.

However, getting the boards to a minimal working state still requires some manual steps:
downloading OS images, flashing microSD cards,
creating required the files for remote access on RPi OS,
and writing the image to the on-board eMMC on the ROCK 4s.

After that minimal working state is achieved, it's as simple as:

1. Create an SSH key-pair, `ssh-keygen -t ed25519 -f ~/.ssh/magpie_ed25519`
2. Run `ansible-playbook bootstrap.yaml -t first-run`
3. Run `ansible-playbook k3s.yaml`

### Writing the image to the on-board eMMC (ROCK 4 A+)

Use `armbian-install` and pick 'Boot from eMMC - system on eMMC'.

If that doesn't work, follow the directions in
[Radxa's wiki](https://wiki.radxa.com/Rockpi4/install/eMMC):

1. `wget $ARMBIAN_IMG_URL`
2. `xzcat $ARMBIAN_IMG | dd of=/dev/mmcblk1 bs=1M`

### Other notes

The [ROCK Pi 23 PoE HAT](https://wiki.radxa.com/ROCKPI_23W_PoE_HAT)
has a PWM controllable fan "supported" by Radxa.
It's not straighforward to set it up using Armbian, so I didn't.
Here's a related
[thread on the Armbian forums](https://forum.armbian.com/topic/20101-open-pwm-on-rockpi4-to-control-fan-on-poe-hat/)
that should be a decent starting point.
