# rtpmixsound

> Mixes pre-recorded audio in real-time A tool to mix pre-recorded audio in real-time with the audio (i.e. RTP) in the specified target audio stream.

> **功能分类**：漏洞分析 ｜ **Kali 包**：`rtpmixsound` ｜ **官方文档**：<https://www.kali.org/tools/rtpmixsound/>

## 1. 安装

```bash
sudo apt update
sudo apt install rtpmixsound
```

| 项目 | 内容 |
|------|------|
| 版本 | 3.0 |
| 架构 | any |
| 可执行命令 | `rtpmixsound` |
| 依赖 | `libc6`、`libfindrtp`、`libnet9`、`libpcap0.8t64` |
| 安装体积 | 231 KB |
| 官网 | <http://www.hackingvoip.com/sec_tools.html> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/rtpmixsound> |
| 包追踪 | <https://pkg.kali.org/pkg/rtpmixsound> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
rtpmixsound -h          # 查看用法
man rtpmixsound         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `rtpmixsound`

官方给出的调用示例：`rtpmixsound /usr/share/rtpmixsound/stapler.wav -v`

```text
root@kali:~# rtpmixsound /usr/share/rtpmixsound/stapler.wav -v
Targeting interface eth0
libfindrtp_find_rtp(): using pcap filter "ip".
State: ip_a ==  | port_a == 0 | ip_b ==  | port_b == 0
```

### `rtpmixsound（示例）`

官方给出的调用示例：`rtpmixsound -h`

```text
root@kali:~# rtpmixsound -h
rtpmixsound - Version 3.0
              January 03, 2007
 Usage:
 Mandatory -
	pathname of file whose audio is to be mixed into the
	    targeted live audio stream. If the file extension is
	    .wav, then the file must be a standard Microsoft
	    RIFF formatted WAVE file meeting these constraints:
	      1) header 'chunks' must be in one of two sequences:
	           RIFF, fmt, fact, data
	             or
	           RIFF, fmt, data
	      2) Compression Code = 1 (PCM/Uncompressed)
	      3) Number of Channels = 1 (mono)
	      4) Sample Rate (Hz) = 8000
	      5) Significant Bits/Sample =
	              signed,   linear 16-bit or
	              unsigned, linear  8-bit
	    If the file name does not specify a .wav extension,
	    then the file is presumed to be a tcpdump formatted
	    file with a sequence of, exclusively, G.711 u-law
	    RTP/UDP/IP/ETHERNET messages
	    Note: Yep, the format is referred to as 'tcpdump'
	          even though this file must contain udp messages
 Optional -
	-a source RTP IPv4 addr
	-A source RTP port
	-b destination RTP IPv4 addr
	-B destination RTP port
	-f spoof factor - amount by which to:
	     a) increment the RTP hdr sequence number obtained
	        from the ith legitimate packet to produce the
	        RTP hdr sequence number for the ith spoofed packet
	     b) multiply the RTP payload length and add that
	        product to the RTP hdr timestamp obtained from
	        the ith legitimate packet to produce the RTP hdr
	        timestamp for the ith spoofed packet
	     c) increment the IP hdr ID number obtained from the
	        ith legitimate packet to produce the IP hdr ID
	        number for the ith spoofed packet
	   [ range: +/- 1000, default: 2 ]
	-i interface (e.g. eth0)
	-j jitter factor - the reception of a legitimate RTP
	     packet in the target audio stream enables the output
	     of the next spoofed packet. This factor determines
	     when that spoofed packet is actually transmitted.
	     The factor relates how close to the next legitimate
	     packet you'd actually like the enabled spoofed packet
	     to be transmitted. For example, -j 10 means 10% of
	     the codec's transmission interval. If the transmission
	     interval = 20,000 usec (i.e. G.711), then delay the
	     output of the spoofed RTP packet until the time-of-day
	     is within 2,000 usec (i.e. 10%) of the time the next
	     legitimate RTP packet is expected. In other words,
	     delay 100% minus the jitter factor, or 18,000 usec
	     in this example. The smaller the jitter factor, the
	     greater the risk you run of not outputting the
	     spoofed packet before the next legitimate RTP packet
	     is received. Therefore, a factor >= 10 is advised.
	   [ range: 0 - 80, default: 80 = output spoof ASAP ]
	-p seconds to pause between setup and injection
	-h help - print this usage
	-v verbose output mode
Note: If you are running the tool from a host with multiple
      ethernet interfaces which are up, be forewarned that
      the order those interfaces appear in your route table
      and the networks accessible from those interfaces might
      compel Linux to output spoofed audio packets to an
      interface different than the one stipulated by you on
      command line. This should not affect the tool unless
      those spoofed packets arrive back at the host through
      the interface you have specified on the command line
      (e.g. the interfaces have connectivity through a hub).
Updated on: 2025-Dec-09
 Edit this page
rtpinsertsound
rubeus
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install rtpmixsound`，再执行 `rtpmixsound --version` 2>/dev/null || `rtpmixsound -V`
- [ ] **2.** **读官方帮助** —— `rtpmixsound -h`，需要细节时 `man rtpmixsound`
- [ ] **3.** **在自有靶场跑最小用例** —— 官方给出的调用形式是：`Usage:`
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/rtpmixsound/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/discovery.md`](../../tools/by-attack/discovery.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/rtpmixsound/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/rtpmixsound/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
