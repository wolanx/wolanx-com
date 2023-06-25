---
title: codeception测试
date: 2017-09-11
tags:
  - php
---

# doc

- [x] 单元测试 -
  创建测试用例 [http://www.kkh86.com/it/codeception/guide-unit-test-create.html](http://www.kkh86.com/it/codeception/guide-unit-test-create.html)

## install

```text
php codecept.phar bootstrap --namespace project1_tests
php codecept.phar bootstrap
```

## /qr/tests/_bootstrap.php

```text
require(__DIR__ . '../../aaaa/phpqrcode.php');
```

## /qr/tests/unit.suite.yml

```text
class_name: UnitTester
coverage:
    enabled: true
    white_list:
        include:
            - ../aaaa/*
        exclude:
            - ../tests/*
modules:
    enabled:
        - Asserts
        - \project1_tests\Helper\Unit
```

## run

```text
php codecept.phar generate:test unit HelloWorld
php codecept.phar run unit HelloWorldTest
php codecept.phar run unit --coverage --coverage-html
```
