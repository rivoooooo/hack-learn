# gobuster

> High-performance discovery tool for directories, DNS and cloud storage Gobuster is a high-performance tool used to brute-force and discover: URIs (directories and files) in web sites DNS subdomains (with wildcard support) Virtual Host name…

> **功能分类**：通用工具 ｜ **Kali 包**：`gobuster` ｜ **官方文档**：<https://www.kali.org/tools/gobuster/>

## 1. 安装

```bash
sudo apt update
sudo apt install gobuster
```

| 项目 | 内容 |
|------|------|
| 版本 | 3.8.2 |
| 架构 | any |
| 可执行命令 | `gobuster` |
| 依赖 | `libc6` |
| 安装体积 | 9.17 MB |
| 官网 | <https://github.com/OJ/gobuster> |
| 源码仓库 | <https://salsa.debian.org/pkg-security-team/gobuster> |
| 包追踪 | <https://pkg.kali.org/pkg/gobuster> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
gobuster -h          # 查看用法
man gobuster         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `gobuster`

> 官方示例调用：`gobuster -h`

```text
root@kali:~# gobuster -h
NAME:
   gobuster - the tool you love
USAGE:
   gobuster command [command options]
VERSION:
   3.8.2
AUTHORS:
   Christian Mehlmauer (@firefart)
   OJ Reeves (@TheColonial)
COMMANDS:
   dir      Uses directory/file enumeration mode
   vhost    Uses VHOST enumeration mode (you most probably want to use the IP address as the URL parameter)
   dns      Uses DNS subdomain enumeration mode
   fuzz     Uses fuzzing mode. Replaces the keyword FUZZ in the URL, Headers and the request body
   tftp     Uses TFTP enumeration mode
   s3       Uses aws bucket enumeration mode
   gcs      Uses gcs bucket enumeration mode
   help, h  Shows a list of commands or help for one command
GLOBAL OPTIONS:
   --help, -h     show help
   --version, -v  print the version
Learn more with
OffSec
Want to learn more about gobuster? get access to in-depth training and hands-on labs:
PEN-200: 8. Introduction to Web Application Attacks
PEN-200: 6.5.1. Information Gathering: Active LLM-Aided enumeration
PEN-200 course
WEB-200 course
Updated on: 2026-Mar-02
 Edit this page
gitxray
gpp-decrypt
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install gobuster`，再执行 `gobuster --version` 2>/dev/null || `gobuster -V`
- [ ] **2.** **读官方帮助** —— `gobuster -h`，需要细节时 `man gobuster`
- [ ] **3.** **在自有靶场跑最小用例** —— 用 `gobuster -h` 里最简单的那个子命令试一次
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/gobuster/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- **精讲教程**（含原理、参数详解、靶场实操与输出解读）：[gobuster](../../tools/tutorials/03-Web应用/gobuster.md)
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/reconnaissance.md`](../../tools/by-attack/reconnaissance.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/gobuster/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/gobuster/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
