---
title: vagrant
date: 2022-01-10T12:00:00+08:00
categories:
  - tool
  - liunx
tags:
---

## Intro
快速可自定义的虚拟机，几行命令搞定，不用再设置一堆东西。
自定义文件Vagrantfile实现环境重复利用 https://www.vagrantup.com/intro

## Install
```shell
https://www.vagrantup.com/downloads
# wget https://releases.hashicorp.com/vagrant/2.2.19/vagrant_2.2.19_x86_64.msi
```

## Start

```shell
vagrant init generic/alpine312  # https://vagrantcloud.com/search

vagrant up --provider=hyperv    # start
vagrant halt                    # stop

vagrant ssh

vagrant destroy # delete
```

## Other

```shell
vagrant box list                # list image
vagrant global-status           # list vm
vagrant destroy 1a2b3c4d

# 手动下包 wget https://app.vagrantup.com/generic/boxes/alpine312/versions/3.6.4/providers/hyperv.box
vagrant box add my/alpine312 hyperv.box

# 127.0.0.1:2222 # root vagrant
```

## Vagrantfile

```shell
# touch Vagrantfile
Vagrant.configure("2") do |config|
  config.vm.box = "generic/alpine312"
end
```
