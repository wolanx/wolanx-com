---
title: postgresql 基础
date: 2018-08-02 10:42:09
tags:
  - db
---

# pg

- [ ] 预览 https://github.com/Vonng/pg
- [x] PG好处都有啥 https://github.com/Vonng/pg/blob/master/misc/pg-yoxi.md
  后端懒得写怎么办
  需要用到Redis的功能
  需要做分析
  用到地理
  存储时序数据
  流计算
  任意程序的输出，监控系统信息
- [ ] PostgreSQL, Greenplum 培训视频下载 https://github.com/digoal/blog

# postgres

```shell
docker run --restart=unless-stopped --name pg-1 -it -d -v "$PWD":/var/lib/postgresql/data -p 5432:5432 -e POSTGRES_PASSWORD=12341234 postgres:10.5
docker exec -it --user=postgres -w /var/lib/postgresql/data pg-1 sh
psql -d at-dev -U postgres -f 1.sql
```

# pgadmin

docker run --restart=unless-stopped --name pgadmin -d -p 54320:80 -e "PGADMIN_DEFAULT_EMAIL=admin" -e "
PGADMIN_DEFAULT_PASSWORD=12341234" dpage/pgadmin4

# timescale

docker run --restart=unless-stopped --name timescaledb -it -d -v "$PWD":/var/lib/postgresql/data -p 5432:5432 -e
POSTGRES_PASSWORD=12341234 timescale/timescaledb:0.11.0-pg10

# connect

docker exec -it timescaledb psql -U postgres

# 配置

- [x] PostgreSQL配置优化 https://cloud.tencent.com/developer/article/1030449

```conf
max_connections = 200
fsync = off
shared_buffers = 1GB
work_mem = 10MB
effective_cache_size = 2GB
maintenance_work_mem = 512MB
```

# \x 切换一行行显示

# 创建数据库

```
postgres=# CREATE DATABASE exampledb OWNER dbuser;
postgres=# GRANT ALL PRIVILEGES ON DATABASE exampledb to dbuser;
postgres=# \c exampledb;
postgres=# ALTER SCHEMA public OWNER to dbuser;
postgres=# GRANT ALL PRIVILEGES ON ALL SEQUENCES IN SCHEMA public TO dbuser;
postgres=# GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO dbuser;
```

ALTER TABLE kline_a RENAME TO kline_b;

# 救急操作

## 查看连接

```sql
show max_connections;
SELECT COUNT(*)
from pg_stat_activity;
select min_val, max_val
from pg_settings
where name = 'max_connections';
```

## 关闭连接

```sql
SELECT pg_terminate_backend(pg_stat_activity.procpid)
FROM pg_stat_get_activity(NULL::integer)
WHERE datid = (SELECT oid from pg_database where datname = 'your_database');
```

```postgresql
show max_connections;
SELECT *
from pg_stat_activity;
select pg_cancel_backend(93); -- kill select
select pg_terminate_backend(93); -- kill DML
```

# 切换db \c gis

# 备份

https://docs.timescale.com/v0.12/using-timescaledb/backup

```sql
-- save
pg_dump -U postgres -s --table kline_1d -N _timescaledb_internal | grep -v _timescaledb_internal > kline_1d.sql
psql -U postgres -c "\COPY (SELECT * FROM kline_1d) TO kline_1d.csv DELIMITER ',' CSV"

-- import
psql -U postgres -c "\COPY kline_1d FROM kline_1d.csv CSV"
```

# explain

explain analyze select * from a;

- [./pg-bitdata.sql](./pg-bitdata.sql)
- [./pg-select.sql](./pg-select.sql)
