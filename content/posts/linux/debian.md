---
title: debian
date: 2021-06-18
categories:
  - linux
---

## 加速
```shell
# backup
cp /etc/apt/sources.list /etc/apt/sources.list.bak
sed 's/deb.debian.org/mirrors.aliyun.com/g' /etc/apt/sources.list
sed 's/security.debian.org/mirrors.aliyun.com/g' /etc/apt/sources.list

# run
sed -i 's/deb.debian.org/mirrors.aliyun.com/g' /etc/apt/sources.list
sed -i 's/security.debian.org/mirrors.aliyun.com/g' /etc/apt/sources.list
apt-get update -y
```

## common
```shell
apt-get install procps # top ps

apt-get install net-tools
apt-get install iputils-ping

apt-get install apt-transport-https ca-certificates # https
```

## vi bug
```shell
vi /etc/vim/vimrc.tiny
set nocompatible
set backspace=2
```
