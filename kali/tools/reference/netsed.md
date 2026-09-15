# netsed

> Network packet-altering stream editor NetSED is a small and handy utility designed to alter, in real time, the contents of packets forwarded through your network. It is really useful for network packet alteration, forging, or manipulation.…

> **功能分类**：通用工具 ｜ **Kali 包**：`netsed` ｜ **官方文档**：<https://www.kali.org/tools/netsed/>

## 1. 安装

```bash
sudo apt update
sudo apt install netsed
```

| 项目 | 内容 |
|------|------|
| 版本 | 1.4 |
| 架构 | any |
| 可执行命令 | `netsed` |
| 依赖 | `libc6` |
| 安装体积 | 53 KB |
| 官网 | <http://silicone.homelinux.org/projects/netsed/> |
| 源码仓库 | <https://salsa.debian.org/debian/netsed> |
| 包追踪 | <https://pkg.kali.org/pkg/netsed> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
netsed -h          # 查看用法
man netsed         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `netsed`

官方给出的调用示例：`netsed -h`

```text
root@kali:~# netsed -h
Usage: netsed [option] proto lport rhost rport rule1 [ rule2 ... ]
  options - can be --ipv4 or -4 to force address resolution in IPv4,
            --ipv6 or -6 to force address resolution in IPv6,
            --ipany to resolve the address in either IPv4 or IPv6.
          - --help or -h to display this usage information.
  proto   - protocol specification (tcp or udp)
  lport   - local port to listen on (see README for transparent
            traffic intercepting on some systems)
  rhost   - where connection should be forwarded (0 = use destination
            address of incoming connection, see README)
  rport   - destination port (0 = dst port of incoming connection)
  ruleN   - replacement rules (see below)
General syntax of replacement rules: s/pat1/pat2[/expire]
This will replace all occurrences of pat1 with pat2 in any matching packet.
An additional parameter, 'expire' of the form [CHAR][NUM], can be used to
expire a rule after NUM successful substitutions during a given connection.
The character CHAR is one of "iIoO", with the effect of restricting the rule
to apply to incoming ("iI") or to outgoing ("oO") packets only, as seen from
the client's perspective. Both of CHAR and NUM are optional.
Eight-bit characters, including NULL and '/', can be applied using HTTP-like
hex escape sequences (e.g. CRLF as %0a%0d).
A match on '%' can be achieved by specifying '%%'.
Examples:
  's/andrew/mike/1'     - replace 'andrew' with 'mike' (only first time)
  's/andrew/mike'       - replace all occurrences of 'andrew' with 'mike'
  's/andrew/mike%00%00' - replace 'andrew' with 'mike\x00\x00'
                          (manually padding to keep original size)
  's/%%/%2f/20'         - replace the 20 first occurrence of '%' with '/'
  's/andrew/mike/o'     - the server will always see 'mike', never 'andrew'
  's/Rilke/Proust/o s/Proust/Rilke/i'
                        - let Rilke travel incognito as Proust
Rules are not active across packet boundaries, and they are evaluated
from first to last, not yet expired rule, as stated on the command line.
Updated on: 2025-Dec-09
 Edit this page
netmask
nextnet
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install netsed`，再执行 `netsed --version` 2>/dev/null || `netsed -V`
- [ ] **2.** **读官方帮助** —— `netsed -h`，需要细节时 `man netsed`
- [ ] **3.** **在自有靶场跑最小用例** —— 官方给出的调用形式是：`Usage: netsed [option] proto lport rhost rport rule1 [ rule2 ... ]`
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/netsed/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/netsed/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/netsed/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
