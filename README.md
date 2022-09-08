# magpie

magpie is a simple homelab setup.

| Host                      | RAM   | Hostname | IP            |
| ------------------------- | ----- | -------- | ------------- |
| NanoPi NEO v1.4           | 512MB | n.magpie | 192.168.0.200 |
| Raspberry Pi 4B (rev 1.1) | 4GB   | r.magpie | 192.168.0.201 |

## Setup

1. Create an SSH key-pair, `ssh-keygen -t ed25519 -f ~/.ssh/magpie_ed25519`

### Downloading and patching images

For both the NEO and the Pi, download the images using `scripts/get-dietpi`.

Patch each image using `scripts/patch-dietpi` and passing the appropriate arguments.

### Bootstraping

1. Flash SD cards and boot up; DietPi's first boot can take a while (10+ minutes)
2. Make sure you can SSH in using the default credentials
3. Run `ansible-playbook bootstrap.yaml -t first-run`
