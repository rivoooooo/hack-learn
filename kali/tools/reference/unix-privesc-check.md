# unix-privesc-check

> Script to check for simple privilege escalation vectors Unix-privesc-checker is a script that runs on Unix systems (tested on Solaris 9, HPUX 11, Various Linuxes, FreeBSD 6.2). It tries to find misconfigurations that could allow local unpr…

> **功能分类**：漏洞分析 ｜ **Kali 包**：`unix-privesc-check` ｜ **官方文档**：<https://www.kali.org/tools/unix-privesc-check/>

## 1. 安装

```bash
sudo apt update
sudo apt install unix-privesc-check
```

| 项目 | 内容 |
|------|------|
| 版本 | 1.6 |
| 架构 | all |
| 可执行命令 | `unix-privesc-check` |
| 安装体积 | 112 KB |
| 官网 | <https://pentestmonkey.net/tools/audit/unix-privesc-check> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/unix-privesc-check> |
| 包追踪 | <https://pkg.kali.org/pkg/unix-privesc-check> |

## 2. 官方用法示例

> 以下为 Kali 官方工具页给出的示例与输出原文。

```text
Usage Example
root@kali:~# unix-privesc-check standard
Assuming the OS is: linux
Starting unix-privesc-check v1.4 ( http://pentestmonkey.net/tools/unix-privesc-check )

This script checks file permissions and other settings that could allow
local users to escalate privileges.

Use of this script is only permitted on systems which you have been granted
legal permission to perform a security assessment of.  Apart from this
condition the GPL v2 applies.

Search the output below for the word 'WARNING'.  If you don't see it then
this script didn't find any problems.


############################################
Recording hostname
############################################
kali

############################################
Recording uname
############################################
Linux kali 3.12-kali1-amd64 #1 SMP Debian 3.12.9-1kali1 (2014-05-13) x86_64 GNU/Linux

############################################
Recording Interface IP addresses
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `unix-privesc-check`

官方给出的调用示例：`unix-privesc-check standard`

```text
root@kali:~# unix-privesc-check standard
Assuming the OS is: linux
Starting unix-privesc-check v1.4 ( http://pentestmonkey.net/tools/unix-privesc-check )
This script checks file permissions and other settings that could allow
local users to escalate privileges.
Use of this script is only permitted on systems which you have been granted
legal permission to perform a security assessment of.  Apart from this
condition the GPL v2 applies.
Search the output below for the word 'WARNING'.  If you don't see it then
this script didn't find any problems.
############################################
Recording hostname
############################################
kali
############################################
Recording uname
############################################
Linux kali 3.12-kali1-amd64 #1 SMP Debian 3.12.9-1kali1 (2014-05-13) x86_64 GNU/Linux
############################################
Recording Interface IP addresses
```

### `unix-privesc-check（示例）`

官方给出的调用示例：`unix-privesc-check -h`

```text
root@kali:~# unix-privesc-check -h
unix-privesc-check v1.6-svn- ( http://pentestmonkey.net/tools/unix-privesc-check )
Usage: unix-privesc-check { standard | detailed }
"standard" mode: Speed-optimised check of lots of security settings.
"detailed" mode: Same as standard mode, but also checks perms of open file
                 handles and called files (e.g. parsed from shell scripts,
                 linked .so files).  This mode is slow and prone to false
                 positives but might help you find more subtle flaws in 3rd
                 party programs.
This script checks file permissions and other settings that could allow
local users to escalate privileges.
Use of this script is only permitted on systems which you have been granted
legal permission to perform a security assessment of.  Apart from this
condition the GPL v2 applies.
Search the output for the word 'WARNING'.  If you don't see it then this
script didn't find any problems.
Learn more with
OffSec
Want to learn more about unix-privesc-check? get access to in-depth training and hands-on labs:
PEN-200: 18.1.3. Linux Privilege Escalation: Automated Enumeration
PEN-200 course
Updated on: 2026-Aug-25
 Edit this page
unblob
unrar-nonfree
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install unix-privesc-check`，再执行 `unix-privesc-check --version` 2>/dev/null || `unix-privesc-check -V`
- [ ] **2.** **读官方帮助** —— `unix-privesc-check -h`，需要细节时 `man unix-privesc-check`
- [ ] **3.** **在自有靶场跑最小用例** —— 官方给出的调用形式是：`Usage: unix-privesc-check { standard | detailed }`
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/unix-privesc-check/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/privilege-escalation.md`](../../tools/by-attack/privilege-escalation.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/unix-privesc-check/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/unix-privesc-check/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
