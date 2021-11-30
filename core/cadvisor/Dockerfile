FROM arm32v7/golang:1.17.0-bullseye AS build

ENV CADVISOR_VERSION "v0.39.2"

WORKDIR /go/src/github.com/google/cadvisor

RUN apt-get update && apt-get install --no-install-recommends -y \
      git=1:2.30.2-1 \
      dmsetup=2:1.02.175-2.1 \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* \
    && git clone --branch ${CADVISOR_VERSION} https://github.com/google/cadvisor.git /go/src/github.com/google/cadvisor \
    && make build


FROM arm32v7/debian:bullseye

COPY --from=build /go/src/github.com/google/cadvisor/cadvisor /usr/bin/cadvisor

EXPOSE 8080

HEALTHCHECK --interval=30s --timeout=3s \
  CMD wget --quiet --tries=1 --spider http://localhost:8080/healthz || exit 1

ENTRYPOINT ["/usr/bin/cadvisor", "-logtostderr"]
