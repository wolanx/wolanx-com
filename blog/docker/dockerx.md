---
title: docker buildx 跨平台 arm64
date: 2025-10-11
tags: [ docker ]
---

- doc https://www.voidking.com/dev-docker-buildx

```shell
docker buildx ls

docker buildx create --name arm64 --driver docker-container --use
docker buildx use arm64
docker buildx inspect --bootstrap # 查看 builder 详情并初始化
docker buildx build --platform linux/arm64 -t your-image-name:tag --load .

docker buildx use default
```
