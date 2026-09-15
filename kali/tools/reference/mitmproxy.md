# mitmproxy

> SSL-capable man-in-the-middle HTTP proxy mitmproxy is an interactive man-in-the-middle proxy for HTTP and HTTPS. It provides a console interface that allows traffic flows to be inspected and edited on the fly. Also shipped is mitmdump, the…

> **功能分类**：信息搜集 ｜ **Kali 包**：`mitmproxy` ｜ **官方文档**：<https://www.kali.org/tools/mitmproxy/>

## 1. 安装

```bash
sudo apt update
sudo apt install mitmproxy
```

| 项目 | 内容 |
|------|------|
| 版本 | 12.2.3 |
| 架构 | all |
| 可执行命令 | `mitmproxy`、`mitmdump`、`mitmweb` |
| 依赖 | `dpkg`、`fonts-font-awesome`、`python3`、`python3-aioquic`、`python3-argon2`、`python3-asgiref`、`python3-bcrypt`、`python3-brotli`、`python3-certifi`、`python3-cryptography`、`python3-flask`、`python3-h11` 等 |
| 安装体积 | 4.96 MB |
| 官网 | <https://mitmproxy.org> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/mitmproxy> |
| 包追踪 | <https://pkg.kali.org/pkg/mitmproxy> |

## 2. 官方用法示例

> 以下为 Kali 官方工具页给出的示例与输出原文。

```text
Usage Example
Run mitmproxy listening (p) on port2139.
root@kali:~# mitmproxy -p 2139
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 3 个可执行命令，下面是官方页面内嵌的帮助原文。

### `mitmproxy`

官方给出的调用示例：`mitmproxy -p 2139`

```text
root@kali:~# mitmproxy -p 2139
```

### `mitmdump`

官方给出的调用示例：`mitmdump -h`

```text
root@kali:~# mitmdump -h
usage: mitmdump [options] [filter]
positional arguments:
  filter_args           Filter expression, equivalent to setting both the
                        view_filter and save_stream_filter options.
options:
  -h, --help            show this help message and exit
  --version             show version number and exit
  --options             Show all options and their default values
  --commands            Show all commands and their signatures
  --set option[=value]  Set an option. When the value is omitted, booleans are
                        set to true, strings and integers are set to None (if
                        permitted), and sequences are emptied. Boolean values
                        can be true, false or toggle. Sequences are set using
                        multiple invocations to set for the same option.
  -q, --quiet           Quiet.
  -v, --verbose         Increase log verbosity.
  --mode, -m MODE       The proxy server type(s) to spawn. Can be passed
                        multiple times. Mitmproxy supports "regular" (HTTP),
                        "local", "transparent", "socks5", "reverse:SPEC",
                        "upstream:SPEC", and "wireguard[:PATH]" proxy servers.
                        For reverse and upstream proxy modes, SPEC is host
                        specification in the form of "http[s]://host[:port]".
                        For WireGuard mode, PATH may point to a file
                        containing key material. If no such file exists, it
                        will be created on startup. You may append
                        `@listen_port` or `@listen_host:listen_port` to
                        override `listen_host` or `listen_port` for a specific
                        proxy mode. Features such as client playback will use
                        the first mode to determine which upstream server to
                        use. May be passed multiple times.
  --no-anticache
  --anticache           Strip out request headers that might cause the server
                        to return 304-not-modified.
  --no-showhost
  --showhost            Use the Host header to construct URLs for display.
                        This option is disabled by default because malicious
                        apps may send misleading host headers to evade your
                        analysis. If this is not a concern, enable this
                        options for better flow display.
  --no-show-ignored-hosts
  --show-ignored-hosts  Record ignored flows in the UI even if we do not
                        perform TLS interception. This option will keep
                        ignored flows' contents in memory, which can greatly
                        increase memory usage. A future release will fix this
                        issue, record ignored flows by default, and remove
                        this option.
  --rfile, -r PATH      Read flows from file.
  --scripts, -s SCRIPT  Execute a script. May be passed multiple times.
  --stickycookie FILTER
                        Set sticky cookie filter. Matched against requests.
  --stickyauth FILTER   Set sticky auth filter. Matched against requests.
  --save-stream-file, -w PATH
                        Stream flows to file as they arrive. Prefix path with
                        + to append. The full path can use python strftime()
                        formating, missing directories are created as needed.
                        A new file is opened every time the formatted string
                        changes.
  --no-anticomp
  --anticomp            Try to convince servers to send us un-compressed data.
  --flow-detail LEVEL   The display detail level for flows in mitmdump: 0
                        (quiet) to 4 (very verbose). 0: no output 1: shortened
                        request URL with response status code 2: full request
                        URL with response status code and HTTP headers 3: 2 +
                        truncated response content, content of WebSocket and
                        TCP messages (content_view_lines_cutoff: 512) 4: 3 +
                        nothing is truncated
