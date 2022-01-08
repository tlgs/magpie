FROM alpine:3.15

# http://wiki.linux-nfs.org/wiki/index.php/Nfsv4_configuration
RUN apk --update --no-cache add \
      bash=~5.1.8-r0 \
      nfs-utils=~2.5.4-r1 \
      curl=~7.80.0-r0 \
      patch=~2.7.6-r7 \
    && rm -v /etc/idmapd.conf /etc/exports \
    && mkdir -p /var/lib/nfs/rpc_pipefs \
    && mkdir -p /var/lib/nfs/v4recovery \
    && echo "rpc_pipefs  /var/lib/nfs/rpc_pipefs  rpc_pipefs  defaults  0  0" >> /etc/fstab \
    && echo "nfsd        /proc/fs/nfsd            nfsd        defaults  0  0" >> /etc/fstab


# apply patch
COPY ./entrypoint.patch /usr/local/bin/entrypoint.patch

WORKDIR /usr/local/bin

RUN curl -o entrypoint.sh https://raw.githubusercontent.com/ehough/docker-nfs-server/v2.2.1/entrypoint.sh \
    && patch < entrypoint.patch \
    && chmod +x entrypoint.sh

EXPOSE 2049

ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]
