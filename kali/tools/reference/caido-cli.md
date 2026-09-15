# caido-cli

> Security auditing toolkit (CLI) This package contains caido CLI, a security auditing toolkit.

> **功能分类**：通用工具 ｜ **Kali 包**：`caido-cli` ｜ **官方文档**：<https://www.kali.org/tools/caido-cli/>

## 1. 安装

```bash
sudo apt update
sudo apt install caido-cli
```

| 项目 | 内容 |
|------|------|
| 版本 | 0.58.3 |
| 架构 | amd64 |
| 可执行命令 | `caido-cli` |
| 依赖 | `libc6`、`libgcc-s1` |
| 安装体积 | 118.41 MB |
| 官网 | <https://github.com/caido/caido> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/caido-cli> |
| 包追踪 | <https://pkg.kali.org/pkg/caido-cli> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
caido-cli -h          # 查看用法
man caido-cli         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `caido-cli`

> 官方示例调用：`caido-cli -h`

```text
root@kali:~# caido-cli -h
A lightweight web security auditing toolkit
Usage: caido-cli [OPTIONS]
Options:
  -l, --listen <ADDR:PORT>                         Listening address
      --invisible                                  Enable invisible mode for all listeners
      --no-sync                                    Disable sync with sync server
      --proxy-listen <ADDR:PORT>                   Proxy listening addresses
      --ui-listen <ADDR:PORT>                      UI listening addresses
      --ui-domain <UI_DOMAIN>                      Allowed domains for UI
      --no-open                                    Do not open the UI a browser tab
      --debug                                      Record and display debug logs
      --reset-cache                                Reset the instance cache of cloud data
      --reset-credentials                          Reset the instance credentials (DANGEROUS)
      --data-path <DATA_PATH>                      Directory to store data
      --no-logging                                 Disable file logging
      --no-renderer-sandbox                        Disable sandboxing for the renderer
      --import-ca-cert <IMPORT_CA_CERT>            Import CA certificate
      --import-ca-cert-pass <IMPORT_CA_CERT_PASS>  Import CA certificate password
      --allow-guests                               Allow login as guest
      --safe                                       Enable safe mode
      --registration-key <ckey_[20 characters]>    Registration key [env: CAIDO_REGISTRATION_KEY=]
      --config <CONFIG>                            Load configuration from file
  -h, --help                                       Print help (see more with '--help')
  -V, --version                                    Print version
Updated on: 2026-Aug-25
 Edit this page
caido
caldera
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install caido-cli`，再执行 `caido-cli --version` 2>/dev/null || `caido-cli -V`
- [ ] **2.** **读官方帮助** —— `caido-cli -h`，需要细节时 `man caido-cli`
- [ ] **3.** **在自有靶场跑最小用例** —— 官方给出的调用形式是：`Usage: caido-cli [OPTIONS]`
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/caido-cli/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/reconnaissance.md`](../../tools/by-attack/reconnaissance.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/caido-cli/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/caido-cli/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
