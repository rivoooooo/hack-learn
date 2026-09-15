# sctpscan

> SCTP network scanner for discovery and security SCTP network scanner for discovery and security

> **功能分类**：漏洞分析 ｜ **Kali 包**：`sctpscan` ｜ **官方文档**：<https://www.kali.org/tools/sctpscan/>

## 1. 安装

```bash
sudo apt update
sudo apt install sctpscan
```

| 项目 | 内容 |
|------|------|
| 版本 | 0.1 |
| 架构 | any |
| 可执行命令 | `sctpscan` |
| 依赖 | `libc6`、`libglib2.0-0t64` |
| 安装体积 | 78 KB |
| 官网 | <https://github.com/philpraxis/sctpscan> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/sctpscan> |
| 包追踪 | <https://pkg.kali.org/pkg/sctpscan> |

## 2. 官方用法示例

> 以下为 Kali 官方工具页给出的示例与输出原文。

```text
Usage Example
Scan (-s) for frequently used ports (-F) on the remote network (-r 192.168.1.*):
root@kali:~# sctpscan -s -F -r 192.168.1.*
SCTPscan - Copyright (C) 2002 - 2009 Philippe Langlois.
Netscanning with Crc32 checksumed packet
Portscanning Frequent Ports on 192.168.1.*.
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `sctpscan`

官方给出的调用示例：`sctpscan -s -F -r 192.168.1.*`

```text
root@kali:~# sctpscan -s -F -r 192.168.1.*
SCTPscan - Copyright (C) 2002 - 2009 Philippe Langlois.
Netscanning with Crc32 checksumed packet
Portscanning Frequent Ports on 192.168.1.*.
```

### `sctpscan（示例）`

官方给出的调用示例：`sctpscan -h`

```text
root@kali:~# sctpscan -h
SCTPscan - Copyright (C) 2002 - 2009 Philippe Langlois.
SCTPscan - Copyright (C) 2002 - 2009 Philippe Langlois.
SCTPscan comes with ABSOLUTELY NO WARRANTY; for details read the LICENSE or COPYING file.
Usage:  sctpscan [options]
Options:
  -p, --port <port>           (default: 10000)
      port specifies the remote port number
  -P, --loc_port <port>           (default: 10000)
      port specifies the local port number
  -l, --loc_host <loc_host>   (default: 127.0.0.1)
      loc_host specifies the local (bind) host for the SCTP
      stream with optional local port number
  -r, --rem_host <rem_host>   (default: 127.0.0.2)
      rem_host specifies the remote (sendto) address for the SCTP
      stream with optional remote port number
  -s  --scan -r aaa[.bbb[.ccc]]
      scan all machines within network
  -m  --map
      map all SCTP ports from 0 to 65535 (portscan)
  -F  --Frequent
      Portscans the frequently used SCTP ports
      Frequent SCTP ports: 1, 7, 9, 20, 21, 22, 80, 100, 128, 179, 260, 250, 443, 1167, 1812, 2097, 2000, 2001, 2010, 2011, 2020, 2021, 2100, 2110, 2120, 2225, 2427, 2477, 2577, 2904, 2905, 2906, 2907, 2908, 2909, 2944, 2945, 3000, 3097, 3565, 3740, 3863, 3864, 3868, 4000, 4739, 4740, 5000, 5001, 5060, 5061, 5090, 5091, 5672, 5675, 6000, 6100, 6110, 6120, 6130, 6140, 6150, 6160, 6170, 6180, 6190, 6529, 6700, 6701, 6702, 6789, 6790, 7000, 7001, 7102, 7103, 7105, 7551, 7626, 7701, 7800, 8000, 8001, 8471, 8787, 9006, 9084, 9899, 9911, 9900, 9901, 9902, 10000, 10001, 11146, 11997, 11998, 11999, 12205, 12235, 13000, 13001, 14000, 14001, 20049, 29118, 29168, 30000, 32905, 32931, 32768
  -a  --autoportscan
      Portscans automatically any host with SCTP aware TCP/IP stack
  -i  --linein
      Receive IP to scan from stdin
  -f  --fuzz
      Fuzz test all the remote protocol stack
  -B  --bothpackets
      Send packets with INIT chunk for one, and SHUTDOWN_ACK for the other
  -b  --both_checksum
      Send both checksum: new crc32 and old legacy-driven adler32
  -C  --crc32
      Calculate checksums with the new crc32
  -A  --adler32
      Calculate checksums with the old adler32
  -Z  --zombie
      Does not collaborate to the SCTP Collaboration platform. No reporting.
  -d  --dummyserver
      Starts a dummy SCTP server on port 10000. You can then try to scan it from another machine.
  -E  --exec <script_name>
      Executes <script_name> each time an open SCTP port is found.
      Execution arguments: <script_name> host_ip sctp_port
  -t  --tcpbridge <listen TCP port>
      Bridges all connection from <listen TCP port> to remote designated SCTP port.
  -S  --streams <number of streams>
      Tries to establish SCTP association with the specified <number of streams> to remote designated SCTP destination.
Scan port 9999 on 192.168.1.24
sctpscan -l 192.168.1.2 -r 192.168.1.24 -p 9999
Scans for availability of SCTP on 172.17.8.* and portscan any host with SCTP stack
sctpscan -s -l 172.22.1.96 -r 172.17.8
Scans frequently used ports on 172.17.8.*
sctpscan -s -F -l 172.22.1.96 -r 172.17.8
Scans all class-B network for frequent port
sctpscan -s -F -r 172.22 -l `ifconfig eth0 | grep 'inet addr:' |  cut -d: -f2 | cut -d ' ' -f 1 `
Simple verification end to end on the local machine:
sctpscan -d &
sctpscan -s -l 192.168.1.24 -r 192.168.1 -p 10000
This tool does NOT work behind most NAT.
That means that most of the routers / firewall don't know how to NAT SCTP packets.
You _need_ to use this tool from a computer having a public IP address (i.e. non-RFC1918)
Updated on: 2025-Dec-09
 Edit this page
scrounge-ntfs
secure-socket-funneling
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install sctpscan`，再执行 `sctpscan --version` 2>/dev/null || `sctpscan -V`
- [ ] **2.** **读官方帮助** —— `sctpscan -h`，需要细节时 `man sctpscan`
- [ ] **3.** **在自有靶场跑最小用例** —— 官方给出的调用形式是：`Usage:  sctpscan [options]`
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/sctpscan/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/discovery.md`](../../tools/by-attack/discovery.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/sctpscan/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/sctpscan/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
