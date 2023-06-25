---
title: curl 参数
date: 2016-02-05
tags:
  - linux
---

# curl

```shell
# 例1：抓取页面到指定文件，如果有乱码可以使用iconv转码
curl -o baidu.html www.baidu.com
curl –s –o baidu.html www.baidu.com |iconv -f utf-8  #减少输出信息
# 例2：模拟浏览器头（user-agent）
curl -A "Mozilla/4.0 (compatible;MSIE 6.0; Windows NT 5.0)" www.baidu.com
# 例3：处理重定向页面
curl –L http://192.168.1.100/301.php   #默认curl是不处理重定向
# 例4：模拟用户登陆，保存cookie信息到cookies.txt文件，再使用cookie登陆
curl -c ./cookies.txt -F NAME=user -F PWD=***URL            #NAME和PWD是表单属性不同，每个网站基本都不同
curl -b ./cookies.txt –o URL
# 例5：获取HTTP响应头headers
curl -I http://www.baidu.com
curl -D ./header.txt http://www.baidu.com   #将headers保存到文件中
# 例6：访问HTTP认证页面
curl –u user:pass URL
#例7：通过ftp上传和下载文件
curl -T filename ftp://user:pass@ip/docs  #上传
curl -O ftp://user:pass@ip/filename   #下载
# 忽略 tls
curl --insecure https://10.10.18.158:6443
```

## 手动hosts

curl --resolve www.bitfinex.com:443:104.16.174.181 https://www.bitfinex.com
curl --resolve www.accountchooser.com:443:216.239.38.10 https://www.accountchooser.com

## 时间分析

```shell
curl -o /dev/null -w %{time_namelookup}::%{time_connect}::%{time_starttransfer}::%{time_total}::%{speed_download}"\n" "http://www.taobao.com"
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current  
                                 Dload  Upload   Total   Spent    Left  Speed  
100 28774    0 28774    0     0  1145k      0 --:--:-- --:--:-- --:--:-- 7550k  
0.014::0.016::0.020::0.025::1173060.000

-o:把curl 返回的html、js 写到垃圾回收站[ /dev/null]
-s:去掉所有状态
-w:按照后面的格式写出rt
time_namelookup:DNS 解析域名[www.taobao.com]的时间
time_commect:client和server端建立TCP 连接的时间
time_starttransfer:从client发出请求；到web的server 响应第一个字节的时间
time_total:client发出请求；到web的server发送会所有的相应数据的时间
speed_download:下周速度  单位 byte/s

上面时间rt的理解【单位是 秒】
0.014: DNS 服务器解析www.taobao.com 的时间单位是s   
0.015: client发出请求，到c/s 建立TCP 的时间；里面包括DNS解析的时间  
0.018: client发出请求；到s响应发出第一个字节开始的时间；包括前面的2个时间  
0.019: client发出请求；到s把响应的数据全部发送给client；并关闭connect的时间  
1516256.00 ：下周数据的速度  

建立TCP连接到server返回client第一个字节的时间：0.018s - 0.015s = 0.003s  
server把响应数据发送给client的时间：0.019s - 0.018 = 0.01s
```

### -w

```text
curl -w "
TCP handshake: %{time_connect}
SSL handshake: %{time_appconnect}
SSL handshake: %{time_appconnect}
time_total,%{time_total}
" -so /dev/null https://www.alipay.com

curl -w "
time_appconnect,%{time_appconnect},SSL handshake
time_connect,%{time_connect},TCP handshake
time_namelookup,%{time_namelookup}
time_pretransfer,%{time_pretransfer}
time_starttransfer,%{time_starttransfer}
time_redirect,%{time_redirect}
time_total,%{time_total}
url_effective,%{url_effective}
content_type,%{content_type}
local_ip,%{local_ip}
remote_ip,%{remote_ip}
speed_download,%{speed_download}
" -so /dev/null https://api.bitdata.com.cn/ | column -s',' -t
```
