---
title: lua db sqlite
date: 2024-06-03
tags: [ linux ]
---

## install

> apk add sqlite lua-sql-sqlite3

### crud

```lua
local sqlite3 = require "luasql.sqlite3"

-- 创建一个 SQLite 环境
local env = sqlite3.sqlite3()

-- 打开内存数据库
local db = env:connect("test.db")

-- 创建一个示例表
db:execute("CREATE TABLE test (id INTEGER PRIMARY KEY, content)")
db:execute("INSERT INTO test VALUES (1, 'Hello, World!')")
db:execute("INSERT INTO test VALUES (2, 'Lua with SQLite3')")

-- 查询并输出数据
local cursor = db:execute("SELECT * FROM test")

local row = cursor:fetch({}, "a")
print(row)
while row do
    print(string.format("Row %d: %s", row.id, row.content))
    row = cursor:fetch(row, "a")
end

-- 关闭游标和数据库连接
cursor:close()
db:close()
env:close()
```
