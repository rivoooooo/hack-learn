# coercer

> Coerce a Windows server to authenticate on an arbitrary machine A Python script to automatically coerce a Windows server to authenticate on an arbitrary machine through many methods.

> **功能分类**：通用工具 ｜ **Kali 包**：`coercer` ｜ **官方文档**：<https://www.kali.org/tools/coercer/>

## 1. 安装

```bash
sudo apt update
sudo apt install coercer
```

| 项目 | 内容 |
|------|------|
| 版本 | 2.4.3 |
| 架构 | all |
| 可执行命令 | `coercer` |
| 依赖 | `python3`、`python3-impacket`、`python3-jinja2`、`python3-xlsxwriter` |
| 安装体积 | 241 KB |
| 官网 | <https://github.com/p0dalirius/Coercer> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/coercer> |
| 包追踪 | <https://pkg.kali.org/pkg/coercer> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
coercer -h          # 查看用法
man coercer         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `coercer`

> 官方示例调用：`coercer -h`

```text
root@kali:~# coercer -h
       ______
      / ____/___  ___  _____________  _____
     / /   / __ \/ _ \/ ___/ ___/ _ \/ ___/
    / /___/ /_/ /  __/ /  / /__/  __/ /      v2.4.3
    \____/\____/\___/_/   \___/\___/_/       by @podalirius_
usage: coercer [-h] [-v] {scan,coerce,fuzz} ...
Automatic windows authentication coercer using various methods.
positional arguments:
  {scan,coerce,fuzz}  Mode
    scan              Tests known methods with known working paths on all
                      methods, and report when an authentication is received.
    coerce            Trigger authentications through all known methods with
                      known working paths
    fuzz              Tests every method with a list of exploit paths, and
                      report when an authentication is received.
options:
  -h, --help          show this help message and exit
  -v, --verbose       Verbose mode (default: False)
Learn more with
OffSec
Want to learn more about coercer? get access to in-depth training and hands-on labs:
PEN-300: 22.2.2. Attacking Active Directory Certificate Services: NTLM Relay to ADCS HTTP Endpoints
PEN-300 course
Updated on: 2025-Dec-09
 Edit this page
code-oss
colly
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install coercer`，再执行 `coercer --version` 2>/dev/null || `coercer -V`
- [ ] **2.** **读官方帮助** —— `coercer -h`，需要细节时 `man coercer`
- [ ] **3.** **在自有靶场跑最小用例** —— 用 `coercer -h` 里最简单的那个子命令试一次
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/coercer/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/coercer/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/coercer/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
