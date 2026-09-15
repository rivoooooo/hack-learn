# hexinject

> Versatile packet injector and sniffer HexInject is a very versatile packet injector and sniffer, that provide a command-line framework for raw network access. It’s designed to work together with others command-line utilities, and for this …

> **功能分类**：嗅探与欺骗 ｜ **Kali 包**：`hexinject` ｜ **官方文档**：<https://www.kali.org/tools/hexinject/>

## 1. 安装

```bash
sudo apt update
sudo apt install hexinject
```

| 项目 | 内容 |
|------|------|
| 版本 | 1.6 |
| 架构 | any |
| 可执行命令 | `hexinject`、`hex2raw`、`packets.tcl`、`prettypacket` |
| 依赖 | `libc6`、`libpcap0.8t64`、`tcl`、`hex2raw` |
| 安装体积 | 100 KB |
| 官网 | <https://hexinject.sourceforge.net/> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/hexinject> |
| 包追踪 | <https://pkg.kali.org/pkg/hexinject> |

## 2. 官方用法示例

> 以下为 Kali 官方工具页给出的示例与输出原文。

```text
Usage Example
Start in sniffing mode (-s) through the eth0 interface (-i eth0):
root@kali:~# hexinject -s -i eth0
FF FF FF FF FF FF 40 6C 8F 1B CB 90 08 00 45 00 00 31 E4 36 00 00 40 11 11 4E C0 A8 01 E8 C0 A8 01 FF D3 C6 7E 9C 00 1D B1 DA 4D 2D 53 45 41 52 43 48 20 2A 20 48 54 54 50 2F 31 2E 31 0D 0A
FF FF FF FF FF FF 40 6C 8F 1B CB 90 08 00 45 00 00 31 A1 63 00 00 40 11 54 21 C0 A8 01 E8 C0 A8 01 FF FF 69 7E 9E 00 1D 86 35 4D 2D 53 45 41 52 43 48 20 2A 20 48 54 54 50 2F 31 2E 31 0D 0A
FF FF FF FF FF FF 7C C3 A1 A4 B4 70 08 00 45 00 00 31 BF 94 00 00 40 11 35 FC C0 A8 01 DC C0 A8 01 FF E3 ED 7E 9C 00 1D A1 BF 4D 2D 53 45 41 52 43 48 20 2A 20 48 54 54 50 2F 31 2E 31 0D 0A
FF FF FF FF FF FF 7C C3 A1 A4 B4 70 08 00 45 00 00 31 2F DE 00 00 40 11 C5 B2 C0 A8 01 DC C0 A8 01 FF C5 16 7E 9E 00 1D C0 94 4D 2D 53 45 41 52 43 48 20 2A 20 48 54 54 50 2F 31 2E 31 0D 0A

prettypacket Usage Example
Print an example of a UDP packet (-x udp):
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 4 个可执行命令，下面是官方页面内嵌的帮助原文。

### `hexinject`

> 官方示例调用：`hexinject -s -i eth0`

```text
root@kali:~# hexinject -s -i eth0
FF FF FF FF FF FF 40 6C 8F 1B CB 90 08 00 45 00 00 31 E4 36 00 00 40 11 11 4E C0 A8 01 E8 C0 A8 01 FF D3 C6 7E 9C 00 1D B1 DA 4D 2D 53 45 41 52 43 48 20 2A 20 48 54 54 50 2F 31 2E 31 0D 0A
FF FF FF FF FF FF 40 6C 8F 1B CB 90 08 00 45 00 00 31 A1 63 00 00 40 11 54 21 C0 A8 01 E8 C0 A8 01 FF FF 69 7E 9E 00 1D 86 35 4D 2D 53 45 41 52 43 48 20 2A 20 48 54 54 50 2F 31 2E 31 0D 0A
FF FF FF FF FF FF 7C C3 A1 A4 B4 70 08 00 45 00 00 31 BF 94 00 00 40 11 35 FC C0 A8 01 DC C0 A8 01 FF E3 ED 7E 9C 00 1D A1 BF 4D 2D 53 45 41 52 43 48 20 2A 20 48 54 54 50 2F 31 2E 31 0D 0A
FF FF FF FF FF FF 7C C3 A1 A4 B4 70 08 00 45 00 00 31 2F DE 00 00 40 11 C5 B2 C0 A8 01 DC C0 A8 01 FF C5 16 7E 9E 00 1D C0 94 4D 2D 53 45 41 52 43 48 20 2A 20 48 54 54 50 2F 31 2E 31 0D 0A
prettypacket Usage Example
Print an example of a UDP packet (
-x udp
):
```

### `prettypacket`

> 官方示例调用：`prettypacket -x udp`

```text
root@kali:~# prettypacket -x udp
Ethernet Header:
 1C AF F7 6B 0E 4D        Destination hardware address
 AA 00 04 00 0A 04        Source hardware address
 08 00                    Lenght/Type
