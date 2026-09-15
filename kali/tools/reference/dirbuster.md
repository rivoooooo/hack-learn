# dirbuster

> Web server directory brute-forcer DirBuster is a multi threaded java application designed to brute force directories and files names on web/application servers. Often is the case now of what looks like a web server in a state of default in…

> **功能分类**：信息搜集 ｜ **Kali 包**：`dirbuster` ｜ **官方文档**：<https://www.kali.org/tools/dirbuster/>

## 1. 安装

```bash
sudo apt update
sudo apt install dirbuster
```

| 项目 | 内容 |
|------|------|
| 版本 | 1.0 |
| 架构 | all |
| 可执行命令 | `dirbuster` |
| 依赖 | `default-jre` |
| 安装体积 | 10.75 MB |
| 官网 | <https://www.owasp.org/index.php/Category:OWASP_DirBuster_Project> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/dirbuster> |
| 包追踪 | <https://pkg.kali.org/pkg/dirbuster> |

## 2. 官方用法示例

> 以下为 Kali 官方工具页给出的示例与输出原文。

```text
Screenshots
dirbuster
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `dirbuster`

官方给出的调用示例：`dirbuster -h`

```text
root@kali:~# dirbuster -h
DirBuster - 1.0-RC1
Usage: java -jar DirBuster-1.0-RC1 -u <URL http://example.com/> [Options]
	Options:
	 -h : Display this help message
	 -H : Start DirBuster in headless mode (no gui), report will be auto saved on exit
	 -l <Word list to use> : The Word list to use for the list based brute force. Default: /home/kali/kali-www/bin/kali-tools/tool-output/dirbuster/directory-list-2.3-small.txt
	 -g : Only use GET requests. Default Not Set
	 -e <File Extention list> : File Extention list eg asp,aspx. Default: php
	 -t <Number of Threads> : Number of connection threads to use. Default: 10
	 -s <Start point> : Start point of the scan. Default: /
	 -v : Verbose output, Default: Not set
	 -P : Don't Parse html, Default: Not Set
	 -R : Don't be recursive, Default: Not Set
	 -r <location> : File to save report to. Default: /home/kali/kali-www/bin/kali-tools/tool-output/dirbuster/DirBuster-Report-[hostname]-[port].txt
Examples:
Run DirBuster in headless mode
java -jar DirBuster-1.0-RC1.jar -H -u https://www.target.com/
Start GUI with target prepopulated
java -jar DirBuster-1.0-RC1.jar -u https://www.target.com/
Learn more with
OffSec
Want to learn more about dirbuster? get access to in-depth training and hands-on labs:
WEB-200 course
PEN-200 course
Updated on: 2025-Dec-09
 Edit this page
dcfldd
dirsearch
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install dirbuster`，再执行 `dirbuster --version` 2>/dev/null || `dirbuster -V`
- [ ] **2.** **读官方帮助** —— `dirbuster -h`，需要细节时 `man dirbuster`
- [ ] **3.** **在自有靶场跑最小用例** —— 官方给出的调用形式是：`Usage: java -jar DirBuster-1.0-RC1 -u <URL http://example.com/> [Options]`
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/dirbuster/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- **精讲教程**（含原理、参数详解、靶场实操与输出解读）：[dirb](../../tools/tutorials/03-Web应用/dirb.md)
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/reconnaissance.md`](../../tools/by-attack/reconnaissance.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/dirbuster/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/dirbuster/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
