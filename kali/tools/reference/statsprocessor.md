# statsprocessor

> Word generator based on per-position Markov chains Statsprocessor is a word generator based on per-position Markov chains packed into a single stand-alone binary. It generates candidate words based on a Hashcat format .hcstat file by using…

> **功能分类**：口令攻击 ｜ **Kali 包**：`statsprocessor` ｜ **官方文档**：<https://www.kali.org/tools/statsprocessor/>

## 1. 安装

```bash
sudo apt update
sudo apt install statsprocessor
```

| 项目 | 内容 |
|------|------|
| 版本 | 0.11 |
| 架构 | any |
| 可执行命令 | `statsprocessor`、`sp32`、`sp64` |
| 依赖 | `libc6`、`sp32` |
| 安装体积 | 45 KB |
| 官网 | <https://github.com/hashcat/statsprocessor> |
| 源码仓库 | <https://salsa.debian.org/pkg-security-team/statsprocessor> |
| 包追踪 | <https://pkg.kali.org/pkg/statsprocessor> |

## 2. 官方用法示例

> 以下为 Kali 官方工具页给出的示例与输出原文。

```text
Usage Example
Generate passwords with a minimum length of 6 (–pw-min=6) and a maximum length of 8 (–pw-max=8) using the stats in the provided file (/usr/share/oclhashcat/hashcat.hcstat):
root@kali:~# statsprocessor --pw-min=6 --pw-max=8 /usr/share/oclhashcat/hashcat.hcstat
13nger
13aner
13rina
13erer
13ller
131200
13ster
13iner
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 3 个可执行命令，下面是官方页面内嵌的帮助原文。

### `statsprocessor`

> 官方示例调用：`statsprocessor --pw-min=6 --pw-max=8 /usr/share/oclhashcat/hashcat.hcstat`

```text
root@kali:~# statsprocessor --pw-min=6 --pw-max=8 /usr/share/oclhashcat/hashcat.hcstat
13nger
13aner
13rina
13erer
13ller
131200
13ster
13iner
```

### `sp32`

> 官方示例调用：`sp32 -h`

```text
root@kali:~# sp32 -h
sp by atom, High-Performance word generator based on hashcat markov stats
Usage: sp32 [options]... hcstat-file [filter-mask]
* Startup:
  -V,  --version             Print version
  -h,  --help                Print help
* Increment:
       --pw-min=NUM          Start incrementing at NUM
       --pw-max=NUM          Stop incrementing at NUM
* Markov:
       --markov-disable      Emulates maskprocessor output
       --markov-classic      No per-position tables
       --threshold=NUM       Filter out chars after NUM chars added
                             Set to 0 to disable
* Misc:
       --combinations        Calculate number of combinations
       --hex-charset         Assume charset is given in hex
* Resources:
  -s,  --skip=NUM            skip number of words (for restore)
  -l,  --limit=NUM           limit number of words (for distributed)
* Files:
  -o,  --output-file=FILE    Output-file
* Custom charsets:
  -1,  --custom-charset1=CS  User-defineable charsets
  -2,  --custom-charset2=CS  Example:
  -3,  --custom-charset3=CS  --custom-charset1=?dabcdef
  -4,  --custom-charset4=CS  sets charset ?1 to 0123456789abcdef
* Built-in charsets:
  ?l = abcdefghijklmnopqrstuvwxyz
  ?u = ABCDEFGHIJKLMNOPQRSTUVWXYZ
  ?d = 0123456789
  ?s =  !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
  ?a = ?l?u?d?s
  ?h = 8 bit characters from 0xc0 - 0xff
  ?D = 8 bit characters from german alphabet
  ?F = 8 bit characters from french alphabet
  ?R = 8 bit characters from russian alphabet
```

### `sp64`

> 官方示例调用：`sp64 -h`

```text
root@kali:~# sp64 -h
sp by atom, High-Performance word generator based on hashcat markov stats
Usage: sp64 [options]... hcstat-file [filter-mask]
* Startup:
  -V,  --version             Print version
  -h,  --help                Print help
* Increment:
       --pw-min=NUM          Start incrementing at NUM
       --pw-max=NUM          Stop incrementing at NUM
* Markov:
       --markov-disable      Emulates maskprocessor output
       --markov-classic      No per-position tables
       --threshold=NUM       Filter out chars after NUM chars added
                             Set to 0 to disable
* Misc:
       --combinations        Calculate number of combinations
       --hex-charset         Assume charset is given in hex
* Resources:
  -s,  --skip=NUM            skip number of words (for restore)
  -l,  --limit=NUM           limit number of words (for distributed)
* Files:
  -o,  --output-file=FILE    Output-file
* Custom charsets:
  -1,  --custom-charset1=CS  User-defineable charsets
  -2,  --custom-charset2=CS  Example:
  -3,  --custom-charset3=CS  --custom-charset1=?dabcdef
  -4,  --custom-charset4=CS  sets charset ?1 to 0123456789abcdef
* Built-in charsets:
  ?l = abcdefghijklmnopqrstuvwxyz
  ?u = ABCDEFGHIJKLMNOPQRSTUVWXYZ
  ?d = 0123456789
  ?s =  !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
  ?a = ?l?u?d?s
  ?h = 8 bit characters from 0xc0 - 0xff
  ?D = 8 bit characters from german alphabet
  ?F = 8 bit characters from french alphabet
  ?R = 8 bit characters from russian alphabet
Updated on: 2025-Dec-09
 Edit this page
sslstrip
stegcracker
LIGHT
DARK
Links
Home
Download / Get Kali
Blog
OS Documentation
Tool Documentation
System Status
Archived Releases
Partnerships
Platforms
ARM (SBC)
NetHunter (Mobile)
Amazon AWS
Docker
Linode
Microsoft Azure
Microsoft Store (WSL)
Vagrant
Development
Bug Tracker
Continuous Integration
Network Mirror
Package Tracker
GitLab
Community
Discord
Support Forum
PeerTube
Follow Us
Bluesky
Facebook
Instagram
Mastodon
Substack
X
Newsletter
RSS
Policies
Cookie Policy
Privacy Policy
Trademark Policy
© OffSec Services Limited 2026. All rights reserved.
Kali Linux is part of OffSec's Community Projects
Learn more about OffSec's free, open-source penetration testing tools for cybersecurity professionals
```

## 4. 实践清单

按顺序做完这五步，就能把工具从「装上」推进到「会用」：

- [ ] **1.** **装好并确认版本** —— `sudo apt install statsprocessor`，再执行 `statsprocessor --version` 2>/dev/null || `statsprocessor -V`
- [ ] **2.** **读官方帮助** —— `statsprocessor -h`，需要细节时 `man statsprocessor`
- [ ] **3.** **在自有靶场跑最小用例** —— 官方给出的调用形式是：`Usage: sp32 [options]... hcstat-file [filter-mask]`
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/statsprocessor/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/statsprocessor/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/statsprocessor/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
