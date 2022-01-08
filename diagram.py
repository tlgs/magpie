from diagrams import Cluster, Diagram, Edge
from diagrams.onprem.client import Users
from diagrams.onprem.container import Docker
from diagrams.onprem.network import Traefik

http = Edge(color="#005B9C")
dns = Edge(color="#F5821F")
nfs = Edge(color="#5484A4")

graph_attr = {
    "splines": "spline",
}

with Diagram(
    "",
    filename="assets/architecture",
    direction="TB",
    show=False,
    graph_attr=graph_attr,
):
    users = Users("users")

    with Cluster("magpie"):
        with Cluster("dns"):
            pihole = Docker("pihole")
            unbound = Docker("unbound")

        with Cluster("core"):
            traefik = Traefik("traefik")
            portainer = Docker("portainer")
            cadvisor = Docker("cadvisor*")

        with Cluster("media"):
            airsonic = Docker("airsonic")
            nfs_server = Docker("nfs-server*")

    traefik >> http >> [traefik, portainer, cadvisor, pihole, airsonic]

    pihole >> dns >> unbound

    users >> http >> traefik
    users >> dns >> pihole
    users >> nfs >> nfs_server
