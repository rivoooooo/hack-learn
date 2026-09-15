# ligolo-ng

> Advanced, yet simple, tunneling/pivoting tool that uses a TUN interface Ligolo-ng is a simple, lightweight and fast tool that allows pentesters to establish tunnels from a reverse TCP/TLS connection using a tun interface (without the need …

> **功能分类**：通用工具 ｜ **Kali 包**：`ligolo-ng` ｜ **官方文档**：<https://www.kali.org/tools/ligolo-ng/>

## 1. 安装

```bash
sudo apt update
sudo apt install ligolo-ng
```

| 项目 | 内容 |
|------|------|
| 版本 | 0.9.1 |
| 架构 | amd64 |
| 可执行命令 | `ligolo-ng`、`ligolo-agent`、`ligolo-proxy` |
| 依赖 | `libc6`、`ligolo-agent` |
| 安装体积 | 26.49 MB |
| 官网 | <https://github.com/nicocha30/ligolo-ng> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/ligolo-ng> |
| 包追踪 | <https://pkg.kali.org/pkg/ligolo-ng> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
ligolo-ng -h          # 查看用法
man ligolo-ng         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 3 个可执行命令，下面是官方页面内嵌的帮助原文。

### `ligolo-agent`

> 官方示例调用：`ligolo-agent -h`

```text
root@kali:~# ligolo-agent -h
  -accept-fingerprint string
    	accept certificates matching the following SHA256 fingerprint (hex format)
  -bind string
    	bind to ip:port
  -connect string
    	connect to proxy (domain:port)
  -ignore-cert
    	ignore TLS certificate validation (dangerous), only for debug purposes
  -proxy string
    	proxy URL address (http://admin:
[email protected]
:8080) or socks://admin:
[email protected]
:8080
  -reconnect
    	auto-reconnect after established connection is lost (default true)
  -reconnect-delay int
    	reconnection delay in seconds (default: 20) (default 20)
  -reconnect-timeout int
    	total reconnection timeout in seconds (default: 300 = 5 minutes) (default 300)
  -retry
    	auto-retry on initial connection error
  -retry-delay int
    	retry delay in seconds for initial connection (default: 5) (default 5)
  -ua string
    	HTTP User-Agent (default "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36")
  -v	enable verbose mode
  -version
    	show the current version
```

### `ligolo-proxy`

> 官方示例调用：`ligolo-proxy -h`

```text
root@kali:~# ligolo-proxy -h
  -allow-domains string
    	autocert authorised domains, if empty, allow all domains, multiple domains should be comma-separated.
  -api-laddr string
    	API server listening address (default: 127.0.0.1:8080)
  -autocert
    	automatically request letsencrypt certificates, requires port 80 to be accessible
  -certfile string
    	TLS server certificate (default "certs/cert.pem")
  -config string
    	the config file to use
  -cpuprofile file
    	write cpu profile to file
  -daemon
    	run as daemon mode (no CLI)
  -history string
    	readline history file
  -keyfile string
    	TLS server key (default "certs/key.pem")
  -laddr string
    	listening address (prefix with http(s):// for websocket) (default "0.0.0.0:11601")
  -max-inflight int
    	maximum number of in-flight TCP connection requests per tunnel (default 4096)
  -memprofile file
    	write memory profile to file
  -nobanner
    	don't show banner on startup
  -selfcert
    	dynamically generate self-signed certificates
  -selfcert-cache string
    	directory used to cache self-signed certificates
  -selfcert-domain string
    	The selfcert TLS domain to use (default "ligolo")
  -v	enable verbose mode
  -version
    	show the current version
Learn more with
OffSec
Want to learn more about ligolo-ng? get access to in-depth training and hands-on labs:
SkillForge (Lab)
Hugs (Lab)
Updated on: 2026-Aug-25
 Edit this page
lapsdumper
ligolo-ng-common-binaries
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install ligolo-ng`，再执行 `ligolo-ng --version` 2>/dev/null || `ligolo-ng -V`
- [ ] **2.** **读官方帮助** —— `ligolo-ng -h`，需要细节时 `man ligolo-ng`
- [ ] **3.** **在自有靶场跑最小用例** —— 用 `ligolo-ng -h` 里最简单的那个子命令试一次
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/ligolo-ng/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- **精讲教程**（含原理、参数详解、靶场实操与输出解读）：[ligolo-ng](../../tools/tutorials/08-后渗透/ligolo-ng.md)
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/command-and-control.md`](../../tools/by-attack/command-and-control.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/ligolo-ng/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/ligolo-ng/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
