# ettercap

> Multipurpose sniffer/content filter for man in the middle attacks root@kali:~# ettercap -h ettercap 0.8.4.1 copyright 2001-2026 Ettercap Development Team Usage: ettercap [OPTIONS] [TARGET1] [TARGET2] TARGET is in the format MAC/IP/IPv6/POR…

> **功能分类**：漏洞利用 ｜ **Kali 包**：`ettercap` ｜ **官方文档**：<https://www.kali.org/tools/ettercap/>

## 1. 安装

```bash
sudo apt update
sudo apt install ettercap-text-only
```

| 项目 | 内容 |
|------|------|
| 版本 | 0.8.4.1 |
| 架构 | any |
| 可执行命令 | `ettercap-common`、`ettercap-graphical`、`ettercap`、`ettercap-pkexec`、`etterfilter`、`etterlog`、`ettercap-text-only` |
| 依赖 | `ettercap-common`、`libc6`、`libncurses6`、`libpcre2-8-0`、`libtinfo6`、`zlib1g` |
| 安装体积 | 308 KB |
| 官网 | <https://ettercap.github.io/ettercap/> |
| 源码仓库 | <https://salsa.debian.org/pkg-security-team/ettercap> |
| 包追踪 | <https://pkg.kali.org/pkg/ettercap> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
ettercap-common -h          # 查看用法
man ettercap-common         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 7 个可执行命令，下面是官方页面内嵌的帮助原文。

### `ettercap`

官方给出的调用示例：`ettercap -h`

```text
root@kali:~# ettercap -h
ettercap 0.8.4.1 copyright 2001-2026 Ettercap Development Team
Usage: ettercap [OPTIONS] [TARGET1] [TARGET2]
TARGET is in the format MAC/IP/IPv6/PORTs (see the man for further detail)
Sniffing and Attack options:
  -M, --mitm <METHOD:ARGS>    perform a mitm attack
  -o, --only-mitm             don't sniff, only perform the mitm attack
  -b, --broadcast             sniff packets destined to broadcast
  -B, --bridge <IFACE>        use bridged sniff (needs 2 ifaces)
  -p, --nopromisc             do not put the iface in promisc mode
  -S, --nosslmitm             do not forge SSL certificates
  -u, --unoffensive           do not forward packets
  -r, --read <file>           read data from pcapfile <file>
  -f, --pcapfilter <string>   set the pcap filter <string>
  -R, --reversed              use reversed TARGET matching
  -t, --proto <proto>         sniff only this proto (default is all)
      --certificate <file>    certificate file to use for SSL MiTM
      --private-key <file>    private key file to use for SSL MiTM
User Interface Type:
  -T, --text                  use text only GUI
       -q, --quiet                 do not display packet contents
       -s, --script <CMD>          issue these commands to the GUI
  -C, --curses                use curses GUI
  -D, --daemon                daemonize ettercap (no GUI)
  -G, --gtk                   use GTK+ GUI
Logging options:
  -w, --write <file>          write sniffed data to pcapfile <file>
  -L, --log <logfile>         log all the traffic to this <logfile>
  -l, --log-info <logfile>    log only passive infos to this <logfile>
  -m, --log-msg <logfile>     log all the messages to this <logfile>
  -c, --compress              use gzip compression on log files
Visualization options:
  -d, --dns                   resolves ip addresses into hostnames
  -V, --visual <format>       set the visualization format
  -e, --regex <regex>         visualize only packets matching this regex
  -E, --ext-headers           print extended header for every pck
  -Q, --superquiet            do not display user and password
LUA options:
      --lua-script <script1>,[<script2>,...]     comma-separted list of LUA scripts
      --lua-args n1=v1,[n2=v2,...]               comma-separated arguments to LUA script(s)
General options:
  -i, --iface <iface>         use this network interface
  -I, --liface                show all the network interfaces
  -Y, --secondary <ifaces>    list of secondary network interfaces
  -n, --netmask <netmask>     force this <netmask> on iface
  -A, --address <address>     force this local <address> on iface
  -P, --plugin <plugin>       launch this <plugin> - multiple occurance allowed
      --plugin-list <plugin1>,[<plugin2>,...]       comma-separated list of plugins
  -F, --filter <file>         load the filter <file> (content filter)
  -z, --silent                do not perform the initial ARP scan
  -6, --ip6scan               send ICMPv6 probes to discover IPv6 nodes on the link
  -j, --load-hosts <file>     load the hosts list from <file>
  -k, --save-hosts <file>     save the hosts list to <file>
  -W, --wifi-key <wkey>       use this key to decrypt wifi packets (wep or wpa)
  -a, --config <config>       use the alternative config file <config>
Standard options:
  -v, --version               prints the version and exit
  -h, --help                  this help screen
```

