# doona

> Network fuzzer forked from bed Doona is a fork of the Bruteforce Exploit Detector Tool (BED). BED is a program which is designed to check daemons for potential buffer overflows, format string bugs etc.

> **功能分类**：通用工具 ｜ **Kali 包**：`doona` ｜ **官方文档**：<https://www.kali.org/tools/doona/>

## 1. 安装

```bash
sudo apt update
sudo apt install doona
```

| 项目 | 内容 |
|------|------|
| 版本 | 1.0 |
| 架构 | all |
| 可执行命令 | `doona` |
| 依赖 | `perl` |
| 安装体积 | 128 KB |
| 官网 | <https://github.com/wireghoul/doona> |
| 源码仓库 | <https://salsa.debian.org/pkg-security-team/doona> |
| 包追踪 | <https://pkg.kali.org/pkg/doona> |

## 2. 官方用法示例

> 以下为 Kali 官方工具页给出的示例与输出原文。

```text
Usage Example
Use the HTTP plugin (-m HTTP) to fuzz the target (-t 192.168.1.15), stopping after 5 cases (-M 5):
root@kali:~# doona -m HTTP -t 192.168.1.15 -M 5

 Doona 1.0 by Wireghoul (www.justanotherhacker.com)

 + Buffer overflow testing
    1/37   [XAXAX] ......
Max requests (5) completed, index: 5
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `doona`

> 官方示例调用：`doona -m HTTP -t 192.168.1.15 -M 5`

```text
root@kali:~# doona -m HTTP -t 192.168.1.15 -M 5
 Doona 1.0 by Wireghoul (www.justanotherhacker.com)
 + Buffer overflow testing
    1/37   [XAXAX] ......
Max requests (5) completed, index: 5
```

### `doona -h`

> 官方示例调用：`doona -h`

```text
root@kali:~# doona -h
 Doona 1.0 by Wireghoul (www.justanotherhacker.com)
Usage:
 ./doona.pl -m [module] <options>
 -m <module>   = DICT/FINGER/FTP/HTTP/HTTP_MORE/HTTP_SP/HTTP_WEBDAV/IMAP/IRC/LPD/NNTP/PJL/POP/PROXY/RTSP/SMTP/SOCKS4/SOCKS5/TFTP/WHOIS
 -c <int>      = Execute a health check after every <int> fuzz cases
 -t <target>   = Host to check (default: localhost)
 -p <port>     = Port to connect to (default: module specific standard port)
 -o <timeout>  = seconds to wait after each test (default: 2 seconds)
 -r <index>    = Resumes fuzzing at test case index
 -k            = Keep trying until server passes a health check
 -d            = Dump test case to stdout (use in combination with -r)
 -M <num>      = Exit after executing <num> number of fuzz cases
 -h            = Help (this text)
 use "./doona.pl -m [module] -h" for module specific option.
 Only -m is a mandatory switch.
Updated on: 2025-Dec-09
 Edit this page
dnstwist
dotdotpwn
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install doona`，再执行 `doona --version` 2>/dev/null || `doona -V`
- [ ] **2.** **读官方帮助** —— `doona -h`，需要细节时 `man doona`
- [ ] **3.** **在自有靶场跑最小用例** —— 官方给出的调用形式是：`Usage:`
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/doona/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/doona/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/doona/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
