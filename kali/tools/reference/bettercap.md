# bettercap

> Complete, modular, portable and easily extensible MITM framework The Swiss Army knife for 802.11, BLE, IPv4 and IPv6 networks reconnaissance and MITM attacks. bettercap is a powerful, easily extensible and portable framework written in Go …

> **功能分类**：嗅探与欺骗 ｜ **Kali 包**：`bettercap` ｜ **官方文档**：<https://www.kali.org/tools/bettercap/>

## 1. 安装

```bash
sudo apt update
sudo apt install bettercap
```

| 项目 | 内容 |
|------|------|
| 版本 | 2.41.5 |
| 架构 | any |
| 可执行命令 | `bettercap` |
| 依赖 | `ca-certificates`、`iproute2`、`iptables`、`iw`、`libc6`、`libpcap0.8t64`、`libusb-1.0-0`、`net-tools` |
| 安装体积 | 63.14 MB |
| 官网 | <https://www.bettercap.org> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/bettercap> |
| 包追踪 | <https://pkg.kali.org/pkg/bettercap> |

## 2. 官方用法示例

> 以下为 Kali 官方工具页给出的示例与输出原文。

```text
Usage Example
Scan the system in quiet mode (-Q) and output in cronjob format (–cronjob):
root@kali:~# bettercap
bettercap v2.11 (type 'help' for a list of commands)

172.16.10.0/24 > 172.16.10.212  » [12:34:15] [endpoint.new] endpoint 172.16.10.254 detected as 00:50:56:01:33:70 (VMware, Inc.).
172.16.10.0/24 > 172.16.10.212  » help

           help MODULE : List available commands or show module specific help if no module name is provided.
                active : Show information about active modules.
                  quit : Close the session and exit.
         sleep SECONDS : Sleep for the given amount of seconds.
              get NAME : Get the value of variable NAME, use * alone for all, or NAME* as a wildcard.
        set NAME VALUE : Set the VALUE of variable NAME.
  read VARIABLE PROMPT : Show a PROMPT to ask the user for input that will be saved inside VARIABLE.
                 clear : Clear the screen.
        include CAPLET : Load and run this caplet in the current session.
             ! COMMAND : Execute a shell command and print its output.
        alias MAC NAME : Assign an alias to a given endpoint given its MAC address.

Modules

      any.proxy > not running
       api.rest > not running
      arp.spoof > not running
      ble.recon > not running
        caplets > not running
    dhcp6.spoof > not running
      dns.spoof > not running
  events.stream > running
            gps > not running
     http.proxy > not running
    http.server > not running
    https.proxy > not running
    mac.changer > not running
   mysql.server > not running
      net.probe > not running
      net.recon > running
      net.sniff > not running
   packet.proxy > not running
       syn.scan > not running
      tcp.proxy > not running
         ticker > not running
         update > not running
           wifi > not running
            wol > not running

172.16.10.0/24 > 172.16.10.212  » net.show

+-----------------+--------------------+----------+-------------------------+---------+---------+------------+
|       IP        |        MAC         |  Name    |         Vendor          | Sent    | Recvd  | Last Seen  |
+-----------------+--------------------+----------+-------------------------+---------+---------+------------+
| 172.16.10.212   | 00:b0:52:af:4a:50  | eth0     | Atheros Communications  | 0 B     | 0 B     | 12:34:15   |
| 172.16.10.2     | 00:50:56:13:37:0a  | gateway  | VMware, Inc.            | 49 kB   | 20 kB   | 12:34:15   |
|                 |                    |          |                         |         |         |            |
| 172.16.10.254   | 00:50:56:01:33:70  |          | VMware, Inc.            | 2.4 kB  | 2.4 kB  | 12:35:15   |
+-----------------+--------------------+----------+-------------------------+---------+---------+------------+

↑ 0 B / ↓ 3.2 MB / 11354 pkts / 0 errs
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `bettercap`

```text
root@kali:~# bettercap
bettercap v2.11 (type 'help' for a list of commands)
172.16.10.0/24 > 172.16.10.212  » [12:34:15] [endpoint.new] endpoint 172.16.10.254 detected as 00:50:56:01:33:70 (VMware, Inc.).
172.16.10.0/24 > 172.16.10.212  » help
           help MODULE : List available commands or show module specific help if no module name is provided.
                active : Show information about active modules.
                  quit : Close the session and exit.
         sleep SECONDS : Sleep for the given amount of seconds.
              get NAME : Get the value of variable NAME, use * alone for all, or NAME* as a wildcard.
        set NAME VALUE : Set the VALUE of variable NAME.
  read VARIABLE PROMPT : Show a PROMPT to ask the user for input that will be saved inside VARIABLE.
                 clear : Clear the screen.
        include CAPLET : Load and run this caplet in the current session.
             ! COMMAND : Execute a shell command and print its output.
        alias MAC NAME : Assign an alias to a given endpoint given its MAC address.
