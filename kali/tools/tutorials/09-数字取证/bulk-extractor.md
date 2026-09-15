# bulk_extractor（无文件系统解析的特征提取）

> **一句话**：**不解析文件系统、不看文件边界**，直接把整块镜像（或内存转储）当作字节流，用正则和特征扫描器把邮箱、URL、IP、信用卡号、密钥、EXIF、网络包、NTFS 元数据等**一次性全捞出来**。
> **分类**：数字取证 / 文件雕刻与特征提取 ｜ **Kali 包**：`bulk-extractor`（命令 `bulk_extractor`）｜ **官方文档**：<https://github.com/simsong/bulk_extractor> ｜ `man bulk_extractor`

---

## 1. 它解决什么问题

传统取证流程是「解析文件系统 → 打开每个文件 → 看内容」。但有三类内容用这个流程**捞不到**：

1. **已删除且文件系统元数据全毁**的数据（inode 没了、目录项没了，但数据块还在）；
2. **藏在未分配空间/松弛空间（slack space）/内存页**里的碎片（一个邮箱可能横跨两个文件、两页内存）；
3. **跨文件的信息**（比如整个镜像里散落的所有 URL 与 IP —— 你想知道「这台机器联系过哪些外部地址」）。

bulk_extractor 的思路是**彻底放弃「文件」这个概念**：

| 传统方式 | bulk_extractor |
|----------|----------------|
| 解析文件系统 → 打开文件 → 读内容 | **直接扫描字节流**，命中特征就记录（偏移 + 上下文） |
| 一个邮箱必须完整地待在一个文件里 | 邮箱可以**横跨块边界**/散落在无用空间 |
| 需要先恢复文件才能分析 | **不需要恢复文件**，直接出结果 |
| 输出是「文件」 | 输出是「**特征文件 + 直方图**」 |

**它的核心竞争力是「快」和「全」**：C++ 实现、多线程、扫描速度可到 **1 GB/s 量级**（SSD + 多核），比逐个文件打开快一个数量级。

**它不做什么**：不重建目录树、不恢复文件名、不判断文件类型归属。**要知道「这个邮箱属于哪个文件」，仍要用 [`sleuthkit.md`](sleuthkit.md) 的 `ifind`/`icat`**。

对比同类：

| 工具 | 输入假设 | 输出 | 互补关系 |
|------|----------|------|----------|
| **bulk_extractor** | 无（纯字节流） | 特征清单 + 直方图 | **先跑它**，快速摸清「有什么」 |
| **`foremost`/`scalpel`** | 无（靠文件头尾） | **恢复出的文件** | 需要**拿到文件本体**时用；见 [`foremost.md`](foremost.md)、[`scalpel.md`](scalpel.md) |
| **`sleuthkit`** | 需要完好的文件系统元数据 | 目录树 + inode + 内容 | 精确定位与归属；见 [`sleuthkit.md`](sleuthkit.md) |
| **`binwalk`** | 二进制中的嵌套结构 | 内嵌文件/熵图 | 固件场景；见 [`binwalk.md`](binwalk.md) |
| **`strings` + `grep`** | 无 | 原始文本行 | bulk_extractor 的**专业化+并行+去重**版本 |

**最佳协同顺序**：`bulk_extractor`（30 分钟摸清全貌）→ `sleuthkit`（精确定位归属）→ `foremost`/`scalpel`（抢救文件本体）→ `exiftool`（元数据细节）。

---

## 2. 工作原理

