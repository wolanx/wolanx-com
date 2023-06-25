---
title: elasticsearch 全文搜索
date: 2018-05-09
updated: 2019-05-08 17:39:00
tags:
  - db
---

## install

```sh
docker run -d -p 9200:9200 -p 9300:9300 --name es-1 elasticsearch:5.6.16-alpine
# 查询tool
docker run -d -p 5601:5601 --name kibana --link es-1:elasticsearch kibana:5.6.16
# 查询tool sql转es
docker run -d -p 9800:9800 --name es-hd --link es-1:demo containerize/elastichd
```

## doc

http://how2j.cn/k/search-engine/search-engine-index-manage/1694.html

## http api

```
http://<url>:9200/<index>/<type>/<id>
curl http://localhost:9200/db_name/table_name/a
curl http://localhost:9200/db_name/table_name/_search?q=sql
```

## htop

```
#磁盘
curl http://localhost:9200/_cat/shards?v
curl http://localhost:9200/_cat/allocation?v

```

# help

```
/_cat/
/_cat/indices?v
```

## kibana操作

```sh
# 查询 排序
GET /how2java/_search
{
  "query": { "match_all": {} },
  "sort": [
    { "price": "desc" }
  ]
}
# 部分字段
GET /how2java/_search
{
	"query":{"match_all":{}},
	"_source":["name","price"]
}
# 条件
GET /how2java/_search
{
	"query":{"match":{"name":"时尚连衣裙"}}
}

# 聚合 select count(*),place from product group by place limit 0,3  
GET /how2java/_search
{
  "size": 0,
  "aggs": {
    "group_by_place": {
      "terms": {
        "field": "place.keyword",
        "size": 3
      }
    }
  }
}
```

## curl操作

```sh
# 1 加索引 其实就是database
curl -X PUT http://172.16.30.13:9200/how2java?pretty # 添加
curl http://172.16.30.13:9200/_cat/indices?v # 1 检查索引
curl -X DELETE http://172.16.30.13:9200/how2java?pretty # 1 删除索引

# 2 装插件 分词
elasticsearch-plugin install https://github.com/medcl/elasticsearch-analysis-ik/releases/download/v5.6.16/elasticsearch-analysis-ik-5.6.16.zip
## 检查插件
curl -s http://172.16.30.13:9200/_analyze -H 'content-type: application/json' -d '{
  "analyzer":"ik_max_word",
  "text":"护眼带光源"
}' | jq

# 添加
curl -s -X PUT http://172.16.30.13:9200/how2java/product/1?pretty -H 'content-type: application/json' -d '{
  "name": "蜡烛"
}' | jq
# 查询
curl http://172.16.30.13:9200/how2java/product/1?pretty
# 修改 添加覆盖用
## POST /how2java/product/1/_update
# 删除单个
curl -X DELETE http://172.16.30.13:9200/how2java/product/1?pretty

# 批量添加
curl -s -X POST http://172.16.30.13:9200/_bulk -H 'content-type: application/json' -d '
{"index":{"_index":"how2java","_type":"product","_id":10001}}
{"code":"540785126782","price":398,"name":"房屋卫士自流平美缝剂瓷砖地砖专用双组份真瓷胶防水填缝剂镏金色","place":"上海","category":"品质建材"}
{"index":{"_index":"how2java","_type":"product","_id":10002}}
{"code":"24727352473","price":21.799999237060547,"name":"艾瑞泽手工大号小号调温热熔胶枪玻璃胶枪硅胶条热溶胶棒20W-100W","place":"山东青岛","category":"品质建材"}
{"index":{"_index":"how2java","_type":"product","_id":10003}}'

# 批量文件导入 http://how2j.cn/k/search-engine/search-engine-curl-batch/1704.html
## pan.baidu source_java/products_16w条elasticsearch.json.rar
curl -X POST http://172.16.30.13:9200/how2java/product/_bulk?refresh -H 'content-type: application/json' --data-binary "@products.json"

# search
## 部分字段  "_source": ["name","price"]
## 条件 "query": { "match_all": {} },
## 条件 "query": { "match": { "name": "时尚连衣裙" } },
## 分页 "from": 1, "size": 3,
curl -s http://172.16.30.13:9200/how2java/_search -d '{
  "query": { "match": { "name": "时尚连衣裙" } },
  "sort": [
    { "price": "desc" }
  ],
  "_source": ["name","price"]
}' | jq

# 清空索引
curl -X DELETE http://localhost:9200/_all

curl -X POST http://localhost:9200/_delete_by_query -d '{
  "query": {
    "match_all": {}
  }
}'
```
