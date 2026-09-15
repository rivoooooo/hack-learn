# burpsuite

> Platform for security testing of web applications Burp Suite is an integrated platform for performing security testing of web applications. Its various tools work seamlessly together to support the entire testing process, from initial mapp…

> **功能分类**：Web 应用 ｜ **Kali 包**：`burpsuite` ｜ **官方文档**：<https://www.kali.org/tools/burpsuite/>

## 1. 安装

```bash
sudo apt update
sudo apt install burpsuite
```

| 项目 | 内容 |
|------|------|
| 版本 | 2026.8 |
| 架构 | amd64 |
| 可执行命令 | `burpsuite` |
| 依赖 | `default-jre`、`java-wrappers` |
| 安装体积 | 344.68 MB |
| 官网 | <https://portswigger.net> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/burpsuite> |
| 包追踪 | <https://pkg.kali.org/pkg/burpsuite> |

## 2. 官方用法示例

> 以下为 Kali 官方工具页给出的示例与输出原文。

```text
Screenshots
burpsuite
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `burpsuite`

官方给出的调用示例：`burpsuite --help`

```text
root@kali:~# burpsuite --help
Usage:
--help                            Print this message
--version                         Print version details
--disable-extensions              Prevent loading of extensions on startup
--diagnostics                     Print diagnostic information
--use-defaults                    Start with default settings
--collaborator-server             Run in Collaborator server mode
--collaborator-config             Specify Collaborator server configuration file; defaults to collaborator.config
--data-dir                        Specify data directory
--project-file                    Open the specified project file; this will be created as a new project if the file does not exist
--developer-extension-class-name  Fully qualified name of locally-developed extension class; extension will be loaded from the classpath
--config-file                     Load the specified project configuration file(s); this option may be repeated to load multiple files
--user-config-file                Load the specified user configuration file(s); this option may be repeated to load multiple files
--auto-repair                     Automatically repair a corrupted project file specified by the --project-file option
--unpause-spider-and-scanner      Do not pause the Spider and Scanner when opening an existing project
--disable-auto-update             Suppress auto update behavior
Learn more with
OffSec
Want to learn more about burpsuite? get access to in-depth training and hands-on labs:
PEN-200: 8.2.4. Introduction to Web Application Attacks
WEB-200: 3. Introduction to Burp Suite
WEB-200 course
PEN-200 course
Updated on: 2026-Aug-25
 Edit this page
bulk-extractor
caido
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install burpsuite`，再执行 `burpsuite --version` 2>/dev/null || `burpsuite -V`
- [ ] **2.** **读官方帮助** —— `burpsuite -h`，需要细节时 `man burpsuite`
- [ ] **3.** **在自有靶场跑最小用例** —— 官方给出的调用形式是：`Usage:`
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/burpsuite/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/reconnaissance.md`](../../tools/by-attack/reconnaissance.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/burpsuite/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/burpsuite/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
