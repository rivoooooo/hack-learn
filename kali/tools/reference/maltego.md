# maltego

> Open source intelligence and forensics application Maltego is an open source intelligence and forensics application. It will offer you timous mining and gathering of information as well as the representation of this information in a easy t…

> **功能分类**：信息搜集 ｜ **Kali 包**：`maltego` ｜ **官方文档**：<https://www.kali.org/tools/maltego/>

## 1. 安装

```bash
sudo apt update
sudo apt install maltego
```

| 项目 | 内容 |
|------|------|
| 版本 | 4.12.1 |
| 架构 | all |
| 可执行命令 | `maltego` |
| 依赖 | `openjdk-11-jdk-headless`、`openjdk-11-jre` |
| 安装体积 | 301.19 MB |
| 官网 | <https://www.maltego.com> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/maltego> |
| 包追踪 | <https://pkg.kali.org/pkg/maltego> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
maltego -h          # 查看用法
man maltego         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `maltego`

官方给出的调用示例：`maltego -h`

```text
root@kali:~# maltego -h
amd64
./../platform/lib/nbexec: WARNING: environment variable DISPLAY is not set
Module reload options:
  --reload /path/to/module.jar  install or reinstall a module JAR file
Additional module options:
  -s, --serverHttpAllowed
  -o, --open <arg1>...<argN>
  -h, --hub <arg>
  -z, --cloudDebug <arg>
  -c, --cloud <arg>
  --v3ProtocolDisabled
  -s, --serverHttpAllowed
  -i, --import <arg>
  -u, --updates <arg>
  -p, --automationPort <arg>
  -m, --machine <arg>
Core options:
  --laf <LaF classname> use given LookAndFeel class instead of the default
  --fontsize <size>     set the base font size of the user interface, in points
  --locale <language[:country[:variant]]> use specified locale
  --userdir <path>      use specified directory to store user settings
  --cachedir <path>     use specified directory to store user cache, must be different from userdir
  --nosplash            do not show the splash screen
Learn more with
OffSec
Want to learn more about maltego? get access to in-depth training and hands-on labs:
Incident Responder Foundations: 12.1.4. Post-Mortem Report Template
Updated on: 2026-Aug-25
 Edit this page
llvm-defaults
mcp-kali-server
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install maltego`，再执行 `maltego --version` 2>/dev/null || `maltego -V`
- [ ] **2.** **读官方帮助** —— `maltego -h`，需要细节时 `man maltego`
- [ ] **3.** **在自有靶场跑最小用例** —— 用 `maltego -h` 里最简单的那个子命令试一次
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/maltego/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/reconnaissance.md`](../../tools/by-attack/reconnaissance.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/maltego/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/maltego/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
