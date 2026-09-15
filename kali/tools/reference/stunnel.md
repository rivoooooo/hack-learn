# stunnel

> Universal SSL tunnel for network daemons The stunnel program is designed to work as SSL encryption wrapper between remote client and local (inetd-startable) or remote server. The concept is that having non-SSL aware daemons running on your…

> **功能分类**：Web 应用 ｜ **Kali 包**：`stunnel` ｜ **官方文档**：<https://www.kali.org/tools/stunnel/>

## 1. 安装

```bash
sudo apt update
sudo apt install stunnel
```

| 项目 | 内容 |
|------|------|
| 版本 | 5.80 |
| 架构 | any |
| 可执行命令 | `stunnel`、`stunnel3`、`stunnel4` |
| 依赖 | `libc6`、`libssl3t64`、`libsystemd0`、`libwrap0`、`netbase`、`openssl`、`perl` |
| 安装体积 | 575 KB |
| 官网 | <https://www.stunnel.org/> |
| 源码仓库 | <https://salsa.debian.org/debian/stunnel/> |
| 包追踪 | <https://pkg.kali.org/pkg/stunnel> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
stunnel -h          # 查看用法
man stunnel         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 3 个可执行命令，下面是官方页面内嵌的帮助原文。

### `man`

> 官方示例调用：`man stunnel`

