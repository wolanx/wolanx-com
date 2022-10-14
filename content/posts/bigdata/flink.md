---
title: flink
date: 2021-05-06T20:10:57+08:00
categories: [bigdata]
---

https://ci.apache.org/projects/flink/flink-docs-stable/zh/

tar -xzf flink-1.13.0-bin-scala_2.11.tgz
cd flink-1.13.0


https://ci.apache.org/projects/flink/flink-docs-stable/zh/

./bin/flink run -m flink.cc5ee3108d340437b956b5d18bf1a9ba7.cn-shanghai.alicontainer.com -py asdf.py
./bin/flink run -m flink.cc5ee3108d340437b956b5d18bf1a9ba7.cn-shanghai.alicontainer.com:80 examples/streaming/WordCount.jar


./bin/flink run -pyfs ./examples/python/table/batch -pym word_count

