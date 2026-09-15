# rainbowcrack

> Rainbow table password cracker RainbowCrack is a general propose implementation of Philippe Oechslin’s faster time-memory trade-off technique. It crack hashes with rainbow tables. RainbowCrack uses time-memory tradeoff algorithm to crack h…

> **功能分类**：口令攻击 ｜ **Kali 包**：`rainbowcrack` ｜ **官方文档**：<https://www.kali.org/tools/rainbowcrack/>

## 1. 安装

```bash
sudo apt update
sudo apt install rainbowcrack
```

| 项目 | 内容 |
|------|------|
| 版本 | 1.8 |
| 架构 | amd64 |
| 可执行命令 | `rainbowcrack`、`rcrack`、`rt2rtc`、`rtc2rt`、`rtgen`、`rtmerge`、`rtsort` |
| 依赖 | `libc6`、`libgcc-s1`、`libstdc++6`、`rcrack` |
| 安装体积 | 497 KB |
| 官网 | <https://project-rainbowcrack.com/index.htm> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/rainbowcrack> |
| 包追踪 | <https://pkg.kali.org/pkg/rainbowcrack> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
rainbowcrack -h          # 查看用法
man rainbowcrack         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 7 个可执行命令，下面是官方页面内嵌的帮助原文。

### `rcrack`

官方给出的调用示例：`rcrack -h`

```text
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

### `rt2rtc`

官方给出的调用示例：`rt2rtc -h`

```text
root@kali:~# rt2rtc -h
no rainbow table found
```

### `rtc2rt`

官方给出的调用示例：`rtc2rt -h`

```text
root@kali:~# rtc2rt -h
no rainbow table found
```

### `rtgen`

官方给出的调用示例：`rtgen -h`

```text
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

## 4. 实践清单

按顺序做完这五步，就能把工具从「装上」推进到「会用」：

- [ ] **1.** **装好并确认版本** —— `sudo apt install rainbowcrack`，再执行 `rainbowcrack --version` 2>/dev/null || `rainbowcrack -V`
- [ ] **2.** **读官方帮助** —— `rainbowcrack -h`，需要细节时 `man rainbowcrack`
- [ ] **3.** **在自有靶场跑最小用例** —— 用 `rainbowcrack -h` 里最简单的那个子命令试一次
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/rainbowcrack/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- **精讲教程**（含原理、参数详解、靶场实操与输出解读）：[rainbowcrack](../../tools/tutorials/04-口令攻击/rainbowcrack.md)
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/credential-access.md`](../../tools/by-attack/credential-access.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/rainbowcrack/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/rainbowcrack/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
