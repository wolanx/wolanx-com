---
title: springboot
date: 2019-05-14T20:10:57+08:00
tags: [java]
---

# event
- 芋道 Spring Boot 事件机制 Event 入门 https://www.iocoder.cn/Spring-Boot/Event/?qun=
  1. ApplicationEvent EventObject
  2. ApplicationEventPublisherAware
  3. ApplicationListener<?> or @EventListener

# cache
- @Cacheable(key = "#id")
- @CachePut(key = "#user.id")
- @CacheEvict(key = "#id")

# async
- 芋道 Spring Boot 异步任务入门 https://www.iocoder.cn/Spring-Boot/Async-Job/?self

# springcloud
- eureka server 服务注册 http://localhost:8761/
- eureka client 可以起多个
- call service: Ribbon, Feign(主流,再封装)
- zipkin 链路追踪
- config 总线 amqp重载
- hystrix 熔断器,监控
- zuul 网关
