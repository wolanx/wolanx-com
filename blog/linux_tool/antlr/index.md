---
title: antlr4 ast
date: 2021-06-29
tags:
  - antlr
---

# doc

- https://github.com/antlr/antlr4/blob/master/doc/index.md
- ANTLR 4简明教程 https://wizardforcel.gitbooks.io/antlr4-short-course/content/getting-started.html
- 用 ANTLR4 和 python 十多行代码写一个计算器 https://blog.keyi-li.com/2020/04/16/ANTRL4-Python-Calculator/
- ANTLR巨型教程 https://blog.csdn.net/dnc8371/article/details/106812555
- lang demo https://github.com/antlr/grammars-v4

# install

cd ~/.jdks
curl -O https://www.antlr.org/download/antlr-4.9.2-complete.jar

cat antlr

```shell
#!/bin/sh
java -jar ~/.jdks/antlr-4.9.2-complete.jar $*
```

cat compile

```shell
#!/bin/sh
javac -cp antlr-4.9.2-complete.jar $*
```

cat grun

```shell
#!/bin/sh
java -cp .:$PWD/antlr-4.9.2-complete.jar org.antlr.v4.gui.TestRig $*
```

# run

./antlr myhello/Hello.g -o myhello-out
./compile myhello-out/*.java
./grun myhello-out/Hello s -tokens

antlr -Dlanguage=Python3 Calculantlr.g4 -visitor -o dist_Calculantlr
antlr -Dlanguage=Python3 Hello.g -visitor -o dist_Hello
antlr -Dlanguage=Python3 PiiCalc.g4 -visitor -o PiiCalc

# run go

./antlr -Dlanguage=Go MyGrammar.g
