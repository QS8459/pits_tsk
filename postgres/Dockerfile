FROM alpine:latest

RUN apk --no-cache update sudo bash && \
    apk add nano \
    postgresql15 postgresql15-contrib postgresql15-openrc postgresql15-client libpq su-exec tzdata\
    postgresql-url_encode && \
#     rm --rf /var/cache/apk/* && \
    mkdir /docker-entrypoint-initdb.d \

ENV LANG en_GB.utf8
ENV PGDATA /var/lib/postgresql/data

RUN addgroup -S pitsburg && adduser pitsburg -S -G pitsburg pitsburg

RUN echo "pitsburg:admin" | chpasswd

RUN echo "pitsburg ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers

VOLUME /var/lib/postgresql/data

COPY --chown=pitsburg:pitsburg docker-entrypoint.sh /

ENTRYPOINT ["/docker-entrypoint.sh"]

EXPOSE 5432

RUN chmod -R 755 /docker-entrypoint.sh &&\
    mkdir -p /run/postgresql &&\
    chown postgres: /run/postgresql

WORKDIR /pitsburg

#USER pitsburg

CMD ["postgres"]