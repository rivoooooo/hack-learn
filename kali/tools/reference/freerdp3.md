# freerdp3

> FreeRDP proxy server FreeRDP is a libre client/server implementation of the Remote Desktop Protocol (RDP). This package contains the proxy server that can be used as man in the middle proxy for RDP connections.

> **功能分类**：信息搜集 ｜ **Kali 包**：`freerdp3` ｜ **官方文档**：<https://www.kali.org/tools/freerdp3/>

## 1. 安装

```bash
sudo apt update
sudo apt install freerdp-proxy
```

| 项目 | 内容 |
|------|------|
| 版本 | 3.31.1 |
| 架构 | any |
| 可执行命令 | `freerdp-proxy`、`freerdp-proxy-modules`、`freerdp-sdl`、`sdl-freerdp`、`freerdp-shadow-x11`、`freerdp-shadow-cli`、`freerdp-wayland`、`wlfreerdp`、`freerdp-x11`、`xfreerdp`、`freerdp3-dev`、`freerdp3-proxy`、`freerdp-proxy3`、`freerdp3-proxy-modules`、`freerdp3-sdl`、`sdl-freerdp3`、`freerdp3-shadow-x11`、`freerdp-shadow-cli3`、`freerdp3-wayland`、`wlfreerdp3`、`freerdp3-x11`、`xfreerdp3`、`libfreerdp-client3-3`、`libfreerdp-server-proxy3-3`、`libfreerdp-server3-3`、`libfreerdp-shadow-subsystem3-3`、`libfreerdp-shadow3-3`、`libfreerdp3-3`、`libwinpr-tools3-3`、`libwinpr3-3`、`libwinpr3-dev`、`winpr-utils`、`winpr-hash`、`winpr-makecert`、`winpr3-utils`、`winpr-hash3`、`winpr-makecert3` |
| 依赖 | `libc6`、`libfreerdp-server-proxy3-3`、`libfreerdp3-3`、`libwinpr3-3`、`freerdp-proxy` |
| 安装体积 | 30 KB |
| 官网 | <https://www.freerdp.com/> |
| 源码仓库 | <https://salsa.debian.org/debian-remote-team/freerdp3> |
| 包追踪 | <https://pkg.kali.org/pkg/freerdp3> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
freerdp-proxy -h          # 查看用法
man freerdp-proxy         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 37 个可执行命令，下面是官方页面内嵌的帮助原文。

### `freerdp-proxy`

> 官方示例调用：`freerdp-proxy -h`

```text
root@kali:~# freerdp-proxy -h
[05:43:14:524] [200330:00030e8a] [INFO][com.freerdp.proxy.server] - [main]: freerdp-proxy version info:
[05:43:14:524] [200330:00030e8a] [INFO][com.freerdp.proxy.server] - [main]: 	FreeRDP version: 3.31.1
[05:43:14:524] [200330:00030e8a] [INFO][com.freerdp.proxy.server] - [main]: 	Git commit: 3.31.1
Usage:
freerdp-proxy -h                                  Display this help text.
freerdp-proxy --help                              Display this help text.
freerdp-proxy --buildconfig                       Print the build configuration.
freerdp-proxy <config ini file>                   Start the proxy with <config.ini>
freerdp-proxy --dump-config [<config ini file>|stdout|stderr] Create a template <config.ini> or print to stdout/stderr.
freerdp-proxy -v                                  Print out binary version.
freerdp-proxy --version                           Print out binary version.
```

### `sdl-freerdp`

> 官方示例调用：`sdl-freerdp --help`

