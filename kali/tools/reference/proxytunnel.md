# proxytunnel

> Help SSH and other protocols through HTTP(S) proxies Proxytunnel creates tunnels through HTTP(S) proxies for any TCP based protocol. It comes in handy when one sits behind a firewall that allows for HTTP(S) traffic only. The program connec…

> **功能分类**：Web 应用 ｜ **Kali 包**：`proxytunnel` ｜ **官方文档**：<https://www.kali.org/tools/proxytunnel/>

## 1. 安装

```bash
sudo apt update
sudo apt install proxytunnel
```

| 项目 | 内容 |
|------|------|
| 版本 | 1.13.0 |
| 架构 | any |
| 可执行命令 | `proxytunnel` |
| 依赖 | `libc6`、`libssl3t64` |
| 安装体积 | 98 KB |
| 官网 | <https://proxytunnel.sourceforge.io/> |
| 源码仓库 | <https://salsa.debian.org/pkg-security-team/proxytunnel> |
| 包追踪 | <https://pkg.kali.org/pkg/proxytunnel> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
proxytunnel -h          # 查看用法
man proxytunnel         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `proxytunnel`

官方给出的调用示例：`proxytunnel -h`

```text
root@kali:~# proxytunnel -h
proxytunnel 1.13.0 Copyright 2001-2026 Proxytunnel Project
Usage: proxytunnel [OPTIONS]...
Build generic tunnels through HTTPS proxies using HTTP authentication
Standard options:
 -i, --inetd                Run from inetd (default: off)
 -a, --standalone=STRING    Run as standalone daemon on specified port or
                            address:port combination
 -p, --proxy=STRING         Local proxy host:port combination
 -r, --remproxy=STRING      Remote proxy host:port combination (using 2 proxies)
 -d, --dest=STRING          Destination host:port combination
 -e, --encrypt              SSL encrypt data between local proxy and destination
 -E, --encrypt-proxy        SSL encrypt data between client and local proxy
 -X, --encrypt-remproxy     SSL encrypt data between local and remote proxy
Additional options for specific features:
 -z, --no-check-certificate Don't verify server SSL certificate
 -C, --cacert=STRING        Path to trusted CA certificate or directory
 -4, --ipv4                 Enforce IPv4 connection to local proxy
 -6, --ipv6                 Enforce IPv6 connection to local proxy
 -F, --passfile=STRING      File with credentials for proxy authentication
 -P, --proxyauth=STRING     Proxy auth credentials user:pass combination
 -R, --remproxyauth=STRING  Remote proxy auth credentials user:pass combination
 -c, --cert=FILENAME        client SSL certificate (chain)
 -k, --key=FILENAME         client SSL key
 -N, --ntlm                 Use NTLM based authentication
 -t, --domain=STRING        NTLM domain (default: autodetect)
 -H, --header=STRING        Add additional HTTP headers to send to proxy
 -o, --host=STRING          Send custom Host Header/SNI
 -x, --proctitle=STRING     Use a different process title
 -I, --no-sni               Disable SNI
Miscellaneous options:
 -v, --verbose              Turn on verbosity
 -q, --quiet                Suppress messages
 -h, --help                 Print help and exit
 -V, --version              Print version and exit
Updated on: 2026-Aug-25
 Edit this page
proxychains-ng
pyinstaller
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install proxytunnel`，再执行 `proxytunnel --version` 2>/dev/null || `proxytunnel -V`
- [ ] **2.** **读官方帮助** —— `proxytunnel -h`，需要细节时 `man proxytunnel`
- [ ] **3.** **在自有靶场跑最小用例** —— 官方给出的调用形式是：`Usage: proxytunnel [OPTIONS]...`
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/proxytunnel/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/command-and-control.md`](../../tools/by-attack/command-and-control.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/proxytunnel/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/proxytunnel/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