### `man`

官方给出的调用示例：`man ettercap-pkexec`

```text
root@kali:~# man ettercap-pkexec
ETTERCAP(8)                 System Manager's Manual                 ETTERCAP(8)
NAME
     ettercap-pkexec - graphical pkexec-based launcher for ettercap
     This  launcher depends on policykit-1 and the menu packages, and basically
     wraps the ettercap binary command
     with a pkexec action script  usually  defined  on  /usr/share/polkit-1/ac-
     tions/org.pkexec.ettercap.policy,
     allowing users to directly call ettercap from the desktop or menu launcher
     with root privileges.
     The commands available are exactly the same as the ettercap man page.
     Please refer to man ettercap for the list of available parameters.
     (don't  forget  to  change  "ettercap" to "ettercap-pkexec" as caller pro-
     gram).
     example:
     ettercap-pkexec -G will start ettercap with root privileges and  the  GTK2
     interface.
AUTHOR
     This  code  was  originally taken from arch distro, and refactored to work
     with cmake system by
     Gianfranco Costamagna (LocutusOfBorg) <
[email protected]
>
ORIGINAL AUTHORS
     Alberto Ornaghi (ALoR) <
[email protected]
>
     Marco Valleri (NaGA) <
[email protected]
>
PROJECT STEWARDS
     Emilio Escobar (exfil)  <
[email protected]
>
     Eric Milam (Brav0Hax)  <
[email protected]
>
OFFICIAL DEVELOPERS
     Mike Ryan (justfalter)  <
[email protected]
>
     Gianfranco Costamagna (LocutusOfBorg)  <
[email protected]
>
     Antonio Collarino (sniper)  <
[email protected]
>
     Ryan Linn   <
[email protected]
>
     Jacob Baines   <
[email protected]
>
CONTRIBUTORS
     Dhiru Kholia (kholia)  <
[email protected]
>
     Alexander Koeppe (koeppea)  <
[email protected]
>
     Martin Bos (PureHate)  <
[email protected]
>
     Enrique Sanchez
     Gisle Vanem  <
[email protected]
>
     Johannes Bauer  <
[email protected]
>
     Daten (Bryan Schneiders)  <
[email protected]
>
SEE ALSO
     etter.conf(5) ettercap_curses(8) ettercap_plugins(8) etterlog(8) etterfil-
     ter(8)
AVAILABILITY
     https://github.com/Ettercap/ettercap/downloads
GIT
     git clone git://github.com/Ettercap/ettercap.git
     or
     git clone https://github.com/Ettercap/ettercap.git
BUGS
     Our software never has bugs.
     It just develops random features.   ;)
     KNOWN-BUGS
     - ettercap doesn't handle fragmented packets...  only  the  first  segment
     will  be displayed by the sniffer. However all the fragments are correctly
     forwarded.
     + please send bug-report, patches or  suggestions  to  <ettercap-betatest-
[email protected]
>   or  visit  https://github.com/Ettercap/etter-
     cap/issues.
     + to report a bug, follow the instructions in the README.BUGS file
PHILOLOGICAL HISTORY
     "Even if blessed with a feeble intelligence, they are cruel and  smart..."
     this  is  the  description of Ettercap, a monster of the RPG Advanced Dun-
     geons & Dragon.
     The name "ettercap" was chosen because it has an assonance with "ethercap"
     which means "ethernet capture" (what ettercap actually does) and also  be-
     cause  such  monsters  have a powerful poison... and you know, arp poison-
     ing... ;)
The Lord Of The (Token)Ring
     (the fellowship of the packet)
     "One Ring to link them all, One Ring to ping them,
      one Ring to bring them all and in the darkness sniff them."
Last words
     "Programming today is a race between software engineers striving to  build
     bigger and better idiot-proof programs, and the Universe trying to produce
     bigger and better idiots. So far, the Universe is winning." - Rich Cook
ettercap 0.8.4.1                                                    ETTERCAP(8)
```

### `etterfilter`

官方给出的调用示例：`etterfilter -h`

