---
title: jenkins 部署
date: 2019-05-21
tags: [linux]
---

## jenkins
Docker持续部署图文详解 http://www.csdn.net/article/2015-07-21/2825266
使用Docker构建持续集成与自动部署的Docker集 https://my.oschina.net/jayqqaa12/blog/633683

## install
```sh
mkdir jk && cd jk
# 注意是当前user
docker run --restart=unless-stopped --name jenkins -it -d \
 --privileged=true \
 -u root \
 -p 8080:8080 -p 50000:50000 \
 -v "$PWD":/var/jenkins_home jenkins:2.60.3
```

## proxy
jenkins->系统管理->管理插件->高级
把：http://updates.jenkins-ci.org/update-center.json
换成：http://mirror.esuni.jp/jenkins/updates/update-center.json

## 时区问题
【系统管理】->【脚本命令行】运行下面的命令
System.setProperty('org.apache.commons.jelly.tags.fmt.timeZone', 'Asia/Shanghai')
