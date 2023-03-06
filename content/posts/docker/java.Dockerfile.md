---
title: java Dockerfile
date: 2023-03-06T20:06:00+08:00
categories: [java]
---

## 2023-03-06 grundfos java17-graalvm22

```Dockerfile
FROM debian:11-slim
LABEL maintainer="wolanx<82540776@qq.com>"

RUN sed -i 's/deb.debian.org/mirrors.aliyun.com/g' /etc/apt/sources.list \
    && sed -i 's/security.debian.org/mirrors.aliyun.com/g' /etc/apt/sources.list

# https://github.com/graalvm/graalvm-ce-builds/releases
# https://github.com/graalvm/container/raw/master/community/gu-wrapper.sh /usr/local/bin/gu
# https://github.com/graalvm/graalvm-ce-builds/releases/download/vm-22.3.1/graalvm-ce-java17-linux-amd64-22.3.1.tar.gz graalvm-ce-java17-linux-amd64-22.3.1.tar.gz
ADD graalvm-ce-java17-linux-amd64-22.3.1.tar.gz /opt/
ADD gu-wrapper.sh /opt/
RUN mv /opt/gu-wrapper.sh /usr/local/bin/gu && chmod +x /usr/local/bin/gu

ENV LANG=en_US.UTF-8
ENV JAVA_HOME=/opt/graalvm-ce-java17-22.3.1
ENV PATH="$PATH:$JAVA_HOME/bin"

RUN apt-get update -y && \
    apt-get install -y procps net-tools iputils-ping htop gcc curl wget ca-certificates \
    fontconfig

ADD https://gfdcc-production-profile.oss-cn-shanghai.aliyuncs.com/profile/fonts/SourceHanSansCN-Normal.ttf /usr/share/fonts/truetype/wolanx/
ADD https://gfdcc-production-profile.oss-cn-shanghai.aliyuncs.com/profile/fonts/SourceHanSansCN-Bold.ttf /usr/share/fonts/truetype/wolanx/

CMD java -version

# docker build -t wolanx/java .
```

## 2021-03-13 google jib plugin

```gradle
plugins {
    id 'com.google.cloud.tools.jib' version '3.3.0'
    id 'java'
}
jib {
    from {
        image = 'openjdk:17-slim'
    }
    to {
        image = 'xxxx'
        // tags = [version.toString()]
    }
    container {
        mainClass = 'com.wolanx.proxy.edierp.EdiApplication'
        ports = ['22100']
        format = 'OCI'
        creationTime = 'USE_CURRENT_TIMESTAMP'
    }
}
```
