---
title: c base
date: 2015-02-13T20:43:41+08:00
tags: [clang]
---

# 数据类型

## 常量

```c
//习惯大写
#define MAX 10
#define STING "hello world\n"
//习惯小写
const int a=10;
const char *str = "hello c";
```

## 字符串

```c
printf("%p\n",&amp;a);//显示内存地址
printf("%c\n",&amp;a);//字符
printf("%o\n",&amp;a);//八进制
printf("%x\n",&amp;a);//十六进制abcdef
printf("%X\n",&amp;a);//十六进制ABCDEF

char c = 'a';
sizeof(c);//大小1
char c = '\a';//报警
char c = '\b';//退格
char c = '\n';//换行
char c = '\r';//回车
```

## 浮点

```c
float a;//sizeof=4 2.000000
double b;//sizeof=4
long double c;//sizeof=8
```

## 类型限定

```c
const a;
volatile int a;//a=a+1;a=a+2;a=a+3; 不合并成 a=a+6 变量可能在cpu指令意外的地方改变，编译器不要去优化
register int a;//变量不在内存中，在寄存器中
```

# method

## system

```c
#include &lt;stdlib.h&gt;

int main(){
 system("ls -l");
 return 0;
}
```
