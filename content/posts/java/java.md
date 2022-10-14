---
title: java 基础
date: 2018-12-24T20:10:57+08:00
categories: [java]
---

## docker image

```shell
# https://github.com/graalvm/container/pkgs/container/graalvm-ce
# ghcr.io/graalvm/$IMAGE_NAME[:][$os_version][-$java_version][-$version][-$build_number]
docker pull ghcr.io/graalvm/jdk:ol8-java17-22

docker tag ghcr.io/graalvm/jdk:ol8-java17-22 wolanx/java:jdk17-graalvm22
docker push wolanx/java:jdk17-graalvm22

docker tag ghcr.io/graalvm/jdk:ol8-java17-22 wolanx/java:latest
docker push wolanx/java:latest
```

## doc

- [ ] 多线程编程完全指南-系列 https://zhuanlan.zhihu.com/p/70325764

### 面试题

- [x] 2018年BATJ面试题精选 https://www.itcodemonkey.com/article/13260.html
- [x] 死磕面试：2019最全Java面试题 https://blog.csdn.net/crazymakercircle/article/details/82555359
- [x] Java 最常见 200+ 面试题全解析：面试必备 https://gitchat.csdn.net/activity/5c6cf6044bb44360f3370255
- [x] 2018年最新Java面试题及答案整理 https://blog.csdn.net/qq_41701956/article/details/80250226
- [x] 2019年最新Java面试题及答案整理（上） https://blog.csdn.net/qq_41701956/article/details/86686492
- [x] 2019年最新Java面试题及答案整理（下） https://blog.csdn.net/qq_41701956/article/details/86699263
- [x] 这30个我精选的含答案的面试题 https://mp.weixin.qq.com/s/1SMQTkR88lyzazEQOdW34g

### 优化 jvm

- [ ] 这 17 个 JVM 参数，高级 Java 必须掌握！https://mp.weixin.qq.com/s/HYT49JD38f6iIpyVFWmH-Q

### spring

- [x] 快速开发一个自定义 Spring Boot
  Starter https://mp.weixin.qq.com/s?__biz=MzUxOTc4NjEyMw==&mid=2247484379&idx=1&sn=351a7f669a1b1314520d8f5455fb7ade
- [x] 深入理解 Spring 中的各种注解，总有一个你不懂的？ https://mp.weixin.qq.com/s/7Qo-zbUb-_l3WwmFNYBB2g
- [x] 看完这个不会配置 logback ，请你吃瓜！https://juejin.im/post/5b51f85c5188251af91a7525

### db

- [x] SpringBoot 中 JPA 的使用 https://www.jianshu.com/p/c14640b63653
- [x] 手写一个Jedis以及JedisPool https://mp.weixin.qq.com/s/4RjyyYVU95I7R7v9MKutEA
- [ ] 深入理解 Spring 之 SpringBoot 事务原理 https://blog.csdn.net/qq_38182963/article/details/78891044

## jmap 分析

```shell
字段详细解释 https://www.cnblogs.com/kongzhongqijing/articles/3621163.html
jmap -heap 1
jmap -dump:file=jmap.dump 1
jmap -dump:format=b,file=jmap.hprof 1
tar -zcvf a.tar.gz jmap.hprof
k cp dep-monitor-center-577f76bb89-xjfwg:/a.tar.gz a.tar.gz
https://www.eclipse.org/mat/
```

## java基础

### 常用命令

```sh
# .java => .class
javac HelloWorld.java

# 运行 .class
java HelloWorld
java -classpath /www/demo HelloWorld

# .class => .jar
jar -cvf hello.jar Hello.class
# 运行 jar
java -jar 1.jar

# .jar => .exe
javaFX

# .jar => folder
jar xvf etp-cs-i18n.jar
```

### decode

```shell
.class => .java
java -jar ~/Desktop/app/fernflower/build/libs/fernflower.jar classes src/main/java-temp
```
