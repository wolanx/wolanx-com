---
title: pytorch mnist vgg16 错误记录
date: 2022-05-06T20:01:16+08:00
categories:
  - csdn
tags:
---

> https://blog.csdn.net/wolanx/article/details/124599294

## Intro
在尝试了FC，CNN等模型在 mnist 的练习后，使用 torchvision.models 的官方定义尝试运行 vgg16，resnet。
常见会出现以下错误：

- `RuntimeError`: Given groups=1, weight of size [64, 3, 3, 3], expected input[64, 1, 28, 28] to have 3 channels, but got 1 channels instead
- `RuntimeError`: Given input size: (512x1x1). Calculated output size: (512x0x0). Output size is too small

### 模型定义如下
```python
# mnist cnn 不知道怎么写的，可以参考 https://github.com/wolanx/pii/blob/main/x10_ml/demo2-6_mnist/demo2-6.ipynb
dataset1 = torchvision.datasets.MNIST(root="./data", train=True, download=True, transform=transform)

model = torchvision.models.vgg16(pretrained=False, num_classes=10)
model = model.to(device)
print(model)
```
```text
VGG(
  (features): Sequential(
    (0): Conv2d(3, 64, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1))
    (1): ReLU(inplace=True)
    (2): Conv2d(64, 64, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1))
    (3): ReLU(inplace=True)
    (4): MaxPool2d(kernel_size=2, stride=2, padding=0, dilation=1, ceil_mode=False)
    ...
  )
  (avgpool): AdaptiveAvgPool2d(output_size=(7, 7))
  (classifier): Sequential(
    (0): Linear(in_features=25088, out_features=4096, bias=True)
    (1): ReLU(inplace=True)
    ...
  )
)
```

## 错误一
> Given groups=1, weight of size [64, 3, 3, 3], expected input[64, 1, 28, 28] to have 3 channels, but got 1 channels instead

是说维度不同，mnist里的数据为单色*28px*28px，所以是(1, 28, 28)，但vgg是面向RGB图像是三色的，需要把它变成RGB的3通道，但是显然要自己去搞这样的数据太麻烦。换个思路，查看vgg16的定义把vgg的features的第一层修改下
```text
VGG(
  (features): Sequential(
    (0): Conv2d(3, 64, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1))                # 改这一层
    (1): ReLU(inplace=True)
```
修改完如下
```python
model = torchvision.models.vgg16(pretrained=False, num_classes=10)
model.features[0] = nn.Conv2d(1, 64, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1))  # 这里的 conv2d(3,64) 改成了 conv2d(1,64)
model = model.to(device)
print(model) # 再次检查下
```
```text
VGG(
  (features): Sequential(
    (0): Conv2d(1, 64, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1))                # 改这一层
    (1): ReLU(inplace=True)
```
到这一步，错误一就解决了，但紧接着会出现错误二

## 错误二
> Given input size: (512x1x1). Calculated output size: (512x0x0). Output size is too small

这一步说的太抽象，先回顾下vgg16的几层模型，需要注意到，图像经过多次conv，而conv stride=1时，相当于多图像进行了缩小（一半），而 mnist 的像素为 28 * 28，缩小一半为 14 * 14，再 7 * 7，再 4* 4，再 2 * 2，再 1 * 1，再就 0 * 0。而vgg层数还没运行到最后就没了。和错误一相似，一里是RGB不满足，错误二是像素不满足，同样要换样本不现实。简单处理就是，不要不断的缩小，减层可以，但是会破坏定义结构。但也可以是反卷积：
```python
model = torchvision.models.vgg16(pretrained=False, num_classes=10)
model.features[0] = nn.Conv2d(1, 16, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1))  # 不是 (3,64) (1,16)，单通道再加小一点
model.features[2] = nn.ConvTranspose2d(16, 64, kernel_size=(3, 3), stride=(2, 2), padding=(0, 0), bias=False)
model = model.to(device)
print(model) # 再次检查下
```
```text
VGG(
  (features): Sequential(
    (0): Conv2d(1, 16, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1))   # 这里变了
    (1): ReLU(inplace=True)
    (2): ConvTranspose2d(16, 64, kernel_size=(3, 3), stride=(2, 2), bias=False)  # 这里变了
```
这样就解决了像素太低问题，整个模型至少现在能跑了，但是如果有做train的话，发现error实在收敛太慢，还需要再优化下。
