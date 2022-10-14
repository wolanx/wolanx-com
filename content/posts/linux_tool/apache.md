---
title: apache安装密钥
date: 2016-10-02
categories: [linux]
---

### Admin password

```text
docker run --rm httpd:2.4-alpine htpasswd -nbB admin 12341234

admin:$2y$05$1VZxOFif9eR0Or4eE6aj7.a8ccXUtO7zadQKU6Mmm7AFnL3WhZ7Xq   //有换行

or

echo "admin:$(openssl passwd -crypt admin123)" > .espasswd
```

## ab install

```shell
apt-get install apache2-utils
yum install httpd-tools

ab -c 50 -n 1000 http://api.bitdata.inner/
ab -c 1000 -n 10000 http://mgb.appcoachs.test/api/other/country
```

```text
Server Software:        nginx/1.12.2
Server Hostname:        api.bitdata.inner
Server Port:            80

Document Path:          /
Document Length:        191 bytes

Concurrency Level:      50
Time taken for tests:   19.608 seconds
Complete requests:      1000
Failed requests:        0
Total transferred:      661007 bytes
HTML transferred:       191000 bytes
Requests per second:    51.00 [#/sec] (mean)
Time per request:       980.379 [ms] (mean)
Time per request:       19.608 [ms] (mean, across all concurrent requests)
Transfer rate:          32.92 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        1    3  13.8      2     145
Processing:    48  953 835.3    741   10363
Waiting:       48  953 835.3    741   10363
Total:         50  957 835.5    743   10365

Percentage of the requests served within a certain time (ms)
  50%    743
  66%   1001
  75%   1227
  80%   1416
  90%   1973
  95%   2618
  98%   3455
  99%   3876
 100%  10365 (longest request)
 ```