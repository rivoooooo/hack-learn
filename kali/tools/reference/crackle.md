# crackle

> Crack and decrypt BLE encryption crackle exploits a flaw in the BLE pairing process that allows an attacker to guess or very quickly brute force the TK (Temporary Key). With the TK and other data collected from the pairing process, the STK…

> **功能分类**：口令攻击 ｜ **Kali 包**：`crackle` ｜ **官方文档**：<https://www.kali.org/tools/crackle/>

## 1. 安装

```bash
sudo apt update
sudo apt install crackle
```

| 项目 | 内容 |
|------|------|
| 版本 | 0.1~git01282014 |
| 架构 | any |
| 可执行命令 | `crackle` |
| 依赖 | `libc6`、`libpcap0.8t64` |
| 安装体积 | 54 KB |
| 官网 | <https://github.com/mikeryan/crackle> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/crackle> |
| 包追踪 | <https://pkg.kali.org/pkg/crackle> |

## 2. 官方用法示例

> 以下为 Kali 官方工具页给出的示例与输出原文。

```text
Usage Example
Read the input file (-i ltk_exchange.pcap) and write the decrypted output to disk (-o ltk-decrypted.pcap):
root@kali:~# crackle -i ltk_exchange.pcap -o ltk-decrypted.pcap


!!!
TK found: 000000
ding ding ding, using a TK of 0! Just Cracks(tm)
!!!

Warning: packet is too short to be encrypted (1), skipping
LTK found: 7f62c053f104a5bbe68b1d896a2ed49c
Done, processed 712 total packets, decrypted 3
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `crackle`

官方给出的调用示例：`crackle -i ltk_exchange.pcap -o ltk-decrypted.pcap`

```text
root@kali:~# crackle -i ltk_exchange.pcap -o ltk-decrypted.pcap
!!!
TK found: 000000
ding ding ding, using a TK of 0! Just Cracks(tm)
!!!
Warning: packet is too short to be encrypted (1), skipping
LTK found: 7f62c053f104a5bbe68b1d896a2ed49c
Done, processed 712 total packets, decrypted 3
```

### `crackle（示例）`

官方给出的调用示例：`crackle -h`

```text
root@kali:~# crackle -h
Usage: crackle -i <input.pcap> [-o <output.pcap>] [-l <ltk>]
Cracks Bluetooth Low Energy encryption (AKA Bluetooth Smart)
Major modes:  Crack TK // Decrypt with LTK
Crack TK:
    Input PCAP file must contain a complete pairing conversation. If any
    packet is missing, cracking will not proceed. The PCAP file will be
    decrypted if -o <output.pcap> is specified. If LTK exchange is in
    the PCAP file, the LTK will be dumped to stdout.
Decrypt with LTK:
    Input PCAP file must contain at least LL_ENC_REQ and LL_ENC_RSP
    (which contain the SKD and IV). The PCAP file will be decrypted if
    the LTK is correct.
    LTK format: string of hex bytes, no separator, most-significant
    octet to least-significant octet.
    Example: -l 81b06facd90fe7a6e9bbd9cee59736a7
Optional arguments:
    -v   Be verbose
    -t   Run tests against crypto engine
Written by Mike Ryan <
[email protected]
>
See web site for more info:
    http://lacklustre.net/projects/crackle/
Updated on: 2025-Dec-09
 Edit this page
cowpatty
creddump7
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install crackle`，再执行 `crackle --version` 2>/dev/null || `crackle -V`
- [ ] **2.** **读官方帮助** —— `crackle -h`，需要细节时 `man crackle`
- [ ] **3.** **在自有靶场跑最小用例** —— 官方给出的调用形式是：`Usage: crackle -i <input.pcap> [-o <output.pcap>] [-l <ltk>]`
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/crackle/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/credential-access.md`](../../tools/by-attack/credential-access.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/crackle/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/crackle/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
