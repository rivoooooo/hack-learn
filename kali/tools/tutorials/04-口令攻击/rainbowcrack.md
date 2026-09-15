# rainbowcrack（彩虹表：时间-内存权衡破解）

> **一句话**：用「预先花时间算好、把结果压成表存起来」的方式，换取「以后破解时几乎不花时间」——**时间-内存权衡（time-memory tradeoff）** 的经典实现，专治**无盐**的 LM/NTLM/MD5/SHA1/SHA256 哈希。
> **分类**：口令攻击 / 离线哈希破解 ｜ **Kali 包**：`rainbowcrack`（命令 `rcrack`、`rtgen`、`rtsort`、`rtmerge`、`rt2rtc`、`rtc2rt`）｜ **官方文档**：<https://www.kali.org/tools/rainbowcrack/> ｜ 上游：<https://project-rainbowcrack.com/index.htm>

---

## 1. 它解决什么问题

破解一个哈希，朴素做法是**暴力枚举所有候选口令，逐个哈希比对**：

```
候选 "aaa"  → md5 → 比较
候选 "aab"  → md5 → 比较
候选 "aac"  → md5 → 比较
...（对 8 位小写字母 = 2080 亿次）
```

对**同一个哈希空间重复破解**（比如每次渗透都遇到 NTLM 哈希）来说，这种「每次都从零算」是巨大浪费。彩虹表的思路是：

> **把「候选口令 → 哈希」的计算结果提前算好、压缩存储；以后再遇到该空间里的哈希时，直接查表。**

**对比同类**：

| 工具 | 核心思路 | 时间/内存特征 | 适用场景 |
|------|----------|---------------|----------|
| **rainbowcrack** | **预计算表 + 查表** | 预计算久、表大、**查询极快**（毫秒级） | 同一哈希空间被**反复**破解；无盐哈希 |
| **hashcat / john（字典+规则）** | 实时计算 | 每次都要算，但**字典/规则更灵活** | 目标性强、口令有规律 |
| **hashcat 纯暴力** | 实时穷举 | 慢但覆盖完整 | 空间小（如 8 位纯数字） |
| **ophcrack** | **也基于彩虹表**，带 GUI | 面向 Windows LM/NTLM | Windows 口令审计。见 [`ophcrack.md`](ophcrack.md) |

**2026 年的现实判断（必须先说清楚）**：

| 场景 | 彩虹表是否值得 |
|------|----------------|
| **无盐**、算法固定（LM/NTLM/MD5）、且**你要反复破解同一空间** | ✅ 仍然有价值（查表毫秒级） |
| **有盐**的哈希（bcrypt/scrypt/Argon2/modern 加盐） | ❌ **直接失效**（见第 2 节） |
| **一次性**破解、口令有明确特征 | ❌ 用 hashcat + 规则更划算 |
| **NTLM（Windows）审计** | ⚠️ 可以，但 **hashcat 的 GPU 暴力/NTLM 表**通常更实用 |
| **学习「时间-内存权衡」原理** | ✅ **最佳教具** |

**一句话**：**彩虹表是理解「预计算攻击」的必学概念，但不是 2026 年的首选工具**；它的现实价值集中在「无盐哈希 + 反复破解同一空间」和「教学」。

---

## 2. 工作原理

### 2.1 朴素表的两个极端都不可行

假设口令空间是 8 位小写字母（`a-z`，26⁸ ≈ **2080 亿**）。

| 方案 | 存储 | 查询 | 问题 |
|------|------|------|------|
| **完整表**：把所有「口令→哈希」都存下来 | 2080 亿条 | **O(1) 查一下** | **存储爆炸**（TB 级根本存不下） |
| **不建表**：每次实时穷举 | 0 | **数小时 ~ 数天** | **时间爆炸** |

**彩虹表是这两个极端之间的折中**——用「中等存储 + 很短查询时间」。

### 2.2 核心构件：归约函数（reduction function）

```
        ┌──────────────────── 一条「链」─────────────────────┐
        │                                                    │
口令起点                                                  口令（链尾）
  p0 ──[hash]──► h0 ──[reduce R]──► p1 ──[hash]──► h1 ──[reduce R]──► p2 ──► ... ──► p_k
        │                │                  │
        │                │                  └─ R 是「把哈希变成另一个口令」的函数
        │                │                    （不是逆运算！只是构造一个确定映射）
        │                └─ 这就是真实哈希（比如 md5(p0)）
        └─ 链上所有中间口令都被「丢掉」，只存【链首 p0 + 链尾 p_k】
```

**关键点**：

- **`R` 不是哈希的逆**（哈希不可逆）——它只是「哈希 → 口令空间」的**确定性映射**（例如「取哈希的前 4 字节，映射成 4 个小写字母」）；
- 一条长度为 `k` 的链，**中间所有哈希都被丢弃**，只保留「链首 + 链尾」→ **这就是节省存储的全部秘密**；
- 查询时，如果目标哈希在某条链上，就能**从链尾反推出它是哪个位置**，然后**从链首重放**那条链，把中间的口令找出来。

### 2.3 查询过程（理解这个才理解「为什么快」）

```
目标哈希 H
   │
   ├─ 假设 H 在链的【最后一步】：R(H) == 链尾？            → 命中，重放链找出口令
   ├─ 否则：H ──R──► p ──hash──► h ──R──► == 链尾？         → 命中（H 在第 k-1 步）
   ├─ 否则：再往前推一次，比较链尾 …
   └─ 最多做 k 次「hash+reduce+比较」→ 都没中 → 该表不包含 H
```