```
镜像 / 内存转储 / 目录
        │
        ▼
┌─────────────────────────────────────────────────────┐
│ Phase 1：多线程扫描（默认 6 线程，可调）               │
│   把输入切成页（默认 16 MiB）+ 留重叠边界（4 MiB）      │
│   ┌───────────────────────────────────────────────┐ │
│   │ 扫描器（Scanner）并行运行：                     │ │
│   │  accts  aes  base64  elf  email  evtx  exif     │ │
│   │  facebook  find  gps  gzip  httplogs  json      │ │
│   │  kml_carved  msxml  net  ntfsindx ntfslogfile   │ │
│   │  ntfsmft ntfsusn pdf  rar  sqlite  utmp         │ │
│   │  vcard_carved  vin  windirs winlnk winpe        │ │
│   │  winprefetch  zip                              │ │
│   └───────────────────────────────────────────────┘ │
│   每个命中记录：偏移、内容、±context_window 字节上下文  │
└─────────────────────────────────────────────────────┘
        │
        ▼
┌─────────────────────────────────────────────────────┐
│ Phase 2/3：停止扫描器、生成直方图                      │
│   输出目录（-o）里得到：                                │
│     email.txt   url.txt   ip.txt   ccn.txt            │
│     domain.txt  telephone.txt  aes_keys.txt ...       │
│     *_histogram.txt（按出现频次排序）                  │
│     report.xml（全部结果的结构化汇总）                  │
└─────────────────────────────────────────────────────┘
```

**关键概念**：

- **页（page）与边界重叠（margin）**：把大镜像切成 `-G pagesize`（默认 16 MiB）大小的页并行处理，页之间保留 `-g marginsize`（默认 4 MiB）的重叠区域 —— 这样**横跨页边界**的特征照样能被发现（例如一个 URL 跨在两页之间）。
- **上下文窗口（context window）**：每命中一条，记录命中位置前后 `-C`（默认 16）字节，输出里就是 `偏移<TAB>特征<TAB>上下文` 的形式——**上下文常常比特征本身更有价值**（能看到邮箱出现在哪个字段里）。
- **直方图**：同一特征出现多次时会被计数。**出现次数最高的往往最重要**（例如某台 C2 服务器被访问了 500 次）。
- **不解析文件系统**：所以**对加密容器（LUKS/BitLocker）内部的明文无能为力**——加密数据就是高熵噪声。但对**未加密的镜像**，连「文件系统已损坏」的镜像也能扫。**内存转储是它的最佳输入之一**（内存里没有文件系统，但有大量明文）。

---

## 3. 安装与快速上手

```bash
sudo apt update
sudo apt install bulk-extractor
command -v bulk_extractor
```

```console
$ bulk_extractor -V
bulk_extractor version 2.1.1: A high-performance flexible digital forensics program.
```

最短用法（**官方文档的经典示例**）：

```bash
bulk_extractor -o bulk-out xp-laptop-2005-07-04-1430.img
```

```console
bulk_extractor version: 2.1.1
Hostname: kali
Input file: xp-laptop-2005-07-04-1430.img
Output directory: bulk-out
Disk Size: 536715264
Threads: 1
Phase 1.
13:02:46 Offset 0MB (0.00%) Done in n/a at 13:02:45
13:03:39 Offset 67MB (12.50%) Done in  0:06:14 at 13:09:53
...
All Threads Finished!
Producer time spent waiting: 335.984 sec.
Average consumer time spent waiting: 0.143353 sec.
*******************************************
** bulk_extractor is probably CPU bound. **
**    Run on a computer with more cores  **
**      to get better performance.       **
*******************************************
Phase 2. Shutting down scanners
Phase 3. Creating Histograms
   ccn histogram...   ccn_track2 histogram...   domain histogram...
   email histogram...   ether histogram...   find histogram...
   ip histogram...   tcp histogram...   telephone histogram...
   url histogram...   url microsoft-live...   url services...
   url facebook-address...   url facebook-id...   url searches...

Elapsed time: 378.5 sec.
Overall performance: 1.418 MBytes/sec.
Total email features found: 899
```

**看结果**（这一步比扫描本身更重要）：

```bash
ls bulk-out/ | head -30
```

```console
aes_keys.txt          domain_histogram.txt   telephone.txt
ccn.txt               email.txt              url.txt
ccn_histogram.txt     ip.txt                 url_histogram.txt
report.xml            email_histogram.txt    ...
```

```bash
head -5 bulk-out/email.txt
wc -l bulk-out/email.txt bulk-out/url.txt bulk-out/ip.txt
```