```text
root@kali:~# etterfilter -h
Usage: etterfilter [OPTIONS] filterfile
General Options:
  -o, --output <file>         output file (default is filter.ef)
  -t, --test <file>           test the file (debug mode)
  -d, --debug                 print some debug info while compiling
  -w, --suppress-warnings     ignore warnings during compilation
Standard Options:
  -v, --version               prints the version and exit
  -h, --help                  this help screen
etterfilter 0.8.4.1 copyright 2001-2026 Ettercap Development Team
```

### `etterlog`

官方给出的调用示例：`etterlog -h`

```text
root@kali:~# etterlog -h
Usage: etterlog [OPTIONS] logfile
General Options:
  -a, --analyze               analyze a log file and return useful infos
  -c, --connections           display the table of connections
  -f, --filter <TARGET>       print packets only from this target
  -t, --proto <proto>         display only this proto (default is all)
  -F, --filcon <CONN>         print packets only from this connection
  -s, --only-source           print packets only from the source
  -d, --only-dest             print packets only from the destination
  -r, --reverse               reverse the target/connection matching
  -n, --no-headers            skip header information between packets
  -m, --show-mac              show mac addresses in the headers
  -k, --color                 colorize the output
  -l, --only-local            show only local hosts parsing info files
  -L, --only-remote           show only remote hosts parsing info files
Search Options:
  -e, --regex <regex>         display only packets that match the regex
  -u, --user <user>           search for info about the user <user>
  -p, --passwords             print only accounts information
  -i, --show-client           show client address in the password profiles
  -I, --client <ip>           search for pass from a specific client
Editing Options:
  -C, --concat                concatenate more files into one single file
  -o, --outfile <file>        the file used as output for concatenation
  -D, --decode                used to extract files from connections
Visualization Method:
  -B, --binary                print packets as they are
  -X, --hex                   print packets in hex mode
  -A, --ascii                 print packets in ascii mode (default)
  -T, --text                  print packets in text mode
  -E, --ebcdic                print packets in ebcdic mode
  -H, --html                  print packets in html mode
  -U, --utf8 <encoding>       print packets in uft-8 using the <encoding>
  -Z, --zero                  do not print packets, only headers
  -x, --xml                   print host infos in xml format
Standard Options:
  -v, --version               prints the version and exit
  -h, --help                  this help screen
etterlog 0.8.4.1 copyright 2001-2026 Ettercap Development Team
```

### `ettercap（示例）`

官方给出的调用示例：`ettercap -h`

```text
root@kali:~# ettercap -h
ettercap 0.8.4.1 copyright 2001-2026 Ettercap Development Team
Usage: ettercap [OPTIONS] [TARGET1] [TARGET2]
TARGET is in the format MAC/IP/IPv6/PORTs (see the man for further detail)
Sniffing and Attack options:
  -M, --mitm <METHOD:ARGS>    perform a mitm attack
  -o, --only-mitm             don't sniff, only perform the mitm attack
  -b, --broadcast             sniff packets destined to broadcast
  -B, --bridge <IFACE>        use bridged sniff (needs 2 ifaces)
  -p, --nopromisc             do not put the iface in promisc mode
  -S, --nosslmitm             do not forge SSL certificates
  -u, --unoffensive           do not forward packets
  -r, --read <file>           read data from pcapfile <file>
  -f, --pcapfilter <string>   set the pcap filter <string>
  -R, --reversed              use reversed TARGET matching
  -t, --proto <proto>         sniff only this proto (default is all)
      --certificate <file>    certificate file to use for SSL MiTM
      --private-key <file>    private key file to use for SSL MiTM
User Interface Type:
  -T, --text                  use text only GUI
       -q, --quiet                 do not display packet contents
       -s, --script <CMD>          issue these commands to the GUI
  -C, --curses                use curses GUI
  -D, --daemon                daemonize ettercap (no GUI)
  -G, --gtk                   use GTK+ GUI
Logging options:
  -w, --write <file>          write sniffed data to pcapfile <file>
  -L, --log <logfile>         log all the traffic to this <logfile>
  -l, --log-info <logfile>    log only passive infos to this <logfile>
  -m, --log-msg <logfile>     log all the messages to this <logfile>
  -c, --compress              use gzip compression on log files
Visualization options:
  -d, --dns                   resolves ip addresses into hostnames
  -V, --visual <format>       set the visualization format
  -e, --regex <regex>         visualize only packets matching this regex
  -E, --ext-headers           print extended header for every pck
  -Q, --superquiet            do not display user and password
LUA options:
      --lua-script <script1>,[<script2>,...]     comma-separted list of LUA scripts
      --lua-args n1=v1,[n2=v2,...]               comma-separated arguments to LUA script(s)
General options:
  -i, --iface <iface>         use this network interface
  -I, --liface                show all the network interfaces
  -Y, --secondary <ifaces>    list of secondary network interfaces
  -n, --netmask <netmask>     force this <netmask> on iface
  -A, --address <address>     force this local <address> on iface
  -P, --plugin <plugin>       launch this <plugin> - multiple occurance allowed
      --plugin-list <plugin1>,[<plugin2>,...]       comma-separated list of plugins
  -F, --filter <file>         load the filter <file> (content filter)
  -z, --silent                do not perform the initial ARP scan
  -6, --ip6scan               send ICMPv6 probes to discover IPv6 nodes on the link
  -j, --load-hosts <file>     load the hosts list from <file>
  -k, --save-hosts <file>     save the hosts list to <file>
  -W, --wifi-key <wkey>       use this key to decrypt wifi packets (wep or wpa)
  -a, --config <config>       use the alternative config file <config>
Standard options:
  -v, --version               prints the version and exit
  -h, --help                  this help screen
```

