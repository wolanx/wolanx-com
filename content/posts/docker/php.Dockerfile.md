---
title: php Dockerfile
date: 2018-03-22
categories:
  - docker
tags:
---

# 2019.04.04
```sh
FROM php:7.1.11-fpm-alpine

RUN apk add --no-cache freetype libpng libjpeg-turbo freetype-dev libpng-dev libjpeg-turbo-dev \
    && apk add --no-cache --virtual .build-deps autoconf g++ libssh2 openssl openssl-dev make pcre-dev tree curl \
    && apk add --no-cache postgresql-dev \
    && docker-php-ext-configure gd \
        --with-gd \
        --with-freetype-dir=/usr/include/ \
        --with-png-dir=/usr/include/ \
        --with-jpeg-dir=/usr/include/ \
    && pecl install mongodb-1.5.2 redis apcu xdebug \
    && docker-php-ext-enable mongodb redis apcu xdebug \
    && docker-php-ext-install gd pdo_mysql opcache bcmath pgsql pdo_pgsql zip sockets \
    && apk del .build-deps \
    && pecl clear-cache \
    && docker-php-source delete

RUN curl https://getcomposer.org/composer.phar -o /usr/local/bin/composer \
    && chmod +x /usr/local/bin/composer \
    && mkdir -p /var/runtime && chmod -R 777 /var/runtime \
    && alias ll='ls -l'

# COPY __cicd__/php/php.ini /usr/local/etc/php/
# COPY __cicd__/php/www.conf /usr/local/etc/php-fpm.d/
# docker build -f Dockerfile.php -t zx5435/php:7.1.11 .
```

# 2019.03.07 error
```text
librabbitmq
pecl install amqp
composer config -g repo.packagist composer https://packagist.phpcomposer.com
```

# 2018.10.09 bitdata
```sh
FROM php:7.1.10-fpm-alpine

RUN apk add --no-cache freetype libpng libjpeg-turbo freetype-dev libpng-dev libjpeg-turbo-dev \
    && apk add --no-cache --virtual .build-deps autoconf g++ libssh2 openssl openssl-dev make pcre-dev \
    && apk add --no-cache postgresql-dev \
    && docker-php-ext-configure gd \
        --with-gd \
        --with-freetype-dir=/usr/include/ \
        --with-png-dir=/usr/include/ \
        --with-jpeg-dir=/usr/include/ \
    && pecl install mongodb-1.5.2 redis apcu xdebug \
    && docker-php-ext-enable mongodb redis apcu xdebug \
    && docker-php-ext-install gd pdo_mysql opcache bcmath pgsql pdo_pgsql zip \
    && apk del .build-deps \
    && pecl clear-cache \
    && docker-php-source delete

RUN curl https://getcomposer.org/composer.phar -o /usr/local/bin/composer \
    && chmod +x /usr/local/bin/composer \
    && mkdir -p /var/runtime && chmod -R 777 /var/runtime

# COPY __cicd__/php/php.ini /usr/local/etc/php/
# COPY __cicd__/php/www.conf /usr/local/etc/php-fpm.d/
# docker build -f __cicd__/php/Dockerfile.runtime -t zx5435/php:7.1.10 .
```
