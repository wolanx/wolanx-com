---
title: git安装配置
date: 2016-06-10
tags:
  - linux
---

# doc

- [x] 45 个 Git 经典操作场景，专治不会合代码 https://mp.weixin.qq.com/s/o9LAEcbCvNXSzAOYKLND4w

# install

- https://git-scm.com/download/win
- C:\Git

## 安装

> 下载 https://github.com/git/git/releases

```sh
sudo yum update

//安装依赖的包
sudo yum install curl-devel expat-devel gettext-devel openssl-devel zlib-devel gcc perl-ExtUtils-MakeMaker

wget https://github.com/git/git/archive/v2.9.0-rc1.tar.gz
tar -zxvf v2.9.0-rc1.tar.gz
cd git-2.9.0-rc1/
make prefix=/usr/local/git all
sudo make prefix=/usr/local/git install

sudo vim /etc/profile
export PATH=/usr/local/git/bin:$PATH
source /etc/profile
```

## config user

```shell
git config --global user.email "825407762@qq.com"
git config --global user.name "wolanx"
git config --global credential.helper store
```

## config buffer

```shell
git remote add origin https://git.oschina.net/zhaoyujie/www.825407762.com.git
git push -u origin master

git checkout --orphan gh-pages
git push origin gh-pages

# buffer
git config --list
git config --global http.postBuffer 524288000
git config http.postBuffer 524288000
```

## 权限

git update-index --chmod=+x gradlew

## submodule

```sh
git submodule add -f -b main git@github.com:wolanx/jii.git
git submodule foreach git pull origin main

# 已有git的初始
git submodule init
git submodule update
```

## multi key

```text
Host ssh.dev.azure.com
HostName ssh.dev.azure.com
User git
IdentityFile C:\Users\admin\.ssh\id_azure
IdentitiesOnly yes
```

# 常用 cmd

```
git --no-pager log --graph --color=never --pretty=format:"%h %cr %an %s" -n20
git config alias.logs lg --color --graph --pretty=format:'%C(bold white)%h%Creset -%C(bold green)%d%Creset %s %C(bold green)(%cr)%Creset %C(bold blue)<%an>%Creset' --abbrev-commit --date=relative
git config alias.logs lg
git --no-pager lg --color=never
```

## gist

```shell
# 获取 gitid
git rev-parse HEAD
git rev-parse --short HEAD
```

## empty 完全覆盖

```shell
# 当前分支
git reset --hard origin/paytest
git push -f
```

## hook 钩子

> .git/hooks/commit-msg

```sh
#!/bin/sh
cd backend-gim

black . --check
if [ $? -ne 0 ]; then
  echo
  echo "black . --check failed"
  echo
  exit 1
fi
```

## lfs 大文件

- https://git-lfs.com/
- https://blog.yuanpei.me/posts/a-story-of-git-large-file-storage

## 代码统计

```shell
find . -name "*.js" -or -name "*.css" | xargs grep -v "^$" | wc -l

git log --author="zhaoyujie" --since="2016-12-10" --pretty=tformat: --numstat -- ./controllers ./library/service | gawk '{ add += $1 ; subs += $2 ; loc += $1 - $2 } END { printf "add %s remove %s total %s\n",add,subs,loc }'
git log --author="zhaoyujie" --since="2016-12-10" --pretty=tformat: --numstat -- ./controllers ./library/service | awk '{ add += $1 ; subs += $2 ; loc += $1 - $2 } END { printf "add %s remove %s total %s\n",add,subs,loc }'

// 代码数量统计
git ls-files | xargs wc -l
git log --author="zhaoyujie" --pretty=tformat: --numstat -- ./app/assets/less ./app/views ./app/components | gawk '{ add += $1 ; subs += $2 ; loc += $1 - $2 } END { printf "add %s remove %s total %s zhaoyujie\n",add,subs,loc }'
```

### 代码统计 cloc

```shell
# https://github.com/AlDanial/cloc
PS C:\Users\106006\Desktop\www\gimc> cloc --vcs=git
    1699 text files.
    1630 unique files.
      85 files ignored.

github.com/AlDanial/cloc v 2.00  T=17.38 s (93.8 files/s, 16301.6 lines/s)
-------------------------------------------------------------------------------
Language                     files          blank        comment           code
-------------------------------------------------------------------------------
JavaScript                     670          10314           9544         150549
Python                         426          10582           9395          52535
LESS                            90           2228            670          11398
SQL                             20            444             78           6757
JSON                             5              0              0           6281
YAML                            38              6            105           4022
SVG                            318             49            219           3460
HTML                            11            107              6            632
INI                              1             16              0            564
PO File                          2            257            366            456
Jupyter Notebook                 6              0            797            350
Markdown                         8             33              0            181
Lua                              4             28             18            140
GraphQL                          5              8              0             95
CSS                              2              7              0             72
TypeScript                      10              0              0             70
Dockerfile                       3             33             20             68
Text                             2              3              0             54
XML                              1              0              0             50
Properties                       2             16             72             43
Bourne Shell                     4             10              8             37
TOML                             1              0              1             21
make                             1              4              0             12
-------------------------------------------------------------------------------
SUM:                          1630          24145          21299         237847
-------------------------------------------------------------------------------
```
