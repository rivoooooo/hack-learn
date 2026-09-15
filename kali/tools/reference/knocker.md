# knocker

> Simple and easy to use TCP security port scanner Knocker is a new, simple, and easy to use TCP security port scanner written in C, using threads. It is able to analyze hosts and the network services which are running on them.

> **功能分类**：通用工具 ｜ **Kali 包**：`knocker` ｜ **官方文档**：<https://www.kali.org/tools/knocker/>

## 1. 安装

```bash
sudo apt update
sudo apt install knocker
```

| 项目 | 内容 |
|------|------|
| 版本 | 0.7.1 |
| 架构 | any |
| 可执行命令 | `knocker` |
| 依赖 | `libc6` |
| 安装体积 | 83 KB |
| 官网 | <http://knocker.sourceforge.net/> |
| 源码仓库 | <https://salsa.debian.org/pkg-security-team/knocker> |
| 包追踪 | <https://pkg.kali.org/pkg/knocker> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
knocker -h          # 查看用法
man knocker         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `knocker`

官方给出的调用示例：`knocker -h`

```text
root@kali:~# knocker -h
knocker, the net portscanner. Version 0.7.1 (24 May 2002)
Usage: knocker --host <HOST> [OPTIONS]
Example: knocker -H 192.168.0.1 -SP 1 -EP 1024
Required options:
      -H,  --host              host name or numeric Internet address
        or
      --last-host              get the last scanned host name
Common options (if SP is specified you must also give EP):
      -P,  --port              single port number (for one port scans only)
      -SP, --start-port        port number to begin the scan from
      -EP, --end-port          port number to end the scan at
      --last-scan              performs again the last port scan
Extra options:
      -4,  --ipv4              only IPv4 host addressing
      -6,  --ipv6              only IPv6 host addressing
      -q,  --quiet             quiet mode (no console output, logs to file)
      -lf, --logfile <logfile> log scan results to the specified file
      -nf, --no-fency          disable fancy output
      -nc, --no-colors         disable colored output
      --configure              let you configure knocker
Info options:
      -h,  --help              display this help and exit
      -v,  --version           output version information and exit
SEE THE MAN PAGE FOR MORE DESCRIPTIONS, AND EXAMPLES
Report bugs to <
[email protected]
>.
Updated on: 2025-Dec-09
 Edit this page
kismet
laudanum
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install knocker`，再执行 `knocker --version` 2>/dev/null || `knocker -V`
- [ ] **2.** **读官方帮助** —— `knocker -h`，需要细节时 `man knocker`
- [ ] **3.** **在自有靶场跑最小用例** —— 官方给出的调用形式是：`Usage: knocker --host <HOST> [OPTIONS]`
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/knocker/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/knocker/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/knocker/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
