---
title: php C扩展开发
date: 2018-03-22 16:39:22
tags:
  - php
---

# doc

- [x] function() [http://www.bo56.com/php7扩展开发之hello-word](http://www.bo56.com/php7扩展开发之hello-word)
- [x] function(...arg) [http://www.bo56.com/php7扩展开发之传参与返回值](http://www.bo56.com/php7扩展开发之传参与返回值)
- [x] class() [http://www.bo56.com/白话php7扩展开发之创建对象](http://www.bo56.com/白话php7扩展开发之创建对象)

# function()

## 1.生成代码

```
cd php_src/ext/
./ext_skel --extname=say

cd ..
vi ext/say/config.m4
./buildconf
./configure --[with|enable]-say
make
./sapi/cli/php -f ext/say/say.php
vi ext/say/say.c
make
```

## 2.修改config.m4配置文件

```
dnl If your extension references something external, use with:

dnl PHP_ARG_WITH(say, for say support,
dnl Make sure that the comment is aligned:
dnl [  --with-say             Include say support])

dnl Otherwise use enable:

PHP_ARG_ENABLE(say, whether to enable say support,
Make sure that the comment is aligned:
[  --enable-say           Enable say support])
```

## 3.代码实现

```
修改say.c文件。实现say方法。
找到PHP_FUNCTION(confirm_say_compiled)，在其上面增加如下代码：
PHP_FUNCTION(say)
{
    zend_string *strg;
    strg = strpprintf(0, "hello word");
    RETURN_STR(strg);
}

找到 PHP_FE(confirm_say_compiled, 在上面增加如下代码：
PHP_FE(say, NULL)

修改后的代码如下：
const zend_function_entry say_functions[] = {
	PHP_FE(say, NULL)
	PHP_FE(confirm_say_compiled,	NULL)		/* For testing, remove later. */
	PHP_FE_END	/* Must be the last line in say_functions[] */
};
```

## 4.编译安装

```
编译扩展的步骤如下：
phpize
./configure
make && make install

修改php.ini文件，增加如下代码：
[say]
extension = say.so

然后执行，php -m 命令。在输出的内容中，你会看到say字样。
```

# function(...arg)

## test.php

```php
<?php
function default_value ($type, $value = null) {
    if ($type == "int") {
        return $value ?? 0;
    } else if ($type == "bool") {
        return $value ?? false;
    } else if ($type == "str") {
        return is_null($value) ? "" : $value;
    }
    return null;
}

var_dump(default_value("int"));
var_dump(default_value("int", 1));
var_dump(default_value("bool"));
var_dump(default_value("bool", true));
var_dump(default_value("str"));
var_dump(default_value("str", "a"));
var_dump(default_value("array"));
?>
```

## say.c

```c
PHP_FUNCTION(default_value)
{
    zend_string     *type;    
    zval            *value = NULL;
 
#ifndef FAST_ZPP
    /* Get function parameters and do error-checking. */
    if (zend_parse_parameters(ZEND_NUM_ARGS(), "S|z", &type, &value) == FAILURE) {
        return;
    }    
#else
    ZEND_PARSE_PARAMETERS_START(1, 2)
        Z_PARAM_STR(type)
        Z_PARAM_OPTIONAL
        Z_PARAM_ZVAL_EX(value, 0, 1)
    ZEND_PARSE_PARAMETERS_END();
#endif
     
    if (ZSTR_LEN(type) == 3 && strncmp(ZSTR_VAL(type), "int", 3) == 0 && value == NULL) {
        RETURN_LONG(0);
    } else if (ZSTR_LEN(type) == 3 && strncmp(ZSTR_VAL(type), "int", 3) == 0 && value != NULL) {
        RETURN_ZVAL(value, 0, 1); 
    } else if (ZSTR_LEN(type) == 4 && strncmp(ZSTR_VAL(type), "bool", 4) == 0 && value == NULL) {
        RETURN_FALSE;
    } else if (ZSTR_LEN(type) == 4 && strncmp(ZSTR_VAL(type), "bool", 4) == 0 && value != NULL) {
        RETURN_ZVAL(value, 0, 1); 
    } else if (ZSTR_LEN(type) == 3 && strncmp(ZSTR_VAL(type), "str", 3) == 0 && value == NULL) {
        RETURN_EMPTY_STRING();
    } else if (ZSTR_LEN(type) == 3 && strncmp(ZSTR_VAL(type), "str", 3) == 0 && value != NULL) {
        RETURN_ZVAL(value, 0, 1); 
    } 
    RETURN_NULL();
}
```

`PHP_FE` add `PHP_FE(default_value, NULL)`