```text
root@kali:~# sdl-freerdp --help
sdl-freerdp - A Free Remote Desktop Protocol Implementation
See www.freerdp.com for more information
Usage: sdl-freerdp [file] [options] [/v:<server>[:port]]
Syntax:
    /flag (enables flag)
    /option:<value> (specifies option with value)
    +toggle -toggle (enables or disables toggle, where '/' is a synonym of '+')
    /a: <addin>[,<options>]           Addin
    /action-script: <file-name>       Action script
    +admin                            Admin (or console) session
    +aero                             Enable desktop composition
    /app: program:[<path>|<||alias>],cmd:<command>,file:<filename>,guid:<guid>,
          icon:<filename>,name:<name>,workdir:<directory>,hidef:[on|off]
                                      Remote application program
    /args-from: file:<file>|stdin|fd:<number>|env:<name>
                                      Read command line from a file, stdin or
                                      file descriptor. This argument can not be
                                      combined with any other. Provide one
                                      argument per line.
    /assistance: <password>           Remote assistance password
    +async-channels                   Enable Asynchronous channels
                                      (experimental)
    +async-update                     Enable Asynchronous update
    /audio-mode: [[none|2]|[server|1]|[redirect|0]]
                                      Audio output mode
    +auth-only                        Enable Authenticate only
    /auth-pkg-list: [[none],]<!ntlm,kerberos,!u2u>
                                      Authentication package filter
                                      (comma-separated list, use '!' to
                                      disable). By default all methods are
                                      enabled. Use explicit 'none' as first
                                      argument to disable all methods,
                                      selectively enabling only the ones
                                      following.
    -authentication                   Disable Authentication (experimental)
    +auto-reconnect                   Enable Automatic reconnection
    /auto-reconnect-max-retries: <retries>
                                      Automatic reconnection maximum retries, 0
                                      for unlimited [0,1000]
    +auto-request-control             Automatically request remote assistance
                                      input control
    /azure: [tenantid:<id>],[use-tenantid[:[on|off]],[ad:<url>][
            avd-access:<format string>],[avd-token:<format string>],[
            avd-scope:<format string>] AzureAD options
    /bpp: <depth>                     Session bpp (color depth)
    +buildconfig                      Print the build configuration
    /cache: [bitmap[:on|off],codec[:rfx|nsc],glyph[:on|off],offscreen[:on|off],
            persist,persist-file:<filename>]
    /cert: [deny,ignore,name:<name>,tofu,fingerprint:<hash>:<hash as hex>[,
           fingerprint:<hash>:<another hash>]]
                                      Certificate accept options. Use with
                                      care!
                                       * deny         ... Automatically abort
                                      connection if the certificate does not
                                      match, no user interaction.
                                       * ignore       ... Ignore the
                                      certificate checks altogether (overrules
                                      all other options)
                                       * name         ... Use the alternate
                                      <name> instead of the certificate subject
                                      to match locally stored certificates
                                       * tofu         ... Accept certificate
                                      unconditionally on first connect and deny
                                      on subsequent connections if the
                                      certificate does not match
                                       * fingerprints ... A list of certificate
                                      hashes that are accepted unconditionally
                                      for a connection
    /client-build-number: <number>    Client Build Number sent to server
                                      (influences smartcard behaviour, see
                                      [MS-RDPESC])
    /client-hostname: <name>          Client Hostname to send to server
    [-|/]clipboard[: [[use-selection:<atom>],[direction-to:[
                     all|local|remote|off]],[files-to[:all|local|remote|off]]]]
                                      Disable Redirect clipboard:
                                       * use-selection:<atom>  ... (X11)
                                      Specify which X selection to access.
                                      Default is CLIPBOARD. PRIMARY is the
                                      X-style middle-click selection.
                                       * direction-to:[all|local|remote|off]
                                      control enabled clipboard direction
                                       * files-to:[all|local|remote|off]
                                      control enabled file clipboard direction
    -compression                      Disable compression
    /compression-level: <level>       Compression level (0,1,2)
    +credentials-delegation           Enable credentials delegation
    /d: <domain>                      Domain
    -decorations                      Disable Window decorations
    +disable-output                   Deactivate all graphics decoding in the
                                      client session. Useful for load tests
                                      with many simultaneous connections
    +disp                             Display control
    /drive: <name>,<path>             Redirect directory <path> as named share
                                      <name>. Hotplug support is enabled with
                                      /drive:hotplug,*. This argument provides
                                      the same function as "Drives that I plug
                                      in later" option in MSTSC.
    +drives                           Enable Redirect all mount points as
                                      shares
    /dump: <record|replay>,file:<file>[,nodelay]
                                      record or replay dump
    /dvc: <channel>[,<options>]       Dynamic virtual channel
    +dynamic-resolution               Enable Send resolution updates when the
                                      window is resized
    +echo                             Echo channel
    -encryption                       Disable Encryption (experimental)
    /encryption-methods: [40,][56,][128,][FIPS]
                                      RDP standard security encryption methods
    /endpointfedauth: <token>         Endpoint FedAuth token for Hyper-V VM
                                      console-connect scenarios
    +f                                Fullscreen mode (<Ctrl>+<Alt>+<Enter>
                                      toggles fullscreen)
    +fipsmode                         Enable FIPS mode
    /floatbar[: sticky:[on|off],default:[visible|hidden],show:[
                always|fullscreen|window]]
                                      floatbar is disabled by default (when
                                      enabled defaults to sticky in fullscreen
                                      mode)
    -fonts                            Disable smooth fonts (ClearType)
    +force-console-callbacks          Enable Use default callbacks (console)
                                      for certificate/credential/...
    /frame-ack: <number>              Number of frame acknowledgement
    /from-stdin[: force]              Read credentials from stdin. With <force>
                                      the prompt is done before connection,
                                      otherwise on server request.
    /gateway: g:<gateway>[:<port>],u:<user>,d:<domain>,p:<password>,
              usage-method:[direct|detect],access-token:<token>,type:[rpc|http[,
              no-websockets][,extauth-sspi-ntlm]|auto[,no-websockets][,
              extauth-sspi-ntlm]]|arm,url:<wss://url>,
              bearer:<oauth2-bearer-token>
                                      Gateway Hostname
    /gdi: sw|hw                       GDI rendering
    +geometry                         Geometry tracking channel
    +gestures                         Enable Consume multitouch input locally
    /gfx[: [[progressive[:on|off]|RFX[:on|off]|AVC420[:on|off]AVC444[:on|off]],
           mask:<value>,small-cache[:on|off],thin-client[:on|off],progressive[
           :on|off],frame-ack[:on|off]]
                                      RDP8 graphics pipeline
    -grab-keyboard                    Disable Grab keyboard focus, forward all
                                      keys to remote
    -grab-mouse                       Disable Grab mouse focus, forward all
                                      events to remote
    /h: <height>                      Height
    -heartbeat                        Disable Support heartbeat PDUs
    +help                             Print help
    +home-drive                       Enable Redirect user home as share
    /ipv4[: [:force]]                 Prefer IPv4 A record over IPv6 AAAA
                                      record
    /ipv6[: [:force]]                 Prefer IPv6 AAAA record over IPv4 A
                                      record
    +jpeg                             JPEG codec support
    /jpeg-quality: <percentage>       JPEG quality
    /kbd: [layout:[0x<id>|<name>],lang:<0x<id>>,fn-key:<value>,type:<value>,
          subtype:<value>,unicode[:on|off],remap:<key1>=<value1>,
          remap:<key2>=<value2>,pipe:<filename>]
                                      Keyboard related options:
                                       * layout: set the keybouard layout
                                      announced to the server
                                       * lang: set the keyboard language
                                      identifier sent to the server
                                       * fn-key: Function key value
                                       * remap: RDP scancode to another one.
                                      Use /list:kbd-scancode to get the
                                      mapping. Example: To switch 'a' and 's'
                                      on a US keyboard:
                                      /kbd:remap:0x1e=0x1f,remap:0x1f=0x1e
                                       * pipe: Name of a named pipe that can be
                                      used to type text into the RDP session
    /kerberos: [kdc-url:<url>,lifetime:<time>,start-time:<time>,
               renewable-lifetime:<time>,cache:<path>,armor:<path>,
               pkinit-anchors:<path>,pkcs11-module:<name>]
                                      Kerberos options
    /list: [kbd|kbd-scancode|kbd-lang[:<value>]|smartcard[:[
           pkinit-anchors:<path>][,pkcs11-module:<name>]]
           |monitor|tune|timezones]   List available options for subcommand
    /load-balance-info: <info-string> Load balance info
    /log-filters: <tag>:<level>[,<tag>:<level>[,...]]
                                      Set logger filters, see wLog(7) for
                                      details
    /log-level: [OFF|FATAL|ERROR|WARN|INFO|DEBUG|TRACE]
                                      Set the default log level, see wLog(7)
                                      for details
    /max-fast-path-size: <size>       Specify maximum fast-path update size
    /max-loop-time: <time>            Specify maximum time in milliseconds
                                      spend treating packets
    +menu-anims                       Enable menu animations
    /microphone[: [sys:<sys>,][dev:<dev>,][format:<format>,][rate:<rate>,][
                  channel:<channel>]] Audio input (microphone)
    /monitors: <id>[,<id>[,...]]      [experimental] Select monitors to use
                                      (only effective in fullscreen or
                                      multimonitor mode)
    /mouse: [relative:[on|off],grab:[on|off]]
                                      Mouse related options:
                                       * relative:   send relative mouse
                                      movements if supported by server
                                       * grab:       grab the mouse if within
                                      the window
    -mouse-motion                     Disable Send mouse motion events
    +mouse-relative                   Enable Send mouse motion with relative
                                      addressing
    /multimon[: force]                Use multiple monitors
    +multitouch                       Enable Redirect multitouch input
    -multitransport                   Disable Support multitransport protocol
    -nego                             Disable protocol security negotiation
    /network: [invalid|modem|broadband|broadband-low|broadband-high|wan|lan|auto]
                                      Network connection type
    +nsc                              NSCodec support
    +old-license                      Enable Use the old license workflow (no
                                      CAL and hwId set to 0)
    /orientation: [0|90|180|270]      Orientation of display in degrees
    /p[: <password>]                  Password. Pass /p without arguments to
                                      silences interactive password prompts if
                                      no credentials are required for the
                                      connection.
    /parallel[: <name>[,<path>]]      Redirect parallel device
    /parent-window: <window-id>       Parent window id
    /pcb: <blob>                      Preconnection Blob
    /pcid: <id>                       Preconnection Id
    /pheight: <height>                Physical height of display (in
```

