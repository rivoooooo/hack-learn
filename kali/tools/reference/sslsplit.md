# sslsplit

> Transparent and scalable SSL/TLS interception SSLsplit is a tool for man-in-the-middle attacks against SSL/TLS encrypted network connections. Connections are transparently intercepted through a network address translation engine and redire…

> **功能分类**：Web 应用 ｜ **Kali 包**：`sslsplit` ｜ **官方文档**：<https://www.kali.org/tools/sslsplit/>

## 1. 安装

```bash
sudo apt update
sudo apt install sslsplit
```

| 项目 | 内容 |
|------|------|
| 版本 | 0.5.5 |
| 架构 | any |
| 可执行命令 | `sslsplit` |
| 依赖 | `libc6`、`libevent-2.1-7t64`、`libevent-openssl-2.1-7t64`、`libevent-pthreads-2.1-7t64`、`libnet9`、`libpcap0.8t64`、`libssl3t64` |
| 安装体积 | 254 KB |
| 官网 | <https://www.roe.ch/SSLsplit> |
| 源码仓库 | <https://salsa.debian.org/debian/sslsplit> |
| 包追踪 | <https://pkg.kali.org/pkg/sslsplit> |

## 2. 官方用法示例

> 以下为 Kali 官方工具页给出的示例与输出原文。

