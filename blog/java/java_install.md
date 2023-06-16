---
title: java 安装配置
date: 2018-12-24T20:10:57+08:00
tags: [java]
---

# java

```sh
yum list installed | grep java
yum install -y java # jre
yum install -y java-1.8.0-openjdk # jre
yum install -y java-1.8.0-openjdk-devel # javac

apt install default-jdk

# 看那个java
which java
ls -lrt /usr/bin/java
ls -lrt /etc/alternatives/java

# vi /etc/profile
export JAVA_HOME=/usr/lib/jvm/java-1.8.0-openjdk-1.8.0.212.b04-0.el7_6.x86_64
export JRE_HOME=$JAVA_HOME/jre
export CLASSPATH=$JAVA_HOME/lib:$JRE_HOME/lib:$CLASSPATH
export PATH=$JAVA_HOME/bin:$JRE_HOME/bin:$PATH

# ln
ln -sf /usr/lib/jvm/java-1.8.0-openjdk-1.8.0.242.b08-0.el7_7.x86_64/bin/java /etc/alternatives/java
```
