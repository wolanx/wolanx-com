---
title: php opcache
date: 2018-03-22 16:39:22
tags:
  - php
---

# opcache

- [x] 使用 opcache 优化生产环境 PHP https://segmentfault.com/a/1190000009724016

```text
开发模式下推荐，直接禁用opcache扩展更好

opcache.revalidate_freq=0
opcache.validate_timestamps=1
opcache.max_accelerated_files=3000
opcache.memory_consumption=192
opcache.interned_strings_buffer=16
opcache.fast_shutdown=1


多台机器集群模式或者代码更新频繁时推荐，可以兼顾性能，方便代码更新

opcache.revalidate_freq=300
opcache.validate_timestamps=1
opcache.max_accelerated_files=7963
opcache.memory_consumption=192
opcache.interned_strings_buffer=16
opcache.fast_shutdown=1


稳定项目推荐，性能最好

opcache.revalidate_freq=0
opcache.validate_timestamps=0
opcache.max_accelerated_files=7963
opcache.memory_consumption=192
opcache.interned_strings_buffer=16
opcache.fast_shutdown=1

;other
opcache.huge_code_pages = 1
opcache.save_comments = 1
```