

## docker-nfs-server

The `erichough/nfs-server` is the most versatile NFS server solution
in Docker; however, it suffers from a couple of big problems:

- no ARM image
- largely unmaintained (no commits in more than one year)

My first attempt at a solution was to simply use the original repository
as a git submodule and build the image myself,
but the project breaks with the latest Alpine base image.
There is currently a PR with the solution
([#67](https://github.com/ehough/docker-nfs-server/pull/67)),
but I don't have any hope of it being merged anytime soon.

What I did then, was clone the project here, remove unnecessary files
and apply the patch myself.

```console
$ git clone --depth 1 https://github.com/ehough/docker-nfs-server.git
$ rm -rf docker-nfs-server/.git
$ rm -rf docker-nfs-server/.github
$ rm -rf docker-nfs-server/doc
$ rm docker-nfs-server/.gitignore
$ rm docker-nfs-server/.dockerignore
$ rm docker-nfs-server/CHANGELOG.md
$ rm docker-nfs-server/README.md
```
