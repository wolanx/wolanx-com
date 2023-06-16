---
title: supervisor 多进程监控
date: 2017-03-09
tags: [linux]
---

## supervisor

- [x] 从安装到使用 https://www.jianshu.com/p/3658c963d28b

yum install -y supervisor

## start
supervisord -c /etc/supervisord.conf

## 开机启动

```shell
systemctl enable supervisord
systemctl is-enabled supervisord # check

supervisord : 启动supervisor
supervisorctl reload :修改完配置文件后重新启动supervisor
supervisorctl status :查看supervisor监管的进程状态
supervisorctl start 进程名 ：启动XXX进程
supervisorctl stop 进程名 ：停止XXX进程
supervisorctl stop all：停止全部进程，注：start、restart、stop都不会载入最新的配置文件。
supervisorctl update：根据最新的配置文件，启动新配置或有改动的进程，配置没有改动的进程不会受影响而重启

tail -f /var/log/supervisor/supervisord.log

cd /var/log/supervisor/
```

## /etc/supervisord.d/kline.ini

```text
[program:super_kline]
command=/gosrc/src/git.bitdata.com.cn/bitdata/ws/cmd/kafka/kline
autostart=true
autorestart=true
startsecs=10
stdout_logfile=/var/log/supervisor/super_kline.log
stderr_logfile=/var/log/supervisor/super_kline.log
stdout_logfile_backups=10
stderr_logfile_backups=10
stdout_logfile_maxbytes=10MB
stderr_logfile_maxbytes=10MB
stdout_capture_maxbytes=10MB
stderr_capture_maxbytes=10MB
```
