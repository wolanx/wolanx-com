---
title: shell 脚本
date: 2017-12-13
categories:
  - linux
---

## sh

- Shell 教程 http://www.runoob.com/linux/linux-shell.html
- 分享70个经典的 Shell 脚本面试题与答案 https://www.jb51.net/article/135168.htm
- 6条shell小技巧，让脚本显得不再业余 https://mp.weixin.qq.com/s/ixVK4ockNE46bTdmarsDHQ

## 常用小技巧

```shell
#!/bin/bash
set -o nounset # 变量必须存在
set -o errexit # set -e

# bash -n xxx # 检查语法
set -o verbose # bash -v xxx
set -o xtrace # bash -x xxx

## 函数封装
log () {
  local prefix="[$(date +%Y/%m/%d\ %H:%M:%S)]:"
  echo "${prefix} $@" >&2
}
log "INFO" "a message"

## 函数封装
ExactBashComments() {
  egrep "^#"
}
cat /etc/hosts | ExactBashComments | wc
comments=$(ExactBashComments < /etc/hosts)

## 只读 默认值
readonly DEFAULT_VAL=${DEFAULT_VAL:--99}
echo $DEFAULT_VAL # -99

## if
if [[ 100 > "${DEFAULT_VAL}" ]]; then
    echo 222
fi
```

## tsdb => csv => sql => influx => oss

```shell
# cd /z/wolanx/GiMC/src/backend/temp/mig
# chcp.com 65001
# sh ./db2csv.sh
# nohup bash all.sh > ~/1.log 2>&1 &
set -e

tt="20201231"
tz="20200101"
while [[ "${tt}" -ge "${tz}" ]];
do
    #tt="20220502"
    echo "start ${tt}"

    python3 db2csv.py $tt
    python2 /root/datax-wolanx/bin/datax.py /root/datax-wolanx/mig/${tt}.json > /dev/null
    rm ${tt}.json

    cat /z/data/${tt}__* > /z/data/${tt}.csv
    cat /z/data/${tt}.csv | wc -l
    rm /z/data/${tt}__*

    echo -e "# DML\n# CONTEXT-DATABASE: gimc-hk" > /z/data/${tt}.sql
    cat /z/data/${tt}.csv | awk -F',' '{printf "sensor_0s,SNO=%s %s=%s %s\n", $3, $1, $4, $2}' >> /z/data/${tt}.sql
    rm /z/data/${tt}.csv

    sed -i '/checkhitsdb/d' /z/data/${tt}.sql
    sed -i '/= /d' /z/data/${tt}.sql
    sed -i 's/ _/_/g' /z/data/${tt}.sql
    influx -ssl -host ts-xxx.influxdata.tsdb.aliyuncs.com -port 8086 -username grundfos -password password -database gimc-hk -import -path=/z/data/${tt}.sql -precision=s

    ossutil cp /z/data/${tt}.sql oss://oss-dcc-gimc-tsdb-hk/ds-hk-sql/
    rm /z/data/${tt}.sql

    echo "end ${tt}"

    tt=$(date -d "${tt} -1day" +%Y%m%d)
done

```

### 上传文件批量

```
for ((a=10;a<=245;a++));do
    n=`printf "%03d" $a`;
    echo $n;
    echo $(curl -H 'Content-Type:text/plain' --data-binary @seofile_${n} "http://data.zz.baidu.com/urls?site=www.app-echo.com&token=3iyzwDoYB6IQAMKL");
done
```

## 循环机器执行

```sh
#! /bin/bash

ips="
172.16.30.13
172.16.30.14
172.16.30.15
172.16.30.25
172.16.30.26
172.16.30.27
"
for ip in $ips
do
    echo "do @$ip"
    echo "=============================="
    # ssh root@$ip "pwd"

    ssh root@$ip '#!/bin/sh
echo $LANG
'

	# echo $doStr
    # ssh root@$ip $doStr

    echo "\n\n"
done
```

## 久游代码部署

```
rsync -avl --delete    --exclude "log" --exclude "cli" --exclude "admin" --exclude "caches" --exclude "yaf_config.php" /usr/db/htdocs/au3/beta/ maintain@114.141.159.7:/usr/db/htdocs/au3/
```

```
#!/bin/bash
weball="
192.168.1.5
192.168.1.6
192.168.1.7
"
for ip in $weball
do
    rsync -avl --delete    --exclude "log" --exclude "cli" --exclude "caches" --exclude "upload" --exclude "fileupload"   -e ssh /usr/db/htdocs/yaf_aushop/preproduct/ maintain@$ip:/usr/db/htdocs/shop_with_yaf/

    echo "maintain@$ip is ok"

done
```

## with ssh

```
#! /bin/bash

ssh root@172.16.30.15 "pwd"

ssh www@172.16.45.87 '#!/bin/sh
	export LC_ALL=C
	hostname
	cd /srv/wwwroot/app
	git branch
	git pull
	git submodule init
	git submodule sync
	git submodule update
	git status
'
```
