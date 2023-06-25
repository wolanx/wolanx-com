---
title: Telegraf+Influxdb+Grafana 可视化监控系统搭建
date: 2018-03-22 16:14:49
tags:
  - linux
---

# Telegraf+Influxdb+Grafana 可视化监控系统搭建
------

参考 https://runnerlee.com/2017/08/18/influxdb-telegraf-grafana-monitor

## 全部配置

docker run --rm telegraf:1.4-alpine telegraf config

## influxdb curd

```shell
curl -XPOST "http://influxdb:8086/query" --data-urlencode "q=CREATE DATABASE telegraf"

curl -G "http://localhost:8086/query?pretty=true" --data-urlencode "db=mydb" \
  --data-urlencode "q=SELECT * FROM cpu WHERE host='server01' AND time < now() - 1d"

curl -G "influxdb:8086/query?pretty=true" --data-urlencode "db=telegraf" \
  --data-urlencode "q=SELECT * FROM nginx"
curl -G "influxdb:8086/query?pretty=true" --data-urlencode "db=telegraf" \
  --data-urlencode "q=show MEASUREMENTS"
```

- [./docker-compose.yml](./docker-compose.yml)
- [./telegraf.conf](./telegraf.conf)
