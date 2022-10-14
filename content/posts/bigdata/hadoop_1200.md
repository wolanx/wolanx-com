---
title: hadoop 1200
date: 2018-03-19
categories: [bigdata]
---

# 01.课程介绍，HDFS架构和原理，搭建CentOS开发环境

## 下载地址
```
centos http://www.centoscn.com/CentosSoft/
jdk1.7 http://www.oracle.com/technetwork/java/javase/downloads/jdk7-downloads-1880260.html
hadoop http://apache.fayea.com/hadoop/common/

修改eth0
cat /etc/sysconfig/network-scripts/ifcfg-eth0

DEVICE=eth0
TYPE=Ethernet
ONBOOT=yes
BOOTPROTO=static
IPADDR=192.168.1.101
NETMASK=255.255.255.0
GATEWAY=192.168.1.1

关闭iptables
service iptables stop
chkconfig iptables off

# selinux 关闭
/etc/selinux/config
SELINUX=disabled

配置dns
/etc/resolv.conf
nameserver 180.168.255.118

rm -f /etc/udev/rules.d/70-persistent-net.rules #mac地址conf

mount -t vboxsf BaiduShare /mnt/bdshare/
```

## jdk 安装
```

jdk 安装配置
rpm -ivh jdk-7u79-linux-x64.rpm
cd /usr/java/
vi ~/.bashrc
export JAVA_HOME=/usr/java/latest
export PATH=$PATH:$JAVA_HOME/bin
env | grep JAVA
reboot
env | grep JAVA
```

# 02.hdfs单机和集群的配置安装

## hadoop 下载安装
```
wget http://apache.fayea.com/hadoop/common/hadoop-2.5.2/hadoop-2.5.2.tar.gz
md5sum hadoop-2.6.0.tar.gz | tr "a-z" "A-Z"
tar -zxvf hadoop-2.5.2.tar.gz
ln -sf hadoop-2.5.2 hadoop #链接

vi ~/.bashrc
export JAVA_HOME=/usr/java/latest
export HADOOP_HOME=/bao/hadoop
export PATH=$PATH:$JAVA_HOME/bin:$HADOOP_HOME/bin:$HADOOP_HOME/sbin
```

## 无密码登录
```
ssh-keygen -t dsa -P '' -f ~/.ssh/id_dsa
cat ~/.ssh/id_dsa.pub >> ~/.ssh/authorized_keys
```

## 配置看官方文档

