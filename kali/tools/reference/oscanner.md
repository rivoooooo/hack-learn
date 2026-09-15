# oscanner

> Oracle assessment framework Oscanner is an Oracle assessment framework developed in Java. It has a plugin-based architecture and comes with a couple of plugins that currently do: Sid Enumeration Passwords tests (common & dictionary)

> **功能分类**：Web 应用 ｜ **Kali 包**：`oscanner` ｜ **官方文档**：<https://www.kali.org/tools/oscanner/>

## 1. 安装

```bash
sudo apt update
sudo apt install oscanner
```

| 项目 | 内容 |
|------|------|
| 版本 | 1.0.6 |
| 架构 | all |
| 可执行命令 | `oscanner` |
| 依赖 | `default-jre` |
| 安装体积 | 1.46 MB |
| 官网 | <http://www.cqure.net/wp/tools/database/oscanner/> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/oscanner> |
| 包追踪 | <https://pkg.kali.org/pkg/oscanner> |

## 2. 官方用法示例

> 以下为 Kali 官方工具页给出的示例与输出原文。

```text
Usage Example
Scan the target server (-s 192.168.1.15) on port 1040 (-P 1040):
root@kali:~# oscanner -s 192.168.1.15 -P 1040
Oracle Scanner 1.0.6 by patrik@cqure.net
--------------------------------------------------
[-] Checking host 192.168.1.15
[x] Failed to enumerate sids from host
[-] Loading services/sids from service file
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `oscanner`

> 官方示例调用：`oscanner -s 192.168.1.15 -P 1040`

```text
root@kali:~# oscanner -s 192.168.1.15 -P 1040
Oracle Scanner 1.0.6 by
[email protected]
--------------------------------------------------
[-] Checking host 192.168.1.15
[x] Failed to enumerate sids from host
[-] Loading services/sids from service file
```

### `oscanner -h`

> 官方示例调用：`oscanner -h`

```text
root@kali:~# oscanner -h
	Oracle Scanner 1.0.6 by
[email protected]
	--------------------------------------
	OracleScanner -s <ip> -r <repfile> [options]
		-s	<servername>
		-f	<serverlist>
		-P	<portnr>
		-v	be verbose
Updated on: 2026-Mar-02
 Edit this page
openssh-ssh1
osrframework
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install oscanner`，再执行 `oscanner --version` 2>/dev/null || `oscanner -V`
- [ ] **2.** **读官方帮助** —— `oscanner -h`，需要细节时 `man oscanner`
- [ ] **3.** **在自有靶场跑最小用例** —— 用 `oscanner -h` 里最简单的那个子命令试一次
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/oscanner/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/discovery.md`](../../tools/by-attack/discovery.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/oscanner/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/oscanner/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