### `freerdp-shadow-cli`

> 官方示例调用：`freerdp-shadow-cli -h`

```text
root@kali:~# freerdp-shadow-cli -h
Usage: freerdp-shadow-cli [options]
Notes: By default NLA security is active.
	In this mode a SAM database is required.
	Provide one with /sam-file:<file with path>
	else the default path /etc/FreeRDP/FreeRDP/SAM is used.
	If there is no existing SAM file authentication for all users will fail.
	If authentication against PAM is desired, start with -sec-nla (requires compiled in support for PAM)
Syntax:
    /flag (enables flag)
    /option:<value> (specifies option with value)
    +toggle -toggle (enables or disables toggle, where '/' is a synonym of '+')
    -auth (default:on)
	Clients must authenticate
    /bind-address:<bind-address>[,<another address>, ...]
	An address to bind to. Use '[<ipv6>]' for IPv6 addresses, e.g. '[::1]' for localhost
    +bitmap-compat (default:off)
	Limit BitmapUpdate to 1 rectangle (fixes broken windows 11 24H2 clients)
    /buildconfig
	Print the build configuration
    /ccache:<file>
	Kerberos host ccache file for NLA authentication
    -gfx (default:on)
	Allow GFX pipeline
    -gfx-avc420 (default:on)
	Allow GFX AVC420 codec
    -gfx-avc444 (default:on)
	Allow GFX AVC444 codec
    -gfx-planar (default:on)
	Allow GFX planar codec
    -gfx-progressive (default:on)
	Allow GFX progressive codec
    -gfx-rfx (default:on)
	Allow GFX RFX codec
    /help
	Print help
    /ipc-socket:<ipc-socket>
	Server IPC socket
    /keytab:<file>
	Kerberos keytab file for NLA authentication
    /log-filters:<tag>:<level>[,<tag>:<level>[,...]]
	Set logger filters, see wLog(7) for details
    /log-level:[OFF|FATAL|ERROR|WARN|INFO|DEBUG|TRACE]
	Set the default log level, see wLog(7) for details
    /max-connections:<number>
	maximum connections allowed to server, 0 to deactivate
    -may-interact (default:on)
	Clients may interact without prompt
    -may-view (default:on)
	Clients may view without prompt
    /monitors:<0,1,2...>
	Select or list monitors
    +mouse-relative (default:off)
	enable support for relative mouse events
    -nsc (default:on)
	Allow NSC codec
    /port:<number>
	Server port
    /rect:<x,y,w,h>
	Select rectangle within monitor to share
    +remote-guard (default:off)
	Remote credential guard
    -restricted-admin (default:on)
	Restricted Admin
    -rfx (default:on)
	Allow RFX surface bits
    /sam-file:<file>
	NTLM SAM file for NLA authentication
    /sec:<rdp|tls|nla|ext>
	force specific protocol security
    +sec-ext (default:off)
	nla extended protocol security
    -sec-nla (default:on)
	nla protocol security
    -sec-rdp (default:on)
	rdp protocol security
    -sec-tls (default:on)
	tls protocol security
    +server-side-cursor (default:off)
	hide mouse cursor in RDP client.
    /tls-secrets-file:<file>
	file where tls secrets shall be stored
    /version
	Print version
    /vmconnect
	Hyper-V console server (bind on vsock://1)
```

### `man`

> 官方示例调用：`man wlfreerdp`

```text
root@kali:~# man wlfreerdp
wlfreerdp(1)                        FreeRDP                        wlfreerdp(1)
NAME
     wlfreerdp - FreeRDP wayland client
SYNOPSIS
     wlfreerdp  [file] [default_client_options] [/v:<server>[:port]] [/version]
     [/help]
DESCRIPTION
     wlfreerdp is a wayland Remote Desktop Protocol (RDP) client which is  part
     of  the FreeRDP project. A RDP server is built-in to many editions of Win-
     dows.. Alternative servers included ogon, gnome-remote-desktop,  xrdp  and
     VRDP (VirtualBox).
OPTIONS
     The wayland client also supports a lot of the default client options which
     are not described here. For details on those see the xfreerdp(1) man page.
     /v:<server>[:port]
            The server hostname or IP, and optionally the port, to connect to.
     /version
            Print the version and exit.
     /help  Print the help and exit.
EXIT STATUS
     0      Successful program execution.
     not 0  On failure.
SEE ALSO
     xfreerdp(1) wlog(7)
AUTHOR
     FreeRDP <
[email protected]
>
3.31.1                             2017-01-12                      wlfreerdp(1)
```

### `xfreerdp`

> 官方示例调用：`xfreerdp --help`

