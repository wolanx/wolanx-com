---
title: goaccess nginx日志分析
date: 2016-05-11
categories: [linux]
tags: [nginx]
---

## doc
- [x] nginx分析日志利器goaccess [http://www.jianshu.com/p/33e2e79d0373](http://www.jianshu.com/p/33e2e79d0373)

cat /usr/local/etc/goaccess.conf
```sh
time-format %T
date-format %d/%b/%Y
log-format %h %^[%d:%t %^] "%r" %s %b "%R" "%u"
```

cat 1.sh
```
#!/bin/bash
fname=$1
echo $fname
cd /alidata/log/nginx/access/
goaccess -f $fname -a > /alidata/www/log/index.html
goaccess  -a  -f /pcmoto/log/nginx/www_access.log -p /etc/goaccess.conf > /pcmoto/web/test/index.html
```

```
Overall
Unique visitors
Requested files
Requested static files
Not found URLs
Hosts
Operating Systems
Browsers
Time Distribution
Referrers URLs
Referring sites
Status codes
```