```text
root@kali:~# man stunnel
STUNNEL(8)                     stunnel TLS Proxy                     STUNNEL(8)
NAME
     stunnel - TLS offloading and load-balancing proxy
SYNOPSIS
     * Unix: stunnel [FILE] | -fd N | -help | -version | -sockets | -options
     * WIN32:  stunnel  [  [ -install | -uninstall | -start | -stop | -reload |
       -reopen | -exit ] [-quiet] [FILE] ] | -help | -version | -sockets | -op-
       tions
DESCRIPTION
     The stunnel program is designed to work as TLS encryption wrapper  between
     remote clients and local (inetd-startable) or remote servers.  The concept
     is that having non-TLS aware daemons running on your system you can easily
     set them up to communicate with clients over secure TLS channels.
     stunnel  can  be used to add TLS functionality to commonly used Inetd dae-
     mons like POP-2, POP-3, and IMAP servers, to standalone daemons like NNTP,
     SMTP and HTTP, and in tunneling PPP over network sockets  without  changes
     to the source code.
     This  product  includes  cryptographic  software  written  by  Eric  Young
     (
[email protected]
)
OPTIONS
     * FILE
       Use specified configuration file
     * -fd N (Unix only)
       Read the config file from specified file descriptor
     * -help
       Print stunnel help menu
     * -version
       Print stunnel version and compile time defaults
     * -sockets
       Print default socket options
     * -options
       Print supported TLS options
     * -install (Windows NT and later only)
       Install NT Service
     * -uninstall (Windows NT and later only)
       Uninstall NT Service
     * -start (Windows NT and later only)
       Start NT Service
     * -stop (Windows NT and later only)
       Stop NT Service
     * -reload (Windows NT and later only)
       Reload the configuration file of the running NT Service
     * -reopen (Windows NT and later only)
       Reopen the log file of the running NT Service
     * -exit (Win32 only)
       Exit an already started stunnel
     * -quiet (Win32 only)
       Don't display any message boxes
CONFIGURATION FILE
     Each line of the configuration file can be either:
     * An empty line (ignored).
     * A comment starting with `;' (ignored).
     * An `option_name = option_value' pair.
     * `[service_name]' indicating a start of a service definition.
     An address parameter of an option may be either:
     * A port number.
     * A colon-separated pair of IP address (either IPv4, IPv6, or domain name)
       and port number.
     * A Unix socket path (Unix only).
   GLOBAL OPTIONS
     * chroot = DIRECTORY (Unix only)
       directory to chroot stunnel process
       chroot keeps stunnel in a chrooted jail.  CApath, CRLpath, pid and  exec
       are  located  inside the jail and the patches have to be relative to the
       directory specified with chroot.
       Several functions of the operating system also need their  files  to  be
       located within the chroot jail, e.g.:
       * Delayed  resolver  typically  needs  /etc/nsswitch.conf  and  /etc/re-
         solv.conf.
       * Local time in log files needs /etc/timezone.
       * Some other functions may need devices, e.g. /dev/zero or /dev/null.
     * compression = deflate | zlib | zstd | brotli
       select data compression algorithm
       default: no compression
       Data compression is available only for TLS 1.2  and  earlier.   Requires
       lowering securityLevel to 1 when compiled with OpenSSL 1.1.0 and later.
       The  zlib,  zstd,  and  brotli  algorithms  are  disabled in the default
       OpenSSL configuration.
       The zstd and brotli algorithms were added in OpenSSL 3.2.
       Data compression poses a risk in applications that allow an attacker  to
       inject chosen plaintext.
       Deflate is the standard compression method as described in RFC 1951.
       Warning:  TLS compression can enable plaintext-recovery attacks, such as
       CRIME, when attacker-controlled data is compressed together with  secret
       material.
     * debug = [FACILITY.]LEVEL
       debugging level
       Level  is one of the syslog level names or numbers emerg (0), alert (1),
       crit (2), err (3), warning (4), notice (5), info (6), or debug (7).  All
       logs for the specified level and all levels  numerically  less  than  it
       will be shown.
       The debug = debug (or the equivalent <debug = 7>) level produces for the
       most  verbose log output.  This logging level is only meant to be under-
       stood by stunnel developers, and not by users.  Please  either  use  the
       debug level when requested to do so by an stunnel developer, or when you
       intend to get confused.
       The default logging level is notice (5).
       The syslog `daemon' facility will be used unless a facility name is sup-
       plied.  (Facilities are not supported on Win32.)
       Case is ignored for both facilities and levels.
     * EGD = EGD_PATH (Unix only)
       path to Entropy Gathering Daemon socket
       Entropy Gathering Daemon socket to use to feed the OpenSSL random number
       generator.
     * engine = auto | ENGINE_ID
       select hardware or software cryptographic engine
       default: software-only cryptography
       See  Examples section for an engine configuration to use the certificate
       and the corresponding private key from a cryptographic device.
     * engineCtrl = COMMAND[:PARAMETER]
       control hardware engine
     * engineDefault = TASK_LIST
       set OpenSSL tasks delegated to the current engine
       The parameter specifies a comma-separated list of task to  be  delegated
       to the current engine.
       The  following  tasks may be available, if supported by the engine: ALL,
       RSA, DSA, ECDH, ECDSA, DH, RAND, CIPHERS,  DIGESTS,  PKEY,  PKEY_CRYPTO,
       PKEY_ASN1.
     * fips = yes | no
       enable or disable FIPS 140-2 mode.
       This option allows you to disable entering FIPS mode if stunnel was com-
       piled with FIPS 140-2 support.
       default: no (since version 5.00)
     * foreground = yes | quiet | no (Unix only)
       foreground mode
       Stay in foreground (don't fork).
       With  the yes parameter it also logs to stderr in addition to the desti-
       nations specified with syslog and output.
       default: background in daemon mode
     * iconActive = ICON_FILE (GUI only)
       GUI icon to be displayed when there are established connections
       On Windows platform the parameter should be an .ico  file  containing  a
       16x16 pixel image.
     * iconError = ICON_FILE (GUI only)
       GUI icon to be displayed when no valid configuration is loaded
       On  Windows  platform  the parameter should be an .ico file containing a
       16x16 pixel image.
     * iconIdle = ICON_FILE (GUI only)
       GUI icon to be displayed when there are no established connections
       On Windows platform the parameter should be an .ico  file  containing  a
       16x16 pixel image.
     * log = append | overwrite
       log file handling
       This  option  allows  you to choose whether the log file (specified with
       the output option) is appended or overwritten when opened or re-opened.
       default: append
     * output = FILE
       append log messages to a file
       /dev/stdout device can be used to send log messages to the standard out-
       put (for example to log them with daemontools splogger).
     * pid = FILE (Unix only)
       pid file location
       If the argument is empty, then no pid file will be created.
       pid path is relative to the chroot directory if specified.
     * provider = PROVIDER_ID
       Specifies the identifier of the provider to be used.  PROVIDER_ID  is  a
       unique   identifier   referring  to  a  specific  cryptographic  service
       provider.
       This option requires OpenSSL 3.0 or later.
     * providerParameter = PROVIDER_ID:PARAMETER=VALUE
       Sets a specific parameter for the given provider.   PROVIDER_ID  identi-
       fies  the  provider,  PARAMETER  is the parameter name, and VALUE is its
       value.  This option allows customization of the  selected  cryptographic
       service provider's configuration.
       This option requires OpenSSL 3.5 or later.
     * RNDbytes = BYTES
       bytes to read from random seed files
     * RNDfile = FILE
       path to file with random seed data
       The  OpenSSL library will use data from this file first to seed the ran-
       dom number generator.
     * RNDoverwrite = yes | no
       overwrite the random seed files with new random data
       default: yes
     * service = SERVICE (Unix only)
       stunnel service name
       The specified service name is used for syslog and as the inetd mode ser-
       vice name for TCP Wrappers.  While this option can technically be speci-
       fied in the service sections, it is only useful in global options.
       default: stunnel
     * setEnv = VAR_NAME=VALUE
       Change or add an environment variable for child processes.  If  VAR_NAME
       already  exists,  its  value  will be updated; otherwise, a new variable
       will be created.   This  modification  applies  only  to  spawned  child
       processes and does not affect the current environment.
     * syslog = yes | no (Unix only)
       enable logging via syslog
       default: yes
     * taskbar = yes | no (WIN32 only)
       enable the taskbar icon
       default: yes
   SERVICE-LEVEL OPTIONS
     Each  configuration section begins with a service name in square brackets.
     The service name is used for libwrap (TCP  Wrappers)  access  control  and
     lets you distinguish stunnel services in your log files.
     Note that if you wish to run stunnel in inetd mode (where it is provided a
     network  socket  by a server such as inetd, xinetd, or tcpserver) then you
     should read the section entitled INETD MODE below.
     * accept = [HOST:]PORT
       accept connections on specified address
       If no host specified, defaults to all IPv4 addresses for the local host.
       To listen on all IPv6 addresses use:
              accept = :::PORT
     * CAengine = ENGINE-SPECIFIC_CA_CERTIFICATE_IDENTIFIER
       load a trusted CA certificate from an engine
       The loaded CA certificates will be used with the verifyChain  and  veri-
       fyPeer options.
       Multiple CAengine options are allowed in a single service section.
       Currently supported engines: pkcs11, cng.
     * CApath = CA_DIRECTORY
       load trusted CA certificates from a directory
       The  loaded  CA certificates will be used with the verifyChain and veri-
       fyPeer options.  Note that the certificates in this directory should  be
       named  XXXXXXXX.0  where  XXXXXXXX  is the hash value of the DER encoded
       subject of the cert.
       This parameter can also be used  to  provide  the  root  CA  certificate
       needed to validate OCSP stapling in server mode.
```