```text
root@kali:~# xfreerdp --help
xfreerdp - A Free Remote Desktop Protocol Implementation
See www.freerdp.com for more information
Usage: xfreerdp [file] [options] [/v:<server>[:port]]
Syntax:
    /flag (enables flag)
    /option:<value> (specifies option with value)
    +toggle -toggle (enables or disables toggle, where '/' is a synonym of '+')
    /a: <addin>[,<options>]           Addin
    /action-script: <file-name>       Action script
    +admin                            Admin (or console) session
    +aero                             Enable desktop composition
    /app: program:[<path>|<||alias>],cmd:<command>,file:<filename>,guid:<guid>,
          icon:<filename>,name:<name>,workdir:<directory>,hidef:[on|off]
                                      Remote application program
    /args-from: file:<file>|stdin|fd:<number>|env:<name>
                                      Read command line from a file, stdin or
                                      file descriptor. This argument can not be
                                      combined with any other. Provide one
                                      argument per line.
    /assistance: <password>           Remote assistance password
    +async-channels                   Enable Asynchronous channels
                                      (experimental)
    +async-update                     Enable Asynchronous update
    /audio-mode: [[none|2]|[server|1]|[redirect|0]]
                                      Audio output mode
    +auth-only                        Enable Authenticate only
    /auth-pkg-list: [[none],]<!ntlm,kerberos,!u2u>
                                      Authentication package filter
                                      (comma-separated list, use '!' to
                                      disable). By default all methods are
                                      enabled. Use explicit 'none' as first
                                      argument to disable all methods,
                                      selectively enabling only the ones
                                      following.
    -authentication                   Disable Authentication (experimental)
    +auto-reconnect                   Enable Automatic reconnection
    /auto-reconnect-max-retries: <retries>
                                      Automatic reconnection maximum retries, 0
                                      for unlimited [0,1000]
    +auto-request-control             Automatically request remote assistance
                                      input control
    /azure: [tenantid:<id>],[use-tenantid[:[on|off]],[ad:<url>][
            avd-access:<format string>],[avd-token:<format string>],[
            avd-scope:<format string>] AzureAD options
    /bpp: <depth>                     Session bpp (color depth)
    +buildconfig                      Print the build configuration
    /cache: [bitmap[:on|off],codec[:rfx|nsc],glyph[:on|off],offscreen[:on|off],
            persist,persist-file:<filename>]
    /cert: [deny,ignore,name:<name>,tofu,fingerprint:<hash>:<hash as hex>[,
           fingerprint:<hash>:<another hash>]]
                                      Certificate accept options. Use with
                                      care!
                                       * deny         ... Automatically abort
                                      connection if the certificate does not
                                      match, no user interaction.
                                       * ignore       ... Ignore the
                                      certificate checks altogether (overrules
                                      all other options)
                                       * name         ... Use the alternate
                                      <name> instead of the certificate subject
                                      to match locally stored certificates
                                       * tofu         ... Accept certificate
                                      unconditionally on first connect and deny
                                      on subsequent connections if the
                                      certificate does not match
                                       * fingerprints ... A list of certificate
                                      hashes that are accepted unconditionally
                                      for a connection
    /client-build-number: <number>    Client Build Number sent to server
                                      (influences smartcard behaviour, see
                                      [MS-RDPESC])
    /client-hostname: <name>          Client Hostname to send to server
    [-|/]clipboard[: [[use-selection:<atom>],[direction-to:[
                     all|local|remote|off]],[files-to[:all|local|remote|off]]]]
                                      Disable Redirect clipboard:
                                       * use-selection:<atom>  ... (X11)
                                      Specify which X selection to access.
                                      Default is CLIPBOARD. PRIMARY is the
                                      X-style middle-click selection.
                                       * direction-to:[all|local|remote|off]
                                      control enabled clipboard direction
                                       * files-to:[all|local|remote|off]
                                      control enabled file clipboard direction
    -compression                      Disable compression
    /compression-level: <level>       Compression level (0,1,2)
    +credentials-delegation           Enable credentials delegation
    /d: <domain>                      Domain
    -decorations                      Disable Window decorations
    +disable-output                   Deactivate all graphics decoding in the
                                      client session. Useful for load tests
                                      with many simultaneous connections
    +disp                             Display control
    /drive: <name>,<path>             Redirect directory <path> as named share
                                      <name>. Hotplug support is enabled with
                                      /drive:hotplug,*. This argument provides
                                      the same function as "Drives that I plug
                                      in later" option in MSTSC.
    +drives                           Enable Redirect all mount points as
                                      shares
    /dump: <record|replay>,file:<file>[,nodelay]
                                      record or replay dump
    /dvc: <channel>[,<options>]       Dynamic virtual channel
    +dynamic-resolution               Enable Send resolution updates when the
                                      window is resized
    +echo                             Echo channel
    -encryption                       Disable Encryption (experimental)
    /encryption-methods: [40,][56,][128,][FIPS]
                                      RDP standard security encryption methods
    /endpointfedauth: <token>         Endpoint FedAuth token for Hyper-V VM
                                      console-connect scenarios
    +f                                Fullscreen mode (<Ctrl>+<Alt>+<Enter>
                                      toggles fullscreen)
    +fipsmode                         Enable FIPS mode
    /floatbar[: sticky:[on|off],default:[visible|hidden],show:[
                always|fullscreen|window]]
                                      floatbar is disabled by default (when
                                      enabled defaults to sticky in fullscreen
                                      mode)
    -fonts                            Disable smooth fonts (ClearType)
    +force-console-callbacks          Enable Use default callbacks (console)
                                      for certificate/credential/...
    /frame-ack: <number>              Number of frame acknowledgement
    /from-stdin[: force]              Read credentials from stdin. With <force>
                                      the prompt is done before connection,
                                      otherwise on server request.
    /gateway: g:<gateway>[:<port>],u:<user>,d:<domain>,p:<password>,
              usage-method:[direct|detect],access-token:<token>,type:[rpc|http[,
              no-websockets][,extauth-sspi-ntlm]|auto[,no-websockets][,
              extauth-sspi-ntlm]]|arm,url:<wss://url>,
              bearer:<oauth2-bearer-token>
                                      Gateway Hostname
    /gdi: sw|hw                       GDI rendering
    +geometry                         Geometry tracking channel
    +gestures                         Enable Consume multitouch input locally
    /gfx[: [[progressive[:on|off]|RFX[:on|off]|AVC420[:on|off]AVC444[:on|off]],
           mask:<value>,small-cache[:on|off],thin-client[:on|off],progressive[
           :on|off],frame-ack[:on|off]]
                                      RDP8 graphics pipeline
    -grab-keyboard                    Disable Grab keyboard focus, forward all
                                      keys to remote
    -grab-mouse                       Disable Grab mouse focus, forward all
                                      events to remote
    /h: <height>                      Height
    -heartbeat                        Disable Support heartbeat PDUs
    +help                             Print help
    +home-drive                       Enable Redirect user home as share
    /ipv4[: [:force]]                 Prefer IPv4 A record over IPv6 AAAA
                                      record
    /ipv6[: [:force]]                 Prefer IPv6 AAAA record over IPv4 A
                                      record
    +jpeg                             JPEG codec support
    /jpeg-quality: <percentage>       JPEG quality
    /kbd: [layout:[0x<id>|<name>],lang:<0x<id>>,fn-key:<value>,type:<value>,
          subtype:<value>,unicode[:on|off],remap:<key1>=<value1>,
          remap:<key2>=<value2>,pipe:<filename>]
                                      Keyboard related options:
                                       * layout: set the keybouard layout
                                      announced to the server
                                       * lang: set the keyboard language
                                      identifier sent to the server
                                       * fn-key: Function key value
                                       * remap: RDP scancode to another one.
                                      Use /list:kbd-scancode to get the
                                      mapping. Example: To switch 'a' and 's'
                                      on a US keyboard:
                                      /kbd:remap:0x1e=0x1f,remap:0x1f=0x1e
                                       * pipe: Name of a named pipe that can be
                                      used to type text into the RDP session
    /kerberos: [kdc-url:<url>,lifetime:<time>,start-time:<time>,
               renewable-lifetime:<time>,cache:<path>,armor:<path>,
               pkinit-anchors:<path>,pkcs11-module:<name>]
                                      Kerberos options
    /list: [kbd|kbd-scancode|kbd-lang[:<value>]|smartcard[:[
           pkinit-anchors:<path>][,pkcs11-module:<name>]]
           |monitor|tune|timezones]   List available options for subcommand
    /load-balance-info: <info-string> Load balance info
    /log-filters: <tag>:<level>[,<tag>:<level>[,...]]
                                      Set logger filters, see wLog(7) for
                                      details
    /log-level: [OFF|FATAL|ERROR|WARN|INFO|DEBUG|TRACE]
                                      Set the default log level, see wLog(7)
                                      for details
    /max-fast-path-size: <size>       Specify maximum fast-path update size
    /max-loop-time: <time>            Specify maximum time in milliseconds
                                      spend treating packets
    +menu-anims                       Enable menu animations
    /microphone[: [sys:<sys>,][dev:<dev>,][format:<format>,][rate:<rate>,][
                  channel:<channel>]] Audio input (microphone)
    /monitors: <id>[,<id>[,...]]      [experimental] Select monitors to use
                                      (only effective in fullscreen or
                                      multimonitor mode)
    /mouse: [relative:[on|off],grab:[on|off]]
                                      Mouse related options:
                                       * relative:   send relative mouse
                                      movements if supported by server
                                       * grab:       grab the mouse if within
                                      the window
    -mouse-motion                     Disable Send mouse motion events
    +mouse-relative                   Enable Send mouse motion with relative
                                      addressing
    /multimon[: force]                Use multiple monitors
    +multitouch                       Enable Redirect multitouch input
    -multitransport                   Disable Support multitransport protocol
    -nego                             Disable protocol security negotiation
    /network: [invalid|modem|broadband|broadband-low|broadband-high|wan|lan|auto]
                                      Network connection type
    +nsc                              NSCodec support
    +old-license                      Enable Use the old license workflow (no
                                      CAL and hwId set to 0)
    /orientation: [0|90|180|270]      Orientation of display in degrees
    /p[: <password>]                  Password. Pass /p without arguments to
                                      silences interactive password prompts if
                                      no credentials are required for the
                                      connection.
    /parallel[: <name>[,<path>]]      Redirect parallel device
    /parent-window: <window-id>       Parent window id
    /pcb: <blob>                      Preconnection Blob
    /pcid: <id>                       Preconnection Id
    /pheight: <height>                Physical height of display (in
```

