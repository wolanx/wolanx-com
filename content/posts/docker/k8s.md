---
title: k8s
date: 2019-10-10
categories: [docker]
tags:
---

## auth api

```shell
# cd /var/run/secrets/kubernetes.io/serviceaccount 默认token目录
CA_CERT=/var/run/secrets/kubernetes.io/serviceaccount/ca.crt
TOKEN=$(cat /var/run/secrets/kubernetes.io/serviceaccount/token)
NAMESPACE=$(cat /var/run/secrets/kubernetes.io/serviceaccount/namespace)

curl --cacert $CA_CERT -H "Authorization: Bearer $TOKEN" "https://10.10.18.158:6443/api/v1/namespaces/$NAMESPACE/services/"
# 失败 需要 bind role
k get clusterroles
k -nccm-perf create rolebinding my-view --serviceaccount=ccm-perf:default --clusterrole=view
k -nccm-perf create rolebinding my-view --serviceaccount=ccm-perf:default --clusterrole=admin
k get rolebinding
```

## log app

- 基于 Golang 的云原生日志采集服务设计与实践 https://mp.weixin.qq.com/s/3sCyWg-HwfZ4ymm8T9s4zg

```shell
/var/lib/docker/containers/{}/{}-json.log
/var/lib/kubelet/pods/{}/volumes/kubernetes.io~empty-dir/log
```

## pvc
```yml
volumes:
  - name: mypd
    persistentVolumeClaim:
      claimName: pvc-oss-test
volumeMounts:
  - name: mypd
    mountPath: "/pvvv-test"
```

## helm

```shell
## install
wget https://get.helm.sh/helm-v2.16.0-linux-amd64.tar.gz
tar -zxvf helm-v2.16.0-linux-amd64.tar.gz
mv linux-amd64/helm /usr/local/bin/

## helm init
kubectl create serviceaccount --namespace kube-system tiller
kubectl create clusterrolebinding tiller-cluster-rule --clusterrole=cluster-admin --serviceaccount=kube-system:tiller
helm init --service-account tiller --upgrade
helm install stable/redis --name redis
```
