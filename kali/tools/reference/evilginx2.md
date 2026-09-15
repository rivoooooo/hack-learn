# evilginx2

> Man-in-the-middle attack framework This package contains a man-in-the-middle attack framework used for phishing login credentials along with session cookies, which in turn allows to bypass 2-factor authentication protection. This tool is a…

> **功能分类**：通用工具 ｜ **Kali 包**：`evilginx2` ｜ **官方文档**：<https://www.kali.org/tools/evilginx2/>

## 1. 安装

```bash
sudo apt update
sudo apt install evilginx2
```

| 项目 | 内容 |
|------|------|
| 版本 | 3.3.0 |
| 架构 | any |
| 可执行命令 | `evilginx2` |
| 依赖 | `libc6` |
| 安装体积 | 10.13 MB |
| 官网 | <https://github.com/kgretzky/evilginx2> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/evilginx2> |
| 包追踪 | <https://pkg.kali.org/pkg/evilginx2> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
evilginx2 -h          # 查看用法
man evilginx2         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `evilginx2`

> 官方示例调用：`evilginx2 -h`

```text
root@kali:~# evilginx2 -h
Usage of evilginx2:
  -c string
    	Configuration directory path
  -debug
    	Enable debug output
  -developer
    	Enable developer mode (generates self-signed certificates for all hostnames)
  -p string
    	Phishlets directory path
  -t string
    	HTML redirector pages directory path
  -v	Show version
Updated on: 2025-Dec-09
 Edit this page
evil-ssdp
exe2hexbat
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install evilginx2`，再执行 `evilginx2 --version` 2>/dev/null || `evilginx2 -V`
- [ ] **2.** **读官方帮助** —— `evilginx2 -h`，需要细节时 `man evilginx2`
- [ ] **3.** **在自有靶场跑最小用例** —— 官方给出的调用形式是：`Usage of evilginx2:`
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/evilginx2/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/collection.md`](../../tools/by-attack/collection.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/evilginx2/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/evilginx2/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
