# smtp-user-enum

> Username guessing tool for the SMTP service Username guessing tool primarily for use against the default Solaris SMTP service. Can use either EXPN, VRFY or RCPT TO.

> **功能分类**：信息搜集 ｜ **Kali 包**：`smtp-user-enum` ｜ **官方文档**：<https://www.kali.org/tools/smtp-user-enum/>

## 1. 安装

```bash
sudo apt update
sudo apt install smtp-user-enum
```

| 项目 | 内容 |
|------|------|
| 版本 | 1.2 |
| 架构 | all |
| 可执行命令 | `smtp-user-enum` |
| 依赖 | `libio-socket-ip-perl`、`libsocket-perl`、`perl` |
| 安装体积 | 98 KB |
| 官网 | <http://pentestmonkey.net/tools/user-enumeration/smtp-user-enum> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/smtp-user-enum> |
| 包追踪 | <https://pkg.kali.org/pkg/smtp-user-enum> |

## 2. 官方用法示例

> 以下为 Kali 官方工具页给出的示例与输出原文。

```text
Usage Example
Use the VRFY method (-M VRFY) to search for the specified user (-u root) on the target server (-t 192.168.1.25):
root@kali:~# smtp-user-enum -M VRFY -u root -t 192.168.1.25
Starting smtp-user-enum v1.2 ( http://pentestmonkey.net/tools/smtp-user-enum )

 ----------------------------------------------------------
|                   Scan Information                       |
 ----------------------------------------------------------

Mode ..................... VRFY
Worker Processes ......... 5
Target count ............. 1
Username count ........... 1
Target TCP port .......... 25
Query timeout ............ 5 secs
Target domain ............

######## Scan started at Tue May 13 16:06:28 2014 #########
192.168.1.25: root exists
######## Scan completed at Tue May 13 16:06:29 2014 #########
1 results.

1 queries in 1 seconds (1.0 queries / sec)
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `smtp-user-enum`

官方给出的调用示例：`smtp-user-enum -M VRFY -u root -t 192.168.1.25`

```text
root@kali:~# smtp-user-enum -M VRFY -u root -t 192.168.1.25
Starting smtp-user-enum v1.2 ( http://pentestmonkey.net/tools/smtp-user-enum )
 ----------------------------------------------------------
|                   Scan Information                       |
 ----------------------------------------------------------
Mode ..................... VRFY
Worker Processes ......... 5
Target count ............. 1
Username count ........... 1
Target TCP port .......... 25
Query timeout ............ 5 secs
Target domain ............
######## Scan started at Tue May 13 16:06:28 2014 #########
192.168.1.25: root exists
######## Scan completed at Tue May 13 16:06:29 2014 #########
1 results.
1 queries in 1 seconds (1.0 queries / sec)
```

### `smtp-user-enum（示例）`

官方给出的调用示例：`smtp-user-enum -h`

```text
root@kali:~# smtp-user-enum -h
smtp-user-enum v1.2 ( http://pentestmonkey.net/tools/smtp-user-enum )
Usage: smtp-user-enum [options] ( -u username | -U file-of-usernames ) ( -t host | -T file-of-targets )
options are:
        -m n     Maximum number of processes (default: 5)
	-M mode  Method to use for username guessing EXPN, VRFY or RCPT (default: VRFY)
	-u user  Check if user exists on remote system
	-f addr  MAIL FROM email address.  Used only in "RCPT TO" mode (default:
[email protected]
)
        -D dom   Domain to append to supplied user list to make email addresses (Default: none)
                 Use this option when you want to guess valid email addresses instead of just usernames
                 e.g. "-D example.com" would guess
[email protected]
,
[email protected]
, etc.  Instead of
                      simply the usernames foo and bar.
	-U file  File of usernames to check via smtp service
	-t host  Server host running smtp service
	-T file  File of hostnames running the smtp service
	-p port  TCP port on which smtp service runs (default: 25)
	-d       Debugging output
	-w n     Wait a maximum of n seconds for reply (default: 5)
	-v       Verbose
	-h       This help message
Also see smtp-user-enum-user-docs.pdf from the smtp-user-enum tar ball.
Examples:
$ smtp-user-enum -M VRFY -U users.txt -t 10.0.0.1
$ smtp-user-enum -M EXPN -u admin1 -t 10.0.0.1
$ smtp-user-enum -M RCPT -U users.txt -T mail-server-ips.txt
$ smtp-user-enum -M EXPN -D example.com -U users.txt -t 10.0.0.1
Updated on: 2025-Dec-09
 Edit this page
smbmap
sniffjoke
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install smtp-user-enum`，再执行 `smtp-user-enum --version` 2>/dev/null || `smtp-user-enum -V`
- [ ] **2.** **读官方帮助** —— `smtp-user-enum -h`，需要细节时 `man smtp-user-enum`
- [ ] **3.** **在自有靶场跑最小用例** —— 官方给出的调用形式是：`Usage: smtp-user-enum [options] ( -u username | -U file-of-usernames ) ( -t host | -T file-of-targets )`
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/smtp-user-enum/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/discovery.md`](../../tools/by-attack/discovery.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/smtp-user-enum/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/smtp-user-enum/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
