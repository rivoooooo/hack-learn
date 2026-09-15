# rtpbreak

> Detects, reconstructs, and analyzes RTP sessions With rtpbreak you can detect, reconstruct and analyze any RTP session. It doesn’t require the presence of RTCP packets and works independently form the used signaling protocol (SIP, H.323, S…

> **功能分类**：漏洞分析 ｜ **Kali 包**：`rtpbreak` ｜ **官方文档**：<https://www.kali.org/tools/rtpbreak/>

## 1. 安装

```bash
sudo apt update
sudo apt install rtpbreak
```

| 项目 | 内容 |
|------|------|
| 版本 | 1.3a |
| 架构 | any |
| 可执行命令 | `rtpbreak` |
| 依赖 | `libc6`、`libnet9`、`libpcap0.8t64` |
| 安装体积 | 92 KB |
| 官网 | <http://dallachiesa.com/code/rtpbreak/> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/rtpbreak> |
| 包追踪 | <https://pkg.kali.org/pkg/rtpbreak> |

## 2. 官方用法示例

> 以下为 Kali 官方工具页给出的示例与输出原文。

```text
Usage Example
Analyze RTP traffic using interface eth0 (-i eth0), fill in gaps (-g), sniff in promiscuous mode (-m), and save to the given directory (-d rtplog):
root@kali:~# rtpbreak -i eth0 -g -m -d rtplog
 + rtpbreak v1.3a running here!
 + pid: 10951, date/time: 17/05/2014#13:40:02
 + Configuration
   + INPUT
     Packet source: iface 'eth0'
     Force datalink header length: disabled
   + OUTPUT
     Output directory: 'rtplog'
     RTP raw dumps: enabled
     RTP pcap dumps: enabled
     Fill gaps: enabled
     Dump noise: disabled
     Logfile: 'rtplog/rtp.0.txt'
     Logging to stdout: enabled
     Logging to syslog: disabled
     Be verbose: disabled
   + SELECT
     Sniff packets in promisc mode: enabled
     Add pcap filter: disabled
     Expecting even destination UDP port: disabled
     Expecting unprivileged source/destination UDP ports: disabled
     Expecting RTP payload type: any
     Expecting RTP payload length: any
     Packet timeout: 10.00 seconds
     Pattern timeout: 0.25 seconds
     Pattern packets: 5
   + EXECUTION
     Running as user/group: root/root
     Running daemonized: disabled
 * You can dump stats sending me a SIGUSR2 signal
 * Reading packets...
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `rtpbreak`

> 官方示例调用：`rtpbreak -i eth0 -g -m -d rtplog`

```text
root@kali:~# rtpbreak -i eth0 -g -m -d rtplog
 + rtpbreak v1.3a running here!
 + pid: 10951, date/time: 17/05/2014#13:40:02
 + Configuration
   + INPUT
     Packet source: iface 'eth0'
     Force datalink header length: disabled
   + OUTPUT
     Output directory: 'rtplog'
     RTP raw dumps: enabled
     RTP pcap dumps: enabled
     Fill gaps: enabled
     Dump noise: disabled
     Logfile: 'rtplog/rtp.0.txt'
     Logging to stdout: enabled
     Logging to syslog: disabled
     Be verbose: disabled
   + SELECT
     Sniff packets in promisc mode: enabled
     Add pcap filter: disabled
     Expecting even destination UDP port: disabled
     Expecting unprivileged source/destination UDP ports: disabled
     Expecting RTP payload type: any
     Expecting RTP payload length: any
     Packet timeout: 10.00 seconds
     Pattern timeout: 0.25 seconds
     Pattern packets: 5
   + EXECUTION
     Running as user/group: root/root
     Running daemonized: disabled
 * You can dump stats sending me a SIGUSR2 signal
 * Reading packets...
```

### `rtpbreak -h`

> 官方示例调用：`rtpbreak -h`

```text
root@kali:~# rtpbreak -h
Copyright (c) 2007-2008 Dallachiesa Michele <micheleDOTdallachiesaATposteDOTit>
rtpbreak v1.3a is free software, covered by the GNU General Public License.
USAGE: rtpbreak (-r|-i) <source> [options]
 INPUT
  -r <str>      Read packets from pcap file <str>
  -i <str>      Read packets from network interface <str>
  -L <int>      Force datalink header length == <int> bytes
 OUTPUT
  -d <str>      Set output directory to <str> (def:.)
  -w            Disable RTP raw dumps
  -W            Disable RTP pcap dumps
  -g            Fill gaps in RTP raw dumps (caused by lost packets)
  -n            Dump noise packets
  -f            Disable stdout logging
  -F            Enable syslog logging
  -v            Be verbose
 SELECT
  -m            Sniff packets in promisc mode
  -p <str>      Add pcap filter <str>
  -e            Expect even destination UDP port
  -u            Expect unprivileged source/destination UDP ports (>1024)
  -y <int>      Expect RTP payload type == <int>
  -l <int>      Expect RTP payload length == <int> bytes
  -t <float>    Set packet timeout to <float> seconds (def:10.00)
  -T <float>    Set pattern timeout to <float> seconds (def:0.25)
  -P <int>      Set pattern packets count to <int> (def:5)
 EXECUTION
  -Z <str>      Run as user <str>
  -D            Run in background (option -f implicit)
 MISC
  -k            List known RTP payload types
  -h            This
Updated on: 2025-Dec-09
 Edit this page
rsmangler
rtpinsertsound
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install rtpbreak`，再执行 `rtpbreak --version` 2>/dev/null || `rtpbreak -V`
- [ ] **2.** **读官方帮助** —— `rtpbreak -h`，需要细节时 `man rtpbreak`
- [ ] **3.** **在自有靶场跑最小用例** —— 用 `rtpbreak -h` 里最简单的那个子命令试一次
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/rtpbreak/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/discovery.md`](../../tools/by-attack/discovery.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/rtpbreak/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/rtpbreak/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
