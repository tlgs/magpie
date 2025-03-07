# magpie

magpie is an incomplete homelab setup.

| Hostname  | Host           | OS                        | Storage                       |
| --------- | -------------- | ------------------------- | ----------------------------- |
| pica      | Raspberry Pi 4 | Armbian 24.8.1            | 64GB microSD                  |
| cissa     | ROCK 4 A+      | Armbian community 24.11.0 | 32GB eMMC                     |
| cyanopica | ROCK 4 A+      | Armbian community 24.11.0 | 32GB eMMC                     |
| urocissa  | ROCK 4 A+      | Armbian community 24.11.0 | 32GB eMMC + 1TB SATA 2.5″ SSD |

## Setup

Download OS images, flash microSD cards, write images to the on-board eMMC on the ROCK 4s.

1. `ssh-keygen -t ed25519 -f ~/.ssh/magpie_ed25519`
2. `ansible-playbook bootstrap.yaml -t first-run`
3. `ansible-playbook k3s.yaml`

### Configuration

```bash
export ANSIBLE_GATHERING=explicit
export ANSIBLE_INVENTORY=hosts.ini
export ANSIBLE_PYTHON_INTERPRETER=auto_silent
export ANSIBLE_REMOTE_USER=ansible

export KUBECONFIG=.kube/config
```

### Other notes

To write the image to the on-board eMMC (Rock 4s),
run `armbian-install` and select 'Boot from eMMC - system on eMMC' → 'ext4'.
See [Rockpi4/install/eMMC on Radxa's wiki](https://wiki.radxa.com/Rockpi4/install/eMMC).

The [ROCK Pi 23 PoE HAT](https://wiki.radxa.com/ROCKPI_23W_PoE_HAT)
has a PWM controllable fan "supported" by Radxa.
It's not straighforward to set it up using Armbian, so I didn't.
Here's a related
[thread on the Armbian forums](https://forum.armbian.com/topic/20101-open-pwm-on-rockpi4-to-control-fan-on-poe-hat/)
that should be a decent starting point.
