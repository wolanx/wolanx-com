---
title: hugo-book
date: 2022-01-20T22:17:51+08:00
tags: [tool]
---

## Intro

本站使用 博客系统hugo，搭配主题hugo-book

- hugo
    - https://gohugo.io/getting-started/quick-start/
- hugo-book
    - 官方demo https://hugo-book-demo.netlify.app/posts/migrate-from-jekyll/
    - 代码demo https://github1s.com/alex-shpak/hugo-book

## Start

```sh
# 本地测试
hugo server -w

# add
hugo new posts/xxx.md
```

## Guide

```md
Intro
Install
Start

Packages
Contributing

About
License
```

## Test

{{< tabs "uniqueid" >}}
{{< tab "MacOS" >}} # MacOS Content {{< /tab >}}
{{< tab "Linux" >}} # Linux Content {{< /tab >}}
{{< tab "Windows" >}} # Windows Content {{< /tab >}}
{{< /tabs >}}

## 百度统计

自定义 layouts/partials/docs/inject/footer.html

