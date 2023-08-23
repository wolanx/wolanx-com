---
title: spark pyspark
date: 2023-08-22T10:26:00+08:00
tags: [ bigdata ]
---

- hdfs https://help.aliyun.com/zh/oss/use-cases/use-jindosdk-with-spark-to-query-data-stored-in-oss-hdfs

## demo1

```shell
docker run -it apache/spark:python3 /opt/spark/bin/pyspark

# >>> spark.range(1000 * 1000 * 1000).count()
```

## job

```shell
docker run --restart=unless-stopped -it -d --name spark -p 4040:4040 -v $(pwd):/app -e TZ=utc-8 apache/spark:python3 tail -f
docker run --restart=unless-stopped -it -d --name spark -p 4040:4040 -v $(pwd):/app -e TZ=utc-8 wolanx/spark /opt/spark/bin/spark-submit /app/test.py

# add jars
cd /opt/spark/jars
wget https://repo1.maven.org/maven2/mysql/mysql-connector-java/8.0.25/mysql-connector-java-8.0.25.jar
pip install requests
# spark-submit --jars /opt/spark/jars/mysql-connector-java-8.0.25.jar /app/test.py

docker exec -it --user=root spark bash
docker exec -it spark /opt/spark/bin/spark-submit /app/test.py
```

### test.py

```python
import ast
import time
from datetime import datetime

import requests
from pyspark.sql import SparkSession, SQLContext
from pyspark.sql.functions import col

spark = SparkSession.builder.getOrCreate()

df = (
    spark.read.format("jdbc")
    .option("url", "jdbc:mysql://xxx:3306/xxx")
    .option("dbtable", "xxx")
    .option("user", "xxx")
    .option("password", "xxx")
    .load()
)
print(df.columns)


def write_to_influxdb(data):
    # print(data)
    # return
    url = "https://ts-xxx.influxdata.tsdb.aliyuncs.com:8086/write?db=xxx&u=xxx&p=xxx&precision=s"
    headers = {'Content-Type': 'text/plain'}
    r = requests.post(url, data=data, headers=headers)
    print(r.text)


def process_row(row):
    rowMap: dict = ast.literal_eval(row['data'].replace('nan', 'None').replace(' _', '\\ _'))
    fields = ','.join([f"{k}={v}" for k, v in rowMap.items() if v is not None])
    write_to_influxdb(f"sensor_0s,SNO=#device({row['device_id']}).perf {fields}")


def doRun():
    while True:
        current_second = int(time.time()) % 60

        if current_second == 0:
            rDt = datetime.now().replace(second=0)
            df2 = df.where((df.d == rDt.day) & (df.his == rDt.strftime("%H:%M:%S"))).orderBy(
                col("id").desc())  # .limit(5)
            # print(df2.show())

            df2.foreach(process_row)

        time.sleep(1)


doRun()
```

## cluster

```shell
spark-shell --master local
```

