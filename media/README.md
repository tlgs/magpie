# media

Possible alternative to airsonic-advanced is
[Navidrome](https://github.com/navidrome/navidrome/)
once Sonos is supported [(#165)](https://github.com/navidrome/navidrome/issues/165).
Note that Sonos support can be achieved by a
[separate service](https://github.com/simojenki/bonob).

## nfs-server

The [`erichough/nfs-server`](https://github.com/ehough/docker-nfs-server)
is the most versatile NFS server solution in Docker;
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
