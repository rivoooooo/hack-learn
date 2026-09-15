# proxify

> Swiss Army knife Proxy tool for HTTP/HTTPS traffic capture, manipulation This package contains a Swiss Army Knife Proxy for rapid deployments. It supports multiple operations such as request/response dump, filtering and manipulation via DS…

> **功能分类**：通用工具 ｜ **Kali 包**：`proxify` ｜ **官方文档**：<https://www.kali.org/tools/proxify/>

## 1. 安装

```bash
sudo apt update
sudo apt install proxify
```

| 项目 | 内容 |
|------|------|
| 版本 | 0.0.5 |
| 架构 | any |
| 可执行命令 | `proxify`、`mitmrelay`、`replay-proxify` |
| 依赖 | `libc6`、`mitmrelay` |
| 安装体积 | 35.08 MB |
| 官网 | <https://github.com/projectdiscovery/proxify> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/proxify> |
| 包追踪 | <https://pkg.kali.org/pkg/proxify> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
proxify -h          # 查看用法
man proxify         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 3 个可执行命令，下面是官方页面内嵌的帮助原文。

### `mitmrelay`

官方给出的调用示例：`mitmrelay -h`

```text
root@kali:~# mitmrelay -h
Usage of mitmrelay:
  -client-cert string
    	Relay => Server Cert File
  -client-key string
    	Relay => Server Key File
  -dns-addr string
    	Listen DNS Ip and port (ip:port) (default ":5353")
  -dns-mapping string
    	DNS A mapping (eg domain:ip,domain:ip,..)
  -http-addr string
    	HTTP Server Listen Address (default "127.0.0.1:49999")
  -output string
    	Output Folder (default "logs/")
  -protocol string
    	tcp or udp (default "tcp")
  -proxy-addr string
    	HTTP Proxy Address
  -relay value
    	listen_ip:listen_port => destination_ip:destination_port
  -request-match-replace-dsl string
    	Request Match-Replace DSL
  -resolver-addr string
    	Listen DNS Ip and port (ip:port)
  -response-match-replace-dsl string
    	Request Match-Replace DSL
  -server-cert string
    	Client => Relay Cert File
  -server-key string
    	Client => Relay Key File
  -timeout int
    	Connection Timeout In Seconds (default 180)
  -tls-client
    	Relay => Server should use tls
  -tls-server
    	Client => Relay should use tls
```

### `proxify`

官方给出的调用示例：`proxify -h`

```text
root@kali:~# proxify -h
Swiss Army Knife Proxy for rapid deployments. Supports multiple operations such as request/response dump,filtering and manipulation via DSL language, upstream HTTP/Socks5 proxy
Usage:
  proxify [flags]
Flags:
OUTPUT:
   -o, -output string  Output Directory to store HTTP proxy logs (default "logs")
   -dump-req           Dump only HTTP requests to output file
   -dump-resp          Dump only HTTP responses to output file
FILTER:
   -req-fd, -request-dsl string                   Request Filter DSL
   -resp-fd, -response-dsl string                 Response Filter DSL
   -req-mrd, -request-match-replace-dsl string    Request Match-Replace DSL
   -resp-mrd, -response-match-replace-dsl string  Response Match-Replace DSL
NETWORK:
   -ha, -http-addr string    Listening HTTP IP and Port address (ip:port) (default "127.0.0.1:8888")
   -sa, -socks-addr string   Listening SOCKS IP and Port address (ip:port) (default "127.0.0.1:10080")
   -da, -dns-addr string     Listening DNS IP and Port address (ip:port)
   -dm, -dns-mapping string  Domain to IP DNS mapping (eg domain:ip,domain:ip,..)
   -r, -resolver string      Custom DNS resolvers to use (ip:port)
PROXY:
   -hp, -http-proxy string    Upstream HTTP Proxies (eg http://proxy-ip:proxy-port
   -sp, -socks5-proxy string  Upstream SOCKS5 Proxies (eg socks5://proxy-ip:proxy-port)
   -c int                     Number of requests before switching to the next upstream proxy (default 1)
EXPORT:
   -elastic-address string    elasticsearch address (ip:port)
   -elastic-ssl               enable elasticsearch ssl
   -elastic-ssl-verification  enable elasticsearch ssl verification
   -elastic-username string   elasticsearch username
   -elastic-password string   elasticsearch password
   -elastic-index string      elasticsearch index name (default "proxify")
   -kafka-address string      address of kafka broker (ip:port)
   -kafka-topic string        kafka topic to publish messages on (default "proxify")
CONFIGURATION:
   -config string        Directory for storing program information (default "/root/.config/proxify")
   -cert-cache-size int  Number of certificates to cache (default 256)
   -allow string         Allowed list of IP/CIDR's to be proxied
   -deny string          Denied list of IP/CIDR's to be proxied
DEBUG:
   -silent         Silent
   -nc, -no-color  No Color (default true)
   -version        Version
   -v, -verbose    Verbose
```

### `replay-proxify`

官方给出的调用示例：`replay-proxify -h`

```text
root@kali:~# replay-proxify -h
Usage of replay-proxify:
  -burp-addr string
    	Burp HTTP Address (default "http://127.0.0.1:8080")
  -dns-addr string
    	DNS UDP Server Listen Address (default ":10000")
  -http-addr string
    	HTTP Server Listen Address (default ":80")
  -output string
    	Output Folder (default "db/")
  -proxy-addr string
    	HTTP Proxy Server Listen Address (default ":8081")
Updated on: 2025-Dec-09
 Edit this page
princeprocessor
proximoth
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install proxify`，再执行 `proxify --version` 2>/dev/null || `proxify -V`
- [ ] **2.** **读官方帮助** —— `proxify -h`，需要细节时 `man proxify`
- [ ] **3.** **在自有靶场跑最小用例** —— 官方给出的调用形式是：`Usage of mitmrelay:`
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/proxify/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/proxify/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/proxify/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
