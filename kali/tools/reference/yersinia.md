# yersinia

> Network vulnerabilities check software Yersinia is a framework for performing layer 2 attacks. It is designed to take advantage of some weakeness in different network protocols. It pretends to be a solid framework for analyzing and testing…

> **功能分类**：漏洞分析 ｜ **Kali 包**：`yersinia` ｜ **官方文档**：<https://www.kali.org/tools/yersinia/>

## 1. 安装

```bash
sudo apt update
sudo apt install yersinia
```

| 项目 | 内容 |
|------|------|
| 版本 | 0.8.2 |
| 架构 | any |
| 可执行命令 | `yersinia` |
| 依赖 | `libc6`、`libncurses6`、`libnet9`、`libpcap0.8t64`、`libtinfo6` |
| 安装体积 | 415 KB |
| 官网 | <https://github.com/tomac/yersinia> |
| 源码仓库 | <https://salsa.debian.org/debian/yersinia> |
| 包追踪 | <https://pkg.kali.org/pkg/yersinia> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
yersinia -h          # 查看用法
man yersinia         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `yersinia`

官方给出的调用示例：`yersinia -h`

```text
root@kali:~# yersinia -h
    Û²ÛÛ²²Û
   ²Û°°°²²Û²²
 Û²²²°ÛÛÛ°²Û²²
²²°²°Û±²±Û²°°²²²Û
°²°°Û±²±²²±Û²²°²²Û
²°²°Û±²±±²²±Û°°²°²²               Yersinia...
²²°°²Û²²±²²±²±Û°²ÛÛ²²²
Û²²²°Û±²²²±±²²±ÛÛ°²°ÛÛ²²²         The Black Death for nowadays networks
 ²²²°²ÛÛ±²²²²²²²²±Û°°²²°²²
 ²ÛÛ°°²°Û±²²±±±²²²²²±Û°²²Û²²             by Slay & tomac
  Û²²Û²°°Û±²²²±±²²²²²²±Û²°°²²Û
     ²²Û²°Û±±²²±±±±±±²²²±Û°²°²Û        http://www.yersinia.net
      Û²°²²ÛÛ±±±²²±±±±²²²ÛÛÛ²Û²
[email protected]
       Û²²°°²ÛÛ±±±²²²±²²²ÛÛ²°ÛÛ
         ²Û²°²²°Û±±±²²²²±Û²°Û²²
         ²Û²²Û°²°ÛÛÛÛÛ±ÛÛ°²²²²     Prune your MSTP, RSTP, STP trees!!!!
             ²²Û°°²²²°°²°°Û²²
Usage: yersinia [-hVGIDd] [-l logfile] [-c conffile] protocol [protocol_options]
       -V   Program version.
       -h   This help screen.
       -G   Graphical mode (GTK).
       -I   Interactive mode (ncurses).
       -D   Daemon mode.
       -d   Debug.
       -l logfile   Select logfile.
       -c conffile  Select config file.
  protocol   One of the following: cdp, dhcp, dot1q, dot1x, dtp, hsrp, isl, mpls, stp, vtp.
Try 'yersinia protocol -h' to see protocol_options help
Please, see the man page for a full list of options and many examples.
Send your bugs & suggestions to the Yersinia developers <
[email protected]
>
MOTD: Daniela blu-eyes... :)
Updated on: 2026-Aug-25
 Edit this page
yara
zaproxy
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install yersinia`，再执行 `yersinia --version` 2>/dev/null || `yersinia -V`
- [ ] **2.** **读官方帮助** —— `yersinia -h`，需要细节时 `man yersinia`
- [ ] **3.** **在自有靶场跑最小用例** —— 官方给出的调用形式是：`Usage: yersinia [-hVGIDd] [-l logfile] [-c conffile] protocol [protocol_options]`
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/yersinia/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/discovery.md`](../../tools/by-attack/discovery.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/yersinia/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/yersinia/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
