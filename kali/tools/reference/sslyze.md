# sslyze

> Fast and full-featured SSL scanner SSLyze is a Python tool that can analyze the SSL configuration of a server by connecting to it. It is designed to be fast and comprehensive, and should help organizations and testers identify misconfigura…

> **功能分类**：信息搜集 ｜ **Kali 包**：`sslyze` ｜ **官方文档**：<https://www.kali.org/tools/sslyze/>

## 1. 安装

```bash
sudo apt update
sudo apt install sslyze
```

| 项目 | 内容 |
|------|------|
| 版本 | 6.3.1 |
| 架构 | all |
| 可执行命令 | `sslyze` |
| 依赖 | `libjs-sphinxdoc`、`python3`、`python3-cryptography`、`python3-nassl`、`python3-pkg-resources`、`python3-pydantic`、`python3-tls-parser`、`python3-typing-extensions` |
| 安装体积 | 2.19 MB |
| 官网 | <https://github.com/nabla-c0d3/sslyze> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/sslyze> |
| 包追踪 | <https://pkg.kali.org/pkg/sslyze> |

## 2. 官方用法示例

> 以下为 Kali 官方工具页给出的示例与输出原文。

```text
Usage Example
Launch a regular scan type (–regular) against the target host (www.example.com):
root@kali:~# sslyze --regular www.example.com

 REGISTERING AVAILABLE PLUGINS
 -----------------------------

  PluginCompression
  PluginCertInfo
  PluginSessionResumption
  PluginSessionRenegotiation
  PluginOpenSSLCipherSuites



 CHECKING HOST(S) AVAILABILITY
 -----------------------------

   www.example.com:443                 => 93.184.216.119:443



 SCAN RESULTS FOR WWW.EXAMPLE.COM:443 - 93.184.216.119:443
 ---------------------------------------------------------

  * Compression :
        Compression Support:      Disabled

  * Certificate :
      Validation w/ Mozilla's CA Store:  Certificate is Trusted
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `sslyze`

> 官方示例调用：`sslyze --regular www.example.com`

```text
root@kali:~# sslyze --regular www.example.com
 REGISTERING AVAILABLE PLUGINS
 -----------------------------
  PluginCompression
  PluginCertInfo
  PluginSessionResumption
  PluginSessionRenegotiation
  PluginOpenSSLCipherSuites
 CHECKING HOST(S) AVAILABILITY
 -----------------------------
   www.example.com:443                 => 93.184.216.119:443
 SCAN RESULTS FOR WWW.EXAMPLE.COM:443 - 93.184.216.119:443
 ---------------------------------------------------------
  * Compression :
        Compression Support:      Disabled
  * Certificate :
      Validation w/ Mozilla's CA Store:  Certificate is Trusted
```

### `sslyze -h`

> 官方示例调用：`sslyze -h`

```text
root@kali:~# sslyze -h
usage: sslyze [-h] [--update_trust_stores] [--cert CERTIFICATE_FILE]
              [--key KEY_FILE] [--keyform KEY_FORMAT] [--pass PASSPHRASE]
              [--json_out JSON_FILE] [--targets_in TARGET_FILE] [--quiet]
              [--slow_connection] [--https_tunnel PROXY_SETTINGS]
              [--starttls PROTOCOL] [--xmpp_to HOSTNAME]
              [--sni SERVER_NAME_INDICATION] [--tlsv1_3] [--resum]
              [--resum_attempts RESUM_ATTEMPTS] [--certinfo]
              [--certinfo_ca_file CERTINFO_CA_FILE] [--fallback] [--robot]
              [--tlsv1_1] [--reneg] [--tlsv1_2] [--sslv3] [--heartbleed]
              [--elliptic_curves] [--openssl_ccs] [--compression]
              [--http_headers] [--early_data] [--tlsv1] [--ems] [--sslv2]
              [--custom_tls_config CUSTOM_TLS_CONFIG]
              [--mozilla_config {modern,intermediate,old,disable}]
              [target ...]
SSLyze version 6.3.1
positional arguments:
  target                The list of servers to scan.
options:
  -h, --help            show this help message and exit
  --custom_tls_config CUSTOM_TLS_CONFIG
                        Path to a JSON file containing a specific TLS
                        configuration to check the server against, following
                        Mozilla's format. Cannot be used with
                        --mozilla_config.
  --mozilla_config {modern,intermediate,old,disable}
                        Shortcut to queue various scan commands needed to
                        check the server's TLS configurations against one of
                        Mozilla's recommended TLS configurations. Set to
                        "intermediate" by default. Use "disable" to disable
                        this check.
Trust stores options:
  --update_trust_stores
                        Update the default trust stores used by SSLyze. The
                        latest stores will be downloaded from https://github.c
                        om/nabla-c0d3/trust_stores_observatory. This option is
                        meant to be used separately, and will silence any
                        other command line option supplied to SSLyze.
