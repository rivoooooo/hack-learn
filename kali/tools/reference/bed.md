# bed

> A network protocol fuzzer BED is a program which is designed to check daemons for potential buffer overflows, format strings et. al.

> **功能分类**：漏洞分析 ｜ **Kali 包**：`bed` ｜ **官方文档**：<https://www.kali.org/tools/bed/>

## 1. 安装

```bash
sudo apt update
sudo apt install bed
```

| 项目 | 内容 |
|------|------|
| 版本 | 0.5 |
| 架构 | any |
| 可执行命令 | `bed` |
| 依赖 | `perl` |
| 安装体积 | 73 KB |
| 官网 | <http://www.snake-basket.de> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/bed> |
| 包追踪 | <https://pkg.kali.org/pkg/bed> |

## 2. 官方用法示例

> 以下为 Kali 官方工具页给出的示例与输出原文。

```text
Usage Example
Use the HTTP plugin (-s HTTP) to fuzz the target server (-t 192.168.1.15):
root@kali:~# bed -s HTTP -t 192.168.1.15

 BED 0.5 by mjm ( www.codito.de ) & eric ( www.snake-basket.de )

 + Buffer overflow testing:
        testing: 1  HEAD XAXAX HTTP/1.0
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `bed`

官方给出的调用示例：`bed -s HTTP -t 192.168.1.15`

```text
root@kali:~# bed -s HTTP -t 192.168.1.15
 BED 0.5 by mjm ( www.codito.de ) & eric ( www.snake-basket.de )
 + Buffer overflow testing:
        testing: 1  HEAD XAXAX HTTP/1.0
```

### `bed（示例）`

官方给出的调用示例：`bed -h`

```text
root@kali:~# bed -h
 BED 0.5 by mjm ( www.codito.de ) & eric ( www.snake-basket.de )
 Usage:
 bed -s <plugin> -t <target> -p <port> -o <timeout> [ depends on the plugin ]
 <plugin>   = FTP/SMTP/POP/HTTP/IRC/IMAP/PJL/LPD/FINGER/SOCKS4/SOCKS5
 <target>   = Host to check (default: localhost)
 <port>     = Port to connect to (default: standard port)
 <timeout>  = seconds to wait after each test (default: 2 seconds)
 use "bed -s <plugin>" to obtain the parameters you need for the plugin.
 Only -s is a mandatory switch.
Updated on: 2026-Mar-02
 Edit this page
amap
bettercap
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install bed`，再执行 `bed --version` 2>/dev/null || `bed -V`
- [ ] **2.** **读官方帮助** —— `bed -h`，需要细节时 `man bed`
- [ ] **3.** **在自有靶场跑最小用例** —— 官方给出的调用形式是：`Usage:`
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/bed/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/resource-development.md`](../../tools/by-attack/resource-development.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/bed/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/bed/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
