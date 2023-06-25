---
title: xdebug配置
date: 2017-09-11
tags:
  - php
---

# docker PHPSTORM

- [x] PhpStorm + Docker LNMP 中 Xdebug 配置 https://www.jianshu.com/p/c40a27129aca

PHPSTORM setting

- Language php Debug => Xdebug port 9001
- Language php Debug/DBGp => port:901 #项目的port
- Language php Servers => Name:server-def, Host:0.0.0.0:901, Port:901, 右边map:/www # 项目文件夹

```docker.yml
      environment:
        PHP_IDE_CONFIG: "serverName=server-def"
      volumes:
        - ./__cicd__/php/xdebug.ini:/usr/local/etc/php/conf.d/docker-php-ext-xdebug.ini
```

```ini
[xdebug]
;./__cicd__/php/xdebug.ini:/usr/local/etc/php/conf.d/docker-php-ext-xdebug.ini
zend_extension = /usr/local/lib/php/extensions/no-debug-non-zts-20160303/xdebug.so
xdebug.remote_handler = dbgp
xdebug.remote_port = 9001
xdebug.remote_host = 192.168.1.203
xdebug.remote_enable = 1
xdebug.remote_connect_back = 0
xdebug.profiler_enable = 1
xdebug.idekey = PHPSTORM
xdebug.remote_log = "/tmp/xdebug.log"
```
