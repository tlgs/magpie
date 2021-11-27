from diagrams import Cluster, Diagram
from diagrams.onprem.container import Docker
from diagrams.onprem.network import Traefik

with Diagram("magpie", filename="assets/architecture", direction="TB", show=False):
    with Cluster("core"):
        traefik = Traefik("traefik")
        portainer = Docker("portainer")
        cadvisor = Docker("cadvisor")

    with Cluster("pihole"):
        pihole = Docker("pihole")
        unbound = Docker("unbound-rpi")

    with Cluster("media"):
        airsonic = Docker("airsonic")
        nfs = Docker("nfs-server")

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

    pihole << unbound
