---
title: php composer配置
date: 2018-03-22 16:39:22
tags:
  - php
---

# composer

你必须知道的 17 个 Composer 最佳实践 https://juejin.im/entry/5a72d506518825734501dd6d

# 代理

composer config -g repo.packagist composer https://packagist.phpcomposer.com

## 简化 bower

`composer.json` && `composer fxp`

```json
{
  "scripts": {
    "fxp": [
      "composer global require 'fxp/composer-asset-plugin'"
    ]
  },
  "config": {
    "process-timeout": 1800,
    "fxp-asset": {
      "enabled": true,
      "installer-paths": {
        "npm-asset-library": "vendor/npm",
        "bower-asset-library": "vendor/bower"
      }
    }
  }
}
```

# 装单个

```sh
composer update nothing

composer require league/oauth2-client --no-update
composer update league/oauth2-client

php composer.phar require --dev --prefer-dist yiisoft/yii2-gii
```

# autoload 加速

composer dump-autoload --classmap-authoritative
