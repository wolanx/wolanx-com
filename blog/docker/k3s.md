---
title: k3s
date: 2019-12-16
tags: [docker]
---

## k3s

> Lightweight Kubernetes

```shell
# start
k3s server --docker --no-deploy=traefik

# systemd /etc/systemd/system/k3s.service
journalctl -u k3s -f # 日志
```

## config

```shell
cd /var/lib/rancher/k3s/server/manifests
/etc/rancher/k3s/k3s.yaml
```

## install

```shell
curl -sfL https://get.k3s.io | sh -
# images
wget https://github.com/rancher/k3s/releases/download/v1.0.0/k3s-airgap-images-amd64.tar
docker load --input k3s-airgap-images-amd64.tar

# download k3s bin
wget https://github.com/rancher/k3s/releases/download/v1.17.4%2Bk3s1/k3s
cp k3s /usr/local/bin/
chmod 777 /usr/local/bin/k3s
curl -sfL https://get.k3s.io > ~/a.sh

# reinstall
cp /usr/local/bin/k3s ~/k3s
cp ~/k3s /usr/local/bin/k3s
INSTALL_K3S_SKIP_DOWNLOAD=true sh a.sh server --docker --no-deploy=traefik
```

```text
[INFO]  Finding latest release
[INFO]  Using v1.0.0 as release
[INFO]  Downloading hash https://github.com/rancher/k3s/releases/download/v1.0.0/sha256sum-amd64.txt
[INFO]  Downloading binary https://github.com/rancher/k3s/releases/download/v1.0.0/k3s
[INFO]  Verifying binary download
[INFO]  Installing k3s to /usr/local/bin/k3s
which: no kubectl in (/root/.cargo/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/root/bin)
[INFO]  Creating /usr/local/bin/kubectl symlink to k3s
which: no crictl in (/root/.cargo/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/root/bin)
[INFO]  Creating /usr/local/bin/crictl symlink to k3s
which: no ctr in (/root/.cargo/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/root/bin)
[INFO]  Creating /usr/local/bin/ctr symlink to k3s
[INFO]  Creating killall script /usr/local/bin/k3s-killall.sh
[INFO]  Creating uninstall script /usr/local/bin/k3s-uninstall.sh
[INFO]  env: Creating environment file /etc/systemd/system/k3s.service.env
[INFO]  systemd: Creating service file /etc/systemd/system/k3s.service
[INFO]  systemd: Enabling k3s unit
Created symlink from /etc/systemd/system/multi-user.target.wants/k3s.service to /etc/systemd/system/k3s.service.
[INFO]  systemd: Starting k3s
```
