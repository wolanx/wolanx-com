import ast
from datetime import datetime

import requests
from pyspark.sql import SparkSession
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
    dt = datetime.strptime(f"2023-08-{row['d']} {str(row['his'])[11:]}", "%Y-%m-%d %H:%M:%S")
    print(dt)
    write_to_influxdb(f"sensor_0s,SNO=#device({row['device_id']}).perf {fields} {int(dt.timestamp())}")


def doRun():
    df2 = df.where((df.d == 23) & (df.his >= "00:00:00") & (df.his <= "15:00:00")).orderBy(col("id").desc())

    df2.foreach(process_row)


doRun()
