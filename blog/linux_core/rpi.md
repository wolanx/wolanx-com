---
title: 树莓派 rpi
date: 2020-08-15
tags:
  - linux
---

# raspberry pi

户名为 pi ，密码为 raspberry
ssh root@10.15.202.200

官网 https://www.raspberrypi.org/

download https://alpinelinux.org/downloads

Raspberry Pi OS (previously called Raspbian)
Win32DiskImager
硬盘 FAT32
电源 5v 3A

# config

```shell
sudo raspi-config
```

# windows远程访问的实现

apt-get install xrdp

https://www.instructables.com/id/Install-Alpine-Linux-on-Raspberry-Pi/

```
wpa_supplicant.conf

ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1
ap_scan=1
fast_reauth=1
country=CN
network={
	ssid="WIFI名称"
	psk="WIFI密码"
	priority=100
}
```

# repo

https://mirror.tuna.tsinghua.edu.cn/help/raspbian/

## buster

vi /etc/apt/sources.list
deb http://mirrors.tuna.tsinghua.edu.cn/raspbian/raspbian/ buster main non-free contrib rpi
deb http://mirrors.tuna.tsinghua.edu.cn/raspberry-pi-os/raspbian/ buster main non-free contrib rpi
deb-src http://mirrors.tuna.tsinghua.edu.cn/raspberry-pi-os/raspbian/ buster main non-free contrib rpi

/etc/apt/sources.list.d/raspi.list
deb http://mirrors.tuna.tsinghua.edu.cn/raspberrypi/ buster main ui

sudo apt-get update

# 必装

sudo apt install -y vim tree

# 视频 usb motion

sudo apt install motion
sudo motion
http://localhost:8081

## 开机启动

```sh
sudo vi /etc/default/motion
#no修改成yes:
start_motion_daemon=yes
```

## remote

```sh
sudo vi /etc/motion/motion.conf
# deamon off 改成 on
deamon on
# 设置分辨率
width 800
height 600
# 刷新率
framerate 30
streame_maxrate 30
# 关闭 localhost 的限制
stream_localhost off
webcontrol_localhost off
```

# samba win+linux 文件共享

# MJPGStreamer进行实时监控（USB摄像头篇）https://www.bilibili.com/video/BV1bt411c7fC?p=35

```shell
sudo apt-get install -y subversion
sudo apt-get install -y libjpeg8-dev
sudo apt-get install -y imagemagick
sudo apt-get install -y libv4l-dev
sudo apt-get install -y cmake
sudo git clone https://github.com/jacksonliam/mjpg-streamer.git
cd mjpg-streamer/mjpg-streamer-experimental
sudo make all
sudo make install
./mjpg_streamer -i "./input_uvc.so" -o "./output_http.so -w ./www"
./mjpg_streamer -i "./input_uvc.so -f 30 -r 800x600" -o "./output_http.so -w ./www"
http://192.168.100.39:8080/stream.html
```
