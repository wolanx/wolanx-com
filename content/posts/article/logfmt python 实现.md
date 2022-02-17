---
title: logfmt python 实现
date: 2022-02-11T15:45:10+08:00
categories:
  - csdn
tags:
---

> https://blog.csdn.net/wolanx/article/details/122733747

## Intro
现在很多主流日志系统推崇 `logfmt` 格式，但是 `python` 中配套的不多，这边给个参考

日志大概长这样
```shell
# log.info("haha")
time="2022-01-28T17:00:52+0800" type=default level=info method="a.py:82" msg="haha"
# log.warning("no access")
time="2022-01-28T17:00:52+0800" type=default level=warning method="a.py:83" msg="no access"
```

## 实现过程
- PiiLogger 继承 logging.Logger
	- 绑定自定义的 formatter
	- 清空原有 handler 否则会重复输出
	- 把 formatter 注册给 handler
	- hook 外层 变量 （如：每条log带上web请求的uuid）
- PiiLoggerFormatter 继承 logging.Formatter
	- 实现 format 的 自定义，内嵌变量请参考 [官方 LogRecord 属性](https://docs.python.org/zh-cn/3/library/logging.html#logrecord-attributes)
	- hook 外层 变量

## 外层变量的使用
```python
def getUUid():
    v = None
    if has_request_context(): # 判断 flask web 的生命周期下
        v = Pii.app.get("uuid", "") # 根据自己业务写

    return {"uuid": v}

log = PiiLogger.manager.getLogger("default")
log.withFormatter(getUUid)
log.info("haha")
# time="2022-01-29T10:38:21+0800" type=default level=info method="views.request_after" uuid="860ea870-80ac-11ec-a366-1eaadecc49e8" msg="haha"
```

## 完整代码
```python
import logging
import numbers
from json.encoder import JSONEncoder
from typing import Any


class PiiLogger(logging.Logger):
    def __init__(self, name: str, level=logging.NOTSET) -> None:
        super().__init__(name, level)

        self.setLevel(logging.INFO)
        self.root.handlers.clear()

        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)
        self.formatter = PiiLoggerFormatter(
            fmt='time="%(asctime)s" type=%(name)s level=%(levelname)s method="%(method)s"',
            datefmt="%Y-%m-%dT%H:%M:%S%z",
        )
        ch.setFormatter(self.formatter)

        self.addHandler(ch)

    def withFields(self, ret):
        print(ret)
        return self

    def withFormatter(self, func):
        self.formatter.setExt(func)


class PiiLoggerFormatter(logging.Formatter):
    ext: Any = None

    def format(self, record):
        if record.funcName == "<module>":
            method = f"{record.filename}:{record.lineno}"
        else:
            method = f"{record.module}.{record.funcName}"

        record.__setattr__("method", method)
        record.levelname = record.levelname.lower()
        msg = JSONEncoder().encode(str(record.msg))

        ret = super().format(record)

        if self.ext:
            mor = logfmt(self.ext())
            if mor:
                ret += " " + mor

        return f"{ret} msg={msg}"

    def setExt(self, func):
        self.ext = func


def logfmt(extra):
    outarr = []
    for k, v in extra.items():
        if v is None:
            outarr.append("%s=" % k)
            continue

        if isinstance(v, bool):
            v = "true" if v else "false"
        elif isinstance(v, numbers.Number):
            pass
        else:
            if isinstance(v, (dict, object)):
                v = str(v)
            v = '"%s"' % v.replace('"', '\\"')
        outarr.append("%s=%s" % (k, v))
    return " ".join(outarr)


PiiLogger.manager.setLoggerClass(PiiLogger)


if __name__ == "__main__":
    # use
    log = PiiLogger.manager.getLogger("default")
    log.info("haha")
    log.warning("no access")
```
