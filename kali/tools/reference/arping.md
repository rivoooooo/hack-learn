# arping

> Sends IP and/or ARP pings (to the MAC address) The arping utility sends ARP and/or ICMP requests to the specified host and displays the replies. The host may be specified by its hostname, its IP address, or its MAC address.

> **功能分类**：信息搜集 ｜ **Kali 包**：`arping` ｜ **官方文档**：<https://www.kali.org/tools/arping/>

## 1. 安装

```bash
sudo apt update
sudo apt install arping
```

| 项目 | 内容 |
|------|------|
| 版本 | 2.29 |
| 架构 | any |
| 可执行命令 | `arping` |
| 依赖 | `libc6`、`libnet9`、`libpcap0.8t64`、`libseccomp2` |
| 安装体积 | 97 KB |
| 官网 | <https://www.habets.pp.se/synscan/programs.php?prog=arping> |
| 源码仓库 | <https://salsa.debian.org/debian/arping> |
| 包追踪 | <https://pkg.kali.org/pkg/arping> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
arping -h          # 查看用法
man arping         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `arping`

官方给出的调用示例：`arping --help`

```text
root@kali:~# arping --help
ARPing 2.29, by Thomas Habets <
[email protected]
>
usage: arping [ -0aAbdDeFpPqrRuUvzZ ] [ -w <sec> ] [ -W <sec> ] [ -S <host/ip> ]
              [ -T <host/ip ] [ -s <MAC> ] [ -t <MAC> ] [ -c <count> ]
              [ -C <count> ] [ -i <interface> ] [ -m <type> ] [ -g <group> ]
              [ -V <vlan> ] [ -Q <priority> ] <host/ip/MAC | -B>
Options:
    -0     Use this option to ping with source IP address 0.0.0.0. Use this
           when you haven't configured your interface yet.  Note that  this
           may  get  the  MAC-ping  unanswered.   This  is  an alias for -S
           0.0.0.0.
    -a     Audiable ping.
    -A     Only count addresses matching  requested  address  (This  *WILL*
           break  most things you do. Only useful if you are arpinging many
           hosts at once. See arping-scan-net.sh for an example).
    -b     Like -0 but source broadcast source  address  (255.255.255.255).
           Note that this may get the arping unanswered since it's not nor-
           mal behavior for a host.
    -B     Use instead of host if you want to address 255.255.255.255.
    -c count
           Only send count requests.
    -C count
           Only wait for this many replies, regardless of -c and -w.
    -d     Find duplicate replies. Exit with 1 if there are answers from
           two different MAC addresses.
    -D     Display answers as exclamation points and missing packets as dots.
    -e     Like -a but beep when there is no reply.
    -F     Don't try to be smart about the interface name.  (even  if  this
           switch is not given, -i overrides smartness)
    -g group
           setgid() to this group instead of the nobody group.
    -h     Displays a help message and exits.
    -i interface
           Use the specified interface.
    -m type
           Type of timestamp to use for incoming packets. Use -vv when
           pinging to list available ones.
    -q     Does not display messages, except error messages.
    -Q pri 802.1p priority to set. Should be used with 802.1Q (-V).
           Defaults to 0.
    -r     Raw output: only the MAC/IP address is displayed for each reply.
    -R     Raw output: Like -r but shows "the other one", can  be  combined
           with -r.
    -s MAC Set source MAC address. You may need to use -p with this.
    -S IP  Like  -b and -0 but with set source address.  Note that this may
           get the arping unanswered if the target does not have routing to
           the  IP.  If you don't own the IP you are using, you may need to
           turn on promiscious mode on the interface (with -p).  With  this
           switch  you can find out what IP-address a host has without tak-
           ing an IP-address yourself.
    -t MAC Set target MAC address to use when pinging IP address.
    -T IP  Use -T as target address when pinging MACs that won't respond to
           a broadcast ping but perhaps to a directed broadcast.
           Example:
           To check the address of MAC-A, use knowledge of MAC-B and  IP-B.
           $ arping -S <IP-B> -s <MAC-B> -p <MAC-A>
    -p     Turn  on  promiscious  mode  on interface, use this if you don't
           "own" the MAC address you are using.
    -P     Send ARP replies instead of requests. Useful with -U.
    -u     Show index=received/sent instead  of  just  index=received  when
           pinging MACs.
    -U     Send unsolicited ARP.
    -v     Verbose output. Use twice for more messages.
    -V num 802.1Q tag to add. Defaults to no VLAN tag.
    -w sec Specify a timeout before ping exits regardless of how many
           packets have been sent or received.
    -W sec Time to wait between pings.
    -z     Enable seccomp
    -Z     Disable seccomp (default)
Report bugs to:
[email protected]
Arping home page: <http://www.habets.pp.se/synscan/>
Development repo: http://github.com/ThomasHabets/arping
Updated on: 2026-Aug-25
 Edit this page
arp-scan
arpwatch
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install arping`，再执行 `arping --version` 2>/dev/null || `arping -V`
- [ ] **2.** **读官方帮助** —— `arping -h`，需要细节时 `man arping`
- [ ] **3.** **在自有靶场跑最小用例** —— 用 `arping -h` 里最简单的那个子命令试一次
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/arping/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/discovery.md`](../../tools/by-attack/discovery.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/arping/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/arping/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
