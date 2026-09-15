# enumiax

> IAX protocol username enumerator enumIAX is an Inter Asterisk Exchange protocol username brute-force enumerator. enumIAX may operate in two distinct modes; Sequential Username Guessing or Dictionary Attack.

> **功能分类**：漏洞分析 ｜ **Kali 包**：`enumiax` ｜ **官方文档**：<https://www.kali.org/tools/enumiax/>

## 1. 安装

```bash
sudo apt update
sudo apt install enumiax
```

| 项目 | 内容 |
|------|------|
| 版本 | 0.4a |
| 架构 | any |
| 可执行命令 | `enumiax` |
| 依赖 | `libc6` |
| 安装体积 | 35 KB |
| 官网 | <https://enumiax.sourceforge.net/> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/enumiax> |
| 包追踪 | <https://pkg.kali.org/pkg/enumiax> |

## 2. 官方用法示例

> 以下为 Kali 官方工具页给出的示例与输出原文。

```text
Usage Example
Run a dictionary attack (-d /usr/share/wordlists/metasploit/unix_users.txt) against the target host (192.168.1.1):
root@kali:~# enumiax -d /usr/share/wordlists/metasploit/unix_users.txt 192.168.1.1
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `enumiax`

> 官方示例调用：`enumiax -d /usr/share/wordlists/metasploit/unix_users.txt 192.168.1.1`

```text
root@kali:~# enumiax -d /usr/share/wordlists/metasploit/unix_users.txt 192.168.1.1
```

### `enumiax --help`

> 官方示例调用：`enumiax --help`

```text
root@kali:~# enumiax --help
enumiax: invalid option -- '-'
enumIAX 0.4a
Dustin D. Trammell <
[email protected]
>
Usage: enumiax [options] target
  options:
    -d <dict>   Dictionary attack using <dict> file
    -i <count>  Interval for auto-save (# of operations, default 1000)
    -m #        Minimum username length (in characters)
    -M #        Maximum username length (in characters)
    -r #        Rate-limit calls (in microseconds)
    -s <file>   Read session state from state file
    -v          Increase verbosity (repeat for additional verbosity)
    -V          Print version information and exit
    -h          Print help/usage information and exit
Updated on: 2025-Dec-09
 Edit this page
enum4linux
evil-ssdp
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install enumiax`，再执行 `enumiax --version` 2>/dev/null || `enumiax -V`
- [ ] **2.** **读官方帮助** —— `enumiax -h`，需要细节时 `man enumiax`
- [ ] **3.** **在自有靶场跑最小用例** —— 官方给出的调用形式是：`Usage: enumiax [options] target`
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/enumiax/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/credential-access.md`](../../tools/by-attack/credential-access.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/enumiax/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/enumiax/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
