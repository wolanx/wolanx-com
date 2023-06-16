---
title: kubectl
date: 2019-03-23
tags: [docker]
---

## kubectl

- 备忘录 https://kubernetes.io/docs/reference/kubectl/cheatsheet/

```shell
export KUBECONFIG=~/Desktop/www/work-book/env/sandbox/1_kubernetes/kubeconfig

kubectl get pod -A

kubectl run hello-minikube --image=zx5435/go-fs:v1 --port=8080

kubectl delete -n default deployment hello-minikube

kubectl logs -f pod-gim-uat-app-2
kubectl logs --tail=50 -f pod-gim-uat-app-2
```

## install

```shell
curl -LO https://storage.googleapis.com/kubernetes-release/release/v1.16.0/bin/windows/amd64/kubectl.exe
```

## config

### namespace

```shell
kubectl config set-context --current --namespace=$(basename $PWD)
kubectl config set-context --current --namespace=ccm-perf
kubectl config set-context $(kubectl config current-context) --namespace=ccm-perf
```

## run

```shell
kubectl run hello-minikube --image=zx5435/go-fs:v1 --port=8080
```

## delete 批量

```shell
kubectl -nccm-uat get pod --field-selector=status.phase!=Running
kubectl -nccm-uat get pod --field-selector=status.phase==Failed
```

## port-forward

```shell
# outside:inside 左外右内
kubectl -nzx5435 port-forward --address 0.0.0.0 service/air-ticket 7777:80

kubectl -nzx5435 expose deployment air-ticket --type=LoadBalancer --name=my-service
```

## configmap

```shell
kubectl -nccm-perf create configmap mq-conf --from-file=activemq
```

## kustomize

### kubectl builtins

```yaml
# kustomization.yaml
# k apply -k config/
apiVersion: kustomize.config.k8s.io/v1beta1
kind: Kustomization
generatorOptions:
# disableNameSuffixHash: true
labels:
  type: generated
annotations:
  note: generated
configMapGenerator:
- name: gim-fs
  files:
    - pii.yml
    - activemq.xml
    - broker.ks
- name: ept-env
  literals:
    - ACTIVEMQ_PASSWORD=admin
```

### install

```shell
# install
curl -s "https://raw.githubusercontent.com/kubernetes-sigs/kustomize/master/hack/install_kustomize.sh"  | bash

kustomize build | kubectl apply -f -
```

### config tpl

```yaml
# kustomization.yaml
namespace: gimc-prod
generatorOptions:
  # disableNameSuffixHash: true
  labels:
    type: generated
  annotations:
    note: generated
configMapGenerator:
  - name: gimc-cfgs
    files:
      - pii.yml
  - name: ept-env
    literals:
      - MYSQL_DB_NAME=gimc-prod
secretGenerator:
  - name: gimc-https
    files:
      - tls.key
      - tls.crt
```
