---
title: gradle 配置
date: 2019-06-18T20:10:57+08:00
categories: [java]
---

# install

gradle home: /usr/local/Cellar/gradle/5.4.1/libexec

```sh
wget https://services.gradle.org/distributions/gradle-5.4.1-bin.zip
mkdir /opt/gradle
unzip -d /opt/gradle gradle-5.4.1-bin.zip

# vi
export PATH=$PATH:/opt/gradle/gradle-5.4.1/bin
```

## task run

```sh
GRADLE_OPTS: "-Dorg.gradle.daemon=false"
./gradlew
./gradlew :base:bundleDebug
./gradlew -p egids-webapp jibDockerBuild
```

## gradle

### task +参数

```text
def versionName = project.hasProperty('vest') ? project.property('vest') : "123"

task myTask {
    println "config myTask${versionName} hello"
}

./gradlew :myTask -Pvest=3333
```

### demo

build.gradle

```
plugins {
    id 'java'
}

group 'com.zx5435'
version '1.0-SNAPSHOT'
sourceCompatibility = 1.8

jar {
    from {
        configurations.compile.collect { it.isDirectory() ? it : zipTree(it) }
    }
    manifest {
        attributes 'Main-Class': 'Hello'
    }
}

repositories {
    mavenLocal()
    maven { url "https://maven.aliyun.com/nexus/content/groups/public" }
    mavenCentral()
}

dependencies {
    implementation 'org.springframework.boot:spring-boot-starter-json:2.6.4'
    implementation 'org.springframework.boot:spring-boot-starter-logging:2.6.4'

    // lombok
    compileOnly 'org.projectlombok:lombok:1.18.22'
    annotationProcessor 'org.projectlombok:lombok:1.18.22'

    compile "cn.hutool:hutool-all:$ver"
    testCompile group: 'junit', name: 'junit', version: '4.12'
}

ext {
    ver = '4.3.1'
}
```

settings.gradle

```
rootProject.name = 'gradle-test'
```

## gradle springcloud

## parent

```
plugins {
    id 'org.springframework.boot' version '2.1.4.RELEASE' // 重点
    id 'java'
}

allprojects {
    apply plugin: 'java'
    apply plugin: 'io.spring.dependency-management'
    apply plugin: 'org.springframework.boot'

    group = 'com.zx5435'
    version = '1.0'
    sourceCompatibility = '1.8'

    repositories {
        mavenCentral()
        mavenLocal()
    }
}

subprojects {
    dependencyManagement {
        imports {
            mavenBom 'org.springframework.cloud:spring-cloud-dependencies:Greenwich.RELEASE' // 重点
        }
    }

    dependencies {
        compile "cn.hutool:hutool-all:4.3.1"
        testCompile 'junit:junit:4.11'
//        testCompile 'org.springframework.boot:spring-boot-starter-test:2.1.4.RELEASE'
    }
}
```

## sub

```
dependencies {
//    compile 'org.springframework.cloud:spring-cloud-starter-netflix-eureka-server'
    compile 'org.springframework.boot:spring-boot-starter-web'
}
```
