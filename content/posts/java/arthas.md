---
title: Arthas
date: 2022-01-27T20:10:57+08:00
---

## Intro

Java 诊断工具 Arthas 入门教程 https://start.aliyun.com/course?id=qDlgqpBT
进阶 命令 https://arthas.aliyun.com/doc/advanced-use.html

## Install

wget https://arthas.aliyun.com/arthas-boot.jar
> use java > 8 when jre tool.java

## Start

```sh
java -jar arthas-boot.jar

# input pid

help

dashboard

thread 1
thread 1 | grep 'main('

sc -d *MathGame # 查找JVM里已加载的类

jad demo.MathGame # 反编译代码

watch demo.MathGame primeFactors returnObj # 查看函数的参数/返回值/异常信息

```

