# maskprocessor

> High-performance word generator with a per-position configurable charset Maskprocessor is a fast word list generator. It enumerates all combinations from a given user-defined keyspace and outputs the results. Since it supports different al…

> **功能分类**：口令攻击 ｜ **Kali 包**：`maskprocessor` ｜ **官方文档**：<https://www.kali.org/tools/maskprocessor/>

## 1. 安装

```bash
sudo apt update
sudo apt install maskprocessor
```

| 项目 | 内容 |
|------|------|
| 版本 | 0.73 |
| 架构 | any |
| 可执行命令 | `maskprocessor`、`mp32`、`mp64` |
| 依赖 | `libc6`、`mp32` |
| 安装体积 | 44 KB |
| 官网 | <https://github.com/hashcat/maskprocessor> |
| 源码仓库 | <https://salsa.debian.org/pkg-security-team/maskprocessor> |
| 包追踪 | <https://pkg.kali.org/pkg/maskprocessor> |

## 2. 官方用法示例

> 以下为 Kali 官方工具页给出的示例与输出原文。

```text
Usage Example
Generate a list of words beginning with (pass) and append one digit (?d) and one lowercase letter (?l):
root@kali:~# maskprocessor pass?d?l
pass0a
pass0b
pass0c
pass0d
pass0e
pass0f
pass0g
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 3 个可执行命令，下面是官方页面内嵌的帮助原文。

### `maskprocessor`

> 官方示例调用：`maskprocessor pass?d?l`

```text
root@kali:~# maskprocessor pass?d?l
pass0a
pass0b
pass0c
pass0d
pass0e
pass0f
pass0g
```

### `mp32`

> 官方示例调用：`mp32 -h`

```text
root@kali:~# mp32 -h
High-Performance word generator with a per-position configureable charset
Usage: mp32 [options]... mask
* Startup:
  -V,  --version             Print version
  -h,  --help                Print help
* Increment:
  -i,  --increment=NUM:NUM   Enable increment mode. 1st NUM=start, 2nd NUM=stop
                             Example: -i 4:8 searches lengths 4-8 (inclusive)
* Misc:
       --combinations        Calculate number of combinations
       --hex-charset         Assume charset is given in hex
  -q,  --seq-max=NUM         Maximum number of multiple sequential characters
  -r,  --occurrence-max=NUM  Maximum number of occurrence of a character
* Resources:
  -s,  --start-at=WORD       Start at specific position
  -l,  --stop-at=WORD        Stop at specific position
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
  ?b = 0x00 - 0xff
```

### `mp64`

> 官方示例调用：`mp64 -h`

```text
root@kali:~# mp64 -h
High-Performance word generator with a per-position configureable charset
Usage: mp64 [options]... mask
* Startup:
  -V,  --version             Print version
  -h,  --help                Print help
* Increment:
  -i,  --increment=NUM:NUM   Enable increment mode. 1st NUM=start, 2nd NUM=stop
                             Example: -i 4:8 searches lengths 4-8 (inclusive)
* Misc:
       --combinations        Calculate number of combinations
       --hex-charset         Assume charset is given in hex
  -q,  --seq-max=NUM         Maximum number of multiple sequential characters
  -r,  --occurrence-max=NUM  Maximum number of occurrence of a character
* Resources:
  -s,  --start-at=WORD       Start at specific position
  -l,  --stop-at=WORD        Stop at specific position
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
  ?b = 0x00 - 0xff
Updated on: 2025-Dec-09
 Edit this page
maryam
masscan
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install maskprocessor`，再执行 `maskprocessor --version` 2>/dev/null || `maskprocessor -V`
- [ ] **2.** **读官方帮助** —— `maskprocessor -h`，需要细节时 `man maskprocessor`
- [ ] **3.** **在自有靶场跑最小用例** —— 官方给出的调用形式是：`Usage: mp32 [options]... mask`
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/maskprocessor/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/maskprocessor/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/maskprocessor/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