### `stunnel3`

> 官方示例调用：`stunnel3 --help`

```text
root@kali:~# stunnel3 --help
/usr/bin/stunnel3 version [unknown] calling Getopt::Std::getopts (version 1.14 [paranoid]),
running under Perl version 5.42.2.
Usage: stunnel3 [-OPTIONS [-MORE_OPTIONS]] [--] [PROGRAM_ARG1 ...]
The following single-character options are accepted:
	With arguments: -D -O -o -C -p -v -a -A -t -N -u -n -E -R -B -I -d -s -g -P -r -L -l
	Boolean (without arguments): -c -T -W -f
Options may be merged together.  -- stops processing of options.
Space is not required between options and their arguments.
  [Now continuing due to backward compatibility and excessive paranoia.
   See 'perldoc Getopt::Std' about $Getopt::Std::STANDARD_HELP_VERSION.]
[.] stunnel 5.80 on x86_64-pc-linux-gnu platform
[.] Compiled/running with OpenSSL 3.6.3 9 Jun 2026
[.] Threading:PTHREAD Sockets:POLL,IPv6,SYSTEMD TLS:ENGINE,OCSP,PSK,SNI,DTLS Auth:LIBWRAP
[.] Reading configuration from descriptor 3
[.] FIPS provider disabled
[!] Inetd mode: TLS server needs a certificate
[!] Configuration failed
```

