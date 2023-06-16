---
title: python i18n 多语言
date: 2021-06-17T17:01:51+08:00
tags: [python]
---


mkdir locales
pybabel extract -o locales/base.pot .

pybabel init -i locales/base.pot -D base -d locales --locale zh_CN

pybabel update -i locales/base.pot -D base -d locales --locale zh_CN

pybabel compile -D base -d locales


## mkdir locales
```makefile
default:
	cat Makefile

a:
	pybabel extract -o ./base.pot ../temp

init:
	pybabel init -i ./base.pot -D base -d . --locale en_US
	pybabel init -i ./base.pot -D base -d . --locale zh_CN

b:
	pybabel update -i ./base.pot -D base -d . --locale en_US
	pybabel update -i ./base.pot -D base -d . --locale zh_CN

c:
	pybabel compile -D base -d .

```
