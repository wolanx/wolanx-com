---
title: go 性能跟踪
date: 2018-03-20 16:34:12
tags:
  - go
---

# pprof

- [x] 视频笔记：7种 Go 程序性能分析方法 - Dave
  Cheney https://blog.lab99.org/post/golang-2017-10-20-video-seven-ways-to-profile-go-apps.html
- [x] [译] Go 可视化性能分析工具 https://colobu.com/2017/03/02/a-short-survey-of-golang-pprof/

# pprof

```shell
brew install gperftools
brew install graphviz

import _ "net/http/pprof"

http://localhost:1777/debug/pprof/
http://localhost:1777/debug/pprof/profile

go tool pprof http://localhost:1777/debug/pprof/profile
```

# go-torch

```shell
go get github.com/uber/go-torch
cd $GOPATH/src/github.com/uber/go-torch
git clone https://github.com/brendangregg/FlameGraph.git

go-torch --file "profile" --url http://localhost:2345
go-torch -u http://localhost:1777/
```
