---
title: go doc
date: 2018-03-20 16:34:12
tags:
  - go
---

# go

# build

```sh
CGO_ENABLED=0 GOOS=linux go build -v -installsuffix cgo -o wolan-ingress

## 生成 dll
# 生成 .so .h
go build -o libddd.so -buildmode=c-shared main.go
# go build -ldflags "-s -w" -o libdemo.dll -buildmode=c-shared main.go
# ldflags "-s -w" -s -w 选项用于减小生成动态链接库的体积，-s 是压缩，-w 是去掉调试信息
# c 连接 lib
gcc test.c -L ./ -lddd -o test
# 默认使用 /usr/lib，临时env
LD_LIBRARY_PATH=$LD_LIBRARY_PATH:. ./test

# 生成静态库
c-archive
```

# blog

- [x] [译]Go文件操作大全 http://colobu.com/2016/10/12/go-file-operations
- [x] [转]Golang资料集 https://gocn.io/article/65
- [x] Go 的构建模式 https://blog.lab99.org/post/golang-2017-10-01-video-go-build-mode.html
- [x] 视频笔记：gRPC
  从学习到生产 https://blog.lab99.org/post/golang-2017-09-27-video-grpc-from-tutorial-to-production.html

- [x] tonybai http://tonybai.com

- Go程序设计语言(二) http://tonybai.com/2012/08/27/the-go-programming-language-tutorial-part2/
- Go程序设计语言(三) http://tonybai.com/2012/08/28/the-go-programming-language-tutorial-part3/

# awesome

- 中文 https://github.com/hackstoic/golang-open-source-projects
- Go by Example 中文版 https://gobyexample-cn.github.io/

# env

```shell
-GOPATH z:\www	下面会自动src bin
go env -w GOPROXY=https://goproxy.cn/,direct
GOPATH=~/Desktop/www
GOPATH=~/Desktop/www GOPROXY=https://goproxy.cn,direct go get -v golang.org/x/tools/cmd/goimports
```
