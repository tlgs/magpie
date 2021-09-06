# core

## cAdvisor

Currently an handmade image as there's no official ARM support for cAdvisor
(see [#1236](https://github.com/google/cadvisor/issues/1236)).

This is a mix between the
[official Dockerfile](https://github.com/google/cadvisor/blob/master/deploy/Dockerfile)
and the seemingly unmaintained
[Budry/cadvisor-arm](https://github.com/Budry/cadvisor-arm) workaround.
