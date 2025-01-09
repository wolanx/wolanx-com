---
title: linux常用命令
date: 2015-12-13
tags:
  - linux
---

# doc

- [x] linux 命令源码 c http://git.savannah.gnu.org/cgit/coreutils.git/tree/src
- [x] Linux常用命令 http://www.kuqin.com/shuoit/20160805/352716.html
- [ ] Linux命令大全 http://man.linuxde.net/par/2
- [ ] 云架构师进阶攻略 - 刘超 通俗云计算 https://mp.weixin.qq.com/s/tBQ5tjSqk94_AtrgYgO0xA
    - 图说Linux进程

# 类似man 查看命令用法

curl cht.sh/ls

# 用户权限

```sh
adduser www
passwd www # 修改密码
#修改 /etc/sudoers 文件，找到下面一行，在root下面添加一行，如下所示：
## Allow root to run any commands anywhere
root    ALL=(ALL)     ALL
www   ALL=(ALL)     ALL
#修改完毕，现在可以用www帐号登录，然后用命令 sudo – ，即可获得root权限进行操作
```

# some

### ip 查看

```sh
netstat -nltp
iptables -L
lsof -i:80
lsof -n -P -i TCP -s TCP:LISTEN
```

## netstat

```
yum install -y net-tools
netstat -nltp # 查看 ip

netstat -nap | grep 进程pid
netstat -nap | grep 端口号
```

# chkconfig

chkconfig --list #列出所有的系统服务
chkconfig --list mysqld #列出mysqld服务设置情况
chkconfig --add httpd #增加httpd服务
chkconfig --del httpd #删除httpd服务 /etc/rc[0-6].d删除
chkconfig --level httpd 2345 on #设置httpd在运行级别为2、3、4、5的情况下都是on（开启）的状态
chkconfig --level 35 mysqld on #设定mysqld在等级3和5为开机运行服务，--level 35表示操作只在等级3和5执行，on表示启动，off表示关闭
chkconfig mysqld on #设定mysqld在各等级为on，“各等级”包括2、3、4、5等级

### wget

```sh
#1：下载单个文件到当前目录下，也可以-P指定下载目录
wget http://nginx.org/download/nginx-1.8.0.tar.gz
#2：对于网络不稳定的用户可以使用-c和--tries参数，保证下载完成
wget --tries=20 -c http://nginx.org/download/nginx-1.8.0.tar.gz
#3：下载大的文件时，我们可以放到后台去下载，这时会生成wget-log文件来保存下载进度
wget -b http://nginx.org/download/nginx-1.8.0.tar.gz
#4：可以利用—spider参数判断网址是否有效
wget --spider http://nginx.org/download/nginx-1.8.0.tar.gz
#5：自动从多个链接下载文件
cat url_list.txt   #先创建一个URL文件
http://nginx.org/download/nginx-1.8.0.tar.gz
http://nginx.org/download/nginx-1.6.3.tar.gz
wget -i url_list.txt
#6：限制下载速度
wget --limit-rate=1m http://nginx.org/download/nginx-1.8.0.tar.gz
#7：登陆ftp下载文件
wget --ftp-user=user --ftp-password=pass ftp://ip/filename
```

# find xargs

find . -name "*.py" | xargs -I name sh -c 'echo name ; cat name'
find . -name "*.py" | xargs -I name sh -c 'echo "\"\"\"@copyright {name}\"\"\"" ; cat name ; echo -e "\n\n\n\n"' > ~
/Desktop/a.txt
find . -name "*.js" | xargs -I name sh -c 'echo "\"\"\"@copyright {name}\"\"\"" ; cat name ; echo -e "\n\n\n\n"' > ~
/Desktop/b.txt

## iftop 图看 net-io

```sh
# https://www.vpser.net/manage/iftop.html
yum install -y iftop

# 5m 为背景长度
iftop -m 5m
# then p S o
```

```text
TX:     发送流量
RX:     接收流量
TOTAL:  总流量
Cumm:   运行iftop到目前时间的总流量
peak:   流量峰值
rates:  分别表示过去 2s 10s 40s 的平均流量

-P使host信息及端口信息默认就都显示;
-m设置界面最上边的刻度的最大值，刻度分五个大段显示，例：#
Host display:                          General:
 n - toggle DNS host resolution         P - pause display
 s - toggle show source host            h - toggle this help display
 d - toggle show destination host	b - toggle bar graph display
 t - cycle line display mode            B - cycle bar graph average
                                        T - toggle cumulative line totals
Port display:                           j/k - scroll display
 N - toggle service resolution          f - edit filter code
 S - toggle show source port            l - set screen filter
 D - toggle show destination port	L - lin/log scales
 p - toggle port display                ! - shell command
                                        q - quit
Sorting:
 1/2/3 - sort by 1st/2nd/3rd column
 < - sort by source name
 > - sort by dest name
 o - freeze current order
```

## iotop http://man.linuxde.net/iotop

```
yum install -y iotop
iotop -d 5

常用快捷键：
左右箭头：改变排序方式，默认是按IO排序。
r：改变排序顺序。
o：只显示有IO输出的进程。
p：进程/线程的显示方式的切换。
a：显示累积使用量。
```

