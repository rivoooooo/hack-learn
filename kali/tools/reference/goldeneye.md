# goldeneye

> HTTP DoS test tool GoldenEye is a HTTP DoS Test Tool. This tool can be used to test if a site is susceptible to Deny of Service (DoS) attacks. Is possible to open several parallel connections against a URL to check if the web server can be…

> **功能分类**：通用工具 ｜ **Kali 包**：`goldeneye` ｜ **官方文档**：<https://www.kali.org/tools/goldeneye/>

## 1. 安装

```bash
sudo apt update
sudo apt install goldeneye
```

| 项目 | 内容 |
|------|------|
| 版本 | 1.2.0 |
| 架构 | all |
| 可执行命令 | `goldeneye` |
| 依赖 | `python3` |
| 安装体积 | 963 KB |
| 官网 | <https://github.com/jseidl/GoldenEye> |
| 源码仓库 | <https://salsa.debian.org/pkg-security-team/goldeneye> |
| 包追踪 | <https://pkg.kali.org/pkg/goldeneye> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
goldeneye -h          # 查看用法
man goldeneye         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `goldeneye`

> 官方示例调用：`goldeneye -h`

```text
root@kali:~# goldeneye -h
-----------------------------------------------------------------------------------------------------------
GoldenEye v2.1 by Jan Seidl <
[email protected]
>
 USAGE: goldeneye <url> [OPTIONS]
 OPTIONS:
	 Flag			Description						Default
	 -u, --useragents	File with user-agents to use				(default: randomly generated)
	 -w, --workers		Number of concurrent workers				(default: 10)
	 -s, --sockets		Number of concurrent sockets				(default: 500)
	 -m, --method		HTTP Method to use 'get' or 'post'  or 'random'		(default: get)
	 -n, --nosslcheck	Do not verify SSL Certificate				(default: True)
	 -d, --debug		Enable Debug Mode [more verbose output]			(default: False)
	 -h, --help		Shows this help
-----------------------------------------------------------------------------------------------------------
Updated on: 2026-Jun-19
 Edit this page
bluesnarfer
mitm6
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install goldeneye`，再执行 `goldeneye --version` 2>/dev/null || `goldeneye -V`
- [ ] **2.** **读官方帮助** —— `goldeneye -h`，需要细节时 `man goldeneye`
- [ ] **3.** **在自有靶场跑最小用例** —— 用 `goldeneye -h` 里最简单的那个子命令试一次
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/goldeneye/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/impact.md`](../../tools/by-attack/impact.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/goldeneye/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/goldeneye/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
