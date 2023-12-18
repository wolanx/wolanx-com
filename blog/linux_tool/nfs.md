---
title: nfs ossfs s3fs
date: 2023-12-18T12:00:00+08:00
tags: [linux]
---

## ossfs

```shell
wget https://gosspublic.alicdn.com/ossfs/ossfs_1.91.1_ubuntu22.04_amd64.deb
dpkg -i ossfs_1.91.1_ubuntu22.04_amd64.deb

dpkg --configure -a
apt-get -f install

echo cert:key > /etc/passwd-ossfs
chmod 600 /etc/passwd-ossfs

s3fs madex-test /www/minio-oss -o passwd_file=/etc/passwd-ossfs -o url=http://oss-cn-shanghai-internal.aliyuncs.com
umount /www/minio-oss
```
