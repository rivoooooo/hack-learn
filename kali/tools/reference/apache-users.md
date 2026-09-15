# apache-users

> Enumerate usernames on systems with Apache UserDir module This Perl script will enumerate the usernames on any system that uses Apache with the UserDir module.

> **功能分类**：Web 应用 ｜ **Kali 包**：`apache-users` ｜ **官方文档**：<https://www.kali.org/tools/apache-users/>

## 1. 安装

```bash
sudo apt update
sudo apt install apache-users
```

| 项目 | 内容 |
|------|------|
| 版本 | 2.1 |
| 架构 | any |
| 可执行命令 | `apache-users` |
| 依赖 | `libio-all-lwp-perl`、`libio-socket-ip-perl`、`libparallel-forkmanager-perl` |
| 安装体积 | 13 KB |
| 官网 | <https://labs.portcullis.co.uk/downloads/> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/apache-users> |
| 包追踪 | <https://pkg.kali.org/pkg/apache-users> |

## 2. 官方用法示例

> 以下为 Kali 官方工具页给出的示例与输出原文。

```text
Usage Example
Run against the remote host (-h 192.168.1.202), passing a dictionary of usernames (-l /usr/share/wordlists/metasploit/unix_users.txt), the port to use (-p 80), disable SSL (-s 0), specify the HTTP error code (-e 403), using 10 threads (-t 10):
root@kali:~# apache-users -h 192.168.1.202 -l /usr/share/wordlists/metasploit/unix_users.txt -p 80 -s 0 -e 403 -t 10
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `apache-users`

> 官方示例调用：`apache-users -h 192.168.1.202 -l /usr/share/wordlists/metasploit/unix_users.txt -p 80 -s 0 -e 403 -t 10`

```text
root@kali:~# apache-users -h 192.168.1.202 -l /usr/share/wordlists/metasploit/unix_users.txt -p 80 -s 0 -e 403 -t 10
```

### `apache-users -h`

> 官方示例调用：`apache-users -h`

```text
root@kali:~# apache-users -h
USAGE: apache-users [-h 1.2.3.4] [-l names] [-p 80] [-s (SSL Support 1=true 0=false)] [-e 403 (http code)] [-t threads]
Updated on: 2025-Dec-09
 Edit this page
android-sdk-meta
apple-bleee
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install apache-users`，再执行 `apache-users --version` 2>/dev/null || `apache-users -V`
- [ ] **2.** **读官方帮助** —— `apache-users -h`，需要细节时 `man apache-users`
- [ ] **3.** **在自有靶场跑最小用例** —— 用 `apache-users -h` 里最简单的那个子命令试一次
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/apache-users/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/discovery.md`](../../tools/by-attack/discovery.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/apache-users/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/apache-users/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