IP Header:
 45                       Version / Header length
 00                       ToS / DFS
 00 3C                    Total length
 9B 23                    ID
 00 00                    Flags / Fragment offset
 40                       TTL
 11                       Protocol
 70 BC                    Checksum
 C0 A8 01 09              Source address
 D0 43 DC DC              Destination address
UDP Header:
 91 02                    Source port
 00 35                    Destination port
 00 28                    Length
 6F 0B                    Checksum
Payload or Trailer:
 AE 9C 01 00 00 01 00 00 00 00 00 00 03 77 77 77 06 67 6F 6F 67 6C 65 03 63 6F
 6D 00 00 01 00 01
hex2raw Usage Example
```

### `hex2raw`

```text
root@kali:~# hex2raw
 FF 40 6C 8F 1B CB 90 08 00 45 00 00 31 E4 36 00 00 40 11 11 4E C0 A8 01 E8 C0 A8 01 FF D3 C6 7E 9C 00 1D B1 DA 4D 2D 53 45 41 52 43 48 20 2A 20 48 54 54 50 2F 31 2E 31 0D 0A
FF FF FF FF FF FF 40 6C 8F 1B CB 90 08 00 45 00 00 31 A1 63 00 00 40 11 54 21 C0 A8 01 E8 C0 A8 01 FF FF 69 7E 9E 00 1D 86 35 4D 2D 53 45 41 52 43 48 20 2A 20 48 54 54 50 2F 31 2E 31 0D 0A
������@lE1�c@T!�������i~��5M-SEARCH * HTTP/1.1
packets.tcl Usage Example
```

### `packets.tcl`

> 官方示例调用：`packets.tcl 'ethernet(dst=ff:ff:ff:ff:ee:ee,src=aa:aa:ee:ff:ff:ff,type=0x0800)+ip(ihl=5,ver=4,tos=0xc0,totlen=58,id=62912,fragoff=0,mf=0,df=0,rf=0,ttl=64,proto=1,cksum=0xe500,saddr=192.168.1.7,daddr=192.168.1.6)+icmp(type=3,code=3,unused=0)+data(str=aaaa)+udp(sport=33169,dport=10,len=10,cksum=0x94d6)+data(str=aaaa)+arp(htype=ethernet,ptype=ip,hsize=6,psize=4,op=request,shard=00:11:22:33:44:55,sproto=192.168.1.1,thard=22:22:22:22:22:22,tproto=10.0.0.1)' > packet-out`

```text
root@kali:~# packets.tcl 'ethernet(dst=ff:ff:ff:ff:ee:ee,src=aa:aa:ee:ff:ff:ff,type=0x0800)+ip(ihl=5,ver=4,tos=0xc0,totlen=58,id=62912,fragoff=0,mf=0,df=0,rf=0,ttl=64,proto=1,cksum=0xe500,saddr=192.168.1.7,daddr=192.168.1.6)+icmp(type=3,code=3,unused=0)+data(str=aaaa)+udp(sport=33169,dport=10,len=10,cksum=0x94d6)+data(str=aaaa)+arp(htype=ethernet,ptype=ip,hsize=6,psize=4,op=request,shard=00:11:22:33:44:55,sproto=192.168.1.1,thard=22:22:22:22:22:22,tproto=10.0.0.1)' > packet-out
```

### `hex2raw -h`

> 官方示例调用：`hex2raw -h`

```text
root@kali:~# hex2raw -h
Hex2Raw 1.6 [convert hexstrings on stdin to raw data on stdout]
written by: Emanuele Acri <
[email protected]
>
Usage:
	hex2raw [-r|-h]
Options:
	-r	reverse mode (raw to hexstring)
	-h	this help screen
