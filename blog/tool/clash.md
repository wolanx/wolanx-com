---
title: clash 设置
date: 2018-04-04 16:26:02
tags: [ tool ]
---

## clash

```shell
# install win mac
https://github.com/Fndroid/clash_for_windows_pkg/releases
https://github.com/Fndroid/clash_for_windows_pkg/releases/download/0.19.12/Clash.for.Windows.Setup.0.19.12.exe
D:\clash

# setting
https://docs.cfw.lbyczf.com/contents/quickstart.html
https://portal.shadowsocks.nz/knowledgebase/182/

# shell
host_ip=$(cat /etc/resolv.conf |grep "nameserver" |cut -f 2 -d " ")
export ALL_PROXY="http://$host_ip:7890"
export ALL_PROXY="http://127.0.0.1:7890"
```

## trojan

https://github.com/trojan-gfw/trojan/releases
tar -xvf trojan-1.16.0-linux-amd64.tar.xz

"cert": "/etc/pki/ca-trust/extracted/pem/tls-ca-bundle.pem",

## docker

- api https://clash.wiki/runtime/external-controller.html
- dashboard http://localhost:17890/ui/#/proxies

> cd /etc/clash

```yaml title="docker-compose.yml"
version: "3"
services:
  svc-clash:
    image: dreamacro/clash
    restart: always
    ports:
      - "7890:7890"
      - "17890:9090"
    volumes:
      - .:/root/.config/clash
    environment:
      - TZ=utc-8
```

```yaml title="docker-compose.yml"
mixed-port: 7890
allow-lan: true
external-controller: 0.0.0.0:9090
external-ui: /root/.config/clash/ui

#secret: bb975c61-c6b6-4ffe-9a22-0f5d00d7342e

# 后半段 copy windows profiles 里的内容
```

```shell
export http_proxy=http://127.0.0.1:7890
export https_proxy=http://127.0.0.1:7890
export ALL_PROXY=http://127.0.0.1:7890
# 测试代理可用
curl -i google.com
# 在终端取消代理
unset http_proxy
unset https_proxy
```


## ssh forward use proxy rule

```js

```
