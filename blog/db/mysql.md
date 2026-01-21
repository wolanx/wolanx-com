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
    `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
    `updated_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间',
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

## partition 分区

```sql
-- 速度优化 ALGORITHM=INPLACE, LOCK=NONE;
ALTER TABLE t1
    ADD INDEX idx_name (name), ALGORITHM=INPLACE, LOCK=NONE;

-- 删除分区（数据也会被删除）
ALTER TABLE table_name DROP PARTITION p_old;

-- 只删除数据，保留分区结构
ALTER TABLE table_name TRUNCATE PARTITION p_old;
```

### 分区状态

```sql
SELECT PARTITION_NAME,
       TABLE_ROWS,
       CONCAT(ROUND((DATA_LENGTH + INDEX_LENGTH) / 1024 / 1024, 2), ' MB') as 'size', CONCAT(ROUND(DATA_FREE / 1024 / 1024, 2), ' MB') as 'free'
FROM information_schema.PARTITIONS
WHERE TABLE_SCHEMA = 'gimc-dev2' and TABLE_NAME = 'ept_online_real_wave_daily';
```

### ept_online_real_wave_daily

```sql
ALTER TABLE ept_online_real_wave_daily
    PARTITION BY RANGE ( id )
    (
    PARTITION p202401 VALUES LESS THAN (1741489387729846272),
    PARTITION p202402 VALUES LESS THAN (1752723411563446272),
    PARTITION p202403 VALUES LESS THAN (1763232659665846272),
    PARTITION p202404 VALUES LESS THAN (1774466683499446272),
    PARTITION p202405 VALUES LESS THAN (1785338319467446272),
    PARTITION p202406 VALUES LESS THAN (1796572343301046272),
    PARTITION p202407 VALUES LESS THAN (1807443979269046272),
    PARTITION p202408 VALUES LESS THAN (1818678003102646272),
    PARTITION p202409 VALUES LESS THAN (1829912026936246272),
    PARTITION p202410 VALUES LESS THAN (1840783662904246272),
    PARTITION p202411 VALUES LESS THAN (1852017686737846272),
    PARTITION p202412 VALUES LESS THAN (1862889322705846272),
    PARTITION p202501 VALUES LESS THAN (1874123346539446272),
    PARTITION p202502 VALUES LESS THAN (1885357370373046272),
    PARTITION p202503 VALUES LESS THAN (1895504230609846272),
    PARTITION p202504 VALUES LESS THAN (1906738254443446272),
    PARTITION p202505 VALUES LESS THAN (1917609890411446272),
    PARTITION p202506 VALUES LESS THAN (1928843914245046272),
    PARTITION p202507 VALUES LESS THAN (1939715550213046272),
    PARTITION p202508 VALUES LESS THAN (1950949574046646272),
    PARTITION p202509 VALUES LESS THAN (1962183597880246272),
    PARTITION p202510 VALUES LESS THAN (1973055233848246272),
    PARTITION p202511 VALUES LESS THAN (1984289257681846272),
    PARTITION p202512 VALUES LESS THAN (1995160893649846272),
    PARTITION p202601 VALUES LESS THAN (2006394917483446272),
    PARTITION p202602 VALUES LESS THAN (2017628941317046272),
    PARTITION p202603 VALUES LESS THAN (2027775801553846272),
    PARTITION p202604 VALUES LESS THAN (2039009825387446272),
    PARTITION p202605 VALUES LESS THAN (2049881461355446272),
    PARTITION p202606 VALUES LESS THAN (2061115485189046272),
    PARTITION p202607 VALUES LESS THAN (2071987121157046272),
    PARTITION p202608 VALUES LESS THAN (2083221144990646272),
    PARTITION p202609 VALUES LESS THAN (2094455168824246272),
    PARTITION p202610 VALUES LESS THAN (2105326804792246272),
    PARTITION p202611 VALUES LESS THAN (2116560828625846272),
    PARTITION p202612 VALUES LESS THAN (2127432464593846272),
    PARTITION p202701 VALUES LESS THAN (2138666488427446272),
    PARTITION p_future VALUES LESS THAN MAXVALUE
    );

-- 把 分区 a 拆解成 a1 a2
ALTER TABLE ept_online_real_wave_daily REORGANIZE PARTITION p202401 INTO (
    PARTITION p202306 VALUES LESS THAN (1663938384491446272),
    PARTITION p202307 VALUES LESS THAN (1674810020459446272),
    PARTITION p202308 VALUES LESS THAN (1686044044293046272),
    PARTITION p202309 VALUES LESS THAN (1697278068126646272),
    PARTITION p202310 VALUES LESS THAN (1708149704094646272),
    PARTITION p202311 VALUES LESS THAN (1719383727928246272),
    PARTITION p202312 VALUES LESS THAN (1730255363896246272),
    PARTITION p202401 VALUES LESS THAN (1741489387729846272)
);
```

### 分区 生成 脚本

```pycon
from datetime import datetime


def gen(ya, ma, yb, mb):
    total_months = (yb - ya) * 12 + (mb - ma) + 1

    y1, m1 = ya, ma

    for i in range(total_months):
        ms = int(datetime(y1, m1, 1).timestamp() * 1000)
        partition_value = (ms - 1288834974657) << 22
        month_str = f"{y1}{m1:02d}"

        print(f"    PARTITION p{month_str} VALUES LESS THAN ({partition_value}),")
        m1 += 1
        if m1 > 12:
            m1 = 1
            y1 += 1

    print("    PARTITION p_future VALUES LESS THAN MAXVALUE")


gen(2024, 1, 2027, 1)
```
