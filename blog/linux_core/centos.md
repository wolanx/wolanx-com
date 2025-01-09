---
title: centos
date: 2017-04-29
tags:
  - linux
---

# 语言error

```sh
tee /etc/locale.conf <<-'EOF'
LANG="en_US.utf8"
#LC_ALL="en_US.utf8"
LC_ALL="C"
EOF

tee /root/.vimrc <<-'EOF'
set encoding=utf-8
set fileencoding=utf-8
EOF
```

# repo 修改源

```sh
# mv CentOS-Base.repo CentOS-Base.repo.bak
curl -o /etc/yum.repos.d/CentOS-Base.repo http://mirrors.aliyun.com/repo/Centos-7.repo
yum clean all
yum makecache #生产本地缓存
# yum-update
```

# epel 加好多rpm

```shell
yum install -y epel-release
amazon-linux-extras install epel # amazon-linux
```

# 常用必装

```sh
yum install -y yum-utils	# yum-config-manager --add-repo
yum install -y htop
yum install -y tree
yum install -y net-tools	# netstat -ntlp
yum install iputils         # ping
```

## 其他

### yum lock

yum-complete-transaction

### wifi

```shell
dmesg | grep firmware
ip addr show wlo1
wpa_supplicant -B -i wlo1 -c <(wpa_passphrase "iPhone 8" "1234567890")
```

### ssh remote

```shell
yum list installed | grep openssh-server
yum install openssh-server

/etc/ssh/sshd_config
PermitRootLogin yes
PasswordAuthentication yes

sudo service sshd start
```