### `freerdp-proxy3`

> 官方示例调用：`freerdp-proxy3 -h`

```text
root@kali:~# freerdp-proxy3 -h
[05:44:02:159] [203375:00031a6f] [INFO][com.freerdp.proxy.server] - [main]: freerdp-proxy version info:
[05:44:02:159] [203375:00031a6f] [INFO][com.freerdp.proxy.server] - [main]: 	FreeRDP version: 3.31.1
[05:44:02:159] [203375:00031a6f] [INFO][com.freerdp.proxy.server] - [main]: 	Git commit: 3.31.1
Usage:
freerdp-proxy3 -h                                  Display this help text.
freerdp-proxy3 --help                              Display this help text.
freerdp-proxy3 --buildconfig                       Print the build configuration.
freerdp-proxy3 <config ini file>                   Start the proxy with <config.ini>
freerdp-proxy3 --dump-config [<config ini file>|stdout|stderr] Create a template <config.ini> or print to stdout/stderr.
freerdp-proxy3 -v                                  Print out binary version.
freerdp-proxy3 --version                           Print out binary version.
```

### `sdl-freerdp3`

> 官方示例调用：`sdl-freerdp3 --help`

```text
root@kali:~# sdl-freerdp3 --help
sdl-freerdp3 - A Free Remote Desktop Protocol Implementation
See www.freerdp.com for more information
Usage: sdl-freerdp3 [file] [options] [/v:<server>[:port]]
Syntax:
    /flag (enables flag)
    /option:<value> (specifies option with value)
    +toggle -toggle (enables or disables toggle, where '/' is a synonym of '+')
    /a: <addin>[,<options>]           Addin
    /action-script: <file-name>       Action script
    +admin                            Admin (or console) session
    +aero                             Enable desktop composition
    /app: program:[<path>|<||alias>],cmd:<command>,file:<filename>,guid:<guid>,
          icon:<filename>,name:<name>,workdir:<directory>,hidef:[on|off]
                                      Remote application program
    /args-from: file:<file>|stdin|fd:<number>|env:<name>
                                      Read command line from a file, stdin or
                                      file descriptor. This argument can not be
                                      combined with any other. Provide one
                                      argument per line.
    /assistance: <password>           Remote assistance password
    +async-channels                   Enable Asynchronous channels
                                      (experimental)
    +async-update                     Enable Asynchronous update
    /audio-mode: [[none|2]|[server|1]|[redirect|0]]
                                      Audio output mode
    +auth-only                        Enable Authenticate only
    /auth-pkg-list: [[none],]<!ntlm,kerberos,!u2u>
                                      Authentication package filter
                                      (comma-separated list, use '!' to
                                      disable). By default all methods are
                                      enabled. Use explicit 'none' as first
                                      argument to disable all methods,
                                      selectively enabling only the ones
                                      following.
    -authentication                   Disable Authentication (experimental)
    +auto-reconnect                   Enable Automatic reconnection
    /auto-reconnect-max-retries: <retries>
                                      Automatic reconnection maximum retries, 0
                                      for unlimited [0,1000]
    +auto-request-control             Automatically request remote assistance
                                      input control
    /azure: [tenantid:<id>],[use-tenantid[:[on|off]],[ad:<url>][
            avd-access:<format string>],[avd-token:<format string>],[
            avd-scope:<format string>] AzureAD options
    /bpp: <depth>                     Session bpp (color depth)
    +buildconfig                      Print the build configuration
    /cache: [bitmap[:on|off],codec[:rfx|nsc],glyph[:on|off],offscreen[:on|off],
            persist,persist-file:<filename>]
    /cert: [deny,ignore,name:<name>,tofu,fingerprint:<hash>:<hash as hex>[,
           fingerprint:<hash>:<another hash>]]
                                      Certificate accept options. Use with
                                      care!
                                       * deny         ... Automatically abort
                                      connection if the certificate does not
                                      match, no user interaction.
                                       * ignore       ... Ignore the
                                      certificate checks altogether (overrules
                                      all other options)
                                       * name         ... Use the alternate
                                      <name> instead of the certificate subject
                                      to match locally stored certificates
                                       * tofu         ... Accept certificate
                                      unconditionally on first connect and deny
                                      on subsequent connections if the
                                      certificate does not match
                                       * fingerprints ... A list of certificate
                                      hashes that are accepted unconditionally
                                      for a connection
    /client-build-number: <number>    Client Build Number sent to server
                                      (influences smartcard behaviour, see
                                      [MS-RDPESC])
    /client-hostname: <name>          Client Hostname to send to server
    [-|/]clipboard[: [[use-selection:<atom>],[direction-to:[
                     all|local|remote|off]],[files-to[:all|local|remote|off]]]]
                                      Disable Redirect clipboard:
                                       * use-selection:<atom>  ... (X11)
                                      Specify which X selection to access.
                                      Default is CLIPBOARD. PRIMARY is the
                                      X-style middle-click selection.
                                       * direction-to:[all|local|remote|off]
                                      control enabled clipboard direction
                                       * files-to:[all|local|remote|off]
                                      control enabled file clipboard direction
    -compression                      Disable compression
    /compression-level: <level>       Compression level (0,1,2)
    +credentials-delegation           Enable credentials delegation
    /d: <domain>                      Domain
    -decorations                      Disable Window decorations
    +disable-output                   Deactivate all graphics decoding in the
                                      client session. Useful for load tests
                                      with many simultaneous connections
    +disp                             Display control
    /drive: <name>,<path>             Redirect directory <path> as named share
                                      <name>. Hotplug support is enabled with
                                      /drive:hotplug,*. This argument provides
                                      the same function as "Drives that I plug
                                      in later" option in MSTSC.
    +drives                           Enable Redirect all mount points as
                                      shares
    /dump: <record|replay>,file:<file>[,nodelay]
                                      record or replay dump
    /dvc: <channel>[,<options>]       Dynamic virtual channel
    +dynamic-resolution               Enable Send resolution updates when the
                                      window is resized
    +echo                             Echo channel
    -encryption                       Disable Encryption (experimental)
    /encryption-methods: [40,][56,][128,][FIPS]
                                      RDP standard security encryption methods
    /endpointfedauth: <token>         Endpoint FedAuth token for Hyper-V VM
                                      console-connect scenarios
    +f                                Fullscreen mode (<Ctrl>+<Alt>+<Enter>
                                      toggles fullscreen)
    +fipsmode                         Enable FIPS mode
    /floatbar[: sticky:[on|off],default:[visible|hidden],show:[
                always|fullscreen|window]]
                                      floatbar is disabled by default (when
                                      enabled defaults to sticky in fullscreen
                                      mode)
    -fonts                            Disable smooth fonts (ClearType)
    +force-console-callbacks          Enable Use default callbacks (console)
                                      for certificate/credential/...
    /frame-ack: <number>              Number of frame acknowledgement
    /from-stdin[: force]              Read credentials from stdin. With <force>
                                      the prompt is done before connection,
                                      otherwise on server request.
    /gateway: g:<gateway>[:<port>],u:<user>,d:<domain>,p:<password>,
              usage-method:[direct|detect],access-token:<token>,type:[rpc|http[,
              no-websockets][,extauth-sspi-ntlm]|auto[,no-websockets][,
              extauth-sspi-ntlm]]|arm,url:<wss://url>,
              bearer:<oauth2-bearer-token>
                                      Gateway Hostname
    /gdi: sw|hw                       GDI rendering
    +geometry                         Geometry tracking channel
    +gestures                         Enable Consume multitouch input locally
    /gfx[: [[progressive[:on|off]|RFX[:on|off]|AVC420[:on|off]AVC444[:on|off]],
           mask:<value>,small-cache[:on|off],thin-client[:on|off],progressive[
           :on|off],frame-ack[:on|off]]
                                      RDP8 graphics pipeline
    -grab-keyboard                    Disable Grab keyboard focus, forward all
                                      keys to remote
    -grab-mouse                       Disable Grab mouse focus, forward all
                                      events to remote
    /h: <height>                      Height
    -heartbeat                        Disable Support heartbeat PDUs
    +help                             Print help
    +home-drive                       Enable Redirect user home as share
    /ipv4[: [:force]]                 Prefer IPv4 A record over IPv6 AAAA
                                      record
    /ipv6[: [:force]]                 Prefer IPv6 AAAA record over IPv4 A
                                      record
    +jpeg                             JPEG codec support
    /jpeg-quality: <percentage>       JPEG quality
    /kbd: [layout:[0x<id>|<name>],lang:<0x<id>>,fn-key:<value>,type:<value>,
          subtype:<value>,unicode[:on|off],remap:<key1>=<value1>,
          remap:<key2>=<value2>,pipe:<filename>]
                                      Keyboard related options:
                                       * layout: set the keybouard layout
                                      announced to the server
                                       * lang: set the keyboard language
                                      identifier sent to the server
                                       * fn-key: Function key value
                                       * remap: RDP scancode to another one.
                                      Use /list:kbd-scancode to get the
                                      mapping. Example: To switch 'a' and 's'
                                      on a US keyboard:
                                      /kbd:remap:0x1e=0x1f,remap:0x1f=0x1e
                                       * pipe: Name of a named pipe that can be
                                      used to type text into the RDP session
    /kerberos: [kdc-url:<url>,lifetime:<time>,start-time:<time>,
               renewable-lifetime:<time>,cache:<path>,armor:<path>,
               pkinit-anchors:<path>,pkcs11-module:<name>]
                                      Kerberos options
    /list: [kbd|kbd-scancode|kbd-lang[:<value>]|smartcard[:[
           pkinit-anchors:<path>][,pkcs11-module:<name>]]
           |monitor|tune|timezones]   List available options for subcommand
    /load-balance-info: <info-string> Load balance info
    /log-filters: <tag>:<level>[,<tag>:<level>[,...]]
                                      Set logger filters, see wLog(7) for
                                      details
    /log-level: [OFF|FATAL|ERROR|WARN|INFO|DEBUG|TRACE]
                                      Set the default log level, see wLog(7)
                                      for details
    /max-fast-path-size: <size>       Specify maximum fast-path update size
    /max-loop-time: <time>            Specify maximum time in milliseconds
                                      spend treating packets
    +menu-anims                       Enable menu animations
    /microphone[: [sys:<sys>,][dev:<dev>,][format:<format>,][rate:<rate>,][
                  channel:<channel>]] Audio input (microphone)
    /monitors: <id>[,<id>[,...]]      [experimental] Select monitors to use
                                      (only effective in fullscreen or
                                      multimonitor mode)
    /mouse: [relative:[on|off],grab:[on|off]]
                                      Mouse related options:
                                       * relative:   send relative mouse
                                      movements if supported by server
                                       * grab:       grab the mouse if within
                                      the window
    -mouse-motion                     Disable Send mouse motion events
    +mouse-relative                   Enable Send mouse motion with relative
                                      addressing
    /multimon[: force]                Use multiple monitors
    +multitouch                       Enable Redirect multitouch input
    -multitransport                   Disable Support multitransport protocol
    -nego                             Disable protocol security negotiation
    /network: [invalid|modem|broadband|broadband-low|broadband-high|wan|lan|auto]
                                      Network connection type
    +nsc                              NSCodec support
    +old-license                      Enable Use the old license workflow (no
                                      CAL and hwId set to 0)
    /orientation: [0|90|180|270]      Orientation of display in degrees
    /p[: <password>]                  Password. Pass /p without arguments to
                                      silences interactive password prompts if
                                      no credentials are required for the
                                      connection.
    /parallel[: <name>[,<path>]]      Redirect parallel device
    /parent-window: <window-id>       Parent window id
    /pcb: <blob>                      Preconnection Blob
    /pcid: <id>                       Preconnection Id
    /pheight: <height>                Physical height of display (in
```

