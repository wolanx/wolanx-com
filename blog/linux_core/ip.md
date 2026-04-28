---
title: ip route
date: 2026-04-28
tags:
  - linux
---

### 多网卡，路由设置

```shell
ip route del default

# 172.0.0.0/8 指定网卡1
ip route add 172.0.0.0/8 via 192.168.1.1 dev eth1
# 默认路由走公网
ip route add default via 10.0.0.1 dev eth2
```

## ip route add 持久化

### interfaces 不推荐了，用（NetworkManager）

```shell title="/etc/network/interfaces"
auto eth2
iface eth2 inet dhcp
    # 如果DHCP提供了错误的网关，可以覆盖它
    # post-up ip route del default
    post-up ip route add default via 10.0.0.1 dev eth2

auto enx344b50000000
iface enx344b50000000 inet dhcp
    address 192.168.91.0/24
    up ip route add default via 192.168.91.1 dev enx344b50000000


# systemctl restart networking
```

### NetworkManager

```shell
# list
nmcli device status

# 启动连接
nmcli con up "my-usb-lan"

# 持久化 ip route add default xxx
vi /etc/NetworkManager/system-connections/usb-wifi1.nmconnection
[ipv4]
never-default=false
```