```text
Usage Example
Run in debug mode (-D), log the connections (-l connections.log), set the chroot jail (-j /tmp/sslsplit/), save files to disk (-S /tmp/), specify the key (-k ca.key), specify the cert (-c ca.crt), specify ssl (ssl), and configure the proxy (0.0.0.0 8443 tcp 0.0.0.0 8080):
root@kali:~# sslsplit -D -l connections.log -j /tmp/sslsplit/ -S /tmp/ -k ca.key -c ca.crt ssl 0.0.0.0 8443 tcp 0.0.0.0 8080
Generated RSA key for leaf certs.
SSLsplit 0.4.6 (built 2013-06-06)
Copyright (c) 2009-2013, Daniel Roethlisberger <daniel@roe.ch>
http://www.roe.ch/SSLsplit
Features: -DDISABLE_SSLV2_SESSION_CACHE -DHAVE_NETFILTER
NAT engines: netfilter* tproxy
netfilter:  IP_TRANSPARENT SOL_IPV6 !IPV6_ORIGINAL_DST
compiled against OpenSSL 1.0.1e 11 Feb 2013 (1000105f)
rtlinked against OpenSSL 1.0.1e 11 Feb 2013 (1000105f)
TLS Server Name Indication (SNI) supported
OpenSSL is thread-safe with THREADID
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `sslsplit`

官方给出的调用示例：`sslsplit -D -l connections.log -j /tmp/sslsplit/ -S /tmp/ -k ca.key -c ca.crt ssl 0.0.0.0 8443 tcp 0.0.0.0 8080`

```text
root@kali:~# sslsplit -D -l connections.log -j /tmp/sslsplit/ -S /tmp/ -k ca.key -c ca.crt ssl 0.0.0.0 8443 tcp 0.0.0.0 8080
Generated RSA key for leaf certs.
SSLsplit 0.4.6 (built 2013-06-06)
Copyright (c) 2009-2013, Daniel Roethlisberger <
[email protected]
>
http://www.roe.ch/SSLsplit
Features: -DDISABLE_SSLV2_SESSION_CACHE -DHAVE_NETFILTER
NAT engines: netfilter* tproxy
netfilter:  IP_TRANSPARENT SOL_IPV6 !IPV6_ORIGINAL_DST
compiled against OpenSSL 1.0.1e 11 Feb 2013 (1000105f)
rtlinked against OpenSSL 1.0.1e 11 Feb 2013 (1000105f)
TLS Server Name Indication (SNI) supported
OpenSSL is thread-safe with THREADID
```

### `sslsplit（示例）`

官方给出的调用示例：`sslsplit -h`

```text
root@kali:~# sslsplit -h
Usage: sslsplit [-D] [-f conffile] [-o opt=val] [options...] [proxyspecs...]
  -f conffile use conffile to load configuration from
  -o opt=val  override conffile option opt with value val
  -c pemfile  use CA cert (and key) from pemfile to sign forged certs
  -k pemfile  use CA key (and cert) from pemfile to sign forged certs
  -C pemfile  use CA chain from pemfile (intermediate and root CA certs)
  -K pemfile  use key from pemfile for leaf certs (default: generate)
  -q crlurl   use URL as CRL distribution point for all forged certs
  -t certdir  use cert+chain+key PEM files from certdir to target all sites
              matching the common names (non-matching: -T or generate if CA)
  -A pemfile  use cert+chain+key PEM file as fallback leaf cert when none of
              those given by -t match, instead of generating one on the fly
  -w gendir   write leaf key and only generated certificates to gendir
  -W gendir   write leaf key and all certificates to gendir
  -O          deny all OCSP requests on all proxyspecs
  -P          passthrough SSL connections if they cannot be split because of
              client cert auth or no matching cert and no CA (default: drop)
  -a pemfile  use cert from pemfile when destination requests client certs
  -b pemfile  use key from pemfile when destination requests client certs
  -g pemfile  use DH group params from pemfile (default: keyfiles or auto)
  -G curve    use ECDH named curve (default: prime256v1)
  -Z          disable SSL/TLS compression on all connections
  -r proto    only support one of tls10 tls11 tls12 (default: all)
  -R proto    disable one of tls10 tls11 tls12 (default: none)
  -s ciphers  use the given OpenSSL cipher suite spec (default: ALL:-aNULL)
  -x engine   load OpenSSL engine with the given identifier
  -e engine   specify default NAT engine to use (default: netfilter)
  -E          list available NAT engines and exit
  -u user     drop privileges to user (default if run as root: nobody)
  -m group    when using -u, override group (default: primary group of user)
  -j jaildir  chroot() to jaildir (impacts sni proxyspecs, see manual page)
  -p pidfile  write pid to pidfile (default: no pid file)
  -l logfile  connect log: log one line summary per connection to logfile
  -L logfile  content log: full data to file or named pipe (excludes -S/-F)
  -S logdir   content log: full data to separate files in dir (excludes -L/-F)
  -F pathspec content log: full data to sep files with % subst (excl. -L/-S):
              %T - initial connection time as an ISO 8601 UTC timestamp
              %d - destination host and port
              %D - destination host
              %p - destination port
              %s - source host and port
              %S - source host
              %q - source port
              %% - literal '%'
      e.g.    "/var/log/sslsplit/%T-%s-%d.log"
  -X pcapfile pcap log: packets to pcapfile (excludes -Y/-y)
  -Y pcapdir  pcap log: packets to separate files in dir (excludes -X/-y)
  -y pathspec pcap log: packets to sep files with % subst (excl. -X/-Y):
              see option -F for pathspec format
  -I if       mirror packets to interface
  -T addr     mirror packets to target address (used with -I)
  -M logfile  log master keys to logfile in SSLKEYLOGFILE format
  -d          daemon mode: run in background, log error messages to syslog
  -D          debug mode: run in foreground, log debug messages on stderr
  -V          print version information and exit
  -h          print usage information and exit
  proxyspec = type listenaddr+port [natengine|targetaddr+port|"sni"+port]
      e.g.    http 0.0.0.0 8080 www.roe.ch 80  # http/4; static hostname dst
              https ::1 8443 2001:db8::1 443   # https/6; static address dst
              https 127.0.0.1 9443 sni 443     # https/4; SNI DNS lookups
              tcp 127.0.0.1 10025              # tcp/4; default NAT engine
              ssl 2001:db8::2 9999 pf          # ssl/6; NAT engine 'pf'
              autossl ::1 10025                # autossl/6; STARTTLS et al
Example:
  sslsplit -k ca.key -c ca.pem -P  https 127.0.0.1 8443  https ::1 8443
Updated on: 2026-Jun-17
 Edit this page
sslsniff
sudo
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install sslsplit`，再执行 `sslsplit --version` 2>/dev/null || `sslsplit -V`
- [ ] **2.** **读官方帮助** —— `sslsplit -h`，需要细节时 `man sslsplit`
- [ ] **3.** **在自有靶场跑最小用例** —— 官方给出的调用形式是：`Usage: sslsplit [-D] [-f conffile] [-o opt=val] [options...] [proxyspecs...]`
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/sslsplit/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/collection.md`](../../tools/by-attack/collection.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/sslsplit/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/sslsplit/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
