---
title: docker 基础
date: 2018-03-22
tags: [ docker ]
---

## doc

- [x] Docker学习笔记 [https://segmentfault.com/a/1190000005930858](https://segmentfault.com/a/1190000005930858)
- [x] Docker 核心技术与实现原理 [https://draveness.me/docker](https://draveness.me/docker)
- [x] Docker 问答录（100问） [https://blog.lab99.org/post/docker-2016-07-14-faq.html](https://blog.lab99.org/post/docker-2016-07-14-faq.html)
- [x] Docker 实践系列文章 [https://segmentfault.com/a/1190000006449675](https://segmentfault.com/a/1190000006449675)

## install

### centos

```shell
sudo yum-config-manager --add-repo http://mirrors.aliyun.com/docker-ce/linux/centos/docker-ce.repo
yum list docker-ce --showduplicates | sort -r
sudo yum install -y docker-ce
```

### debian

```shell
# Debian Bullseye 11 (stable)
# Debian Buster 10 (oldstable)
# https://docs.docker.com/engine/install/debian/
apt-get install ca-certificates curl gnupg lsb-release
mkdir -p /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/debian/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/debian \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
apt update
apt-get install docker-ce docker-ce-cli containerd.io docker-compose-plugin
```

### 开机启动

```shell
systemctl status docker
systemctl enable docker

service docker restart
kill -SIGHUP $(pidof dockerd)
```

## config

```shell
cat > /etc/docker/daemon.json << EOF
{
  "registry-mirrors": [
    "https://registry.docker-cn.com"
  ],
  "log-opts": {"max-size": "500m", "max-file": "2"}
}
EOF
```

```json
{
  "debug": true,
  "registry-mirrors": [
    "https://registry.docker-cn.com"
  ],
  "log-driver": "loki",
  "log-opts": {
    "max-size": "500m",
    "max-file": "2",
    "loki-url": "http://192.168.2.238:3100/loki/api/v1/push"
  }
}
```

### root

docker exec -it --user=root 114 sh

### timezone 时区问题

```shell
# docker-compose.yml
environment:
  - TZ=utc-8

# k8s.yml
env:
  - name: TZ
    value: "utc-8"

# dpkg-reconfigure -f noninteractive tzdata
apk add tzdata --no-cache \
  && ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime \
  && echo "Asia/Shanghai" > /etc/timezone
```

## ops - maintain

### log

```shell
# 查看log大小
docker ps -q | xargs docker inspect --format="{{.LogPath}}" | xargs ls -lh

# nginx forward
RUN ln -sf /dev/stdout /var/log/nginx/access.log \
	&& ln -sf /dev/stderr /var/log/nginx/error.log
```

### prune

```shell
docker system prune -f

docker container prune -a --filter "until=72h"
docker volume prune --filter "label!=keep"
docker network prune --filter "until=24h"

docker image prune
docker image prune --filter "dangling=true"
docker image prune -a --filter "until=72h"
docker rmi $(docker images | grep "gimc-code" | tail -n +20 | awk '{print $3}')

crictl rm $(crictl ps -aq)
crictl rmi --prune
```

### image proxy

```shell
echo $CR_PAT | docker login ghcr.io -u zx5435 --password-stdin
docker pull registry.cn-hangzhou.aliyuncs.com/google_containers/tiller:v2.16.0
docker tag registry.cn-hangzhou.aliyuncs.com/google_containers/tiller:v2.16.0 gcr.io/kubernetes-helm/tiller:v2.16.0
```

### network

- iptables -t nat -L DOCKER -n --line-numbers
- iptables -nL -t nat

## tools

### ctop - container-top

```shell
# https://github.com/bcicen/ctop
sudo wget https://github.com/bcicen/ctop/releases/download/v0.7.7/ctop-0.7.7-linux-amd64 -O /usr/local/bin/ctop
sudo chmod +x /usr/local/bin/ctop
```
