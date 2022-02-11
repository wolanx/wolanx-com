---
title: python Dockerfile
date: 2022-02-11T22:17:51+08:00
categories:
  - docker
tags:
---

```Dockerfile
FROM python:3.10.0-slim

RUN sed -i 's/deb.debian.org/mirrors.aliyun.com/g' /etc/apt/sources.list \
    && sed -i 's/security.debian.org/mirrors.aliyun.com/g' /etc/apt/sources.list

RUN mkdir ~/.pip \
    && echo '[global]\n \
trusted-host=mirrors.aliyun.com\n \
index-url=https://mirrors.aliyun.com/pypi/simple\n \
' > ~/.pip/pip.conf

RUN apt-get update -y \
    && apt-get install -y gcc curl \
    && apt-get install -y --no-install-recommends vim tree \
    && rm -rf /var/lib/apt/lists/*


RUN curl -s -L -o ~/rocketmq-client-cpp-2.0.0.amd64.deb \
    'https://github.com.cnpmjs.org/apache/rocketmq-client-cpp/releases/download/2.0.0/rocketmq-client-cpp-2.0.0.amd64.deb' \
    && dpkg -i ~/rocketmq-client-cpp-2.0.0.amd64.deb \
    && rm -f ~/rocketmq-client-cpp-2.0.0.amd64.deb

ADD https://gfdcc-production-profile.oss-cn-shanghai.aliyuncs.com/profile/fonts/SourceHanSansCN-Normal.ttf /root/.fonts/
ADD https://gfdcc-production-profile.oss-cn-shanghai.aliyuncs.com/profile/fonts/SourceHanSansCN-Bold.ttf /root/.fonts/

RUN pip install --no-cache-dir --default-timeout=600 gunicorn==20.1.0 numpy==1.21.4 CPython

WORKDIR /www/backend-gim

COPY src/backend/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# todo
#RUN apt-get -y --purge remove vim vim-runtime vim-common xxd cpp-8
#RUN apt-get autoremove -y

CMD ["gunicorn", "run:app", "-c", "./gunicorn.conf.py"]

# docker build -f __cicd__/gimc.rt.Dockerfile -t registry.cn-shanghai.aliyuncs.com/digital-web/gimc-rt:20211203-1148 .
```
