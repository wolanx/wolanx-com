---
title: rancher
date: 2018-03-22T16:14:32+08:00
tags: [linux]
---

## rancher

```shell
sudo docker run -d --restart=unless-stopped -p 8080:8080 rancher/server:stable

sudo docker run --rm --privileged \
 -v /var/run/docker.sock:/var/run/docker.sock \
 -v /var/lib/rancher:/var/lib/rancher \
  rancher/agent:v1.2.9 http://192.168.199.7:8080/v1/scripts/DBB33093FAD05C390C97:1514678400000:g38ksyRrU9Badhb36BjQmckY1j8
```
