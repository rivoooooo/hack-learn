# thc-ipv6

> The Hacker Choice’s IPv6 Attack Toolkit Attack toolkit for testing IPv6 and ICMPv6 protocol weaknesses. Some of the tools included: alive6: an effective alive scanning. denial6: try a collection of denial-of-service tests against a target.

> **功能分类**：信息搜集 ｜ **Kali 包**：`thc-ipv6` ｜ **官方文档**：<https://www.kali.org/tools/thc-ipv6/>

## 1. 安装

```bash
sudo apt update
sudo apt install thc-ipv6
```

| 项目 | 内容 |
|------|------|
| 版本 | 3.8 |
| 架构 | linux-any |
| 可执行命令 | `thc-ipv6`、`atk6-address6`、`atk6-alive6`、`atk6-connect6`、`atk6-connsplit6`、`atk6-covert_send6`、`atk6-covert_send6d`、`atk6-denial6`、`atk6-detect-new-ip6`、`atk6-detect_sniffer6`、`atk6-dnsdict6`、`atk6-dnsrevenum6`、`atk6-dnssecwalk`、`atk6-dos-new-ip6`、`atk6-dump_dhcp6`、`atk6-dump_router6`、`atk6-exploit6`、`atk6-extract_hosts6`、`atk6-extract_networks6`、`atk6-fake_advertise6`、`atk6-fake_dhcps6`、`atk6-fake_dns6d`、`atk6-fake_dnsupdate6`、`atk6-fake_mipv6`、`atk6-fake_mld26`、`atk6-fake_mld6`、`atk6-fake_mldrouter6`、`atk6-fake_pim6`、`atk6-fake_router26`、`atk6-fake_router6`、`atk6-fake_solicitate6`、`atk6-firewall6`、`atk6-flood_advertise6`、`atk6-flood_dhcpc6`、`atk6-flood_mld26`、`atk6-flood_mld6`、`atk6-flood_mldrouter6`、`atk6-flood_redir6`、`atk6-flood_router26`、`atk6-flood_router6`、`atk6-flood_rs6`、`atk6-flood_solicitate6`、`atk6-flood_unreach6`、`atk6-four2six`、`atk6-fragmentation6`、`atk6-fragrouter6`、`atk6-fuzz_dhcpc6`、`atk6-fuzz_dhcps6`、`atk6-fuzz_ip6`、`atk6-implementation6`、`atk6-implementation6d`、`atk6-inject_alive6`、`atk6-inverse_lookup6`、`atk6-kill_router6`、`atk6-ndpexhaust26`、`atk6-ndpexhaust6`、`atk6-node_query6`、`atk6-parasite6`、`atk6-passive_discovery6`、`atk6-randicmp6`、`atk6-redir6`、`atk6-redirsniff6`、`atk6-rsmurf6`、`atk6-sendpees6`、`atk6-sendpeesmp6`、`atk6-smurf6`、`atk6-thcping6`、`atk6-thcsyn6`、`atk6-toobig6`、`atk6-toobigsniff6`、`atk6-trace6` |
| 依赖 | `libc6`、`libnetfilter-queue1`、`libpcap0.8t64`、`libssl3t64`、`atk6-address6` |
| 安装体积 | 3.68 MB |
| 官网 | <http://www.thc.org/thc-ipv6/> |
| 源码仓库 | <https://salsa.debian.org/pkg-security-team/thc-ipv6> |
| 包追踪 | <https://pkg.kali.org/pkg/thc-ipv6> |

## 2. 官方用法示例

> 以下为 Kali 官方工具页给出的示例与输出原文。

