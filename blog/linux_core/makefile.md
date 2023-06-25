---
title: makefile样例
date: 2015-12-13
tags:
  - linux
---

# makefile

## 1

```sh
default:
	cat Makefile

a:
	go run cmd/pipeline-demo/main.go 

b:
	go run cmd/pipeline-demo/main.go 
```

## 2

```sh
demo="Usage: \n\
\# 设置 crontab \n\
\t make crontab proj=xdq type=yy env=test \
"

default:
	@echo ${demo}

crontab:
	@echo $(proj) $(type) $(env)
```

## 3

```sh
default:
	cat Makefile

build: build-fe build-be build-pkg

build-be:
	docker run -it --rm \
	    -v "$$GOPATH/src":/go/src \
	    -w /go/src/github.com/zx5435/wolan/cmd/wolan-server \
	    golang:1.10.2 \
        sh -c "CGO_ENABLED=0 GOOS=linux go build -v -installsuffix cgo -o wolan-server"

build-fe:
	cd frontend && npm run build

build-pkg:
	docker build -f __cicd__/Dockerfile -t zx5435/wolan .

ingress-build:
	docker run -it --rm \
	    -v "$$GOPATH/src":/go/src \
	    -w /go/src/github.com/zx5435/wolan/cmd/wolan-ingress \
	    golang:1.10.2 \
        sh -c "CGO_ENABLED=0 GOOS=linux go build -v -installsuffix cgo -o wolan-ingress"

ingress-pkg:
	docker build -f __cicd__/Dockerfile.ingress -t zx5435/wolan:ingress .

ingress-test:
	docker run -it -d --name wolan-ingress -p80:80 -p443:443 zx5435/wolan:ingress

restart: down up

up:
	docker stop wolan
	docker rm wolan
	cd __work__ && docker run -it -d --name wolan -p 4321:23456 \
	    -v "$$PWD":/app/__work__ \
	    -v "/var/run/docker.sock:/var/run/docker.sock" \
	    zx5435/wolan
```

## 参考

```sh
NAME=timescaledb-postgis
ORG=timescale
PG_VER=pg10
VERSION=$(shell awk -F ':' '/^FROM/ { print $$2 }' Dockerfile | sed "s/\(.*\)-.*/\1/")

default: image

.build_postgis_$(VERSION)_$(PG_VER): Dockerfile
ifeq ($(PG_VER),pg9.6)
	docker build --build-arg POSTGIS_VERSION=2.3.7 --build-arg PG_VERSION_TAG=$(PG_VER) -t $(ORG)/$(NAME):latest-$(PG_VER) .
	docker tag $(ORG)/$(NAME):latest-$(PG_VER) $(ORG)/$(NAME):latest
else
	docker build --build-arg POSTGIS_VERSION=2.4.4 --build-arg PG_VERSION_TAG=$(PG_VER) -t $(ORG)/$(NAME):latest-$(PG_VER) .
endif
	docker tag $(ORG)/$(NAME):latest-$(PG_VER) $(ORG)/$(NAME):$(VERSION)-$(PG_VER)
	touch .build_postgis_$(VERSION)_$(PG_VER)

image: .build_postgis_$(VERSION)_$(PG_VER)

push: image
	docker push $(ORG)/$(NAME):$(VERSION)-$(PG_VER)
	docker push $(ORG)/$(NAME):latest-$(PG_VER)
ifeq ($(PG_VER),pg9.6)
	docker push $(ORG)/$(NAME):latest
endif


clean:
	rm -f *~ .build_postgis_*

.PHONY: default image push clean
```

## grundfos ccm

```shell
IMAGE_NS := registry.cn-shanghai.aliyuncs.com/digital-web
#TIME := $(shell date +"%Y%m%d_%H%M%S")
TIME := $(shell date +"%Y%m%d")
VER := ${TIME}_${CI_COMMIT_SHORT_SHA}
VER_RT := $(shell date +"%Y%m%d_%H%M")

default:
	cat Makefile

test:
	@echo ${VER}

gsc-build-runtime-image:
	docker build -f __cicd__/sct.rt.Dockerfile -t ${IMAGE_NS}/sct-rt:${VER_RT} .
	docker push ${IMAGE_NS}/sct-rt:${VER_RT}

ccm-build:
	echo ${sid} ${env}
	docker build -f __cicd__/ccm.code.Dockerfile --build-arg env=${env} -t ${IMAGE_NS}/ccm-code:${VER}_${env} .
	docker push ${IMAGE_NS}/ccm-code:${VER}_${env}

ccm-deploy:
	echo ${sid} ${env}
	docker build -f __cicd__/gim.code.Dockerfile --build-arg env=${env} -t ${IMAGE_NS}/gim-code:${VER}_${env} .
	docker push ${IMAGE_NS}/gim-code:${VER}_${env}
	docker exec -w /www/env/sandbox/6.2.0.${sid}_ccm tf_tf_1 terraform apply -auto-approve -var sha=${VER}_${env}
```
