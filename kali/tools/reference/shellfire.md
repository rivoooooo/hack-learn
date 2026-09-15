# shellfire

> Exploiting LFI, RFI, and command injection vulnerabilities This package contains an exploitation shell which focuses on exploiting LFI, RFI, and command injection vulnerabilities.

> **功能分类**：通用工具 ｜ **Kali 包**：`shellfire` ｜ **官方文档**：<https://www.kali.org/tools/shellfire/>

## 1. 安装

```bash
sudo apt update
sudo apt install shellfire
```

| 项目 | 内容 |
|------|------|
| 版本 | 0.16 |
| 架构 | all |
| 可执行命令 | `shellfire` |
| 依赖 | `python3`、`python3-cryptography`、`python3-pkg-resources`、`python3-requests` |
| 安装体积 | 104 KB |
| 官网 | <https://github.com/unix-ninja/shellfire> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/shellfire> |
| 包追踪 | <https://pkg.kali.org/pkg/shellfire> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
shellfire -h          # 查看用法
man shellfire         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `shellfire`

官方给出的调用示例：`shellfire -h`

```text
root@kali:~# shellfire -h
usage: shellfire [-h] [-c [CONFIG]] [-d] [--generate PAYLOAD] [--version]
An exploitation shell for command injection vulnerabilities.
options:
  -h, --help          show this help message and exit
  -c [CONFIG]         load a named config on startup.
  -d                  enable debugging (show queries during execution)
  --generate PAYLOAD  generate a payload to stdout. PAYLOAD can be "php" or
                      "aspnet".
  --version           display version and exit.
Updated on: 2026-Aug-25
 Edit this page
sharphound
sherlock
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install shellfire`，再执行 `shellfire --version` 2>/dev/null || `shellfire -V`
- [ ] **2.** **读官方帮助** —— `shellfire -h`，需要细节时 `man shellfire`
- [ ] **3.** **在自有靶场跑最小用例** —— 用 `shellfire -h` 里最简单的那个子命令试一次
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/shellfire/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/shellfire/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/shellfire/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