**所以单次查询成本 ≈ k 次哈希运算**（`k` 是链长，通常几百到几万）——**这比 2080 亿次暴力快了几个数量级**。

### 2.4 彩虹表相对「普通哈希链表」的改进：**用不同的 R**

朴素的「哈希链表」（Hellman 表）用**同一个 R**，会有一个严重问题：**链与链之间会碰撞并合并**，导致大量链实际上是重复的（浪费存储）。

**彩虹表（Oechslin 2003）的改进**：链上**每一步用不同的归约函数 R₁, R₂, …, R_k**。

```
p0 ──hash──► h0 ──R1──► p1 ──hash──► h1 ──R2──► p2 ──hash──► h2 ──R3──► ...
                          ▲                    ▲
                          └────────────────────┴── 每步用不同的 R，降低链间碰撞合并
```

**这就是它叫「彩虹」表的原因**（每一步一个「颜色」，官方文档也是这么解释的）。**用不同的 R 显著减少了链合并，从而用更少的存储覆盖更大的空间**——这是彩虹表相对 Hellman 表的核心优势。

### 2.5 为什么「加盐」让彩虹表彻底失效

```
彩虹表的前提：哈希函数是【无盐】的、且对同一口令【永远输出同一个值】

   md5("password") = 5f4dcc3b5aa765d61d8327deb882cf99   ← 永远是它
   → 预计算一次，全世界所有 "password" 的 md5 都能查表命中

现代做法：加盐（salt）
   hash("password", salt="a1b2c3") = 完全不同的值
   hash("password", salt="d4e5f6") = 又一个完全不同的值
                          ▲
                          └─ 攻击者必须【为每一个 salt 单独建一套彩虹表】
                             → 预计算成本 × 盐空间大小 → 不可行
```

**同理，慢哈希（bcrypt / scrypt / Argon2 / PBKDF2）也让预计算变得不可行**——因为单次哈希本身就要几十到几百毫秒。

**所以「彩虹表还有用吗」的答案是**：

| 哈希类型 | 彩虹表可用性 |
|----------|--------------|
| **LM / NTLM**（Windows，历史上无盐） | ✅ 可用（这也是 `ophcrack` 的领域） |
| **无盐 MD5 / SHA1** | ✅ 可用（老系统、很多 CTF） |
| **无盐 SHA256** | ⚠️ 可用但空间大、表更大 |
| **加盐哈希**（`md5($salt.$pass)`） | ❌ 每个 salt 要一套表 → 不可行 |
| **bcrypt / scrypt / Argon2 / PBKDF2** | ❌ 不可行 |

### 2.6 工具链：五个命令各干什么

```
   ┌──────────────── rtgen ────────────────┐
   │  生成彩虹表（最耗时的步骤，可能要跑几天）│
   │  rtgen <算法> <字符集> <最小长度> <最大长度> \
   │         <表索引> <链长> <链数> <部分索引>        │
   └───────────────────┬───────────────────┘
                       ▼  产出多个 .rt 分片（part）
   ┌──────────────── rtsort ───────────────┐
   │  按「链尾」排序（查询需要二分/有序查找）│
   └───────────────────┬───────────────────┘
                       ▼  排好序的 .rt
   ┌──────────────── rtmerge ──────────────┐
   │  合并多个表（多文件 → 一个）           │
   └───────────────────┬───────────────────┘
                       ▼
   ┌────────── rt2rtc / rtc2rt ────────────┐
   │  .rt（文本格式） ⇄ .rtc（二进制/压缩）  │
   │  转换：省空间、加快加载                 │
   └───────────────────┬───────────────────┘
                       ▼
   ┌──────────────── rcrack ───────────────┐
   │  实际破解：给一个哈希（或一批），查表    │
   │  rcrack <表所在目录> -h <哈希>          │
   └───────────────────────────────────────┘
```

**`rtgen` 的「表索引 / 链长 / 链数 / 部分索引」是什么意思**：

| 参数 | 含义 |
|------|------|
| **表索引（table_index）** | 多张表用不同索引区分（不同表覆盖不同部分/用不同随机起点）。**`rtgen` 一次生成一张表** |
| **链长（chain_len）** | 每条链有多少步。**链越长 → 覆盖越大 → 但查询越慢** |
| **链数（chain_num）** | 表里有多少条链。**链越多 → 覆盖越大 → 表越大** |
| **部分索引（part_index）** | 把一张大表切成分片（`part_index`），便于分批生成、便于并行 |

**「参数组合必须一致」是彩虹表最容易踩的坑**：查询时用的表必须和生成时的**算法、字符集、长度范围、表索引**完全匹配，否则查不到——**而且不报错，只是「无结果」**。

> **预置表**：上游 <https://project-rainbowcrack.com/table.htm> 提供了一批**已算好的表**（付费/免费混合）。**自己从零 `rtgen` 一张有用的表通常要几天到几个月**——所以现实中要么用预置表，要么用 hashcat。

---

## 3. 安装与快速上手

```bash
sudo apt install rainbowcrack
command -v rcrack rtgen rtsort rtmerge rt2rtc rtc2rt
```

```console
root@kali:~# command -v rcrack rtgen rtsort rtmerge rt2rtc rtc2rt
/usr/bin/rcrack
/usr/bin/rtgen
/usr/bin/rtsort
/usr/bin/rtmerge
/usr/bin/rt2rtc
/usr/bin/rtc2rt
```

```bash
rcrack -h
```

