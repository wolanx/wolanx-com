---
title: docker-compose
date: 2018-03-22
categories:
  - docker
tags:
---

## docker-compose

```shell
docker-compose ps

docker-compose logs --tail=100 -f
docker-compose logs --tail=100 -f svc-web

docker-compose restart svc-web
```

## install

```shell
# https://docs.docker.com/compose/install/#install-compose
yum install -y docker-compose
sudo curl -L https://github.com/docker/compose/releases/download/1.21.2/docker-compose-`uname -s`-`uname -m` -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
docker-compose --version
```

## tpl

### java + redis + influxdb

```yaml
version: "3"

services:

  svc-web:
    image: ghcr.io/wolanx/iothub-echo
    ports:
      - 1883:1883
      - 18830:8080
    entrypoint: java -cp /app/resources:/app/classes:/app/libs/* com.wolanx.echo.iothub.IotHubApplication
    volumes:
      - .:/root
    environment:
      - TZ=utc-8
      - JVM=-XX:+UseContainerSupport
      - REDIS_HOST=svc-redis
      - INFLUXDB_HOST=svc-influxdb
    networks:
      - mynet

  svc-redis:
    image: redis:6.0.3-alpine
    ports:
      - 6379:6379
    networks:
      - mynet

  svc-influxdb:
    image: influxdb:1.7.11
    ports:
      - 8086:8086
    environment:
      - TZ=utc-8
      - INFLUXDB_ADMIN_USER=root
      - INFLUXDB_ADMIN_PASSWORD=root
      - INFLUXDB_DB=iothub
      - INFLUXDB_HTTP_ENABLED=true
      - INFLUXDB_HTTP_AUTH_ENABLED=true
    networks:
      - mynet

networks:
  mynet:
```

### loki + grafana

```yaml
version: "3"

services:

  svc-loki:
    image: grafana/loki:2.4.0
    ports:
      - "3100:3100"
      - "9095:9095"
    command: -config.file=/etc/loki/local-config.yaml
    networks:
      - loki

  svc-grafana:
    image: grafana/grafana:latest
    ports:
      - "3000:3000"
    networks:
      - loki

networks:
  loki:
```
