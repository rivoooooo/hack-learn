# cntlm

> Fast NTLM authentication proxy with tunneling Cntlm is a fast and efficient NTLM proxy, with support for TCP/IP tunneling, authenticated connection caching, ACLs, proper daemon logging and behaviour and much more. It has up to ten times fa…

> **功能分类**：通用工具 ｜ **Kali 包**：`cntlm` ｜ **官方文档**：<https://www.kali.org/tools/cntlm/>

## 1. 安装

```bash
sudo apt update
sudo apt install cntlm
```

| 项目 | 内容 |
|------|------|
| 版本 | 0.94.0 |
| 架构 | any |
| 可执行命令 | `cntlm` |
| 依赖 | `libc6`、`libgssapi-krb5-2` |
| 安装体积 | 703 KB |
| 官网 | <https://github.com/versat/cntlm/> |
| 源码仓库 | <https://salsa.debian.org/debian/cntlm> |
| 包追踪 | <https://pkg.kali.org/pkg/cntlm> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
cntlm -h          # 查看用法
man cntlm         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `cntlm`

官方给出的调用示例：`cntlm -h`

```text
root@kali:~# cntlm -h
CNTLM - Accelerating NTLM Authentication Proxy version 0.94.0
Copyright (c) 2oo7-2o1o David Kubicek
This program comes with NO WARRANTY, to the extent permitted by law. You
may redistribute copies of it under the terms of the GNU GPL Version 2 or
newer. For more information about these matters, see the file LICENSE.
For copyright holders of included encryption routines see headers.
Usage: cntlm [-AaBcDdFfGgHhILlMNOPpqRrSsTUuvwXx] <proxy_host>[:]<proxy_port> ...
	-A  <address>[/<net>]
	    ACL allow rule. IP or hostname, net must be a number (CIDR notation)
	-a  ntlm | nt | lm | gss
	    Authentication type - combined NTLM, just LM, just NT, or GSS. Default NTLM.
	    GSS activates kerberos auth: you need a cached credential.
	    NTLM is the most versatile setting and likely to work for you.
	-B  Enable NTLM-to-basic authentication.
	-c  <config_file>
	    Configuration file. Other arguments can be used as well, overriding
	    config file settings.
	-D  <address>[/<net>]
	    ACL deny rule. Syntax same as -A.
	-d  <domain>
	    Domain/workgroup can be set separately.
	-F  <flags>
	    NTLM authentication flags.
	-f  Run in foreground, do not fork into daemon mode.
	-G  <pattern>
	    User-Agent matching for the trans-isa-scan plugin.
	-g  Gateway mode - listen on all interfaces, not only loopback.
	-H  Print password hashes for use in config file (NTLMv2 needs -u and -d).
	-h  Print this help info along with version number.
	-I  Prompt for the password interactively.
	-L  [<saddr>:]<lport>:<rhost>:<rport>
	    Forwarding/tunneling a la OpenSSH. Same syntax - listen on lport
	    and forward all connections through the proxy to rhost:rport.
	    Can be used for direct tunneling without corkscrew, etc.
	-l  [<saddr>:]<lport>
	    Main listening port for the NTLM proxy.
	-M  <testurl>
	    Magic autodetection of proxy's NTLM dialect.
	-N  "<hostname_wildcard1>[, <hostname_wildcardN>"
	    List of URL's to serve directly as stand-alone proxy (e.g. '*.local')
	-O  [<saddr>:]<lport>
	    Enable SOCKS5 proxy on port lport (binding to address saddr)
	-P  <pidfile>
	    Create a PID file upon successful start.
	-p  <password>
	    Account password. Will not be visible in "ps", /proc, etc.
	-q  Sets the Syslog logging level to DEBUG (default level is INFO).
	-R  <username>:<password>
	    Enable authorization for SOCKS5 proxy, when enabled.
	    It can be used several times, to create a whole list of accounts.
	-r  "HeaderName: value"
	    Add a header substitution. All such headers will be added/replaced
	    in the client's requests.
	-S  <size_in_kb>
	    Enable automation of GFI WebMonitor ISA scanner for files < size_in_kb.
	-s  Do not use threads, serialize all requests - for debugging only.
	-T  <file.log>
	    Redirect all debug information into a trace file for support upload.
	    MUST be the first argument on the command line, implies -v.
	-U  <uid>
	    Run as uid. It is an important security measure not to run as root.
	-u  <user>[@<domain]
	    Domain/workgroup can be set separately.
	-v  Print debugging information.
	-w  <workstation>
	    Some proxies require correct NetBIOS hostname.
	-x  <PAC_file>
	    Specify a PAC file to load.
	-X  <sspi_handle_type>
	    Use SSPI with specified handle type. Works only under Windows.
	    Default is negotiate.
Updated on: 2026-Jun-17
 Edit this page
autorecon
cupid-wpa
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install cntlm`，再执行 `cntlm --version` 2>/dev/null || `cntlm -V`
- [ ] **2.** **读官方帮助** —— `cntlm -h`，需要细节时 `man cntlm`
- [ ] **3.** **在自有靶场跑最小用例** —— 官方给出的调用形式是：`Usage: cntlm [-AaBcDdFfGgHhILlMNOPpqRrSsTUuvwXx] <proxy_host>[:]<proxy_port> ...`
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/cntlm/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/cntlm/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/cntlm/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
