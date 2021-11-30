# core

- [`traefik`](https://doc.traefik.io/traefik/) is a
  [reverse proxy](https://www.cloudflare.com/en-gb/learning/cdn/glossary/reverse-proxy/) (and more)
- [`portainer`](https://docs.portainer.io/) is a GUI management application for Docker (and more)
- [`cAdvisor`](https://github.com/google/cadvisor) analyzes resource usage and performance
  characteristics of running containers

## cAdvisor

Currently an handmade image as there's no official ARM support for cAdvisor
(see [#1236](https://github.com/google/cadvisor/issues/1236)).
This is a mix between the
[official Dockerfile](https://github.com/google/cadvisor/blob/master/deploy/Dockerfile)
and the seemingly unmaintained
[Budry/cadvisor-arm](https://github.com/Budry/cadvisor-arm) workaround.

Remember to run `docker-compose build` after changes to this Dockerfile.
