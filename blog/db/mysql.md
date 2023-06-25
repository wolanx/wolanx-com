---
title: mysql 安装配置
date: 2018-03-20 10:41:33
tags:
  - db
---

# mysql

# doc

- [x] MYSQL最朴素的监控方式 状态指标 https://mp.weixin.qq.com/s/J7R8eJY8pNOnxLBOeSRlgA
- [x] 无限容量数据库架构设计 https://mp.weixin.qq.com/s/ad4tpM6cdi9r6vgfbaTzxg

## 时区

select now();
set global time_zone = '+8:00';

## commit 查看未提交事务

https://blog.csdn.net/u013235478/article/details/68062939
select trx_state, trx_started, trx_mysql_thread_id, trx_query from information_schema.innodb_trx;
show global variables LIKE '%wait_timeout%';

## processlist

# docker

```shell
docker run --restart=unless-stopped --name mysql-1 -it -d \
  -v "$PWD":/var/lib/mysql -p 3306:3306 -e MYSQL_ROOT_PASSWORD=12341234 -e TZ=Asia/Shanghai mysql:8.0.15 \
  --character-set-server=utf8mb4 --collation-server=utf8mb4_general_ci
docker run --restart=unless-stopped --name mysql-1 -it -d \
  -v "$PWD":/var/lib/mysql -p 3306:3306 -e MYSQL_ROOT_PASSWORD=12341234 -e TZ=Asia/Shanghai mysql:8.0.15 \
  --character-set-server=utf8 --collation-server=utf8_general_ci
docker run --restart=unless-stopped --name mysql-1 -it -d \
  -v "$PWD":/var/lib/mysql -p 3306:3306 -e MYSQL_ROOT_PASSWORD=12341234 -e TZ=Asia/Shanghai mysql:5.7.25 \
  --character-set-server=utf8 --collation-server=utf8_general_ci

# 导入 sql
docker exec -i gimclocal_svc-mysql-1_1 sh -c 'exec mysql -uroot -p"1234@1234"' < config/20221027.sql

# 加user https://www.cnblogs.com/xujishou/p/6306765.html
CREATE DATABASE IF NOT EXISTS `{$bundle}-app-test` default charset utf8 COLLATE utf8_general_ci;
grant all privileges on `{$bundle}-app-test`.* to `{$bundle}-app`@'%' identified by 'Abc.1234';
grant select on `gimc-prod`.* to `gtest`@'%';
grant select on `gimc-prod\_%`.* to `gtest`@'%';

# 修改时区
cp /usr/share/zoneinfo/GMT /etc/localtime
cp /usr/share/zoneinfo/PRC /etc/localtime
docker cp /etc/localtime mysql-1:/etc/localtime
docker cp /usr/share/zoneinfo/PRC mysql-1:/etc/localtime

SHOW VARIABLES LIKE 'character%';

# cnf
/etc/mysql/mysql.conf.d/mysqld.cnf
/etc/mysql/my.cnf

show tables;
show table status; # 大小行数more
```

## table

```sql
CREATE TABLE `table_demo`
(
    `id`         int(11)    NOT NULL AUTO_INCREMENT,
    `status`     tinyint(1) NOT NULL DEFAULT '1' COMMENT '状态',
    `created_at` timestamp  NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
    `updated_at` timestamp  NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间',
    PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB
  DEFAULT CHARSET = utf8 COMMENT ='参考';
```

## optmize + repair

```sh
#!/bin/bash

host_name=localhost  
user_name=haohe_club  
user_pwd=iy9nPKJV   
database=club  
need_optmize_table=true  
tables=$(mysql -h$host_name -u$user_name -p$user_pwd $database -A -Bse "show tables")  

for table_name in $tables  
do  
  check_result=$(mysql -h$host_name -u$user_name -p$user_pwd $database -A -Bse "check table $table_name" | awk '{ print $4 }')  
  if [ "$check_result" = "OK" ]  
  then  
    echo "It's no need to repair table $table_name"  
  else  
    echo $(mysql -h$host_name -u$user_name -p$user_pwd $database -A -Bse "repair table $table_name")  
  fi  

  # 优化表,可提高性能  
  if [ $need_optmize_table = true ]  
  then  
    echo $(mysql -h$host_name -u$user_name -p$user_pwd $database -A -Bse "optimize table $table_name")  
  fi  
done  
```