```console
899 bulk-out/email.txt
2140 bulk-out/url.txt
355 bulk-out/ip.txt
```

---

## 4. 核心参数详解

以下为 `bulk_extractor -h` 的**真实参数**（按用途分组）。

### 4.1 必用基础参数

| 参数 | 作用 | 使用建议 |
|------|------|----------|
| `-o, --outdir <dir>` | **输出目录（必填）** | 建议与镜像同一数据盘；保留所有特征文件 |
| `-Z, --zap` | 开始前**递归清空**输出目录 | 重复实验时方便（**注意会删掉目录内容**） |
| `-q, --quit` | 不输出状态与性能信息 | 脚本化时用 |
| `-j, --threads <n>` | 线程数（默认 6） | **调到 CPU 核数**，提速最明显 |
| `-G, --pagesize <n>` | 页大小（默认 16777216 = 16 MiB） | 内存受限时调小 |
| `-g, --marginsize <n>` | 页边界重叠（默认 4194304 = 4 MiB） | 一般不动；调小会漏跨页特征 |
| `-C, --context_window <n>` | 上下文窗口字节数（默认 16） | 调大（如 64）能看到更多字段语境 |
| `-V, --version` | 版本 | —— |
| `-h, --help` | 帮助（含全部扫描器与选项） | **`-h` 输出较长，建议重定向到文件慢慢看** |

### 4.2 扫描器控制（哪些特征要扫）

| 参数 | 作用 | 使用建议 |
|------|------|----------|
| `-e, --enable <scanner>` | 启用某个扫描器（可重复） | 默认**禁用**的扫描器有：`base16`、`hiberfile`、`outlook`、`wordlist`、`xor` |
| `-x, --disable <scanner>` | 禁用某个扫描器（可重复） | 去掉不需要的以提速 |
| `-E, --enable_exclusive <scanner>` | 只启用指定扫描器 | 等价 `-x all -E <scanner>`：**定向扫描，最快** |
| `-H, --info_scanners` | 列出所有扫描器及其**可设选项** | **上手第一步：先看这个** |
| `-S, --set <name=value>` | 设置扫描器/全局选项 | 如 `-S hash_alg=sha1`、`-S word_min=6` |
| `-f, --find <pattern>` | 自定义字符串搜索（可重复） | 找特定关键字（如内部项目代号） |
| `-F, --find_file <file>` | 从文件读入多个搜索模式 | 批量关键字 |
| `-r, --alert_list <file>` | 命中即告警的模式列表 | 高优先级关键词（如「机密」） |
| `-w, --stop_list <file>` | 排除列表（命中则不输出） | 去掉噪音（如通用域名） |

### 4.3 范围与递归

| 参数 | 作用 | 使用建议 |
|------|------|----------|
| `-Y, --scan <start>[-end]` | 只扫描指定区域 | 定向分析某个分区/区块 |
| `-A, --offset_add <n>` | 给所有偏移**加上基数** | 扫描分区切片时，让偏移与整盘对齐 |
| `-p, --path <path>[:len][/h][/r]` | 打印指定路径的内容 | 定向提取 |
| `-R, --recurse` | 把输入当作**目录**递归扫描 | 批量处理一堆文件（如雕刻输出的目录） |
| `-s, --sampling <frac[:passes]>` | 随机采样 | 巨大镜像的快速摸底（**可能有漏，慎用于取证结论**） |
| `-z, --page_start <n>` | 从第 N 页开始 | 断点续扫 |
| `-M, --max_depth <n>` | 最大递归深度（默认 12） | `-R` 时用 |
| `--max_minute_wait <n>` | 等待线程结束的最长分钟数（默认 60） | —— |
| `-0, --no_notify` | 关闭实时通知 | 脚本化 |
| `-b, --banner_file <file>` | 在特征文件顶部加入说明行 | 多案件并行时区分来源 |

### 4.4 值得调的扫描器选项（用 `-S` 设置）

