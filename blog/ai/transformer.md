---
title: T5
date: 2026-08-18T09:35:00+08:00
tags: [gpt]
---

好，这个需求非常「工程脑」——  
我们直接把前面所有碎片：**RoPE / QK / MLP / 残差 / 层数 / H / 循环 / shape**  
压成一份**“读代码级”的终极 TUI 总结表 + 流**。

只讲**现在主流的 Pre-Norm + RoPE + SwiGLU 架构**（LLaMA / Qwen / DeepSeek / Gemma 通用）。

---

## 一、全局常量（先看一眼）

```
B = batch
L = seq_len
H = num_heads
d = head_dim
D = H × d          (model_dim)
E = 4D 或 8/3·D     (FFN 中间)
N = num_layers
```

---

## 二、一个 Block 的「TUI 循环模板」（核心）

> **下面这个，重复 N 次**

```
┌─ Block l ───────────────────────────────────────────────┐
│                                                        │
│  IN:  x_l                     [B, L, D]                │
│       │                                                │
│       ├─► RMSNorm ──► x                       [B,L,D] │
│       │                                                │
│       ├─► Linear(qkv)      ──► [B,L,3D]               │
│       │    reshape           [B, H, L, d] ×3           │
│       │                                                │
│       ├─► RoPE on Q,K       （仅 Q/K）                 │
│       │    Qr [B,H,L,d]  Kr [B,H,L,d]  V [B,H,L,d]    │
│       │                                                │
│       ├─► Attn              Q@K^T/√d → softmax → @V    │
│       │    scores [B,H,L,L]                          │
│       │    out    [B,H,L,d]                          │
│       │    merge  [B,L,D]                            │
│       │                                                │
│       ├─► Linear(out)       [B,L,D]                   │
│       │                                                │
│       ├─► + residual        x_l + Attn = x_mid        │
│       │                                                │
│       ├─► RMSNorm(x_mid)    [B,L,D]                   │
│       │                                                │
│       ├─► FFN (SwiGLU)                                   │
│       │   up/gate ── silu*up ── down                  │
│       │   [B,L,D]→[B,L,E]→[B,L,D]                    │
│       │                                                │
│       └─► + residual        x_{l+1} = x_mid + FFN     │
│                                                        │
└────────────────────────────────────────────────────────┘
         ↓
      进 Block l+1（共 N 次）
```

---

## 三、把「N 次循环」展开成具体模型（真·主流）

### 🔹 LLaMA-2 / LLaMA-3 风格

```
Embedding: [B, L] → [B, L, 4096]

for l in 0 .. 31:
    Block(l)
    # 内部：
    #   H = 32
    #   d = 128
    #   E = 11008 (≈ 8/3·D)

Final RMSNorm
LM Head (tied or not)
→ logits [B, L, vocab]
```

**数字速查**

| 项 | 值 |
|---|---|
| 层数 N | 32 |
| H | 32 |
| d | 128 |
| RoPE 频率 | 10000, base=500k(L3) |
| FFN 次数 | 32 |
| 残差加法 | 64 次（每层 2） |

---

### 🔹 Qwen2-7B / 72B（同模板）

```
N = 28 / 80
H = 28→28, 80→64
d = 128
E = 18944 (Qwen 的 FFN 偏好)
```

TUI 循环完全一样，只换 N / H / E。

---

### 🔹 DeepSeek-V2 / Mixtral（MoE 版）

```
for l in 0 .. 59:
    x = x + Attention(...)
    x = x + MoE_FFN(x)   # 8 expert, top-2
```

MoE 内部：
```
FFN(x) = sum_i(gate_i · Expert_i(x))
shape: 仍然是 [B,L,D] → [B,L,D]
```

👉 **Block 数 = 60，MLP 逻辑调用 = 60×2**

---

## 四、用「循环次数 + shape」压缩成一张表（收藏级）

| 阶段 | 循环次数 | 核心张量 shape | 备注 |
|---|---|---|---|
| Embedding | 1 | `[B,L] → [B,L,D]` | 词表映射 |
| Q/K/V 投影 | N | `[B,L,D] → [B,H,L,d]×3` | 每层 |
| RoPE | N | `[B,H,L,d]×2` | 只 Q/K |
| Attention 内积 | N | `[B,H,L,L]` | 位置信息在此 |
| Head merge | N | `[B,L,D]` | |
| Attn 残差 | N | +1 | 第 1 条高速路 |
| FFN 升维 | N | `[B,L,D] → [B,L,E]` | |
| FFN 降维 | N | `[B,L,E] → [B,L,D]` | |
| FFN 残差 | N | +1 | 第 2 条高速路 |
| 总残差加法 | 2N | — | 防梯度炸 |
| Final Norm | 1 | `[B,L,D]` | |
| LM Head | 1 | `[B,L,V]` | |


---

## deepseek v4 flash

```text
Embedding: [B, L] → [B, L, 4096]

for l in 0..42:                      # 循环 N=43 次
    x: [B, L, 4096]
    │
    ├─ mHC 分流: x → 复制 hc_mult=4 路 → [B, L, 4, 4096]   # 残差升级版
    │
    ├─ Q 路径:
    │   x → wq_a: [B,L,4096]→[B,L,1024]
    │       → q_norm → wq_b: [B,L,1024]→[B,L,64 * 512]
    │       → reshape Q: [B, H=64, L, d=512]
    │       → RoPE 只转其中 64 维/头
    │
    ├─ KV 路径 (MLA):
    │   x → wkv: [B,L,4096]→[B,L,512]      # 1 个 latent，兼当 K 和 V
    │   broadcast 给 64 个 Q 头
    │   KV cache 每 token 只存 512 个数
    │
    ├─ 混合注意力（按层交替）:
    │   前 2 层: 纯 SWA (window=128)        scores [B,64,L,128]
    │   其余: CSA(compress=4, topk=512) / HCA(compress=128) 交替
    │   稀疏打分靠 Indexer: index_n_heads=64, index_head_dim=128
    │
    ├─ 输出: attn_out [B,64,L,512] → merge [B,L,32768]
    │       → wo_lora(1024) → [B,L,4096]
    │
    ├─ + mHC 残差（4 路 Sinkhorn 收敛回 1 路）
    │
    ├─ SwiGLU MoE:
    │   gate/up: [B,L,4096]→[B,L,2048] ×7 专家
    │   down:    → [B,L,4096]
    │
    └─ + mHC 残差 → 进下一层

Final RMSNorm → LM Head → [B, L, 129280]
```

---