```text
Usage Example
Convert an IPv6 address to a MAC address and vice-versa:
root@kali:~# address6 fe80::76d4:35ff:fe4e:39c8
74:d4:35:4e:39:c8
root@kali:~# address6 74:d4:35:4e:39:c8
fe80::76d4:35ff:fe4e:39c8

alive6 Usage Example
root@kali:~# alive6 eth0
Alive: fd77:7c68:420a:1:426c:8fff:fe1b:cb90 [ICMP parameter problem]
Alive: fd77:7c68:420a:1:20c:29ff:fee5:5bf4 [ICMP echo-reply]
Alive: fd77:7c68:420a:1:75d9:4f39:a46a:6f83 [ICMP echo-reply]
Alive: fd77:7c68:420a:1:6912:8e80:e02f:1969 [ICMP echo-reply]
Alive: fd77:7c68:420a:1:201:6cff:fe6f:ddd1 [ICMP echo-reply]

detect-new-ip6 Usage Example
root@kali:~# detect-new-ip6 eth0
Started ICMP6 DAD detection (Press Control-C to end) ...
Detected new ip6 address: fe80::85d:9879:9251:853a

dnsdict6 Usage Example
root@kali:~# dnsdict6 example.com
Starting DNS enumeration work on example.com. ...
Starting enumerating example.com. - creating 8 threads for 798 words...
Estimated time to completion: 1 to 2 minutes
www.example.com. => 2606:2800:220:6d:26bf:1447:1097:aa7
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 71 个可执行命令，下面是官方页面内嵌的帮助原文。

### `address6`

> 官方示例调用：`address6 fe80::76d4:35ff:fe4e:39c8`

```text
root@kali:~# address6 fe80::76d4:35ff:fe4e:39c8
74:d4:35:4e:39:c8
```

### `address6 74:d4:35:4e:39:c8`

> 官方示例调用：`address6 74:d4:35:4e:39:c8`

```text
root@kali:~# address6 74:d4:35:4e:39:c8
fe80::76d4:35ff:fe4e:39c8
alive6 Usage Example
```

### `alive6`

> 官方示例调用：`alive6 eth0`

```text
root@kali:~# alive6 eth0
Alive: fd77:7c68:420a:1:426c:8fff:fe1b:cb90 [ICMP parameter problem]
Alive: fd77:7c68:420a:1:20c:29ff:fee5:5bf4 [ICMP echo-reply]
Alive: fd77:7c68:420a:1:75d9:4f39:a46a:6f83 [ICMP echo-reply]
Alive: fd77:7c68:420a:1:6912:8e80:e02f:1969 [ICMP echo-reply]
Alive: fd77:7c68:420a:1:201:6cff:fe6f:ddd1 [ICMP echo-reply]
detect-new-ip6 Usage Example
```

### `detect-new-ip6`

> 官方示例调用：`detect-new-ip6 eth0`

```text
root@kali:~# detect-new-ip6 eth0
Started ICMP6 DAD detection (Press Control-C to end) ...
Detected new ip6 address: fe80::85d:9879:9251:853a
dnsdict6 Usage Example
```

### `dnsdict6`

> 官方示例调用：`dnsdict6 example.com`

```text
root@kali:~# dnsdict6 example.com
Starting DNS enumeration work on example.com. ...
Starting enumerating example.com. - creating 8 threads for 798 words...
Estimated time to completion: 1 to 2 minutes
www.example.com. => 2606:2800:220:6d:26bf:1447:1097:aa7
```

### `atk6-address6`

> 官方示例调用：`atk6-address6 -h`

```text
root@kali:~# atk6-address6 -h
atk6-address6 3.8 (c) 2020 by van Hauser / THC <
[email protected]
> www.github.com/vanhauser-thc/thc-ipv6
Syntax:
	atk6-address6 mac-address [ipv6-prefix]
	atk6-address6 ipv4-address [ipv6-prefix]
	atk6-address6 ipv6-address
Converts a mac or IPv4 address to an IPv6 address (link local if no prefix is
given as 2nd option) or, when given an IPv6 address, prints the mac or IPv4
address. Prints all possible variations. Returns -1 on errors or the number of
variations found
```

### `atk6-alive6`

> 官方示例调用：`atk6-alive6 -h`

```text
root@kali:~# atk6-alive6 -h
atk6-alive6 3.8 (c) 2020 by van Hauser / THC <
[email protected]
> www.github.com/vanhauser-thc/thc-ipv6
Syntax: atk6-alive6 [-CFHLMPSdlpvV] [-I srcip6] [-i file] [-o file] [-e opt] [-s port,..] [-a port,..] [-u port,..] [-T tag] [-W TIME] interface [unicast-or-multicast-address [remote-router]]
Options:
 Output Options:
  -i file    check systems from input file
  -o file    write results to output file
  -v         verbose information (twice: detailed, thrice: dumping packets)
  -d         DNS resolve alive IPv6 addresses
 Enumerate Options:
  -M         enumerate hardware addresses (MAC) from input addresses (slow!)
  -C         enumerate common addresses of input networks, -CC for large scan
  -4 ipv4/range  test various IPv4 address encodings per network (eg 1.2.3.4/24)
 Alive Technique Options:
  -p         send a ping packet for alive check (default)
  -e dst,hop send an errornous packets: destination (default), hop-by-hop
  -s port,port,..  TCP-SYN packet to ports for alive check or "portscan"
  -a port,port,..  TCP-ACK packet to ports for alive check
  -u port,port,..  UDP packet to ports for alive check
  -F         firewall mode: -p -e dst -u 53 -s 22,25,80,443,9511 -a 9511
 Sending Options
  -n number  how often to send each packet (default: local 1, remote 2)
  -W time    time in ms to wait after sending a packet (default: 1)
  -S         slow mode, get best router for each remote target or when proxy-NA
  -I src[/mask]  use the specified IPv6 address as source. Use mask for random.
  -l         use link-local address for multicast addresses instead of global
  -P         only print addresses that would be scanned, no packets are sent!
  -m         raw mode (for network adapters where you do not have Ethernet)
 Help Options:
  -hh        show even more options
