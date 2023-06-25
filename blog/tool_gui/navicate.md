---
title: navicat
date: 2020-01-08
tags:
  - 工具
---

```shell
docker stop lubuntu
docker rm lubuntu

docker run -d --hostname lubuntu --name lubuntu --restart always --privileged -p 9092:5901 -e TZ=Asia/Jakarta vncserver/lubuntu

docker cp /www/navicate lubuntu:/home/developer/navicate
docker cp lubuntu:/home/developer/navicate navicate

docker run -d --hostname lubuntu --name lubuntu --restart always --privileged -p 9092:5901 -e TZ=Asia/Jakarta \
  -v /www/navicate/app:/home/developer/app -v /www/navicate/config:/home/developer/.config/navicat \
  vncserver/lubuntu

docker exec -u developer -it lubuntu bash

过期删 MySQL rm -rf preferences.json*

```

# vnc

```shell
docker run -d --hostname lubuntu --name lubuntu --restart always --privileged -p 9092:5901 -e TZ=Asia/Jakarta vncserver/lubuntu
```
