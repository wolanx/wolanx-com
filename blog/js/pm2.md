---
title: pm2进程管理
date: 2019-05-25 13:38:57
tags:
  - js
---

# install

npm install -g pm2

# for java

```json
{
  "name": "j-a",
  "script": "java",
  "args": [
    "-jar",
    "base-eureka/build/libs/base-eureka-1.0.jar"
  ],
  "exec_interpreter": "",
  "exec_mode": "fork"
}
```

npm install -g pm2

# for k3s

```json
{
  "name": "k3s",
  "script": "k3s",
  "args": [
    "server",
    "--docker"
  ],
  "exec_interpreter": "",
  "exec_mode": "fork"
}
```

pm2 start pm2.json

# log

~/.pm2/logs

## 常用

```sh
pm2 ls
pm2 start app
pm2 stop app
pm2 delete app
pm2 restart app
```
