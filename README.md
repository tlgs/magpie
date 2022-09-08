# magpie

magpie is a simple homelab setup.

| Host                      | CPU              | RAM   | Storage      | Hostname | IP            |
| ------------------------- | ---------------- | ----- | ------------ | -------- | ------------- |
| NanoPi NEO v1.4           | Allwinner H3     | 512MB | 32GB MicroSD | n.magpie | 192.168.0.200 |
| Raspberry Pi 4B (rev 1.1) | Broadcom BCM2711 | 4GB   | 64GB MicroSD | r.magpie | 192.168.0.201 |

## Setup

1. Create an SSH key-pair, `ssh-keygen -t ed25519 -f ~/.ssh/magpie_ed25519`

### Getting and patching images

For the NanoPi NEO:

1. Download and decompress image: `./scripts/get-dietpi nanopineo`
2. Patch: `./scripts/patch-dietpi DietPi_NanoPiNEO-ARMv7-Bullseye.img n.magpie 192.168.0.200`

For the Raspberry Pi:

1. Download and decompress image: `./scripts/get-dietpi rpi4b`
2. Patch: `./scripts/patch-dietpi DietPi_RPi-ARMv8-Bullseye.img r.magpie 192.168.0.201`

### Bootstraping

1. Flash SD cards and boot up; DietPi's first boot can take a while (10+ minutes)
2. Make sure you can SSH in using the default credentials
3. Run `ansible-playbook bootstrap.yaml -t first-run`
