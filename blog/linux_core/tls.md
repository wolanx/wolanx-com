---
title: tls ssl openssl
date: 2017-04-27
tags:
  - linux
---

## openssl

- openssl pkcs12 https://www.cnblogs.com/aixiaoxiaoyu/articles/8796372.html
- 自签 https://learn.microsoft.com/zh-cn/azure/application-gateway/self-signed-certificates
- .cer 根证书

# 查看 cert

keytool -printcert -file ca.crt

```sh
# 普通
openssl genrsa -out private.key 2048
# password
openssl genrsa -passout pass:_passphrase_ -out private.key 2048

# 私钥 => 公钥
openssl rsa -in private.key -pubout -out public.key
# 私钥 => 公钥 password
openssl rsa -in private.key -passin 'pass:P@s5w0rD' -pubout -out public.key

## 私钥 => pfx
```shell
mima=_passphrase_
openssl req -new -key private.key -out ssl.csr # 证书请求文件
openssl x509 -req -days 3650 -in ssl.csr -signkey private.key -out ssl.crt # 证书文件
openssl pkcs12 -export -inkey private.key -in ssl.crt -out ssl.pfx

## pfx renew crt
openssl pkcs12 -in a.pfx -nocerts -out a.key -nodes
# copy crt to here
openssl pkcs12 -export -out b.pfx -inkey a.key -in b.crt # or b.pem
```

# window pfx => https

openssl pkcs12 -in a.pfx -nodes -out a.pem -passin 'pass:GfosCn20!'
openssl pkcs12 -in a.pfx -nocerts -out a.pem -nodes -passin 'pass:Sandy2020' # full chain
openssl rsa -in a.pem -out a.key
openssl x509 -in a.pem -out a.crt
kubectl create secret tls ccm-https --key a.key --cert a.crt --namespace=gim-uat

## end can

zx.sh

```shell
mima=$(cat zx.txt)
echo $mima

openssl pkcs12 -in zx.pfx -nokeys -passin "pass:${mima}" | sed -ne '/-BEGIN CERTIFICATE-/,/-END CERTIFICATE-/p' > a
openssl pkcs12 -in zx.pfx -nocerts -nodes -passin "pass:${mima}" | sed -ne '/-BEGIN PRIVATE KEY-/,/-END PRIVATE KEY-/p' > b

cat a | base64 -w 0 > aa
cat b | base64 -w 0 > bb
```

# http auth

openssl passwd -crypt admin123
echo "admin:$(openssl passwd -crypt admin123)" > .espasswd

```

# 4要素
 - cert.pem        	服务端证书
 - chain.pem       	浏览器需要的所有证书但不包括服务端证书，比如根证书和中间证书
 - fullchain.pem   	包括了cert.pem和chain.pem的内容
 - privkey.pem     	证书的私钥

```sh
# cert
openssl pkcs12 -in a.pfx -nokeys -clcerts -out cert.pem -passin 'pass:GfosCn20!'
# chain
openssl pkcs12 -in a.pfx -nokeys -cacerts -out chain.pem -passin 'pass:GfosCn20!'
# fullchain
openssl pkcs12 -in a.pfx -nokeys -out fullchain.pem -passin 'pass:GfosCn20!'
# privkey
openssl pkcs12 -in a.pfx -nocerts -nodes -out privkey.pem -passin 'pass:GfosCn20!'
```

## keytool

```sh
keytool -genkey -alias broker -keyalg RSA -keystore broker.ks
#导出经纪人的证书，以便可以与客户共享：
keytool -export -alias broker -keystore broker.ks -file broker_cert
#为客户端创建证书/密钥库：
keytool -genkey -alias client -keyalg RSA -keystore client.ks
#为客户端创建一个信任库，并导入代理的证书。这样可以确定客户“信任”经纪人：
keytool -import -alias broker -keystore client.ts -file broker_cert
```

## openssl ca

```sh
# https://www.cnblogs.com/leffss/p/14705551.html
openssl genrsa -out ssl.key 2048
# openssl rsa -in ssl.key -des3 -out encrypted.key # 密码
openssl req -new -key ssl.key -out ssl.csr

# 自签
openssl x509 -req -in ssl.csr -signkey ssl.key -out ssl.crt

# ca 签
# openssl genrsa -out sign.key 2048
# openssl req -new -key sign.key -out sign.csr
openssl x509 -req -in sign.csr -extensions v3_ca -signkey sign.key -out sign.crt
openssl x509 -req -in ssl.csr -extensions v3_usr -CA sign.crt -CAkey sign.key -CAcreateserial -out ssl.crt
```
