---
title: python
date: 2019-05-08T17:15:51+08:00
tags: [python]
---

## python -m

```shell
cat b.json | python -m json.tool # json
python -m http.server 3333 # local file
```

## pip加速

pip install tensorflow-gpu -i https://pypi.tuna.tsinghua.edu.cn/simple

```shell
mkdir ~/.pip
cat > ~/.pip/pip.conf << EOF
[global]
trusted-host=mirrors.aliyun.com
index-url=https://mirrors.aliyun.com/pypi/simple/
EOF
```

## @deprecated

warnings.warn("弃用", DeprecationWarning)

## venv

```shell
pip install virtualenv -i https://pypi.tuna.tsinghua.edu.cn/simple
virtualenv --no-site-packages venv
```

## anaconda

```shell
conda create -n py39 python=3.9 anaconda

conda install pytorch torchvision torchaudio cudatoolkit=11.3 -c pytorch
```

## opencv

- OpenCV中文官方文档 http://www.woshicver.com/
- 使用Python+opencv进行图像处理(一) https://zhuanlan.zhihu.com/p/63429810
