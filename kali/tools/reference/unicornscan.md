# unicornscan

> Userland distributed TCP/IP stack Unicornscan is a new information gathering and correlation engine built for and by members of the security research and testing communities. It was designed to provide an engine that is Scalable, Accurate,…

> **功能分类**：信息搜集 ｜ **Kali 包**：`unicornscan` ｜ **官方文档**：<https://www.kali.org/tools/unicornscan/>

## 1. 安装

```bash
sudo apt update
sudo apt install unicornscan
```

| 项目 | 内容 |
|------|------|
| 版本 | 0.4.7 |
| 架构 | any |
| 可执行命令 | `unicornscan`、`fantaip`、`unibrow`、`unicfgtst`、`us` |
| 依赖 | `flex`、`libc6`、`libpcap0.8t64`、`fantaip` |
| 安装体积 | 3.61 MB |
| 官网 | <http://www.unicornscan.org/> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/unicornscan> |
| 包追踪 | <https://pkg.kali.org/pkg/unicornscan> |

## 2. 官方用法示例

> 以下为 Kali 官方工具页给出的示例与输出原文。

```text
Usage Example
root@kali:~# unicornscan -mTsf -Iv -r 1000 192.168.0.102:a
adding 192.168.0.102/32 mode `TCPscan' ports `a' pps 1000
using interface(s) eth0
scaning 1.00e+00 total hosts with 6.55e+04 total packets, should take a little longer than 1 Minutes, 12 Seconds
connected 192.168.103.227:23221 -> 192.168.0.102:445
TCP open 192.168.0.102:445  ttl 128
connected 192.168.103.227:50006 -> 192.168.0.102:443
TCP open 192.168.0.102:443  ttl 128
connected 192.168.103.227:54487 -> 192.168.0.102:161
TCP open 192.168.0.102:161  ttl 128
connected 192.168.103.227:47765 -> 192.168.0.102:80
TCP open 192.168.0.102:80  ttl 128
connected 192.168.103.227:4267 -> 192.168.0.102:1884
TCP open 192.168.0.102:139  ttl 128
sender statistics 963.9 pps with 65536 packets sent total
listener statistics 131180 packets recieved 0 packets droped and 0 interface drops
TCP open                http[   80]     from 192.168.0.102  ttl 128
TCP open         netbios-ssn[  139]     from 192.168.0.102  ttl 128
TCP open                snmp[  161]     from 192.168.0.102  ttl 128
TCP open               https[  443]     from 192.168.0.102  ttl 128
TCP open        microsoft-ds[  445]     from 192.168.0.102  ttl 128
root@kali:~#
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 5 个可执行命令，下面是官方页面内嵌的帮助原文。

### ``

```text
root@kali:~#
">
 192.168.0.102:445
TCP open 192.168.0.102:445  ttl 128
connected 192.168.103.227:50006 -> 192.168.0.102:443
TCP open 192.168.0.102:443  ttl 128
connected 192.168.103.227:54487 -> 192.168.0.102:161
TCP open 192.168.0.102:161  ttl 128
connected 192.168.103.227:47765 -> 192.168.0.102:80
TCP open 192.168.0.102:80  ttl 128
connected 192.168.103.227:4267 -> 192.168.0.102:1884
TCP open 192.168.0.102:139  ttl 128
sender statistics 963.9 pps with 65536 packets sent total
listener statistics 131180 packets recieved 0 packets droped and 0 interface drops
TCP open                http[   80]     from 192.168.0.102  ttl 128
TCP open         netbios-ssn[  139]     from 192.168.0.102  ttl 128
TCP open                snmp[  161]     from 192.168.0.102  ttl 128
TCP open               https[  443]     from 192.168.0.102  ttl 128
TCP open        microsoft-ds[  445]     from 192.168.0.102  ttl 128
```

### `（示例）`

