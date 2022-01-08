# media

- [`navidrome`](https://github.com/navidrome/navidrome) is a music streaming server
- [`bonob`](https://github.com/simojenki/bonob) is an
  [SMAPI](https://developer.sonos.com/reference/sonos-music-api/) implementation,
  bridges Sonos devices and Navidrome
- `nfs-server` is an [NFS](https://en.wikipedia.org/wiki/Network_File_System) server (duh!)

Expected environment variables in `.env`:

| Environment variable | Description                                                                         |
| -------------------- | ----------------------------------------------------------------------------------- |
| TZ                   | Timezone (see [here](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones)) |
| SPOTIFY\_ID          | Spotify client ID                                                                   |
| SPOTIFY\_SECRET      | Spotify client secret                                                               |
| SONOS\_IP            | Sonos device IP address                                                             |
| HOST\_IP             | Host IP address                                                                     |

## Notes

- Navidrome requires `SPOTIFY_{ID,SECRET}` to fetch artist images.
- bonob cannot see `http://navidrome.magpie.local`, hence the `extra_hosts`
  workaround and the need for `HOST_IP`.

### nfs-server

The [`erichough/nfs-server`](https://github.com/ehough/docker-nfs-server)
image is the most versatile NFS server solution for Docker;
however, it suffers from a couple of big problems:

- no ARM image
- largely unmaintained (no commits in more than one year)

My first attempt at a solution was to simply use the original repository
as a git submodule and build the image myself,
but the project breaks with the latest Alpine base image.
There is currently a PR with the solution
([#67](https://github.com/ehough/docker-nfs-server/pull/67)),
but I don't have any hope of it being merged anytime soon.

The current working solution involves changing the original Dockerfile to fetch
the latest tagged version of the _entrypoint file_ and applying a patch.
The patch was created by cloning the working fork and running
`git diff v2.2.1..HEAD entrypoint.sh > entrypoint.patch`.

#### Client connection

On Arch Linux:

1. `# pacman -S nfs-utils`
2. `# mkdir /mnt/magpie`
3. `# mount -t nfs4 magpie.local:/ /mnt/magpie`
