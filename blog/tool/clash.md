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

## clash-verge 新版 gui

- download https://github.com/clash-verge-rev/clash-verge-rev
- windows 便携版 https://github.com/clash-verge-rev/clash-verge-rev/releases/tag/v1.7.7

## proxy to server

```shell
# 本地端口转发（常用）
# -N：不执行远程命令，只做端口转发
# -f：后台运行
ssh -R 7897:127.0.0.1:7897 -N root@172.16.14.218
curl --proxy http://127.0.0.1:7897 https://google.com

vim /lib/systemd/system/docker.service

[Service]
Environment="HTTP_PROXY=http://127.0.0.1:7897"
Environment="HTTPS_PROXY=http://127.0.0.1:7897"
```

## Clash.Meta(改名为mihomo)

- download https://github.com/MetaCubeX/mihomo
- setting https://wiki.metacubex.one/startup/service/#systemd
- log journalctl -u mihomo -o cat -f

### config.yaml
```yaml
mixed-port: 7890
allow-lan: true
external-ui: public
external-controller: 0.0.0.0:9090
secret: 123456
```

## clash-docker

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
      - TZ=Etc/GMT-8
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


## proxy rule via ssh forward

```js
// clash mixin
// ssh -i ~/Desktop/kc/id_rsa_yjzhao-d -D 10086 yjzhao@jumphost-d.grundfos.cn -N
module.exports.parse = ({ content, name, url }, { yaml, axios, notify }) => {
    // return content
    content.proxies.push({
        name: "my-socks5",
        type: 'socks5',
        server: '127.0.0.1',
        port: 10086,
    })
    const newRules = [
        "DOMAIN-SUFFIX,rds.aliyuncs.com,my-socks5",
        "DOMAIN-SUFFIX,influxdata.tsdb.aliyuncs.com,my-socks5",
        "DOMAIN-SUFFIX,cn-shanghai-internal.aliyuncs.com,my-socks5",
        "IP-CIDR,10.231.0.0/16,my-socks5",
    ]
    content.rules = [...newRules, ...content.rules]
    
    return content
}
```
