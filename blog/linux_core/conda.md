---
title: conda init
date: 2023-02-23
tags: [ linux ]
---

## cuda install

```shell
# https://developer.nvidia.com/cuda-11-6-0-download-archive?target_os=Linux&target_arch=x86_64&Distribution=Debian&target_version=11&target_type=deb_local
wget https://developer.download.nvidia.com/compute/cuda/11.6.0/local_installers/cuda-repo-debian11-11-6-local_11.6.0-510.39.01-1_amd64.deb
dpkg -i cuda-repo-debian11-11-6-local_11.6.0-510.39.01-1_amd64.deb
apt-key add /var/cuda-repo-debian11-11-6-local/7fa2af80.pub
add-apt-repository contrib
apt-get update
apt-get -y install cuda # error

wget http://ftp.de.debian.org/debian/pool/contrib/g/glx-alternatives/update-glx_1.2.1~deb11u1_amd64.deb
wget http://ftp.de.debian.org/debian/pool/contrib/g/glx-alternatives/glx-alternative-mesa_1.2.1~deb11u1_amd64.deb
wget http://ftp.de.debian.org/debian/pool/contrib/n/nvidia-support/nvidia-installer-cleanup_20151021+13_amd64.deb
wget http://ftp.de.debian.org/debian/pool/contrib/g/glx-alternatives/glx-diversions_1.2.1~deb11u1_amd64.deb
wget http://ftp.de.debian.org/debian/pool/contrib/g/glx-alternatives/glx-alternative-nvidia_1.2.1~deb11u1_amd64.deb

apt-get -y install cuda
apt-get install linux-headers-$(uname -r) # ！！！
reboot # ！！！
```

## conda install

```shell
apt-get install linux-headers-$(uname -r) # ！！！
curl -O https://repo.anaconda.com/archive/Anaconda3-2022.10-Linux-x86_64.sh
sh Anaconda3-2022.10-Linux-x86_64.sh
# /etc/conda
# conda install pytorch torchvision torchaudio pytorch-cuda=11.6 -c pytorch -c nvidia
# conda install cuda -c nvidia
```

$ source <CONDA_INSTALL_DIR>/bin/activate
$ conda create -y -n <CONDA_NAME>
$ conda activate <CONDA_NAME>

## conda update

```shell
conda -V
conda update -n base conda
conda update --all
conda install python=3.11
```

## uninstall

```shell
conda install anaconda-clean
rm -rf /etc/conda

apt-get remove --purge '^nvidia-.*'
apt-get remove --purge '^libnvidia-.*'
apt-get remove --purge '^cuda-.*'

apt-get install linux-headers-$(uname -r)
```

## check tool

```shell
lspci | grep -i nvidia # 查看PCI设备

# 查看硬件信息
apt-get install lshw
lshw -numeric -C display # 没有 unclaimed

cat /proc/driver/nvidia/version # 检查驱动版本

nvidia-smi
```