```text
root@kali:~#
">
 192.168.0.102:445
TCP open 192.168.0.102:445  ttl 128
connected 192.168.103.227:50006 -> 192.168.0.102:443
TCP open 192.168.0.102:443  ttl 128
connected 192.168.103.227:54487 -> 192.168.0.102:161
TCP open 192.168.0.102:161  ttl 128
connected 192.168.103.227:47765 -> 192.168.0.102:80
TCP open 192.168.0.102:80  ttl 128
connected 192.168.103.227:4267 -> 192.168.0.102:1884
TCP open 192.168.0.102:139  ttl 128
sender statistics 963.9 pps with 65536 packets sent total
listener statistics 131180 packets recieved 0 packets droped and 0 interface drops
TCP open                http[   80]     from 192.168.0.102  ttl 128
TCP open         netbios-ssn[  139]     from 192.168.0.102  ttl 128
TCP open                snmp[  161]     from 192.168.0.102  ttl 128
TCP open               https[  443]     from 192.168.0.102  ttl 128
TCP open        microsoft-ds[  445]     from 192.168.0.102  ttl 128
```

### `（示例）`

```text
root@kali:~#
">
 192.168.0.102:445
TCP open 192.168.0.102:445  ttl 128
connected 192.168.103.227:50006 -> 192.168.0.102:443
TCP open 192.168.0.102:443  ttl 128
connected 192.168.103.227:54487 -> 192.168.0.102:161
TCP open 192.168.0.102:161  ttl 128
connected 192.168.103.227:47765 -> 192.168.0.102:80
TCP open 192.168.0.102:80  ttl 128
connected 192.168.103.227:4267 -> 192.168.0.102:1884
TCP open 192.168.0.102:139  ttl 128
sender statistics 963.9 pps with 65536 packets sent total
listener statistics 131180 packets recieved 0 packets droped and 0 interface drops
TCP open                http[   80]     from 192.168.0.102  ttl 128
TCP open         netbios-ssn[  139]     from 192.168.0.102  ttl 128
TCP open                snmp[  161]     from 192.168.0.102  ttl 128
TCP open               https[  443]     from 192.168.0.102  ttl 128
TCP open        microsoft-ds[  445]     from 192.168.0.102  ttl 128
```

### `（示例）`

```text
root@kali:~#
">
Join Free CTF
Get Kali
Blog
Documentation
Documentation Pages
Tools Documentation
Frequently Asked Questions
Known Issues
Community
Community Support
Forums
Discord
Join Newsletter
Mirror Location
Get Involved
Courses
Developers
Git Repositories
Packages
Auto Package Test
Bug Tracker
Kali NetHunter Stats
About
Kali Linux Overview
Press Pack
Wallpapers
Kali Swag Store
Meet The Kali Team
Partnerships
Contact Us
```

### `unicornscan`

官方给出的调用示例：`unicornscan -mTsf -Iv -r 1000 192.168.0.102:a`

```text
root@kali:~# unicornscan -mTsf -Iv -r 1000 192.168.0.102:a
adding 192.168.0.102/32 mode `TCPscan' ports `a' pps 1000
using interface(s) eth0
scaning 1.00e+00 total hosts with 6.55e+04 total packets, should take a little longer than 1 Minutes, 12 Seconds
connected 192.168.103.227:23221 -> 192.168.0.102:445
TCP open 192.168.0.102:445  ttl 128
connected 192.168.103.227:50006 -> 192.168.0.102:443
TCP open 192.168.0.102:443  ttl 128
connected 192.168.103.227:54487 -> 192.168.0.102:161
TCP open 192.168.0.102:161  ttl 128
connected 192.168.103.227:47765 -> 192.168.0.102:80
TCP open 192.168.0.102:80  ttl 128
connected 192.168.103.227:4267 -> 192.168.0.102:1884
TCP open 192.168.0.102:139  ttl 128
sender statistics 963.9 pps with 65536 packets sent total
listener statistics 131180 packets recieved 0 packets droped and 0 interface drops
TCP open                http[   80]     from 192.168.0.102  ttl 128
TCP open         netbios-ssn[  139]     from 192.168.0.102  ttl 128
TCP open                snmp[  161]     from 192.168.0.102  ttl 128
TCP open               https[  443]     from 192.168.0.102  ttl 128
TCP open        microsoft-ds[  445]     from 192.168.0.102  ttl 128
```

### `（示例）`

```text
root@kali:~#
```

### `fantaip`

官方给出的调用示例：`fantaip -h`

```text
root@kali:~# fantaip -h
FantaIP by Kiki
Usage: fantaip (options) IP
	-d		Detach from terminal and daemonize
	-H		Hardware address like XX:XX:XX:XX:XX:XX (otherwise use nics hwaddr)
	-h		help
	-i		*interface
	-v		verbose operation
