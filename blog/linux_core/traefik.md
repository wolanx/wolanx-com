---
title: traefik安装配置
date: 2025-07-28 11:10:00
tags:
  - ingress
---

## install

```yaml
name: admin
services:
  svc-ing:
    image: traefik:v2.10.4
    ports:
      - "80:80"
      - "443:443"
      - "8080:8080"
    network_mode: "host"
    command:
      #- "--log.level=DEBUG"
      - --accesslog
      - --api.insecure=true
      - --providers.docker=true
      - --providers.docker.exposedbydefault=false
      - --entrypoints.web.address=:80
      - --entrypoints.websecure.address=:443
      - --entrypoints.web.http.redirections.entrypoint.to=websecure
      - --entrypoints.web.http.redirections.entrypoint.scheme=https
    volumes:
      - /var/run/docker.sock:/var/run/docker.sock:ro
      - /acme
    environment:
      - TZ=Etc/GMT-8
```

## compose demo

### gis https

```yaml
    labels:
      - traefik.enable=true
      - traefik.http.routers.gimc.entrypoints=websecure
      - traefik.http.routers.gimc.tls=true
      - traefik.http.routers.gimc.rule=PathPrefix(`/`)
      - traefik.http.services.gimc.loadbalancer.server.scheme=http
      - traefik.http.services.gimc.loadbalancer.server.port=6201
      - traefik.http.routers.gimc.middlewares=add-x-scheme
      - traefik.http.middlewares.add-x-scheme.headers.customrequestheaders.X-Scheme=https
```

### websocket

```yaml
    labels:
      - traefik.enable=true
      - traefik.http.routers.myws.priority=100
      - traefik.http.routers.myws.entrypoints=websecure
      - traefik.http.routers.myws.tls=true
      - traefik.http.routers.myws.rule=PathPrefix(`/websocket`)
      - traefik.http.services.myws.loadbalancer.server.port=30080
      # rewrite
      - traefik.http.routers.myws.middlewares=myws-re
      - traefik.http.middlewares.myws-re.stripprefix.prefixes=/websocket
```
