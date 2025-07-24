---
title: nginx安装配置
date: 2018-03-22 15:44:57
tags: 
- nginx
---

# 配置参考

- [bitdata.conf](bitdata.conf) 推荐: gzip
- [pcmoto.conf](pcmoto.conf)
- [zx5435.com.conf](zx5435.com.conf) 推荐: ssl优化

# doc
- [x] nginx文档翻译系列 新手指南 [https://segmentfault.com/a/1190000006129358](https://segmentfault.com/a/1190000006129358)
- [x] Nginx的优化与防盗链 [http://os.51cto.com/art/201703/535326.htm](http://os.51cto.com/art/201703/535326.htm)

## 反向代理
```conf
server {
    listen       80 default_server;
    server_name  _;
    root         /;
}
server {
    listen       80;
    server_name  a.test.zx5435.com;

    location / {
        proxy_redirect      off;
        proxy_set_header    Host      $host;
        proxy_set_header    X-Real-IP $remote_addr;
        proxy_set_header    X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header    X-Forwarded-Proto $scheme;
        proxy_pass          http://127.0.0.1:666;
    }
}

// /websocket/ws to /ws
upstream svc_websocket {
    server svc-websocket:30080;
}
server {
    location /websocket/ {
        proxy_pass http://svc_websocket/;
        proxy_set_header Host $host;

        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";

        proxy_read_timeout 3600s;
        proxy_send_timeout 3600s;
    }
    location / {
        proxy_pass http://svc_gimc;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_set_header X-Scheme $scheme;
    }
}
```

## location 优先级问题
```conf
https://www.cnblogs.com/IPYQ/p/7889399.html
location ^~ /images/ {
    # 匹配任何以 /images/ 开头的地址，匹配符合以后，停止往下搜索正则，采用这一条。
}
```

## ali最佳配置

>配置解释 http://blog.csdn.net/tjcyjd/article/details/50695922
>配置解释 每一行 https://segmentfault.com/a/1190000016385662

```conf
log_format  main  '$remote_addr - $remote_user [$time_local] "$request" $http_host '
                            '$status $request_length $body_bytes_sent "$http_referer" '
                            '"$http_user_agent"  $request_time $upstream_response_time';
```

## ssl最佳配置
https://gist.github.com/fotock/9cf9afc2fd0f813828992ebc4fdaad6f

```text
user  www www;
worker_processes  1;

error_log  /alidata/log/nginx/error.log crit;
pid        /alidata/server/nginx/logs/nginx.pid;

worker_rlimit_nofile 65535;

events
{
    use epoll;
    worker_connections 65535;
}


http {
    include       mime.types;
    default_type  application/octet-stream;

    #charset  gb2312;

    server_names_hash_bucket_size 128;
    client_header_buffer_size 32k;
    large_client_header_buffers 4 32k;
    client_max_body_size 8m;

    sendfile on;
    tcp_nopush     on;

    keepalive_timeout 60;

    tcp_nodelay on;

    fastcgi_connect_timeout 300;
    fastcgi_send_timeout 300;
    fastcgi_read_timeout 300;
    fastcgi_buffer_size 64k;
    fastcgi_buffers 4 64k;
    fastcgi_busy_buffers_size 128k;
    fastcgi_temp_file_write_size 128k;

    gzip on;
    gzip_min_length  1k;
    gzip_buffers     4 16k;
    gzip_http_version 1.0;
    gzip_comp_level 2;
    gzip_types       text/plain application/x-javascript text/css application/xml;
    gzip_vary on;
    #limit_zone  crawler  $binary_remote_addr  10m;
    log_format '$remote_addr - $remote_user [$time_local] "$request" '
                  '$status $body_bytes_sent "$http_referer" '
                  '"$http_user_agent" "$http_x_forwarded_for"';
    include /alidata/server/nginx/conf/vhosts/*.conf;
}
```
