FROM alpine:latest

RUN apk --update --no-cache add bash nfs-utils curl && \
    rm -v /etc/idmapd.conf /etc/exports

# http://wiki.linux-nfs.org/wiki/index.php/Nfsv4_configuration
RUN mkdir -p /var/lib/nfs/rpc_pipefs && \
    mkdir -p /var/lib/nfs/v4recovery && \
    echo "rpc_pipefs  /var/lib/nfs/rpc_pipefs  rpc_pipefs  defaults  0  0" >> /etc/fstab && \
    echo "nfsd        /proc/fs/nfsd            nfsd        defaults  0  0" >> /etc/fstab

COPY ./entrypoint.patch /usr/local/bin/entrypoint.patch
RUN cd /usr/local/bin && \
    curl -o entrypoint.sh https://raw.githubusercontent.com/ehough/docker-nfs-server/v2.2.1/entrypoint.sh && \
    patch < entrypoint.patch

EXPOSE 2049

ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]
