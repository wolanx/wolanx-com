---
title: cgo
date: 2018-03-20 16:34:12
tags:
  - go
  - c
---

- [x] golang生成.a文件被C调用遇到的坑 https://www.jianshu.com/p/dafc3ac76d9c

# 生成.a .h

go build -buildmode=c-archive -o liba.a liba.go

# build

```shell
gcc liba.c liba.a -o liba
./liba
```

[./liba.c](./liba.c)
[./liba.go](./liba.go)
