---
title: clash 设置
date: 2018-04-04 16:26:02
categories:
  - tool
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
