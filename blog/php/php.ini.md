---
title: php.ini配置
date: 2018-03-22 16:39:22
tags:
- php
---

# php.ini

```ini
;/usr/local/etc/php/php.ini
date.timezone = "Asia/Shanghai"

;opcache.md
opcache.revalidate_freq = 300
opcache.validate_timestamps = 1
opcache.max_accelerated_files = 7963
opcache.memory_consumption = 192
opcache.interned_strings_buffer = 16
opcache.fast_shutdown = 1
;other
opcache.huge_code_pages = 1
opcache.save_comments = 1

expose_php = Off

upload_max_filesize = 20m
post_max_size = 20m
```

# www.conf

```conf
;/usr/local/etc/php-fpm.d/www.conf
pm = dynamic
pm.max_children = 100
pm.start_servers = 10
pm.min_spare_servers = 10
pm.max_spare_servers = 50
pm.max_requests = 500

pm.max_children = $(($Mem/2/20))        8g=200
pm.start_servers = $(($Mem/2/30))       8g=150
pm.min_spare_servers = $(($Mem/2/40))   8g=100
pm.max_spare_servers = $(($Mem/2/20))   8g=200
```
