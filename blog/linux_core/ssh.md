---
title: ssh && autossh
date: 2015-12-13
tags:
  - linux
---

## 无密码登录

    ssh-keygen -t rsa -P '' -f ~/.ssh/id_rsa
    cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys

## pem

    ssh-keygen -t rsa -P '' -f ~/.ssh/id_zyj
    openssl rsa -in ~/.ssh/id_zyj -outform pem > id_zyj.pem
    chmod 700 id_zyj.pem


## install sshd

```shell
apt-get install openssh-server

# 修改ssh默认端口
vim /etc/ssh/sshd_config
# PermitRootLogin yes

service sshd restart
systemctl restart sshd
```

## autossh 内网穿透

https://www.cnblogs.com/kwongtai/p/6903420.html

```sh
# 在inner机器用777远端开启9292
ssh -fCNR 9292:localhost:777 root@101.132.151.41
# mysql 代理
ssh -fNg -L 3307:10.10.75.22:3306 -p 22 root@101.1.5.53

# ssh -fCNR [B机器IP或省略]:[B机器端口]:[A机器的IP]:[A机器端口] [登陆B机器的用户名@服务器IP]
# autossh
autossh -f -M Bport监控 -fCNR Bport:Aip:Aport root@Bip
autossh -f -M 6023 -fCNR 6022:localhost:22 -p1022 root@101.132.77.68 # 远程ssh
autossh -f -M 7002 -fCNR 7001:localhost:7003 -p1022 root@101.132.77.68
autossh -f -M 7778 -fCNR 7777:localhost:777 root@101.132.151.41
```

# expect iterm 登录

```sh
set user zhaoyujie
set password qwerqwer
set timeout -1

spawn ssh -p2222 -i ~/Desktop/docs/zhaoyujie-jumpserver.pem $user@47.101.140.238
expect "*assword:*"
send "$password\r"
# expect "Opt>*"
# send "\r"
interact
#expect eof
```

# vpn

https://www.jianshu.com/p/4801adfcd07e