### `man stunnel4`

> 官方示例调用：`man stunnel4`

```text
root@kali:~# man stunnel4
STUNNEL(8)                     stunnel TLS Proxy                     STUNNEL(8)
NAME
     stunnel - TLS offloading and load-balancing proxy
SYNOPSIS
     * Unix: stunnel [FILE] | -fd N | -help | -version | -sockets | -options
     * WIN32:  stunnel  [  [ -install | -uninstall | -start | -stop | -reload |
       -reopen | -exit ] [-quiet] [FILE] ] | -help | -version | -sockets | -op-
       tions
DESCRIPTION
     The stunnel program is designed to work as TLS encryption wrapper  between
     remote clients and local (inetd-startable) or remote servers.  The concept
     is that having non-TLS aware daemons running on your system you can easily
     set them up to communicate with clients over secure TLS channels.
     stunnel  can  be used to add TLS functionality to commonly used Inetd dae-
     mons like POP-2, POP-3, and IMAP servers, to standalone daemons like NNTP,
     SMTP and HTTP, and in tunneling PPP over network sockets  without  changes
     to the source code.
     This  product  includes  cryptographic  software  written  by  Eric  Young
     (
[email protected]
)
OPTIONS
     * FILE
       Use specified configuration file
     * -fd N (Unix only)
       Read the config file from specified file descriptor
     * -help
       Print stunnel help menu
     * -version
       Print stunnel version and compile time defaults
     * -sockets
       Print default socket options
     * -options
       Print supported TLS options
     * -install (Windows NT and later only)
       Install NT Service
     * -uninstall (Windows NT and later only)
       Uninstall NT Service
     * -start (Windows NT and later only)
       Start NT Service
     * -stop (Windows NT and later only)
       Stop NT Service
     * -reload (Windows NT and later only)
       Reload the configuration file of the running NT Service
     * -reopen (Windows NT and later only)
       Reopen the log file of the running NT Service
     * -exit (Win32 only)
       Exit an already started stunnel
     * -quiet (Win32 only)
       Don't display any message boxes
CONFIGURATION FILE
     Each line of the configuration file can be either:
     * An empty line (ignored).
     * A comment starting with `;' (ignored).
     * An `option_name = option_value' pair.
     * `[service_name]' indicating a start of a service definition.
     An address parameter of an option may be either:
     * A port number.
     * A colon-separated pair of IP address (either IPv4, IPv6, or domain name)
       and port number.
     * A Unix socket path (Unix only).
   GLOBAL OPTIONS
     * chroot = DIRECTORY (Unix only)
       directory to chroot stunnel process
       chroot keeps stunnel in a chrooted jail.  CApath, CRLpath, pid and  exec
       are  located  inside the jail and the patches have to be relative to the
       directory specified with chroot.
       Several functions of the operating system also need their  files  to  be
       located within the chroot jail, e.g.:
       * Delayed  resolver  typically  needs  /etc/nsswitch.conf  and  /etc/re-
         solv.conf.
       * Local time in log files needs /etc/timezone.
       * Some other functions may need devices, e.g. /dev/zero or /dev/null.
     * compression = deflate | zlib | zstd | brotli
       select data compression algorithm
       default: no compression
       Data compression is available only for TLS 1.2  and  earlier.   Requires
       lowering securityLevel to 1 when compiled with OpenSSL 1.1.0 and later.
       The  zlib,  zstd,  and  brotli  algorithms  are  disabled in the default
       OpenSSL configuration.
       The zstd and brotli algorithms were added in OpenSSL 3.2.
       Data compression poses a risk in applications that allow an attacker  to
       inject chosen plaintext.
       Deflate is the standard compression method as described in RFC 1951.
       Warning:  TLS compression can enable plaintext-recovery attacks, such as
       CRIME, when attacker-controlled data is compressed together with  secret
       material.
     * debug = [FACILITY.]LEVEL
       debugging level
       Level  is one of the syslog level names or numbers emerg (0), alert (1),
       crit (2), err (3), warning (4), notice (5), info (6), or debug (7).  All
       logs for the specified level and all levels  numerically  less  than  it
       will be shown.
       The debug = debug (or the equivalent <debug = 7>) level produces for the
       most  verbose log output.  This logging level is only meant to be under-
       stood by stunnel developers, and not by users.  Please  either  use  the
       debug level when requested to do so by an stunnel developer, or when you
       intend to get confused.
       The default logging level is notice (5).
       The syslog `daemon' facility will be used unless a facility name is sup-
       plied.  (Facilities are not supported on Win32.)
       Case is ignored for both facilities and levels.
     * EGD = EGD_PATH (Unix only)
       path to Entropy Gathering Daemon socket
       Entropy Gathering Daemon socket to use to feed the OpenSSL random number
       generator.
     * engine = auto | ENGINE_ID
       select hardware or software cryptographic engine
       default: software-only cryptography
       See  Examples section for an engine configuration to use the certificate
       and the corresponding private key from a cryptographic device.
     * engineCtrl = COMMAND[:PARAMETER]
       control hardware engine
     * engineDefault = TASK_LIST
       set OpenSSL tasks delegated to the current engine
       The parameter specifies a comma-separated list of task to  be  delegated
       to the current engine.
       The  following  tasks may be available, if supported by the engine: ALL,
       RSA, DSA, ECDH, ECDSA, DH, RAND, CIPHERS,  DIGESTS,  PKEY,  PKEY_CRYPTO,
       PKEY_ASN1.
     * fips = yes | no
       enable or disable FIPS 140-2 mode.
       This option allows you to disable entering FIPS mode if stunnel was com-
       piled with FIPS 140-2 support.
       default: no (since version 5.00)
     * foreground = yes | quiet | no (Unix only)
       foreground mode
       Stay in foreground (don't fork).
       With  the yes parameter it also logs to stderr in addition to the desti-
       nations specified with syslog and output.
       default: background in daemon mode
     * iconActive = ICON_FILE (GUI only)
       GUI icon to be displayed when there are established connections
       On Windows platform the parameter should be an .ico  file  containing  a
       16x16 pixel image.
     * iconError = ICON_FILE (GUI only)
       GUI icon to be displayed when no valid configuration is loaded
       On  Windows  platform  the parameter should be an .ico file containing a
       16x16 pixel image.
     * iconIdle = ICON_FILE (GUI only)
       GUI icon to be displayed when there are no established connections
       On Windows platform the parameter should be an .ico  file  containing  a
       16x16 pixel image.
     * log = append | overwrite
       log file handling
       This  option  allows  you to choose whether the log file (specified with
       the output option) is appended or overwritten when opened or re-opened.
       default: append
     * output = FILE
       append log messages to a file
       /dev/stdout device can be used to send log messages to the standard out-
       put (for example to log them with daemontools splogger).
     * pid = FILE (Unix only)
       pid file location
       If the argument is empty, then no pid file will be created.
       pid path is relative to the chroot directory if specified.
     * provider = PROVIDER_ID
       Specifies the identifier of the provider to be used.  PROVIDER_ID  is  a
       unique   identifier   referring  to  a  specific  cryptographic  service
       provider.
       This option requires OpenSSL 3.0 or later.
     * providerParameter = PROVIDER_ID:PARAMETER=VALUE
       Sets a specific parameter for the given provider.   PROVIDER_ID  identi-
       fies  the  provider,  PARAMETER  is the parameter name, and VALUE is its
       value.  This option allows customization of the  selected  cryptographic
       service provider's configuration.
       This option requires OpenSSL 3.5 or later.
     * RNDbytes = BYTES
       bytes to read from random seed files
     * RNDfile = FILE
       path to file with random seed data
       The  OpenSSL library will use data from this file first to seed the ran-
       dom number generator.
     * RNDoverwrite = yes | no
       overwrite the random seed files with new random data
       default: yes
     * service = SERVICE (Unix only)
       stunnel service name
       The specified service name is used for syslog and as the inetd mode ser-
       vice name for TCP Wrappers.  While this option can technically be speci-
       fied in the service sections, it is only useful in global options.
       default: stunnel
     * setEnv = VAR_NAME=VALUE
       Change or add an environment variable for child processes.  If  VAR_NAME
       already  exists,  its  value  will be updated; otherwise, a new variable
       will be created.   This  modification  applies  only  to  spawned  child
       processes and does not affect the current environment.
     * syslog = yes | no (Unix only)
       enable logging via syslog
       default: yes
     * taskbar = yes | no (WIN32 only)
       enable the taskbar icon
       default: yes
   SERVICE-LEVEL OPTIONS
     Each  configuration section begins with a service name in square brackets.
     The service name is used for libwrap (TCP  Wrappers)  access  control  and
     lets you distinguish stunnel services in your log files.
     Note that if you wish to run stunnel in inetd mode (where it is provided a
     network  socket  by a server such as inetd, xinetd, or tcpserver) then you
     should read the section entitled INETD MODE below.
     * accept = [HOST:]PORT
       accept connections on specified address
       If no host specified, defaults to all IPv4 addresses for the local host.
       To listen on all IPv6 addresses use:
              accept = :::PORT
     * CAengine = ENGINE-SPECIFIC_CA_CERTIFICATE_IDENTIFIER
       load a trusted CA certificate from an engine
       The loaded CA certificates will be used with the verifyChain  and  veri-
       fyPeer options.
       Multiple CAengine options are allowed in a single service section.
       Currently supported engines: pkcs11, cng.
     * CApath = CA_DIRECTORY
       load trusted CA certificates from a directory
       The  loaded  CA certificates will be used with the verifyChain and veri-
       fyPeer options.  Note that the certificates in this directory should  be
       named  XXXXXXXX.0  where  XXXXXXXX  is the hash value of the DER encoded
       subject of the cert.
       This parameter can also be used  to  provide  the  root  CA  certificate
       needed to validate OCSP stapling in server mode.
```

## 4. 实践清单

按顺序做完这五步，就能把工具从「装上」推进到「会用」：

- [ ] **1.** **装好并确认版本** —— `sudo apt install stunnel`，再执行 `stunnel --version` 2>/dev/null || `stunnel -V`
- [ ] **2.** **读官方帮助** —— `stunnel -h`，需要细节时 `man stunnel`
- [ ] **3.** **在自有靶场跑最小用例** —— 官方给出的调用形式是：`Usage: stunnel3 [-OPTIONS [-MORE_OPTIONS]] [--] [PROGRAM_ARG1 ...]`
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/stunnel/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/stunnel/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/stunnel/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
