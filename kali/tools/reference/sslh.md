# sslh

> Applicative protocol multiplexer sslh lets one accept HTTPS, SSH, OpenVPN, tinc and XMPP connections on the same port. This makes it possible to connect to any of these servers on port 443 (e.g. from inside a corporate firewall, which almo…

> **功能分类**：信息搜集 ｜ **Kali 包**：`sslh` ｜ **官方文档**：<https://www.kali.org/tools/sslh/>

## 1. 安装

```bash
sudo apt update
sudo apt install sslh
```

| 项目 | 内容 |
|------|------|
| 版本 | 2.3.1 |
| 架构 | any |
| 可执行命令 | `sslh`、`sslh-ev`、`sslh-select` |
| 依赖 | `adduser` |
| 安装体积 | 844 KB |
| 官网 | <http://www.rutschle.net/tech/sslh/README.html> |
| 源码仓库 | <https://salsa.debian.org/debian/sslh.git> |
| 包追踪 | <https://pkg.kali.org/pkg/sslh> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
sslh -h          # 查看用法
man sslh         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 3 个可执行命令，下面是官方页面内嵌的帮助原文。

### `sslh`

> 官方示例调用：`sslh -h`

```text
root@kali:~# sslh -h
sslhcfg: invalid option "-h"
 [-Vfin] [-F <file>] [-v <n>] [--verbose-config=<n>] [--verbose-config-error=<n>] [--verbose-connections=<n>] [--verbose-connections-try=<n>] [--verbose-connections-error=<n>] [--verbose-fd=<n>] [--verbose-packets=<n>] [--verbose-probe-info=<n>] [--verbose-probe-error=<n>] [--verbose-system-error=<n>] [--verbose-int-error=<n>] [--transparent] [-t <n>] [--udp-max-connections=<n>] [-u <str>] [-P <file>] [-C <path>] [--syslog-facility=<str>] [--logfile=<str>] [--on-timeout=<str>] [--prefix=<str>] [-p <host:port>]... [--ssh=<host:port>]... [--tls=<host:port>]... [--ssl=<host:port>]... [--openvpn=<host:port>]... [--tinc=<host:port>]... [--wireguard=<host:port>]... [--xmpp=<host:port>]... [--http=<host:port>]... [--adb=<host:port>]... [--socks5=<host:port>]... [--syslog=<host:port>]... [--msrdp=<host:port>]... [--anyprot=<host:port>]...
  -F, --config=<file>      	Specify configuration file
  -v, --verbose=<n>        	Override all verbosness options
  --verbose-config=<n>     	Print configuration at startup
  --verbose-config-error=<n>	Print configuration errors
  --verbose-connections=<n>	Trace established incoming address to forward address
  --verbose-connections-try=<n>	Connection errors
  --verbose-connections-error=<n>	Connection attempts towards targets
  --verbose-fd=<n>         	File descriptor activity, open/close/whatnot
  --verbose-packets=<n>    	Hexdump packets on which probing is done
  --verbose-probe-info=<n> 	Trace the probe process
  --verbose-probe-error=<n>	Failures and problems during probing
  --verbose-system-error=<n>	System call failures
  --verbose-int-error=<n>  	Internal errors that should never happen
  -V, --version            	Print version information and exit
  -f, --foreground         	Run in foreground instead of as a daemon
  -i, --inetd              	Run in inetd mode: use stdin/stdout instead of network listen
  -n, --numeric            	Print IP addresses and ports as numbers
  --transparent            	Set up as a transparent proxy
  -t, --timeout=<n>        	Set up timeout before connecting to default target
  --udp-max-connections=<n>	Number of concurrent UDP connections
  -u, --user=<str>         	Username to change to after set-up
  -P, --pidfile=<file>     	Path to file to store PID of current instance
  -C, --chroot=<path>      	Root to change to after set-up
  --syslog-facility=<str>  	Facility to syslog to
  --logfile=<str>          	Log messages to a file
  --on-timeout=<str>       	Target to connect to when timing out
  --prefix=<str>           	Reserved for testing
  -p, --listen=<host:port> 	Listen on host:port
  --ssh=<host:port>        	Set up ssh target
  --tls=<host:port>        	Set up TLS/SSL target
  --ssl=<host:port>        	Set up TLS/SSL target
  --openvpn=<host:port>    	Set up OpenVPN target
  --tinc=<host:port>       	Set up tinc target
  --wireguard=<host:port>  	Set up WireGuard target
  --xmpp=<host:port>       	Set up XMPP target
  --http=<host:port>       	Set up HTTP (plain) target
  --adb=<host:port>        	Set up ADB (Android Debug) target
  --socks5=<host:port>     	Set up socks5 target
  --syslog=<host:port>     	Set up syslog target
  --msrdp=<host:port>      	Set up msrdp target
  --anyprot=<host:port>    	Set up default target
```

### `sslh-ev`

> 官方示例调用：`sslh-ev -h`

```text
root@kali:~# sslh-ev -h
sslhcfg: invalid option "-h"
 [-Vfin] [-F <file>] [-v <n>] [--verbose-config=<n>] [--verbose-config-error=<n>] [--verbose-connections=<n>] [--verbose-connections-try=<n>] [--verbose-connections-error=<n>] [--verbose-fd=<n>] [--verbose-packets=<n>] [--verbose-probe-info=<n>] [--verbose-probe-error=<n>] [--verbose-system-error=<n>] [--verbose-int-error=<n>] [--transparent] [-t <n>] [--udp-max-connections=<n>] [-u <str>] [-P <file>] [-C <path>] [--syslog-facility=<str>] [--logfile=<str>] [--on-timeout=<str>] [--prefix=<str>] [-p <host:port>]... [--ssh=<host:port>]... [--tls=<host:port>]... [--ssl=<host:port>]... [--openvpn=<host:port>]... [--tinc=<host:port>]... [--wireguard=<host:port>]... [--xmpp=<host:port>]... [--http=<host:port>]... [--adb=<host:port>]... [--socks5=<host:port>]... [--syslog=<host:port>]... [--msrdp=<host:port>]... [--anyprot=<host:port>]...
  -F, --config=<file>      	Specify configuration file
  -v, --verbose=<n>        	Override all verbosness options
  --verbose-config=<n>     	Print configuration at startup
  --verbose-config-error=<n>	Print configuration errors
  --verbose-connections=<n>	Trace established incoming address to forward address
  --verbose-connections-try=<n>	Connection errors
  --verbose-connections-error=<n>	Connection attempts towards targets
  --verbose-fd=<n>         	File descriptor activity, open/close/whatnot
  --verbose-packets=<n>    	Hexdump packets on which probing is done
  --verbose-probe-info=<n> 	Trace the probe process
  --verbose-probe-error=<n>	Failures and problems during probing
  --verbose-system-error=<n>	System call failures
  --verbose-int-error=<n>  	Internal errors that should never happen
  -V, --version            	Print version information and exit
  -f, --foreground         	Run in foreground instead of as a daemon
  -i, --inetd              	Run in inetd mode: use stdin/stdout instead of network listen
  -n, --numeric            	Print IP addresses and ports as numbers
  --transparent            	Set up as a transparent proxy
  -t, --timeout=<n>        	Set up timeout before connecting to default target
  --udp-max-connections=<n>	Number of concurrent UDP connections
  -u, --user=<str>         	Username to change to after set-up
  -P, --pidfile=<file>     	Path to file to store PID of current instance
  -C, --chroot=<path>      	Root to change to after set-up
  --syslog-facility=<str>  	Facility to syslog to
  --logfile=<str>          	Log messages to a file
  --on-timeout=<str>       	Target to connect to when timing out
  --prefix=<str>           	Reserved for testing
  -p, --listen=<host:port> 	Listen on host:port
  --ssh=<host:port>        	Set up ssh target
  --tls=<host:port>        	Set up TLS/SSL target
  --ssl=<host:port>        	Set up TLS/SSL target
  --openvpn=<host:port>    	Set up OpenVPN target
  --tinc=<host:port>       	Set up tinc target
  --wireguard=<host:port>  	Set up WireGuard target
  --xmpp=<host:port>       	Set up XMPP target
  --http=<host:port>       	Set up HTTP (plain) target
  --adb=<host:port>        	Set up ADB (Android Debug) target
  --socks5=<host:port>     	Set up socks5 target
  --syslog=<host:port>     	Set up syslog target
  --msrdp=<host:port>      	Set up msrdp target
  --anyprot=<host:port>    	Set up default target
```

### `sslh-select`

> 官方示例调用：`sslh-select -h`

```text
root@kali:~# sslh-select -h
sslhcfg: invalid option "-h"
 [-Vfin] [-F <file>] [-v <n>] [--verbose-config=<n>] [--verbose-config-error=<n>] [--verbose-connections=<n>] [--verbose-connections-try=<n>] [--verbose-connections-error=<n>] [--verbose-fd=<n>] [--verbose-packets=<n>] [--verbose-probe-info=<n>] [--verbose-probe-error=<n>] [--verbose-system-error=<n>] [--verbose-int-error=<n>] [--transparent] [-t <n>] [--udp-max-connections=<n>] [-u <str>] [-P <file>] [-C <path>] [--syslog-facility=<str>] [--logfile=<str>] [--on-timeout=<str>] [--prefix=<str>] [-p <host:port>]... [--ssh=<host:port>]... [--tls=<host:port>]... [--ssl=<host:port>]... [--openvpn=<host:port>]... [--tinc=<host:port>]... [--wireguard=<host:port>]... [--xmpp=<host:port>]... [--http=<host:port>]... [--adb=<host:port>]... [--socks5=<host:port>]... [--syslog=<host:port>]... [--msrdp=<host:port>]... [--anyprot=<host:port>]...
  -F, --config=<file>      	Specify configuration file
  -v, --verbose=<n>        	Override all verbosness options
  --verbose-config=<n>     	Print configuration at startup
  --verbose-config-error=<n>	Print configuration errors
  --verbose-connections=<n>	Trace established incoming address to forward address
  --verbose-connections-try=<n>	Connection errors
  --verbose-connections-error=<n>	Connection attempts towards targets
  --verbose-fd=<n>         	File descriptor activity, open/close/whatnot
  --verbose-packets=<n>    	Hexdump packets on which probing is done
  --verbose-probe-info=<n> 	Trace the probe process
  --verbose-probe-error=<n>	Failures and problems during probing
  --verbose-system-error=<n>	System call failures
  --verbose-int-error=<n>  	Internal errors that should never happen
  -V, --version            	Print version information and exit
  -f, --foreground         	Run in foreground instead of as a daemon
  -i, --inetd              	Run in inetd mode: use stdin/stdout instead of network listen
  -n, --numeric            	Print IP addresses and ports as numbers
  --transparent            	Set up as a transparent proxy
  -t, --timeout=<n>        	Set up timeout before connecting to default target
  --udp-max-connections=<n>	Number of concurrent UDP connections
  -u, --user=<str>         	Username to change to after set-up
  -P, --pidfile=<file>     	Path to file to store PID of current instance
  -C, --chroot=<path>      	Root to change to after set-up
  --syslog-facility=<str>  	Facility to syslog to
  --logfile=<str>          	Log messages to a file
  --on-timeout=<str>       	Target to connect to when timing out
  --prefix=<str>           	Reserved for testing
  -p, --listen=<host:port> 	Listen on host:port
  --ssh=<host:port>        	Set up ssh target
  --tls=<host:port>        	Set up TLS/SSL target
  --ssl=<host:port>        	Set up TLS/SSL target
  --openvpn=<host:port>    	Set up OpenVPN target
  --tinc=<host:port>       	Set up tinc target
  --wireguard=<host:port>  	Set up WireGuard target
  --xmpp=<host:port>       	Set up XMPP target
  --http=<host:port>       	Set up HTTP (plain) target
  --adb=<host:port>        	Set up ADB (Android Debug) target
  --socks5=<host:port>     	Set up socks5 target
  --syslog=<host:port>     	Set up syslog target
  --msrdp=<host:port>      	Set up msrdp target
  --anyprot=<host:port>    	Set up default target
Updated on: 2026-Aug-25
 Edit this page
sqlninja
sslscan
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install sslh`，再执行 `sslh --version` 2>/dev/null || `sslh -V`
- [ ] **2.** **读官方帮助** —— `sslh -h`，需要细节时 `man sslh`
- [ ] **3.** **在自有靶场跑最小用例** —— 用 `sslh -h` 里最简单的那个子命令试一次
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/sslh/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/command-and-control.md`](../../tools/by-attack/command-and-control.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/sslh/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/sslh/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
