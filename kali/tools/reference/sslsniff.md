# sslsniff

> SSL/TLS man-in-the-middle attack tool sslsniff is designed to create man-in-the-middle (MITM) attacks for SSL/TLS connections, and dynamically generates certs for the domains that are being accessed on the fly. The new certificates are con…

> **功能分类**：Web 应用 ｜ **Kali 包**：`sslsniff` ｜ **官方文档**：<https://www.kali.org/tools/sslsniff/>

## 1. 安装

```bash
sudo apt update
sudo apt install sslsniff
```

| 项目 | 内容 |
|------|------|
| 版本 | 0.8 |
| 架构 | any |
| 可执行命令 | `sslsniff` |
| 依赖 | `libboost-filesystem1.90.0`、`libboost-thread1.90.0`、`libc6`、`libgcc-s1`、`liblog4cpp5v5`、`libssl3t64`、`libstdc++6` |
| 安装体积 | 452 KB |
| 官网 | <https://github.com/moxie0/sslsniff> |
| 源码仓库 | <https://salsa.debian.org/pkg-security-team/sslsniff> |
| 包追踪 | <https://pkg.kali.org/pkg/sslsniff> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
sslsniff -h          # 查看用法
man sslsniff         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `sslsniff`

> 官方示例调用：`sslsniff -h`

```text
root@kali:~# sslsniff -h
sslsniff: option requires an argument -- 'h'
Usage: sslsniff [options]
Modes:
-a	Authority mode.  Specify a certificate that will act as a CA.
-t	Targeted mode.  Specify a directory full of certificates to target.
Required Options:
-c <file|directory>	File containing CA cert/key (authority mode) or
			directory containing a collection of certs/keys
			(targeted mode)
-s <port>		Port to listen on for SSL interception.
-w <file>		File to log to
Optional Options:
-u <updateLocation>	Loction of any Firefox XML update files.
-m <certificateChain>	Location of any intermediary certificates.
-h <port>		Port to listen on for HTTP interception (required for
			fingerprinting).
-f <ff,ie,safari,opera,ios>	Only intercept requests from the specified browser(s).
-d			Deny OCSP requests for our certificates.
-p			Only log HTTP POSTs
-e <url>		Intercept Mozilla Addon Updates
-j <sha256>		The sha256sum value of the addon to inject
Updated on: 2026-Jun-17
 Edit this page
ssldump
sslsplit
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install sslsniff`，再执行 `sslsniff --version` 2>/dev/null || `sslsniff -V`
- [ ] **2.** **读官方帮助** —— `sslsniff -h`，需要细节时 `man sslsniff`
- [ ] **3.** **在自有靶场跑最小用例** —— 官方给出的调用形式是：`Usage: sslsniff [options]`
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/sslsniff/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/collection.md`](../../tools/by-attack/collection.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/sslsniff/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/sslsniff/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
