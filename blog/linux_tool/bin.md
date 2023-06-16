---
title: 二进制文件bin
date: 2021-05-27
tags: [linux]
---

## ldd 看 dynamic link
ldd hehe

## objdump

```sh
#显示所可用的头信息，包括符号表、重定位入口。-x 等价于-a -f -h -r -t 同时指定。
objdump -x ota
#显示文件的符号表入口
objdump -t ota
```

## hexdump

```sh
hexdump -C config.json  # 16进制查看
xdd config.json # 二进制查看
```

## .so func list

```sh
nm -D libSP.so
objdump -T libSP.so  # --dynamic-syms 显示文件的动态符号表入口，仅仅对动态目标文件意义
```

## strip 压缩 脱衣服

```sh
#iot-echo: ELF 64-bit LSB executable, x86-64, version 1 (SYSV), dynamically linked (uses shared libs), not stripped
#iot-echo: ELF 64-bit LSB executable, x86-64, version 1 (SYSV), dynamically linked (uses shared libs), stripped
#iot-echo: ELF 64-bit LSB executable, x86-64, version 1 (SYSV), statically linked, stripped
# nm iothub-echo # strip后就没有了
strip iothub-echo
```