```console
root@kali:~# rcrack -h
RainbowCrack 1.8
Copyright 2020 RainbowCrack Project. All rights reserved.
http://project-rainbowcrack.com/

usage: ./rcrack path [path] [...] -h hash
       ./rcrack path [path] [...] -l hash_list_file
       ./rcrack path [path] [...] -lm pwdump_file
       ./rcrack path [path] [...] -ntlm pwdump_file
path:              directory where rainbow tables (*.rt, *.rtc) are stored
-h hash:           load single hash
-l hash_list_file: load hashes from a file, each hash in a line
-lm pwdump_file:   load lm hashes from pwdump file
-ntlm pwdump_file: load ntlm hashes from pwdump file

implemented hash algorithms:
    lm HashLen=8 PlaintextLen=0-7
    ntlm HashLen=16 PlaintextLen=0-15
    md5 HashLen=16 PlaintextLen=0-15
    sha1 HashLen=20 PlaintextLen=0-20
    sha256 HashLen=32 PlaintextLen=0-20

examples:
    ./rcrack . -h 5d41402abc4b2a76b9719d911017c592
    ./rcrack . -l hash.txt
```

```bash
rtgen -h
```

```console
root@kali:~# rtgen -h
RainbowCrack 1.8
Copyright 2020 RainbowCrack Project. All rights reserved.
http://project-rainbowcrack.com/

usage: rtgen hash_algorithm charset plaintext_len_min plaintext_len_max table_index chain_len chain_num part_index
       rtgen hash_algorithm charset plaintext_len_min plaintext_len_max table_index -bench

hash algorithms implemented:
    lm HashLen=8 PlaintextLen=0-7
    ntlm HashLen=16 PlaintextLen=0-15
    md5 HashLen=16 PlaintextLen=0-15
    sha1 HashLen=20 PlaintextLen=0-20
    sha256 HashLen=32 PlaintextLen=0-20

examples:
    rtgen md5 loweralpha 1 7 0 1000 1000 0
    rtgen md5 loweralpha 1 7 0 -bench
```

**最小可用（用官方示例的哈希验证工具链是否正常）**：

```bash
# 造一个「空间极小」的表：能立刻生成完，用来验证整条链路
mkdir -p /tmp/rt-demo/tables
cd /tmp/rt-demo

# 字符集 'numeric'，长度 1-4，链长 1000，链数 1000（很小，秒级完成）
rtgen md5 numeric 1 4 0 1000 1000 0
ls -l *.rt
rtsort ./*.rt
ls -l *.rt
```

```console
root@kali:~# rtgen md5 numeric 1 4 0 1000 1000 0
RainbowCrack 1.8
Copyright 2020 RainbowCrack Project. All rights reserved.
http://project-rainbowcrack.com/

generating rainbow table for md5(numeric, 1-4) table index 0
...
1000 rainbow chains generated (0.01 seconds)
```

```bash
# 查表破解：md5("1234") = 81dc9bdb52d04dc20036dbd8313ed055
rcrack /tmp/rt-demo -h 81dc9bdb52d04dc20036dbd8313ed055
```

```console
root@kali:~# rcrack /tmp/rt-demo -h 81dc9bdb52d04dc20036dbd8313ed055
RainbowCrack 1.8
Copyright 2020 RainbowCrack Project. All rights reserved.
http://project-rainbowcrack.com/

1 hash(es) loaded.
Warning: table md5_numeric#1-4_0_1000x1000_0.rt: 1000 chains, 1000 chain length
...
81dc9bdb52d04dc20036dbd8313ed055  md5  1234
```

**格式转换（可选，用来省空间/加速加载）**：

```bash
rt2rtc ./*.rt        # .rt（文本）→ .rtc（压缩二进制）
ls -l *.rtc
rtc2rt ./*.rtc       # 反向：.rtc → .rt
```

> 实战中**先用预置表**（或直接上 hashcat），**不要从零生成大表**。自己 `rtgen` 一张能覆盖 8 位小写字母的表，需要**数天到数周的 CPU 时间和数百 GB 存储**。

---

## 4. 核心参数详解

> 全部取自上面的 `rcrack -h` / `rtgen -h` 原文。`rt2rtc`/`rtc2rt`/`rtmerge`/`rtsort` 在 Kali 页面里 `-h` 输出为 `no rainbow table found`（它们把参数当表文件解析），实际用法见下。

### 4.1 rcrack（破解 / 查表）

```
usage: rcrack path [path] [...] -h hash
       rcrack path [path] [...] -l hash_list_file
       rcrack path [path] [...] -lm pwdump_file
       rcrack path [path] [...] -ntlm pwdump_file
```

| 参数 | 作用 | 使用建议 |
|------|------|----------|
| `path [path] [...]` | **彩虹表所在目录**（可有多个） | 可以有多个路径；`.rt` 与 `.rtc` 都会被识别 |
| `-h <hash>` | 破解**单个**哈希 | 冒烟测试、单点破解 |
| `-l <file>` | 从文件读**一批哈希**（每行一个） | **批量破解用这个**；比循环调用 `-h` 高效得多 |
| `-lm <pwdump>` | 从 pwdump 文件读 **LM** 哈希 | Windows 老系统口令审计 |
| `-ntlm <pwdump>` | 从 pwdump 文件读 **NTLM** 哈希 | Windows 口令审计（更常用） |

**支持的算法与长度上限**（决定了你的表要覆盖多大空间）：