Proxy Options:
  --listen-host HOST    Address to bind proxy server(s) to (may be overridden
                        for individual modes, see `mode`).
  --listen-port, -p PORT
                        Port to bind proxy server(s) to (may be overridden for
                        individual modes, see `mode`). By default, the port is
                        mode-specific. The default regular HTTP proxy spawns
                        on port 8080.
  --no-server, -n
  --server              Start a proxy server. Enabled by default.
  --ignore-hosts HOST   Ignore host and forward all traffic without processing
                        it. In transparent mode, it is recommended to use an
                        IP address (range), not the hostname. In regular mode,
                        only SSL traffic is ignored and the hostname should be
                        used. The supplied value is interpreted as a regular
                        expression and matched on the ip or the hostname. May
                        be passed multiple times.
  --allow-hosts HOST    Opposite of --ignore-hosts. May be passed multiple
                        times.
  --tcp-hosts HOST      Generic TCP SSL proxy mode for all hosts that match
                        the pattern. Similar to --ignore-hosts, but SSL
                        connections are intercepted. The communication
                        contents are printed to the log in verbose mode. May
                        be passed multiple times.
  --upstream-auth USER:PASS
                        Add HTTP Basic authentication to upstream proxy and
                        reverse proxy requests. Format: username:password.
  --proxyauth SPEC      Require proxy authentication. Format: "username:pass",
                        "any" to accept any user/pass combination, "@path" to
                        use an Apache htpasswd file, or "ldap[s]:url_server_ld
                        ap[:port]:dn_auth:password:dn_subtree[?search_filter_k
                        ey=...]" for LDAP authentication.
  --no-store-streamed-bodies
  --store-streamed-bodies
                        Store HTTP request and response bodies when streamed
                        (see `stream_large_bodies`). This increases memory
                        consumption, but makes it possible to inspect streamed
                        bodies.
  --no-rawtcp
  --rawtcp              Enable/disable raw TCP connections. TCP connections
                        are enabled by default.
  --no-http2
  --http2               Enable/disable HTTP/2 support. HTTP/2 support is
                        enabled by default.
SSL:
  --certs SPEC          SSL certificates of the form "[domain=]path". The
                        domain may include a wildcard, and is equal to "*" if
                        not specified. The file at path is a certificate in
                        PEM format. If a private key is included in the PEM,
                        it is used, else the default key in the conf dir is
                        used. The PEM file should contain the full certificate
                        chain, with the leaf certificate as the first entry.
                        May be passed multiple times.
  --cert-passphrase PASS
                        Passphrase for decrypting the private key provided in
                        the --cert option. Note that passing cert_passphrase
                        on the command line makes your passphrase visible in
                        your system's process list. Specify it in config.yaml
                        to avoid this.
  --no-ssl-insecure
  --ssl-insecure, -k    Do not verify upstream server SSL/TLS certificates. If
                        this option is enabled, certificate validation is
                        skipped and mitmproxy itself will be vulnerable to TLS
                        interception.
Client Replay:
  --client-replay, -C PATH
                        Replay client requests from a saved file. May be
                        passed multiple times.
Server Replay:
  --server-replay, -S PATH
                        Replay server responses from a saved file. May be
                        passed multiple times.
  --no-server-replay-kill-extra
  --server-replay-kill-extra
                        Kill extra requests during replay (for which no
                        replayable response was found).[Deprecated, prefer to
                        use server_replay_extra='kill']
  --server-replay-extra {forward,kill,204,400,404,500}
                        Behaviour for extra requests during replay for which
                        no replayable response was found. Setting a numeric
                        string value will return an empty HTTP response with
                        the respective status code.
  --no-server-replay-reuse
  --server-replay-reuse
                        Don't remove flows from server replay state after use.
                        This makes it possible to replay same response
                        multiple times.
  --no-server-replay-refresh
  --server-replay-refresh
                        Refresh server replay responses by adjusting date,
                        expires and last-modified headers, as well as
                        adjusting cookie expiration.
