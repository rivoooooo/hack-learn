# sippts

> Set of tools to audit SIP based VoIP Systems Sippts is a set of tools to audit VoIP servers and devices using SIP protocol. Sippts is programmed in Python and it allows pentesters to check the security of a VoIP server using SIP protocol.

> **功能分类**：通用工具 ｜ **Kali 包**：`sippts` ｜ **官方文档**：<https://www.kali.org/tools/sippts/>

## 1. 安装

```bash
sudo apt update
sudo apt install sippts
```

| 项目 | 内容 |
|------|------|
| 版本 | 4.1.2 |
| 架构 | all |
| 可执行命令 | `sippts`、`sippts-gui` |
| 依赖 | `python3`、`python3-ipy`、`python3-netifaces`、`python3-pyshark`、`python3-rel`、`python3-requests`、`python3-scapy`、`python3-websocket` |
| 安装体积 | 762 KB |
| 官网 | <https://github.com/Pepelux/sippts> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/sippts> |
| 包追踪 | <https://pkg.kali.org/pkg/sippts> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
sippts -h          # 查看用法
man sippts         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 2 个可执行命令，下面是官方页面内嵌的帮助原文。

### `sippts`

> 官方示例调用：`sippts -h`

```text
root@kali:~# sippts -h
usage: sippts [-h]
              {video,astami,scan,exten,rcrack,send,wssend,enumerate,leak,ping,invite,dump,dcrack,flood,sniff,spoof,pcapdump,rtpbleed,rtcpbleed,rtpbleedflood,rtpbleedinject} ...
               __ _
             .: .' '.
            /: /     \_
           ;: ;  ,-'/`:\
           |: | |  |() :|
           ;: ;  '-.\_:/
            \: \     /`
             ':_'._.'
                ||
               /__\
    .---.     |====|
  .'   _,"-,__|::  |
 /    ((O)=;--.::  |
;      `|: |  |::  |
|       |: |  |::  |
|       |: |  |::  |                                                   SIPPTS version 4.1.2 (last version found an invalid character in header name)
|       |: |  |::  |                                                        CVE version 0.1 (last version found an invalid character in header name)
|      /:'__\ |::  |                                      https://github.com/Pepelux/sippts
|     [______]|::  |                              by Pepelux - https://twitter.com/pepeluxx
|      `----` |::  |__
|         _.--|::  |  ''--._
;       .'  __|====|__      '.
 \    .'_.-'._ `""` _.'-._    '.
  '--'/`      `'' ''`     `\    '.__
      '._     SIPPTS     _.'
        # `""--......--""`
 -= SIPPTS is a set of tools for auditing VoIP systems based on the SIP protocol =-
Commands:
  {video,astami,scan,exten,rcrack,send,wssend,enumerate,leak,ping,invite,dump,dcrack,flood,sniff,spoof,pcapdump,rtpbleed,rtcpbleed,rtpbleedflood,rtpbleedinject}
    video                                         Animated help
    astami                                        Asterisk AMI pentest
    scan                                          Fast SIP scanner
    exten                                         Search SIP extensions of a
                                                  PBX
    rcrack                                        Remote password cracker
    send                                          Send a customized message
    wssend                                        Send a customized message
                                                  over WS
    enumerate                                     Enumerate methods of a SIP
                                                  server
    leak                                          Exploit SIP Digest Leak
                                                  vulnerability
    ping                                          SIP ping
    invite                                        Try to make calls through a
                                                  PBX
    dump                                          Dump SIP digest
                                                  authentications from a PCAP
                                                  file
    dcrack                                        SIP digest authentication
                                                  cracking
    flood                                         Flood a SIP server
    sniff                                         SIP network sniffing
    spoof                                         ARP Spoofing tool
    pcapdump                                      Extract data from a PCAP
                                                  file
    rtpbleed                                      Detect RTPBleed
                                                  vulnerability (send RTP
                                                  streams)
    rtcpbleed                                     Detect RTPBleed
                                                  vulnerability (send RTCP
                                                  streams)
    rtpbleedflood                                 Exploit RTPBleed
                                                  vulnerability (flood RTP)
    rtpbleedinject                                Exploit RTPBleed
                                                  vulnerability (inject WAV
                                                  file)
Options:
  -h, --help                                      show this help message and
                                                  exit
Command help:
  sippts <command> -h
```

### `sippts-gui`

> 官方示例调用：`sippts-gui -h`

```text
root@kali:~# sippts-gui -h
              _              _
             | |------------| |
          .-'| |            | |`-.
        .'   | |   SIPPTS   | |   `.
     .-'      \ \          / /      `-.
   .'        _.| |--------| |._        `.
  /    -.  .'  | |        | |  `.  .-    \
 /       `(    | |________| |    )'       \
|          \  .i------------i.  /          |
|        .-')/                \(`-.        |
\    _.-'.-'/     ________     \`-.`-._    /
 \.-'_.-'  /   .-' ______ `-.   \  `-._`-./\
  `-'     /  .' .-' _   _`-. `.  \     `-' \\
         | .' .' _ (3) (2) _`. `. |        //
        / /  /  (4)  ___  (1)_\  \ \       \\                                   SIPPTS version 4.1.2 (last version found an invalid character in header name)
        | | |  _   ,'   `.==' `| | |       //                                        CVE version 0.1 (last version found an invalid character in header name)
        | | | (5)  |     | (O) | | |      //                       https://github.com/Pepelux/sippts
        | | |   _  `.___.' _   | | |      \\               by Pepelux - https://twitter.com/pepeluxx
        | \  \ (6)  _   _ (9) /  / |      //
        /  `. `.   (7) (8)  .' .'  \      \\
       /     `. `-.______.-' .'     \     //
      /        `-.________.-'        \ __//
     |                                |--'
     |================================|
     "--------------------------------"
Welcome to SIPPTS! Type ? or help to list commands
[!] Client interface: eth0
[!] Client IP address: 10.0.2.15
[!] Network mask: 255.255.255.0
[!] Gateway: 10.0.2.2
Type ? or help to list commands
SIPPTS>
Updated on: 2026-Aug-25
 Edit this page
sigma-cli
sleuthkit
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install sippts`，再执行 `sippts --version` 2>/dev/null || `sippts -V`
- [ ] **2.** **读官方帮助** —— `sippts -h`，需要细节时 `man sippts`
- [ ] **3.** **在自有靶场跑最小用例** —— 用 `sippts -h` 里最简单的那个子命令试一次
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/sippts/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/discovery.md`](../../tools/by-attack/discovery.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/sippts/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/sippts/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
