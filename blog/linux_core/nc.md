---
title: nc 端口转发
date: 2017-04-27
tags:
  - linux
---

# nc 端口转发

- [x] 10 个例子教你学会 ncat (nc) 命令 https://linux.cn/article-9190-1.html

## 看 一个端口 通不通

```shell
# telnet 192.168.1.10 80
$ nc -zv 10.182.124.171 5432
Connection to 10.182.124.171 5432 port [tcp/postgresql] succeeded!
```

## 2台机器互传text

```sh
# A 起一个端口
nc -lk 5000
# B 链接 A
nc ip-a 5000
```

## 端口转发

### windows

netsh interface portproxy add v4tov4 connectaddress=127.0.0.1 connectport=2375 listenport=2376 protocol=tcp

```sh
yum install -y nmap-ncat

ncat -l 8080 #

ncat --sh-exec "ncat localhost 80" -l 7777 --keep-open
```