| 算法 | 哈希长度 | **明文长度范围** |
|------|----------|------------------|
| `lm` | 8 | **0-7**（LM 本身的设计限制） |
| `ntlm` | 16 | **0-15** |
| `md5` | 16 | **0-15** |
| `sha1` | 20 | **0-20** |
| `sha256` | 32 | **0-20** |

> **注意**：`rcrack` **不支持** bcrypt/scrypt/Argon2/PBKDF2 等现代算法，**也不支持带盐的哈希**。它只处理「无盐、算法在列表内」的情况。

**关键用法要点**：

1. **路径参数在前，选项在后**（官方用法就是 `rcrack path -h hash`）；
2. **表必须与哈希类型匹配**：给 md5 表喂 NTLM 哈希 → **无结果且不报错**；
3. **表必须与生成参数匹配**：长度范围/字符集/表索引都要对上；
4. **一次给多个路径**可以合并多组表（比如分片存放在不同目录）。

### 4.2 rtgen（生成表）

```
usage: rtgen hash_algorithm charset plaintext_len_min plaintext_len_max table_index chain_len chain_num part_index
       rtgen hash_algorithm charset plaintext_len_min plaintext_len_max table_index -bench
```

| 位置 | 参数 | 作用 | 使用建议 |
|------|------|------|----------|
| 1 | `hash_algorithm` | `lm` / `ntlm` / `md5` / `sha1` / `sha256` | 与目标哈希一致 |
| 2 | `charset` | **字符集** | 见下表；**这是决定空间大小的关键** |
| 3 | `plaintext_len_min` | 明文最小长度 | 与 `plaintext_len_max` 一起限定范围 |
| 4 | `plaintext_len_max` | 明文最大长度 | —— |
| 5 | `table_index` | **表索引** | 多张表时用不同值；**查询时无需指定**（rcrack 会遍历目录里所有表） |
| 6 | `chain_len` | **链长** | 越大覆盖越大、查询越慢；常用 `1000`~`10000` |
| 7 | `chain_num` | **链数** | 越大覆盖越大、表越大；常与 `chain_len` 同量级或更大 |
| 8 | `part_index` | **分片索引** | 一张大表分批生成时用；**同一张表的分片要一起用** |
| 替代 | `-bench` | **只跑基准测试**，不生成表 | **先 `-bench` 估算「生成要多久」**——强烈建议 |

**可用字符集**（以本机程序为准；以下是项目文档中的常见集合）：

| 字符集名 | 内容 | 空间大小示例 |
|----------|------|--------------|
| `numeric` | `0123456789` | 10^n |
| `loweralpha` | `abcdefghijklmnopqrstuvwxyz` | 26^n |
| `loweralphanum` | 小写字母 + 数字 | 36^n |
| `alpha` | 大小写字母 | 52^n |
| `alphanum` | 大小写字母 + 数字 | 62^n |
| `ascii-32-95` | 可打印 ASCII | 95^n |
| `mixalpha-numeric-all-space` | 更全（含空格等） | 更大 |

**`-bench` 的用法（先估时间，再决定要不要生成）**：

```bash
# 只做基准测试：不会写表文件，只告诉你「这张表要算多久」
rtgen md5 loweralpha 1 7 0 -bench
```

**空间大小与时间的直觉感受**：

| 字符集 | 长度 | 空间大小 | `rtgen` 的现实感受 |
|--------|------|----------|-------------------|
| `numeric` | 1-8 | 10⁸ = 1 亿 | 数分钟 ~ 数小时（视参数） |
| `loweralpha` | 1-6 | ≈ 3.2 亿 | 数小时 |
| `loweralpha` | 1-7 | ≈ 83 亿 | **数天** |
| `alphanum` | 1-8 | ≈ 2.2 × 10¹⁴ | **完全不可行（需要巨大集群 + TB 存储）** |

→ **这就是为什么现实中用预置表或 hashcat。**

### 4.3 rtsort / rtmerge / rt2rtc / rtc2rt

| 命令 | 用法 | 作用 | 为什么需要 |
|------|------|------|------------|
| **`rtsort`** | `rtsort *.rt`（或目录） | **按链尾排序** | 查询算法需要按链尾查找/二分；**`rtgen` 生成的表未排序，不 sort 无法正常用** |
| **`rtmerge`** | `rtmerge in1.rt in2.rt -o merged.rt`（以本机用法为准） | **合并多张表** | 减少文件数、便于管理 |
| **`rt2rtc`** | `rt2rtc *.rt` | `.rt`（文本）→ `.rtc`（压缩二进制） | **显著省空间、加载更快** |
| **`rtc2rt`** | `rtc2rt *.rtc` | `.rtc` → `.rt` | 需要兼容旧工具或想直接看文本时 |

**`rtsort` 是必做步骤**——官方工作流里，`rtgen` 之后必须 `rtsort`，否则 `rcrack` 会给出 `Warning: ... table is not sorted` 并**无法正常命中**。

---

## 5. 实战演练

> **环境声明**：全部使用**你自己造的哈希或 CTF/教学用的公开哈希**。
> - 破解的是**无盐哈希**——这类哈希大多来自**老系统 / 你自己做的测试 / CTF 题目 / 已公开的数据泄露**；
> - **不要**对来自他人系统的哈希做破解（即使是「捡到的」）；
> - **不要**从零生成大表（浪费几天算力）——用**小表做实验**、理解机制即可，真实需求交给 [`hashcat.md`](hashcat.md)。

### 场景 1：从零走一遍「生成 → 排序 → 查表」全链路（小空间）

**目标**：把「时间-内存权衡」亲手跑一遍，并用一个**小空间**让全流程在分钟级完成。

