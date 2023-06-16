---
title: redis
date: 2018-05-03
tags: [db]
---

## redis

- 命令参考 http://doc.redisfans.com
- 持久化persistence http://doc.redisfans.com/topic/persistence.html
- x stream https://zhuanlan.zhihu.com/p/37591626

## stream

```shell
redis-cli -h 10.231.9.159 -p 32621
xrange x:topic:test - + count 10
xadd x:topic:test * name youming age 60

# 控制长度
xadd x:topic:test maxlen ~ 100 * name youming age 60
xtrim x:topic:test maxlen ~ 100

xlen x:topic:test
```

### java stream

```java
public static void main(String[] args) {
    Jedis r = new Jedis("x.x.x.x", 6379);
    r.select(11);

    XReadGroupParams p = XReadGroupParams.xReadGroupParams().count(20).noAck();
    Map<String, StreamEntryID> entry = Collections.singletonMap("jdddddd", StreamEntryID.UNRECEIVED_ENTRY);

    List<Map.Entry<String, List<StreamEntry>>> entries = r.xreadGroup("gggn", "cccn", p, entry);

    if (entries != null) {
        for (Map.Entry<String, List<StreamEntry>> stringListEntry : entries) {
            for (StreamEntry sEntry : stringListEntry.getValue()) {
                Map<String, String> fields = sEntry.getFields();
                System.out.println(fields);
            }
        }
    }
}
```
