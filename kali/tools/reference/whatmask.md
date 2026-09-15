# whatmask

> Helper for network settings This package contains a small C program that will help you with network settings. Whatmask can work in two modes. The first mode is to invoke Whatmask with only a subnet mask as the argument. In this mode Whatma…

> **功能分类**：通用工具 ｜ **Kali 包**：`whatmask` ｜ **官方文档**：<https://www.kali.org/tools/whatmask/>

## 1. 安装

```bash
sudo apt update
sudo apt install whatmask
```

| 项目 | 内容 |
|------|------|
| 版本 | 1.2 |
| 架构 | any |
| 可执行命令 | `whatmask` |
| 依赖 | `libc6` |
| 安装体积 | 40 KB |
| 官网 | <http://www.laffeycomputer.com/whatmask.html> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/whatmask> |
| 包追踪 | <https://pkg.kali.org/pkg/whatmask> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
whatmask -h          # 查看用法
man whatmask         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `man`

官方给出的调用示例：`man whatmask`

```text
root@kali:~# man whatmask
Whatmask(1)                         Network                         Whatmask(1)
NAME
     whatmask - Subnet mask notation conversion tool.
SYNTAX
     whatmask <netmask or ip/netmask>
     see the Examples section below
DESCRIPTION
     Whatmask is a small C program that will help you with network settings.
     Whatmask can work in two modes.  The first mode is to invoke Whatmask with
     only  a  subnet mask as the argument. In this mode Whatmask will echo back
     the subnet mask in four formats, plus the number of useable  addresses  in
     the range.
     Netmask Notations supported:
      Name                  Example
      CIDR                         /24
      Netmask            255.255.255.0
      Netmask (hex)         0xffffff00
      Wildcard Bits           0.0.0.255
     The  above  notations are all identical.  CIDR notation commonly has a "/"
     in front of the number (representing the number of  bits).   Whatmask  can
     accept these notations with or without a slash. This notation is used more
     and  more recently. A lot of popular routers and software support this no-
     tation.
     Netmask notation is pretty much the standard old-school way of  doing  it.
     It is supported by most systems (Un*x, Win, Mac, etc.).
     Netmask  (Hex)  is the hexadecimal representation of the netmask. Many im-
     plementations of ifconfig use this notation
     Wildcard Bits are similar to the netmask, but they are the logical not  of
     the netmask. This notation is used by a number of popular routers (and no-
     body knows why...).
     To  use  Whatmask  in the first mode simply type "whatmask <notation>" The
     notation can be in any of the four formats and Whatmask will automagically
     figure out what it is and display all four notations.
     To use Whatmask in its second mode execute Whatmask with  any  ip  address
     within  the subnet, followed by a slash ('/'), followed by the subnet mask
     in any format. (e.g. 192.168.0.23/255.255.255.224, or 192.168.0.23/27) Put
     no spaces in the argument.
     Whatmask will echo back the following:
     - The netmask in the following formats: CIDR, Netmask, Netmask (Hex),
     Wildcard Bits
     - The Network Address
     - The Broadcast Address
     - The number of Usable IP Addresses
     - The First Usable IP Address
     - The Last Usable IP Address
            (Whatmask assumes that the Broadcast address is the highest address
            in the subnet. This is the most common configuration.)
OPTIONS
     <no options> see above and below for usage.
EXAMPLES
     Examples of how Whatmask works:
          myhost> whatmask /26
          ---------------------------------------------
                  TCP/IP SUBNET MASK EQUIVALENTS
          ---------------------------------------------
          CIDR = .....................: /26
          Netmask = ..................: 255.255.255.192
          Netmask (hex) = ............: 0xffffffc0
          Wildcard Bits = ............: 0.0.0.63
          Usable IP Addresses = ......: 62
          myhost> whatmask 255.255.192.0
          ---------------------------------------------
                  TCP/IP SUBNET MASK EQUIVALENTS
          ---------------------------------------------
          CIDR = .....................: /18
          Netmask = ..................: 255.255.192.0
          Netmask (hex) = ............: 0xffffc000
          Wildcard Bits = ............: 0.0.63.255
          Usable IP Addresses = ......: 16,382
          myhost> whatmask 0xffffffe0
          ---------------------------------------------
                  TCP/IP SUBNET MASK EQUIVALENTS
          ---------------------------------------------
          CIDR = .....................: /27
          Netmask = ..................: 255.255.255.224
          Netmask (hex) = ............: 0xffffffe0
          Wildcard Bits = ............: 0.0.0.31
          Usable IP Addresses = ......: 30
          myhost> whatmask 0.0.0.31
          ---------------------------------------------
                  TCP/IP SUBNET MASK EQUIVALENTS
          ---------------------------------------------
          CIDR = .....................: /27
          Netmask = ..................: 255.255.255.224
          Netmask (hex) = ............: 0xffffffe0
          Wildcard Bits = ............: 0.0.0.31
          Usable IP Addresses = ......: 30
          myhost> whatmask 192.168.165.23/19
          ------------------------------------------------
                       TCP/IP NETWORK INFORMATION
          ------------------------------------------------
          IP Entered = ..................: 192.168.165.23
          CIDR = ........................: /19
          Netmask = .....................: 255.255.224.0
          Netmask (hex) = ...............: 0xffffe000
          Wildcard Bits = ...............: 0.0.31.255
          ------------------------------------------------
          Network Address = .............: 192.168.160.0
          Broadcast Address = ...........: 192.168.191.255
          Usable IP Addresses = .........: 8,190
          First Usable IP Address = .....: 192.168.160.1
          Last Usable IP Address = ......: 192.168.191.254
          myhost> whatmask 192.168.0.13/255.255.255.0
          ------------------------------------------------
                       TCP/IP NETWORK INFORMATION
          ------------------------------------------------
          IP Entered = ..................: 192.168.0.13
          CIDR = ........................: /24
          Netmask = .....................: 255.255.255.0
          Netmask (hex) = ...............: 0xffffff00
          Wildcard Bits = ...............: 0.0.0.255
          ------------------------------------------------
          Network Address = .............: 192.168.0.0
          Broadcast Address = ...........: 192.168.0.255
          Usable IP Addresses = .........: 254
          First Usable IP Address = .....: 192.168.0.1
          Last Usable IP Address = ......: 192.168.0.254
          myhost> whatmask 192.168.0.113/0xffffffe0
          ------------------------------------------------
                       TCP/IP NETWORK INFORMATION
          ------------------------------------------------
          IP Entered = ..................: 192.168.0.113
          CIDR = ........................: /27
          Netmask = .....................: 255.255.255.224
          Netmask (hex) = ...............: 0xffffffe0
          Wildcard Bits = ...............: 0.0.0.31
          ------------------------------------------------
          Network Address = .............: 192.168.0.96
          Broadcast Address = ...........: 192.168.0.127
          Usable IP Addresses = .........: 30
          First Usable IP Address = .....: 192.168.0.97
          Last Usable IP Address = ......: 192.168.0.126
          myhost> whatmask 192.168.0.169/0.0.0.127
          ------------------------------------------------
                       TCP/IP NETWORK INFORMATION
          ------------------------------------------------
          IP Entered = ..................: 192.168.0.169
          CIDR = ........................: /25
          Netmask = .....................: 255.255.255.128
          Netmask (hex) = ...............: 0xffffff80
          Wildcard Bits = ...............: 0.0.0.127
          ------------------------------------------------
          Network Address = .............: 192.168.0.128
          Broadcast Address = ...........: 192.168.0.255
          Usable IP Addresses = .........: 126
          First Usable IP Address = .....: 192.168.0.129
          Last Usable IP Address = ......: 192.168.0.254
BUGS
     Report bugs to <
[email protected]
>
CONTRIBUTORS
     Original code:
            Joe Laffey <
[email protected]
>
     Assistance with Manpage and Packaging:
            David Wirch <
[email protected]
>
     Many thanks to the beta testers and users who sent in valuable feedback!
UPDATES
     Official Whatmask website:
            http://www.laffeycomputer.com/whatmask.html
LAFFEY Computer Imaging           Nov 14, 2003                      Whatmask(1)
Updated on: 2026-May-25
 Edit this page
websploit
whatweb
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install whatmask`，再执行 `whatmask --version` 2>/dev/null || `whatmask -V`
- [ ] **2.** **读官方帮助** —— `whatmask -h`，需要细节时 `man whatmask`
- [ ] **3.** **在自有靶场跑最小用例** —— 用 `whatmask -h` 里最简单的那个子命令试一次
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/whatmask/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/whatmask/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/whatmask/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
