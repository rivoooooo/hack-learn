# ngrep

> Grep for network traffic ngrep strives to provide most of GNU grep’s common features, applying them to the network layer. ngrep is a pcap-aware tool that will allow you to specify extended regular expressions to match against data payloads…

> **功能分类**：通用工具 ｜ **Kali 包**：`ngrep` ｜ **官方文档**：<https://www.kali.org/tools/ngrep/>

## 1. 安装

```bash
sudo apt update
sudo apt install ngrep
```

| 项目 | 内容 |
|------|------|
| 版本 | 1.47 |
| 架构 | any |
| 可执行命令 | `ngrep` |
| 依赖 | `libc6`、`libnet9`、`libpcap0.8t64`、`libpcre2-8-0` |
| 安装体积 | 73 KB |
| 官网 | <https://github.com/jpr5/ngrep> |
| 源码仓库 | <https://salsa.debian.org/debian/ngrep> |
| 包追踪 | <https://pkg.kali.org/pkg/ngrep> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
ngrep -h          # 查看用法
man ngrep         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `ngrep`

官方给出的调用示例：`ngrep -h`

```text
root@kali:~# ngrep -h
usage: ngrep <-hNXViwqpevxlDtTRM> <-IO pcap_dump> <-n num> <-d dev> <-A num>
             <-s snaplen> <-S limitlen> <-W normal|byline|single|none> <-c cols>
             <-P char> <-F file>             <-K count>
             <match expression> <bpf filter>
   -h  is help/usage
   -V  is version information
   -q  is be quiet (don't print packet reception hash marks)
   -e  is show empty packets
   -i  is ignore case
   -v  is invert match
   -R  is don't do privilege revocation logic
   -x  is print in alternate hexdump format
   -X  is interpret match expression as hexadecimal
   -w  is word-regex (expression must match as a word)
   -p  is don't go into promiscuous mode
   -l  is make stdout line buffered
   -D  is replay pcap_dumps with their recorded time intervals
   -t  is print timestamp every time a packet is matched
   -T  is print delta timestamp every time a packet is matched
         specify twice for delta from first match
   -M  is don't do multi-line match (do single-line match instead)
   -I  is read packet stream from pcap format file pcap_dump
   -O  is dump matched packets in pcap format to pcap_dump
   -n  is look at only num packets
   -A  is dump num packets after a match
   -s  is set the bpf caplen
   -S  is set the limitlen on matched packets
   -W  is set the dump format (normal, byline, single, none)
   -c  is force the column width to the specified size
   -P  is set the non-printable display char to what is specified
   -F  is read the bpf filter from the specified file
   -N  is show sub protocol number
   -d  is use specified device instead of the pcap default
   -K  is send N packets to kill observed connections
Updated on: 2026-May-25
 Edit this page
netw-ib-ox-ag
nmap
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install ngrep`，再执行 `ngrep --version` 2>/dev/null || `ngrep -V`
- [ ] **2.** **读官方帮助** —— `ngrep -h`，需要细节时 `man ngrep`
- [ ] **3.** **在自有靶场跑最小用例** —— 用 `ngrep -h` 里最简单的那个子命令试一次
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/ngrep/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/ngrep/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/ngrep/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
