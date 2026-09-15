# ismtp

> SMTP user enumeration and testing tool Test for SMTP user enumeration (RCPT TO and VRFY), internal spoofing, and relay.

> **功能分类**：通用工具 ｜ **Kali 包**：`ismtp` ｜ **官方文档**：<https://www.kali.org/tools/ismtp/>

## 1. 安装

```bash
sudo apt update
sudo apt install ismtp
```

| 项目 | 内容 |
|------|------|
| 版本 | 1.6 |
| 架构 | all |
| 可执行命令 | `ismtp` |
| 依赖 | `python3` |
| 安装体积 | 40 KB |
| 官网 | <https://github.com/altjx/ipwn/> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/ismtp> |
| 包追踪 | <https://pkg.kali.org/pkg/ismtp> |

## 2. 官方用法示例

> 以下为 Kali 官方工具页给出的示例与输出原文。

```text
Usage Example
Test a list of IPs from a file (-f smtp-ips.txt) enumerating usernames from a dictionary file (-e /usr/share/wordlists/metasploit/unix_users.txt):
root@kali:~# ismtp -f smtp-ips.txt -e /usr/share/wordlists/metasploit/unix_users.txt

 ---------------------------------------------------------------------
  iSMTP v1.6 - SMTP Server Tester, Alton Johnson (alton.jx@gmail.com)
 ---------------------------------------------------------------------

 Testing SMTP server [user enumeration]: 192.168.1.25:25
 Emails provided for testing: 109

 Performing SMTP VRFY test...

 [-] 4Dgifts ------------- [ invalid ]
 [-] EZsetup ------------- [ invalid ]
 [+] ROOT ---------------- [ success ]
 [+] adm ----------------- [ success ]
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `ismtp`

> 官方示例调用：`ismtp -f smtp-ips.txt -e /usr/share/wordlists/metasploit/unix_users.txt`

```text
root@kali:~# ismtp -f smtp-ips.txt -e /usr/share/wordlists/metasploit/unix_users.txt
 ---------------------------------------------------------------------
  iSMTP v1.6 - SMTP Server Tester, Alton Johnson (
[email protected]
)
 ---------------------------------------------------------------------
 Testing SMTP server [user enumeration]: 192.168.1.25:25
 Emails provided for testing: 109
 Performing SMTP VRFY test...
 [-] 4Dgifts ------------- [ invalid ]
 [-] EZsetup ------------- [ invalid ]
 [+] ROOT ---------------- [ success ]
 [+] adm ----------------- [ success ]
```

### `ismtp -h`

> 官方示例调用：`ismtp -h`

```text
root@kali:~# ismtp -h
 Error: option -h requires argument
 ---------------------------------------------------------------------
  iSMTP v1.6 - SMTP Server Tester, Alton Johnson (
[email protected]
)
 ---------------------------------------------------------------------
 Usage: ./iSMTP.py <OPTIONS>
 Required:
	-f <import file>	Imports a list of SMTP servers for testing.
				(Cannot use with '-h'.)
	-h <host>		The target IP and port (IP:port).
				(Cannot use with '-f'.)
 Spoofing:
	-i <consultant email>	The consultant's email address.
	-s <sndr email>		The sender's email address.
	-r <rcpt email>		The recipient's email address.
	   --sr <email>		Specifies both the sender's and recipient's email address.
	-S <sndr name>		The sender's first and last name.
	-R <rcpt name>		The recipient's first and last name.
	   --SR <name>		Specifies both the sender's and recipient's first and last name.
	-m			Enables SMTP spoof testing.
	-a			Includes .txt attachment with spoofed email.
 SMTP enumeration:
	-e <file>	Enable SMTP user enumeration testing and imports email list.
	-l <1|2|3>	Specifies enumeration type (1 = VRFY, 2 = RCPT TO, 3 = all).
			(Default is 3.)
 SMTP relay:
	-i <consultant email>	The consultant's email address.
	-x			Enables SMTP external relay testing.
 Misc:
	-t <secs>	The timeout value. (Default is 10.)
	-o		Creates "ismtp-results" directory and writes output to
			ismtp-results/smtp_<service>_<ip>(port).txt
 Note: Any combination of options is supported (e.g., enumeration, relay, both, all, etc.).
Updated on: 2025-Dec-09
 Edit this page
irpas
iw
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install ismtp`，再执行 `ismtp --version` 2>/dev/null || `ismtp -V`
- [ ] **2.** **读官方帮助** —— `ismtp -h`，需要细节时 `man ismtp`
- [ ] **3.** **在自有靶场跑最小用例** —— 官方给出的调用形式是：`Usage: ./iSMTP.py <OPTIONS>`
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/ismtp/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/ismtp/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/ismtp/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
