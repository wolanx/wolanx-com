---
title: nginx https申请配置
date: 2018-03-22 15:44:57
tags:
  - ingress
---

# https

```shell
docker create \
  --name=letsencrypt \
  -v "$PWD/lets":/config \
  -e EMAIL=825407762@qq.com \
  -e URL=825407762.com \
  -e SUBDOMAINS=www \
  -e VALIDATION=http \
  -p 80:80 -p 443:443 \
  -e TZ=PRC \
  linuxserver/letsencrypt
```

```sh
## pfx => pem => key crt
# pfx => pem
openssl pkcs12 -in a.pfx -nodes -out a.pem
openssl rsa -in a.pem -out a.key
openssl x509 -in a.pem -out a.crt
kubectl create secret tls ccm-https --key a.key --cert a.crt --namespace=gim-uat
## k8s https 3 层
# pfx => crt
openssl pkcs12 -in a.pfx -nokeys -out a -passin 'pass:Welcome123'
# pfx => key
openssl pkcs12 -in a.pfx -nocerts -out b -nodes -passin 'pass:Welcome123'
cat a | base64 -w 0
cat b | base64 -w 0
```

## Version 2018/05/31 - Changelog: https://github.com/linuxserver/docker-letsencrypt/commits/master/root/defaults/ssl.conf

# session settings

```
ssl_session_timeout 1d;
ssl_session_cache shared:SSL:50m;
ssl_session_tickets off;
```

# Diffie-Hellman parameter for DHE cipher suites

ssl_dhparam /config/nginx/dhparams.pem;

# ssl certs

```
ssl_certificate /config/keys/letsencrypt/fullchain.pem;
ssl_certificate_key /config/keys/letsencrypt/privkey.pem;
```

# protocols

```
ssl_protocols TLSv1 TLSv1.1 TLSv1.2;
ssl_prefer_server_ciphers on;
ssl_ciphers 'ECDHE-RSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-RSA-AES256-GCM-SHA384:ECDHE-ECDSA-AES256-GCM-SHA384:DHE-RSA-AES128-GCM-SHA256:ECDHE-RSA-AES128-SHA256:ECDHE-ECDSA-AES128-SHA256:ECDHE-RSA-AES128-SHA:ECDHE-ECDSA-AES128-SHA:ECDHE-RSA-AES256-SHA384:ECDHE-ECDSA-AES256-SHA384:ECDHE-RSA-AES256-SHA:ECDHE-ECDSA-AES256-SHA:DHE-RSA-AES128-SHA256:DHE-RSA-AES128-SHA:DHE-RSA-AES256-SHA256:DHE-RSA-AES256-SHA:!aNULL:!eNULL:!EXPORT:!DES:!RC4:!MD5:!PSK:!aECDH:!EDH-DSS-DES-CBC3-SHA:!EDH-RSA-DES-CBC3-SHA:!KRB5-DES-CBC3-SHA';
```

# HSTS, remove # from the line below to enable HSTS

#add_header Strict-Transport-Security "max-age=63072000; includeSubDomains; preload" always;

# OCSP Stapling

ssl_stapling on;
ssl_stapling_verify on;

# certbot

- [x] 免费证书 [https://certbot.eff.org](https://certbot.eff.org)
- [x] 全民安全站Let's
  Encrypt配置NGINX [http://www.tuicool.com/articles/NVNvUf3](http://www.tuicool.com/articles/NVNvUf3)

certbot-auto certonly --webroot -w /alidata/www -d 825407762.com -d www.825407762.com

# docker

```
docker run -it -v "$PWD":/mk -w /mk -v "$PWD"/__cicd__/ssl:/etc/letsencrypt certbot/certbot certonly \
  --webroot --agree-tos --work-dir /mk --email 82547762@qq.com -d www.825407762.com -d 825407762.com -d hub.825407762.com

  location /.well-known {
    root /www/certbot;
  }
```

```shell
docker run -it -v "$PWD":/mk -w /mk -v "$PWD"/ssl:/etc/letsencrypt certbot/certbot certonly \
  --webroot --agree-tos --work-dir /mk --email 82547762@qq.com \
  -d ws.bitdata.com.cn \
  -d admin.bitdata.com.cn
docker run -it -v "$PWD":/mk -w /mk -v "$PWD"/ssl:/etc/letsencrypt certbot/certbot:v0.25.1 certonly \
  --webroot --agree-tos --work-dir /mk --email 82547762@qq.com \
  -d m.bitdata.com.cn \
  -d api.bitdata.com.cn \
  -d www.bitdata.com.cn \
  -d download.bitdata.com.cn
  -d admin.bitdata.com.cn
docker run -it -v "$PWD":/mk -w /mk -v "$PWD"/ssl:/etc/letsencrypt certbot/certbot:v0.25.1 certonly \
  --webroot --agree-tos --work-dir /mk --email 82547762@qq.com \
  -d bitdata.com.cn \
  -d s1.bitdata.com.cn

# input 输入webroot
/mk
```
