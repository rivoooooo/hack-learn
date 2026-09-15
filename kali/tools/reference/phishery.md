# phishery

> Basic Auth Credential Harvester with Word Doc Template Injector This package contains a Simple SSL Enabled HTTP server with the primary purpose of phishing credentials via Basic Authentication. The power of phishery is best demonstrated by…

> **功能分类**：通用工具 ｜ **Kali 包**：`phishery` ｜ **官方文档**：<https://www.kali.org/tools/phishery/>

## 1. 安装

```bash
sudo apt update
sudo apt install phishery
```

| 项目 | 内容 |
|------|------|
| 版本 | 1.0.2 |
| 架构 | any |
| 可执行命令 | `phishery` |
| 依赖 | `libc6` |
| 安装体积 | 5.05 MB |
| 官网 | <https://github.com/ryhanson/phishery> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/phishery> |
| 包追踪 | <https://pkg.kali.org/pkg/phishery> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
phishery -h          # 查看用法
man phishery         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `phishery`

官方给出的调用示例：`phishery -h`

```text
root@kali:~# phishery -h
|\   \\\\__   O         __    _      __
| \_/    o \  o  ____  / /_  (_)____/ /_  ___  _______  __
> _   (( <_ oO  / __ \/ __ \/ / ___/ __ \/ _ \/ ___/ / / /
| / \__+___/   / /_/ / / / / (__  ) / / /  __/ /  / /_/ /
|/     |/     / .___/_/ /_/_/____/_/ /_/\___/_/   \__, /
             /_/ Basic Auth Credential Harvester (____/
                 with Word Doc Template Injector
  Start the server  : phishery -s settings.json -c credentials.json
  Inject a template : phishery -u https://secure.site.local/docs -i good.docx -o bad.docx
  Options:
    -h, --help      Show usage and exit.
    -v              Show version and exit.
    -s              The JSON settings file used to setup the server. [default: "/etc/phishery/settings.json"]
    -c              The JSON file to store harvested credentials. [default: "/etc/phishery/credentials.json"]
    -u              The phishery URL to use as the Word document template.
    -i              The Word .docx file to inject with a template URL.
    -o              The new Word .docx file with the injected template URL.
Updated on: 2026-Jun-19
 Edit this page
mitm6
xsstrike
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install phishery`，再执行 `phishery --version` 2>/dev/null || `phishery -V`
- [ ] **2.** **读官方帮助** —— `phishery -h`，需要细节时 `man phishery`
- [ ] **3.** **在自有靶场跑最小用例** —— 用 `phishery -h` 里最简单的那个子命令试一次
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/phishery/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/phishery/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/phishery/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
