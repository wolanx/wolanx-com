---
title: mysql 常用sql
date: 2018-03-20 10:41:33
tags:
  - db
---

### auth

```sql
update user
set host = '10.%.%.%'
where user = 'root';
select host, user
from user;

-- 只读账号
GRANT SELECT ON *.* TO 'read'@'%' IDENTIFIED BY '12341234';

-- 8.0 bug fix mysql_native_password
ALTER USER 'root'@'%' IDENTIFIED WITH mysql_native_password BY '12341234';
```

### user表每天注册数

```sql
SELECT from_unixtime(regdate, '%Y-%m-%d') AS regymd,
       count(1)                           AS num
FROM v9_member
GROUP BY regymd
ORDER BY regymd ASC;
```

### 日数据 以每月排

```sql
SELECT from_unixtime(time, '%Y%m') AS M,
       count(1)                    AS day_num,
       sum(payment_total)          AS payment_m
FROM echo_register_payment_info
GROUP BY M
ORDER BY m DESC;
```

### 复制表

```sql
CREATE TABLE `echo_total_databank`.`echo_controller2cname`
(
    `id`    INT(11) NOT NULL,
    `ename` VARCHAR(100) DEFAULT NULL,
    `cname` VARCHAR(100) DEFAULT NULL,
    `type`  VARCHAR(10)  DEFAULT NULL
) ENGINE = MyISAM
  DEFAULT CHARSET = utf8 COMMENT = 'echo-last-page-info控制器名称对应';

ALTER TABLE `echo_total_databank`.`echo_controller2cname`
    ADD PRIMARY KEY (`id`),
    ADD UNIQUE KEY `un` (`ename`) USING BTREE;

ALTER TABLE `echo_total_databank`.`echo_controller2cname`
    MODIFY `id` INT(11) NOT NULL AUTO_INCREMENT;

SET SQL_MODE = 'NO_AUTO_VALUE_ON_ZERO';

INSERT INTO `echo_total_databank`.`echo_controller2cname`
SELECT *
FROM `databank`.`echo_controller2cname`;
```
