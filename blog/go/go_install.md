---
title: go install
date: 2018-03-20 16:34:12
tags:
  - go
---

## install liunx

```sh
wget https://storage.googleapis.com/golang/go1.17.5.linux-amd64.tar.gz
tar -xvf go1.8.1.linux-amd64.tar.gz -C /usr/local/
sudo vi /etc/profile
export GOROOT=/usr/local/go
export GOPATH=/go # bin pkg src
export PATH=$PATH:$GOROOT/bin:$GOPATH/bin

go env -w GOPROXY=https://goproxy.cn/,direct

```

git clone https://github.com/golang/text.git $GOPATH/src/golang.org/x/text

## 下载

https://golang.org/dl/
