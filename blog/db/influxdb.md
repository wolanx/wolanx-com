---
title: influxdb
date: 2018-03-22
tags:
  - db
---

# influxdb

- py demo https://ts-uf68z3on142991o8b-grafana.influxdata.rds.aliyuncs.com:3000/?grundfos(Ab123456)
- sql doc https://docs.influxdata.com/influxdb/v1.8/query_language/explore-data/

docker run --restart=unless-stopped --name influxdb-1 -d -p 8086:8086 -v $PWD:/var/lib/influxdb influxdb

docker run --restart=unless-stopped --name influxdb-1 -d \
-p 8086:8086 \
-p 8083:8083 -e INFLUXDB_ADMIN_ENABLED=true \
-v $PWD:/var/lib/influxdb influxdb

```
svc-influxdb:
	image: influxdb:1.7.11
	ports:
		- 8086:8086
	environment:
		- TZ=utc-8
		- INFLUXDB_ADMIN_USER=root
		- INFLUXDB_ADMIN_PASSWORD=root
		- INFLUXDB_DB=iothub
		- INFLUXDB_HTTP_ENABLED=true
		- INFLUXDB_HTTP_AUTH_ENABLED=true
```

# 常用命令

```sh
influx
influx -ssl -host ts-uf68z3on142991o8b.influxdata.tsdb.aliyuncs.com -port 8086 -username grundfos -password Ab123456 -database gimc-perf
influx -ssl -host ts-uf68z3on142991o8b.influxdata.tsdb.aliyuncs.com -port 8086 -username grundfos -password Ab123456 -database gimc-perf -precision rfc3339

auth
show users
show databases
show MEASUREMENTS

# 设置time格式
precision rfc3339

# sql https://archive.docs.influxdata.com/influxdb/v1.2/query_language/data_exploration/#the-basic-select-statement
SELECT * FROM "temperature"
SELECT * FROM /.*/ LIMIT 1
SELECT * FROM sensor where "deviceId"='sensor1'
# tz https://en.wikipedia.org/wiki/List_of_tz_database_time_zones#List
select * from sensor_0s tz('Asia/Shanghai')
select * from sensor_0s tz('Etc/GMT-8')
```
