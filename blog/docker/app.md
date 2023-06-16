---
title: docker app
date: 2018-03-22
tags: [docker]
---

## infrastructure

### portainer 管理

```shell
docker run -d --restart=unless-stopped --name portainer -p 1234:9000 -v "/var/run/docker.sock:/var/run/docker.sock" portainer/portainer-ce:2.6.0
docker run -d --restart=unless-stopped --name portainer -p 1234:9000 -v "/var/run/docker.sock:/var/run/docker.sock" portainer/portainer:1.23.2
# //./pipe/docker_engine
# "hosts": ["tcp://0.0.0.0:2375"]
server {
    listen       80;
    charset      utf-8;
    server_name  uat.docker.manager;
    location / {
        proxy_pass http://127.0.0.1:1234;

        proxy_http_version 1.1;
        proxy_set_header Connection "";

        proxy_set_header Host $host;
        proxy_set_header Scheme $scheme;
    }
}
```

### registry

```shell
DOCKER_OPTS="--insecure-registry 192.168.1.19:5000"
docker run -d -p 5000:5000 --restart=always --name registry registry:2.6.2

docker push 192.168.199.115:5000/r1
docker rmi  192.168.199.115:5000/r1
docker pull 192.168.199.115:5000/r1

# /var/lib/registry/docker/registry/v2 # tree -L 4
```

### cadvisor

```shell
sudo docker run \
  --volume=/:/rootfs:ro \
  --volume=/var/run:/var/run:rw \
  --volume=/sys:/sys:ro \
  --volume=/var/lib/docker/:/var/lib/docker:ro \
  --volume=/dev/disk/:/dev/disk:ro \
  --publish=2345:8080 \
  --detach=true \
  --name=cadvisor \
  google/cadvisor:v0.28.3
```

## db

### mysql

```shell
docker run --restart=unless-stopped --name mysql-1 -it -d \
  -v "$PWD":/var/lib/mysql -p 3306:3306 -e MYSQL_ROOT_PASSWORD=password -e TZ=Asia/Shanghai mysql:8.0.15 \
  --character-set-server=utf8mb4 --collation-server=utf8mb4_general_ci
# --character-set-server=utf8 --collation-server=utf8_general_ci
```

### redis

```shell
docker run --restart=unless-stopped --name redis-1 -d -p 6379:6379 redis:6.0.3-alpine
docker run --restart=unless-stopped --name redis-1 -d -p 6379:6379 redis:3.2.9-alpine
docker run --name some-redis -d redis:alpine
docker run -it --link some-redis:redis --rm redis:alpine redis-cli -h 139.196.14.14 -p 6379

docker run --restart=unless-stopped -v "$PWD/redis.conf":/usr/local/etc/redis/redis.conf -v "$PWD":/data --name redis-2 -d -p 6379:6379 redis:3.2.9-alpine redis-server /usr/local/etc/redis/redis.conf

redis-server --requirepass 12345
```

### mongodb

```shell
docker run --restart=unless-stopped --name mongo-1 -d -p 27017:27017 -v "$PWD":/etc/mongo mongo:3.6.4
# 常用命令
show dbs # 全部db
use test # 进database
db # 查看当前database
db.stats(); # 显示当前db状态
db.dropDatabase();  #删除当前使用数据库

# user
show users; # 显示当前所有用户
db.createUser({user:"ynh-test",pwd:"ynh-test",roles:[{role:"userAdmin",db:"ynh-test"}]}); # 创建用户
db.removeUser("userName"); # 删除用户

db.tb_test.insert({"_id":"520","name":"xiaoming"})
db.tb_test.find();
```

### phpmyadmin

```shell
docker run --restart=unless-stopped --name pmd -d -p 33060:80 phpmyadmin/phpmyadmin:4.7
-e PMA_HOST=139.196.14.10
vi /etc/phpmyadmin/config.user.inc.php
supervisorctl restart all
```

## other

### zentao 禅道
```text
docker run -d -p 8880:80 \
        -e USER="root" -e PASSWD="password" \
        -e BIND_ADDRESS="false" \
        -e SMTP_HOST="163.177.90.125 smtp.exmail.qq.com" \
        -v "$PWD":/opt/zbox/ \
        --name zentao-server \
        idoop/zentao:latest
```