Map Remote:
  --map-remote, -M PATTERN
                        Map remote resources to another remote URL using a
                        pattern of the form "[/flow-filter]/url-
                        regex/replacement", where the separator can be any
                        character. May be passed multiple times.
Map Local:
  --map-local PATTERN   Map remote resources to a local file using a pattern
                        of the form "[/flow-filter]/url-regex/file-or-
                        directory-path", where the separator can be any
                        character. May be passed multiple times.
Modify Body:
  --modify-body, -B PATTERN
                        Replacement pattern of the form "[/flow-
                        filter]/regex/[@]replacement", where the separator can
                        be any character. The @ allows to provide a file path
                        that is used to read the replacement string. May be
                        passed multiple times.
Modify Headers:
  --modify-headers, -H PATTERN
                        Header modify pattern of the form "[/flow-
                        filter]/header-name/[@]header-value", where the
                        separator can be any character. The @ allows to
                        provide a file path that is used to read the header
                        value string. An empty header-value removes existing
                        header-name headers. May be passed multiple times.
```

### `mitmproxy（示例）`

官方给出的调用示例：`mitmproxy -h`

```text
root@kali:~# mitmproxy -h
usage: mitmproxy [options]
options:
  -h, --help            show this help message and exit
  --version             show version number and exit
  --options             Show all options and their default values
  --commands            Show all commands and their signatures
  --set option[=value]  Set an option. When the value is omitted, booleans are
                        set to true, strings and integers are set to None (if
                        permitted), and sequences are emptied. Boolean values
                        can be true, false or toggle. Sequences are set using
                        multiple invocations to set for the same option.
  -q, --quiet           Quiet.
  -v, --verbose         Increase log verbosity.
  --mode, -m MODE       The proxy server type(s) to spawn. Can be passed
                        multiple times. Mitmproxy supports "regular" (HTTP),
                        "local", "transparent", "socks5", "reverse:SPEC",
                        "upstream:SPEC", and "wireguard[:PATH]" proxy servers.
                        For reverse and upstream proxy modes, SPEC is host
                        specification in the form of "http[s]://host[:port]".
                        For WireGuard mode, PATH may point to a file
                        containing key material. If no such file exists, it
                        will be created on startup. You may append
                        `@listen_port` or `@listen_host:listen_port` to
                        override `listen_host` or `listen_port` for a specific
                        proxy mode. Features such as client playback will use
                        the first mode to determine which upstream server to
                        use. May be passed multiple times.
  --no-anticache
  --anticache           Strip out request headers that might cause the server
                        to return 304-not-modified.
  --no-showhost
  --showhost            Use the Host header to construct URLs for display.
                        This option is disabled by default because malicious
                        apps may send misleading host headers to evade your
                        analysis. If this is not a concern, enable this
                        options for better flow display.
  --no-show-ignored-hosts
  --show-ignored-hosts  Record ignored flows in the UI even if we do not
                        perform TLS interception. This option will keep
                        ignored flows' contents in memory, which can greatly
                        increase memory usage. A future release will fix this
                        issue, record ignored flows by default, and remove
                        this option.
  --rfile, -r PATH      Read flows from file.
  --scripts, -s SCRIPT  Execute a script. May be passed multiple times.
  --stickycookie FILTER
                        Set sticky cookie filter. Matched against requests.
  --stickyauth FILTER   Set sticky auth filter. Matched against requests.
  --save-stream-file, -w PATH
                        Stream flows to file as they arrive. Prefix path with
                        + to append. The full path can use python strftime()
                        formating, missing directories are created as needed.
                        A new file is opened every time the formatted string
                        changes.
  --no-anticomp
  --anticomp            Try to convince servers to send us un-compressed data.
  --console-layout {horizontal,single,vertical}
                        Console layout.
  --no-console-layout-headers
  --console-layout-headers
                        Show layout component headers
