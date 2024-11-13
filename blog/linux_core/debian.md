---
title: debian
date: 2021-06-18
tags: [linux]
---

## version

```shell
# cat /etc/os-release 
PRETTY_NAME="Debian GNU/Linux 12 (bookworm)"
NAME="Debian GNU/Linux"
VERSION_ID="12"
VERSION="12 (bookworm)"
VERSION_CODENAME=bookworm
```

## 加速
```shell
# backup
cp /etc/apt/sources.list /etc/apt/sources.list.bak

# run 10
sed -i 's/deb.debian.org/mirrors.aliyun.com/g' /etc/apt/sources.list
sed -i 's/security.debian.org/mirrors.aliyun.com/g' /etc/apt/sources.list
apt-get update -y

# run 12 (bookworm)
sed -i 's/deb.debian.org/mirrors.aliyun.com/g' /etc/apt/sources.list.d/debian.sources
sed -i 's/security.debian.org/mirrors.aliyun.com/g' /etc/apt/sources.list.d/debian.sources
apt-get update -y
```

## common
```shell
apt-get install procps # top ps

apt-get install net-tools
apt-get install iputils-ping # ping
apt-get install dnsutils # nslookup

apt-get install apt-transport-https ca-certificates # https
```

## user
```shell
adduser new_user
usermod -G sudo new_user # 将用户添加到sudo组中
su - new_user
```

## vi bug 方向键
```shell
vi /etc/vim/vimrc.tiny
set nocompatible
set backspace=2
```

## ubuntu 加速
```shell
cp /etc/apt/sources.list /etc/apt/sources.list.bak
sed 's/archive.ubuntu.com/mirrors.aliyun.com/g' /etc/apt/sources.list
sed 's/security.ubuntu.com/mirrors.aliyun.com/g' /etc/apt/sources.list

sed -i 's/archive.ubuntu.com/mirrors.aliyun.com/g' /etc/apt/sources.list
sed -i 's/security.ubuntu.com/mirrors.aliyun.com/g' /etc/apt/sources.list

apt update
```