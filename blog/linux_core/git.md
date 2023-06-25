---
title: git安装配置
date: 2016-06-10
tags:
  - linux
---

# doc

- [x] 45 个 Git 经典操作场景，专治不会合代码 https://mp.weixin.qq.com/s/o9LAEcbCvNXSzAOYKLND4w

# config

```
git config --global user.email "825407762@qq.com"
git config --global user.name "wolanx"
git config --global credential.helper store
```

# 常用 gl

```
git --no-pager log --graph --color=never --pretty=format:"%h %cr %an %s" -n20
git config alias.logs lg --color --graph --pretty=format:'%C(bold white)%h%Creset -%C(bold green)%d%Creset %s %C(bold green)(%cr)%Creset %C(bold blue)<%an>%Creset' --abbrev-commit --date=relative
git config alias.logs lg
git --no-pager lg --color=never
```

## multi key

```text
Host ssh.dev.azure.com
HostName ssh.dev.azure.com
User git
IdentityFile C:\Users\admin\.ssh\id_azure
IdentitiesOnly yes
```

# install

- https://git-scm.com/download/win
- C:\Git

# only one

git clone -n https://github.com/aliyun/aliyun-openapi-python-sdk --depth 1
git checkout HEAD aliyun-python-sdk-core/aliyunsdkcore

## 权限

git update-index --chmod=+x gradlew

## submodule

```sh
git submodule add -f -b master git@47.100.245.85:php/center.git
git submodule foreach git pull origin master

# 已有git的初始
git submodule init
git submodule update
```

### .git/hooks/commit-msg

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

### 设置

```sh
git remote add origin https://git.oschina.net/zhaoyujie/www.825407762.com.git
git push -u origin master

git checkout --orphan empty_branch

#buffer
git config --list
git config --global http.postBuffer 524288000
git config http.postBuffer 524288000
```

### 安装

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

### 代码统计

```text
find . -name "*.js" -or -name "*.css" | xargs grep -v "^$" | wc -l

git log --author="zhaoyujie" --since="2016-12-10" --pretty=tformat: --numstat -- ./controllers ./library/service | gawk '{ add += $1 ; subs += $2 ; loc += $1 - $2 } END { printf "add %s remove %s total %s\n",add,subs,loc }'
git log --author="zhaoyujie" --since="2016-12-10" --pretty=tformat: --numstat -- ./controllers ./library/service | awk '{ add += $1 ; subs += $2 ; loc += $1 - $2 } END { printf "add %s remove %s total %s\n",add,subs,loc }'

// 代码数量统计
git ls-files | xargs wc -l
git log --author="zhaoyujie" --pretty=tformat: --numstat -- ./app/assets/less ./app/views ./app/components | gawk '{ add += $1 ; subs += $2 ; loc += $1 - $2 } END { printf "add %s remove %s total %s zhaoyujie\n",add,subs,loc }'
```

### 小命令

```text
// 获取 gitid
git rev-parse HEAD
git rev-parse --short HEAD
```

### 完全覆盖

```shell
# 当前分支
git reset --hard origin/paytest
git push -f
```

## lfs 大文件

- https://git-lfs.com/
- https://blog.yuanpei.me/posts/a-story-of-git-large-file-storage

