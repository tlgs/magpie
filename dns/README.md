# dns

- [`pihole`](https://github.com/pi-hole/docker-pi-hole)
  is a [DNS sinkhole](https://en.wikipedia.org/wiki/DNS_sinkhole) (and more)
- [`unbound`](https://gitlab.com/klutchell/unbound)
  is a [recursive DNS server](https://www.cloudflare.com/en-gb/learning/dns/what-is-recursive-dns/)

Together, these services provide an _All-Around DNS Solution_;
their need and usefulness is best described in
[this page](https://docs.pi-hole.net/guides/dns/unbound/) of Pi-hole's documentation.

## Notes

- Both images are pretty well documented so the setup is relatively straightforward.
  This combination is fairly standard so there are a couple of similar stacks thrown around GitHub issues
  (e.g. [#918](https://github.com/pi-hole/docker-pi-hole/issues/918),
  [#922](https://github.com/pi-hole/docker-pi-hole/issues/922),
  [#315](https://github.com/pi-hole/docker-pi-hole/issues/315)).
- This stack creates the `dns_net` network as `unbound` really only needs to talk to `pihole`
  and does not need to be exposed to the frontend network.
- Makes use of `extra_hosts` to include Local DNS entries.
- The `pihole` service uses a [Traefik middleware](https://doc.traefik.io/traefik/middlewares/overview/)
  to redirect to `/admin`.
