# sipsak

> SIP Swiss army knife sipsak is a small command line tool for developers and administrators of Session Initiation Protocol (SIP) applications. It can be used for some simple tests on SIP applications and devices.

> **功能分类**：漏洞分析 ｜ **Kali 包**：`sipsak` ｜ **官方文档**：<https://www.kali.org/tools/sipsak/>

## 1. 安装

```bash
sudo apt update
sudo apt install sipsak
```

| 项目 | 内容 |
|------|------|
| 版本 | 0.9.8.1 |
| 架构 | any |
| 可执行命令 | `sipsak` |
| 依赖 | `libc6`、`libcares2`、`libgnutls30t64` |
| 安装体积 | 133 KB |
| 官网 | <https://github.com/nils-ohlmeier/sipsak> |
| 源码仓库 | <https://salsa.debian.org/pkg-voip-team/sipsak> |
| 包追踪 | <https://pkg.kali.org/pkg/sipsak> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
sipsak -h          # 查看用法
man sipsak         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `sipsak`

官方给出的调用示例：`sipsak --help`

```text
root@kali:~# sipsak --help
long option help
sipsak 0.9.8.1 by Nils Ohlmeier
 Copyright (C) 2002-2004 FhG Fokus
 Copyright (C) 2004-2005 Nils Ohlmeier
 report bugs to
[email protected]
 shoot  : sipsak [-f FILE] [-L] -s SIPURI
 trace  : sipsak -T -s SIPURI
 usrloc : sipsak -U [-I|M] [-b NUMBER] [-e NUMBER] [-x NUMBER] [-z NUMBER] -s SIPURI
 usrloc : sipsak -I|M [-b NUMBER] [-e NUMBER] -s SIPURI
 usrloc : sipsak -U [-C SIPURI] [-x NUMBER] -s SIPURI
 message: sipsak -M [-B STRING] [-O STRING] [-c SIPURI] -s SIPURI
 flood  : sipsak -F [-e NUMBER] -s SIPURI
 random : sipsak -R [-t NUMBER] -s SIPURI
 additional parameter in every mode:
   [-a PASSWORD] [-d] [-i] [-H HOSTNAME] [-l PORT] [-m NUMBER] [-n] [-N]
   [-r PORT] [-v] [-V] [-w]
  --help                     displays this help message
  --version                  prints version string only
  --filename=FILE            the file which contains the SIP message to send
                               use - for standard input
  --no-crlf                  de-activate CR (\r) insertion
  --sip-uri=SIPURI           the destination server URI in form
                               sip:[user@]servername[:port]
  --traceroute               activates the traceroute mode
  --usrloc-mode              activates the usrloc mode
  --invite-mode              simulates a successful calls with itself
  --message-mode             sends messages to itself
  --contact=SIPURI           use the given URI as Contact in REGISTER
  --appendix-begin=NUMBER    the starting number appendix to the user name (default: 0)
  --appendix-end=NUMBER      the ending number of the appendix to the user name
  --sleep=NUMBER             sleep number ms before sending next request
  --expires=NUMBER           the expires header field value (default: 15)
  --remove-bindings=NUMBER   activates randomly removing of user bindings
  --flood-mode               activates the flood mode
  --random-mode              activates the random mode (dangerous)
  --trash-chars=NUMBER       the maximum number of trashed character in random mode
                               (default: request length)
  --local-port=PORT          the local port to use (default: any)
  --remote-port=PORT         the remote port to use (default: 5060)
  --outbound-proxy=HOSTNAME  request target (outbound proxy)
  --hostname=HOSTNAME        overwrites the local hostname in all headers
  --max-forwards=NUMBER      the value for the max-forwards header field
  --numeric                  use FQDN instead of IP in the Via-Line
  --processes=NUMBER         Divide the workflow among the number of processes
  --auth-username=STRING     username for authentication
  --no-via                   deactivate the insertion of a Via-Line
  --password=PASSWORD        password for authentication
                               (if omitted password=username)
  --ignore-redirects         ignore redirects
  --verbose                  each v produces more verbosity (max. 3)
  --extract-ip               extract IP from the warning in reply
  --replace-string=STRING    replacement for a special mark in the message
  --replace                  activates replacement of variables
  --nagios-code              returns exit codes Nagios compliant
  --nagios-warn=NUMBER       return Nagios warning if retrans > number
  --message-body=STRING      send a message with string as body
  --disposition=STRING       Content-Disposition value
  --search=REGEXP            search for a RegExp in replies and return error
                             on failure
  --timing=NUMBER            number of test runs and print just the timings
  --symmetric                send and received on the same port
  --from=SIPURI              use the given URI as From in MESSAGE
  --timeout-factor=NUMBER    timeout multiplier for INVITE transactions
                             on non-reliable transports (default: 64)
  --timer-t1=NUMBER          timeout T1 in ms (default: 500)
  --transport=STRING         specify transport to be used
  --headers=STRING           adds additional headers to the request
  --local-ip=STRING          specify local ip address to be used
  --authhash=STRING          HA1 hash for authentication instead of password
  --syslog=NUMBER            log exit message to syslog with given log level
  --tls-ca-cert=FILE         file with the cert of the root CA
  --tls-client-cert=FILE     file with the cert which sipsak will send
  --tls-ignore-cert-failure  ignore failures during the TLS handshake
Updated on: 2026-May-25
 Edit this page
siege
snort
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install sipsak`，再执行 `sipsak --version` 2>/dev/null || `sipsak -V`
- [ ] **2.** **读官方帮助** —— `sipsak -h`，需要细节时 `man sipsak`
- [ ] **3.** **在自有靶场跑最小用例** —— 用 `sipsak -h` 里最简单的那个子命令试一次
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/sipsak/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/discovery.md`](../../tools/by-attack/discovery.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/sipsak/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/sipsak/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