- [x] Documentation 2.5.2 [http://hadoop.apache.org/docs/r2.5.2](http://hadoop.apache.org/docs/r2.5.2)


### Single Node Setup
```
C:\Windows\System32\drivers\etc\hosts
vi /etc/hosts
192.168.1.201   hadoop1

vi core-site.xml # /bao/hadoop/etc/hadoop
<configuration>
        <property>
                <name>fs.default.name</name>
                <value>hdfs://hadoop1:9000</value>
        </property>
</configuration>

vi hdfs-site.xml # /bao/hadoop/etc/hadoop
<configuration>
    <property>
        <name>dfs.name.dir</name>
        <value>/hdata/namenode</value>
    </property>
    <property>
        <name>dfs.data.dir</name>
        <value>/hdata/datanode</value>
    </property>
    <property>
        <name>dfs.tmp.dir</name>
        <value>/hdata/tmp</value>
    </property>
    <property>
        <name>dfs.replication</name>
        <value>1</value><!-- 大约0  0:Requested replication 0 is less than the required minimum 1 -->
    </property>
</configuration>

vi slaves # /bao/hadoop/etc/hadoop
hadoop1
```

## 初始化 启动
```
hdfs namenode -format

start-dfs.sh
stop-dfs.sh

jps #看进程
netstat -anp | grep java
```

### log
```
cd /bao/hadoop/logs
tail -n50 -f hadoop-root-namenode-localhost.localdomain.log
```

### curd
```
hdfs dfs -put /bao/hadoop-2.5.2.tar.gz /
hdfs dfs -ls /
```

## 集群

### 复制一个hadoop2
```
hostnamectl set-hostname hadoop2

vi hdfs-site.xml # /bao/hadoop/etc/hadoop
<configuration>
    <property>
        <name>dfs.name.dir</name>
        <value>/hdata/namenode</value>
    </property>
    <property>
        <name>dfs.data.dir</name>
        <value>/hdata/datanode</value>
    </property>
    <property>
        <name>dfs.tmp.dir</name>
        <value>/hdata/tmp</value>
    </property>
    <property>
        <name>dfs.replication</name>
        <value>2</value><!-- 大约0  0:Requested replication 0 is less than the required minimum 1 -->
    </property>
</configuration>

vi slaves # /bao/hadoop/etc/hadoop
hadoop1
hadoop2
```

### 初始化启动
```
cd /hdata
rm -rf *

stop-dfs.sh
hdfs namenode -format
start-dfs.sh

# http://192.168.1.201:50070/dfshealth.html#tab-datanode
检查是不是有两个 Node
```

```
#hadoop checknative -a #检查
#warn

yum -y install  svn   ncurses-devel   gcc*
yum -y install lzo-devel zlib-devel autoconf    automake    libtool    cmake     openssl –devel

#安装 protobuf（不安装，编译将无法完成）
Hadoop使用protocol buffer进行通信，需要下载和安装protobhf-2.5.0.tar.gz
cd   protobuf - 2.5.0
./configure
make
make install
protoc –-version

cd /hadoop-2.5.2-src
mvn package -Pdist,native -DskipTests -Dtar

export HADOOP_MAPRED_HOME=$HADOOP_HOME
export HADOOP_COMMON_HOME=$HADOOP_HOME
export HADOOP_HDFS_HOME=$HADOOP_HOME
export YARN_HOME=$HADOOP_HOME
export HADOOP_COMMON_LIB_NATIVE_DIR="/app/hadoop/lib/native"
export HADOOP_OPTS="-Djava.library.path=/app/hadoop/lib/native"
```

# 03.hdfs应用-云存储系统1

## windows java
```
eclipse-jee-luna-R-win32-x86_64.zip
jdk-7u45-nb-7_4-windows-x64.exe

A:\eclipse\eclipse.ini
-vm
C:\Program Files\Java\jdk1.7.0_45\bin
```

## jetty
```
Help -> Eclipse Marketplace
Search jetty
Run-Jetty-Run install
```

## maven
```
File -> New -> Maven Project
maven-archetype-webapp

web -> Bulid Path -> Configure Bulid Path
Jave Bulid Path -> Soure -> 2个missing 的 Remove

web -> Source Foloer
    src/main/java
    src/main/test

web -> Bulid Path -> Configure Bulid Path
Jave Bulid Path -> Output folder -> target/classes * 3

Peferences -> jre -> Installed JREs -> Check version

web -> Bulid Path -> Configure Bulid Path
Libraries -> JRE -> Edit -> Workspace default JRE
```

# 06.hdfs应用-云存储系统4


./ffmpeg.exe -list_devices true -f dshow -i dummy

./ffmpeg.exe -f dshow -i video="screen-capture-recorder":audio="virtual-audio-capturer" ab.mp4
./ffmpeg.exe -f dshow -i video="screen-capture-recorder" yo.mp4
./ffmpeg.exe -f dshow -i audio="virtual-audio-capturer" yo.mp3


./ffmpeg.exe -f dshow -i video="screen-capture-recorder" -f dshow -i audio="virtual-audio-capturer" 222.avi



./ffmpeg.exe -list_devices true -f dshow -i test.mp4
./ffmpeg.exe -f x11grab -s 842x676 -r 50 -i :0.0+228,213 test.mp4
./ffmpeg.exe -vcodec mpeg4 -b 1000 -r 10 -g 300 test.avi
