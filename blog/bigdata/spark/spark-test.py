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
