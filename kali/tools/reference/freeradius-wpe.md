# freeradius-wpe

> FreeRadius Wireless Pawn Edition This package is FreeRadius Wireless Pawn Edition. There are supported and tested EAP Types/Inner Authentication Methods (others may also work): PEAP/PAP (OTP) PEAP/MSCHAPv2

> **功能分类**：无线攻击 ｜ **Kali 包**：`freeradius-wpe` ｜ **官方文档**：<https://www.kali.org/tools/freeradius-wpe/>

## 1. 安装

```bash
sudo apt update
sudo apt install freeradius-wpe
```

| 项目 | 内容 |
|------|------|
| 版本 | 3.2.5 |
| 架构 | any |
| 可执行命令 | `freeradius-wpe` |
| 依赖 | `libc6`、`libcrypt1`、`libct4`、`libgdbm6t64`、`libjson-c5`、`libpam0g`、`libpcap0.8t64`、`libperl5.42`、`libpython3.14`、`libsqlite3-0`、`libssl3t64`、`libsystemd0` 等 |
| 安装体积 | 4.69 MB |
| 官网 | <https://www.freeradius.org/> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/freeradius-wpe> |
| 包追踪 | <https://pkg.kali.org/pkg/freeradius-wpe> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
freeradius-wpe -h          # 查看用法
man freeradius-wpe         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `freeradius-wpe`

官方给出的调用示例：`freeradius-wpe -h`

```text
root@kali:~# freeradius-wpe -h
Usage: freeradius [options]
Options:
  -C            Check configuration and exit.
  -f            Run as a foreground process, not a daemon.
  -h            Print this help message.
  -i <ipaddr>   Listen on ipaddr ONLY.
  -l <log_file> Logging output will be written to this file.
  -m            On SIGINT or SIGQUIT clean up all used memory instead of just exiting.
  -n <name>     Read raddb/name.conf instead of raddb/radiusd.conf.
  -p <port>     Listen on port ONLY.
  -P            Always write out PID, even with -f.
  -s            Do not spawn child processes to handle requests (same as -ft).
  -t            Disable threads.
  -v            Print server version information.
  -X            Turn on full debugging (similar to -tfxxl stdout).
  -x            Turn on additional debugging (-xx gives more debugging).
Updated on: 2026-Aug-25
 Edit this page
freeradius
freerdp3
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install freeradius-wpe`，再执行 `freeradius-wpe --version` 2>/dev/null || `freeradius-wpe -V`
- [ ] **2.** **读官方帮助** —— `freeradius-wpe -h`，需要细节时 `man freeradius-wpe`
- [ ] **3.** **在自有靶场跑最小用例** —— 官方给出的调用形式是：`Usage: freeradius [options]`
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/freeradius-wpe/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/freeradius-wpe/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/freeradius-wpe/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