```bash
mkdir -p /tmp/rt-lab && cd /tmp/rt-lab
```

```bash
# ① 先做基准测试，看看生成「md5 loweralpha 1-6」大概要多久
rtgen md5 loweralpha 1 6 0 -bench
```

```console
root@kali:~# rtgen md5 loweralpha 1 6 0 -bench
RainbowCrack 1.8
...
md5_loweralpha#1-6_0  1000x1000  ...
benchmark ... time ...
```

**解读**：`-bench` 只测速不落盘。**它的意义是让你在「花几小时生成」之前，先知道要花多久**。

```bash
# ② 为了教学，用一个「极小」的表（numeric 1-4，几秒完成）
rtgen md5 numeric 1 4 0 1000 1000 0
ls -l *.rt
```

```console
-rw-r--r-- 1 root root  ...  md5_numeric#1-4_0_1000x1000_0.rt
```

```bash
# ③ 排序（必做！）
rtsort .
rcrack . -h 81dc9bdb52d04dc20036dbd8313ed055      # md5("1234")
```

```console
81dc9bdb52d04dc20036dbd8313ed055  md5  1234
```

**解读（这条链回答了「为什么快」）**：

| 步骤 | 耗时 | 说明 |
|------|------|------|
| `rtgen` | 几秒（空间极小） | **一次性成本** |
| `rtsort` | 极短 | 一次性成本 |
| `rcrack` | **毫秒级** | **每次查询的成本** ← 这就是「预计算」的收益 |

```bash
# ④ 转成 .rtc（压缩二进制），看体积与加载速度的差别
rt2rtc ./*.rt
ls -lh *.rt *.rtc
rcrack . -h 81dc9bdb52d04dc20036dbd8313ed055      # 用 .rtc 也能查（rcrack 自动识别）
```

**解读**：`.rtc` 是压缩后的二进制格式，**体积更小、加载更快**。生产环境常用 `.rtc` 分发。

**⑤ 故意制造「不命中」，理解「参数必须匹配」**

```bash
# 目标哈希是 md5("password")，但我们的表只覆盖「纯数字 1-4 位」
rcrack . -h 5f4dcc3b5aa765d61d8327deb882cf99
```

```console
# 无任何命中输出（搜索完成但未找到）
```

**解读**：**这就是彩虹表最常见的「静默失败」**——不是工具出错，而是**表里没有这个空间的口令**。所以：

| 表覆盖 | 能查到的口令 |
|--------|--------------|
| `md5(numeric, 1-4)` | `1` ~ `9999` |
| `md5(loweralpha, 1-6)` | `a` ~ `zzzzzz` |
| `md5(loweralpha, 1-7)` | 再加上 7 位小写 |
| …… | **字典之外的一概查不到** |

**表格要「对得上」才能用**：

```
rtgen 参数                                   ┐
  hash_algorithm = md5                       │
  charset        = numeric                   ├─ 必须与目标哈希「在同一个空间」
  len_min/max    = 1-4                       │
  table_index    = 0                         ┘

如果目标是 NTLM 哈希 → 必须用 rtgen ntlm ... 生成的表
```

### 场景 2：把整个「参数空间」量化——`-bench` + 空间计算

**2a. 先算空间大小（决定可行性）**

```bash
# 纯数字 1-8 位的空间
python3 -c "
cs=10
print('numeric 1-8:', sum(cs**i for i in range(1,9)))
# 小写字母 1-7 位
cs=26
print('loweralpha 1-7:', sum(cs**i for i in range(1,8)))
# 大小写+数字 1-8 位
cs=62
print('alphanum 1-8:', sum(cs**i for i in range(1,9)))
"
```

```console
numeric 1-8:   111111110
loweralpha 1-7: 8353082582
alphanum 1-8:   221919451578090
```

**2b. 用 `-bench` 把「空间」换算成「时间」**

```bash
rtgen md5 numeric 1 8 0 -bench
rtgen md5 loweralpha 1 7 0 -bench
```

**解读（工程判断表）**：

| 目标空间 | 大小 | 现实可行性 |
|----------|------|------------|
| `md5(numeric, 1-8)` | 1.1 × 10⁸ | **可行**（小时级 + 几十 GB 表） |
| `md5(loweralpha, 1-7)` | 8.4 × 10⁹ | **勉强**（天级 + 数百 GB） |
| `md5(alphanum, 1-8)` | 2.2 × 10¹⁴ | **不可行**（放弃，改 hashcat + 规则） |

**结论**：**彩虹表只在「口令空间小且固定」时可行**——这也是为什么它的现实用途集中在 **LM/NTLM 的短口令** 和 **纯数字/短小写** 场景。

```bash
# 清理大表，别占磁盘
rm -f /tmp/rt-lab/*.rt /tmp/rt-lab/*.rtc
```

### 场景 3：与 hashcat 对比 + 「什么时候不该用彩虹表」

**3a. 同一个无盐 MD5：彩虹表 vs hashcat**

```bash
# 目标：md5("1234")（场景 1 已用彩虹表破解）
# 换 hashcat 用「纯数字掩码」暴力（见 04-口令攻击/hashcat.md）
echo -n '1234' | md5sum     # 确认目标哈希
echo '81dc9bdb52d04dc20036dbd8313ed055' > /tmp/md5.txt
# 掩码 ?d?d?d?d = 4 位纯数字
hashcat -m 0 /tmp/md5.txt -a 3 '?d?d?d?d' --force --potfile-disable
```

**对比（这才是现实中的选择依据）**：