Proxy Options:
  --listen-host HOST    Address to bind proxy server(s) to (may be overridden
                        for individual modes, see `mode`).
  --listen-port, -p PORT
                        Port to bind proxy server(s) to (may be overridden for
                        individual modes, see `mode`). By default, the port is
                        mode-specific. The default regular HTTP proxy spawns
                        on port 8080.
  --no-server, -n
  --server              Start a proxy server. Enabled by default.
  --ignore-hosts HOST   Ignore host and forward all traffic without processing
                        it. In transparent mode, it is recommended to use an
                        IP address (range), not the hostname. In regular mode,
                        only SSL traffic is ignored and the hostname should be
                        used. The supplied value is interpreted as a regular
                        expression and matched on the ip or the hostname. May
                        be passed multiple times.
  --allow-hosts HOST    Opposite of --ignore-hosts. May be passed multiple
                        times.
  --tcp-hosts HOST      Generic TCP SSL proxy mode for all hosts that match
                        the pattern. Similar to --ignore-hosts, but SSL
                        connections are intercepted. The communication
                        contents are printed to the log in verbose mode. May
                        be passed multiple times.
  --upstream-auth USER:PASS
                        Add HTTP Basic authentication to upstream proxy and
                        reverse proxy requests. Format: username:password.
  --proxyauth SPEC      Require proxy authentication. Format: "username:pass",
                        "any" to accept any user/pass combination, "@path" to
                        use an Apache htpasswd file, or "ldap[s]:url_server_ld
                        ap[:port]:dn_auth:password:dn_subtree[?search_filter_k
                        ey=...]" for LDAP authentication.
  --no-store-streamed-bodies
  --store-streamed-bodies
                        Store HTTP request and response bodies when streamed
                        (see `stream_large_bodies`). This increases memory
                        consumption, but makes it possible to inspect streamed
                        bodies.
  --no-rawtcp
  --rawtcp              Enable/disable raw TCP connections. TCP connections
                        are enabled by default.
  --no-http2
  --http2               Enable/disable HTTP/2 support. HTTP/2 support is
                        enabled by default.
SSL:
  --certs SPEC          SSL certificates of the form "[domain=]path". The
                        domain may include a wildcard, and is equal to "*" if
                        not specified. The file at path is a certificate in
                        PEM format. If a private key is included in the PEM,
                        it is used, else the default key in the conf dir is
                        used. The PEM file should contain the full certificate
                        chain, with the leaf certificate as the first entry.
                        May be passed multiple times.
  --cert-passphrase PASS
                        Passphrase for decrypting the private key provided in
                        the --cert option. Note that passing cert_passphrase
                        on the command line makes your passphrase visible in
                        your system's process list. Specify it in config.yaml
                        to avoid this.
  --no-ssl-insecure
  --ssl-insecure, -k    Do not verify upstream server SSL/TLS certificates. If
                        this option is enabled, certificate validation is
                        skipped and mitmproxy itself will be vulnerable to TLS
                        interception.
Client Replay:
  --client-replay, -C PATH
                        Replay client requests from a saved file. May be
                        passed multiple times.
Server Replay:
  --server-replay, -S PATH
                        Replay server responses from a saved file. May be
                        passed multiple times.
  --no-server-replay-kill-extra
  --server-replay-kill-extra
                        Kill extra requests during replay (for which no
                        replayable response was found).[Deprecated, prefer to
                        use server_replay_extra='kill']
  --server-replay-extra {forward,kill,204,400,404,500}
                        Behaviour for extra requests during replay for which
                        no replayable response was found. Setting a numeric
                        string value will return an empty HTTP response with
                        the respective status code.
  --no-server-replay-reuse
  --server-replay-reuse
                        Don't remove flows from server replay state after use.
                        This makes it possible to replay same response
                        multiple times.
  --no-server-replay-refresh
  --server-replay-refresh
                        Refresh server replay responses by adjusting date,
                        expires and last-modified headers, as well as
                        adjusting cookie expiration.
Map Remote:
  --map-remote, -M PATTERN
                        Map remote resources to another remote URL using a
                        pattern of the form "[/flow-filter]/url-
                        regex/replacement", where the separator can be any
                        character. May be passed multiple times.
Map Local:
  --map-local PATTERN   Map remote resources to a local file using a pattern
                        of the form "[/flow-filter]/url-regex/file-or-
                        directory-path", where the separator can be any
                        character. May be passed multiple times.
Modify Body:
  --modify-body, -B PATTERN
                        Replacement pattern of the form "[/flow-
                        filter]/regex/[@]replacement", where the separator can
                        be any character. The @ allows to provide a file path
                        that is used to read the replacement string. May be
                        passed multiple times.
Modify Headers:
  --modify-headers, -H PATTERN
                        Header modify pattern of the form "[/flow-
                        filter]/header-name/[@]header-value", where the
                        separator can be any character. The @ allows to
                        provide a file path that is used to read the header
                        value string. An empty header-value removes existing
                        header-name headers. May be passed multiple times.
Filters:
  See help in mitmproxy for filter expression syntax.
  --intercept FILTER    Intercept filter expression.
  --view-filter FILTER  Limit the view to matching flows.
