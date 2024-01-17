---
title: c demo
date: 2015-02-13T20:43:41+08:00
tags: [clang]
---

## doc

- 深入浅出让你理解什么是LLVM https://www.jianshu.com/p/1367dad95445

## install

```shell
# https://releases.llvm.org/download.html

# windows
winget.exe install LLVM.LLVM
# LIBCLANG_PATH=D:\programs\LLVM\bin

# Debian-based Linuxes
apt install llvm-dev libclang-dev clang

# mac
brew install llvm
port install clang
```

### 命令

```shell
### -E 预编译
`gcc -E -o a.e a.c` 把`/usr/include/stdio.h`的内容`include`过来,并`删除注释`
### -S 汇编
`gcc -S -o a.s a.c` `c`转化成`汇编`
### -c 编译
`gcc -c -o a.o a.s` `汇编`转化成`二进制机器指令`
### 链接 没参数
`gcc -o a a.o`

## 快速生成
rm -f a.out;
cc a.c;
./a.out;

`gcc a.c` = `gcc -o a a.c`
```
