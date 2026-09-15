# iodine

> Tool for tunneling IPv4 data through a DNS server This is a piece of software that lets you tunnel IPv4 data through a DNS server. This can be usable in different situations where internet access is firewalled, but DNS queries are allowed.

> **功能分类**：后渗透 ｜ **Kali 包**：`iodine` ｜ **官方文档**：<https://www.kali.org/tools/iodine/>

## 1. 安装

```bash
sudo apt update
sudo apt install iodine
```

| 项目 | 内容 |
|------|------|
| 版本 | 0.7.0 |
| 架构 | any |
| 可执行命令 | `iodine`、`iodine-client-start`、`iodined` |
| 依赖 | `adduser` |
| 安装体积 | 245 KB |
| 官网 | <https://code.kryo.se/iodine> |
| 源码仓库 | <https://salsa.debian.org/debian/iodine> |
| 包追踪 | <https://pkg.kali.org/pkg/iodine> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
iodine -h          # 查看用法
man iodine         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 3 个可执行命令，下面是官方页面内嵌的帮助原文。

### `iodine`

官方给出的调用示例：`iodine -h`

```text
root@kali:~# iodine -h
iodine IP over DNS tunneling client
Usage: iodine [-v] [-h] [-f] [-r] [-u user] [-t chrootdir] [-d device] [-P password] [-m maxfragsize] [-M maxlen] [-T type] [-O enc] [-L 0|1] [-I sec] [-z context] [-F pidfile] [nameserver] topdomain
Options to try if connection doesn't work:
  -T force dns type: NULL, PRIVATE, TXT, SRV, MX, CNAME, A (default: autodetect)
  -O force downstream encoding for -T other than NULL: Base32, Base64, Base64u,
     Base128, or (only for TXT:) Raw  (default: autodetect)
  -I max interval between requests (default 4 sec) to prevent DNS timeouts
  -L 1: use lazy mode for low-latency (default). 0: don't (implies -I1)
  -m max size of downstream fragments (default: autodetect)
  -M max size of upstream hostnames (~100-255, default: 255)
  -r to skip raw UDP mode attempt
  -P password used for authentication (max 32 chars will be used)
Other options:
  -v to print version info and exit
  -h to print this help and exit
  -f to keep running in foreground
  -u name to drop privileges and run as user 'name'
  -t dir to chroot to directory dir
  -d device to set tunnel device name
  -z context, to apply specified SELinux context after initialization
  -F pidfile to write pid to a file
nameserver is the IP number/hostname of the relaying nameserver. if absent, /etc/resolv.conf is used
topdomain is the FQDN that is delegated to the tunnel endpoint.
```

### `iodine-client-start`

官方给出的调用示例：`iodine-client-start -h`

```text
root@kali:~# iodine-client-start -h
'iodine-client-start' starts an iodine IP-over-DNS tunnel.
Usage: iodine-client-start [option]
  -h, --help		Print help and exit
  -v, --version		Print version info and exit
Invoking the program without options attempts to set up and configure
an iodine IP-over-DNS tunnel using the configuration in the file
/etc/default/iodine-client or by querying the user. It tries to
figure out the right way to set things up by observing the network,
and if all else fails by guessing.
QUICK CONFIGURATION
Put two lines in the file /etc/default/iodine-client
	subdomain=your.tunnel.sub.domain
	passwd=password_for_that_tunnel
or invoke the script with those environment variables set:
	env subdomain=xxx passwd=xxx iodine-client-start
If these are not set, the script will query the user for them.
DETAILS
The configuration file consists of lines which are either comments
starting with '#', or settings of the form VAR="val". Valid VARs are:
subdomain
    Sample value: your.tunnel.sub.domain (no default, must be set)
passwd
    Sample value: password_for_that_tunnel (no default, must be set)
testhost
    Hostname to ping when testing if network is working (default:
    slashdot.org)
bounce_localnet
    Take the local network down and then up again before starting
    tunnel (default: false)
test_ping_localnet
    Test if the local network is working by pinging the gateway
    (default: true)
test_ping_tunnel
    Test if the iodine tunnel is working after it has been set up by
    pinging the host at the other end (default: true)
test_ping_final
    Test if the tunnel is working after everything is ostensibly set
    up by trying to ping an external host (default: true)
default_router
    IP address of router on the local network---should be found
    automatically, set this if that fails and the program guesses wrong.
interface
    Interface to use (e.g., eth1, eth0, etc) for connection to DNS
    server used for the iodine tunnel---should be found automatically,
    set this if that fails and the program guesses wrong.
mtu
    Set if tunnel MTU needs to be manually changed (lowered). Should
    not be necessary anymore, as recent versions of iodine negotiate
    an appropriate MTU during tunnel setup. But if that negotiation
    does not happen, or if you are using an older version of iodine,
    the default tunnel MTU is 1024, and if the local DNS server
    restricts to 512 byte packets you might need to use an MTU of 220.
skip_raw_udp_mode
    Set "-r" option in iodine command line. With this option, iodine
    does not try to establish a direct UDP socket to the iodine server
    on port 53. (default: true).
continue_on_error
    Set if the script should continue even if a command fails.
    Use to test script when running as non-root. Defaults to false
    if running as root, true otherwise.
```

### `iodined`

官方给出的调用示例：`iodined -h`

```text
root@kali:~# iodined -h
iodine IP over DNS tunneling server
Usage: iodined [-v] [-h] [-c] [-s] [-f] [-D] [-u user] [-t chrootdir] [-d device] [-m mtu] [-z context] [-l ip address to listen on] [-p port] [-n external ip] [-b dnsport] [-P password] [-F pidfile] tunnel_ip[/netmask] topdomain
  -v to print version info and exit
  -h to print this help and exit
  -c to disable check of client IP/port on each request
  -s to skip creating and configuring the tun device, which then has to be created manually
  -f to keep running in foreground
  -D to increase debug level
     (using -DD in UTF-8 terminal: "LC_ALL=C luit iodined -DD ...")
  -u name to drop privileges and run as user 'name'
  -t dir to chroot to directory dir
  -d device to set tunnel device name
  -m mtu to set tunnel device mtu
  -z context to apply SELinux context after initialization
  -l ip address to listen on for incoming dns traffic (default 0.0.0.0)
  -p port to listen on for incoming dns traffic (default 53)
  -n ip to respond with to NS queries
  -b port to forward normal DNS queries to (on localhost)
  -P password used for authentication (max 32 chars will be used)
  -F pidfile to write pid to a file
  -i maximum idle time before shutting down
tunnel_ip is the IP number of the local tunnel interface.
   /netmask sets the size of the tunnel network.
topdomain is the FQDN that is delegated to this server.
Updated on: 2026-May-25
 Edit this page
instaloader
ipv6toolkit
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install iodine`，再执行 `iodine --version` 2>/dev/null || `iodine -V`
- [ ] **2.** **读官方帮助** —— `iodine -h`，需要细节时 `man iodine`
- [ ] **3.** **在自有靶场跑最小用例** —— 官方给出的调用形式是：`Usage: iodine [-v] [-h] [-f] [-r] [-u user] [-t chrootdir] [-d device] [-P password] [-m maxfragsize] [-M maxlen] [-T type] [-O enc] [-L 0|1] [-I sec] [-z context] [-F pidfile] [nameserver] topdomain`
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/iodine/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/command-and-control.md`](../../tools/by-attack/command-and-control.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/iodine/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/iodine/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