| 选项 | 默认 | 作用 |
|------|------|------|
| `notify_rate=1` | 1 秒 | 状态刷新频率 |
| `hash_alg=sha1` | sha1 | 所有哈希计算使用的算法 |
| `report_read_errors=1` | 1 | 报告读错误（坏盘必开） |
| `carve_net_memory=0` | 0 | **从内存转储中雕刻网络包**（内存取证很有用） |
| `min_carve_packet_bytes=40` | 40 | 最小网络包长度 |
| `min_phone_digits=7` | 7 | 电话号码最小位数（**跨国场景要调**） |
| `ssn_mode=0` | 0 | SSN 匹配严格度 |
| `scan_aes_128/192/256` | 1/0/1 | 是否扫各长度 AES 密钥 |
| `word_min` / `word_max` | 6 / 16 | **wordlist 扫描器**的词长（需 `-e wordlist`） |
| `strings=0` | 0 | wordlist 扫描器改为提取 strings |
| `exif_debug=0` | 0 | EXIF 解析调试 |
| `jpeg_carve_mode=n` | 依扫描器 | 0=不雕刻 1=雕 2=全雕（**雕刻模式影响输出体积**） |

> **提示**：`-H` 会列出**每个扫描器支持的所有 `-S` 选项**——**排错和调优时先看 `-H`**。

---

## 5. 实战演练

