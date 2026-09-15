# nmapsi4

> Graphical interface to nmap, the network scanner NmapSI4 is a complete Qt-based Gui with the design goal to provide a complete nmap interface for users, in order to manage all options of this power security net scanner.

> **功能分类**：通用工具 ｜ **Kali 包**：`nmapsi4` ｜ **官方文档**：<https://www.kali.org/tools/nmapsi4/>

## 1. 安装

```bash
sudo apt update
sudo apt install nmapsi4
```

| 项目 | 内容 |
|------|------|
| 版本 | 0.6~alpha1 |
| 架构 | any |
| 可执行命令 | `nmapsi4` |
| 依赖 | `bind9-dnsutils`、`libc6`、`libgcc-s1`、`libqt6core5compat6`、`libqt6core6t64`、`libqt6dbus6`、`libqt6gui6`、`libqt6network6`、`libqt6qml6`、`libqt6quick6`、`libqt6webenginewidgets6`、`libqt6widgets6` 等 |
| 安装体积 | 1.31 MB |
| 官网 | <https://www.nmapsi4.org> |
| 源码仓库 | <https://salsa.debian.org/pkg-security-team/nmapsi4> |
| 包追踪 | <https://pkg.kali.org/pkg/nmapsi4> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
nmapsi4 -h          # 查看用法
man nmapsi4         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `man`

> 官方示例调用：`man nmapsi4`

```text
root@kali:~# man nmapsi4
nmapsi4(1)                  General Commands Manual                  nmapsi4(1)
NAME
     nmapsi4 - A Qt4 interface for nmap
SYNOPSIS
     nmapsi4 [Qt-options] [KDE-options] [File]
DESCRIPTION
     This  manual page documents briefly the nmapsi4 QT Application.  This man-
     ual page was written for the Debian  GNU/Linux  distribution  because  the
     original program does not have a manual page.
     nmapsi4  is  a  full-featured  interface  for the nmap(1) security network
     scanner.
OPTIONS
   Arguments:
     File(s)
            file(s) to open
   General Options
     --help Show help about options
     --help-qt
            Show Qt specific options
     --help-kde
            Show KDE specific options
     --help-all
            Show all options
     --author
            Show author information
     -v, --version
            Show version information
     --license
            Show license information
     --     End of options
            This manual page was prepared by Francesco Cecconi
            <
[email protected]
> for the Debian GNU/Linux system (but
            may be used by others).
SEE ALSO
     If the khelpcenter program is properly installed at your site, the command
            khelpcenter help:/nmapsi4
     should give you access to the complete manual.
     Alternatively the manual can be browsed in konqueror  giving  it  the  URL
     help:/nmapsi4
QT Application                   April 25, 2007                      nmapsi4(1)
Updated on: 2026-May-25
 Edit this page
nmap
opentaxii
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install nmapsi4`，再执行 `nmapsi4 --version` 2>/dev/null || `nmapsi4 -V`
- [ ] **2.** **读官方帮助** —— `nmapsi4 -h`，需要细节时 `man nmapsi4`
- [ ] **3.** **在自有靶场跑最小用例** —— 用 `nmapsi4 -h` 里最简单的那个子命令试一次
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/nmapsi4/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- **精讲教程**（含原理、参数详解、靶场实操与输出解读）：[nmap](../../tools/tutorials/01-信息搜集/nmap.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/nmapsi4/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/nmapsi4/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
