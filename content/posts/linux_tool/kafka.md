---
title: kafka 安装配置
date: 2018-08-20
categories: [linux]
---

## kafka

- [x] Kafka快速入门 https://colobu.com/2014/08/06/kafka-quickstart/
- [x] Go连接Kafka https://blog.csdn.net/dazheng/article/details/52995260


## quick demo
```shell
# session 1
kafka-console-producer --broker-list   localhost:32773 --topic chat
# session 2 sync from 1
kafka-console-consumer --broker-server localhost:32773 --topic chat --form-beginning
```

## deploy
```shell
docker run -d --name zookeeper -p 2181:2181 zookeeper
docker run -d --name kafka -p 9092:9092 \
	--link zookeeper \
	--env KAFKA_ZOOKEEPER_CONNECT=192.168.31.229:2181 \
	--env KAFKA_ADVERTISED_HOST_NAME=192.168.31.229 \
	--env KAFKA_ADVERTISED_PORT=9092 \
	wurstmeister/kafka
````


## old
```sh
#第二步: 启动服务
bin/zookeeper-server-start.sh config/zookeeper.properties
bin/kafka-server-start.sh config/server.properties

#第三步: 新建一个话题Topic
bin/kafka-topics.sh --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic test
bin/kafka-topics.sh --list --zookeeper localhost:2181

#第四步: 发送消息
bin/kafka-console-producer.sh --broker-list localhost:9092 --topic test

#第五步: 消费消息
bin/kafka-console-consumer.sh --zookeeper localhost:2181 --topic test --from-beginning

#info
bin/kafka-topics.sh --describe --zookeeper localhost:2181
bin/kafka-topics.sh --describe --zookeeper localhost:2181 --topic test
```
