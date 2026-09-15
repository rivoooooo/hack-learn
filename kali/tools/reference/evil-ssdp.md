# evil-ssdp

> Spoof SSDP replies to phish for NTLM hashes on a network This tool responds to SSDP multicast discover requests, posing as a generic UPNP device on a local network. Your spoofed device will magically appear in Windows Explorer on machines …

> **功能分类**：通用工具 ｜ **Kali 包**：`evil-ssdp` ｜ **官方文档**：<https://www.kali.org/tools/evil-ssdp/>

## 1. 安装

```bash
sudo apt update
sudo apt install evil-ssdp
```

| 项目 | 内容 |
|------|------|
| 版本 | 0.8~beta |
| 架构 | all |
| 可执行命令 | `evil-ssdp` |
| 依赖 | `python3` |
| 安装体积 | 100 KB |
| 官网 | <https://github.com/initstring/evil-ssdp> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/evil-ssdp> |
| 包追踪 | <https://pkg.kali.org/pkg/evil-ssdp> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
evil-ssdp -h          # 查看用法
man evil-ssdp         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `evil-ssdp`

官方给出的调用示例：`evil-ssdp -h`

```text
root@kali:~# evil-ssdp -h
___________     .__.__    _________ _________________ __________
\_   _____/__  _|__|  |  /   _____//   _____/\______ \\______   \
 |    __)_\  \/ /  |  |  \_____  \ \_____  \  |    |  \|     ___/
 |        \\   /|  |  |__/        \/        \ |    `   \    |
/_______  / \_/ |__|____/_______  /_______  //_______  /____|
        \/                      \/        \/         \/
...by initstring (gitlab.com/initstring)
Additional contributors: Dwight Hohnstein
usage: evil_ssdp.py [-h] [-p PORT] [-t TEMPLATE] [-s SMB] [-b] [-r REALM]
                    [-u URL] [-a]
                    interface
positional arguments:
  interface             Network interface to listen on.
options:
  -h, --help            show this help message and exit
  -p, --port PORT       Port for HTTP server. Defaults to 8888.
  -t, --template TEMPLATE
                        Name of a folder in the templates directory. Defaults
                        to "office365". This will determine xml and phishing
                        pages used.
  -s, --smb SMB         IP address of your SMB server. Defalts to the primary
                        address of the "interface" provided.
  -b, --basic           Enable base64 authentication for templates and write
                        credentials to log file.
  -r, --realm REALM     Realm when prompting target for authentication via
                        Basic Auth.
  -u, --url URL         Redirect to this URL. Works with templates that do a
                        POST for logon forms and with templates that include
                        the custom redirect JavaScript (see README for more
                        info).[example: -r https://google.com]
  -a, --analyze         Run in analyze mode. Will NOT respond to any SSDP
                        queries, but will still enable and run the web server
                        for testing.
Updated on: 2025-Dec-09
 Edit this page
enumiax
evilginx2
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install evil-ssdp`，再执行 `evil-ssdp --version` 2>/dev/null || `evil-ssdp -V`
- [ ] **2.** **读官方帮助** —— `evil-ssdp -h`，需要细节时 `man evil-ssdp`
- [ ] **3.** **在自有靶场跑最小用例** —— 用 `evil-ssdp -h` 里最简单的那个子命令试一次
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/evil-ssdp/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/evil-ssdp/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/evil-ssdp/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