## firewall

```sh
firewall-cmd --state
systemctl disable firewalld.service # 在开机时禁用一个服务
```

## iostat

```
yum install -y sysstat

iostat -d -k 1 10         #查看TPS和吞吐量信息(磁盘读写速度单位为KB)
iostat -d -m 2            #查看TPS和吞吐量信息(磁盘读写速度单位为MB)
iostat -d -x -m 1 10      #查看设备使用率（%util）

参数
-d 表示，显示设备（磁盘）使用状态；-k某些使用block为单位的列强制使用Kilobytes为单位；2表示，数据显示每隔2秒刷新一次。
-x，该选项将用于显示和io相关的扩展数据。

rrqm/s：每秒这个设备相关的读取请求有多少被Merge了（当系统调用需要读取数据的时候，VFS将请求发到各个FS，如果FS发现不同的读取请求读取的是相同Block的数据，FS会将这个请求合并Merge）；wrqm/s：每秒这个设备相关的写入请求有多少被Merge了。
rsec/s：每秒读取的扇区数；
wsec/：每秒写入的扇区数。
rKB/s：The number of read requests that were issued to the device per second；
wKB/s：The number of write requests that were issued to the device per second；
avgrq-sz 平均请求扇区的大小
avgqu-sz 是平均请求队列的长度。毫无疑问，队列长度越短越好。    
await：  每一个IO请求的处理的平均时间（单位是微秒毫秒）。这里可以理解为IO的响应时间，一般地系统IO响应时间应该低于5ms，如果大于10ms就比较大了。
         这个时间包括了队列时间和服务时间，也就是说，一般情况下，await大于svctm，它们的差值越小，则说明队列时间越短，反之差值越大，队列时间越长，说明系统出了问题。
svctm    表示平均每次设备I/O操作的服务时间（以毫秒为单位）。如果svctm的值与await很接近，表示几乎没有I/O等待，磁盘性能很好，如果await的值远高于svctm的值，则表示I/O队列等待太长，         系统上运行的应用程序将变慢。
%util： 在统计时间内所有处理IO时间，除以总共统计时间。例如，如果统计间隔1秒，该设备有0.8秒在处理IO，而0.2秒闲置，那么该设备的%util = 0.8/1 = 80%，所以该参数暗示了设备的繁忙程度
。一般地，如果该参数是100%表示设备已经接近满负荷运行了（当然如果是多磁盘，即使%util是100%，因为磁盘的并发能力，所以磁盘使用未必就到了瓶颈）。
```

## sed

> http://man.linuxde.net/sed

```shell
sed -i 's/book/books/g' file

# 删除#开头行
sed -i '/^#/'d filebeat.yml
# 删除空白行
sed -i /^[[:space:]]*$/d filebeat.yml
```

## cat

```sh
cat <<EOF
cat > filename # 敲完内容，ctrl+d
cat > filename <<EOF
敲完内容
EOF
```

## tee

> 读取标准输入的数据，并将其内容输出成文件

```sh
tee /etc/docker/daemon.json <<-'EOF'
{
  "registry-mirrors": ["https://cmf3ratl.mirror.aliyuncs.com"]
}
EOF

[root@localhost ~]# who | tee who.out
root     pts/0        2009-02-17 07:47 (123.123.123.123)
[root@localhost ~]# cat who.out
root     pts/0        2009-02-17 07:47 (123.123.123.123)
[root@localhost ~]# pwd | tee -a who.out
/root
[root@localhost ~]# cat who.out
root     pts/0        2009-02-17 07:47 (123.123.123.123)
/root
[root@localhost ~]#
```

### rename

```shell
rename 's/\.jpeg$/\.jpg/' *.jpeg
rename 's/_\w*/_/' *.mp3
```

### split文件分割

```shell
split -l 2000 data.mt -d seofile_
curl -H 'Content-Type:text/plain' --data-binary @seofile_00 "http://data.zz.baidu.com/urls?site=www.app-echo.com&token=3iyzwDoYB6IQAMKL"

//每3行拆分成一个文件，拆分后的文件名以name开头，以数字作为后缀后缀长度为1
split -l 3 test -d -a 1 name

//每三个字节拆分成一个文件，默认不加单位就是字节，也可以带单位比如KB,MB等
split -b 3 test -d -a 1 new
```

### redis key分布

```shell
# 1.sh
for i in `seq 1 100`;do
redis-cli -h 230f029eefb64e44.m.cnsha.kvstore.aliyuncs.com -a zc1BK5JM randomkey
done

./1.sh > r.keys

cat r.keys | awk -F ':' '{print $1}' | sort | uniq -c | sort -r -n
```

### text len 排序

awk '{ print length, $0}' bj.conf | sort -n | sed 's/.* //'

### grep

