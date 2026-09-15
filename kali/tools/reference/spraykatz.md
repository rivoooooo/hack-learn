# spraykatz

> Tool able to retrieve credentials on Windows machines This package contains a tool without any pretention able to retrieve credentials on Windows machines and large Active Directory environments. It simply tries to procdump machines and pa…

> **功能分类**：通用工具 ｜ **Kali 包**：`spraykatz` ｜ **官方文档**：<https://www.kali.org/tools/spraykatz/>

## 1. 安装

```bash
sudo apt update
sudo apt install spraykatz
```

| 项目 | 内容 |
|------|------|
| 版本 | 0.9.9 |
| 架构 | all |
| 可执行命令 | `spraykatz` |
| 依赖 | `nmap`、`python3`、`python3-impacket`、`python3-lxml`、`python3-openssl`、`python3-pyasn1`、`python3-pycryptodome`、`python3-pypykatz`、`python3-wget` |
| 安装体积 | 780 KB |
| 官网 | <https://github.com/aas-n/spraykatz> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/spraykatz> |
| 包追踪 | <https://pkg.kali.org/pkg/spraykatz> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
spraykatz -h          # 查看用法
man spraykatz         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `spraykatz`

> 官方示例调用：`spraykatz -h`

```text
root@kali:~# spraykatz -h
███████╗██████╗ ██████╗  █████╗ ██╗   ██╗██╗  ██╗ █████╗ ████████╗███████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗╚██╗ ██╔╝██║ ██╔╝██╔══██╗╚══██╔══╝╚══███╔╝
███████╗██████╔╝██████╔╝███████║ ╚████╔╝ █████╔╝ ███████║   ██║     ███╔╝
╚════██║██╔═══╝ ██╔══██╗██╔══██║  ╚██╔╝  ██╔═██╗ ██╔══██║   ██║    ███╔╝
███████║██║     ██║  ██║██║  ██║   ██║   ██║  ██╗██║  ██║   ██║   ███████╗
╚══════╝╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   ╚══════╝v0.9.9
                    Written by @aas_s3curity
usage: spraykatz.py [-h] -u USERNAME -p PASSWORD -t TARGETS [-d DOMAIN] [-r]
                    [-v {warning,info,debug}] [-w WAIT]
A tool to spray love around the world!
options:
  -h, --help            show this help message and exit
Mandatory Arguments:
  -u, --username USERNAME
                        User to spray with. He must have admin rights on
                        targeted systems in order to gain remote code
                        execution.
  -p, --password PASSWORD
                        User's password or NTLM hash in the LM:NT format.
  -t, --targets TARGETS
                        IP addresses and/or IP address ranges. You can submit
                        them via a file of targets (one target per line), or
                        inline (separated by commas).
Optional Arguments:
  -d, --domain DOMAIN   User's domain. If he is not member of a domain, simply
                        use "-d ." instead.
  -r, --remove          Only try to remove ProcDump and dumps left behind on
                        distant machines. Just in case.
  -v, --verbosity {warning,info,debug}
                        Verbosity mode. Default is info.
  -w, --wait WAIT       How many seconds Spraykatz waits before exiting
                        gracefully. Default is 180 seconds.
=> Do not use this on production environments!
Updated on: 2025-Dec-09
 Edit this page
sprayingtoolkit
sqlmc
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install spraykatz`，再执行 `spraykatz --version` 2>/dev/null || `spraykatz -V`
- [ ] **2.** **读官方帮助** —— `spraykatz -h`，需要细节时 `man spraykatz`
- [ ] **3.** **在自有靶场跑最小用例** —— 用 `spraykatz -h` 里最简单的那个子命令试一次
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/spraykatz/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/spraykatz/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/spraykatz/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
