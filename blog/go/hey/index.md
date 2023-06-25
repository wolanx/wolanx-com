---
title: hey压测工具 ab的go实现
date: 2018-03-29 18:27:38
tags:
  - go
---

# hey

go install -v github.com/rakyll/hey

```sh
./hey -c 50 -n 1000 http://api.bitdata.inner/market/coin

./hey -c 200 -n 20000 -m POST -d '{
        "bids": [
                ["6331.25", "1.1"],
                ["6331.1", "0.339"],
                ["633.97", "0.255"],
                ["633.55", "0.255"],
                ["633.75", "0.7371"]
        ],
        "asks": [
                ["6343.87", "0.255"],
                ["6343.88", "0.6"],
                ["6343.95", "0.5"],
                ["6344.31", "0.511"],
                ["6344.39", "0.3457"]
        ]
}' http://192.168.199.201:1777/depth?len=5&coinbase_id=1000&coinquote_id=2392&exchange_id=4

hey -c 10 -H "cookie: pii_session=74baa3e0-c50e-49a6-8332-e60975bfb57e;" https://dev2.gimc.grundfos.cn/api/application/124
```

```text
Summary:
  Total:	21.2181 secs
  Slowest:	6.3987 secs
  Fastest:	0.1012 secs
  Average:	0.9542 secs
  Requests/sec:	47.1295


Response time histogram:
  0.101 [1]	|
  0.731 [445]	|∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎
  1.361 [366]	|∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎∎
  1.990 [111]	|∎∎∎∎∎∎∎∎∎∎
  2.620 [50]	|∎∎∎∎
  3.250 [12]	|∎
  3.880 [7]	|∎
  4.509 [7]	|∎
  5.139 [0]	|
  5.769 [0]	|
  6.399 [1]	|


Latency distribution:
  10% in 0.3092 secs
  25% in 0.4710 secs
  50% in 0.7908 secs
  75% in 1.2031 secs
  90% in 1.7972 secs
  95% in 2.2439 secs
  99% in 3.7303 secs

Details (average, fastest, slowest):
  DNS+dialup:	0.0007 secs, 0.1012 secs, 6.3987 secs
  DNS-lookup:	0.0004 secs, 0.0000 secs, 0.0086 secs
  req write:	0.0000 secs, 0.0000 secs, 0.0005 secs
  resp wait:	0.9529 secs, 0.1009 secs, 6.3980 secs
  resp read:	0.0004 secs, 0.0001 secs, 0.0063 secs

Status code distribution:
  [200]	1000 responses
```

[./hey.go](./hey.go)
