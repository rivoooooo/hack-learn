# massdns

> High-performance DNS stub resolver This package contains a simple high-performance DNS stub resolver targeting those who seek to resolve a massive amount of domain names in the order of millions or even billions. Without special configurat…

> **功能分类**：通用工具 ｜ **Kali 包**：`massdns` ｜ **官方文档**：<https://www.kali.org/tools/massdns/>

## 1. 安装

```bash
sudo apt update
sudo apt install massdns
```

| 项目 | 内容 |
|------|------|
| 版本 | 1.1.0 |
| 架构 | amd64 |
| 可执行命令 | `massdns` |
| 依赖 | `libc6` |
| 安装体积 | 128 KB |
| 官网 | <https://github.com/blechschmidt/massdns> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/massdns> |
| 包追踪 | <https://pkg.kali.org/pkg/massdns> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
massdns -h          # 查看用法
man massdns         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `massdns`

官方给出的调用示例：`massdns -h`

```text
root@kali:~# massdns -h
Usage: massdns [options] [domainlist]
  -b  --bindto           Bind to IP address and port. (Default: 0.0.0.0:0)
      --busy-poll        Use busy-wait polling instead of epoll.
  -c  --resolve-count    Number of resolves for a name before giving up. (Default: 50)
      --drop-group       Group to drop privileges to when running as root. (Default: nogroup)
      --drop-user        User to drop privileges to when running as root. (Default: nobody)
      --extended-input   Input names are followed by a space-separated list of resolvers.
                         These are used before falling back to the resolvers file.
      --filter           Only output packets with the specified response code.
      --flush            Flush the output file whenever a response was received.
  -h  --help             Show this help.
      --ignore           Do not output packets with the specified response code.
  -i  --interval         Interval in milliseconds to wait between multiple resolves of the same
                         domain. (Default: 500)
  -l  --error-log        Error log file path. (Default: /dev/stderr)
      --norecurse        Use non-recursive queries. Useful for DNS cache snooping.
  -o  --output           Flags for output formatting.
      --predictable      Use resolvers incrementally. Useful for resolver tests.
      --processes        Number of processes to be used for resolving. (Default: 1)
  -q  --quiet            Quiet mode.
      --rand-src-ipv6    Use a random IPv6 address from the specified subnet for each query.
      --rcvbuf           Size of the receive buffer in bytes.
      --retry            Unacceptable DNS response codes.
                         (Default: All codes but NOERROR or NXDOMAIN)
  -r  --resolvers        Text file containing DNS resolvers.
      --root             Do not drop privileges when running as root. Not recommended.
  -s  --hashmap-size     Number of concurrent lookups. (Default: 10000)
      --sndbuf           Size of the send buffer in bytes.
      --status-format    Format for real-time status updates, json or ansi (Default: ansi)
      --sticky           Do not switch the resolver when retrying.
      --socket-count     Socket count per process. (Default: 1)
  -t  --type             Record type to be resolved. (Default: A)
      --verify-ip        Verify IP addresses of incoming replies.
  -w  --outfile          Write to the specified output file instead of standard output.
Output flags:
  L - domain list output
  S - simple text output
  F - full text output
  B - binary output
  J - ndjson output
Advanced flags for the domain list output mode:
  0 - Include NOERROR replies without answers.
Advanced flags for the simple output mode:
  d - Include records from the additional section.
  i - Indent any reply record.
  l - Separate replies using a line feed.
  m - Only output reply records that match the question name.
  n - Include records from the answer section.
  q - Print the question.
  r - Print the question with resolver IP address, Unix timestamp and return code prepended.
  s - Separate packet sections using a line feed.
  t - Include TTL and record class within the output.
  u - Include records from the authority section.
Advanced flags for the ndjson output mode:
  e - Write a record for each terminal query failure.
Updated on: 2026-Mar-13
 Edit this page
impacket-scripts
ollydbg
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install massdns`，再执行 `massdns --version` 2>/dev/null || `massdns -V`
- [ ] **2.** **读官方帮助** —— `massdns -h`，需要细节时 `man massdns`
- [ ] **3.** **在自有靶场跑最小用例** —— 官方给出的调用形式是：`Usage: massdns [options] [domainlist]`
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/massdns/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/reconnaissance.md`](../../tools/by-attack/reconnaissance.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/massdns/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/massdns/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
