# driftnet

> Picks out and displays images from network traffic Inspired by EtherPEG, Driftnet is a program which listens to network traffic and picks out images from TCP streams it observes. It is interesting to run it on a host which sees a lot of we…

> **功能分类**：嗅探与欺骗 ｜ **Kali 包**：`driftnet` ｜ **官方文档**：<https://www.kali.org/tools/driftnet/>

## 1. 安装

```bash
sudo apt update
sudo apt install driftnet
```

| 项目 | 内容 |
|------|------|
| 版本 | 1.5.0 |
| 架构 | any |
| 可执行命令 | `driftnet` |
| 依赖 | `libc6`、`libcairo2`、`libgif7`、`libglib2.0-0t64`、`libgtk-3-0t64`、`libjpeg62-turbo`、`libpcap0.8t64`、`libpng16-16t64`、`libwebp7`、`libwebsockets19t64` |
| 安装体积 | 108 KB |
| 官网 | <https://github.com/deiv/driftnet> |
| 源码仓库 | <https://github.com/deiv/driftnet> |
| 包追踪 | <https://pkg.kali.org/pkg/driftnet> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
driftnet -h          # 查看用法
man driftnet         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `driftnet`

官方给出的调用示例：`driftnet -h`

```text
root@kali:~# driftnet -h
driftnet, version 1.5.0
Capture images from network traffic and display them.
Synopsis: driftnet [options] [filter code]
Options:
  -h               Display this help message.
  -v               Verbose operation.
  -b               Beep when a new image is captured.
  -i interface     Select the interface on which to listen (default: all
                   interfaces).
  -f file          Instead of listening on an interface, read captured
                   packets from a pcap dump file; file can be a named pipe
                   for use with Kismet or similar.
  -p               Do not put the listening interface into promiscuous mode.
  -a               Adjunct mode: do not display images on screen, but save
                   them to a temporary directory and announce their names on
                   standard output.
  -m number        Maximum number of images to keep in temporary directory
                   in adjunct mode.
  -d directory     Use the named temporary directory.
  -x prefix        Prefix to use when saving images.
  -s               Attempt to extract streamed audio data from the network,
                   in addition to images. At present this supports MPEG data
                   only.
  -S               Extract streamed audio but not images.
  -M command       Use the given command to play MPEG audio data extracted
                   with the -s option; this should process MPEG frames
                   supplied on standard input. Default: `mpg123 -'.
  -Z username      Drop privileges to user 'username' after starting pcap.
  -l               List the system capture interfaces.
  -p               Put the interface in monitor mode (not supported on all interfaces).
  -g               Enable GTK display (this is the default).
  -w               Enable the HTTP server to display images.
  -W               Port number for the HTTP server (implies -w). Default: 9090.
Filter code can be specified after any options in the manner of tcpdump(8).
The filter code will be evaluated as `tcp and (user filter code)'
You can save images to the current directory by clicking on them.
Adjunct mode is designed to be used by other programs which want to use
driftnet to gather images from the network. With the -m option, driftnet will
silently drop images if more than the specified number of images are saved
in its temporary directory. It is assumed that some other process is
collecting and deleting the image files.
driftnet, copyright (c) 2001-2002 Chris Lightfoot <
[email protected]
>
          copyright (c) 2012-2022 David Suárez <
[email protected]
>
home page: https://github.com/deiv/driftnet
old home page: http://www.ex-parrot.com/~chris/driftnet/
This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2 of the License, or
(at your option) any later version.
Updated on: 2025-Dec-09
 Edit this page
dploot
dscan
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install driftnet`，再执行 `driftnet --version` 2>/dev/null || `driftnet -V`
- [ ] **2.** **读官方帮助** —— `driftnet -h`，需要细节时 `man driftnet`
- [ ] **3.** **在自有靶场跑最小用例** —— 用 `driftnet -h` 里最简单的那个子命令试一次
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/driftnet/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/discovery.md`](../../tools/by-attack/discovery.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/driftnet/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/driftnet/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
