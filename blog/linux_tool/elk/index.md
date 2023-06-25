---
title: elk 安装 bothub配置
date: 2018-03-22 16:14:31
tags:
  - linux
---

# elk docker版

### using

```text
    logging:
      driver: syslog
      options:
        syslog-address: 'tcp://10.1.0.123:5000'
```

- [x] grok debug http://grokdebug.herokuapp.com/
- [x] logstash conf https://www.elastic.co/guide/en/logstash/current/logstash-config-for-filebeat-modules.html


- [ ] logstash最佳实践 https://doc.yonyoucloud.com/doc/logstash-best-practice-cn/filter/grok.html

修改密码 cant
cat /etc/kibana/kibana.yml | grep -B 2 password

sed -ie 's/#elasticsearch.username: "user"/elasticsearch.username: "admin"/g' /etc/kibana/kibana.yml
sed -ie 's/#elasticsearch.password: "pass"/elasticsearch.password: "12341234"/g' /etc/kibana/kibana.yml

- [./docker-compose.yml](./docker-compose.yml)
- [./logstash.conf](./logstash.conf)
- [./filebeat/filebeat.yml](./filebeat/filebeat.yml)

# elk 完整版

## login

```
http://elk.bothub.ai/elk/
user
iruVkQ7L
```

## sender filebeat

## install

https://www.elastic.co/guide/en/beats/filebeat/current/filebeat-installation.html

## conf

vi /etc/filebeat/filebeat.yml

```text
filebeat.prospectors:

- input_type: log
  document_type: js_error
  paths:
    - /var/log/nginx/tracking.log

- input_type: log
  document_type: laravel_error
  paths:
    - /var/www/rapture-api/storage/logs/laravel-error-*.log

output.logstash:
  enabled: true
  hosts: ["10.140.0.3:5044"]
```

## restart

```
// test ok
filebeat.sh -configtest -e
/etc/init.d/filebeat restart
```

# getter elk

## docker

```
// 修改进程数
sysctl -w vm.max_map_count=262144
sysctl vm.max_map_count

// docker image sebp/elk:540
docker run -p 5601:5601 -p 9200:9200 -p 5044:5044 -it --name elk sebp/elk:540

server {
    listen 80;

    location / {
        ## 密码 http auth 密码生成
        # htpasswd -c .espasswd user
        # cat .espasswd
        # user:$apr1$Siq.2MpE$GREX96Q0RgpAYBnB67kKf0
        auth_basic              "Protected Kibana";
        auth_basic_user_file    /.espasswd;
        proxy_pass              http://kibana:5601;
    }
}
```

## query

```
type:nginx_access AND agent: '' -GoogleHC
type:js_error AND err_json.project:"rapture-admin-fe"
fields.appid: 'bitdata-web_php' AND fields.scope:'error'
```

## conf

```
cd /etc/logstash/conf.d
/opt/bitnami/ctlscript.sh restart logstash

input
{
    beats
    {
        ssl => false
        host => "0.0.0.0"
        port => 5044
    }
    gelf
    {
        host => "0.0.0.0"
        port => 12201
    }
    http
    {
        ssl => false
        host => "0.0.0.0"
        port => 8888
    }
    tcp
    {
        mode => "server"
        host => "0.0.0.0"
        port => 5010
    }
    udp
    {
        host => "0.0.0.0"
        port => 5000
    }
}

filter {
    if [type] == "nginx_access" {
        grok {
            match => { "message" => "%{COMBINEDAPACHELOG}" }
        }
        date {
            match => [ "timestamp" , "dd/MMM/yyyy:HH:mm:ss Z" ]
        }
    }
    if [type] == "laravel_error" {
        grok {
            match => { "message" => "\[%{TIMESTAMP_ISO8601:my_logdate}\] %{DATA:env}\.%{DATA:severity}: %{DATA:message_old}$" }
        }
        mutate {
            rename => {
                "@timestamp" => "read_timestamp"
                "message_old" => "message"
            }
        }
        date {
            match => [ "my_logdate", "yyyy-MM-dd HH:mm:ss" ]
            remove_field => "my_logdate"
            timezone => "Asia/Shanghai"
        }
    }
    if [type] == "js_error" {
        grok {
            match => { "message" => "\] \"%{DATA:request}\" \"%{DATA:agent}\" \"%{DATA:extra_fields}\"$" }
        }
        mutate {
            gsub => [
                "extra_fields", "\"","",
                "extra_fields", "\\x0A","",
                "extra_fields", "\\x22",'\"',
                "extra_fields", "(\\)",""
            ]
        }
        json {
            source => "extra_fields"
            target => "err_json"
            remove_field => ["message", "extra_fields"]
        }
        date {
            match => [ "timestamp" , "dd/MMM/yyyy:HH:mm:ss Z" ]
        }
    }
}

output
{
    // file { path => "/log_test/test-%{type}-%{+YYYY.MM.dd}.log" } // 调试用
    if "_grokparsefailure" in [tags] {
        file { path => "/log_test/error-%{type}-%{+YYYY.MM.dd}.log" }
    }

    elasticsearch
    {
        hosts => ["localhost"]
        index => "logstash-%{+YYYY.MM.dd}"
    }

}
```
