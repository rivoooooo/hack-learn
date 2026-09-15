# cisco-auditing-tool

> Scans Cisco routers for vulnerabilities Perl script which scans cisco routers for common vulnerabilities.

> **功能分类**：漏洞分析 ｜ **Kali 包**：`cisco-auditing-tool` ｜ **官方文档**：<https://www.kali.org/tools/cisco-auditing-tool/>

## 1. 安装

```bash
sudo apt update
sudo apt install cisco-auditing-tool
```

| 项目 | 内容 |
|------|------|
| 版本 | 1.0 |
| 架构 | all |
| 可执行命令 | `cisco-auditing-tool` |
| 依赖 | `perl` |
| 安装体积 | 266 KB |
| 官网 | <http://www.scrypt.net/> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/cisco-auditing-tool> |
| 包追踪 | <https://pkg.kali.org/pkg/cisco-auditing-tool> |

## 2. 官方用法示例

> 以下为 Kali 官方工具页给出的示例与输出原文。

```text
Usage Example
Scan the host (-h 192.168.99.230) on port 23 (-p 23), using a password dictionary file (-a /usr/share/wordlists/nmap.lst):
root@kali:~# CAT -h 192.168.99.230 -p 23 -a /usr/share/wordlists/nmap.lst

Cisco Auditing Tool - g0ne [null0]

Checking Host: 192.168.99.230


Guessing passwords:

Invalid Password: 123456
Invalid Password: 12345
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `CAT`

> 官方示例调用：`CAT -h 192.168.99.230 -p 23 -a /usr/share/wordlists/nmap.lst`

```text
root@kali:~# CAT -h 192.168.99.230 -p 23 -a /usr/share/wordlists/nmap.lst
Cisco Auditing Tool - g0ne [null0]
Checking Host: 192.168.99.230
Guessing passwords:
Invalid Password: 123456
Invalid Password: 12345
```

### `CAT --help`

> 官方示例调用：`CAT --help`

```text
root@kali:~# CAT --help
/usr/bin/CAT version [unknown] calling Getopt::Std::getopts (version 1.14 [paranoid]),
running under Perl version 5.42.2.
Usage: CAT [-OPTIONS [-MORE_OPTIONS]] [--] [PROGRAM_ARG1 ...]
The following single-character options are accepted:
	With arguments: -h -f -p -w -a -l
	Boolean (without arguments): -i -q
Options may be merged together.  -- stops processing of options.
Space is not required between options and their arguments.
  [Now continuing due to backward compatibility and excessive paranoia.
   See 'perldoc Getopt::Std' about $Getopt::Std::STANDARD_HELP_VERSION.]
Updated on: 2026-Aug-25
 Edit this page
chromium
clamav
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install cisco-auditing-tool`，再执行 `cisco-auditing-tool --version` 2>/dev/null || `cisco-auditing-tool -V`
- [ ] **2.** **读官方帮助** —— `cisco-auditing-tool -h`，需要细节时 `man cisco-auditing-tool`
- [ ] **3.** **在自有靶场跑最小用例** —— 官方给出的调用形式是：`Usage: CAT [-OPTIONS [-MORE_OPTIONS]] [--] [PROGRAM_ARG1 ...]`
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/cisco-auditing-tool/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/reconnaissance.md`](../../tools/by-attack/reconnaissance.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/cisco-auditing-tool/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/cisco-auditing-tool/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
