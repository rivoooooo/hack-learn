# sqlninja

> SQL server injection and takeover tool Fancy going from a SQL Injection on Microsoft SQL Server to a full GUI access on the DB? Take a few new SQL Injection tricks, add a couple of remote shots in the registry to disable Data Execution Pre…

> **功能分类**：Web 应用 ｜ **Kali 包**：`sqlninja` ｜ **官方文档**：<https://www.kali.org/tools/sqlninja/>

## 1. 安装

```bash
sudo apt update
sudo apt install sqlninja
```

| 项目 | 内容 |
|------|------|
| 版本 | 0.2.6 |
| 架构 | all |
| 可执行命令 | `sqlninja` |
| 依赖 | `libio-socket-ip-perl`、`libnet-dns-perl`、`libnet-pcap-perl`、`libnet-rawip-perl`、`libnetpacket-perl`、`perl` |
| 安装体积 | 1.00 MB |
| 官网 | <https://sqlninja.sourceforge.net/> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/sqlninja> |
| 包追踪 | <https://pkg.kali.org/pkg/sqlninja> |

## 2. 官方用法示例

> 以下为 Kali 官方工具页给出的示例与输出原文。

```text
Usage Example
Connect to the target in test mode (-m t) with the specified config file (-f /root/sqlninja.conf):
root@kali:~# sqlninja -m t -f /root/sqlninja.conf
Sqlninja rel. 0.2.6-r1
Copyright (C) 2006-2011 icesurfer <r00t@northernfortress.net>
[+] Parsing /root/sqlninja.conf...
[+] Target is: 192.168.1.51:80
[+] Trying to inject a 'waitfor delay'....
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `sqlninja`

> 官方示例调用：`sqlninja -m t -f /root/sqlninja.conf`

```text
root@kali:~# sqlninja -m t -f /root/sqlninja.conf
Sqlninja rel. 0.2.6-r1
Copyright (C) 2006-2011 icesurfer <
[email protected]
>
[+] Parsing /root/sqlninja.conf...
[+] Target is: 192.168.1.51:80
[+] Trying to inject a 'waitfor delay'....
```

### `sqlninja --help`

> 官方示例调用：`sqlninja --help`

```text
root@kali:~# sqlninja --help
/usr/bin/sqlninja version [unknown] calling Getopt::Std::getopts (version 1.14 [paranoid]),
running under Perl version 5.42.2.
Usage: sqlninja [-OPTIONS [-MORE_OPTIONS]] [--] [PROGRAM_ARG1 ...]
The following single-character options are accepted:
	With arguments: -m -f -p -w -u -d
	Boolean (without arguments): -g -v
Options may be merged together.  -- stops processing of options.
Space is not required between options and their arguments.
  [Now continuing due to backward compatibility and excessive paranoia.
   See 'perldoc Getopt::Std' about $Getopt::Std::STANDARD_HELP_VERSION.]
Usage: /usr/bin/sqlninja
	-m <mode> : Required. Available modes are:
	    t/test - test whether the injection is working
	    f/fingerprint - fingerprint user, xp_cmdshell and more
	    b/bruteforce - bruteforce sa account
	    e/escalation - add user to sysadmin server role
	    x/resurrectxp - try to recreate xp_cmdshell
	    u/upload - upload a .scr file
	    s/dirshell - start a direct shell
	    k/backscan - look for an open outbound port
	    r/revshell - start a reverse shell
	    d/dnstunnel - attempt a dns tunneled shell
	    i/icmpshell - start a reverse ICMP shell
	    c/sqlcmd - issue a 'blind' OS command
	    m/metasploit - wrapper to Metasploit stagers
	-f <file> : configuration file (default: sqlninja.conf)
	-p <password> : sa password
	-w <wordlist> : wordlist to use in bruteforce mode (dictionary method
	                only)
	-g : generate debug script and exit (only valid in upload mode)
	-v : verbose output
	-d <mode> : activate debug
	    1 - print each injected command
	    2 - print each raw HTTP request
	    3 - print each raw HTTP response
	    all - all of the above
	...see sqlninja-howto.html for details
Updated on: 2026-Aug-25
 Edit this page
sqlmap
sslh
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install sqlninja`，再执行 `sqlninja --version` 2>/dev/null || `sqlninja -V`
- [ ] **2.** **读官方帮助** —— `sqlninja -h`，需要细节时 `man sqlninja`
- [ ] **3.** **在自有靶场跑最小用例** —— 官方给出的调用形式是：`Usage: sqlninja [-OPTIONS [-MORE_OPTIONS]] [--] [PROGRAM_ARG1 ...]`
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/sqlninja/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/initial-access.md`](../../tools/by-attack/initial-access.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/sqlninja/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/sqlninja/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
