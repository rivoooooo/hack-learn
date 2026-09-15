# finalrecon

> Fast and simple Python script for web reconnaissance A fast and simple Python script for web reconnaissance that follows a modular structure and provides detailed information on various areas.

> **功能分类**：通用工具 ｜ **Kali 包**：`finalrecon` ｜ **官方文档**：<https://www.kali.org/tools/finalrecon/>

## 1. 安装

```bash
sudo apt update
sudo apt install finalrecon
```

| 项目 | 内容 |
|------|------|
| 版本 | 1.1.8 |
| 架构 | all |
| 可执行命令 | `finalrecon` |
| 依赖 | `python3`、`python3-aiodns`、`python3-aiohttp`、`python3-bs4`、`python3-cryptography`、`python3-dnspython`、`python3-lxml`、`python3-requests`、`python3-tldextract` |
| 安装体积 | 420 KB |
| 官网 | <https://github.com/thewhiteh4t/FinalRecon> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/finalrecon> |
| 包追踪 | <https://pkg.kali.org/pkg/finalrecon> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
finalrecon -h          # 查看用法
man finalrecon         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `finalrecon`

官方给出的调用示例：`finalrecon -h`

```text
root@kali:~# finalrecon -h
usage: finalrecon [-h] [--url URL] [--headers] [--sslinfo] [--whois] [--crawl]
                  [--dns] [--sub] [--dir] [--wayback] [--ps] [--full] [-nb]
                  [-dt DT] [-pt PT] [-T T] [-w W] [-r] [-s] [-sp SP] [-d D]
                  [-e E] [-o O] [-cd CD] [-of OF] [-k K]
FinalRecon - All in One Web Recon | v1.1.8
options:
  -h, --help  show this help message and exit
  --url URL   Target URL
  --headers   Header Information
  --sslinfo   SSL Certificate Information
  --whois     Whois Lookup
  --crawl     Crawl Target
  --dns       DNS Enumeration
  --sub       Sub-Domain Enumeration
  --dir       Directory Search
  --wayback   Wayback URLs
  --ps        Fast Port Scan
  --full      Full Recon
Extra Options:
  -nb         Hide Banner
  -dt DT      Number of threads for directory enum [ Default : 30 ]
  -pt PT      Number of threads for port scan [ Default : 50 ]
  -T T        Request Timeout [ Default : 30.0 ]
  -w W        Path to Wordlist [ Default : wordlists/dirb_common.txt ]
  -r          Allow Redirect [ Default : False ]
  -s          Toggle SSL Verification [ Default : True ]
  -sp SP      Specify SSL Port [ Default : 443 ]
  -d D        Custom DNS Servers [ Default : 1.1.1.1 ]
  -e E        File Extensions [ Example : txt, xml, php ]
  -o O        Export Format [ Default : txt ]
  -cd CD      Change export directory [ Default : ~/.local/share/finalrecon ]
  -of OF      Change export folder name [ Default :<path>fr_<hostname>_<date>
              ]
  -k K        Add API key [ Example : shodan@key ]
Updated on: 2026-Jun-17
 Edit this page
ferret-sidejack
hydra
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install finalrecon`，再执行 `finalrecon --version` 2>/dev/null || `finalrecon -V`
- [ ] **2.** **读官方帮助** —— `finalrecon -h`，需要细节时 `man finalrecon`
- [ ] **3.** **在自有靶场跑最小用例** —— 用 `finalrecon -h` 里最简单的那个子命令试一次
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/finalrecon/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/reconnaissance.md`](../../tools/by-attack/reconnaissance.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/finalrecon/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/finalrecon/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