```

### `mitmweb`

官方给出的调用示例：`mitmweb -h`

```text
root@kali:~# mitmweb -h
usage: mitmweb [options]
options:
  -h, --help            show this help message and exit
  --version             show version number and exit
  --options             Show all options and their default values
  --commands            Show all commands and their signatures
  --set option[=value]  Set an option. When the value is omitted, booleans are
                        set to true, strings and integers are set to None (if
                        permitted), and sequences are emptied. Boolean values
                        can be true, false or toggle. Sequences are set using
                        multiple invocations to set for the same option.
  -q, --quiet           Quiet.
  -v, --verbose         Increase log verbosity.
  --mode, -m MODE       The proxy server type(s) to spawn. Can be passed
                        multiple times. Mitmproxy supports "regular" (HTTP),
                        "local", "transparent", "socks5", "reverse:SPEC",
                        "upstream:SPEC", and "wireguard[:PATH]" proxy servers.
                        For reverse and upstream proxy modes, SPEC is host
                        specification in the form of "http[s]://host[:port]".
                        For WireGuard mode, PATH may point to a file
                        containing key material. If no such file exists, it
                        will be created on startup. You may append
                        `@listen_port` or `@listen_host:listen_port` to
                        override `listen_host` or `listen_port` for a specific
                        proxy mode. Features such as client playback will use
                        the first mode to determine which upstream server to
                        use. May be passed multiple times.
  --no-anticache
  --anticache           Strip out request headers that might cause the server
                        to return 304-not-modified.
  --no-showhost
  --showhost            Use the Host header to construct URLs for display.
                        This option is disabled by default because malicious
                        apps may send misleading host headers to evade your
                        analysis. If this is not a concern, enable this
                        options for better flow display.
  --no-show-ignored-hosts
  --show-ignored-hosts  Record ignored flows in the UI even if we do not
                        perform TLS interception. This option will keep
                        ignored flows' contents in memory, which can greatly
                        increase memory usage. A future release will fix this
                        issue, record ignored flows by default, and remove
                        this option.
  --rfile, -r PATH      Read flows from file.
  --scripts, -s SCRIPT  Execute a script. May be passed multiple times.
  --stickycookie FILTER
                        Set sticky cookie filter. Matched against requests.
  --stickyauth FILTER   Set sticky auth filter. Matched against requests.
  --save-stream-file, -w PATH
                        Stream flows to file as they arrive. Prefix path with
                        + to append. The full path can use python strftime()
                        formating, missing directories are created as needed.
                        A new file is opened every time the formatted string
                        changes.
  --no-anticomp
  --anticomp            Try to convince servers to send us un-compressed data.
Mitmweb:
  --no-web-open-browser
  --web-open-browser    Start a browser.
  --web-port PORT       Web UI port.
  --web-host HOST       Web UI host.
Proxy Options:
  --listen-host HOST    Address to bind proxy server(s) to (may be overridden
                        for individual modes, see `mode`).
  --listen-port, -p PORT
                        Port to bind proxy server(s) to (may be overridden for
                        individual modes, see `mode`). By default, the port is
                        mode-specific. The default regular HTTP proxy spawns
                        on port 8080.
  --no-server, -n
  --server              Start a proxy server. Enabled by default.
  --ignore-hosts HOST   Ignore host and forward all traffic without processing
                        it. In transparent mode, it is recommended to use an
                        IP address (range), not the hostname. In regular mode,
                        only SSL traffic is ignored and the hostname should be
                        used. The supplied value is interpreted as a regular
                        expression and matched on the ip or the hostname. May
                        be passed multiple times.
  --allow-hosts HOST    Opposite of --ignore-hosts. May be passed multiple
                        times.
  --tcp-hosts HOST      Generic TCP SSL proxy mode for all hosts that match
                        the pattern. Similar to --ignore-hosts, but SSL
                        connections are intercepted. The communication
                        contents are printed to the log in verbose mode. May
                        be passed multiple times.
  --upstream-auth USER:PASS
                        Add HTTP Basic authentication to upstream proxy and
                        reverse proxy requests. Format: username:password.
  --proxyauth SPEC      Require proxy authentication. Format: "username:pass",
                        "any" to accept any user/pass combination, "@path" to
                        use an Apache htpasswd file, or "ldap[s]:url_server_ld
                        ap[:port]:dn_auth:password:dn_subtree[?search_filter_k
                        ey=...]" for LDAP authentication.
  --no-store-streamed-bodies
  --store-streamed-bodies
                        Store HTTP request and response bodies when streamed
                        (see `stream_large_bodies`). This increases memory
                        consumption, but makes it possible to inspect streamed
                        bodies.
  --no-rawtcp
  --rawtcp              Enable/disable raw TCP connections. TCP connections
                        are enabled by default.
  --no-http2
  --http2               Enable/disable HTTP/2 support. HTTP/2 support is
                        enabled by default.
