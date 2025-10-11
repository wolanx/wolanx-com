---
title: linux uft
date: 2025-09-04
tags:
  - linux
---


```shell
# 保存当前规则
# 在 Debian/Ubuntu 上，nftables 服务会自动加载 /etc/nftables.conf。
sudo nft list ruleset > /etc/nftables.conf
```

```shell

# 清空规则
nft flush ruleset

# 定义表
nft add table inet filter

# 定义输入、输出、转发链
nft add chain inet filter input { type filter hook input priority 0 \; policy drop \; }
nft add chain inet filter output { type filter hook output priority 0 \; policy accept \; }
nft add chain inet filter forward { type filter hook forward priority 0 \; policy drop \; }

# 允许已建立的连接
nft add rule inet filter input ct state established,related accept

# 允许SSH（22端口）
nft add rule inet filter input tcp dport 22 accept

# 允许ICMP（可选）
nft add rule inet filter input icmp type echo-request accept

# 允许本地回环流量
nft add rule inet filter input iif lo accept
```

```shell
# 查看当前规则集
nft list ruleset

# 仅允许 ssh 和 docker 的 port
cat > /etc/nftables.conf
```

```text
table inet filter {
    chain input {
        type filter hook input priority filter; policy drop;
        ct state established,related accept
        tcp dport 22 accept
        icmp type echo-request accept
        iif "lo" accept
        iifname "docker0" accept
        iifname "br-*" accept
    }

    chain output {
        type filter hook output priority filter; policy accept;
    }
}
```
