# merlin-agent

> Cross-platform post-exploitation HTTP/2 Command & Control agent This package contains the Agent code for Merlin post-exploitation command and control framework.

> **功能分类**：通用工具 ｜ **Kali 包**：`merlin-agent` ｜ **官方文档**：<https://www.kali.org/tools/merlin-agent/>

## 1. 安装

```bash
sudo apt update
sudo apt install merlin-agent
```

| 项目 | 内容 |
|------|------|
| 版本 | 2.4.3 |
| 架构 | any |
| 可执行命令 | `merlin-agent` |
| 依赖 | `libc6` |
| 安装体积 | 12.19 MB |
| 官网 | <https://github.com/Ne0nd0g/merlin-agent> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/merlin-agent> |
| 包追踪 | <https://pkg.kali.org/pkg/merlin-agent> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
merlin-agent -h          # 查看用法
man merlin-agent         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `merlin-agent`

> 官方示例调用：`merlin-agent -h`

```text
root@kali:~# merlin-agent -h
  -addr string
    	The address in interface:port format the agent will use for communications (default "127.0.0.1:7777")
  -auth string
    	The Agent's authentication method (e.g, OPAQUE (default "opaque")
  -debug
    	Enable debug output
  -headers string
    	A new line separated (e.g., \n) list of additional HTTP headers to use
  -host string
    	HTTP Host header
  -http-client string
    	The HTTP client to use for communication [go, winhttp] (default "go")
  -ja3 string
    	JA3 signature string (not the MD5 hash). Overrides -proto & -parrot flags
  -killdate string
    	The date, as a Unix EPOCH timestamp, that the agent will quit running (default "0")
  -listener string
    	The uuid of the peer-to-peer listener this agent should connect to
  -maxretry string
    	The maximum amount of failed checkins before the agent will quit running (default "7")
  -padding string
    	The maximum amount of data that will be randomly selected and appended to every message (default "4096")
  -parrot string
    	parrot or mimic a specific browser from github.com/refraction-networking/utls (e.g., HelloChrome_Auto)
  -proto string
    	Protocol for the agent to connect with [https (HTTP/1.1), http (HTTP/1.1 Clear-Text), h2 (HTTP/2), h2c (HTTP/2 Clear-Text), http3 (QUIC or HTTP/3.0), tcp-bind, tcp-reverse, udp-bind, udp-reverse, smb-bind, smb-reverse] (default "h2")
  -proxy string
    	Hardcoded proxy to use for http/1.1 traffic only that will override host configuration
  -proxy-pass string
    	Password for proxy authentication
  -proxy-user string
    	Username for proxy authentication
  -psk string
    	Pre-Shared Key used to encrypt initial communications (default "merlin")
  -secure string
    	Require TLS certificate validation for HTTP communications (default "false")
  -skew string
    	Amount of skew, or variance, between agent checkins (default "3000")
  -sleep string
    	Time for agent to sleep (default "30s")
  -transforms string
    	Ordered CSV of transforms to construct a message (default "jwe,gob-base")
  -url string
    	A comma separated list of the full URLs for the agent to connect to (default "https://127.0.0.1:443")
  -useragent string
    	The HTTP User-Agent header string that the Agent will use while sending traffic (default "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.85 Safari/537.36")
  -v	Enable verbose output
  -version
    	Print the agent version and exit
Updated on: 2026-Aug-25
 Edit this page
mercurial
metasploit-framework
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install merlin-agent`，再执行 `merlin-agent --version` 2>/dev/null || `merlin-agent -V`
- [ ] **2.** **读官方帮助** —— `merlin-agent -h`，需要细节时 `man merlin-agent`
- [ ] **3.** **在自有靶场跑最小用例** —— 用 `merlin-agent -h` 里最简单的那个子命令试一次
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/merlin-agent/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/merlin-agent/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/merlin-agent/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
