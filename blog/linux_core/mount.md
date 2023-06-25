---
title: mount fdisk 磁盘挂载
date: 2015-12-13
tags:
  - linux
---

# fdisk

    查看帮助（h）
    新建分区（n）
    删除分区（d）
    查看分区情况（p）
    写分区表并退出（w）

# mount

```sh
# 首先检查是否有硬盘未被挂载
fdisk -l

# 在分别输入n、p、1、2048、1048575999、w
fdisk /dev/vdb

# 对 1 分区格式化
mkfs.ext4 /dev/vdb1

# 新建目录
mkdir disk2

# 分区信息
cat /etc/fstab
echo '/dev/vdb1 /www ext4 defaults 0 0' >> /etc/fstab

# 加载新建分区 reload
mount -a
```

```
/etc/sysconfig/network-scripts/ifcfg-eth0 /etc/resolv.conf

7709f5e8-0d1a-4a02-8dde-aca8214bc46c

vi /etc/grub.d/40_custom
menuentry 'Install haikang'{
    search --no-floppy --fs-uuid --set=root 7709f5e8-0d1a-4a02-8dde-aca8214bc46c
    loopback loop /CentOS-7.6-hik-r5-patch3.iso
    linux16 (loop)/isolinux/vmlinuz linux repo=hd:/dev/disk/by-uuid/7709f5e8-0d1a-4a02-8dde-aca8214bc46c:/ nouveau.modeset=0
    initrd16 (loop)/isolinux/initrd.img
}
将以上命令中的 08879471-79d3-4d98-9380-c40bb4bc300b替换为记录的UUID（注意是两处），并保证CentOS-7-x86_64-Minimal-1804.iso镜像名称和下载的一致。

vi /etc/default/grub
修改或添加GRUB_DEFAULT=saved 为 GRUB_DEFAULT="CentOS-7-x86_64-Minimal-1804.iso"  注意和下载的镜像名称一致
```

# umount

```sh
yum install -y psmisc # fuser
fuser -km /mountdata/ # 释放链接
umount /mountdata # folder name
umount -f /mountdata
```
