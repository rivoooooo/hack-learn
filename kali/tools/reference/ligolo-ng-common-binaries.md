# ligolo-ng-common-binaries

> Prebuilt binaries for Advanced ligolo-ng Ligolo-ng is a simple, lightweight and fast tool that allows pentesters to establish tunnels from a reverse TCP/TLS connection using a tun interface (without the need of SOCKS).

> **功能分类**：通用工具 ｜ **Kali 包**：`ligolo-ng-common-binaries` ｜ **官方文档**：<https://www.kali.org/tools/ligolo-ng-common-binaries/>

## 1. 安装

```bash
sudo apt update
sudo apt install ligolo-ng-common-binaries
```

| 项目 | 内容 |
|------|------|
| 版本 | 0.9.1 |
| 架构 | all |
| 可执行命令 | `ligolo-ng-common-binaries` |
| 安装体积 | 158.37 MB |
| 官网 | <https://github.com/nicocha30/ligolo-ng> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/ligolo-ng> |
| 包追踪 | <https://pkg.kali.org/pkg/ligolo-ng-common-binaries> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
ligolo-ng-common-binaries -h          # 查看用法
man ligolo-ng-common-binaries         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `ligolo-ng-common-binaries`

官方给出的调用示例：`ligolo-ng-common-binaries -h`

```text
root@kali:~# ligolo-ng-common-binaries -h
> ligolo-ng-common-binaries ~ Prebuilt binaries for Advanced ligolo-ng
/usr/share/ligolo-ng-common-binaries
|-- ligolo-ng_agent_0.9.1_darwin_amd64
|-- ligolo-ng_agent_0.9.1_darwin_arm64
|-- ligolo-ng_agent_0.9.1_linux_amd64
|-- ligolo-ng_agent_0.9.1_linux_arm64
|-- ligolo-ng_agent_0.9.1_windows_amd64.exe
|-- ligolo-ng_agent_0.9.1_windows_arm64.exe
|-- ligolo-ng_proxy_0.9.1_darwin_amd64
|-- ligolo-ng_proxy_0.9.1_darwin_arm64
|-- ligolo-ng_proxy_0.9.1_linux_amd64
|-- ligolo-ng_proxy_0.9.1_linux_arm64
|-- ligolo-ng_proxy_0.9.1_windows_amd64.exe
`-- ligolo-ng_proxy_0.9.1_windows_arm64.exe
Learn more with
OffSec
Want to learn more about ligolo-ng-common-binaries? get access to in-depth training and hands-on labs:
SkillForge (Lab)
Hugs (Lab)
Updated on: 2026-Aug-25
 Edit this page
ligolo-ng
llvm-defaults
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install ligolo-ng-common-binaries`，再执行 `ligolo-ng-common-binaries --version` 2>/dev/null || `ligolo-ng-common-binaries -V`
- [ ] **2.** **读官方帮助** —— `ligolo-ng-common-binaries -h`，需要细节时 `man ligolo-ng-common-binaries`
- [ ] **3.** **在自有靶场跑最小用例** —— 用 `ligolo-ng-common-binaries -h` 里最简单的那个子命令试一次
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/ligolo-ng-common-binaries/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- **精讲教程**（含原理、参数详解、靶场实操与输出解读）：[ligolo-ng](../../tools/tutorials/08-后渗透/ligolo-ng.md)
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/command-and-control.md`](../../tools/by-attack/command-and-control.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/ligolo-ng-common-binaries/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/ligolo-ng-common-binaries/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
