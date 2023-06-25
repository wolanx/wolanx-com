---
title: sar 性能指标
date: 2017-12-13
tags:
  - linux
---

# sar

> 性能指标


怀疑CPU

- [x] sar -u
- [x] sar -q

怀疑内存

- [ ] sar -B
- [ ] sar -r
- [ ] sar -W

怀疑I/O

- [x] sar -b
- [x] sar -u
- [ ] sar -d

## install

`sudo apt-get -y install sysstat`

## sar -u 1 5

> 输出CPU使用情况的统计信息

```text
Linux 4.4.0-1022-aws (aws-sandbox)  12/28/2017  _x86_64_    (4 CPU)

07:15:23 AM     CPU     %user     %nice   %system   %iowait    %steal     %idle
07:15:24 AM     all     46.95      0.00      3.05      0.00      0.00     50.00
07:15:25 AM     all     15.86      0.00      2.30      0.00      0.00     81.84
07:15:26 AM     all     10.66      0.00      0.51      0.00      0.00     88.83
07:15:27 AM     all     20.67      0.00      0.52      0.00      0.00     78.81
07:15:28 AM     all     12.12      0.00      0.00      0.00      0.25     87.63
Average:        all     21.25      0.00      1.27      0.00      0.05     77.42
```

```text
CPU      all 表示统计信息为所有 CPU 的平均值
%user    显示在用户级别(application)运行使用 CPU 总时间的百分比
%nice    显示在用户级别，用于nice操作，所占用 CPU 总时间的百分比
%system  在核心级别(kernel)运行所使用 CPU 总时间的百分比
%iowait  显示用于等待I/O操作占用 CPU 总时间的百分比
%steal   管理程序(hypervisor)为另一个虚拟进程提供服务而等待虚拟 CPU 的百分比
%idle    显示 CPU 空闲时间占用 CPU 总时间的百分比
```

```text
若 %iowait 的值过高，表示硬盘存在I/O瓶颈
若 %idle 的值高但系统响应慢时，有可能是 CPU 等待分配内存，此时应加大内存容量
若 %idle 的值持续低于 10，则系统的 CPU 处理能力相对较低，表明系统中最需要解决的资源是 CPU
```

## sar –q 1 5

> 查看平均负荷

```text
Linux 4.4.0-1022-aws (aws-sandbox)  12/28/2017  _x86_64_    (4 CPU)

07:26:52 AM   runq-sz  plist-sz   ldavg-1   ldavg-5  ldavg-15   blocked
07:26:53 AM         6      2121      2.00      1.97      1.56         0
07:26:54 AM         0      2117      2.48      2.07      1.60         0
07:26:55 AM         0      2117      2.48      2.07      1.60         0
07:26:56 AM         1      2117      2.48      2.07      1.60         0
07:26:57 AM         3      2117      2.48      2.07      1.60         0
Average:            2      2118      2.38      2.05      1.59         0
```

```text
runq-sz     运行队列的长度（等待运行的进程数） Run queue length (number of tasks waiting for run time)
plist-sz    进程列表中进程（processes）和线程（threads）的数量 Number of tasks in the task list.
ldavg-1     最后1分钟的系统平均负载（System load average）
ldavg-5     过去5分钟的系统平均负载
ldavg-15    过去15分钟的系统平均负载
```

## sar -r 1 5

> 内存和交换空间监控

```text
Linux 4.4.0-1022-aws (aws-sandbox)  12/28/2017  _x86_64_    (4 CPU)

07:31:24 AM kbmemfree kbmemused  %memused kbbuffers  kbcached  kbcommit   %commit  kbactive   kbinact   kbdirty
07:31:25 AM    604560  15826960     96.32   2490348   2803236  25069280    152.57  11571660   2561176       268
07:31:26 AM    604440  15827080     96.32   2490348   2803236  25069280    152.57  11571984   2561176       268
07:31:27 AM    604440  15827080     96.32   2490348   2803236  25069280    152.57  11571984   2561176       268
07:31:28 AM    604440  15827080     96.32   2490348   2803236  25069280    152.57  11572008   2561176       268
07:31:29 AM    604316  15827204     96.32   2490348   2803236  25069280    152.57  11572308   2561176       268
Average:       604439  15827081     96.32   2490348   2803236  25069280    152.57  11571989   2561176       268
```

```text
kbmemfree           这个值和free命令中的free值基本一致,所以它不包括buffer和cache的空间
kbmemused           这个值和free命令中的used值基本一致,所以它包括buffer和cache的空间
%memused            这个值是kbmemused和内存总量(不包括swap)的一个百分比
kbbuffers和kbcached 这两个值就是free命令中的buffer和cache
kbcommit            保证当前系统所需要的内存,即为了确保不溢出而需要的内存(RAM+swap)
%commit             这个值是kbcommit与内存总量(包括swap)的一个百分比
```

## sar -b 1 5

> 显示I/O和传送速率的统计信息

```text
Linux 4.4.0-1022-aws (aws-sandbox)  12/28/2017  _x86_64_    (4 CPU)

07:21:50 AM       tps      rtps      wtps   bread/s   bwrtn/s
07:21:51 AM      4.00      0.00      4.00      0.00     72.00
07:21:52 AM      0.00      0.00      0.00      0.00      0.00
07:21:53 AM      7.00      0.00      7.00      0.00    320.00
07:21:54 AM      0.00      0.00      0.00      0.00      0.00
07:21:55 AM      1.00      0.00      1.00      0.00     32.00
Average:         2.40      0.00      2.40      0.00     84.63
```

```text
tps     每秒钟物理设备的 I/O 传输总量
rtps    每秒钟从物理设备读入的数据总量
wtps    每秒钟向物理设备写入的数据总量
bread/s 每秒钟从物理设备读入的数据量，单位为 块/s
bwrtn/s 每秒钟向物理设备写入的数据量，单位为 块/s
```