### `freerdp-shadow-cli3`

> 官方示例调用：`freerdp-shadow-cli3 -h`

```text
root@kali:~# freerdp-shadow-cli3 -h
Usage: freerdp-shadow-cli3 [options]
Notes: By default NLA security is active.
	In this mode a SAM database is required.
	Provide one with /sam-file:<file with path>
	else the default path /etc/FreeRDP/FreeRDP/SAM is used.
	If there is no existing SAM file authentication for all users will fail.
	If authentication against PAM is desired, start with -sec-nla (requires compiled in support for PAM)
Syntax:
    /flag (enables flag)
    /option:<value> (specifies option with value)
    +toggle -toggle (enables or disables toggle, where '/' is a synonym of '+')
    -auth (default:on)
	Clients must authenticate
    /bind-address:<bind-address>[,<another address>, ...]
	An address to bind to. Use '[<ipv6>]' for IPv6 addresses, e.g. '[::1]' for localhost
    +bitmap-compat (default:off)
	Limit BitmapUpdate to 1 rectangle (fixes broken windows 11 24H2 clients)
    /buildconfig
	Print the build configuration
    /ccache:<file>
	Kerberos host ccache file for NLA authentication
    -gfx (default:on)
	Allow GFX pipeline
    -gfx-avc420 (default:on)
	Allow GFX AVC420 codec
    -gfx-avc444 (default:on)
	Allow GFX AVC444 codec
    -gfx-planar (default:on)
	Allow GFX planar codec
    -gfx-progressive (default:on)
	Allow GFX progressive codec
    -gfx-rfx (default:on)
	Allow GFX RFX codec
    /help
	Print help
    /ipc-socket:<ipc-socket>
	Server IPC socket
    /keytab:<file>
	Kerberos keytab file for NLA authentication
    /log-filters:<tag>:<level>[,<tag>:<level>[,...]]
	Set logger filters, see wLog(7) for details
    /log-level:[OFF|FATAL|ERROR|WARN|INFO|DEBUG|TRACE]
	Set the default log level, see wLog(7) for details
    /max-connections:<number>
	maximum connections allowed to server, 0 to deactivate
    -may-interact (default:on)
	Clients may interact without prompt
    -may-view (default:on)
	Clients may view without prompt
    /monitors:<0,1,2...>
	Select or list monitors
    +mouse-relative (default:off)
	enable support for relative mouse events
    -nsc (default:on)
	Allow NSC codec
    /port:<number>
	Server port
    /rect:<x,y,w,h>
	Select rectangle within monitor to share
    +remote-guard (default:off)
	Remote credential guard
    -restricted-admin (default:on)
	Restricted Admin
    -rfx (default:on)
	Allow RFX surface bits
    /sam-file:<file>
	NTLM SAM file for NLA authentication
    /sec:<rdp|tls|nla|ext>
	force specific protocol security
    +sec-ext (default:off)
	nla extended protocol security
    -sec-nla (default:on)
	nla protocol security
    -sec-rdp (default:on)
	rdp protocol security
    -sec-tls (default:on)
	tls protocol security
    +server-side-cursor (default:off)
	hide mouse cursor in RDP client.
    /tls-secrets-file:<file>
	file where tls secrets shall be stored
    /version
	Print version
    /vmconnect
	Hyper-V console server (bind on vsock://1)
```