| 维度 | 彩虹表 + rcrack | **hashcat（GPU）** |
|------|-----------------|---------------------|
| **首次成本** | 生成要数小时~数天 | **0**（实时算） |
| **重复成本** | **毫秒** | 每次都要重算（但 GPU 极快） |
| **存储** | **GB ~ TB** | 无 |
| **覆盖调整** | 要重新生成 | **改掩码/字典即可** |
| **带盐哈希** | ❌ 不可行 | ✅ 可行 |
| **现代算法** | ❌ | ✅（bcrypt/PBKDF2…） |
| **综合结论** | 只在「**固定小空间 + 反复破解**」时占优 | **绝大多数场景的首选** |

**3b. 什么时候「确实」值得彩虹表**

```text
✅ 值得：
   - 你是 Windows 域审计方，要反复破解大量「无盐 LM/NTLM」且口令都在 7-8 位以内
     （历史上 ophcrack + 预置表就是这个场景）
   - 你需要给「同一批固定哈希空间」做高频查询（如教学演示、CTF 平台）
   - 你手头已有现成的预置表（直接下载下来用，省掉生成）

❌ 不值得：
   - 目标是加盐哈希 / bcrypt / PBKDF2
   - 只破解一次，且口令有明确特征（用 hashcat + 规则更灵活）
   - 目标空间大（> 10^9，表会大到不可管理）
```

**3c. 如果真要用——下载预置表而不是自己生成**

```bash
# 上游提供预置表（免费/付费混合）
#   https://project-rainbowcrack.com/table.htm
# 下载后：
mkdir -p /opt/rt-tables && cd /opt/rt-tables
# （把下载的 .rt / .rtc 放进来）
rcrack /opt/rt-tables -l /tmp/ntlm-hashes.txt
```

**解读**：**用预置表是你唯一现实的路径**——自己生成的时间成本远超收益。下载时注意**表的参数（算法/字符集/长度范围/表索引）必须与你的目标哈希匹配**。

**3d. 一个完整的「Windows 口令审计」示意流程**（**只在你拥有/授权的域环境**）

```bash
# ① 拿到 pwdump 格式的哈希（这一步需要域控权限/授权审计工具）
#    格式示例：username:rid:lmhash:ntlmhash:::
cat /tmp/pwdump.txt

# ② 用 rcrack 直接吃 pwdump（-ntlm 会解析出 NTLM 列）
rcrack /opt/rt-tables -ntlm /tmp/pwdump.txt

# ③ 或 -lm 处理 LM 列
rcrack /opt/rt-tables -lm /tmp/pwdump.txt
```

```console
# 命中时会输出：<哈希>  ntlm  <明文>
```

**注意**：pwdump 格式**极其敏感**（含全网账号哈希）。**必须按核心凭据数据保护**：加密存储、限制访问、用后销毁、绝不外发。

---

## 6. 输出解读

### 6.1 `rcrack` 输出的三段结构

```console
root@kali:~# rcrack /tmp/rt-demo -h 81dc9bdb52d04dc20036dbd8313ed055
RainbowCrack 1.8                                          ← ① 横幅
Copyright 2020 RainbowCrack Project. All rights reserved.
http://project-rainbowcrack.com/

1 hash(es) loaded.                                        ← ② 加载的哈希数
Warning: table md5_numeric#1-4_0_1000x1000_0.rt:          ← ③ 表加载信息/警告
         1000 chains, 1000 chain length
searching for 1 hash(es)...
81dc9bdb52d04dc20036dbd8313ed055  md5  1234              ← ④ 命中行（关键输出）
```

| 位置 | 内容 | 含义 |
|------|------|------|
| ② | `N hash(es) loaded.` | 输入了多少个哈希（`-l`/`-lm`/`-ntlm` 时尤其要核对） |
| ③ | `table ...: N chains, M chain length` | **表被加载了**；**这里能直接看出表的参数**（字符集/长度/链数/链长） |
| ③ | `Warning: ... table is not sorted` | **忘了 `rtsort`** → 会**无法命中** |
| ④ | `<hash>  <算法>  <明文>` | **命中！** 这正是要写进报告的结果 |
| —— | **没有 ④ 这一行** | **未命中**（该表覆盖不到这个口令） |

### 6.2 关键判据速查

| 现象 | 判断 | 下一步 |
|------|------|--------|
| 有 `<hash>  md5  <明文>` 行 | **命中** | 记录明文；评估口令强度 |
| 只有 `N hash(es) loaded.`，没有命中行 | **未命中** | 换表/换空间；**不是工具出错** |
| `Warning: table ... is not sorted` | **忘了 `rtsort`** | 排序后重跑 |
| 加载的哈希数和输入不符 | pwdump 解析问题（列格式不对） | 检查 pwdump 格式（`username:rid:lm:ntlm:::`） |
| 表根本没被加载（③ 没有 table 行） | **路径错了**，或目录里没有 `.rt`/`.rtc` | `ls` 确认路径与文件扩展名 |
| 表加载了但命中率为 0 | **参数空间不匹配**（算法/字符集/长度） | 对比 ③ 里的表参数与目标哈希类型 |
| 查询很慢 | 表太多/链太长 | 用更小的表、或用 `.rtc`；或换 hashcat |

### 6.3 怎么把结果写进报告

