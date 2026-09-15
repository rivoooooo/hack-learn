# cisco-torch

> Cisco device scanner The main feature that makes cisco-torch different from similar tools is the extensive use of forking to launch multiple scanning processes on the background for maximum scanning efficiency. Also, it uses several method…

> **功能分类**：漏洞分析 ｜ **Kali 包**：`cisco-torch` ｜ **官方文档**：<https://www.kali.org/tools/cisco-torch/>

## 1. 安装

```bash
sudo apt update
sudo apt install cisco-torch
```

| 项目 | 内容 |
|------|------|
| 版本 | 0.4b |
| 架构 | all |
| 可执行命令 | `cisco-torch` |
| 依赖 | `libnet-snmp-perl`、`libnet-ssh2-perl`、`libnet-telnet-perl`、`perl` |
| 安装体积 | 117 KB |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/cisco-torch> |
| 包追踪 | <https://pkg.kali.org/pkg/cisco-torch> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
cisco-torch -h          # 查看用法
man cisco-torch         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `cisco-torch`

官方给出的调用示例：`cisco-torch -A 192.168.99.202`

```text
root@kali:~# cisco-torch -A 192.168.99.202
Using config file torch.conf...
Loading include and plugin ...
###############################################################
#   Cisco Torch Mass Scanner                   #
#   Becase we need it...                                      #
#   http://www.arhont.com/cisco-torch.pl                      #
###############################################################
List of targets contains 1 host(s)
8853:   Checking 192.168.99.202 ...
HUH db not found, it should be in fingerprint.db
Skipping Telnet fingerprint
* Cisco by SNMP found ***
*System Description: Cisco Internetwork Operating System Software
IOS (tm) 3600 Software (C3640-IK9O3S-M), Version 12.3(22), RELEASE SOFTWARE (fc2)
Technical Support: http://www.cisco.com/techsupport
Copyright (c) 1986-2007 by cisco Systems, Inc.
Compiled Wed 24-Jan-07 1
Cisco-IOS Webserver found
 HTTP/1.1 401 Unauthorized
Server: cisco-IOS
Accept-Ranges: none
WWW-Authenticate: Basic realm="level_15_access"
401 Unauthorized
 Cisco WWW-Authenticate webserver found
 HTTP/1.1 401 Unauthorized
Server: cisco-IOS
Accept-Ranges: none
WWW-Authenticate: Basic realm="level_15_access"
401 Unauthorized
--->
- All scans done. Cisco Torch Mass Scanner  -
---> Exiting.
```

### `cisco-torch（示例）`

官方给出的调用示例：`cisco-torch -h`

```text
root@kali:~# cisco-torch -h
Using config file torch.conf...
Loading include and plugin ...
 version
usage: cisco-torch <options> <IP,hostname,network>
or: cisco-torch <options> -F <hostlist>
Available options:
-O <output file>
-A		All fingerprint scan types combined
-t		Cisco Telnetd scan
-s		Cisco SSHd scan
-u		Cisco SNMP scan
-g		Cisco config or tftp file download
-n		NTP fingerprinting scan
-j		TFTP fingerprinting scan
-l <type>	loglevel
		c  critical (default)
		v  verbose
		d  debug
-w		Cisco Webserver scan
-z		Cisco IOS HTTP Authorization Vulnerability Scan
-c		Cisco Webserver with SSL support scan
-b		Password dictionary attack (use with -s, -u, -c, -w , -j or -t only)
-V		Print tool version and exit
examples:	cisco-torch -A 10.10.0.0/16
		cisco-torch -s -b -F sshtocheck.txt
		cisco-torch -w -z 10.10.0.0/16
		cisco-torch -j -b -g -F tftptocheck.txt
Updated on: 2025-Dec-09
 Edit this page
chirp
cisco7crack
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install cisco-torch`，再执行 `cisco-torch --version` 2>/dev/null || `cisco-torch -V`
- [ ] **2.** **读官方帮助** —— `cisco-torch -h`，需要细节时 `man cisco-torch`
- [ ] **3.** **在自有靶场跑最小用例** —— 用 `cisco-torch -h` 里最简单的那个子命令试一次
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/cisco-torch/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/discovery.md`](../../tools/by-attack/discovery.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/cisco-torch/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/cisco-torch/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
