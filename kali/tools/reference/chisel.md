# chisel

> Fast TCP/UDP tunnel over HTTP (program) This package contains a fast TCP/UDP tunnel, transported over HTTP, secured via SSH. Single executable including both client and server. Chisel is mainly useful for passing through firewalls, though …

> **功能分类**：通用工具 ｜ **Kali 包**：`chisel` ｜ **官方文档**：<https://www.kali.org/tools/chisel/>

## 1. 安装

```bash
sudo apt update
sudo apt install chisel
```

| 项目 | 内容 |
|------|------|
| 版本 | 1.12.0~rc2 |
| 架构 | any |
| 可执行命令 | `chisel` |
| 依赖 | `libc6` |
| 安装体积 | 10.17 MB |
| 官网 | <https://github.com/jpillora/chisel> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/chisel> |
| 包追踪 | <https://pkg.kali.org/pkg/chisel> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
chisel -h          # 查看用法
man chisel         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `chisel`

> 官方示例调用：`chisel -h`

```text
root@kali:~# chisel -h
  Usage: chisel [command] [--help]
  Version: 1.12.0~rc2-0kali1 (go1.26.5)
  Commands:
    server - runs chisel in server mode
    client - runs chisel in client mode
  Read more:
    https://github.com/jpillora/chisel
Learn more with
OffSec
Want to learn more about chisel? get access to in-depth training and hands-on labs:
PEN-200: 20.1. Tunneling Through Deep Packet Inspection: HTTP Tunneling Theory and Practice
PEN-300: 17.1.3. Windows Lateral Movement: Reverse RDP Proxying with Chisel
PEN-200 course
PEN-300 course
Updated on: 2026-Aug-25
 Edit this page
chainsaw
chisel-common-binaries
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install chisel`，再执行 `chisel --version` 2>/dev/null || `chisel -V`
- [ ] **2.** **读官方帮助** —— `chisel -h`，需要细节时 `man chisel`
- [ ] **3.** **在自有靶场跑最小用例** —— 官方给出的调用形式是：`Usage: chisel [command] [--help]`
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/chisel/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- **精讲教程**（含原理、参数详解、靶场实操与输出解读）：[chisel](../../tools/tutorials/08-后渗透/chisel.md)
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/command-and-control.md`](../../tools/by-attack/command-and-control.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/chisel/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/chisel/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
