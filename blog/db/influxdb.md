---
title: influxdb
date: 2018-03-22
tags:
  - db
---

# influxdb

- tool download https://github.com/influxdata/influxdb/releases/tag/v1.8.10
- py demo https://ts-uf68z3on142991o8b-grafana.influxdata.rds.aliyuncs.com:3000/?grundfos(Ab123456)
- sql doc https://docs.influxdata.com/influxdb/v1.8/query_language/explore-data/
- sql doc https://docs.influxdata.com/influxdb/v1.8/query_language/functions/

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
		- TZ=Etc/GMT-8
		- INFLUXDB_ADMIN_USER=root
		- INFLUXDB_ADMIN_PASSWORD=root
		- INFLUXDB_DB=iothub
		- INFLUXDB_HTTP_ENABLED=true
		- INFLUXDB_HTTP_AUTH_ENABLED=true
```

# 常用命令

```shell
influx
influx -ssl -host ts-uf68z3on142991o8b.influxdata.tsdb.aliyuncs.com -port 8086 -username grundfos -password Ab123456 -database gimc-perf
influx -ssl -host ts-uf68z3on142991o8b.influxdata.tsdb.aliyuncs.com -port 8086 -username grundfos -password Ab123456 -database gimc-perf -precision rfc3339

auth
show users
show databases
# show tables
show MEASUREMENTS
SHOW MEASUREMENTS ON "gimc-perf"

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

## select

```shell
# 查 所有 tag
show tag keys from sensor_0s;
# 查 tag 下的 name
show tag values from sensor_0s with key="SNO";
# 查时间线
SHOW SERIES ON "gimc-perf" from sensor_0s


# =~/给定字段/ 包含指定字段的
select * from test where monitor_name=~/^app/;

# fill fill(100) fill(previous) fill(linear)
SELECT MAX("water_level") FROM "h2o_feet" WHERE location = 'coyote_creek' GROUP BY time(12m) fill(previous);

# export
influxd backup -database gimc-perf -host ts-uf668p5xos953ygfo.influxdata.tsdb.aliyuncs.com:8088 -username grundfos -password Ab123456 -start 2023-08-15T20:00:00Z -end 2023-08-15T20:10:00Z ts
```

## copy into

```shell
select SNO,c,d,e from sensor_0s where SNO = 'iot-echo-changqing-heatex_1bu' and time > now() - 5m;
select SNO,c,d,e into sensor_test from sensor_0s where SNO = 'iot-echo-changqing-heatex_1bu' and time > now() - 5m;

select SNO,c,d,e from sensor_test where SNO = 'iot-echo-changqing-heatex_1bu' and time > now() - 1h;

select SNO='hahahah',c,d,e into sensor_test from sensor_0s where SNO = 'iot-echo-changqing-heatex_1bu' and time > now() - 5m;
select SNO,c,d,e from sensor_test where SNO = 'iot-echo-changqing-heatex_1bu' and time > now() - 1h;
```

## ddl

```shell
# delete table
drop measurement sensor_test

show measurements
```

## import csv

```shell
cat /z/data/${tt}.csv | awk -F',' '{printf "sensor_0s,SNO=%s %s=%s %s\n", $3, $1, $4, $2}' >> /z/data/${tt}.sql
# cat /z/data/${tt}.txt | awk -F',' '{printf "sensor_0s,SNO=%s value=%s %s\n", $3, $1, $4, $2}' > /z/data/${tt}.sql
# cat /z/data/${tt}.txt | awk -F',' '{gsub(/value/, $1); printf "sensor_0s,%s\n", $2'} >> /z/data/${tt}.sql
influx -ssl -host ts-uf68z3on142991o8b.influxdata.tsdb.aliyuncs.com -port 8086 -username grundfos -password Ab123456 -import -precision=s -path=datarrr.txt
```