### `xfreerdp3`

> 官方示例调用：`xfreerdp3 --help`

```text
root@kali:~# xfreerdp3 --help
xfreerdp3 - A Free Remote Desktop Protocol Implementation
See www.freerdp.com for more information
Usage: xfreerdp3 [file] [options] [/v:<server>[:port]]
Syntax:
    /flag (enables flag)
    /option:<value> (specifies option with value)
    +toggle -toggle (enables or disables toggle, where '/' is a synonym of '+')
    /a: <addin>[,<options>]           Addin
    /action-script: <file-name>       Action script
    +admin                            Admin (or console) session
    +aero                             Enable desktop composition
    /app: program:[<path>|<||alias>],cmd:<command>,file:<filename>,guid:<guid>,
          icon:<filename>,name:<name>,workdir:<directory>,hidef:[on|off]
                                      Remote application program
    /args-from: file:<file>|stdin|fd:<number>|env:<name>
                                      Read command line from a file, stdin or
                                      file descriptor. This argument can not be
                                      combined with any other. Provide one
                                      argument per line.
    /assistance: <password>           Remote assistance password
    +async-channels                   Enable Asynchronous channels
                                      (experimental)
    +async-update                     Enable Asynchronous update
    /audio-mode: [[none|2]|[server|1]|[redirect|0]]
                                      Audio output mode
    +auth-only                        Enable Authenticate only
    /auth-pkg-list: [[none],]<!ntlm,kerberos,!u2u>
                                      Authentication package filter
                                      (comma-separated list, use '!' to
                                      disable). By default all methods are
                                      enabled. Use explicit 'none' as first
                                      argument to disable all methods,
                                      selectively enabling only the ones
                                      following.
    -authentication                   Disable Authentication (experimental)
    +auto-reconnect                   Enable Automatic reconnection
    /auto-reconnect-max-retries: <retries>
                                      Automatic reconnection maximum retries, 0
                                      for unlimited [0,1000]
    +auto-request-control             Automatically request remote assistance
                                      input control
    /azure: [tenantid:<id>],[use-tenantid[:[on|off]],[ad:<url>][
            avd-access:<format string>],[avd-token:<format string>],[
            avd-scope:<format string>] AzureAD options
    /bpp: <depth>                     Session bpp (color depth)
    +buildconfig                      Print the build configuration
    /cache: [bitmap[:on|off],codec[:rfx|nsc],glyph[:on|off],offscreen[:on|off],
            persist,persist-file:<filename>]
    /cert: [deny,ignore,name:<name>,tofu,fingerprint:<hash>:<hash as hex>[,
           fingerprint:<hash>:<another hash>]]
                                      Certificate accept options. Use with
                                      care!
                                       * deny         ... Automatically abort
                                      connection if the certificate does not
                                      match, no user interaction.
                                       * ignore       ... Ignore the
                                      certificate checks altogether (overrules
                                      all other options)
                                       * name         ... Use the alternate
                                      <name> instead of the certificate subject
                                      to match locally stored certificates
                                       * tofu         ... Accept certificate
                                      unconditionally on first connect and deny
                                      on subsequent connections if the
                                      certificate does not match
                                       * fingerprints ... A list of certificate
                                      hashes that are accepted unconditionally
                                      for a connection
    /client-build-number: <number>    Client Build Number sent to server
                                      (influences smartcard behaviour, see
                                      [MS-RDPESC])
    /client-hostname: <name>          Client Hostname to send to server
    [-|/]clipboard[: [[use-selection:<atom>],[direction-to:[
                     all|local|remote|off]],[files-to[:all|local|remote|off]]]]
                                      Disable Redirect clipboard:
                                       * use-selection:<atom>  ... (X11)
                                      Specify which X selection to access.
                                      Default is CLIPBOARD. PRIMARY is the
                                      X-style middle-click selection.
                                       * direction-to:[all|local|remote|off]
                                      control enabled clipboard direction
                                       * files-to:[all|local|remote|off]
                                      control enabled file clipboard direction
    -compression                      Disable compression
    /compression-level: <level>       Compression level (0,1,2)
    +credentials-delegation           Enable credentials delegation
    /d: <domain>                      Domain
    -decorations                      Disable Window decorations
    +disable-output                   Deactivate all graphics decoding in the
                                      client session. Useful for load tests
                                      with many simultaneous connections
    +disp                             Display control
    /drive: <name>,<path>             Redirect directory <path> as named share
                                      <name>. Hotplug support is enabled with
                                      /drive:hotplug,*. This argument provides
                                      the same function as "Drives that I plug
                                      in later" option in MSTSC.
    +drives                           Enable Redirect all mount points as
                                      shares
    /dump: <record|replay>,file:<file>[,nodelay]
                                      record or replay dump
    /dvc: <channel>[,<options>]       Dynamic virtual channel
    +dynamic-resolution               Enable Send resolution updates when the
                                      window is resized
    +echo                             Echo channel
    -encryption                       Disable Encryption (experimental)
    /encryption-methods: [40,][56,][128,][FIPS]
                                      RDP standard security encryption methods
    /endpointfedauth: <token>         Endpoint FedAuth token for Hyper-V VM
                                      console-connect scenarios
    +f                                Fullscreen mode (<Ctrl>+<Alt>+<Enter>
                                      toggles fullscreen)
    +fipsmode                         Enable FIPS mode
    /floatbar[: sticky:[on|off],default:[visible|hidden],show:[
                always|fullscreen|window]]
                                      floatbar is disabled by default (when
                                      enabled defaults to sticky in fullscreen
                                      mode)
    -fonts                            Disable smooth fonts (ClearType)
    +force-console-callbacks          Enable Use default callbacks (console)
                                      for certificate/credential/...
    /frame-ack: <number>              Number of frame acknowledgement
    /from-stdin[: force]              Read credentials from stdin. With <force>
                                      the prompt is done before connection,
                                      otherwise on server request.
    /gateway: g:<gateway>[:<port>],u:<user>,d:<domain>,p:<password>,
              usage-method:[direct|detect],access-token:<token>,type:[rpc|http[,
              no-websockets][,extauth-sspi-ntlm]|auto[,no-websockets][,
              extauth-sspi-ntlm]]|arm,url:<wss://url>,
              bearer:<oauth2-bearer-token>
                                      Gateway Hostname
    /gdi: sw|hw                       GDI rendering
    +geometry                         Geometry tracking channel
    +gestures                         Enable Consume multitouch input locally
    /gfx[: [[progressive[:on|off]|RFX[:on|off]|AVC420[:on|off]AVC444[:on|off]],
           mask:<value>,small-cache[:on|off],thin-client[:on|off],progressive[
           :on|off],frame-ack[:on|off]]
                                      RDP8 graphics pipeline
    -grab-keyboard                    Disable Grab keyboard focus, forward all
                                      keys to remote
    -grab-mouse                       Disable Grab mouse focus, forward all
                                      events to remote
    /h: <height>                      Height
    -heartbeat                        Disable Support heartbeat PDUs
    +help                             Print help
    +home-drive                       Enable Redirect user home as share
    /ipv4[: [:force]]                 Prefer IPv4 A record over IPv6 AAAA
                                      record
    /ipv6[: [:force]]                 Prefer IPv6 AAAA record over IPv4 A
                                      record
    +jpeg                             JPEG codec support
    /jpeg-quality: <percentage>       JPEG quality
    /kbd: [layout:[0x<id>|<name>],lang:<0x<id>>,fn-key:<value>,type:<value>,
          subtype:<value>,unicode[:on|off],remap:<key1>=<value1>,
          remap:<key2>=<value2>,pipe:<filename>]
                                      Keyboard related options:
                                       * layout: set the keybouard layout
                                      announced to the server
                                       * lang: set the keyboard language
                                      identifier sent to the server
                                       * fn-key: Function key value
                                       * remap: RDP scancode to another one.
                                      Use /list:kbd-scancode to get the
                                      mapping. Example: To switch 'a' and 's'
                                      on a US keyboard:
                                      /kbd:remap:0x1e=0x1f,remap:0x1f=0x1e
                                       * pipe: Name of a named pipe that can be
                                      used to type text into the RDP session
    /kerberos: [kdc-url:<url>,lifetime:<time>,start-time:<time>,
               renewable-lifetime:<time>,cache:<path>,armor:<path>,
               pkinit-anchors:<path>,pkcs11-module:<name>]
                                      Kerberos options
    /list: [kbd|kbd-scancode|kbd-lang[:<value>]|smartcard[:[
           pkinit-anchors:<path>][,pkcs11-module:<name>]]
           |monitor|tune|timezones]   List available options for subcommand
    /load-balance-info: <info-string> Load balance info
    /log-filters: <tag>:<level>[,<tag>:<level>[,...]]
                                      Set logger filters, see wLog(7) for
                                      details
    /log-level: [OFF|FATAL|ERROR|WARN|INFO|DEBUG|TRACE]
                                      Set the default log level, see wLog(7)
                                      for details
    /max-fast-path-size: <size>       Specify maximum fast-path update size
    /max-loop-time: <time>            Specify maximum time in milliseconds
                                      spend treating packets
    +menu-anims                       Enable menu animations
    /microphone[: [sys:<sys>,][dev:<dev>,][format:<format>,][rate:<rate>,][
                  channel:<channel>]] Audio input (microphone)
    /monitors: <id>[,<id>[,...]]      [experimental] Select monitors to use
                                      (only effective in fullscreen or
                                      multimonitor mode)
    /mouse: [relative:[on|off],grab:[on|off]]
                                      Mouse related options:
                                       * relative:   send relative mouse
                                      movements if supported by server
                                       * grab:       grab the mouse if within
                                      the window
    -mouse-motion                     Disable Send mouse motion events
    +mouse-relative                   Enable Send mouse motion with relative
                                      addressing
    /multimon[: force]                Use multiple monitors
    +multitouch                       Enable Redirect multitouch input
    -multitransport                   Disable Support multitransport protocol
    -nego                             Disable protocol security negotiation
    /network: [invalid|modem|broadband|broadband-low|broadband-high|wan|lan|auto]
                                      Network connection type
    +nsc                              NSCodec support
    +old-license                      Enable Use the old license workflow (no
                                      CAL and hwId set to 0)
    /orientation: [0|90|180|270]      Orientation of display in degrees
    /p[: <password>]                  Password. Pass /p without arguments to
                                      silences interactive password prompts if
                                      no credentials are required for the
                                      connection.
    /parallel[: <name>[,<path>]]      Redirect parallel device
    /parent-window: <window-id>       Parent window id
    /pcb: <blob>                      Preconnection Blob
    /pcid: <id>                       Preconnection Id
    /pheight: <height>                Physical height of display (in
```

### `winpr-hash`

> 官方示例调用：`winpr-hash --help`

```text
root@kali:~# winpr-hash --help
missing username or password
winpr-hash: NTLM hashing tool
Usage: winpr-hash -u <username> -p <password> [-d <domain>] [-f <_default_,sam>] [-v <_1_,2>]
```

## 4. 实践清单

按顺序做完这五步，就能把工具从「装上」推进到「会用」：

- [ ] **1.** **装好并确认版本** —— `sudo apt install freerdp-proxy`，再执行 `freerdp-proxy --version` 2>/dev/null || `freerdp-proxy -V`
- [ ] **2.** **读官方帮助** —— `freerdp-proxy -h`，需要细节时 `man freerdp-proxy`
- [ ] **3.** **在自有靶场跑最小用例** —— 官方给出的调用形式是：`Usage:`
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/freerdp3/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/defense-evasion.md`](../../tools/by-attack/defense-evasion.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/freerdp3/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/freerdp3/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