Modules
      any.proxy > not running
       api.rest > not running
      arp.spoof > not running
      ble.recon > not running
        caplets > not running
    dhcp6.spoof > not running
      dns.spoof > not running
  events.stream > running
            gps > not running
     http.proxy > not running
    http.server > not running
    https.proxy > not running
    mac.changer > not running
   mysql.server > not running
      net.probe > not running
      net.recon > running
      net.sniff > not running
   packet.proxy > not running
       syn.scan > not running
      tcp.proxy > not running
         ticker > not running
         update > not running
           wifi > not running
            wol > not running
172.16.10.0/24 > 172.16.10.212  » net.show
+-----------------+--------------------+----------+-------------------------+---------+---------+------------+
|       IP        |        MAC         |  Name    |         Vendor          | Sent    | Recvd  | Last Seen  |
+-----------------+--------------------+----------+-------------------------+---------+---------+------------+
| 172.16.10.212   | 00:b0:52:af:4a:50  | eth0     | Atheros Communications  | 0 B     | 0 B     | 12:34:15   |
| 172.16.10.2     | 00:50:56:13:37:0a  | gateway  | VMware, Inc.            | 49 kB   | 20 kB   | 12:34:15   |
|                 |                    |          |                         |         |         |            |
| 172.16.10.254   | 00:50:56:01:33:70  |          | VMware, Inc.            | 2.4 kB  | 2.4 kB  | 12:35:15   |
+-----------------+--------------------+----------+-------------------------+---------+---------+------------+
↑ 0 B / ↓ 3.2 MB / 11354 pkts / 0 errs
```

### `bettercap -h`

> 官方示例调用：`bettercap -h`

```text
root@kali:~# bettercap -h
Usage of bettercap:
  -autostart string
    	Comma separated list of modules to auto start. (default "events.stream")
  -caplet string
    	Read commands from this file and execute them in the interactive session.
  -caplets-path string
    	Specify an alternative base path for caplets.
  -cpu-profile file
    	Write cpu profile file.
  -debug
    	Print debug messages.
  -env-file string
    	Load environment variables from this file if found, set to empty to disable environment persistence.
  -eval string
    	Run one or more commands separated by ; in the interactive session, used to set variables via command line.
  -gateway-override string
    	Use the provided IP address instead of the default gateway. If not specified or invalid, the default gateway will be used.
  -iface string
    	Network interface to bind to, if empty the default interface will be auto selected.
  -mem-profile file
    	Write memory profile to file.
  -no-colors
    	Disable output color effects.
  -no-history
    	Disable interactive session history file.
  -pcap-buf-size int
    	PCAP buffer size, leave to 0 for the default value. (default -1)
  -script string
    	Load a session script.
  -silent
    	Suppress all logs which are not errors.
  -version
    	Print the version and exit.
Learn more with
OffSec
Want to learn more about bettercap? get access to in-depth training and hands-on labs:
PEN-210: 12.1. Installation and Executing
PEN-210 course
Updated on: 2026-Mar-02
 Edit this page
bed
blueranger
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install bettercap`，再执行 `bettercap --version` 2>/dev/null || `bettercap -V`
- [ ] **2.** **读官方帮助** —— `bettercap -h`，需要细节时 `man bettercap`
- [ ] **3.** **在自有靶场跑最小用例** —— 官方给出的调用形式是：`Usage of bettercap:`
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/bettercap/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- **精讲教程**（含原理、参数详解、靶场实操与输出解读）：[bettercap](../../tools/tutorials/05-无线攻击/bettercap.md)
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/reconnaissance.md`](../../tools/by-attack/reconnaissance.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/bettercap/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/bettercap/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
