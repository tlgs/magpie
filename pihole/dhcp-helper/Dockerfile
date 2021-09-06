FROM alpine:3.14
RUN apk --no-cache add dhcp-helper=1.2-r0
EXPOSE 67 67/udp
ENTRYPOINT ["dhcp-helper", "-n"]