> **环境声明**：全部使用**自建实验镜像**（生成方法见 [`dcfldd.md` 场景 1](dcfldd.md#场景-1造一个作案现场先有可练的镜像)）或**公开发布的取证样本**（**NIST CFReDS** 提供了含邮箱/文档/网络痕迹的经典练习镜像，如 `xp-laptop-2005-07-04-1430.img`）。
> **禁止**对未经授权的镜像、设备或内存转储执行分析。

### 场景 1：对整盘镜像做一次「全景摸底」（第一次使用）

```bash
# ① 先看看有哪些扫描器可用（别跳过这步）
bulk_extractor -H > /evidence/scanners.txt
grep -c '^ *-x' /evidence/scanners.txt
```

```console
35
```

```console
# 看默认禁用哪些（这些需要手动 -e 打开）
grep -A3 "These scanners disabled" /evidence/scanners.txt
```

```console
These scanners disabled; enable with -e:
   -e base16 - enable scanner base16
   -e hiberfile - enable scanner hiberfile
   -e outlook - enable scanner outlook
   -e wordlist - enable scanner wordlist
   -e xor - enable scanner xor
```

```bash
# ② 全量扫描（线程数按 CPU 核数）
nproc
bulk_extractor -o /evidence/bulk-out -j 8 /evidence/disk.img
```

```console
bulk_extractor version: 2.1.1
Input file: /evidence/disk.img
Output directory: /evidence/bulk-out
Disk Size: 268435456
Threads: 8
Phase 1.
...
Phase 3. Creating Histograms
   ccn histogram...   domain histogram...   email histogram...
   ip histogram...   telephone histogram...   url histogram...
Elapsed time: 21.3 sec.
Overall performance: 12.6 MBytes/sec.
```

```bash
# ③ 看产出（先按「体积/条数」排序，找信息量大的）
ls -lS /evidence/bulk-out/*.txt | head -15
wc -l /evidence/bulk-out/email.txt /evidence/bulk-out/url.txt /evidence/bulk-out/ip.txt
```

```console
   412 /evidence/bulk-out/email.txt
  1830 /evidence/bulk-out/url.txt
   295 /evidence/bulk-out/ip.txt
```

```bash
head -5 /evidence/bulk-out/email.txt
```

```console
67108864	alice@example-lab.local	...From: "Alice" <alice@
6724address	root@lab.local	...MAILTO=root@lab.local
```

**解读（输出格式）**：

```
<偏移>\t<特征>\t<上下文>
```

| 列 | 含义 | 怎么用 |
|----|------|--------|
| 偏移 | 该特征在镜像中的**字节偏移** | 可反查归属（`ifind -d <block>`，见 [`sleuthkit.md`](sleuthkit.md)） |
| 特征 | 提取到的内容（邮箱/URL/IP…） | 证据主体 |
| 上下文 | 前后 16 字节 | **常能看出字段语义**（如 `MAILTO=`、`From:`、`password=`） |

```bash
# ④ 直方图：出现最多的往往最重要
head -20 /evidence/bulk-out/domain_histogram.txt
```

```console
  412  example-lab.local
   88  mail.example-lab.local
   31  updates.example-lab.local
    5  telemetry.vendor.com        ← 少数但可疑，值得追
```

**解读**：直方图是 bulk_extractor 最独特的能力——**一眼看出「这台机器和谁通信最多」**。异常长尾（出现 1–5 次的外域）常是 C2 或数据外带目标。

### 场景 2：定向扫描 + 内存转储（实战中最有价值的两招）

**2a. 只扫某类特征（大幅提速）**

```bash
# 只扫邮箱与 URL
bulk_extractor -o /evidence/bulk-email -E email -j 8 /evidence/disk.img
# 再加一个（-e 可重复）
bulk_extractor -o /evidence/bulk-multi -e email -e url -e domain -x all -j 8 /evidence/disk.img
```

```console
Phase 1.
0.00% done at ...
Email features found: 412
URL features found: 1830
```

**2b. 扫内存转储（bulk_extractor 的杀手级场景）**

内存里**没有文件系统**，但有大量明文：进程命令行、网络连接、凭据、剪贴板、密钥。**这正是 bulk_extractor 最擅长的输入**。

```bash
# 假设你有合法的内存转储（自建靶机，用 winpmem / LiME / avml 采集）
ls -lh /evidence/memory.raw
```

```console
-rw-r--r-- 1 root root 8.0G Sep 15 09:00 /evidence/memory.raw
```

```bash
# 打开「从内存雕刻网络包」+ 常规特征扫描
bulk_extractor -o /evidence/bulk-mem -j 8 \
    -S carve_net_memory=1 -S min_carve_packet_bytes=40 \
    /evidence/memory.raw
```

```console
Phase 1.
...
Total email features found: 21
Total url features found: 340
Total domain features found: 96
```

```bash
# 常见的高价值产出
head -10 /evidence/bulk-mem/url.txt
head -10 /evidence/bulk-mem/ip.txt
ls /evidence/bulk-mem/ | grep -i 'pcap\|net'
```

```console
0x1f4a0000	http://10.10.20.5/upload.php	...POST /upload.php HT
0x1f4b2310	http://malicious.example/beacon?id=	...GET /beacon?id=
```

```bash
# 自定义关键字：搜内部项目代号、环境变量、凭据字段
printf 'password\nsecret\nAPI_KEY\nPROJECT_CODENAME\n' > /evidence/keys.txt
bulk_extractor -o /evidence/bulk-keys -j 8 -F /evidence/keys.txt /evidence/memory.raw
```

```console
Elapsed time: 96.4 sec.
```

```bash
grep -i 'API_KEY' /evidence/bulk-keys/*.txt | head
```

```console
0x2a3f10	API_KEY=sk-live-...	...export API_KEY=sk-live-...
```

**解读**：内存取证里，**「找到凭据/密钥」通常比「还原进程结构」更快出成果**。bulk_extractor 用几 MB/s–GB/s 的速度替你完成「先把整块内存里所有像凭据的东西捞出来」这件事。

> **注意**：内存转储是**高度敏感数据**（含他人密码、聊天内容）。仅在授权范围内采集与分析，报告必须脱敏。

### 场景 3：与 TSK / 雕刻工具组合，形成完整链条

**Step 1：bulk_extractor 摸清「有什么」**

```bash
bulk_extractor -o /evidence/bulk-out -j 8 /evidence/disk.img
grep -c . /evidence/bulk-out/url.txt
head -3 /evidence/bulk-out/url_histogram.txt
```

```console
2140
   51  http://192.168.56.102:8080/admin
   12  http://example-lab.local/index.html
```

**解读**：`admin` 接口被访问 51 次，值得追查——**这是线索生成器，不是结论**。

**Step 2：用 TSK 定位「这个 URL 属于哪个文件」**

```bash
# 拿到 bulk_extractor 的偏移 → 换算成块号（块大小见 fsstat）
fsstat -o 2048 /evidence/disk.img | grep -i 'block size'
```

```console
Block Size: 4096
```

```bash
# 偏移 71663616 / 4096 = 17496 → 反查 inode
ifind -o 2048 -f ext4 -d 17496 /evidence/disk.img
```

```console
15
```

```bash
# 看这个 inode 是什么文件
istat -o 2048 /evidence/disk.img 15 | head -12
icat -o 2048 /evidence/disk.img 15 | grep -i admin
```

```console
http://192.168.56.102:8080/admin/login.php
```

**解读**：**bulk_extractor 找到线索 → TSK 完成归属**。这个「偏移 → 块 → inode → 文件」的链条是取证报告里最有说服力的论证方式。

**Step 3：需要文件本体时用雕刻兜底**

```bash
# 导出未分配空间，再交给 foremost/scalpel
blkls -A -o 2048 /evidence/disk.img > /evidence/unallocated.bin
foremost -t jpg,pdf,doc,txt -i /evidence/unallocated.bin -o /evidence/carved
cat /evidence/carved/audit.txt | head
```

```console
Foremost version 1.5.7 by Jesse Kornblum, Kris Kendall, and Nick Mikus
Audit File

Foremost started at Sat Sep 15 11:20:03 2024
Invocation: foremost -t jpg,pdf,doc,txt -i /evidence/unallocated.bin -o /evidence/carved
...
File: /evidence/carved/jpg/00000012.jpg
```

**Step 4：再对雕刻出的文件批量跑 bulk_extractor（递归模式）**

```bash
bulk_extractor -o /evidence/bulk-carved -R -j 8 /evidence/carved
```

```console
Input file: /evidence/carved
Threads: 8
...
Email features found: 64
URL features found: 210
```

**解读**：`-R`（递归目录）让 bulk_extractor 可以直接处理**一个目录树**——非常适合对雕刻产物、解压后的邮件归档做二次扫描。

**Step 5：把元数据落到文件级细节**

```bash
exiftool /evidence/carved/jpg/00000012.jpg
```

见 [`exiftool.md`](exiftool.md)。

---

## 6. 输出解读

| 输出文件 | 内容 | 报告里怎么用 |
|----------|------|--------------|
| `email.txt` / `url.txt` / `ip.txt` / `domain.txt` | 各特征清单（`偏移<TAB>特征<TAB>上下文`） | 证据清单主体 |
| `*_histogram.txt` | 按频次排序 | 找「最重要的目标」（访问最多的域、最常出现的邮箱） |
| `ccn.txt` / `telephone.txt` | 信用卡号 / 电话号码 | **敏感数据泄露证据**（含个人金融信息，属高风险） |
| `aes_keys.txt` | 疑似 AES 密钥 | 可能用于解密加密容器/文件 |
| `exif.txt` | 从图片里抽出的 EXIF | 拍摄设备/时间/GPS（配合 [`exiftool.md`](exiftool.md)） |
| `winlnk.txt` / `winprefetch.txt` | Windows 快捷方式 / Prefetch 痕迹 | **「运行过什么程序」的直接证据** |
| `ntfsmft.txt` / `ntfsusn.txt` / `ntfslogfile.txt` | NTFS MFT / USN / $LogFile 特征 | 即使元数据区被破坏也能捞到碎片 |
| `utmp.txt` | 登录记录残留 | 谁在什么时候登录过 |
| `pdf.txt` / `zip.txt` / `rar.txt` / `gzip.txt` | 各格式内部特征 | 压缩包/文档中的线索 |
| `json.txt` / `evtx.txt` | JSON / Windows 事件日志特征 | 结构化数据里的线索 |
| `report.xml` | 所有结果的**结构化汇总** | 便于脚本化处理/导入其他工具 |
| `phase1_*.txt` | 扫描过程统计 | 排错用 |

**关键判断**：

- **同一特征出现次数很高** → 高频目标（C2 服务器、常用邮箱）；
- **上下文中出现 `password=`/`token=`/`API_KEY=`** → 凭据泄露；
- **外域域名 + 罕见出现次数** → 值得专案追查的可疑通信；
- **`ccn.txt` 非空** → 可能涉及金融数据泄露（合规事件，需立即上报）；
- **偏移能在 TSK 中反查到 inode** → 完成「特征 → 文件」的归属闭环。

---

## 7. 与其他工具配合

```
① 获取镜像/内存：dcfldd / ddrescue / winpmem / LiME     dcfldd.md
        │
② 全景摸底：bulk_extractor（本文）
        │   ├─ email/url/ip/domain/ccn/keys 清单 + 直方图
        │   └─ 生成线索：可疑域、高频接口、泄露凭据
        │
③ 归属定位：sleuthkit（ifind 偏移→块→inode→文件）        sleuthkit.md
        │        └─ fls/istat/icat/tsk_recover
        │
④ 文件本体：blkls -A → foremost / scalpel                foremost.md / scalpel.md
        │        └─ 再对雕刻目录跑 bulk_extractor -R
        │
⑤ 细节：exiftool（图片/文档元数据）                       exiftool.md
⑥ 固件：binwalk（嵌入文件/压缩流/熵）                     binwalk.md
⑦ 图形复核：autopsy                                       autopsy.md
```

- 引擎与归属分析：[`sleuthkit.md`](sleuthkit.md) ｜ 图形界面：[`autopsy.md`](autopsy.md)
- 雕刻兜底：[`foremost.md`](foremost.md)、[`scalpel.md`](scalpel.md)
- 元数据：[`exiftool.md`](exiftool.md) ｜ 固件：[`binwalk.md`](binwalk.md) ｜ 获取：[`dcfldd.md`](dcfldd.md)

---

## 8. 常见坑与排错

| 报错/现象 | 原因 | 解决 |
|-----------|------|------|
| `-o is required` | 忘了指定输出目录 | 加 `-o <dir>` |
| 输出目录非空导致混乱 | 上次结果混在一起 | 加 `-Z`（清空）或换目录 |
| 扫描极慢 | 单线程 / CPU 受限 | `-j $(nproc)`；`-h` 里那行 `** probably CPU bound **` 就是在提示你加核 |
| 特征数量为 0（明明该有） | 目标是**加密容器**（高熵噪声） | 加密数据无法扫描；需先解密（合法取得密钥） |
| 漏掉跨页特征 | `marginsize` 调太小 | 保持默认 `-g 4194304`，或调大 |
| 输出里全是已知无害域名 | 无过滤 | 用 `-w <stop_list>` 排除常见域；或用直方图看长尾 |
| 电话号码/SSN 命中一堆噪音 | 匹配阈值不适配本地格式 | `-S min_phone_digits=` / `-S ssn_mode=` 调整；或用 `-x` 关掉该扫描器 |
| 输出目录巨大 | 某些扫描器会**雕刻**文件（`*_carved`） | 用 `_carve_mode=0` 关闭雕刻，或改用非 carving 扫描器 |
| 内存转储扫描报读错误 | 采集时内存已变化（不一致的转储） | 记录并说明；关键结论交叉验证 |
| 想把偏移映射回文件 | 忘了分区偏移 | 用 `-A <分区起始字节>` 让偏移与整盘一致；或在 TSK 里减去 `-o` 的字节偏移 |
| 重复运行结果不一致 | 用了 `-s` 采样 | **取证结论不要用采样**；全量扫描 |
| 无法扫描 E01 | bulk_extractor 需要 raw | 先用 `ewfmount`/`ewfexport` 转 raw（见 [`dcfldd.md`](dcfldd.md)） |
| `-R` 递归目录时日志太长 | 文件太多 | 加 `-q`；或用 `-a/-p`（finclude/fexclude 对应的是 binwalk，bulk_extractor 用 `-R` + 目录组织） |
| 忘记有哪些扫描器选项 | —— | **`bulk_extractor -H`**，一切选项都在里面 |

---

## 9. 防御视角（蓝队 / 应急响应）

bulk_extractor 在蓝队手里是**「快速摸底 + 泄露评估」**工具：

| 场景 | 用法 | 价值 |
|------|------|------|
| 入侵后快速摸底 | 对被入侵主机镜像跑一次全量扫描 | 30 分钟内知道「有没有外联地址、有没有凭据泄露、有没有攻击工具名」 |
| 找外联/C2 | 看 `ip.txt`/`domain_histogram.txt` | 输出可直接与威胁情报/防火墙日志比对，形成 IOC |
| **数据泄露评估** | `ccn.txt`/`email.txt`/`telephone.txt` | 判断是否涉及个人金融信息（**触发合规上报流程**） |
| 内存取证 | 对内存转储跑 `carve_net_memory=1` | 从内存里捞出网络请求、凭据、命令 |
| 找「运行过什么」 | `winprefetch.txt`/`winlnk.txt` | Windows 上的执行痕迹（即使文件已删） |
| 找加密勒索材料 | `aes_keys.txt` + 高熵区域 | 判断是否存在加密容器/勒索软件密钥 |
| 泄露事件的对外沟通 | `*_histogram.txt` | 用「访问最多的域/邮箱」客观描述影响范围 |
| 反取证迹象 | 大量 `ntfslogfile`/`ntfsusn` 碎片但 MFT 缺失 | 说明有人**破坏/清理了文件系统元数据** |

**蓝队实操建议**：

1. **把 bulk_extractor 加入 IR 脚本第一梯队**（与 `dcfldd`、`mmls`、`fls -r -m`、`mactime` 并列）；
2. **直方图优先读**：它是「一眼看清全貌」的最短路径；
3. **结论必须能回到偏移 → inode → 文件**（用 TSK 闭环），否则容易被质疑；
4. **对内存转储和含个人数据的特征文件**按最高敏感级别管理（加密、限定人员、访问留痕）；
5. **在自家环境定期跑一遍**：对员工电脑/服务器镜像做「泄露自检」，比事后补救便宜得多。

---

## 10. 参考

- bulk_extractor 官方仓库（含各类扫描器说明）：<https://github.com/simsong/bulk_extractor>
- Kali 工具页：<https://www.kali.org/tools/bulk-extractor/>
- NIST CFReDS 公开取证镜像（含官方文档中的经典样本）：<https://cfreds.nist.gov/>
- 数字取证期刊论文（bulk_extractor 的设计与评测）：Garfinkel, S. *Digital forensics XML and the DFXML toolset*；以及 bulk_extractor 相关论文
- 本地命令：`bulk_extractor -h`、`bulk_extractor -H`、`man bulk_extractor`

## ⚠️ 法律与伦理

bulk_extractor 的产出**天然包含大量个人信息**：邮箱、电话、信用卡号（`ccn.txt`）、登录记录、聊天片段、凭据与密钥。**一份 100GB 的镜像可能扫出数十万条个人信息。**

未授权分析可能触犯：

- 《刑法》第 285 条（非法获取计算机信息系统数据）、**第 253 条之一（侵犯公民个人信息罪）**；
- 《网络安全法》《数据安全法》《个人信息保护法》（邮箱/电话/信用卡号属个人信息，**卡片信息属敏感个人信息**，处理需更高合规要求）。

**必须遵守**：

1. **书面授权**：明确授权分析的对象、范围与目的；
2. **最小必要**：只扫描与事件相关的区域（用 `-Y`/`-A` 定向，而不是无脑全盘）；
3. **特征文件按敏感数据管理**：加密存储、限定访问人员、记录访问日志；
4. **发现金融/健康等敏感数据立即上报**，按合规流程处理，**不得自行复制或传播**；
5. **报告脱敏**：只给出统计与脱敏样例（如 `a***@example.com`），不粘贴完整凭据与个人信息；
6. **结案销毁**：按约定安全删除所有产出（含输出目录、雕刻文件、`report.xml`）。

本教程请仅在**自建实验镜像**、**NIST CFReDS 公开样本**或**获得明确授权的企业资产**上练习。