### `etterfilter（示例）`

官方给出的调用示例：`etterfilter -h`

```text
root@kali:~# etterfilter -h
Usage: etterfilter [OPTIONS] filterfile
General Options:
  -o, --output <file>         output file (default is filter.ef)
  -t, --test <file>           test the file (debug mode)
  -d, --debug                 print some debug info while compiling
  -w, --suppress-warnings     ignore warnings during compilation
Standard Options:
  -v, --version               prints the version and exit
  -h, --help                  this help screen
etterfilter 0.8.4.1 copyright 2001-2026 Ettercap Development Team
```

### `etterlog（示例）`

官方给出的调用示例：`etterlog -h`

```text
root@kali:~# etterlog -h
Usage: etterlog [OPTIONS] logfile
General Options:
  -a, --analyze               analyze a log file and return useful infos
  -c, --connections           display the table of connections
  -f, --filter <TARGET>       print packets only from this target
  -t, --proto <proto>         display only this proto (default is all)
  -F, --filcon <CONN>         print packets only from this connection
  -s, --only-source           print packets only from the source
  -d, --only-dest             print packets only from the destination
  -r, --reverse               reverse the target/connection matching
  -n, --no-headers            skip header information between packets
  -m, --show-mac              show mac addresses in the headers
  -k, --color                 colorize the output
  -l, --only-local            show only local hosts parsing info files
  -L, --only-remote           show only remote hosts parsing info files
Search Options:
  -e, --regex <regex>         display only packets that match the regex
  -u, --user <user>           search for info about the user <user>
  -p, --passwords             print only accounts information
  -i, --show-client           show client address in the password profiles
  -I, --client <ip>           search for pass from a specific client
Editing Options:
  -C, --concat                concatenate more files into one single file
  -o, --outfile <file>        the file used as output for concatenation
  -D, --decode                used to extract files from connections
Visualization Method:
  -B, --binary                print packets as they are
  -X, --hex                   print packets in hex mode
  -A, --ascii                 print packets in ascii mode (default)
  -T, --text                  print packets in text mode
  -E, --ebcdic                print packets in ebcdic mode
  -H, --html                  print packets in html mode
  -U, --utf8 <encoding>       print packets in uft-8 using the <encoding>
  -Z, --zero                  do not print packets, only headers
  -x, --xml                   print host infos in xml format
Standard Options:
  -v, --version               prints the version and exit
  -h, --help                  this help screen
etterlog 0.8.4.1 copyright 2001-2026 Ettercap Development Team
Updated on: 2026-May-25
 Edit this page
edb-debugger
evil-winrm-py
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install ettercap-text-only`，再执行 `ettercap-common --version` 2>/dev/null || `ettercap-common -V`
- [ ] **2.** **读官方帮助** —— `ettercap-common -h`，需要细节时 `man ettercap-common`
- [ ] **3.** **在自有靶场跑最小用例** —— 官方给出的调用形式是：`Usage: ettercap [OPTIONS] [TARGET1] [TARGET2]`
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/ettercap/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- **精讲教程**（含原理、参数详解、靶场实操与输出解读）：[ettercap](../../tools/tutorials/07-嗅探与欺骗/ettercap.md)
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/collection.md`](../../tools/by-attack/collection.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/ettercap/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/ettercap/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
