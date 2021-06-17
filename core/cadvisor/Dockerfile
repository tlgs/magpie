FROM arm32v7/golang AS build
ENV CADVISOR_VERSION "v0.39.2"
RUN apt-get update && apt-get install -y git dmsetup && apt-get clean
RUN git clone --branch ${CADVISOR_VERSION} https://github.com/google/cadvisor.git /go/src/github.com/google/cadvisor
WORKDIR /go/src/github.com/google/cadvisor
RUN make build

FROM arm32v7/debian
COPY --from=build /go/src/github.com/google/cadvisor/cadvisor /usr/bin/cadvisor
EXPOSE 8080
ENTRYPOINT ["/usr/bin/cadvisor", "-logtostderr"]
