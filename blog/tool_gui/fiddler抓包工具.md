---
title: 抓包工具
date: 2019-01-12
categories:
- 工具
---

- mitmproxy
- charles
- fiddler
- zan-proxy https://youzan.github.io/zan-proxy/book/
- http toolkit


# 抓包 mitmproxy

## doc

https://zhuanlan.zhihu.com/p/23931921

- ? 进入 帮助
- 按z清空请求列表
- 按用j，k或者上下方向键在列表上浏览
- 按回车进入详情界面
- 按q，返回列表界面
- 按tab键或者h，l，在Request，Response，Detail三个tab之间切换。按j，k或者上下方向键可以滚动查看详情
- 按G跳到最新一个请求
- 按g跳到第一个请求
- 按d删除当前选中的请求，按D恢复刚才删除的请求

## install

brew install mitmproxy

## https

safari http://mitm.it
iPhone => 关于本机 => 证书信任设置

## view_filter
https://docs.mitmproxy.org/stable/concepts-filters/

~d regex	Domain
~d regex	baidu
~d xdq ~b bank_name

