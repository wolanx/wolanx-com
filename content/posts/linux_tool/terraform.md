---
title: terraform
date: 2019-08-30T15:11:00+08:00
categories: [linux]
tags: [cicd]
---

## doc
 - [x] Docker: docker_container https://www.terraform.io/docs/providers/docker/r/container.html
 - [x] terraform docker mycat https://blog.csdn.net/weixin_28738845/article/details/88596829

## install
>https://www.terraform.io/downloads.html

```sh
wget https://releases.hashicorp.com/terraform/0.12.18/terraform_0.12.18_linux_amd64.zip
unzip terraform_0.12.18_linux_amd64.zip -d .
mv terraform /usr/bin/
```

## cache
```sh
export TF_PLUGIN_CACHE_DIR="$HOME/.terraform.d/plugin-cache" # windows is must
~/.terraform.rc

tee ~/.terraformrc <<-'EOF'
plugin_cache_dir   = "$HOME/.terraform.d/plugin-cache"
disable_checkpoint = true
EOF
```

## cmd
 - terraform init
 - terraform apply -target=docker_container.mysql-1

```sh
provider "docker" {
  default = "unix:///var/run/docker.sock"
  # default = "tcp://127.0.0.1:2375"
}

variable "edf" {
  default = "qqqq"
}

resource "docker_container" "ptest" {
  name  = "ptest"
  image = "ptest"
  ports {
    internal = 5000
    external = 2222
  }
  provisioner "local-exec" {
    command = "echo ${var.password}"
  }
}

resource "docker_container" "mysql-1" {
  restart = "unless-stopped"
  name    = "mysql-1"
  image   = "mysql:8.0.15"
  command = [
    "--character-set-server=utf8mb4",
    "--collation-server=utf8mb4_unicode_ci",
  ]
  env = [
    "MYSQL_ROOT_PASSWORD=${var.password}",
    "TZ=Asia/Shanghai",
  ]
  ports {
    internal = 3306
    external = 3306
  }
}

```