Target address on command line or in input file can include ranges in the form
of 2001:db8::1-fff or 2001:db8::1-2:0-ffff:0:0-ffff, etc.
Do not use the ranges (from-to) option with -M, -C or -4.
If you use SYN packets (-s/-F option), automatic OS detection is performed.
Returns -1 on errors, 0 if a system was found alive or 1 if nothing was found.
```

### `atk6-connect6`

> 官方示例调用：`atk6-connect6 -h`

```text
root@kali:~# atk6-connect6 -h
connect6 3.8 (c) 2020 by van Hauser / THC <
[email protected]
> www.github.com/vanhauser-thc/thc-ipv6
Syntax: atk6-connect6 [-a | -A type] [-i] target-ip target-port
Options:
  -a       send Hop-by-Hop Router Alert option
  -A type  like -a but lets you define the alarmtype (number)
  -i       interactive mode (like telnet)
  -I       end a linefeed, wait for a string, print it
  -O       try TCP Fast Open connection
  -w ms    wait time for connect in ms (default: 1000)
  -p       ping mode
You can supply a %interface identifier to the target-ip
Returns 0 on successful connect, 1 on timeout/reset
```

### `atk6-connsplit6`

> 官方示例调用：`atk6-connsplit6 -h`

```text
root@kali:~# atk6-connsplit6 -h
splitconnect6 3.8 (c) 2020 by van Hauser / THC <
[email protected]
> www.github.com/vanhauser-thc/thc-ipv6
Syntax: [-vd] atk6-connsplit6 INTERFACE client|server
Options:
  -v   verbose mode
  -d   debug mode
Manipulates all incoming (client) or outgoing (server) TCP connections that are
from (server) or to (client) port 64446, and sets a new destinatin (server) or
source (client) address.
The purpose of this is a proof of concept to make connect analysis difficult.
It is recommended to use the splitconnect6.sh script to control this tool.
```

### `atk6-covert_send6`

> 官方示例调用：`atk6-covert_send6 -h`

```text
root@kali:~# atk6-covert_send6 -h
atk6-covert_send6 3.8 (c) 2020 by van Hauser / THC <
[email protected]
> www.github.com/vanhauser-thc/thc-ipv6
Syntax: atk6-covert_send6 [-m mtu] [-k key] [-s resend] interface target file [port]
Options:
  -m mtu     specifies the maximum MTU (default: interface MTU, min: 1000)
  -k key     encrypt the content with Blowfish-160
  -s resend  send each packet RESEND number of times, default: 1
Sends the content of FILE covertly to the target, And its POC - don't except
too much sophistication - its just put into the destination header.
```

## 4. 实践清单

按顺序做完这五步，就能把工具从「装上」推进到「会用」：

- [ ] **1.** **装好并确认版本** —— `sudo apt install thc-ipv6`，再执行 `thc-ipv6 --version` 2>/dev/null || `thc-ipv6 -V`
- [ ] **2.** **读官方帮助** —— `thc-ipv6 -h`，需要细节时 `man thc-ipv6`
- [ ] **3.** **在自有靶场跑最小用例** —— 用 `thc-ipv6 -h` 里最简单的那个子命令试一次
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/thc-ipv6/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/discovery.md`](../../tools/by-attack/discovery.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/thc-ipv6/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/thc-ipv6/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
