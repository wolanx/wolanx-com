---
title: thrift rpc 协议
date: 2016-08-11T10:15:36+08:00
tags: [linux]
---

# doc
- [x] Thrift RPC 使用指南实战(附golang&PHP代码) [http://studygolang.com/articles/3110](http://studygolang.com/articles/3110)

## support
```sh
thrift 1.0.0-dev

Building C++ Library ......... : no
Building C (GLib) Library .... : no
Building Java Library ........ : no
Building C# Library .......... : no
Building Python Library ...... : no
Building Ruby Library ........ : no
Building Haxe Library ........ : no
Building Haskell Library ..... : no
Building Perl Library ........ : no
Building PHP Library ......... : yes
Building Dart Library ........ : no
Building Erlang Library ...... : no
Building Go Library .......... : yes
Building D Library ........... : no
Building NodeJS Library ...... : yes
Building Lua Library ......... : no
```

## demo1
```sh

git clone https://github.com/apache/thrift.git

./bootstrap.sh
./configure --with-boost=/usr/local

yum install -y libtool
yum install -y byacc #yacc: command not found

make
make install

go get git.apache.org/thrift.git/lib/go/thrift
新建项目目录testphp，然后把thrift/lib/php/lib复制到testphp目录下面
```

`batu.thrift`
```
namespace go batu.demo
namespace php batu.demo

/**
 * 结构体定义
 */
struct Article{
    1: i32 id,
    2: string title,
    3: string content,
    4: string author,
}

const map<string,string> MAPCONSTANT = {'hello':'world', 'goodnight':'moon'}

service batuThrift {
    list<string> CallBack(1:i64 callTime, 2:string name, 3:map<string, string> paramMap),
    void put(1: Article newArticle),
}
```

`server.go`
```go
package main

import (
	"fmt"
	"os"
	"time"

	"./batu/demo" //注意导入Thrift生成的接口包
	"git.apache.org/thrift.git/lib/go/thrift"
)

const (
	NetworkAddr = "192.168.1.101:9090" //监听地址&端口
)

type batuThrift struct {
}

func (this *batuThrift) CallBack(callTime int64, name string, paramMap map[string]string) (r []string, err error) {
	fmt.Println("-->from client Call:", time.Unix(callTime, 0).Format("2006-01-02 15:04:05"), name, paramMap)
	r = append(r, "key:"+paramMap["a"]+"    value:"+paramMap["b"])
	return
}

func (this *batuThrift) Put(s *demo.Article) (err error) {
	fmt.Printf("Article--->id: %d\tTitle:%s\tContent:%t\tAuthor:%d\n", s.ID, s.Title, s.Content, s.Author)
	return nil
}

func main() {
	transportFactory := thrift.NewTFramedTransportFactory(thrift.NewTTransportFactory())
	protocolFactory := thrift.NewTBinaryProtocolFactoryDefault()
	//protocolFactory := thrift.NewTCompactProtocolFactory()

	serverTransport, err := thrift.NewTServerSocket(NetworkAddr)
	if err != nil {
		fmt.Println("Error!", err)
		os.Exit(1)
	}

	handler := &batuThrift{}
	processor := demo.NewBatuThriftProcessor(handler)

	server := thrift.NewTSimpleServer4(processor, serverTransport, transportFactory, protocolFactory)
	fmt.Println("thrift server in", NetworkAddr)
	server.Serve()
}
```

`client.go`
```go
package main

import (
	"fmt"
	"net"
	"os"
	"strconv"
	"time"

	"./batu/demo"
	"git.apache.org/thrift.git/lib/go/thrift"
)

const (
	HOST = "127.0.0.1"
	PORT = "9090"
)

func main() {
	startTime := currentTimeMillis()

	transportFactory := thrift.NewTFramedTransportFactory(thrift.NewTTransportFactory())
	protocolFactory := thrift.NewTBinaryProtocolFactoryDefault()

	transport, err := thrift.NewTSocket(net.JoinHostPort(HOST, PORT))
	if err != nil {
		fmt.Fprintln(os.Stderr, "error resolving address:", err)
		os.Exit(1)
	}

	useTransport := transportFactory.GetTransport(transport)
	client := demo.NewBatuThriftClientFactory(useTransport, protocolFactory)
	if err := transport.Open(); err != nil {
		fmt.Fprintln(os.Stderr, "Error opening socket to "+HOST+":"+PORT, " ", err)
		os.Exit(1)
	}
	defer transport.Close()

	for i := 0; i < 10; i++ {
		paramMap := make(map[string]string)
		paramMap["a"] = "batu.demo"
		paramMap["b"] = "test" + strconv.Itoa(i+1)
		r1, _ := client.CallBack(time.Now().Unix(), "go client", paramMap)
		fmt.Println("GOClient Call->", r1)
	}

	model := demo.Article{1, "Go第一篇文章", "我在这里", "liuxinming"}
	client.Put(&model)
	endTime := currentTimeMillis()
	fmt.Printf("本次调用用时:%d-%d=%d毫秒\n", endTime, startTime, (endTime - startTime))

}

func currentTimeMillis() int64 {
	return time.Now().UnixNano() / 1000000
}
```

`client.php`
```php
<?php
namespace batu\testDemo;
header("Content-type: text/html; charset=utf-8");
$startTime = getMillisecond();//记录开始时间

$ROOT_DIR = realpath(dirname(__FILE__) . '/');
$GEN_DIR = realpath(dirname(__FILE__) . '/') . '/gen-php';
require_once $ROOT_DIR . '/Thrift/ClassLoader/ThriftClassLoader.php';

use Thrift\ClassLoader\ThriftClassLoader;
use Thrift\Protocol\TBinaryProtocol;
use Thrift\Transport\TBufferedTransport;
use Thrift\Transport\TFramedTransport;
use Thrift\Transport\TSocket;
use Thrift\Transport\TSocketPool;

$loader = new ThriftClassLoader();
$loader->registerNamespace('Thrift', $ROOT_DIR);
$loader->registerDefinition('batu\demo', $GEN_DIR);
$loader->register();

// $thriftHost = '127.0.0.1'; //UserServer接口服务器IP
$thriftHost = '192.168.1.101'; //UserServer接口服务器IP
$thriftPort = 9090;            //UserServer端口

$socket = new TSocket($thriftHost, $thriftPort);
$socket->setSendTimeout(10000);#Sets the send timeout.
$socket->setRecvTimeout(20000);#Sets the receive timeout.
//$transport = new TBufferedTransport($socket); #传输方式：这个要和服务器使用的一致 [go提供后端服务,迭代10000次2.6 ~ 3s完成]
$transport = new TFramedTransport($socket); #传输方式：这个要和服务器使用的一致[go提供后端服务,迭代10000次1.9 ~ 2.1s完成，比TBuffer快了点]
$protocol = new TBinaryProtocol($transport);  #传输格式：二进制格式
$client = new \batu\demo\batuThriftClient($protocol);# 构造客户端

$transport->open();
$socket->setDebug(TRUE);

for ($i = 1; $i < 11; $i++) {
    $item = array();
    $item["a"] = "batu.demo";
    $item["b"] = "test" . $i;
    $result = $client->CallBack(time(), "php client", $item); # 对服务器发起rpc调用
    echo "PHPClient Call->" . implode('', $result) . "\n";
}

$s = new \batu\demo\Article();
$s->id = 1;
$s->title = '插入一篇测试文章';
$s->content = '我就是这篇文章内容';
$s->author = 'liuxinming';
$client->put($s);

$s->id = 2;
$s->title = '插入二篇测试文章';
$s->content = '我就是这篇文章内容';
$s->author = 'liuxinming';
$client->put($s);

$endTime = getMillisecond();

echo "本次调用用时: :" . $endTime . "-" . $startTime . "=" . ($endTime - $startTime) . "毫秒\n";

function getMillisecond() {
    list($t1, $t2) = explode(' ', microtime());
    return (float)sprintf('%.0f', (floatval($t1) + floatval($t2)) * 1000);
}

$transport->close();
```