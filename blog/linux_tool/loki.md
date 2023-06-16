---
title: loki grafana promtail
date: 2021-12-20T16:14:31+08:00
tags: [linux]
---


# docker-compose.yaml

```yaml
version: "3"

networks:
  loki:

services:
  loki:
    image: grafana/loki:2.4.0
    ports:
      - "3100:3100"
    command: -config.file=/etc/loki/local-config.yaml
    networks:
      - loki

  promtail:
    image: grafana/promtail:2.4.0
    volumes:
      - /var/lib/docker/containers:/var/lib/docker/containers
      - .:/etc/promtail
    command: -config.file=/etc/promtail/config.yml
    networks:
      - loki

  grafana:
    image: grafana/grafana:latest
    ports:
      - "3000:3000"
    networks:
      - loki
```

# config.yml
```yaml
server:
  http_listen_port: 9080
  grpc_listen_port: 0

positions:
  filename: /tmp/positions.yaml

clients:
  - url: http://loki:3100/loki/api/v1/push

scrape_configs:
  - job_name: system
    static_configs:
    - targets:
        - localhost
      labels:
        job: varlogs
        __path__: /var/log/*log

  - job_name: containers
    entry_parser: raw

    static_configs:
    - targets:
        - localhost
      labels:
        job: containerlogs
        __path__: /var/lib/docker/containers/*/*log

    # --log-opt tag="{{.ImageName}}|{{.Name}}|{{.ImageFullID}}|{{.FullID}}"
    pipeline_stages:

    - json:
        expressions:
          stream: stream
          attrs: attrs
          tag: attrs.tag

    - regex:
        expression: (?P<image_name>(?:[^|]*[^|])).(?P<container_name>(?:[^|]*[^|])).(?P<image_id>(?:[^|]*[^|])).(?P<container_id>(?:[^|]*[^|]))
        source: "tag"

    - labels:
        tag:
        stream:
        image_name:
        container_name:
        image_id:
        container_id:
```