Client certificate options:
  --cert CERTIFICATE_FILE
                        Client certificate chain filename. The certificates
                        must be in PEM format and must be sorted starting with
                        the subject's client certificate, followed by
                        intermediate CA certificates if applicable.
  --key KEY_FILE        Client private key filename.
  --keyform KEY_FORMAT  Client private key format. DER or PEM (default).
  --pass PASSPHRASE     Client private key passphrase.
Input and output options:
  --json_out JSON_FILE  Write the scan results as a JSON document to the file
                        JSON_FILE. If JSON_FILE is set to '-', the JSON output
                        will instead be printed to stdout. The resulting JSON
                        file is a serialized version of the ScanResult objects
                        described in SSLyze's Python API: the nodes and
                        attributes will be the same. See https://nabla-
                        c0d3.github.io/sslyze/documentation/available-scan-
                        commands.html for more details.
  --targets_in TARGET_FILE
                        Read the list of targets to scan from the file
                        TARGET_FILE. It should contain one host:port per line.
  --quiet               Do not output anything to stdout; useful when using
                        --json_out.
Connectivity options:
  --slow_connection     Greatly reduce the number of concurrent connections
                        initiated by SSLyze. This will make the scans slower
                        but more reliable if the connection between your host
                        and the server is slow, or if the server cannot handle
                        many concurrent connections. Enable this option if you
                        are getting a lot of timeouts or errors.
  --https_tunnel PROXY_SETTINGS
                        Tunnel all traffic to the target server(s) through an
                        HTTP CONNECT proxy. HTTP_TUNNEL should be the proxy's
                        URL: 'http://USER:PW@HOST:PORT/'. For proxies
                        requiring authentication, only Basic Authentication is
                        supported.
  --starttls PROTOCOL   Perform a StartTLS handshake when connecting to the
                        target server(s). StartTLS should be one of: auto,
                        smtp, xmpp, xmpp_server, pop3, imap, ftp, ldap, rdp,
                        postgres. The 'auto' option will cause SSLyze to
                        deduce the protocol (ftp, imap, etc.) from the
                        supplied port number, for each target server.
  --xmpp_to HOSTNAME    Optional setting for STARTTLS XMPP. XMPP_TO should be
                        the hostname to be put in the 'to' attribute of the
                        XMPP stream. Default is the server's hostname.
  --sni SERVER_NAME_INDICATION
                        Use Server Name Indication to specify the hostname to
                        connect to. Will only affect TLS 1.0+ connections.
Scan commands:
  --tlsv1_3             Test a server for TLS 1.3 support.
  --resum               Test a server for TLS 1.2 session resumption support
                        using session IDs and TLS tickets.
  --resum_attempts RESUM_ATTEMPTS
                        To be used with --resum. Number of session resumptions
                        (both with Session IDs and TLS Tickets) that SSLyze
                        should attempt. The default value is 5, but a higher
                        value such as 100 can be used to get a more accurate
                        measure of how often session resumption succeeds or
                        fails with the server.
  --certinfo            Retrieve and analyze a server's certificate(s) to
                        verify its validity.
  --certinfo_ca_file CERTINFO_CA_FILE
                        To be used with --certinfo. Path to a file containing
                        root certificates in PEM format that will be used to
                        verify the validity of the server's certificate.
  --fallback            Test a server for the TLS_FALLBACK_SCSV mechanism to
                        prevent downgrade attacks.
  --robot               Test a server for the ROBOT vulnerability.
  --tlsv1_1             Test a server for TLS 1.1 support.
  --reneg               Test a server for insecure TLS renegotiation and
                        client-initiated renegotiation.
  --tlsv1_2             Test a server for TLS 1.2 support.
  --sslv3               Test a server for SSL 3.0 support.
  --heartbleed          Test a server for the OpenSSL Heartbleed
                        vulnerability.
  --elliptic_curves     Test a server for supported elliptic curves.
  --openssl_ccs         Test a server for the OpenSSL CCS Injection
                        vulnerability (CVE-2014-0224).
  --compression         Test a server for TLS compression support, which can
                        be leveraged to perform a CRIME attack.
  --http_headers        Test a server for the presence of security-related
                        HTTP headers.
  --early_data          Test a server for TLS 1.3 early data support.
  --tlsv1               Test a server for TLS 1.0 support.
  --ems                 Test a server for TLS Extended Master Secret extension
                        support.
  --sslv2               Test a server for SSL 2.0 support.
Updated on: 2026-Aug-25
 Edit this page
sslscan
sstimap
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install sslyze`，再执行 `sslyze --version` 2>/dev/null || `sslyze -V`
- [ ] **2.** **读官方帮助** —— `sslyze -h`，需要细节时 `man sslyze`
- [ ] **3.** **在自有靶场跑最小用例** —— 用 `sslyze -h` 里最简单的那个子命令试一次
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/sslyze/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/discovery.md`](../../tools/by-attack/discovery.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/sslyze/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/sslyze/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
