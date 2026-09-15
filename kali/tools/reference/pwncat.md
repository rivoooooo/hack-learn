# pwncat

> Netcat on steroids This package contains Netcat on steroids with Firewall, IDS/IPS evasion, bind and reverse shell, self-injecting shell and port forwarding magic - and its fully scriptable with Python (PSE).

> **功能分类**：通用工具 ｜ **Kali 包**：`pwncat` ｜ **官方文档**：<https://www.kali.org/tools/pwncat/>

## 1. 安装

```bash
sudo apt update
sudo apt install pwncat
```

| 项目 | 内容 |
|------|------|
| 版本 | 0.1.2 |
| 架构 | all |
| 可执行命令 | `pwncat` |
| 依赖 | `python3` |
| 安装体积 | 5.63 MB |
| 官网 | <https://github.com/cytopia/pwncat> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/pwncat> |
| 包追踪 | <https://pkg.kali.org/pkg/pwncat> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
pwncat -h          # 查看用法
man pwncat         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `pwncat`

官方给出的调用示例：`pwncat -h`

```text
root@kali:~# pwncat -h
usage: pwncat [options] hostname port
       pwncat [options] -l [hostname] port
       pwncat [options] -z hostname port
       pwncat [options] -L [addr:]port hostname port
       pwncat [options] -R addr:port hostname port
       pwncat -V, --version
       pwncat -h, --help
Enhanced and comptaible Netcat implementation written in Python (2 and 3) with
connect, zero-i/o, listen and forward modes and techniques to detect and evade
firewalls and intrusion detection/prevention systems.
If no mode arguments are specified, pwncat will run in connect mode and act as
a client to connect to a remote endpoint. If the connection to the remote
endoint is lost, pwncat will quit. See options for how to automatically re-
connect.
positional arguments:
  hostname              Address to listen, forward, scan or connect to.
  port                  [All modes]
                        Single port to listen, forward or connect to.
                        [Zero-I/O mode]
                        Specify multiple ports to scan:
                        Via list:  4444,4445,4446
                        Via range: 4444-4446
                        Via incr:  4444+2
mode arguments:
  -l, --listen          [Listen mode]:
                        Start a server and listen for incoming connections.
                        If using TCP and a connected client disconnects or the
                        connection is interrupted otherwise, the server will
                        quit. See -k/--keep-open to change this behaviour.
  -z, --zero            [Zero-I/0 mode]:
                        Connect to a remote endpoint and report status only.
                        Used for port scanning.
                        See --banner for version detection.
  -L, --local [addr:]port
                        [Local forward mode]:
                        This mode will start a server and a client internally.
                        The internal server will listen locally on specified
                        addr/port (given by --local [addr:]port).
                        The server will then forward traffic to the internal
                        client which connects to another server specified by
                        hostname/port given via positional arguments.
                        (I.e.: proxies a remote service to a local address)
  -R, --remote addr:port
                        [Remote forward mode]:
                        This mode will start two clients internally. One is
                        connecting to the target and one is connecting to
                        another pwncat/netcat server you have started some-
                        where. Once connected, it will then proxy traffic
                        between you and the target.
                        This mode should be applied on machines that block
                        incoming traffic and only allow outbound.
                        The connection to your listening server is given by
                        -R/--remote addr:port and the connection to the
                        target machine via the positional arguments.
optional arguments:
  -e, --exec cmd        Execute shell command. Only for connect or listen mode.
  -C, --crlf lf         Specify, 'lf', 'crlf' or 'cr' to always force replacing
                        line endings for input and outout accordingly. Specify
                        'no' to completely remove any line feeds. By default
                        it will not replace anything and takes what is entered
                        (usually CRLF on Windows, LF on Linux and some times
                        CR on MacOS).
  -n, --nodns           Do not resolve DNS.
  --send-on-eof         Buffer data received on stdin until EOF and send
                        everything in one chunk.
  --no-shutdown         Do not shutdown into half-duplex mode.
                        If this option is passed, pwncat won't invoke shutdown
                        on a socket after seeing EOF on stdin. This is provided
                        for backward-compatibility with OpenBSD netcat, which
                        exhibits this behavior.
  -v, --verbose         Be verbose and print info to stderr. Use -v, -vv, -vvv
                        or -vvvv for more verbosity. The server performance will
                        decrease drastically if you use more than three times.
  --info type           Show additional info about sockets, IPv4/6 or TCP opts
                        applied to the current socket connection. Valid
                        parameter are 'sock', 'ipv4', 'ipv6', 'tcp' or 'all'.
                        Note, you must at least be in INFO verbose mode in order
                        to see them (-vv).
  -c, --color str       Colored log output. Specify 'always', 'never' or 'auto'.
                        In 'auto' mode, color is displayed as long as the output
                        goes to a terminal. If it is piped into a file, color
                        will automatically be disabled. This mode also disables
                        color on Windows by default. (default: auto)
  --safe-word str       All modes:
                        If pwncat is started with this argument, it will shut
                        down as soon as it receives the specified string. The
                        --keep-open (server) or --reconn (client) options will
                        be ignored and it won't listen again or reconnect to you.
                        Use a very unique string to not have it shut down
                        accidentally by other input.
protocol arguments:
  -4                    Only Use IPv4 (default: IPv4 and IPv6 dualstack).
  -6                    Only Use IPv6 (default: IPv4 and IPv6 dualstack).
  -u, --udp             Use UDP for the connection instead of TCP.
  -T, --tos str         Specifies IP Type of Service (ToS) for the connection.
                        Valid values are the tokens 'mincost', 'lowcost',
                        'reliability', 'throughput' or 'lowdelay'.
  --http                Connect / Listen mode (TCP and UDP):
                        Hide traffic in http packets to fool Firewalls/IDS/IPS.
  --https               Connect / Listen mode (TCP and UDP):
                        Hide traffic in https packets to fool Firewalls/IDS/IPS.
  -H, --header [str ...]
                        Add HTTP headers to your request when using --http(s).
command & control arguments:
  --self-inject cmd:host:port[s]
                        Listen mode (TCP only):
                        If you are about to inject a reverse shell onto the
                        victim machine (via php, bash, nc, ncat or similar),
                        start your listening server with this argument.
                        This will then (as soon as the reverse shell connects)
                        automatically deploy and background-run an unbreakable
                        pwncat reverse shell onto the victim machine which then
                        also connects back to you with specified arguments.
                        Example: '--self-inject /bin/bash:10.0.0.1:4444'
                        It is also possible to launch multiple reverse shells by
                        specifying multiple ports.
                        Via list:  --self-inject /bin/sh:10.0.0.1:4444,4445,4446
                        Via range: --self-inject /bin/sh:10.0.0.1:4444-4446
                        Via incr:  --self-inject /bin/sh:10.0.0.1:4444+2
                        Note: this is currently an experimental feature and does
                        not work on Windows remote hosts yet.
pwncat scripting engine:
  --script-send file    All modes (TCP and UDP):
                        A Python scripting engine to define your own custom
                        transformer function which will be executed before
                        sending data to a remote endpoint. Your file must
                        contain the exact following function which will:
                        be applied as the transformer:
                        def transform(data, pse):
                            # NOTE: the function name must be 'transform'
                            # NOTE: the function param name must be 'data'
                            # NOTE: indentation must be 4 spaces
                            # ... your transformations goes here
                            return data
                        You can also define as many custom functions or classes
                        within this file, but ensure to prefix them uniquely to
                        not collide with pwncat's function or classes, as the
                        file will be called with exec().
  --script-recv file    All modes (TCP and UDP):
                        A Python scripting engine to define your own custom
                        transformer function which will be executed after
                        receiving data from a remote endpoint. Your file must
                        contain the exact following function which will:
                        be applied as the transformer:
                        def transform(data, pse):
                            # NOTE: the function name must be 'transform'
                            # NOTE: the function param name must be 'data'
                            # NOTE: indentation must be 4 spaces
                            # ... your transformations goes here
                            return data
                        You can also define as many custom functions or classes
                        within this file, but ensure to prefix them uniquely to
                        not collide with pwncat's function or classes, as the
                        file will be called with exec().
zero-i/o mode arguments:
  --banner              Zero-I/O (TCP and UDP):
                        Try banner grabbing during port scan.
listen mode arguments:
  -k, --keep-open       Listen mode (TCP only):
                        Re-accept new clients in listen mode after a client has
                        disconnected or the connection is interrupted otherwise.
                        (default: server will quit after connection is gone)
  --rebind [x]          Listen mode (TCP and UDP):
                        If the server is unable to bind, it will re-initialize
                        itself x many times before giving up. Omit the
                        quantifier to rebind endlessly or specify a positive
                        integer for how many times to rebind before giving up.
                        See --rebind-robin for an interesting use-case.
                        (default: fail after first unsuccessful try).
  --rebind-wait s       Listen mode (TCP and UDP):
                        Wait x seconds between re-initialization. (default: 1)
  --rebind-robin port   Listen mode (TCP and UDP):
                        If the server is unable to initialize (e.g: cannot bind
                        and --rebind is specified, it it will shuffle ports in
                        round-robin mode to bind to.
                        Use comma separated string such as '80,81,82,83', a range
                        of ports '80-83' or an increment '80+3'.
                        Set --rebind to at least the number of ports to probe +1
                        This option requires --rebind to be specified.
connect mode arguments:
  --source-addr addr    Specify source bind IP address for connect mode.
  --source-port port    Specify source bind port for connect mode.
  --reconn [x]          Connect mode (TCP and UDP):
                        If the remote server is not reachable or the connection
                        is interrupted, the client will connect again x many
                        times before giving up. Omit the quantifier to retry
                        endlessly or specify a positive integer for how many
                        times to retry before giving up.
                        (default: quit if the remote is not available or the
                        connection was interrupted)
                        This might be handy for stable TCP reverse shells ;-)
                        Note on UDP:
                        By default UDP does not know if it is connected, so
                        it will stop at the first port and assume it has a
                        connection. Consider using --udp-sconnect with this
                        option to make UDP aware of a successful connection.
  --reconn-wait s       Connect mode (TCP and UDP):
                        Wait x seconds between re-connects. (default: 1)
  --reconn-robin port   Connect mode (TCP and UDP):
                        If the remote server is not reachable or the connection
                        is interrupted and --reconn is specified, the client
                        will shuffle ports in round-robin mode to connect to.
                        Use comma separated string such as '80,81,82,83', a range
                        of ports '80-83' or an increment '80+3'.
                        Set --reconn to at least the number of ports to probe +1
                        This helps reverse shell to evade intrusiona prevention
                        systems that will cut your connection and block the
                        outbound port.
                        This is also useful in Connect or Zero-I/O mode to
                        figure out what outbound ports are allowed.
  --ping-init           Connect mode (TCP and UDP):
                        UDP is a stateless protocol unlike TCP, so no hand-
                        shake communication takes place and the client just
                        sends data to a server without being "accepted" by
                        the server first.
                        This means a server waiting for an UDP client to
                        connect to, is unable to send any data to the client,
                        before the client hasn't send data first. The server
                        simply doesn't know the IP address before an initial
```

## 4. 实践清单

按顺序做完这五步，就能把工具从「装上」推进到「会用」：

- [ ] **1.** **装好并确认版本** —— `sudo apt install pwncat`，再执行 `pwncat --version` 2>/dev/null || `pwncat -V`
- [ ] **2.** **读官方帮助** —— `pwncat -h`，需要细节时 `man pwncat`
- [ ] **3.** **在自有靶场跑最小用例** —— 用 `pwncat -h` 里最简单的那个子命令试一次
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/pwncat/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/pwncat/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/pwncat/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