SSL:
  --certs SPEC          SSL certificates of the form "[domain=]path". The
                        domain may include a wildcard, and is equal to "*" if
                        not specified. The file at path is a certificate in
                        PEM format. If a private key is included in the PEM,
                        it is used, else the default key in the conf dir is
                        used. The PEM file should contain the full certificate
                        chain, with the leaf certificate as the first entry.
                        May be passed multiple times.
  --cert-passphrase PASS
                        Passphrase for decrypting the private key provided in
                        the --cert option. Note that passing cert_passphrase
                        on the command line makes your passphrase visible in
                        your system's process list. Specify it in config.yaml
                        to avoid this.
  --no-ssl-insecure
  --ssl-insecure, -k    Do not verify upstream server SSL/TLS certificates. If
                        this option is enabled, certificate validation is
                        skipped and mitmproxy itself will be vulnerable to TLS
                        interception.
Client Replay:
  --client-replay, -C PATH
                        Replay client requests from a saved file. May be
                        passed multiple times.
Server Replay:
  --server-replay, -S PATH
                        Replay server responses from a saved file. May be
                        passed multiple times.
  --no-server-replay-kill-extra
  --server-replay-kill-extra
                        Kill extra requests during replay (for which no
                        replayable response was found).[Deprecated, prefer to
                        use server_replay_extra='kill']
  --server-replay-extra {forward,kill,204,400,404,500}
                        Behaviour for extra requests during replay for which
                        no replayable response was found. Setting a numeric
                        string value will return an empty HTTP response with
                        the respective status code.
  --no-server-replay-reuse
  --server-replay-reuse
                        Don't remove flows from server replay state after use.
                        This makes it possible to replay same response
                        multiple times.
  --no-server-replay-refresh
  --server-replay-refresh
                        Refresh server replay responses by adjusting date,
                        expires and last-modified headers, as well as
                        adjusting cookie expiration.
Map Remote:
  --map-remote, -M PATTERN
                        Map remote resources to another remote URL using a
                        pattern of the form "[/flow-filter]/url-
                        regex/replacement", where the separator can be any
                        character. May be passed multiple times.
Map Local:
  --map-local PATTERN   Map remote resources to a local file using a pattern
                        of the form "[/flow-filter]/url-regex/file-or-
                        directory-path", where the separator can be any
                        character. May be passed multiple times.
Modify Body:
  --modify-body, -B PATTERN
                        Replacement pattern of the form "[/flow-
                        filter]/regex/[@]replacement", where the separator can
                        be any character. The @ allows to provide a file path
                        that is used to read the replacement string. May be
                        passed multiple times.
Modify Headers:
  --modify-headers, -H PATTERN
                        Header modify pattern of the form "[/flow-
                        filter]/header-name/[@]header-value", where the
                        separator can be any character. The @ allows to
                        provide a file path that is used to read the header
                        value string. An empty header-value removes existing
                        header-name headers. May be passed multiple times.
Filters:
  See help in mitmproxy for filter expression syntax.
  --intercept FILTER    Intercept filter expression.
Updated on: 2026-Aug-25
 Edit this page
minicom
mssqlpwner
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
```

## 4. 实践清单

按顺序做完这五步，就能把工具从「装上」推进到「会用」：

- [ ] **1.** **装好并确认版本** —— `sudo apt install mitmproxy`，再执行 `mitmproxy --version` 2>/dev/null || `mitmproxy -V`
- [ ] **2.** **读官方帮助** —— `mitmproxy -h`，需要细节时 `man mitmproxy`
- [ ] **3.** **在自有靶场跑最小用例** —— 用 `mitmproxy -h` 里最简单的那个子命令试一次
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/mitmproxy/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- **精讲教程**（含原理、参数详解、靶场实操与输出解读）：[mitmproxy](../../tools/tutorials/07-嗅探与欺骗/mitmproxy.md)
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/collection.md`](../../tools/by-attack/collection.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/mitmproxy/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/mitmproxy/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