```

### `hexinject --help`

> 官方示例调用：`hexinject --help`

```text
root@kali:~# hexinject --help
hexinject: invalid option -- '-'
HexInject 1.6 [hexadecimal packet injector/sniffer]
written by: Emanuele Acri <
[email protected]
>
Usage:
   hexinject <mode> <options>
Options:
  -s sniff mode
  -p inject mode
  -r raw mode (instead of the default hexadecimal mode)
  -f <filter> custom pcap filter
  -i <device> network device to use
  -F <file> pcap file to use as device (sniff mode only)
  -c <count> number of packets to capture
  -t <time> sleep time in microseconds (default 100)
  -I list all available network devices
Injection options:
  -C disable automatic packet checksum
  -S disable automatic packet size fields
Interface options:
  -P disable promiscuous mode
  -M put the wireless interface in monitor mode
     (experimental: use airmon-ng instead of this...)
Other options:
  -h help screen
```

### `packets.tcl -h`

> 官方示例调用：`packets.tcl -h`

```text
root@kali:~# packets.tcl -h
Packets.tcl -- Generates binary packets specified using an
               APD-like data format: http://wiki.hping.org/26
usage:
	packets.tcl 'APD packet description'
example packets:
ethernet(dst=ff:ff:ff:ff:ee:ee,src=aa:aa:ee:ff:ff:ff,type=0x0800)+ip(ihl=5,ver=4,tos=0xc0,totlen=58,id=62912,fragoff=0,mf=0,df=0,rf=0,ttl=64,proto=1,cksum=0xe500,saddr=192.168.1.7,daddr=192.168.1.6)+icmp(type=3,code=3,unused=0)+data(str=aaaa)+udp(sport=33169,dport=10,len=10,cksum=0x94d6)+data(str=aaaa)+arp(htype=ethernet,ptype=ip,hsize=6,psize=4,op=request,shard=00:11:22:33:44:55,sproto=192.168.1.1,thard=22:22:22:22:22:22,tproto=10.0.0.1)
ethernet(dst=ff:ff:ff:ff:ff:ff,src=ff:ff:ff:ff:ff:ff,type=0x0800)+ip(ihl=5,ver=4,tos=00,totlen=30,id=60976,fragoff=0,mf=0,df=1,rf=0,ttl=64,proto=tcp,cksum=0x40c9,saddr=192.168.1.9,daddr=173.194.44.95)+tcp(sport=32857,dport=80,seq=1804471615,ack=0,ns=0,off=5,flags=s,win=62694,cksum=0xda46,urp=0)
ethernet(dst=ff:ff:ff:ff:ff:ff,src=ff:ff:ff:ff:ff:ff,type=0x0800)+ip(ihl=5,ver=4,tos=00,totlen=30,id=60976,fragoff=0,mf=0,df=1,rf=0,ttl=64,proto=tcp,cksum=0x40c9,saddr=192.168.1.9,daddr=173.194.44.95)+tcp(sport=32857,dport=80,seq=1804471615,ack=0,ns=0,off=8,flags=s,win=62694,cksum=0xda46,urp=0)+tcp.nop()+tcp.nop()+tcp.timestamp(val=54111314,ecr=1049055856)+data(str=f0a)
```

### `prettypacket -h`

> 官方示例调用：`prettypacket -h`

```text
root@kali:~# prettypacket -h
PrettyPacket 1.6 [disassembler for raw network packets]
written by: Emanuele Acri <
[email protected]
>
Usage:
	prettypacket [-x|-d|-h]
Options:
	-x <type>  print example packet, to see its structure
	-d <type>  dump example packet as hexstring
	           (types: tcp, udp, icmp, igmp, arp, stp,
	                   ipv6_tcp, ipv6_icmp, ipv6_in_ipv4)
	-h         this help screen
Updated on: 2025-Dec-09
 Edit this page
hekatomb
hexwalk
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install hexinject`，再执行 `hexinject --version` 2>/dev/null || `hexinject -V`
- [ ] **2.** **读官方帮助** —— `hexinject -h`，需要细节时 `man hexinject`
- [ ] **3.** **在自有靶场跑最小用例** —— 官方给出的调用形式是：`Usage:`
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/hexinject/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/discovery.md`](../../tools/by-attack/discovery.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/hexinject/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/hexinject/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
