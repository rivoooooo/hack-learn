# dnscat2

> DNS tunnel (metapackage) This tool is designed to create an encrypted command-and-control (C&C) channel over the DNS protocol, which is an effective tunnel out of almost every network.

> **功能分类**：通用工具 ｜ **Kali 包**：`dnscat2` ｜ **官方文档**：<https://www.kali.org/tools/dnscat2/>

## 1. 安装

```bash
sudo apt update
sudo apt install dnscat2
```

| 项目 | 内容 |
|------|------|
| 版本 | 0.07 |
| 架构 | any |
| 可执行命令 | `dnscat2`、`dnscat2-client`、`dnscat`、`dnscat2-server` |
| 依赖 | `dnscat2-client`、`dnscat2-server`、`dnscat2-client` |
| 安装体积 | 16 KB |
| 官网 | <https://github.com/iagox86/dnscat2> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/dnscat2> |
| 包追踪 | <https://pkg.kali.org/pkg/dnscat2> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
dnscat2 -h          # 查看用法
man dnscat2         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 4 个可执行命令，下面是官方页面内嵌的帮助原文。

### `dnscat`

官方给出的调用示例：`dnscat -h`

```text
root@kali:~# dnscat -h
Usage: dnscat [args] [domain]
General options:
 --help -h               This page.
 --version               Get the version.
 --delay <ms>            Set the maximum delay between packets (default: 1000).
                         The minimum is technically 50 for technical reasons,
                         but transmitting too quickly might make performance
                         worse.
 --steady                If set, always wait for the delay before sending.
                         the next message (by default, when a response is
                         received, the next message is immediately transmitted.
 --max-retransmits <n>   Only re-transmit a message <n> times before giving up
                         and assuming the server is dead (default: 20).
 --retransmit-forever    Set if you want the client to re-transmit forever
                         until a server turns up. This can be helpful, but also
                         makes the server potentially run forever.
 --secret                Set the shared secret; set the same one on the server
                         and the client to prevent man-in-the-middle attacks!
 --no-encryption         Turn off encryption/authentication.
Input options:
 --console               Send/receive output to the console.
 --exec -e <process>     Execute the given process and link it to the stream.
 --command               Start an interactive 'command' session (default).
 --ping                  Simply check if there's a dnscat2 server listening.
Debug options:
 -d                      Display more debug info (can be used multiple times).
 -q                      Display less debug info (can be used multiple times).
 --packet-trace          Display incoming/outgoing dnscat2 packets
Driver options:
 --dns <options>         Enable DNS mode with the given domain.
   domain=<domain>       The domain to make requests for.
   host=<hostname>       The host to listen on (default: 0.0.0.0).
   port=<port>           The port to listen on (default: 53).
   type=<type>           The type of DNS requests to use, can use
                         multiple comma-separated (options: TXT, MX,
                         CNAME, A, AAAA) (default: TXT,CNAME,MX).
   server=<server>       The upstream server for making DNS requests
                         (default: autodetected = 192.168.0.1).
Examples:
 ./dnscat --dns domain=skullseclabs.org
 ./dnscat --dns domain=skullseclabs.org,server=8.8.8.8,port=53
 ./dnscat --dns domain=skullseclabs.org,port=5353
 ./dnscat --dns domain=skullseclabs.org,port=53,type=A,CNAME
By default, a --dns driver on port 53 is enabled if a hostname is
passed on the commandline:
 ./dnscat skullseclabs.org
ERROR: --help requested
```

### `dnscat2-server`

官方给出的调用示例：`dnscat2-server --help`

```text
root@kali:~# dnscat2-server --help
New window created: 0
New window created: crypto-debug
You'll almost certainly want to run this in one of a few ways...
Default host (0.0.0.0) and port (53), with no specific domain:
# ruby dnscat2.rb
Default host/port, with a particular domain to listen on:
# ruby dnscat2.rb domain.com
Or multiple domains:
# ruby dnscat2.rb a.com b.com c.com
If you need to change the address or port it's listening on, that
can be done by passing the --dns argument:
# ruby dnscat2.rb --dns 'host=127.0.0.1,port=53531,domain=a.com,domain=b.com'
For other options, see below!
  -h, --h                   Placeholder for help
  -v, --version             Get the dnscat version
  -d, --dns=<s>             Start a DNS server. Can optionally pass a number of
                            comma-separated name=value pairs (host, port,
                            domain). Eg, '--dns
                            host=0.0.0.0,port=53531,domain=skullseclabs.org' -
                            'domain' can be passed multiple times
  -n, --dnshost=<s>         The DNS ip address to listen on [deprecated]
                            (default: 0.0.0.0)
  -s, --dnsport=<i>         The DNS port to listen on [deprecated] (default:
                            53)
  -p, --passthrough=<s>     Unhandled requests are sent upstream DNS server,
                            host:port (default: )
  -e, --security=<s>        Set the security level; 'open' lets the client
                            choose; 'encrypted' requires encryption (default if
                            --secret isn't set); 'authenticated' requires
                            encryption and authentication (default if --secret
                            is set)
  -c, --secret=<s>          A pre-shared secret, passed to both the client and
                            server to prevent man-in-the-middle attacks
  -a, --auto-command=<s>    Send this to each client that connects (default: )
  -u, --auto-attach         Automatically attach to new sessions
  -k, --packet-trace        Display incoming/outgoing dnscat packets
  -r, --process=<s>         If set, the given process is run for every incoming
                            console/exec session and given stdin/stdout. This
                            has security implications.
  -i, --history-size=<i>    The number of lines of history that windows will
                            maintain (default: 1000)
  -l, --listener=<i>        DEBUG: Start a listener driver on the given port
  -f, --firehose            If set, all output goes to stdout instead of being
                            put in windows.
  --help                    Show this message
Learn more with
OffSec
Want to learn more about dnscat2? get access to in-depth training and hands-on labs:
PEN-200: 20.2.2. Tunneling Through Deep Packet Inspection: DNS Tunneling with dnscat2
PEN-300: 13.7.2. Bypassing Network Filters: DNS Tunneling with dnscat2
PEN-200 course
Updated on: 2026-Aug-25
 Edit this page
dfwinreg
dnsrecon
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install dnscat2`，再执行 `dnscat2 --version` 2>/dev/null || `dnscat2 -V`
- [ ] **2.** **读官方帮助** —— `dnscat2 -h`，需要细节时 `man dnscat2`
- [ ] **3.** **在自有靶场跑最小用例** —— 官方给出的调用形式是：`Usage: dnscat [args] [domain]`
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/dnscat2/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/command-and-control.md`](../../tools/by-attack/command-and-control.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/dnscat2/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/dnscat2/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
