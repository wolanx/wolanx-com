---
title: virualbox 虚拟机
date: 2017-08-14
categories: [tool]
---

## 静态ip
```
// http://blog.csdn.net/johnnycode/article/details/50184073
/etc/sysconfig/network-scripts 路径下找到 ifcfg-*
修改eth0
cat /etc/sysconfig/network-scripts/ifcfg-eth0

// change
ONBOOT=yes #开机启动
BOOTPROTO=static #静态IP
// add
IPADDR=192.168.1.101 #本机地址
NETMASK=255.255.255.0 #子网掩码
GATEWAY=192.168.1.1 #默认网关

/etc/sysconfig/network
# Created by anaconda
DNS1=192.168.1.1
DNS2=8.8.8.8

service network restart

ip addr
```

## 共享目录
```
# 加载光驱 VBoxGuestAdditions_5.0.17-106140.iso
mount /dev/cdrom /media/cdrom
cd /media/cdrom

yum install kernel sources
yum install kernel-devel
yum install gcc

sh VBoxLinuxAdditions.run

cd /
mkdir ptest
mount -t vboxsf ptest /ptest

# 取消挂载
sudo umount -f /mnt/shared

lsmod | grep vboxsf
modprobe vboxsf
```

# mount命令
```sh
yum install -y psmisc # fuser

cat /etc/filesystems # 文件里是centos7支持的文件系统格式

fuser -km /mountdata/ # 释放链接
umount /mountdata

mkfs.xfs /dev/xvdb -f # 格式化

mount /dev/xvdb /mountdata
```

## u盘ubuntu
进入U盘安装界面时，可选中”try ubuntu without installing”，按下”e”,对出现的命令进行编辑，将”quiet splash —”删掉并换为”nvme_load=YES”，接着按下”F10”
