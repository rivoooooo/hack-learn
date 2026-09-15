# creddump7

> Python tool to extract credentials and secrets from Windows registry hives This package contains a Python tool to extract various credentials and secrets from Windows registry hives. It’s based on the creddump program. Many patches and fix…

> **功能分类**：口令攻击 ｜ **Kali 包**：`creddump7` ｜ **官方文档**：<https://www.kali.org/tools/creddump7/>

## 1. 安装

```bash
sudo apt update
sudo apt install creddump7
```

| 项目 | 内容 |
|------|------|
| 版本 | 0.1 |
| 架构 | all |
| 可执行命令 | `creddump7` |
| 依赖 | `python3`、`python3-pycryptodome`、`tree` |
| 安装体积 | 78 KB |
| 官网 | <https://github.com/CiscoCXSecurity/creddump7> |
| 源码仓库 | <https://salsa.debian.org/pkg-security-team/creddump7> |
| 包追踪 | <https://pkg.kali.org/pkg/creddump7> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
creddump7 -h          # 查看用法
man creddump7         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `creddump7`

官方给出的调用示例：`creddump7 -h`

```text
root@kali:~# creddump7 -h
creddump7 - Python tool to extract credentials and secrets from Windows registry hives
/usr/share/creddump7
|-- __pycache__
|-- cachedump.py
|-- framework
|-- lsadump.py
`-- pwdump.py
Learn more with
OffSec
Want to learn more about creddump7? get access to in-depth training and hands-on labs:
PEN-300: 16.1.1. Windows Credentials: SAM Database
MITRE ATT&CK - Credential Access (TA0006): 5. Windows Credentials
PEN-300 course
Updated on: 2025-Dec-09
 Edit this page
crackle
crlfuzz
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install creddump7`，再执行 `creddump7 --version` 2>/dev/null || `creddump7 -V`
- [ ] **2.** **读官方帮助** —— `creddump7 -h`，需要细节时 `man creddump7`
- [ ] **3.** **在自有靶场跑最小用例** —— 用 `creddump7 -h` 里最简单的那个子命令试一次
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/creddump7/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/credential-access.md`](../../tools/by-attack/credential-access.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/creddump7/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/creddump7/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
