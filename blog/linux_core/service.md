---
title: service
date: 2020-02-18
tags:
  - linux
---

# doc

```sh

# 所有的 service
systemctl list-units --type=service

# 看日志
journalctl -u k3s -f

service nginx status
service nginx start
service nginx restart
service nginx stop

```

# file list

```shell
cd /usr/lib/systemd/system
cd /etc/systemd/system/
```

# k3s.service demo

```
[Unit]
Description=Lightweight Kubernetes
Documentation=https://k3s.io
Wants=network-online.target

[Install]
WantedBy=multi-user.target

[Service]
Type=notify
EnvironmentFile=/etc/systemd/system/k3s.service.env
KillMode=process
Delegate=yes
LimitNOFILE=infinity
LimitNPROC=infinity
LimitCORE=infinity
TasksMax=infinity
TimeoutStartSec=0
Restart=always
RestartSec=5s
ExecStartPre=-/sbin/modprobe br_netfilter
ExecStartPre=-/sbin/modprobe overlay
ExecStart=/usr/local/bin/k3s \
    server \
        '--docker' \
```
