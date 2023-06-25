---
title: mysqldump备份 导入导出
date: 2018-03-20 10:41:33
tags:
  - db
---

# 备份

docker exec mysql-1 sh -c 'mysqldump --all-databases -uroot -p12341234' > /www/1.sql
docker exec mysql-1 sh -c 'mysqldump -uroot -p12341234' gfTest > /www/1.sql

## 导出 sh

```shell
Now=$(date +"%Y%m%d_%H%M%S");
File=gaojian_$Now.sql;

/alidata/server/mysql-5.6.21/bin/mysqldump -h127.0.0.1 -ugaojian -p'gaojian123' gaojian > /alidata/www/gaojian/caches/bakup/sql/$File;

mysqldump -hlocalhost -uhaohe_test -p'iy9nPKJV' --skip-lock-tables pcmoto > ./a.sql

echo "Your Database Backup Successfully Completed";
```

## 导入

```shell
source d:\1.sql
```

docker exec mysql-1 sh -c 'mysqldump --all-databases -uroot -pbitdata' > /www/11_23.sql
docker exec mysql-1 sh -c 'mysqldump --databases coin -uroot -pbitdata' > /www/2.sql

mysqldump -u root -p --compatible=postgresql --default-character-set=utf8 at-dev > 1.sql

docker exec mysql-1 sh -c 'mysql -uroot -pbitdata' < /www/11_23.sql

create database coin default character set utf8mb4;

docker run --restart=unless-stopped --name mysql-2 -it -d -v "$PWD":/var/lib/mysql -p 3306:3306 -e
MYSQL_ROOT_PASSWORD=bitdata mysql:5.6.39 --character-set-server=utf8 --collation-server=utf8_general_ci

# source 加速

SET GLOBAL foreign_key_checks=0;
SET GLOBAL unique_checks=0;
SET GLOBAL innodb_flush_log_at_trx_commit=0;
SET GLOBAL sync_binlog=0;

SET GLOBAL foreign_key_checks=1;
SET GLOBAL unique_checks=1;
SET GLOBAL innodb_flush_log_at_trx_commit=1;
SET GLOBAL sync_binlog=1;
