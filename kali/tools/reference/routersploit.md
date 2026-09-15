# routersploit

> Exploitation Framework for Embedded Devices This package contains an open-source exploitation framework dedicated to embedded devices. It consists of various modules that aids penetration testing operations: exploits - modules that take ad…

> **功能分类**：通用工具 ｜ **Kali 包**：`routersploit` ｜ **官方文档**：<https://www.kali.org/tools/routersploit/>

## 1. 安装

```bash
sudo apt update
sudo apt install routersploit
```

| 项目 | 内容 |
|------|------|
| 版本 | 3.4.7 |
| 架构 | all |
| 可执行命令 | `routersploit`、`rsf.py` |
| 依赖 | `python3`、`python3-paramiko`、`python3-pkg-resources`、`python3-pycryptodome`、`python3-pysnmp4`、`python3-requests`、`python3-zombie-telnetlib` |
| 安装体积 | 2.22 MB |
| 官网 | <https://github.com/threat9/routersploit> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/routersploit> |
| 包追踪 | <https://pkg.kali.org/pkg/routersploit> |

## 2. 官方用法示例

> 以下为 Kali 官方工具页给出的示例与输出原文。

```text
Usage Examples
RouterSploit has a number of exploits for different router models and they have the ability to check whether the remote target is vulnerable before sending off an exploit:
rsf > use exploits/multi/misfortune_cookie
rsf (Misfortune Cookie) > show options

Target options:

   Name       Current settings     Description
   ----       ----------------     -----------
   port       80                   Target port
   target                          Target address e.g. http://192.168.1.1


rsf (Misfortune Cookie) > set target 192.168.0.2
[+] {'target': '192.168.0.2'}
rsf (Misfortune Cookie) > check
[-] Target is not vulnerable
rsf (Misfortune Cookie) >

If stealth is not a requirement, you can attempt to use the autopwn scanner module to see if any vulnerabilities can be found:
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 2 个可执行命令，下面是官方页面内嵌的帮助原文。

### `routersploit`

> 官方示例调用：`routersploit -h`

```text
root@kali:~# routersploit -h
/usr/bin/routersploit -m <module> -s "<option> <value>"
```

### `rsf.py`

> 官方示例调用：`rsf.py -h`

```text
root@kali:~# rsf.py -h
/usr/bin/rsf.py -m <module> -s "<option> <value>"
Updated on: 2025-Dec-09
 Edit this page
routerkeygenpc
rsmangler
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install routersploit`，再执行 `routersploit --version` 2>/dev/null || `routersploit -V`
- [ ] **2.** **读官方帮助** —— `routersploit -h`，需要细节时 `man routersploit`
- [ ] **3.** **在自有靶场跑最小用例** —— 用 `routersploit -h` 里最简单的那个子命令试一次
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/routersploit/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/routersploit/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/routersploit/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
