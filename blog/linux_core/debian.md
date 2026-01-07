---
title: debian
date: 2021-06-18
tags: [linux]
---

## install

- https://mirrors.tuna.tsinghua.edu.cn/debian-cd/12.11.0-live/amd64/iso-hybrid/

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
sed -i 's/deb.debian.org/mirrors.aliyun.com/g' /etc/apt/sources.list
sed -i 's/security.debian.org/mirrors.aliyun.com/g' /etc/apt/sources.list
mv /etc/apt/sources.list.d/debian.sources /etc/apt/sources.list.d/debian.sources.bak
apt-get update -y
```

### debian 12 bookworm

- doc https://mirrors.tuna.tsinghua.edu.cn/help/debian
- demo /etc/apt/sources.list.d/debian.sources

```text
Types: deb
URIs: https://mirrors.tuna.tsinghua.edu.cn/debian
Suites: bookworm bookworm-updates bookworm-backports
Components: main contrib non-free non-free-firmware
Signed-By: /usr/share/keyrings/debian-archive-keyring.gpg

# 默认注释了源码镜像以提高 apt update 速度，如有需要可自行取消注释
# Types: deb-src
# URIs: https://mirrors.tuna.tsinghua.edu.cn/debian
# Suites: bookworm bookworm-updates bookworm-backports
# Components: main contrib non-free non-free-firmware
# Signed-By: /usr/share/keyrings/debian-archive-keyring.gpg

# 以下安全更新软件源包含了官方源与镜像站配置，如有需要可自行修改注释切换
Types: deb
URIs: https://security.debian.org/debian-security
Suites: bookworm-security
Components: main contrib non-free non-free-firmware
Signed-By: /usr/share/keyrings/debian-archive-keyring.gpg

# Types: deb-src
# URIs: https://security.debian.org/debian-security
# Suites: bookworm-security
# Components: main contrib non-free non-free-firmware
# Signed-By: /usr/share/keyrings/debian-archive-keyring.gpg
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

## ntp timezone

```shell
# 安装 systemd-timesyncd
sudo apt update
sudo apt install systemd-timesyncd

# 启用并启动服务
sudo systemctl enable systemd-timesyncd
sudo systemctl start systemd-timesyncd

# 检查状态
sudo timedatectl set-ntp true
sudo timedatectl status
sudo timedatectl set-timezone Asia/Shanghai
```

## df -h

```shell
# 调整大小
# 1. 切换到 root 并进入单用户模式
sudo -i
systemctl isolate rescue.target

# 2. 卸载 /home
umount /home

# 3. 检查并修复文件系统
e2fsck -f /dev/mapper/debian--vg-home

# 4. 缩小 /home 逻辑卷（示例：缩小 200G，剩下约 650G）
# 先缩小文件系统：
resize2fs /dev/mapper/debian--vg-home 650G

# 再缩小逻辑卷（必须与上面大小一致！）：
lvreduce -L 650G /dev/mapper/debian--vg-home

# 5. 扩展根分区
# 扩展逻辑卷（+200G 或使用所有可用空间）：
lvextend -l +100%FREE /dev/mapper/debian--vg-root

# 扩展文件系统：
resize2fs /dev/mapper/debian--vg-root

mount -a # 6. 重新挂载
reboot
```
