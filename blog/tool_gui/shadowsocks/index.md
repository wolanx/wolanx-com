---
title: shadowsocks
date: 2017-03-16
tags:
  - 工具
---

# server 远端建立

http://www.360doc.com/content/15/1026/10/36628_508421823.shtml

```sh
vi /etc/shadowsocks.json
{
  "server": "0.0.0.0",
  "server_port": 8388,
  "local_address": "127.0.0.1",
  "local_port": 1080,
  "password": "",
  "timeout": 300,
  "method": "aes-256-cfb",
  "fast_open": false,
  "workers": 1
}

ssserver -c /etc/shadowsocks.json

vi /etc/rc.local
/usr/local/bin/ssserver -c /etc/shadowsocks/config.json
```

# client 本地

## gui 下载

https://github.com/shadowsocks/shadowsocks-windows

## go build

go get -v github.com/shadowsocks/shadowsocks-go/cmd/shadowsocks-local

## config

```shell
{
  "server": "116.246.13.86",
  "server_port": 40121,
  "password": "Py72*N%tNa8!",
  "method": "aes-256-cfb",
  "remarks": "test",
  "timeout": 5
}
{
  "server": "101.1.5.39",
  "server_port": 5838,
  "local_address": "192.168.199.201",
  "local_port": 2580,
  "password": "3fgOk2&J5H",
  "timeout": 300,
  "method": "rc4-md5",
  "fast_open": false,
  "workers": 1
}
20152
n64UKqLA4nGCqaP
chacha20-ietf-poly1305
au1-sta11.3a281.site
```

## gee 极路由

ssh -p 1022 root@192.168.199.1

https://github.com/qiwihui/hiwifi-ss
