# socat

> Multipurpose relay for bidirectional data transfer Socat (for SOcket CAT) establishes two bidirectional byte streams and transfers data between them. Data channels may be files, pipes, devices (terminal or modem, etc.), or sockets (Unix, I…

> **功能分类**：Web 应用 ｜ **Kali 包**：`socat` ｜ **官方文档**：<https://www.kali.org/tools/socat/>

## 1. 安装

```bash
sudo apt update
sudo apt install socat
```

| 项目 | 内容 |
|------|------|
| 版本 | 1.8.1.3 |
| 架构 | linux-any |
| 可执行命令 | `socat`、`filan`、`procan`、`socat-broker.sh`、`socat-chain.sh`、`socat-mux.sh`、`socat1` |
| 依赖 | `libc6`、`libssl3t64`、`libwrap0`、`filan` |
| 安装体积 | 1.82 MB |
| 官网 | <http://www.dest-unreach.org/socat/> |
| 包追踪 | <https://pkg.kali.org/pkg/socat> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
socat -h          # 查看用法
man socat         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 7 个可执行命令，下面是官方页面内嵌的帮助原文。

### `filan`

> 官方示例调用：`filan -h`

```text
root@kali:~# filan -h
filan by Gerhard Rieger and contributors - see http://www.dest-unreach.org/socat/
Analyze file descriptors of the process
Usage:
filan [options]
   options:
      -?|-h          print this help text
      -d             increase verbosity (use up to 4 times)
      -i<fdnum>      only analyze this fd
      -n<fdnum>      analyze all fds from 0 up to fdnum-1 (default: 1024)
      -s             simple output with just type and socket address or path
      -S             like -s but improved format and contents
      -f<filename>   analyze file system entry
      -T<seconds>    wait before analyzing, useful to connect with debugger
      -r             raw output for time stamps and rdev
      -L             follow symbolic links instead of showing their properties
      -W             after printing FDs info, wait and reprint info on SIGWINCH
      -o<filename>   output goes to filename, that can be:
                     a regular file name, the output goes to that
                     +<filedes> , output goes to the file descriptor (which must be open writable)
                     the 3 special names stdin stdout and stderr
```

### `procan`

> 官方示例调用：`procan -h`

```text
root@kali:~# procan -h
procan by Gerhard Rieger and contributors - send bug reports to
[email protected]
Analyze system parameters of process
Usage:
procan [options]
   options:
      -V     print version information to stdout, and exit
      -?|-h  print a help text describing command line options
      -c     print values of compile time C defines
```

### `socat`

> 官方示例调用：`socat -h`

```text
root@kali:~# socat -h
socat by Gerhard Rieger and contributors - see www.dest-unreach.org
Usage:
socat [options] <bi-address> <bi-address>
   options (general command line options):
      -V     print version and feature information to stdout, and exit
      -h|-?  print a help text describing command line options and addresses
      -hh    like -h, plus a list of all common address option names
      -hhh   like -hh, plus a list of all available address option names
      -d[ddd]        increase verbosity (use up to 4 times; 2 are recommended)
      -d0|1|2|3|4    set verbosity level (0: Errors; 4 all including Debug)
      -D     analyze file descriptors before loop
      --experimental enable experimental features
      --statistics   output transfer statistics on exit
      -ly[facility]  log to syslog, using facility (default is daemon)
      -lf<logfile>   log to file
      -ls            log to stderr (default if no other log)
      -lm[facility]  mixed log mode (stderr during initialization, then syslog)
      -lp<progname>  set the program name used for logging and vars
      -lu            use microseconds for logging timestamps
      -lh            add hostname to log messages
      -v     verbose text dump of data traffic
      -x     verbose hexadecimal dump of data traffic
      -r <file>      raw dump of data flowing from left to right
      -R <file>      raw dump of data flowing from right to left
      -b<size_t>     set data buffer size (8192)
      -s     sloppy (continue on error)
      -S<sigmask>    log these signals, override default
      -t<timeout>    wait seconds before closing second channel
      -T<timeout>    total inactivity timeout in seconds
      -u     unidirectional mode (left to right)
      -U     unidirectional mode (right to left)
      -g     do not check option groups
      -L <lockfile>  try to obtain lock, or fail
      -W <lockfile>  try to obtain lock, or wait
      -0     do not prefer an IP version
      -4     prefer IPv4 if version is not explicitly specified
      -6     prefer IPv6 if version is not explicitly specified
   bi-address:  /* is an address that may act both as data sync and source */
      <single-address>
      <single-address>!!<single-address>
   single-address:
      <address-head>[,<opts>]
   address-head:
      ABSTRACT-CLIENT:<filename>		groups=FD,SOCKET,RETRY,UNIX
      ABSTRACT-CONNECT:<filename>		groups=FD,SOCKET,RETRY,UNIX
      ABSTRACT-LISTEN:<filename>		groups=FD,SOCKET,LISTEN,CHILD,RETRY,UNIX
      ABSTRACT-RECV:<filename>			groups=FD,SOCKET,RETRY,UNIX
      ABSTRACT-RECVFROM:<filename>		groups=FD,SOCKET,CHILD,RETRY,UNIX
      ABSTRACT-SENDTO:<filename>		groups=FD,SOCKET,RETRY,UNIX
      ACCEPT-FD:<fdnum>				groups=FD,SOCKET,CHILD,RETRY,RANGE,UNIX,IP4,IP6,UDP,TCP,SCTP,DCCP,UDPLITE
      CREATE:<filename>				groups=FD,REG,NAMED
      DCCP-CONNECT:<host>:<port>		groups=FD,SOCKET,CHILD,RETRY,IP4,IP6,DCCP
      DCCP-LISTEN:<port>			groups=FD,SOCKET,LISTEN,CHILD,RETRY,RANGE,IP4,IP6,DCCP
      DCCP4-CONNECT:<host>:<port>		groups=FD,SOCKET,CHILD,RETRY,IP4,DCCP
      DCCP4-LISTEN:<port>			groups=FD,SOCKET,LISTEN,CHILD,RETRY,RANGE,IP4,DCCP
      DCCP6-CONNECT:<host>:<port>		groups=FD,SOCKET,CHILD,RETRY,IP6,DCCP
      DCCP6-LISTEN:<port>			groups=FD,SOCKET,LISTEN,CHILD,RETRY,RANGE,IP6,DCCP
      EXEC:<command-line>			groups=FD,FIFO,SOCKET,EXEC,FORK,TERMIOS,PTY,PARENT,UNIX
      FD:<fdnum>				groups=FD,FIFO,CHR,BLK,REG,SOCKET,TERMIOS,UNIX,IP4,IP6,UDP,TCP,SCTP,DCCP,UDPLITE
      GOPEN:<filename>				groups=FD,FIFO,CHR,BLK,REG,SOCKET,NAMED,OPEN,TERMIOS,UNIX
      INTERFACE:<interface>			groups=FD,SOCKET,INTERFACE
      IP-DATAGRAM:<host>:<protocol>		groups=FD,SOCKET,RANGE,IP4,IP6
      IP-RECV:<protocol>			groups=FD,SOCKET,RANGE,IP4,IP6
      IP-RECVFROM:<protocol>			groups=FD,SOCKET,CHILD,RANGE,IP4,IP6
      IP-SENDTO:<host>:<protocol>		groups=FD,SOCKET,IP4,IP6
      IP4-DATAGRAM:<host>:<protocol>		groups=FD,SOCKET,RANGE,IP4
      IP4-RECV:<protocol>			groups=FD,SOCKET,RANGE,IP4
      IP4-RECVFROM:<protocol>			groups=FD,SOCKET,CHILD,RANGE,IP4
      IP4-SENDTO:<host>:<protocol>		groups=FD,SOCKET,IP4
      IP6-DATAGRAM:<host>:<protocol>		groups=FD,SOCKET,RANGE,IP6
      IP6-RECV:<protocol>			groups=FD,SOCKET,RANGE,IP6
      IP6-RECVFROM:<protocol>			groups=FD,SOCKET,CHILD,RANGE,IP6
      IP6-SENDTO:<host>:<protocol>		groups=FD,SOCKET,IP6
      OPEN:<filename>				groups=FD,FIFO,CHR,BLK,REG,NAMED,OPEN,TERMIOS
      OPENSSL:<host>:<port>			groups=FD,SOCKET,CHILD,RETRY,IP4,IP6,TCP,OPENSSL
      OPENSSL-DTLS-CLIENT:<host>:<port>		groups=FD,SOCKET,CHILD,RETRY,IP4,IP6,UDP,OPENSSL
      OPENSSL-DTLS-SERVER:<port>		groups=FD,SOCKET,LISTEN,CHILD,RETRY,RANGE,IP4,IP6,UDP,OPENSSL
      OPENSSL-LISTEN:<port>			groups=FD,SOCKET,LISTEN,CHILD,RETRY,RANGE,IP4,IP6,TCP,OPENSSL
      PIPE[:<filename>]				groups=FD,FIFO,NAMED,OPEN
      POSIXMQ-BIDIRECTIONAL:<mqname>		groups=FD,NAMED,OPEN,RETRY,POSIXMQ
      POSIXMQ-READ:<mqname>			groups=FD,NAMED,OPEN,RETRY,POSIXMQ
      POSIXMQ-RECEIVE:<mqname>			groups=FD,NAMED,OPEN,CHILD,RETRY,POSIXMQ
      POSIXMQ-SEND:<mqname>			groups=FD,NAMED,OPEN,CHILD,RETRY,POSIXMQ
      POSIXMQ-WRITE:<mqname>			groups=FD,NAMED,OPEN,CHILD,RETRY,POSIXMQ
      PROXY:<proxy-server>:<host>:<port>	groups=FD,SOCKET,CHILD,RETRY,IP4,IP6,TCP,HTTP
      PTY					groups=FD,NAMED,TERMIOS,PTY
      SCTP-CONNECT:<host>:<port>		groups=FD,SOCKET,CHILD,RETRY,IP4,IP6,SCTP
      SCTP-LISTEN:<port>			groups=FD,SOCKET,LISTEN,CHILD,RETRY,RANGE,IP4,IP6,SCTP
      SCTP4-CONNECT:<host>:<port>		groups=FD,SOCKET,CHILD,RETRY,IP4,SCTP
      SCTP4-LISTEN:<port>			groups=FD,SOCKET,LISTEN,CHILD,RETRY,RANGE,IP4,SCTP
      SCTP6-CONNECT:<host>:<port>		groups=FD,SOCKET,CHILD,RETRY,IP6,SCTP
      SCTP6-LISTEN:<port>			groups=FD,SOCKET,LISTEN,CHILD,RETRY,RANGE,IP6,SCTP
      SHELL[:<shell-command>]			groups=FD,FIFO,SOCKET,EXEC,FORK,SHELL,TERMIOS,PTY,PARENT,UNIX
      SOCKET-CONNECT:<domain>:<protocol>:<remote-address>	groups=FD,SOCKET,CHILD,RETRY
      SOCKET-DATAGRAM:<domain>:<type>:<protocol>:<remote-address>	groups=FD,SOCKET,RANGE
      SOCKET-LISTEN:<domain>:<protocol>:<local-address>	groups=FD,SOCKET,LISTEN,CHILD,RETRY,RANGE
      SOCKET-RECV:<domain>:<type>:<protocol>:<local-address>	groups=FD,SOCKET,RANGE
      SOCKET-RECVFROM:<domain>:<type>:<protocol>:<local-address>	groups=FD,SOCKET,CHILD,RANGE
      SOCKET-SENDTO:<domain>:<type>:<protocol>:<remote-address>	groups=FD,SOCKET
      SOCKETPAIR:<filename>			groups=FD,SOCKET
      SOCKS4:<socks-server>:<host>:<port>	groups=FD,SOCKET,CHILD,RETRY,IP4,IP6,TCP,SOCKS
      SOCKS4A:<socks-server>:<host>:<port>	groups=FD,SOCKET,CHILD,RETRY,IP4,IP6,TCP,SOCKS
      SOCKS5-CONNECT:<socks-server>[:<socks-port>]:<target-host>:<target-port>	groups=FD,SOCKET,CHILD,RETRY,IP4,IP6,TCP,SOCKS
      SOCKS5-LISTEN:<socks-server>[:<socks-port>]:<listen-host>:<listen-port>	groups=FD,SOCKET,CHILD,RETRY,IP4,IP6,TCP,SOCKS
      STALL					groups=FD,FIFO
      STDERR					groups=FD,FIFO,CHR,BLK,REG,SOCKET,TERMIOS,UNIX,IP4,IP6,UDP,TCP,SCTP,DCCP,UDPLITE
      STDIN					groups=FD,FIFO,CHR,BLK,REG,SOCKET,TERMIOS,UNIX,IP4,IP6,UDP,TCP,SCTP,DCCP,UDPLITE
      STDIO					groups=FD,FIFO,CHR,BLK,REG,SOCKET,TERMIOS,UNIX,IP4,IP6,UDP,TCP,SCTP,DCCP,UDPLITE
      STDOUT					groups=FD,FIFO,CHR,BLK,REG,SOCKET,TERMIOS,UNIX,IP4,IP6,UDP,TCP,SCTP,DCCP,UDPLITE
      SYSTEM:<shell-command>			groups=FD,FIFO,SOCKET,EXEC,FORK,TERMIOS,PTY,PARENT,UNIX
      TCP-CONNECT:<host>:<port>			groups=FD,SOCKET,CHILD,RETRY,IP4,IP6,TCP
      TCP-LISTEN:<port>				groups=FD,SOCKET,LISTEN,CHILD,RETRY,RANGE,IP4,IP6,TCP
      TCP4-CONNECT:<host>:<port>		groups=FD,SOCKET,CHILD,RETRY,IP4,TCP
      TCP4-LISTEN:<port>			groups=FD,SOCKET,LISTEN,CHILD,RETRY,RANGE,IP4,TCP
      TCP6-CONNECT:<host>:<port>		groups=FD,SOCKET,CHILD,RETRY,IP6,TCP
      TCP6-LISTEN:<port>			groups=FD,SOCKET,LISTEN,CHILD,RETRY,RANGE,IP6,TCP
      TEXT:<string>				groups=FD,FIFO
      TUN[:<ip-addr>/<bits>]			groups=FD,CHR,OPEN,INTERFACE
      UDP-CONNECT:<host>:<port>			groups=FD,SOCKET,IP4,IP6,UDP
      UDP-DATAGRAM:<host>:<port>		groups=FD,SOCKET,RANGE,IP4,IP6,UDP
      UDP-LISTEN:<port>				groups=FD,SOCKET,LISTEN,CHILD,RANGE,IP4,IP6,UDP
      UDP-RECV:<port>				groups=FD,SOCKET,RANGE,IP4,IP6,UDP
      UDP-RECVFROM:<port>			groups=FD,SOCKET,CHILD,RANGE,IP4,IP6,UDP
      UDP-SENDTO:<host>:<port>			groups=FD,SOCKET,IP4,IP6,UDP
      UDP4-CONNECT:<host>:<port>		groups=FD,SOCKET,IP4,UDP
      UDP4-DATAGRAM:<host>:<port>		groups=FD,SOCKET,RANGE,IP4,UDP
      UDP4-LISTEN:<port>			groups=FD,SOCKET,LISTEN,CHILD,RANGE,IP4,UDP
      UDP4-RECV:<port>				groups=FD,SOCKET,RANGE,IP4,UDP
      UDP4-RECVFROM:<port>			groups=FD,SOCKET,CHILD,RANGE,IP4,UDP
      UDP4-SENDTO:<host>:<port>			groups=FD,SOCKET,IP4,UDP
      UDP6-CONNECT:<host>:<port>		groups=FD,SOCKET,IP6,UDP
      UDP6-DATAGRAM:<host>:<port>		groups=FD,SOCKET,RANGE,IP6,UDP
      UDP6-LISTEN:<port>			groups=FD,SOCKET,LISTEN,CHILD,RANGE,IP6,UDP
      UDP6-RECV:<port>				groups=FD,SOCKET,RANGE,IP6,UDP
      UDP6-RECVFROM:<port>			groups=FD,SOCKET,CHILD,RANGE,IP6,UDP
      UDP6-SENDTO:<host>:<port>			groups=FD,SOCKET,IP6,UDP
      UDPLITE-CONNECT:<host>:<port>		groups=FD,SOCKET,IP4,IP6,UDP,UDPLITE
      UDPLITE-DATAGRAM:<host>:<port>		groups=FD,SOCKET,RANGE,IP4,IP6,UDP,UDPLITE
      UDPLITE-LISTEN:<port>			groups=FD,SOCKET,LISTEN,CHILD,RANGE,IP4,IP6,UDP,UDPLITE
      UDPLITE-RECV:<port>			groups=FD,SOCKET,RANGE,IP4,IP6,UDP,UDPLITE
      UDPLITE-RECVFROM:<port>			groups=FD,SOCKET,CHILD,RANGE,IP4,IP6,UDP,UDPLITE
      UDPLITE-SENDTO:<host>:<port>		groups=FD,SOCKET,IP4,IP6,UDP,UDPLITE
      UDPLITE4-CONNECT:<host>:<port>		groups=FD,SOCKET,IP4,UDP,UDPLITE
      UDPLITE4-DATAGRAM:<remote-address>:<port>	groups=FD,SOCKET,RANGE,IP4,UDP,UDPLITE
      UDPLITE4-LISTEN:<port>			groups=FD,SOCKET,LISTEN,CHILD,RANGE,IP4,UDP,UDPLITE
      UDPLITE4-RECV:<port>			groups=FD,SOCKET,RANGE,IP4,UDP,UDPLITE
      UDPLITE4-RECVFROM:<host>:<port>		groups=FD,SOCKET,CHILD,RANGE,IP4,UDP,UDPLITE
      UDPLITE4-SENDTO:<host>:<port>		groups=FD,SOCKET,IP4,UDP,UDPLITE
      UDPLITE6-CONNECT:<host>:<port>		groups=FD,SOCKET,IP6,UDP,UDPLITE
      UDPLITE6-DATAGRAM:<host>:<port>		groups=FD,SOCKET,RANGE,IP6,UDP,UDPLITE
      UDPLITE6-LISTEN:<port>			groups=FD,SOCKET,LISTEN,CHILD,RANGE,IP6,UDP,UDPLITE
      UDPLITE6-RECV:<port>			groups=FD,SOCKET,RANGE,IP6,UDP,UDPLITE
      UDPLITE6-RECVFROM:<port>			groups=FD,SOCKET,CHILD,RANGE,IP6,UDP,UDPLITE
      UDPLITE6-SENDTO:<host>:<port>		groups=FD,SOCKET,IP6,UDP,UDPLITE
      UNIX-CLIENT:<filename>			groups=FD,SOCKET,NAMED,RETRY,UNIX
      UNIX-CONNECT:<filename>			groups=FD,SOCKET,NAMED,RETRY,UNIX
      UNIX-LISTEN:<filename>			groups=FD,SOCKET,NAMED,LISTEN,CHILD,RETRY,UNIX
      UNIX-RECV:<filename>			groups=FD,SOCKET,NAMED,RETRY,UNIX
      UNIX-RECVFROM:<filename>			groups=FD,SOCKET,NAMED,CHILD,RETRY,UNIX
      UNIX-SENDTO:<filename>			groups=FD,SOCKET,NAMED,RETRY,UNIX
      VSOCK-CONNECT:<cid>:<port>		groups=FD,SOCKET,CHILD,RETRY
      VSOCK-LISTEN:<port>			groups=FD,SOCKET,LISTEN,CHILD,RETRY
```

### `socat-broker.sh`

> 官方示例调用：`socat-broker.sh -h`

```text
root@kali:~# socat-broker.sh -h
Usage: /usr/bin/socat-broker.sh <options> <listener>
	<listener> is a passive address like TCP4-L or SSL-L
	<options>:
		-d*  -S  -t <timeout>  -T <timeout> 	are passed to socat
		-V	Shows executed Socat commands and some infos
For example:
	/usr/bin/socat-broker.sh \
		TCP4-L:1234
Then connect with clients to port 1234
Data sent by any client is forwarded to all other clients
```

### `socat-chain.sh`

> 官方示例调用：`socat-chain.sh -h`

```text
root@kali:~# socat-chain.sh -h
Usage: /usr/bin/socat-chain.sh <options> <address1> <address2> <address3>
	<address1> is typically a passive (listening) address like
		TCP-L:1234
	<address2> must be one of OPENSSL, PROXY, SOCK4, SOCKS4A, or SOCKS5,
		or SSL-L (passive/listening)
		Given server hostname and port are ignored and replaced by internal
		communication point
	<address3> is typically a client address with protocol like OPENSSL
	<options>:
		-d*  -S <sigmask>  -t <timeout>  -T <timeout> 	are passed to socat
		-V	Shows executed Socat commands and some infos
Example to drive SOCKS over TLS:
	/usr/bin/socat-chain.sh \
		TCP4-L:1234,reuseaddr,fork \
		SOCKS::<server>:<port> \
		OPENSSL:10.2.3.4:12345,cafile=...
	Clients that connect to port 1234 will be forwarded to <server>:<port> using socks
	over TLS
```

### `socat-mux.sh`

> 官方示例调用：`socat-mux.sh -h`

```text
root@kali:~# socat-mux.sh -h
Usage: /usr/bin/socat-mux.sh <options> <listener> <target>
Example:
    /usr/bin/socat-mux.sh TCP4-L:1234,reuseaddr,fork TCP:10.2.3.4:12345
Clients may connect to port 1234; data sent by any client is forwarded to 10.2.3.4,
data provided by 10.2.3.4 is sent to ALL clients
    <options>:
	-h	Show this help text and exit
	-V	Shows executed Socat commands and some infos
	-q	Suppress most messages
	-d*	Options beginning with -d are passed to Socat processes
	-l*	Options beginning with -l are passed to Socat processes
	-b|-S|-t|-T|-l <arg>	These options are passed to Socat processes
```

### `socat1`

> 官方示例调用：`socat1 -h`

```text
root@kali:~# socat1 -h
socat by Gerhard Rieger and contributors - see www.dest-unreach.org
Usage:
socat [options] <bi-address> <bi-address>
   options (general command line options):
      -V     print version and feature information to stdout, and exit
      -h|-?  print a help text describing command line options and addresses
      -hh    like -h, plus a list of all common address option names
      -hhh   like -hh, plus a list of all available address option names
      -d[ddd]        increase verbosity (use up to 4 times; 2 are recommended)
      -d0|1|2|3|4    set verbosity level (0: Errors; 4 all including Debug)
      -D     analyze file descriptors before loop
      --experimental enable experimental features
      --statistics   output transfer statistics on exit
      -ly[facility]  log to syslog, using facility (default is daemon)
      -lf<logfile>   log to file
      -ls            log to stderr (default if no other log)
      -lm[facility]  mixed log mode (stderr during initialization, then syslog)
      -lp<progname>  set the program name used for logging and vars
      -lu            use microseconds for logging timestamps
      -lh            add hostname to log messages
      -v     verbose text dump of data traffic
      -x     verbose hexadecimal dump of data traffic
      -r <file>      raw dump of data flowing from left to right
      -R <file>      raw dump of data flowing from right to left
      -b<size_t>     set data buffer size (8192)
      -s     sloppy (continue on error)
      -S<sigmask>    log these signals, override default
      -t<timeout>    wait seconds before closing second channel
      -T<timeout>    total inactivity timeout in seconds
      -u     unidirectional mode (left to right)
      -U     unidirectional mode (right to left)
      -g     do not check option groups
      -L <lockfile>  try to obtain lock, or fail
      -W <lockfile>  try to obtain lock, or wait
      -0     do not prefer an IP version
      -4     prefer IPv4 if version is not explicitly specified
      -6     prefer IPv6 if version is not explicitly specified
   bi-address:  /* is an address that may act both as data sync and source */
      <single-address>
      <single-address>!!<single-address>
   single-address:
      <address-head>[,<opts>]
   address-head:
      ABSTRACT-CLIENT:<filename>		groups=FD,SOCKET,RETRY,UNIX
      ABSTRACT-CONNECT:<filename>		groups=FD,SOCKET,RETRY,UNIX
      ABSTRACT-LISTEN:<filename>		groups=FD,SOCKET,LISTEN,CHILD,RETRY,UNIX
      ABSTRACT-RECV:<filename>			groups=FD,SOCKET,RETRY,UNIX
      ABSTRACT-RECVFROM:<filename>		groups=FD,SOCKET,CHILD,RETRY,UNIX
      ABSTRACT-SENDTO:<filename>		groups=FD,SOCKET,RETRY,UNIX
      ACCEPT-FD:<fdnum>				groups=FD,SOCKET,CHILD,RETRY,RANGE,UNIX,IP4,IP6,UDP,TCP,SCTP,DCCP,UDPLITE
      CREATE:<filename>				groups=FD,REG,NAMED
      DCCP-CONNECT:<host>:<port>		groups=FD,SOCKET,CHILD,RETRY,IP4,IP6,DCCP
      DCCP-LISTEN:<port>			groups=FD,SOCKET,LISTEN,CHILD,RETRY,RANGE,IP4,IP6,DCCP
      DCCP4-CONNECT:<host>:<port>		groups=FD,SOCKET,CHILD,RETRY,IP4,DCCP
      DCCP4-LISTEN:<port>			groups=FD,SOCKET,LISTEN,CHILD,RETRY,RANGE,IP4,DCCP
      DCCP6-CONNECT:<host>:<port>		groups=FD,SOCKET,CHILD,RETRY,IP6,DCCP
      DCCP6-LISTEN:<port>			groups=FD,SOCKET,LISTEN,CHILD,RETRY,RANGE,IP6,DCCP
      EXEC:<command-line>			groups=FD,FIFO,SOCKET,EXEC,FORK,TERMIOS,PTY,PARENT,UNIX
      FD:<fdnum>				groups=FD,FIFO,CHR,BLK,REG,SOCKET,TERMIOS,UNIX,IP4,IP6,UDP,TCP,SCTP,DCCP,UDPLITE
      GOPEN:<filename>				groups=FD,FIFO,CHR,BLK,REG,SOCKET,NAMED,OPEN,TERMIOS,UNIX
      INTERFACE:<interface>			groups=FD,SOCKET,INTERFACE
      IP-DATAGRAM:<host>:<protocol>		groups=FD,SOCKET,RANGE,IP4,IP6
      IP-RECV:<protocol>			groups=FD,SOCKET,RANGE,IP4,IP6
      IP-RECVFROM:<protocol>			groups=FD,SOCKET,CHILD,RANGE,IP4,IP6
      IP-SENDTO:<host>:<protocol>		groups=FD,SOCKET,IP4,IP6
      IP4-DATAGRAM:<host>:<protocol>		groups=FD,SOCKET,RANGE,IP4
      IP4-RECV:<protocol>			groups=FD,SOCKET,RANGE,IP4
      IP4-RECVFROM:<protocol>			groups=FD,SOCKET,CHILD,RANGE,IP4
      IP4-SENDTO:<host>:<protocol>		groups=FD,SOCKET,IP4
      IP6-DATAGRAM:<host>:<protocol>		groups=FD,SOCKET,RANGE,IP6
      IP6-RECV:<protocol>			groups=FD,SOCKET,RANGE,IP6
      IP6-RECVFROM:<protocol>			groups=FD,SOCKET,CHILD,RANGE,IP6
      IP6-SENDTO:<host>:<protocol>		groups=FD,SOCKET,IP6
      OPEN:<filename>				groups=FD,FIFO,CHR,BLK,REG,NAMED,OPEN,TERMIOS
      OPENSSL:<host>:<port>			groups=FD,SOCKET,CHILD,RETRY,IP4,IP6,TCP,OPENSSL
      OPENSSL-DTLS-CLIENT:<host>:<port>		groups=FD,SOCKET,CHILD,RETRY,IP4,IP6,UDP,OPENSSL
      OPENSSL-DTLS-SERVER:<port>		groups=FD,SOCKET,LISTEN,CHILD,RETRY,RANGE,IP4,IP6,UDP,OPENSSL
      OPENSSL-LISTEN:<port>			groups=FD,SOCKET,LISTEN,CHILD,RETRY,RANGE,IP4,IP6,TCP,OPENSSL
      PIPE[:<filename>]				groups=FD,FIFO,NAMED,OPEN
      POSIXMQ-BIDIRECTIONAL:<mqname>		groups=FD,NAMED,OPEN,RETRY,POSIXMQ
      POSIXMQ-READ:<mqname>			groups=FD,NAMED,OPEN,RETRY,POSIXMQ
      POSIXMQ-RECEIVE:<mqname>			groups=FD,NAMED,OPEN,CHILD,RETRY,POSIXMQ
      POSIXMQ-SEND:<mqname>			groups=FD,NAMED,OPEN,CHILD,RETRY,POSIXMQ
      POSIXMQ-WRITE:<mqname>			groups=FD,NAMED,OPEN,CHILD,RETRY,POSIXMQ
      PROXY:<proxy-server>:<host>:<port>	groups=FD,SOCKET,CHILD,RETRY,IP4,IP6,TCP,HTTP
      PTY					groups=FD,NAMED,TERMIOS,PTY
      SCTP-CONNECT:<host>:<port>		groups=FD,SOCKET,CHILD,RETRY,IP4,IP6,SCTP
      SCTP-LISTEN:<port>			groups=FD,SOCKET,LISTEN,CHILD,RETRY,RANGE,IP4,IP6,SCTP
      SCTP4-CONNECT:<host>:<port>		groups=FD,SOCKET,CHILD,RETRY,IP4,SCTP
      SCTP4-LISTEN:<port>			groups=FD,SOCKET,LISTEN,CHILD,RETRY,RANGE,IP4,SCTP
      SCTP6-CONNECT:<host>:<port>		groups=FD,SOCKET,CHILD,RETRY,IP6,SCTP
      SCTP6-LISTEN:<port>			groups=FD,SOCKET,LISTEN,CHILD,RETRY,RANGE,IP6,SCTP
      SHELL[:<shell-command>]			groups=FD,FIFO,SOCKET,EXEC,FORK,SHELL,TERMIOS,PTY,PARENT,UNIX
      SOCKET-CONNECT:<domain>:<protocol>:<remote-address>	groups=FD,SOCKET,CHILD,RETRY
      SOCKET-DATAGRAM:<domain>:<type>:<protocol>:<remote-address>	groups=FD,SOCKET,RANGE
      SOCKET-LISTEN:<domain>:<protocol>:<local-address>	groups=FD,SOCKET,LISTEN,CHILD,RETRY,RANGE
      SOCKET-RECV:<domain>:<type>:<protocol>:<local-address>	groups=FD,SOCKET,RANGE
      SOCKET-RECVFROM:<domain>:<type>:<protocol>:<local-address>	groups=FD,SOCKET,CHILD,RANGE
      SOCKET-SENDTO:<domain>:<type>:<protocol>:<remote-address>	groups=FD,SOCKET
      SOCKETPAIR:<filename>			groups=FD,SOCKET
      SOCKS4:<socks-server>:<host>:<port>	groups=FD,SOCKET,CHILD,RETRY,IP4,IP6,TCP,SOCKS
      SOCKS4A:<socks-server>:<host>:<port>	groups=FD,SOCKET,CHILD,RETRY,IP4,IP6,TCP,SOCKS
      SOCKS5-CONNECT:<socks-server>[:<socks-port>]:<target-host>:<target-port>	groups=FD,SOCKET,CHILD,RETRY,IP4,IP6,TCP,SOCKS
      SOCKS5-LISTEN:<socks-server>[:<socks-port>]:<listen-host>:<listen-port>	groups=FD,SOCKET,CHILD,RETRY,IP4,IP6,TCP,SOCKS
      STALL					groups=FD,FIFO
      STDERR					groups=FD,FIFO,CHR,BLK,REG,SOCKET,TERMIOS,UNIX,IP4,IP6,UDP,TCP,SCTP,DCCP,UDPLITE
      STDIN					groups=FD,FIFO,CHR,BLK,REG,SOCKET,TERMIOS,UNIX,IP4,IP6,UDP,TCP,SCTP,DCCP,UDPLITE
      STDIO					groups=FD,FIFO,CHR,BLK,REG,SOCKET,TERMIOS,UNIX,IP4,IP6,UDP,TCP,SCTP,DCCP,UDPLITE
      STDOUT					groups=FD,FIFO,CHR,BLK,REG,SOCKET,TERMIOS,UNIX,IP4,IP6,UDP,TCP,SCTP,DCCP,UDPLITE
      SYSTEM:<shell-command>			groups=FD,FIFO,SOCKET,EXEC,FORK,TERMIOS,PTY,PARENT,UNIX
      TCP-CONNECT:<host>:<port>			groups=FD,SOCKET,CHILD,RETRY,IP4,IP6,TCP
      TCP-LISTEN:<port>				groups=FD,SOCKET,LISTEN,CHILD,RETRY,RANGE,IP4,IP6,TCP
      TCP4-CONNECT:<host>:<port>		groups=FD,SOCKET,CHILD,RETRY,IP4,TCP
      TCP4-LISTEN:<port>			groups=FD,SOCKET,LISTEN,CHILD,RETRY,RANGE,IP4,TCP
      TCP6-CONNECT:<host>:<port>		groups=FD,SOCKET,CHILD,RETRY,IP6,TCP
      TCP6-LISTEN:<port>			groups=FD,SOCKET,LISTEN,CHILD,RETRY,RANGE,IP6,TCP
      TEXT:<string>				groups=FD,FIFO
      TUN[:<ip-addr>/<bits>]			groups=FD,CHR,OPEN,INTERFACE
      UDP-CONNECT:<host>:<port>			groups=FD,SOCKET,IP4,IP6,UDP
      UDP-DATAGRAM:<host>:<port>		groups=FD,SOCKET,RANGE,IP4,IP6,UDP
      UDP-LISTEN:<port>				groups=FD,SOCKET,LISTEN,CHILD,RANGE,IP4,IP6,UDP
      UDP-RECV:<port>				groups=FD,SOCKET,RANGE,IP4,IP6,UDP
      UDP-RECVFROM:<port>			groups=FD,SOCKET,CHILD,RANGE,IP4,IP6,UDP
      UDP-SENDTO:<host>:<port>			groups=FD,SOCKET,IP4,IP6,UDP
      UDP4-CONNECT:<host>:<port>		groups=FD,SOCKET,IP4,UDP
      UDP4-DATAGRAM:<host>:<port>		groups=FD,SOCKET,RANGE,IP4,UDP
      UDP4-LISTEN:<port>			groups=FD,SOCKET,LISTEN,CHILD,RANGE,IP4,UDP
      UDP4-RECV:<port>				groups=FD,SOCKET,RANGE,IP4,UDP
      UDP4-RECVFROM:<port>			groups=FD,SOCKET,CHILD,RANGE,IP4,UDP
      UDP4-SENDTO:<host>:<port>			groups=FD,SOCKET,IP4,UDP
      UDP6-CONNECT:<host>:<port>		groups=FD,SOCKET,IP6,UDP
      UDP6-DATAGRAM:<host>:<port>		groups=FD,SOCKET,RANGE,IP6,UDP
      UDP6-LISTEN:<port>			groups=FD,SOCKET,LISTEN,CHILD,RANGE,IP6,UDP
      UDP6-RECV:<port>				groups=FD,SOCKET,RANGE,IP6,UDP
      UDP6-RECVFROM:<port>			groups=FD,SOCKET,CHILD,RANGE,IP6,UDP
      UDP6-SENDTO:<host>:<port>			groups=FD,SOCKET,IP6,UDP
      UDPLITE-CONNECT:<host>:<port>		groups=FD,SOCKET,IP4,IP6,UDP,UDPLITE
      UDPLITE-DATAGRAM:<host>:<port>		groups=FD,SOCKET,RANGE,IP4,IP6,UDP,UDPLITE
      UDPLITE-LISTEN:<port>			groups=FD,SOCKET,LISTEN,CHILD,RANGE,IP4,IP6,UDP,UDPLITE
      UDPLITE-RECV:<port>			groups=FD,SOCKET,RANGE,IP4,IP6,UDP,UDPLITE
      UDPLITE-RECVFROM:<port>			groups=FD,SOCKET,CHILD,RANGE,IP4,IP6,UDP,UDPLITE
      UDPLITE-SENDTO:<host>:<port>		groups=FD,SOCKET,IP4,IP6,UDP,UDPLITE
      UDPLITE4-CONNECT:<host>:<port>		groups=FD,SOCKET,IP4,UDP,UDPLITE
      UDPLITE4-DATAGRAM:<remote-address>:<port>	groups=FD,SOCKET,RANGE,IP4,UDP,UDPLITE
      UDPLITE4-LISTEN:<port>			groups=FD,SOCKET,LISTEN,CHILD,RANGE,IP4,UDP,UDPLITE
      UDPLITE4-RECV:<port>			groups=FD,SOCKET,RANGE,IP4,UDP,UDPLITE
      UDPLITE4-RECVFROM:<host>:<port>		groups=FD,SOCKET,CHILD,RANGE,IP4,UDP,UDPLITE
      UDPLITE4-SENDTO:<host>:<port>		groups=FD,SOCKET,IP4,UDP,UDPLITE
      UDPLITE6-CONNECT:<host>:<port>		groups=FD,SOCKET,IP6,UDP,UDPLITE
      UDPLITE6-DATAGRAM:<host>:<port>		groups=FD,SOCKET,RANGE,IP6,UDP,UDPLITE
      UDPLITE6-LISTEN:<port>			groups=FD,SOCKET,LISTEN,CHILD,RANGE,IP6,UDP,UDPLITE
      UDPLITE6-RECV:<port>			groups=FD,SOCKET,RANGE,IP6,UDP,UDPLITE
      UDPLITE6-RECVFROM:<port>			groups=FD,SOCKET,CHILD,RANGE,IP6,UDP,UDPLITE
      UDPLITE6-SENDTO:<host>:<port>		groups=FD,SOCKET,IP6,UDP,UDPLITE
      UNIX-CLIENT:<filename>			groups=FD,SOCKET,NAMED,RETRY,UNIX
      UNIX-CONNECT:<filename>			groups=FD,SOCKET,NAMED,RETRY,UNIX
      UNIX-LISTEN:<filename>			groups=FD,SOCKET,NAMED,LISTEN,CHILD,RETRY,UNIX
      UNIX-RECV:<filename>			groups=FD,SOCKET,NAMED,RETRY,UNIX
      UNIX-RECVFROM:<filename>			groups=FD,SOCKET,NAMED,CHILD,RETRY,UNIX
      UNIX-SENDTO:<filename>			groups=FD,SOCKET,NAMED,RETRY,UNIX
      VSOCK-CONNECT:<cid>:<port>		groups=FD,SOCKET,CHILD,RETRY
      VSOCK-LISTEN:<port>			groups=FD,SOCKET,LISTEN,CHILD,RETRY
Learn more with
OffSec
Want to learn more about socat? get access to in-depth training and hands-on labs:
PEN-200: 19.2.3. Port Redirection and SSH Tunneling: Port Forwarding with Socat
PEN-200 course
Updated on: 2026-Aug-25
 Edit this page
sleuthkit
sploitscan
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install socat`，再执行 `socat --version` 2>/dev/null || `socat -V`
- [ ] **2.** **读官方帮助** —— `socat -h`，需要细节时 `man socat`
- [ ] **3.** **在自有靶场跑最小用例** —— 官方给出的调用形式是：`Usage:`
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/socat/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- **精讲教程**（含原理、参数详解、靶场实操与输出解读）：[socat](../../tools/tutorials/12-基础设施与C2/socat.md)
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/command-and-control.md`](../../tools/by-attack/command-and-control.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/socat/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/socat/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
