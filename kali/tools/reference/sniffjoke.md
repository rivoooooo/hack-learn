# sniffjoke

> Transparent TCP connection scrambler SniffJoke is an application for Linux that handle transparently your TCP connection, delaying, modifyng and inject fake packets inside your transmission, make them almost impossible to be correctly read…

> **功能分类**：嗅探与欺骗 ｜ **Kali 包**：`sniffjoke` ｜ **官方文档**：<https://www.kali.org/tools/sniffjoke/>

## 1. 安装

```bash
sudo apt update
sudo apt install sniffjoke
```

| 项目 | 内容 |
|------|------|
| 版本 | 0.4.1 |
| 架构 | any |
| 可执行命令 | `sniffjoke`、`sj-commit-results`、`sj-iptcpopt-probe`、`sniffjoke-autotest`、`sniffjokectl` |
| 依赖 | `iptables`、`libc6`、`libgcc-s1`、`libstdc++6`、`tcpdump`、`sj-commit-results` |
| 安装体积 | 518 KB |
| 官网 | <https://github.com/vecna/sniffjoke> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/sniffjoke> |
| 包追踪 | <https://pkg.kali.org/pkg/sniffjoke> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
sniffjoke -h          # 查看用法
man sniffjoke         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 5 个可执行命令，下面是官方页面内嵌的帮助原文。

### `sj-commit-results`

官方给出的调用示例：`sj-commit-results -h`

```text
root@kali:~# sj-commit-results -h
usage: /usr/bin/sj-commit-results options
This script is part of SniffJoke autotest
USUALLY - an user has not any needings in use this script
OPTIONS:
   -l      target location to send remotely
   -u      URL which commit to
           (both required)
```

### `sj-iptcpopt-probe`

官方给出的调用示例：`sj-iptcpopt-probe -h`

```text
root@kali:~# sj-iptcpopt-probe -h
usage: /usr/bin/sj-iptcpopt-probe options
This script is part of SniffJoke autotest
This script is invoked by sniffjoke-autotest and try the possibile
combination of IP/TCP header options for the testing 'location'
Is required a detailed test because different ISP will handle
differently these options, considering a packet acceptable or not
by internal policy, router configuration and updating frequency
by hand this script should accept these argument:
OPTIONS:
   -h      show this message
   -w      working directory                                   (required)
            (eg: /tmp/home/, where sniffjoke-autotest is running)
   -u      testing URL                                         (required)
   -n      username to downgrade privileges
   -g      group to downgrade privileges
   -i      server IPv4 format 000.000.000.000                  (required)
```

### `sniffjoke`

官方给出的调用示例：`sniffjoke -h`

```text
root@kali:~# sniffjoke -h
Usage: sniffjoke [OPTION]... :
 --location <name>	specify the network environment (suggested) [default: generic]
 --dir <name>		specify the base directory where the location reside [default: /usr/local/var/sniffjoke/]
			[using both location and dir defaults, the configuration status will not be saved]
 --user <username>	downgrade priviledge to the specified user [default: nobody]
 --group <groupname>	downgrade priviledge to the specified group [default: nogroup]
 --no-tcp		disable tcp mangling [default: tcp mangled]
 --no-udp		disable udp mangling [default: udp mangled]
 --whitelist		inject evasion packets only in the specified ip addresses
 --blacklist		inject evasion packet in all session excluding the blacklisted ip address
 --start		if present, evasion i'ts activated immediatly [default: not present]
 --chain		enable chained hacking, powerful and entropic effects [default: disabled]
 --debug <level 0-5>	set verbosity level [default: 2]
			0: suppress log, 1: common, 2: verbose, 3: debug, 4: session 5: packets
 --foreground		running in foreground [default:background]
 --admin <ip>[:port]	specify administration IP address [default: 127.0.0.1:8844]
 --force		force restart (usable when another sniffjoke service is running)
 --gw-mac-addr		specify default gateway mac address [default: is autodetected]
 --version		show sniffjoke version
 --help			show this help
			http://www.delirandom.net/sniffjoke
```

### `sniffjoke-autotest`

官方给出的调用示例：`sniffjoke-autotest -h`

```text
root@kali:~# sniffjoke-autotest -h
usage: /usr/bin/sniffjoke-autotest options
  This script runs plugins test along different destinations OS to determinate the
selection of plugins and options that correctly works in the current location.
  Every workplace (office, home, freewifi) you use, neet to be setup as location.
  Having a location correctly configurated IS THE ONLY WAY to have SniffJoke working;
  technical details will be found in:
http://www.delirandom.net/sniffjoke/sniffjoke-locations
OPTIONS:
   -h      show this message
   -l      location name                                       (required)
   -n      number of replicas to be passed for the single hack (default 1)
   -g      specify the group to privilege downgrade            (default: nogroup)
   -u      specify the user to privilege downgrade             (default: nobody)
```

### `sniffjokectl`

官方给出的调用示例：`sniffjokectl -h`

```text
root@kali:~# sniffjokectl -h
Usage: sniffjokectl [OPTIONS]... [COMMANDS]...
 --address <ip>[:port]	specify administration IP address [default: 127.0.0.1:8844]
 --version		show sniffjoke version
 --timeout		set milliseconds timeout when contacting SniffJoke service [default: 500]
 --help			show this help
when sniffjoke is running, you should send commands with a command line argument:
 start			start sniffjoke hijacking/injection
 stop			pause sniffjoke
 quit			quit sniffjoke
 saveconf		dump configuration file
 stat			get statistics about sniffjoke configuration and network
 info			get statistics about sniffjoke active sessions
 ttlmap			show the mapped hop count for destination
 showport		show the running port-aggressivity configuration
 set start:end value	set the injection's strogness over selected port [not supported!]
		need to be set in port-aggressivity.conf
 debug			[0-5] change the log debug level
			http://www.delirandom.net/sniffjoke
Updated on: 2025-Dec-09
 Edit this page
smtp-user-enum
snmpcheck
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install sniffjoke`，再执行 `sniffjoke --version` 2>/dev/null || `sniffjoke -V`
- [ ] **2.** **读官方帮助** —— `sniffjoke -h`，需要细节时 `man sniffjoke`
- [ ] **3.** **在自有靶场跑最小用例** —— 官方给出的调用形式是：`Usage: sniffjoke [OPTION]... :`
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/sniffjoke/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/defense-evasion.md`](../../tools/by-attack/defense-evasion.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/sniffjoke/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/sniffjoke/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
