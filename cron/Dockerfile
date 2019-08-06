FROM alpine:3.7

RUN apk add --no-cache curl

RUN mkdir /etc/periodic/5min

RUN echo -e "#!/bin/sh\n\ncurl -L app:8000/subdiscovery/find_subdomains/" > /etc/periodic/5min/findsubs

RUN chmod +x /etc/periodic/5min/findsubs

RUN echo "*/5 * * * * run-parts /etc/periodic/5min" >> /etc/crontabs/root

ENTRYPOINT ["crond", "-f", "-L", "/dev/stdout"]