| 结果 | 报告写法 |
|------|----------|
| 命中 | 「哈希 `xxxx` 对应口令 `1234`（**8 位以内纯数字**）→ **口令强度严重不足**，且若该口令被复用，风险进一步放大」 |
| 未命中 | 「用 N 张表（覆盖字符集 C、长度 1-M）未命中 → **口令落在该空间之外**；**不等于不可破解**，需进一步评估」 |
| 加盐 | 「目标使用加盐哈希，**预计算攻击（彩虹表）不适用** → 这是正确做法」 |
| 用了弱哈希 | 「系统使用**无盐 MD5** 存储口令 → **应改为 bcrypt/scrypt/Argon2**」（这是比「破出了口令」更重要的整改项） |

---

## 7. 与其他工具配合

```
   ① 拿到哈希
      ├─ 本地：/etc/shadow（见 john.md）、Windows 域控 pwdump/impacket（见 ../08-后渗透/）
      ├─ 抓包/注入：见 03-Web应用/、06-漏洞利用/
      └─ 识别类型：hash-identifier（见 hash-identifier.md）
                        │
   ② 判断「能不能用彩虹表」
      ├─ 有盐 / bcrypt / PBKDF2  → ❌ 直接换 hashcat
      └─ 无盐 LM/NTLM/MD5/SHA1   → ⚠️ 可选
                        │
   ③ 破解（按性价比排序）
      ├─ hashcat -m <模式>          ← **首选**，见 hashcat.md
      ├─ john --format=<模式>       ← CPU 备选，见 john.md
      ├─ rcrack + 预置表            ← 本文（固定小空间 + 反复破解）
      └─ ophcrack（GUI + LM/NTLM）  ← 见 ophcrack.md
                        │
   ④ 用词表 / 规则提高命中率
      wordlists.md（rockyou） / crunch.md（规则生成） / cewl.md（从站点抓词）
                        │
   ⑤ 口令复用检查
      拿到明文后，检查是否复用到其他系统（**仅在授权范围内**）
                        │
   ⑥ 报告
      「弱哈希算法 + 弱口令 + 口令复用」三条一起写 ← 这才是完整的整改建议
```

**彩虹表与其它工具的分工**：

| 工具 | 什么时候用它 |
|------|--------------|
| **rcrack（本文）** | 无盐哈希 + 固定小空间 + **要反复查**（或已有预置表） |
| [`hashcat.md`](hashcat.md) | **默认选择**：GPU、支持加盐/现代算法、掩码/规则/字典全能 |
| [`john.md`](john.md) | 只有 CPU，或需要 John 的自动格式识别与规则集 |
| [`ophcrack.md`](ophcrack.md) | Windows LM/NTLM + 想要 GUI + 现成表 |
| [`hash-identifier.md`](hash-identifier.md) | **第一步**：先判断这是什么哈希、有没有盐 |
| [`wordlists.md`](wordlists.md)、[`crunch.md`](crunch.md)、[`cewl.md`](cewl.md) | 准备候选口令（比彩虹表更灵活） |

**一条重要的经验**：**先识别「有没有盐」再决定工具**。加盐的直接放弃彩虹表，省下几天时间。

---

## 8. 常见坑与排错

| 报错/现象 | 原因 | 解决 |
|-----------|------|------|
| `Warning: table ... is not sorted` | **忘了 `rtsort`** | `rtsort .` 后再 `rcrack` |
| 表加载了但**永远不命中** | **参数空间不匹配**：算法/字符集/长度范围/表索引对不上 | 对比 `rcrack` 输出里的表名（`md5_numeric#1-4_0_1000x1000_0.rt` 里的每一段都有意义）与目标哈希 |
| 给 md5 表喂 NTLM 哈希 | 算法不同 | 用 `rtgen ntlm ...` 生成的表 |
| 表目录里明明有文件却**没加载** | 扩展名不是 `.rt`/`.rtc`；或路径写错 | `ls -l <path>/*.rt*` 确认 |
| `rtgen` 跑了几天还没完 | **空间太大** | Ctrl-C；**先 `-bench` 估时间**；换预置表或 hashcat |
| 磁盘写满 | 表文件极大 | 生成前预留空间；分成 `part_index` 分片；用 `.rtc` |
| `rtgen` 报参数错误 | 位置参数顺序写错（8 个参数必须按顺序） | 严格按 `rtgen 算法 字符集 最小长 最大长 表索引 链长 链数 分片索引` |
| `rcrack` 把 `-h` 当成了表文件 | **选项顺序**：路径必须在选项前 | `rcrack <path> -h <hash>`（照官方用法写） |
| 加盐哈希查不到（如 `md5(salt.pass)`） | **彩虹表对加盐哈希无效** | 放弃；用 hashcat 的 `-m 10`（md5($pass.$salt)）等专门模式逐 salt 算 |
| bcrypt/scrypt/Argon2 查不到 | **rcrack 不支持这些算法** | 用 hashcat（`-m 3200` 等） |
| 目标哈希长度 > 表覆盖长度 | 口令比表覆盖的长 | 用覆盖更长的表；或换 hashcat |
| pwdump 解析失败/数量不对 | pwdump 格式不正确 | 用标准格式 `user:rid:lmhash:ntlmhash:::`；或先用 `-l` 手工提取哈希列表 |
| 破解「成功」但明文看着不对（LM） | **LM 会把口令转大写并截断为 7 字节** | LM 的结果是**大写**的；且 > 7 位口令会被拆成两段（表只覆盖一段） |
| 表文件来自网上，加载报错 | 文件损坏/版本不兼容 | 校验下载完整性；用项目推荐的表 |
| 内存不足 | 加载了过多/过大的表 | 分批查；用 `.rtc`；减少目录里的表数量 |
| 误以为「未命中 = 不可破解」 | **逻辑错误** | 改成「不在该表覆盖空间内」；并给出量化结论 |

