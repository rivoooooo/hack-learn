# watobo

> Semi-automated web application scanner WATOBO is intended to enable security professionals to perform highly efficient (semi-automated) web application security audits. It works like a local web proxy.

> **功能分类**：Web 应用 ｜ **Kali 包**：`watobo` ｜ **官方文档**：<https://www.kali.org/tools/watobo/>

## 1. 安装

```bash
sudo apt update
sudo apt install watobo
```

| 项目 | 内容 |
|------|------|
| 版本 | 1.0.1 |
| 架构 | any |
| 可执行命令 | `watobo` |
| 依赖 | `bundler`、`pry`、`ruby`、`ruby-fxruby`、`ruby-jwt`、`ruby-mechanize`、`ruby-net-http-pipeline`、`ruby-selenium-webdriver` |
| 安装体积 | 3.28 MB |
| 官网 | <https://sourceforge.net/projects/watobo/> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/watobo> |
| 包追踪 | <https://pkg.kali.org/pkg/watobo> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
watobo -h          # 查看用法
man watobo         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `watobo`

> 官方示例调用：`watobo -h`

```text
root@kali:~# watobo -h
#############################################################
     W A T O B O - THE Web Application Toolbox
     brought to you by siberas http://www.siberas.de
#############################################################
+ looking for DEV_ENV environment variable ...[N/A]
/usr/share/watobo/config/datastore.yml
/usr/share/watobo/config/forwarding_proxy.yml
/usr/share/watobo/config/general.yml
/usr/share/watobo/config/gui.yml
/usr/share/watobo/config/interceptor.yml
/usr/share/watobo/config/ott_cache.yml
/usr/share/watobo/config/scan_policy.yml
/usr/share/watobo/config/scanner.yml
/usr/share/watobo/config/scope.yml
/usr/share/watobo/config/sid_cache.yml
---
uninitialized constant Watobo::Modules::Active::Ror
when loading module file /usr/share/watobo/modules/active/RoR/cve_2013_015x.rb
---
---
uninitialized constant Watobo::Modules::Active::Sap
when loading module file /usr/share/watobo/modules/active/sap/business_objects.rb
---
Loading FXRuby ... this may take some time ... [OK]
Updated on: 2025-Dec-09
 Edit this page
voiphopper
wce
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install watobo`，再执行 `watobo --version` 2>/dev/null || `watobo -V`
- [ ] **2.** **读官方帮助** —— `watobo -h`，需要细节时 `man watobo`
- [ ] **3.** **在自有靶场跑最小用例** —— 用 `watobo -h` 里最简单的那个子命令试一次
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/watobo/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/reconnaissance.md`](../../tools/by-attack/reconnaissance.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/watobo/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/watobo/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
