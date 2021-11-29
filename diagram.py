from diagrams import Cluster, Diagram
from diagrams.onprem.container import Docker

with Diagram("magpie", filename="assets/architecture", direction="TB", show=False):
    with Cluster("core"):
        traefik = Docker("traefik")
        portainer = Docker("portainer")
        cadvisor = Docker("cadvisor", fontcolor="crimson")

    with Cluster("dns"):
        pihole = Docker("pihole")
        unbound = Docker("unbound")

    with Cluster("media"):
        airsonic = Docker("airsonic")
        nfs = Docker("nfs-server", fontcolor="crimson")

    all_nodes = {
        traefik,
        portainer,
        cadvisor,
        pihole,
        unbound,
        airsonic,
        nfs,
    }

    traefik >> list(all_nodes - {unbound, nfs})
    # cadvisor << list(all_nodes)
    # portainer - list(all_nodes)

    pihole - unbound
