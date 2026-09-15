# urlcrazy

> Domain typo generator Generate and test domain typos and variations to detect and perform typo squatting, URL hijacking, phishing, and corporate espionage.

> **功能分类**：信息搜集 ｜ **Kali 包**：`urlcrazy` ｜ **官方文档**：<https://www.kali.org/tools/urlcrazy/>

## 1. 安装

```bash
sudo apt update
sudo apt install urlcrazy
```

| 项目 | 内容 |
|------|------|
| 版本 | 0.8.2 |
| 架构 | all |
| 可执行命令 | `urlcrazy` |
| 依赖 | `ruby`、`ruby-async`、`ruby-async-dns`、`ruby-async-http`、`ruby-colorize`、`ruby-httpclient`、`rubygems` |
| 安装体积 | 1.31 MB |
| 官网 | <https://www.morningstarsecurity.com/research/urlcrazy> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/urlcrazy> |
| 包追踪 | <https://pkg.kali.org/pkg/urlcrazy> |

## 2. 官方用法示例

> 以下为 Kali 官方工具页给出的示例与输出原文。

```text
Usage Example
Search for URLs using the dvorak layout (-k dvorak) and do no resolve hostnames (-r) for the given domain (example.com):
root@kali:~# urlcrazy -k dvorak -r example.com
URLCrazy Domain Report
Domain    : example.com
Keyboard  : dvorak
At        : 2014-05-13 17:04:01 -0600

# Please wait. 95 hostnames to process

Typo Type              Typo            CC-A  Extn
---------------------------------------------------
Character Omission     eample.com      ?     com
Character Omission     examle.com      ?     com
Character Omission     exampe.com      ?     com
Character Omission     exampl.com      ?     com
Character Omission     example.cm      ?     cm
Character Omission     exaple.com      ?     com
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `urlcrazy`

官方给出的调用示例：`urlcrazy -k dvorak -r example.com`

```text
root@kali:~# urlcrazy -k dvorak -r example.com
URLCrazy Domain Report
Domain    : example.com
Keyboard  : dvorak
At        : 2014-05-13 17:04:01 -0600
# Please wait. 95 hostnames to process
Typo Type              Typo            CC-A  Extn
---------------------------------------------------
Character Omission     eample.com      ?     com
Character Omission     examle.com      ?     com
Character Omission     exampe.com      ?     com
Character Omission     exampl.com      ?     com
Character Omission     example.cm      ?     cm
Character Omission     exaple.com      ?     com
```

### `urlcrazy（示例）`

官方给出的调用示例：`urlcrazy -h`

```text
root@kali:~# urlcrazy -h
Warning. File descriptor limit may be too low. Check with `ulimit -a` and change with `ulimit -n 10000`
Updated on: 2026-Aug-25
 Edit this page
unrar-nonfree
util-linux
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install urlcrazy`，再执行 `urlcrazy --version` 2>/dev/null || `urlcrazy -V`
- [ ] **2.** **读官方帮助** —— `urlcrazy -h`，需要细节时 `man urlcrazy`
- [ ] **3.** **在自有靶场跑最小用例** —— 用 `urlcrazy -h` 里最简单的那个子命令试一次
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/urlcrazy/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/reconnaissance.md`](../../tools/by-attack/reconnaissance.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/urlcrazy/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/urlcrazy/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
