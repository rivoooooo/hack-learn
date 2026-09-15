# chisel-common-binaries

> Prebuilt binaries for chisel This package contains a fast TCP/UDP tunnel, transported over HTTP, secured via SSH. Single executable including both client and server. Chisel is mainly useful for passing through firewalls, though it can also…

> **功能分类**：通用工具 ｜ **Kali 包**：`chisel-common-binaries` ｜ **官方文档**：<https://www.kali.org/tools/chisel-common-binaries/>

## 1. 安装

```bash
sudo apt update
sudo apt install chisel-common-binaries
```

| 项目 | 内容 |
|------|------|
| 版本 | 1.12.0~rc3 |
| 架构 | all |
| 可执行命令 | `chisel-common-binaries` |
| 安装体积 | 108.26 MB |
| 官网 | <https://github.com/jpillora/chisel> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/chisel> |
| 包追踪 | <https://pkg.kali.org/pkg/chisel-common-binaries> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
chisel-common-binaries -h          # 查看用法
man chisel-common-binaries         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `chisel-common-binaries`

官方给出的调用示例：`chisel-common-binaries -h`

```text
root@kali:~# chisel-common-binaries -h
> chisel-common-binaries ~ Prebuilt binaries for chisel
/usr/share/chisel-common-binaries
|-- chisel_1.12.0-rc3_darwin_amd64
|-- chisel_1.12.0-rc3_darwin_arm64
|-- chisel_1.12.0-rc3_linux_386
|-- chisel_1.12.0-rc3_linux_amd64
|-- chisel_1.12.0-rc3_linux_arm64
|-- chisel_1.12.0-rc3_openbsd_386
|-- chisel_1.12.0-rc3_openbsd_amd64
|-- chisel_1.12.0-rc3_openbsd_arm64
|-- chisel_1.12.0-rc3_windows_386.exe
|-- chisel_1.12.0-rc3_windows_amd64.exe
`-- chisel_1.12.0-rc3_windows_arm64.exe
Learn more with
OffSec
Want to learn more about chisel-common-binaries? get access to in-depth training and hands-on labs:
PEN-200: 20.1. Tunneling Through Deep Packet Inspection: HTTP Tunneling Theory and Practice
PEN-300: 17.1.3. Windows Lateral Movement: Reverse RDP Proxying with Chisel
PEN-200 course
PEN-300 course
Updated on: 2026-Aug-25
 Edit this page
chisel
chkrootkit
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install chisel-common-binaries`，再执行 `chisel-common-binaries --version` 2>/dev/null || `chisel-common-binaries -V`
- [ ] **2.** **读官方帮助** —— `chisel-common-binaries -h`，需要细节时 `man chisel-common-binaries`
- [ ] **3.** **在自有靶场跑最小用例** —— 用 `chisel-common-binaries -h` 里最简单的那个子命令试一次
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/chisel-common-binaries/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- **精讲教程**（含原理、参数详解、靶场实操与输出解读）：[chisel](../../tools/tutorials/08-后渗透/chisel.md)
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/command-and-control.md`](../../tools/by-attack/command-and-control.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/chisel-common-binaries/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/chisel-common-binaries/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
