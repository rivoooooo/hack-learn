# dns2tcp

> TCP-over-DNS tunnel server and client dns2tcp is a set of tools to encapsulate a TCP session in DNS packets. This type of encapsulation generates smaller packets than IP-over-DNS, improving throughput. The client does not need root privile…

> **功能分类**：后渗透 ｜ **Kali 包**：`dns2tcp` ｜ **官方文档**：<https://www.kali.org/tools/dns2tcp/>

## 1. 安装

```bash
sudo apt update
sudo apt install dns2tcp
```

| 项目 | 内容 |
|------|------|
| 版本 | 0.5.2 |
| 架构 | any |
| 可执行命令 | `dns2tcp`、`dns2tcpc`、`dns2tcpd` |
| 依赖 | `libc6`、`dns2tcpc` |
| 安装体积 | 152 KB |
| 源码仓库 | <https://salsa.debian.org/debian/dns2tcp> |
| 包追踪 | <https://pkg.kali.org/pkg/dns2tcp> |

## 2. 官方用法示例

> 以下为 Kali 官方工具页给出的示例与输出原文。

```text
Usage Example
root@kali-server:~# cat >>.dns2tcpdrc <<END
listen = 0.0.0.0
port = 53
user=nobody
chroot = /root/dns2tcp
pid_file = /var/run/dns2tcp.pid
domain = dns2tcp.kali.org
key = secretkey
resources = ssh:127.0.0.1:22
END
root@kali-server:~# dns2tcpd -f .dns2tcpdrc
root@kali-server:~#

dns2tcpc Usage Example
root@kali-client:~# cat >>.dns2tcprc <<END
domain = dns2tcp.kali.org
resource = ssh
local_port = 2139
key = secretkey
END
root@kali-client:~# dns2tcpc -f .dns2tcprc
root@kali-client:~# ssh root@localhost -p 2139 -D 8090
The authenticity of host '[localhost]:2139 ([127.0.0.1]:2139)' can't be established.
ECDSA key fingerprint is aa:bb:1f:cc:f1:ab:7c:71:9b:62:37:8c:f1:60:2e:98.
Are you sure you want to continue connecting (yes/no)? yes
Warning: Permanently added '[localhost]:2139' (ECDSA) to the list of known hosts.
root@localhost's password:
Linux flw 3.12-kali1-amd64 #1 SMP Debian 3.12.6-2kali1 (2014-01-06) x86_64

The programs included with the Kali GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Kali GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
Last login: Tue May  6 22:54:15 2014 from beast.fritz.box
root@kali-server:~#

dns2tcpc Example Details
In this case we are going to tunnel some traffic from a client behind a perimeter firewall to our own server. Since dns2tcp is using dns (asking for TXT records within a (sub)domain) to archive the goal we need to create a NS record for a new subdomain pointing to the address of our server.
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 3 个可执行命令，下面是官方页面内嵌的帮助原文。

### `dns2tcpc`

> 官方示例调用：`dns2tcpc -h`

```text
root@kali:~# dns2tcpc -h
dns2tcpc: option requires an argument -- 'h'
dns2tcp v0.5.2 ( http://www.hsc.fr/ )
Usage : dns2tcpc [options] [server]
	-c         	: enable compression
	-z <domain>	: domain to use (mandatory)
	-d <1|2|3>	: debug_level (1, 2 or 3)
	-r <resource>	: resource to access
	-k <key>	: pre-shared key
	-f <filename>	: configuration file
	-l <port|->	: local port to bind, '-' is for stdin (mandatory if resource defined without program )
	-e <program>	: program to execute
	-t <delay>	: max DNS server's answer delay in seconds (default is 3)
	-T <TXT|KEY>	: DNS request type (default is TXT)
	server	: DNS server to use
	If no resources are specified, available resources will be printed
```

### `dns2tcpd`

> 官方示例调用：`dns2tcpd --help`

```text
root@kali:~# dns2tcpd --help
dns2tcpd: invalid option -- '-'
Usage : dns2tcpd [ -i IP ] [ -F ] [ -d debug_level ] [ -f config-file ] [ -p pidfile ]
	 -F : dns2tcpd will run in foreground
Updated on: 2025-Dec-09
 Edit this page
dmitry
dnschef
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install dns2tcp`，再执行 `dns2tcp --version` 2>/dev/null || `dns2tcp -V`
- [ ] **2.** **读官方帮助** —— `dns2tcp -h`，需要细节时 `man dns2tcp`
- [ ] **3.** **在自有靶场跑最小用例** —— 官方给出的调用形式是：`Usage : dns2tcpc [options] [server]`
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/dns2tcp/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/command-and-control.md`](../../tools/by-attack/command-and-control.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/dns2tcp/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/dns2tcp/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
