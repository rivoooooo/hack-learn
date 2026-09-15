# openvpn

> Virtual private network daemon OpenVPN is an application to securely tunnel IP networks over a single UDP or TCP port. It can be used to access remote sites, make secure point-to-point connections, enhance wireless security, etc. OpenVPN u…

> **功能分类**：通用工具 ｜ **Kali 包**：`openvpn` ｜ **官方文档**：<https://www.kali.org/tools/openvpn/>

## 1. 安装

```bash
sudo apt update
sudo apt install openvpn
```

| 项目 | 内容 |
|------|------|
| 版本 | 2.7.5 |
| 架构 | any |
| 可执行命令 | `openvpn` |
| 安装体积 | 1.80 MB |
| 官网 | <https://openvpn.net/community/> |
| 源码仓库 | <https://salsa.debian.org/debian/openvpn> |
| 包追踪 | <https://pkg.kali.org/pkg/openvpn> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
openvpn -h          # 查看用法
man openvpn         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `openvpn`

官方给出的调用示例：`openvpn --help`

```text
root@kali:~# openvpn --help
OpenVPN 2.7.5 x86_64-pc-linux-gnu [SSL (OpenSSL)] [LZO] [LZ4] [EPOLL] [PKCS11] [MH/PKTINFO] [AEAD] [DCO]
General Options:
--config file   : Read configuration options from file.
--help          : Show options.
--version       : Show copyright and version information.
Tunnel Options:
--local host|* [port]: Local host name or IP address and port for bind.
                        If specified, OpenVPN will bindto this address. If unspecified,
                        OpenVPN will bind to all interfaces. '*' can be used as hostname
                        and means 'any host' (OpenVPN will listen on what is returned by the OS).
                        On a client, or in point-to-point mode, this can only be specified once (1 socket).
                        On an OpenVPN setup running as ``--server``, this can be specified multiple times
                        to open multiple listening sockets on different addresses and/or different ports.
                        In order to specify multiple listen ports without specifying an address, use '*'
                        to signal 'use what the operating system gives you as default', for
                        'all IPv4 addresses' use '0.0.0.0', for 'all IPv6 addresses' use '::'.
                        ``--local`` implies ``--bind``.
--remote host [port] : Remote host name or ip address.
--remote-random : If multiple --remote options specified, choose one randomly.
--remote-random-hostname : Add a random string to remote DNS name.
--mode m        : Major mode, m = 'p2p' (default, point-to-point) or 'server'.
--proto p       : Use protocol p for communicating with peer.
                  p = udp (default), tcp-server, tcp-client
                      udp4, tcp4-server, tcp4-client
                      udp6, tcp6-server, tcp6-client
--proto-force p : only consider protocol p in list of connection profiles.
                  p = udp or tcp
--connect-retry n [m] : For client, number of seconds to wait between
                  connection retries (default=1). On repeated retries
                  the wait time is exponentially increased to a maximum of m
                  (default=300).
--connect-retry-max n : Maximum connection attempt retries, default infinite.
--http-proxy s p [up] [auth] : Connect to remote host
                  through an HTTP proxy at address s and port p.
                  If proxy authentication is required,
                  up is a file containing username/password on 2 lines, or
                  'stdin' to prompt from console.  Add auth='ntlm2' if
                  the proxy requires NTLM authentication.
--http-proxy s p 'auto[-nct]' : Like the above directive, but automatically
                  determine auth method and query for username/password
                  if needed.  auto-nct disables weak proxy auth methods.
--http-proxy-option type [parm] : Set extended HTTP proxy options.
                                  Repeat to set multiple options.
                  VERSION version (default=1.0)
                  AGENT user-agent
--socks-proxy s [p] [up] : Connect to remote host through a Socks5 proxy at
                  address s and port p (default port = 1080).
                  If proxy authentication is required,
                  up is a file containing username/password on 2 lines, or
                  'stdin' to prompt for console.
--socks-proxy-retry : Retry indefinitely on Socks proxy errors.
--resolv-retry n: If hostname resolve fails for --remote, retry
                  resolve for n seconds before failing (disabled by default).
                  Set n="infinite" to retry indefinitely.
--preresolve    : Resolve configured --remote, --local, and proxy hostnames at startup.
--float         : Allow remote to change its IP address/port, such as through
                  DHCP (this is the default if --remote is not used).
--ipchange cmd  : Run command cmd on remote ip address initial
                  setting or change -- execute as: cmd ip-address port#
--port port     : TCP/UDP port # for both local and remote.
--lport port    : TCP/UDP port # for local (default=1194). Implies --bind.
--rport port    : TCP/UDP port # for remote (default=1194).
--bind          : Bind to local address and port. (This is the default unless
                  --proto tcp-client or --http-proxy or --socks-proxy is used).
--nobind        : Do not bind to local address and port.
--dev tunX|tapX : tun/tap device (X can be omitted for dynamic device.
--dev-type dt   : Which device type are we using? (dt = tun or tap) Use
                  this option only if the tun/tap device used with --dev
                  does not begin with "tun" or "tap".
--dev-node node : Explicitly set the device node rather than using
                  /dev/net/tun, /dev/tun, /dev/tap, etc.
--disable-dco   : Do not attempt using Data Channel Offload.
--lladdr hw     : Set the link layer address of the tap device.
--topology t    : Set --dev tun topology: 'net30', 'p2p', or 'subnet'.
--ifconfig l rn : TUN: configure device to use IP address l as a local
                  endpoint and rn as a remote endpoint.  l & rn should be
                  swapped on the other peer.  l & rn must be private
                  addresses outside of the subnets used by either peer.
                  TAP: configure device to use IP address l as a local
                  endpoint and rn as a subnet mask.
--ifconfig-ipv6 l r : configure device to use IPv6 address l as local
                      endpoint (as a /64) and r as remote endpoint
--ifconfig-noexec : Don't actually execute ifconfig/netsh command, instead
                    pass --ifconfig parms by environment to scripts.
--ifconfig-nowarn : Don't warn if the --ifconfig option on this side of the
                    connection doesn't match the remote side.
--route-table table_id : Specify a custom routing table for use with --route(-ipv6).
                           If not specified, the id of the default routing table will be used.
--route network [netmask] [gateway] [metric] :
                  Add route to routing table after connection
                  is established.  Multiple routes can be specified.
                  netmask default: 255.255.255.255
                  gateway default: taken from --route-gateway or --ifconfig
                  Specify default by leaving blank or setting to "default".
--route-ipv6 network/bits [gateway] [metric] :
                  Add IPv6 route to routing table after connection
                  is established.  Multiple routes can be specified.
                  gateway default: taken from --route-ipv6-gateway or 'remote'
                  in --ifconfig-ipv6
--route-gateway gw|'dhcp' : Specify a default gateway for use with --route.
--route-ipv6-gateway gw : Specify a default gateway for use with --route-ipv6.
--route-metric m : Specify a default metric for use with --route.
--route-delay n [w] : Delay n seconds after connection initiation before
                  adding routes (may be 0).  If not specified, routes will
                  be added immediately after tun/tap open.  On Windows, wait
                  up to w seconds for TUN/TAP adapter to come up.
--route-up cmd  : Run command cmd after routes are added.
--route-pre-down cmd : Run command cmd before routes are removed.
--route-noexec  : Don't add routes automatically.  Instead pass routes to
                  --route-up script using environmental variables.
--route-nopull  : When used with --client or --pull, accept options pushed
                  by server EXCEPT for routes, dns, and dhcp options.
--allow-pull-fqdn : Allow client to pull DNS names from server for
                    --ifconfig, --route, and --route-gateway.
--redirect-gateway [flags]: Automatically execute routing
                  commands to redirect all outgoing IP traffic through the
                  VPN.  Add 'local' flag if both OpenVPN servers are directly
                  connected via a common subnet, such as with WiFi.
                  Add 'def1' flag to set default route using using 0.0.0.0/1
                  and 128.0.0.0/1 rather than 0.0.0.0/0.  Add 'bypass-dhcp'
                  flag to add a direct route to DHCP server, bypassing tunnel.
                  Add 'bypass-dns' flag to similarly bypass tunnel for DNS.
--redirect-private [flags]: Like --redirect-gateway, but omit actually changing
                  the default gateway.  Useful when pushing private subnets.
--block-ipv6     : (Client) Instead sending IPv6 to the server generate
                   ICMPv6 host unreachable messages on the client.
                   (Server) Instead of forwarding IPv6 packets send
                   ICMPv6 host unreachable packets to the client.
--client-nat snat|dnat network netmask alias : on client add 1-to-1 NAT rule.
--push-peer-info : (client only) push client info to server.
--setenv name value : Set a custom environmental variable to pass to script.
--setenv FORWARD_COMPATIBLE 1 : Relax config file syntax checking to allow
                  directives for future OpenVPN versions to be ignored.
--ignore-unknown-option opt1 opt2 ...: Relax config file syntax. Allow
                  these options to be ignored when unknown
--script-security level: Where level can be:
                  0 -- strictly no calling of external programs
                  1 -- (default) only call built-ins such as ifconfig
                  2 -- allow calling of built-ins and scripts
                  3 -- allow password to be passed to scripts via env
--shaper n      : Restrict output to peer to n bytes per second.
--keepalive n m : Helper option for setting timeouts in server mode.  Send
                  ping once every n seconds, restart if ping not received
                  for m seconds.
--inactive n [bytes] : Exit after n seconds of activity on tun/tap device
                  produces a combined in/out byte count < bytes.
--session-timeout n: Limit connection time to n seconds.
--ping-exit n   : Exit if n seconds pass without reception of remote ping.
--ping-restart n: Restart if n seconds pass without reception of remote ping.
--ping-timer-rem: Run the --ping-exit/--ping-restart timer only if we have a
                  remote address.
--ping n        : Ping remote once every n seconds over TCP/UDP port.
--multihome     : Configure a multi-homed UDP server.
--remap-usr1 s  : On SIGUSR1 signals, remap signal (s='SIGHUP' or 'SIGTERM').
--persist-tun   : Keep tun/tap device open across SIGUSR1 or --ping-restart.
--persist-remote-ip : Keep remote IP address across SIGUSR1 or --ping-restart.
--persist-local-ip  : Keep local IP address across SIGUSR1 or --ping-restart.
--passtos       : TOS passthrough (applies to IPv4 only).
--tun-mtu n     : Take the tun/tap device MTU to be n and derive the
                  TCP/UDP MTU from it (default=1500).
--tun-mtu-extra n : Assume that tun/tap device might return as many
                  as n bytes more than the tun-mtu size on read
                  (default TUN=0 TAP=32).
--tun-mtu-max n : Maximum pushable MTU (default and minimum=1600).
--link-mtu n    : Take the TCP/UDP device MTU to be n and derive the tun MTU
                  from it.
--mtu-disc type : Should we do Path MTU discovery on TCP/UDP channel?
                  'no'    -- Never send DF (Don't Fragment) frames
                  'maybe' -- Use per-route hints
                  'yes'   -- Always DF (Don't Fragment)
--mtu-test      : Empirically measure and report MTU.
--fragment max  : Enable internal datagram fragmentation so that no UDP
                  datagrams are sent which are larger than max bytes.
                  Adds 4 bytes of overhead per datagram.
--mssfix [n]    : Set upper bound on TCP MSS, default = tun-mtu size
                  or --fragment max value, whichever is lower.
--sndbuf size   : Set the TCP/UDP send buffer size.
--rcvbuf size   : Set the TCP/UDP receive buffer size.
--mark value    : Mark encrypted packets being sent with value. The mark value
                  can be matched in policy routing and packetfilter rules.
--bind-dev dev  : Bind to the given device when making connection to a peer or
                  listening for connections. This allows sending encrypted packets
                  via a VRF present on the system.
--txqueuelen n  : Set the tun/tap TX queue length to n (Linux only).
--mlock         : Disable Paging -- ensures key material and tunnel
                  data will never be written to disk.
--up cmd        : Run command cmd after successful tun device open.
                  Execute as: cmd tun/tap-dev tun-mtu link-mtu \
                              ifconfig-local-ip ifconfig-remote-ip
                  (pre --user or --group UID/GID change)
--up-delay      : Delay tun/tap open and possible --up script execution
                  until after TCP/UDP connection establishment with peer.
--down cmd      : Run command cmd after tun device close.
                  (post --user/--group UID/GID change and/or --chroot)
                  (command parameters are same as --up option)
--down-pre      : Run --down command before TUN/TAP close.
--up-restart    : Run up/down commands for all restarts including those
                  caused by --ping-restart or SIGUSR1
--user user     : Set UID to user after initialization.
--group group   : Set GID to group after initialization.
--chroot dir    : Chroot to this directory after initialization.
--cd dir        : Change to this directory before initialization.
--daemon [name] : Become a daemon after initialization.
                  The optional 'name' parameter will be passed
                  as the program name to the system logger.
--syslog [name] : Output to syslog, but do not become a daemon.
                  See --daemon above for a description of the 'name' parm.
--log file      : Output log to file which is created/truncated on open.
--log-append file : Append log to file, or create file if nonexistent.
--suppress-timestamps : Don't log timestamps to stdout/stderr.
--machine-readable-output : Always log timestamp, message flags to stdout/stderr.
--writepid file : Write main process ID to file.
--nice n        : Change process priority (>0 = lower, <0 = higher).
--echo [parms ...] : Echo parameters to log output.
--verb n        : Set output verbosity to n (default=1):
                  (Level 3 is recommended if you want a good summary
                  of what's happening without being swamped by output).
                : 0 -- no output except fatal errors
                : 1 -- startup info + connection initiated messages +
```

## 4. 实践清单

按顺序做完这五步，就能把工具从「装上」推进到「会用」：

- [ ] **1.** **装好并确认版本** —— `sudo apt install openvpn`，再执行 `openvpn --version` 2>/dev/null || `openvpn -V`
- [ ] **2.** **读官方帮助** —— `openvpn -h`，需要细节时 `man openvpn`
- [ ] **3.** **在自有靶场跑最小用例** —— 用 `openvpn -h` 里最简单的那个子命令试一次
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/openvpn/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/openvpn/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/openvpn/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