*: Argument required
Example: fantaip -i eth0 192.168.1.7
```

### `unibrow`

官方给出的调用示例：`unibrow --help`

```text
root@kali:~# unibrow --help
unibrow: invalid option -- '-'
Usage: unibrow:
	-i	*for pcap file to read
	-o	 for output file (append mode)
	-v	 verbose operation
	-h	 display help that you are reading
[*] required argument
pcap filter expression follows options, like unibrow -o new.conf -i file.pcap port 500 and udp
```

### `unicornscan（示例）`

官方给出的调用示例：`unicornscan -h`

```text
root@kali:~# unicornscan -h
unicornscan (version 0.4.7)
usage: unicornscan [options `b:B:cd:De:EFG:hHi:Ij:l:L:m:M:o:p:P:q:Qr:R:s:St:T:u:Uw:W:vVzZ:' ] X.X.X.X/YY:S-E
	-b, --broken-crc     *set broken crc sums on [T]ransport layer, [N]etwork layer, or both[TN]
	-B, --source-port    *set source port? or whatever the scan module expects as a number
	-c, --proc-duplicates process duplicate replies
	-d, --delay-type     *set delay type (numeric value, valid options are `1:tsc 2:gtod 3:sleep')
	-D, --no-defpayload   no default Payload, only probe known protocols
	-e, --enable-module  *enable modules listed as arguments (output and report currently)
	-E, --proc-errors     for processing `non-open' responses (icmp errors, tcp rsts...)
	-F, --try-frags
	-G, --payload-group	*payload group (numeric) for tcp/udp type payload selection (default all)
	-h, --help            help
	-H, --do-dns          resolve hostnames during the reporting phase
	-i, --interface      *interface name, like eth0 or fxp1, not normally required
	-I, --immediate       immediate mode, display things as we find them
	-j, --ignore-seq     *ignore `A'll, 'R'eset sequence numbers for tcp header validation
	-l, --logfile        *write to this file not my terminal
	-L, --packet-timeout *wait this long for packets to come back (default 7 secs)
	-m, --mode           *scan mode, tcp (syn) scan is default, U for udp T for tcp `sf' for tcp connect scan and A for arp
	                       for -mT you can also specify tcp flags following the T like -mTsFpU for example
	                       that would send tcp syn packets with (NO Syn|FIN|NO Push|URG)
	-M, --module-dir     *directory modules are found at (defaults to /usr/lib/unicornscan/modules)
	-o, --format         *format of what to display for replies, see man page for format specification
	-p, --ports           global ports to scan, if not specified in target options
	-P, --pcap-filter    *extra pcap filter string for reciever
	-q, --covertness     *covertness value from 0 to 255
	-Q, --quiet           dont use output to screen, its going somewhere else (a database say...)
	-r, --pps            *packets per second (total, not per host, and as you go higher it gets less accurate)
	-R, --repeats        *repeat packet scan N times
	-s, --source-addr    *source address for packets `r' for random
	-S, --no-shuffle      do not shuffle ports
	-t, --ip-ttl         *set TTL on sent packets as in 62 or 6-16 or r64-128
	-T, --ip-tos         *set TOS on sent packets
	-u, --debug		*debug mask
	-U, --no-openclosed	 dont say open or closed
	-w, --safefile       *write pcap file of recieved packets
	-W, --fingerprint    *OS fingerprint 0=cisco(def) 1=openbsd 2=WindowsXP 3=p0fsendsyn 4=FreeBSD 5=nmap
	                      6=linux 7:strangetcp
	-v, --verbose         verbose (each time more verbose so -vvvvv is really verbose)
	-V, --version         display version
	-z, --sniff           sniff alike
	-Z, --drone-str      *drone String
*:	options with `*' require an argument following them
  address ranges are cidr like 1.2.3.4/8 for all of 1.?.?.?
  if you omit the cidr mask then /32 is implied
  port ranges are like 1-4096 with 53 only scanning one port, a for all 65k and p for 1-1024
example: unicornscan -i eth1 -Ir 160 -E 192.168.1.0/24:1-4000 gateway:a
```

### `us`

官方给出的调用示例：`us -h`

```text
root@kali:~# us -h
unicornscan (version 0.4.7)
usage: unicornscan [options `b:B:cd:De:EFG:hHi:Ij:l:L:m:M:o:p:P:q:Qr:R:s:St:T:u:Uw:W:vVzZ:' ] X.X.X.X/YY:S-E
	-b, --broken-crc     *set broken crc sums on [T]ransport layer, [N]etwork layer, or both[TN]
	-B, --source-port    *set source port? or whatever the scan module expects as a number
	-c, --proc-duplicates process duplicate replies
	-d, --delay-type     *set delay type (numeric value, valid options are `1:tsc 2:gtod 3:sleep')
	-D, --no-defpayload   no default Payload, only probe known protocols
	-e, --enable-module  *enable modules listed as arguments (output and report currently)
	-E, --proc-errors     for processing `non-open' responses (icmp errors, tcp rsts...)
	-F, --try-frags
	-G, --payload-group	*payload group (numeric) for tcp/udp type payload selection (default all)
	-h, --help            help
	-H, --do-dns          resolve hostnames during the reporting phase
	-i, --interface      *interface name, like eth0 or fxp1, not normally required
	-I, --immediate       immediate mode, display things as we find them
	-j, --ignore-seq     *ignore `A'll, 'R'eset sequence numbers for tcp header validation
	-l, --logfile        *write to this file not my terminal
	-L, --packet-timeout *wait this long for packets to come back (default 7 secs)
	-m, --mode           *scan mode, tcp (syn) scan is default, U for udp T for tcp `sf' for tcp connect scan and A for arp
	                       for -mT you can also specify tcp flags following the T like -mTsFpU for example
	                       that would send tcp syn packets with (NO Syn|FIN|NO Push|URG)
	-M, --module-dir     *directory modules are found at (defaults to /usr/lib/unicornscan/modules)
	-o, --format         *format of what to display for replies, see man page for format specification
	-p, --ports           global ports to scan, if not specified in target options
	-P, --pcap-filter    *extra pcap filter string for reciever
	-q, --covertness     *covertness value from 0 to 255
	-Q, --quiet           dont use output to screen, its going somewhere else (a database say...)
	-r, --pps            *packets per second (total, not per host, and as you go higher it gets less accurate)
	-R, --repeats        *repeat packet scan N times
	-s, --source-addr    *source address for packets `r' for random
	-S, --no-shuffle      do not shuffle ports
	-t, --ip-ttl         *set TTL on sent packets as in 62 or 6-16 or r64-128
	-T, --ip-tos         *set TOS on sent packets
	-u, --debug		*debug mask
	-U, --no-openclosed	 dont say open or closed
	-w, --safefile       *write pcap file of recieved packets
	-W, --fingerprint    *OS fingerprint 0=cisco(def) 1=openbsd 2=WindowsXP 3=p0fsendsyn 4=FreeBSD 5=nmap
	                      6=linux 7:strangetcp
	-v, --verbose         verbose (each time more verbose so -vvvvv is really verbose)
	-V, --version         display version
	-z, --sniff           sniff alike
	-Z, --drone-str      *drone String
*:	options with `*' require an argument following them
  address ranges are cidr like 1.2.3.4/8 for all of 1.?.?.?
  if you omit the cidr mask then /32 is implied
  port ranges are like 1-4096 with 53 only scanning one port, a for all 65k and p for 1-1024
example: unicornscan -i eth1 -Ir 160 -E 192.168.1.0/24:1-4000 gateway:a
Updated on: 2025-Dec-09
 Edit this page
unicorn-magic
uniscan
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install unicornscan`，再执行 `unicornscan --version` 2>/dev/null || `unicornscan -V`
- [ ] **2.** **读官方帮助** —— `unicornscan -h`，需要细节时 `man unicornscan`
- [ ] **3.** **在自有靶场跑最小用例** —— 官方给出的调用形式是：`Usage: fantaip (options) IP`
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/unicornscan/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/reconnaissance.md`](../../tools/by-attack/reconnaissance.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/unicornscan/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/unicornscan/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
