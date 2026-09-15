# ligolo-mp

> Multiplayer pivoting solution Ligolo-MP is an advanced version of Ligolo-ng, with client-server architecture, enabling pentesters to play with multiple concurrent tunnels collaboratively. It manages all your TUNs automatically, while also …

> **功能分类**：通用工具 ｜ **Kali 包**：`ligolo-mp` ｜ **官方文档**：<https://www.kali.org/tools/ligolo-mp/>

## 1. 安装

```bash
sudo apt update
sudo apt install ligolo-mp
```

| 项目 | 内容 |
|------|------|
| 版本 | 2.2.1 |
| 架构 | amd64 |
| 可执行命令 | `ligolo-mp`、`ligolo-mp-client` |
| 安装体积 | 129.38 MB |
| 官网 | <https://github.com/ttpreport/ligolo-mp> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/ligolo-mp> |
| 包追踪 | <https://pkg.kali.org/pkg/ligolo-mp> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
ligolo-mp -h          # 查看用法
man ligolo-mp         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 2 个可执行命令，下面是官方页面内嵌的帮助原文。

### `ligolo-mp`

> 官方示例调用：`ligolo-mp -h`

```text
root@kali:~# ligolo-mp -h
Usage of ligolo-mp:
  -agent-addr string
    	listening address (default "0.0.0.0:11601")
  -daemon
    	enable daemon mode
  -insecure-agents
    	Disable certificate verification for agents (insecure!)
  -max-connection int
    	per tunnel connection pool size (default 1024)
  -max-inflight int
    	max inflight TCP connections (default 4096)
  -operator-addr string
    	Address for operators connections (default "0.0.0.0:58008")
  -v	enable verbose mode
```

### `ligolo-mp-client`

> 官方示例调用：`ligolo-mp-client -h`

```text
root@kali:~# ligolo-mp-client -h
Usage of ligolo-mp-client:
  -v	enable verbose mode
Updated on: 2026-May-25
 Edit this page
libimage-exiftool-perl
lsof
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install ligolo-mp`，再执行 `ligolo-mp --version` 2>/dev/null || `ligolo-mp -V`
- [ ] **2.** **读官方帮助** —— `ligolo-mp -h`，需要细节时 `man ligolo-mp`
- [ ] **3.** **在自有靶场跑最小用例** —— 官方给出的调用形式是：`Usage of ligolo-mp:`
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/ligolo-mp/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/command-and-control.md`](../../tools/by-attack/command-and-control.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/ligolo-mp/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/ligolo-mp/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
