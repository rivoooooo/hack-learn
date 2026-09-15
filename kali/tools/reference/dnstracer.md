# dnstracer

> Trace DNS queries to the source dnstracer determines where a given Domain Name Server (DNS) gets its information from for a given hostname, and follows the chain of DNS servers back to the authoritative answer.

> **功能分类**：信息搜集 ｜ **Kali 包**：`dnstracer` ｜ **官方文档**：<https://www.kali.org/tools/dnstracer/>

## 1. 安装

```bash
sudo apt update
sudo apt install dnstracer
```

| 项目 | 内容 |
|------|------|
| 版本 | 1.10 |
| 架构 | any |
| 可执行命令 | `dnstracer` |
| 依赖 | `libc6` |
| 安装体积 | 63 KB |
| 官网 | <http://www.mavetju.org/unix/dnstracer.php> |
| 源码仓库 | <https://salsa.debian.org/creekorful/dnstracer> |
| 包追踪 | <https://pkg.kali.org/pkg/dnstracer> |

## 2. 官方用法示例

> 以下为 Kali 官方工具页给出的示例与输出原文。

```text
Usage Example
Scan a domain (example.com), retry up to 3 times (-r 3), and display verbose output (-v):
root@kali:~# dnstracer -r 3 -v example.com
Tracing to example.com[a] via 192.168.1.1, maximum of 3 retries
192.168.1.1 (192.168.1.1) IP HEADER
- Destination address:  192.168.1.1
DNS HEADER (send)
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `dnstracer`

> 官方示例调用：`dnstracer -r 3 -v example.com`

```text
root@kali:~# dnstracer -r 3 -v example.com
Tracing to example.com[a] via 192.168.1.1, maximum of 3 retries
192.168.1.1 (192.168.1.1) IP HEADER
- Destination address:  192.168.1.1
DNS HEADER (send)
```

### `dnstracer -h`

> 官方示例调用：`dnstracer -h`

```text
root@kali:~# dnstracer -h
dnstracer: invalid option -- 'h'
DNSTRACER version 1.10 - (c) Edwin Groothuis - http://www.mavetju.org
Usage: dnstracer [options] [host]
	-c: disable local caching, default enabled
	-C: enable negative caching, default disabled
	-e: disable EDNS0, default enabled
	-E <size>: set EDNS0 size, default 1500
	-o: enable overview of received answers, default disabled
	-q <querytype>: query-type to use for the DNS requests, default A
	-r <retries>: amount of retries for DNS requests, default 3
	-s <server>: use this server for the initial request, default localhost
	             If . is specified, A.ROOT-SERVERS.NET will be used.
	-t <maximum timeout>: Limit time to wait per try
	-v: verbose
	-S <ip address>: use this source address.
	-4: don't query IPv6 servers
Updated on: 2026-Aug-25
 Edit this page
dnsrecon
dnswalk
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install dnstracer`，再执行 `dnstracer --version` 2>/dev/null || `dnstracer -V`
- [ ] **2.** **读官方帮助** —— `dnstracer -h`，需要细节时 `man dnstracer`
- [ ] **3.** **在自有靶场跑最小用例** —— 官方给出的调用形式是：`Usage: dnstracer [options] [host]`
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/dnstracer/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/reconnaissance.md`](../../tools/by-attack/reconnaissance.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/dnstracer/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/dnstracer/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
