---
title: wsl 工具 Linux 的 Windows 子系统
date: 2019-05-08 09:59:30
tags: [linux]
---

## wsl

- Linux 的 Windows 子系统 https://docs.microsoft.com/zh-cn/windows/wsl/about

## cmd
```shell
wsl -l -v

wsl --shutdown
```

## vim ~/.bashrc
```shell
alias d='cd /mnt/d'
alias e='cd /mnt/e'
alias z='cd /mnt/z'
```

## fix
netsh winsock reset
