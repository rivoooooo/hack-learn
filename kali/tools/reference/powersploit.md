# powersploit

> PowerShell Post-Exploitation Framework PowerSploit is a series of Microsoft PowerShell scripts that can be used in post-exploitation scenarios during authorized penetration tests.

> **功能分类**：后渗透 ｜ **Kali 包**：`powersploit` ｜ **官方文档**：<https://www.kali.org/tools/powersploit/>

## 1. 安装

```bash
sudo apt update
sudo apt install powersploit
```

| 项目 | 内容 |
|------|------|
| 版本 | 3.0.0 |
| 架构 | all |
| 可执行命令 | `powersploit` |
| 依赖 | `kali-defaults` |
| 安装体积 | 5.46 MB |
| 官网 | <https://github.com/PowerShellMafia/PowerSploit> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/powersploit> |
| 包追踪 | <https://pkg.kali.org/pkg/powersploit> |

## 2. 官方用法示例

> 以下为 Kali 官方工具页给出的示例与输出原文。

```text
Usage Example
root@kali:~# ls -l /usr/share/powersploit/
total 52
drwxr-xr-x 2 root root 4096 Feb 11 15:10 AntivirusBypass
drwxr-xr-x 3 root root 4096 Feb 11 15:10 CodeExecution
drwxr-xr-x 2 root root 4096 Feb 11 15:10 Exfiltration
drwxr-xr-x 2 root root 4096 Feb 11 15:10 Persistence
drwxr-xr-x 2 root root 4096 Feb 11 15:10 PETools
-rw-r--r-- 1 root root 3542 Jun 11  2013 PowerSploit.psd1
-rw-r--r-- 1 root root   89 Jun 11  2013 PowerSploit.psm1
-rw-r--r-- 1 root root 8900 Jun 11  2013 README.md
drwxr-xr-x 3 root root 4096 Feb 11 15:10 Recon
drwxr-xr-x 2 root root 4096 Feb 11 15:10 ReverseEngineering
drwxr-xr-x 2 root root 4096 Feb 11 15:10 ScriptModification
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `ls`

官方给出的调用示例：`ls -l /usr/share/powersploit/`

```text
root@kali:~# ls -l /usr/share/powersploit/
total 52
drwxr-xr-x 2 root root 4096 Feb 11 15:10 AntivirusBypass
drwxr-xr-x 3 root root 4096 Feb 11 15:10 CodeExecution
drwxr-xr-x 2 root root 4096 Feb 11 15:10 Exfiltration
drwxr-xr-x 2 root root 4096 Feb 11 15:10 Persistence
drwxr-xr-x 2 root root 4096 Feb 11 15:10 PETools
-rw-r--r-- 1 root root 3542 Jun 11  2013 PowerSploit.psd1
-rw-r--r-- 1 root root   89 Jun 11  2013 PowerSploit.psm1
-rw-r--r-- 1 root root 8900 Jun 11  2013 README.md
drwxr-xr-x 3 root root 4096 Feb 11 15:10 Recon
drwxr-xr-x 2 root root 4096 Feb 11 15:10 ReverseEngineering
drwxr-xr-x 2 root root 4096 Feb 11 15:10 ScriptModification
```

### `powersploit`

官方给出的调用示例：`powersploit -h`

```text
root@kali:~# powersploit -h
> powersploit ~ PowerShell Post-Exploitation Framework
/usr/share/windows-resources/powersploit
|-- AntivirusBypass
|-- CodeExecution
|-- Exfiltration
|-- Mayhem
|-- Persistence
|-- PowerSploit.psd1
|-- PowerSploit.psm1
|-- Privesc
|-- README.md
|-- Recon
|-- ScriptModification
`-- Tests
Learn more with
OffSec
Want to learn more about powersploit? get access to in-depth training and hands-on labs:
PEN-200: 17.2.1. Windows Privilege Escalation: Service Binary Hijacking
PEN-200 course
Updated on: 2025-Dec-09
 Edit this page
powercat
princeprocessor
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install powersploit`，再执行 `powersploit --version` 2>/dev/null || `powersploit -V`
- [ ] **2.** **读官方帮助** —— `powersploit -h`，需要细节时 `man powersploit`
- [ ] **3.** **在自有靶场跑最小用例** —— 用 `powersploit -h` 里最简单的那个子命令试一次
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/powersploit/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/execution.md`](../../tools/by-attack/execution.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/powersploit/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/powersploit/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
