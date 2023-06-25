---
title: jmeter 压测工具
date: 2017-06-10
tags:
  - 工具
---

# jmeter

```text
need java8

cd bin
./jmeter

./jmeter -n -t cdemo.jmx -l cdemo.jtl

Sampler	->	HTTP请求
监听器	->	察看结果树
断言		->	响应断言
监听器	->	Aggregate Graph
监听器	->	生成概要结果
监听器	->	聚合报告
```
