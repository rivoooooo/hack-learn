# goshs

> SimpleHTTPServer written in Go This tool provides a SimpleHTTPServer written in Go, enhanced with features and security. This package contains a simple http server like the Python SimpleHTTPServer but enhanced with a lot of helpful feature…

> **功能分类**：通用工具 ｜ **Kali 包**：`goshs` ｜ **官方文档**：<https://www.kali.org/tools/goshs/>

## 1. 安装

```bash
sudo apt update
sudo apt install goshs
```

| 项目 | 内容 |
|------|------|
| 版本 | 2.1.6 |
| 架构 | any |
| 可执行命令 | `goshs` |
| 依赖 | `libc6` |
| 安装体积 | 22.84 MB |
| 官网 | <https://github.com/patrickhener/goshs> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/goshs> |
| 包追踪 | <https://pkg.kali.org/pkg/goshs> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
goshs -h          # 查看用法
man goshs         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `goshs`

官方给出的调用示例：`goshs -h`

```text
root@kali:~# goshs -h
goshs v2.1.6
Usage: goshs [options]
Web server options:
  -i,  --ip             IP or Interface to listen on              (default: 0.0.0.0)
  -p,  --port           The port to listen on                     (default: 8000)
  -d,  --dir            The web root directory                    (default: current working path)
  -w,  --webdav         Also serve using webdav protocol          (default: false)
  -wp, --webdav-port    The port to listen on for webdav          (default: 8001)
  -ro, --read-only      Read only mode, no upload possible        (default: false)
  -uo, --upload-only    Upload only mode, no download possible    (default: false)
  -uf, --upload-folder  Specify a different upload folder         (default: current working path)
  -mu, --max-upload     Maximum upload size in bytes, 0=unlimited (default: 0)
  -nc, --no-chat        Disable the team chat                     (default: false)
  -pc, --persist-chat   Persist chat to disk (.goshs-chat/)       (default: false)
  -pci,--persist-chat-images  Write pasted chat images to disk   (default: false)
  -nd, --no-delete      Disable the delete option                 (default: false)
  -si, --silent         Running without dir listing               (default: false)
  -I,  --invisible      Invisible mode                            (default: false)
  -c,  --cli            Enable cli (only with auth and tls)       (default: false)
  --catcher, -rc        Enable reverse shell catcher              (default: false)
  -e,  --embedded       Show embedded files in UI                 (default: false)
  -o,  --output         Write output to logfile                   (default: false)
  -t,  --tunnel         Enable tunnel                             (default: false)
TLS options:
  -s,     --ssl           Use TLS
  -ss,    --self-signed   Use a self-signed certificate
  -sk,    --server-key    Path to server key
  -sc,    --server-cert   Path to server certificate
  -p12,   --pkcs12        Path to server p12
  -p12np, --p12-no-pass   Server p12 has empty password
  -sl,    --lets-encrypt  Use Let's Encrypt as certification service
  -sld,   --le-domains    Domain(s) to request from Let's Encrypt	   (comma separated list)
  -sle,   --le-email      Email to use with Let's Encrypt
  -slh,   --le-http       Port to use for Let's Encrypt HTTP Challenge	   (default: 80)
  -slt,   --le-tls        Port to use for Let's Encrypt TLS ALPN Challenge (default: 443)
FTP/SFTP server options:
  -ftp                          Activate FTP server capabilities          (default: false)
  -ftp-port                     The port FTP/SFTP listens on              (default: 2121)
  -ftp-sftp                     Switch to SFTP instead of plain FTP       (default: false)
  -fkf, --ftp-keyfile           Authorized_keys file for SFTP pubkey auth
  -fhk, --ftp-host-keyfile      SSH host key file for SFTP identification
TFTP server options:
  -tftp, --tftp-server          Activate TFTP server capabilities         (default: false)
  -tftp-port                    The port TFTP listens on                  (default: 69)
SMB server options:
  -smb                        Activate SMB server capabilities         (default: false)
  -smb-port,   --smb-port     The port SMB listens on                  (default: 445)
  -smb-domain, --smb-domain   The domain to use for SMB authentication (default: WORKGROUP)
  -smb-share,  --smb-share    The share to use for SMB authentication  (default: goshs)
  -smb-wordlist               Wordlist file for quick hash cracking    (default: none)
LDAP server options:
  -ldap, --ldap-server         Activate LDAP credential capture server (default: false)
  -ldap-port                   The port LDAP listens on                 (default: 389)
  -ldap-jndi                   Enable dynamic JNDI mode — baseDN in the search becomes the
                               factory class name, fetched from the goshs HTTP server
  -ldap-jndi-base              Override codeBase URL for JNDI payloads  (default: auto)
  -ldap-wordlist               Wordlist file for quick LDAP NTLM hash cracking
  Use -s -ss or -s -sc/-sk to enable LDAPS (TLS) on default port 636
Authentication options:
  -b,  --basic-auth     Use basic authentication (user:pass - user can be empty)
  -ca, --cert-auth      Use certificate based authentication - provide ca certificate
  -H,  --hash           Hash a password for file based ACLs
Connection restriction:
  -ipw, --ip-whitelist             Comma separated list of IPs to whitelist
  -tpw, --trusted-proxy-whitelist  Comma separated list of trusted proxies
Collaboration options:
  -dns, --dns-server           Enable DNS server                   (default: false)
  -dns-port, --dns-port        DNS server port                     (default: 8053)
  -dns-ip, --dns-ip            DNS server Reply IP                 (default: 127.0.0.1)
  -smtp, --smtp-server         Enable SMTP server                  (default: false)
  -smtp-port, --smtp-port      SMTP server port                    (default: 2525)
  -smtp-domain, --smtp-domain  SMTP server domain                  (default: open relay)
Webhook options:
  -W,  --webhook            Enable webhook support                      (default: false)
  -Wu, --webhook-url        URL to send webhook requests to
  -We, --webhook-events     Comma separated list of events to notify
                            [all, upload, delete, download, view, webdav,
                            ftp, smb, dns, smtp, redirect, verbose]	    (default: all)
  -Wp, --webhook-provider   Webhook provider
                            [Discord, Mattermost, Slack]                (default: Discord)
Payload templating:
      --template      Render {{.VAR}} placeholders in files requested with ?tpl (default: false)
      --tpl-var       Template variable KEY=VALUE (repeatable), e.g. LPORT=4444
                      LHOST defaults to -i when a single IP is bound; on 0.0.0.0 pass --tpl-var LHOST=
Misc options:
  -C  --config        Provide config file path                (default: false)
  -P  --print-config  Print sample config to STDOUT           (default: false)
  -u  --user          Drop privs to user (unix only)          (default: current user)
      --update        Update goshs to most recent version
  -m  --mdns          Enable zeroconf mDNS registration       (default: false)
      --tui           Run the interactive terminal dashboard  (default: false)
      --ttl           Self-destruct after a duration, e.g. 30m, 2h (default: disabled)
  -V  --verbose       Activate verbose log output             (default: false)
  -v                  Print the current goshs version
      --completion    Install shell tab completion (bash|fish|zsh)
Usage examples:
  Start with default values:    	./goshs
  Start with config file:    	        ./goshs -C /path/to/config.yaml
  Start with wevdav support:    	./goshs -w
  Start with different port:    	./goshs -p 8080
  Start with self-signed cert:  	./goshs -s -ss
  Start with let's encrypt:		./goshs -s -sl -sle
[email protected]
 -sld your.domain.com,your.seconddomain.com
  Start with custom cert:       	./goshs -s -sk <path to key> -sc <path to cert>
  Start with basic auth:        	./goshs -b 'secret-user:$up3r$3cur3'
  Start with basic auth bcrypt hash:   	./goshs -b 'secret-user:$2a$14$ydRJ//Ob4SctB/D7o.rvU.LmPs/vwXkeXCbtpCqzgOJDSShLgiY52'
  Start with basic auth empty user:	./goshs -b ':$up3r$3cur3'
  Start with cli enabled:           	./goshs -b 'secret-user:$up3r$3cur3' -s -ss -c
  Start with payload templating:    	./goshs -i 10.10.14.7 --template --tpl-var LPORT=4444
Updated on: 2026-Aug-25
 Edit this page
gophish
gospider
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install goshs`，再执行 `goshs --version` 2>/dev/null || `goshs -V`
- [ ] **2.** **读官方帮助** —— `goshs -h`，需要细节时 `man goshs`
- [ ] **3.** **在自有靶场跑最小用例** —— 官方给出的调用形式是：`Usage: goshs [options]`
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/goshs/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/exfiltration.md`](../../tools/by-attack/exfiltration.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/goshs/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/goshs/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
