---
title: graalvm
date: 2021-10-26T20:10:57+08:00
tags: [java]
---

# graalvm

```sh
wget --no-check-certificate 'https://github.com.cnpmjs.org/graalvm/graalvm-ce-builds/releases/download/vm-21.3.0/graalvm-ce-java11-linux-amd64-21.3.0.tar.gz'
mkdir /etc/graalvm
tar -zxvf graalvm-ce-java11-linux-amd64-21.3.0.tar.gz -C /etc/graalvm
export PATH=$PATH:/etc/graalvm/graalvm-ce-java11-21.3.0/bin
# docker pull docker.io/springci/graalvm-ce:java11-0.11.x

# yum install gcc glibc-devel zlib-devel
gu install native-image
```

```java
public class HelloWorld {
  public static void main(String[] args) {
    System.out.println("Hello, World!");
  }
}
// javac HelloWorld.java
// native-image -jar HelloWorld
// ./HelloWorld
```

# quarkus
./gradlew build -Dquarkus.package.type=native -Dquarkus.native.container-build=true -Dquarkus.native.native-image-xmx=8g
