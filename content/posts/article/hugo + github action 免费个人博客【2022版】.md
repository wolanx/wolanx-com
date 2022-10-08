---
title: hugo + github action 免费个人博客【2022版】
date: 2022-02-11T17:44:26+08:00
categories:
  - csdn
tags:
---

> https://blog.csdn.net/wolanx/article/details/122857729

## Intro
免费个人博客 的教程非常的 `多`，但大多面向 `纯小白`，反而对有一定基础的同学显得 `落后 + 啰嗦`，本文整合目前已知最好的方式，最快捷优雅的搞定一个博客，并给出 `常见错误`。

## 知识点
- [ ] hugo 的安装及使用不是本文重点，其实同理 hexo
- [ ] git github 默认已掌握
- [x] github page 生成可访问的页面的 `灵魂` 所在
- [x] github action `自动生成`上一步

## 完整链路解析

- git commit 提交
- 触发 github action `.github/workflows/my-pipeline.yml` 并满足设置中的 `on` 条件
- 触发 pipeline 中的 steps
  - checkout：相当与 git clone，并且后续操作具有 github 完整权限，可以通过 permissions 设置
  - setup hugo：准备构建要求，安装对应版本，注意是否需要 extended
  - build：构建出静态文件，并输出到 public 文件夹
  - deploy：该插件来自 [插件市场](https://github.com/marketplace?type=actions&query=hugo+)
    - 自动创建分支 gh-pages
    - 自动 copy public 到新分支
    - 自动提交
    - 自动生成 CNAME 文件，根据 cname 设置，想要 `自定义域名` 的注意这里了
- 打开 `https://github.com/{你的名字}/{你的仓库}/settings/pages`（后续步骤只需要一次）
  - `Source` 选择 gh-pages ，文件夹: 默认 / (root) ，并 save
  - 注意上方提示 `Your site is ready to be published at` https://xxx.github.io/xxx/
  - 将域名部分做 `解析`
  - `Custom domain` 设置 自己的域名
  - `Enforce HTTPS` 点一下，然后等一会

## 步骤1：hugo github
### 步骤1.1: 创建 仓库 & 初始化 hugo
> hugo github 的基本操作不是本文重点，忽略

### 步骤1.2: 创建 .gitmodules 文件
hugo 的 主题 themes 是通过 git 的 sub modules 实现，而 github 上 git 会自动根据 `.gitmodules` clone 子项目。没有 .gitmodules 文件会导致构建失败。
比如我的主题使用的是 hugo-book（推荐），那么配置如下

```text
[submodule "themes/hugo-book"]
	path = themes/hugo-book
	url = https://github.com/alex-shpak/hugo-book
```

## 步骤2：github action 自动生成

官方默认的 Jekyll 其实是会根据分支 `自动` 构建发布的，但如果自己魔改使用 `hugo | hexo` 这类软件以后就不会自动，需要使用 action 功能，而 action 其实就是 github 的 pipeline版本，使用只需要一个文件 `.github/workflows/my-pipeline.yml`。其中可能需要改的：
- main 分支 根据实际情况改一下
- cname 最后一行 如果要使用自定义域名功能

### 步骤2.1: 创建 .github/workflows/my-pipeline.yml
```yaml
name: my-pipeline

on:
  push:
    tags:
      - '*'
    branches:
      - main

env:
  REGISTRY: ghcr.io
  IMAGE_NAME: ${{ github.repository }}

jobs:
  build:
    runs-on: ubuntu-latest
    # permissions:
    #   contents: read
    #   packages: write
    concurrency:
      group: ${{ github.workflow }}-${{ github.ref }}

    steps:
      - name: checkout
        uses: actions/checkout@v2
        with:
          submodules: true  # Fetch Hugo themes (true OR recursive)
          fetch-depth: 0    # Fetch all history for .GitInfo and .Lastmod

      - name: setup hugo
        uses: peaceiris/actions-hugo@v2
        with:
          hugo-version: '0.92.0'
          extended: true

      - name: build
        run: hugo --minify

      - name: deploy
        uses: peaceiris/actions-gh-pages@v3
        if: ${{ github.ref == 'refs/heads/main' }}
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          publish_dir: ./public
          # cname: wolanx.com # 重点 ！！！
```

## 步骤3：github page 页面生成

打开 `https://github.com/{你的名字}/{你的仓库}/settings/pages` , 设置

![在这里插入图片描述](https://img-blog.csdnimg.cn/661f9dea78c8461abb485588ff8c7a28.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAeXVqaWUuemhhbw==,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center)

- 没有 pages 功能：只有公开项目才有，`私有` 项目不支持
- gh-pages 分支不存在：没有成功触发 action，成功触发，会自动生成分支 gh-pages，并将静态资源保存在 gh-pages 上
- cname 一直被重置：.github/workflows/my-pipeline.yml 最后一行没有设置好
- 域名设置没用：需要先做 `域名解析`，如阿里云，参考如下，`记录值` 是 github page 页面上给出的值的域名部分，！！！域名部分！！！域名部分

![在这里插入图片描述](https://img-blog.csdnimg.cn/5f10bc070aff4e89b5132b19d1701394.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAeXVqaWUuemhhbw==,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center)
## 源码参考
- [github.com/wolanx/wolanx-com](https://github.com/wolanx/wolanx-com)
- [成品](https://wolanx.com)

## 总结
2022年了，很多原本复杂的东西，都已经变得非常的容易获得，但网上的文章常年不升级。根据本文方便你更好的白嫖到一个免费博客，如果需要支持自定义域名，阿里云上购买也不到100RMB。
