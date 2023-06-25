---
title: crontab设置
date: 2017-12-13
tags:
  - linux
---

# crontab

```shell
echo $(docker-compose exec php ps -ef | grep crond)
docker-compose exec -T php crond -l 0 -L /var/runtime/crontab.log

docker-compose exec php crontab environments/$1/test/crontab

docker-compose exec php crontab -l
```

## base

```text
# min   hour    day     month   weekday command
*/15    *       *       *       *       run-parts /etc/periodic/15min
0       *       *       *       *       run-parts /etc/periodic/hourly
0       2       *       *       *       run-parts /etc/periodic/daily
0       3       *       *       6       run-parts /etc/periodic/weekly
0       5       1       *       *       run-parts /etc/periodic/monthly
```

## 常用

```text
# prod
YII=/www/yii
LOG_DIR=/www/console/runtime/crontab

# min   hour    day     month   weekday command
*/1     *       *       *       *       php $YII zhao/test/hello >> $LOG_DIR/test.log 2>&1
```
