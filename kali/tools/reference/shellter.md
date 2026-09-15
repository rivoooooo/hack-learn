# shellter

> Dynamic shellcode injection tool and dynamic PE infector Shellter is a dynamic shellcode injection tool aka dynamic PE infector. It can be used in order to inject shellcode into native Windows applications (currently 32-bit apps only). The…

> **功能分类**：后渗透 ｜ **Kali 包**：`shellter` ｜ **官方文档**：<https://www.kali.org/tools/shellter/>

## 1. 安装

```bash
sudo apt update
sudo apt install shellter
```

| 项目 | 内容 |
|------|------|
| 版本 | 7.2 |
| 架构 | i386 |
| 可执行命令 | `shellter` |
| 依赖 | `kali-defaults`、`wine` |
| 安装体积 | 726 KB |
| 官网 | <https://www.shellterproject.com/> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/shellter> |
| 包追踪 | <https://pkg.kali.org/pkg/shellter> |

## 2. 官方用法示例

> 以下为 Kali 官方工具页给出的示例与输出原文。

```text
Usage Examples
root@kali:~# dpkg --add-architecture i386
root@kali:~# apt update && apt install wine32
root@kali:~# shellter
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `dpkg`

> 官方示例调用：`dpkg --add-architecture i386`

```text
root@kali:~# dpkg --add-architecture i386
```

### `apt`

> 官方示例调用：`apt update && apt install wine32`

```text
root@kali:~# apt update && apt install wine32
```

### `shellter`

```text
root@kali:~# shellter
```

### `shellter -h`

> 官方示例调用：`shellter -h`

```text
root@kali:~# shellter -h
┏━(Message from Kali developers)
┃
┃ You may need to install the wine32 package first:
┃  # dpkg --add-architecture i386 && apt update && apt -y install wine32
┃
┗━
Application could not be started, or no application associated with the specified file.
ShellExecuteEx failed:
Learn more with
OffSec
Want to learn more about shellter? get access to in-depth training and hands-on labs:
PEN-200: 15.3.3. Antivirus Evasion: Automating the Process
PEN-200 course
Updated on: 2026-Mar-13
 Edit this page
rev-proxy-grapher
sipvicious
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install shellter`，再执行 `shellter --version` 2>/dev/null || `shellter -V`
- [ ] **2.** **读官方帮助** —— `shellter -h`，需要细节时 `man shellter`
- [ ] **3.** **在自有靶场跑最小用例** —— 用 `shellter -h` 里最简单的那个子命令试一次
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/shellter/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/defense-evasion.md`](../../tools/by-attack/defense-evasion.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/shellter/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/shellter/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