---

## 9. 防御视角（蓝队 / 开发）

彩虹表的存在，**直接决定了「口令该怎么存储」**。

| 风险 | 加固手段 | 说明 |
|------|----------|------|
| **无盐哈希**（MD5/SHA1/SHA256） | **改为加盐 + 慢哈希**：bcrypt / scrypt / Argon2id | **加盐让彩虹表彻底失效**（每个 salt 都要一套表） |
| **快哈希**（MD5/SHA1、单次 SHA256） | **提高计算成本**：Argon2id（可调内存/时间/并行度） | 让每次尝试都变贵，预计算与暴力都不划算 |
| **无盐 NTLM**（Windows） | 启用 Kerberos、**禁止 NTLM**；提升口令强度 | NTLM 的无盐特性使其历史上是彩虹表的主要目标 |
| **LM 哈希** | **彻底禁用 LM**（组策略/注册表） | LM 无盐 + 大写 + 7 位截断 = 最差设计 |
| **弱口令** | **长度 ≥ 12**；非常见词；禁止与组织名/手机号相关 | 让口令**落到表的覆盖空间之外** |
| **口令复用** | 唯一口令 + 密码管理器 + MFA | 一处泄露不扩散 |
| **哈希泄露面** | 最小权限、限制 `NTDS.dit`/`/etc/shadow` 访问；审计读取 | 拿不到哈希就无从破解 |
| **彩虹表检测** | 难以在网络层检测（离线攻击） | **重点在「预防哈希泄露」与「强化存储」** |

**蓝队的五条硬建议**：

1. **一律使用加盐 + 慢哈希**（bcrypt/scrypt/Argon2id）——这是**让彩虹表直接失效**的唯一手段；
2. **Windows 环境禁用 LM**，并尽量禁用 NTLM（迁移到 Kerberos）；
3. **口令长度 ≥ 12、不复用、非常见词**——把口令推出任何预计算表的覆盖范围；
4. **保护哈希本体**：`/etc/shadow`、`NTDS.dit`、pwdump 输出都是**核心凭据**，需加密、限权、审计；
5. **定期用授权的口令强度审计**（hashcat + 规则，而不是彩虹表）检查组织内弱口令，并**推动整改而非公开名单**。

**关于「彩虹表 vs 现代存储」的一句话总结**：

> **彩虹表之所以今天不再是主要威胁，不是因为它弱，而是因为「加盐 + 慢哈希」这个组合在成本上把它彻底压死了。** 这正好说明：**哈希存储方式的每一个设计决定（加盐、迭代次数、内存开销）都是在针对某类攻击。**

---

## 10. 参考

- Kali 工具页（含 `rcrack -h`、`rtgen -h` 原文）：<https://www.kali.org/tools/rainbowcrack/>
- 上游项目（含**预置表下载**与算法说明）：<https://project-rainbowcrack.com/index.htm>
- 预置表列表：<https://project-rainbowcrack.com/table.htm>
- Kali 包跟踪：<https://pkg.kali.org/pkg/rainbowcrack>
- 本地命令：`rcrack -h`、`rtgen -h`、`rtsort`、`rtmerge`、`rt2rtc`、`rtc2rt`
- 原始论文（时间-内存权衡与彩虹表）：Martin Hellman, *A Cryptanalytic Time-Memory Trade-Off* (1980)；Philippe Oechslin, *Making a Faster Cryptanalytic Time-Memory Trade-Off* (2003)
- 配套教程：[`hashcat.md`](hashcat.md)、[`john.md`](john.md)、[`ophcrack.md`](ophcrack.md)、[`hash-identifier.md`](hash-identifier.md)、[`wordlists.md`](wordlists.md)、[`crunch.md`](crunch.md)

## ⚠️ 法律与伦理

彩虹表本身只是一堆**预计算数据**，但围绕它有明确的法律边界：

- **哈希即凭据**：口令哈希（尤其 NTLM/shadow 条目）**可以直接用于横向移动与身份冒充**（Pass-the-Hash）。处理哈希等同于处理**核心凭据**：

  - 《网络安全法》第 27 条：不得非法侵入他人网络、**窃取网络数据**；
  - 《刑法》第 285 条：**非法获取计算机信息系统数据**；
  - 《个人信息保护法》《数据安全法》：凭据常与个人身份绑定，属敏感个人信息。

- **未经授权获取/破解哈希是违法的**——「哈希是密文所以不算数据」是错误认识；
- **把破解出的明文用于登录任何系统**，即构成未授权访问；
- **生成/分发彩虹表**本身通常合法（是数学产物），但**用它攻击他人系统**不合法；
- **CTF / 教学 / 自有系统**是合法场景；**企业口令审计**必须**有书面授权 + 明确范围 + 数据保密约定**。

**必须遵守**：

1. **只破解你有权处理的哈希**：自己的系统、CTF 题目、明确授权范围内的目标；
2. **哈希与破解结果按核心凭据保护**：加密存储、最小访问、限定保存期、**用后销毁**；
3. **绝不使用破解出的口令访问任何系统**（包括「只是验证一下」也不行——验证靠离线比对即可）；
4. **不在公开渠道发布** pwdump 文件、shadow 内容、真实口令列表；
5. **报告脱敏**：写「口令强度不足」和「哈希算法过弱」，而不是把完整口令列表贴出去；
6. 组织内的口令审计必须**事先告知并取得授权**，结果只用于**推动整改**，不得用于考核或惩罚性用途。
