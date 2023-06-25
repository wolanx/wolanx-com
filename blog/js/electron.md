---
title: electron
date: 2018-03-22 16:38:57
tags:
  - js
---

# doc

- [x] 用 Electron 打造跨平台前端
  App [https://segmentfault.com/a/1190000005744529](https://segmentfault.com/a/1190000005744529)

## install

```sh
npm install -g cnpm --registry=https://registry.npm.taobao.org
alias cnpm="npm --registry=https://registry.npm.taobao.org \
--cache=$HOME/.npm/.cache/cnpm \
--disturl=https://npm.taobao.org/dist \
--userconfig=$HOME/.cnpmrc"

cnpm install -g electron-packager

electron-packager . echo-test --platform=win32 --arch=x64 --icon=./app/assets/images/tx.jpg --overwrite --out ./dist --version=1.1.0
```