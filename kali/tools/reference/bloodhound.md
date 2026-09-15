# bloodhound

> Six Degrees of Domain Admin, BloodHound CE This package contains BloodHound Community Edition, a single page Javascript web application. BloodHound uses graph theory to reveal the hidden and often unintended relationships within an Active …

> **功能分类**：通用工具 ｜ **Kali 包**：`bloodhound` ｜ **官方文档**：<https://www.kali.org/tools/bloodhound/>

## 1. 安装

```bash
sudo apt update
sudo apt install bloodhound
```

| 项目 | 内容 |
|------|------|
| 版本 | 9.7.0~rc4 |
| 架构 | amd64 |
| 可执行命令 | `bloodhound`、`bloodhound-setup`、`bloodhound-start`、`bloodhound-stop` |
| 依赖 | `curl`、`kali-defaults`、`neo4j`、`postgresql` |
| 安装体积 | 297.32 MB |
| 官网 | <https://github.com/SpecterOps/BloodHound> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/bloodhound> |
| 包追踪 | <https://pkg.kali.org/pkg/bloodhound> |

## 2. 官方用法示例

> 以下为 Kali 官方工具页给出的示例与输出原文。

```text
How to install and run Bloodhound
Update your package list and install BloodHound from the official Kali repository::
┌──(kali㉿kali)-[~]
└─$ sudo apt update && sudo apt install -y bloodhound

After installation, run BloodHound’s configuration script:
┌──(kali㉿kali)-[~]
└─$ sudo bloodhound-setup

This will initialize the necessary services and configurations.
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 4 个可执行命令，下面是官方页面内嵌的帮助原文。

### `bloodhound`

> 官方示例调用：`bloodhound -h`

```text
root@kali:~# bloodhound -h
┏━(Message from Kali developers)
┃
┃ The command bloodhound is deprecated. Please use bloodhound-start instead.
┃
┗━
```

### `bloodhound-setup`

> 官方示例调用：`bloodhound-setup -h`

```text
root@kali:~# bloodhound-setup -h
 [*] Starting PostgreSQL service
 [*] Creating Database
User _bloodhound already exists in PostgreSQL
 Creating database
```

### `bloodhound-start`

> 官方示例调用：`bloodhound-start -h`

```text
root@kali:~# bloodhound-start -h
It seems it's the first time you run bloodhound
Please run bloodhound-setup first
```

### `bloodhound-stop`

> 官方示例调用：`bloodhound-stop -h`

```text
root@kali:~# bloodhound-stop -h
┏━(Message from Kali developers)
┃
┃ Service status:
┃   * bloodhound.service - Bloodhound service
┃        Loaded: loaded (/usr/lib/systemd/system/bloodhound.service; 5:185mdisabled; preset: 5:185mdisabled)
┃        Active: inactive (dead)
┃
┗━
Neo4j is not running.
Learn more with
OffSec
Want to learn more about bloodhound? get access to in-depth training and hands-on labs:
PEN-200: 22. Active Directory Introduction and Enumeration
PEN-300: 21.5.2. Active Directory Exploitation: Enumeration Beyond the Forest
PEN-200 course
PEN-300 course
Updated on: 2026-Aug-25
 Edit this page
binwalk
bloodyad
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install bloodhound`，再执行 `bloodhound --version` 2>/dev/null || `bloodhound -V`
- [ ] **2.** **读官方帮助** —— `bloodhound -h`，需要细节时 `man bloodhound`
- [ ] **3.** **在自有靶场跑最小用例** —— 用 `bloodhound -h` 里最简单的那个子命令试一次
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/bloodhound/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- **精讲教程**（含原理、参数详解、靶场实操与输出解读）：[bloodhound](../../tools/tutorials/08-后渗透/bloodhound.md)
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/discovery.md`](../../tools/by-attack/discovery.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/bloodhound/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/bloodhound/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