```sh
-i　　忽略大小写
-n　　显示行号
--color 　　高亮关键字，centos7默认已经高亮
-c　　统计符合条件的行数
-o　　只打印关键字，每个被匹配的关键字单独显示一行
-B 　　同时显示之前的行，后面必须有数字，如 -B2
-A 　　同时显示之后的行
-w　　只匹配独立单词，也就是精确匹配
-v　　反向查找
-e　　同时匹配多个目标
-q　　静默模式，只关心有没有匹配到，不关心内容
-E　　可以使用扩展正则，，相当于egrep
-P　　使用兼容perl的正则
fgrep： 不支持正则表达式，只能匹配写死的字符串，但是速度奇快，效率高，fastgrep

tail -f api::header-debug-`date +"%w"`.log | grep ' {.*}' -o --line-buffered | jq

```

### 进程

```shell
#查看端口情况
netstat -apn | grep 9000 # ss better
ps -aux | grep php
```

### scp

```shell
#文件
scp goaccess.conf 139:196:14:10:/usr/local/etc/goaccess.conf
#文件夹
scp -qr -P 20248 name1 root@172.16.3.121:/data/name2/
```

### 文件大小

du -sh
du -sh *

### 文件个数

ls -l | wc -l

### 解压

#### zip

```shell
zip -r a.zip dirname
zip a.zip tests/* -x tests/ln.log #排除一个文件
zip -m a.zip test.md #向压缩文件中a.zip中添加test.md文件
```

#### unzip

```shell
unzip -r a.zip *
unzip -n test.zip -d /tmp #在指定目录/tmp解压缩,如已存在,-n 不覆盖 ~ -o 覆盖
```

#### tar

```shell
tar -zcvf filename.tar.gz folderName #压缩
tar -zcvf FileName.tar.gz DirName --exclude DirName/DirExcName #排除
tar -zcvf FileName.tar.gz DirName --exclude DirName/Dir1Name --exclude DirName/Dir2Name #多个排除

tar -zxvf filename.tar.gz -C /pcmoto/club/ #解压
tar -zxvf filename.tar.gz -C .
```

### seq

seq -f "%04g" 5 4 1000 | xargs -n 15

### completion

yum -y install bash-completion
iot-echo completion bash > /etc/bash_completion.d/iot-echo.bash
source /etc/bash_completion.d/iot-echo.bash

### cpu

```shell
查看各cpu状况，top 然后按1

查看物理CPU的个数
#cat /proc/cpuinfo |grep &quot;physical id&quot;|sort |uniq|wc -l

查看逻辑CPU的个数
#cat /proc/cpuinfo |grep &quot;processor&quot;|wc -l

查看CPU是几核
#cat /proc/cpuinfo |grep &quot;cores&quot;|uniq

查看CPU的主频
#cat /proc/cpuinfo |grep MHz|uniq

### uname -a
Linux euis1 2.6.9-55.ELsmp #1 SMP Fri Apr 20 17:03:35 EDT 2007 i686 i686 i386 GNU/Linux
(查看当前操作系统内核信息)

### cat /etc/issue | grep Linux
Red Hat Enterprise Linux AS release 4 (Nahant Update 5)
(查看当前操作系统发行版信息)

### cat /proc/cpuinfo | grep name | cut -f2 -d: | uniq -c
      8  Intel(R) Xeon(R) CPU            E5410   @ 2.33GHz
(看到有8个逻辑CPU, 也知道了CPU型号)

### cat /proc/cpuinfo | grep physical | uniq -c
      4 physical id      : 0
      4 physical id      : 1
(说明实际上是两颗4核的CPU)

### getconf LONG_BIT
32
(说明当前CPU运行在32bit模式下, 但不代表CPU不支持64bit)

### cat /proc/cpuinfo | grep flags | grep &#39; lm &#39; | wc -l
8
(结果大于0, 说明支持64bit计算. lm指long mode, 支持lm则是64bit)

如何获得CPU的详细信息：
linux命令：cat /proc/cpuinfo
用命令判断几个物理CPU，几个核等：
逻辑CPU个数：
### cat /proc/cpuinfo | grep &quot;processor&quot; | wc -l
物理CPU个数：
### cat /proc/cpuinfo | grep &quot;physical id&quot; | sort | uniq | wc -l
每个物理CPU中Core的个数：
### cat /proc/cpuinfo | grep &quot;cpu cores&quot; | wc -l
是否为超线程？
如果有两个逻辑CPU具有相同的”core id”，那么超线程是打开的。
每个物理CPU中逻辑CPU(可能是core, threads或both)的个数：
### cat /proc/cpuinfo | grep &quot;siblings&quot;
```

# column

```shell
cat  $(find . -name 310.html) | column -s',' -t

# 解决不对齐
cat  $(find . -name 310.html) | column -t -s $'\t'
```

# hostname

```shell
hostname m201
hostnamectl set-hostname m201
cat /proc/sys/kernel/hostname
```

# tcpdump

- Tcpdump 看这一篇就够了 https://www.jianshu.com/p/e3292f4dcc99

```shell
# 端口
tcpdump -i eth0 port 61617 -w ~/tcpdump_61617.pcap

sudo tcpdump 'tcp port 80 and (((ip[2:2] - ((ip[0]&0xf)<<2)) - ((tcp[12]&0xf0)>>2)) != 0)' -A -nn
所以常用的选项也就这几个：
tcpdump -D
tcpdump -c num -i int -nn -XX -vvv
```
