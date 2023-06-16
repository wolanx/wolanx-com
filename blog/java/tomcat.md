---
title: tomcat
date: 2019-03-18T20:10:57+08:00
tags: [java]
---

# tomcat

安装 https://blog.csdn.net/sun8112133/article/details/79944531

```markdown
使用 apt-get 命令 安装后的 tomcat 7的目录结构说明
/etc/tomcat8 ：全局配置
/usr/share/tomcat8/ ：程序主目录
/usr/share/tomcat8/conf/Catalina/localhost/ ：本机部署的 Catalina 配置
/var/lib/tomcat8/ ：工作主目录
/var/lib/tomcat8/webapps ：应用文件实际存放于此
/var/lib/tomcat8/work ：动态工作目录（动态编译的 .jsp 存放于此）
```

## docker

```sh
# 把war放当前目录,会自动解压缩
docker run -it --rm -p 8888:8080 -v $PWD:/usr/local/tomcat/webapps tomcat:8.5.39-jre8-alpine
```

## tar.gz install https://www.jb51.net/article/143185.htm

```sh
wget http://mirrors.tuna.tsinghua.edu.cn/apache/tomcat/tomcat-9/v9.0.17/bin/apache-tomcat-9.0.17.tar.gz
tar -zxvf apache-tomcat-9.0.17.tar.gz
```

# jetty

```shell
wget https://repo1.maven.org/maven2/org/eclipse/jetty/jetty-distribution/9.4.16.v20190411/jetty-distribution-9.4.16.v20190411.tar.gz
tar -zxvf jetty-distribution-9.4.16.v20190411.tar.gz
```
