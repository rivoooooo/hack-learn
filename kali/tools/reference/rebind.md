# rebind

> DNS rebinding tool Rebind is a tool that implements the multiple A record DNS rebinding attack. Although this tool was originally written to target home routers, it can be used to target any public (non RFC1918) IP address. Rebind provides…

> **功能分类**：嗅探与欺骗 ｜ **Kali 包**：`rebind` ｜ **官方文档**：<https://www.kali.org/tools/rebind/>

## 1. 安装

```bash
sudo apt update
sudo apt install rebind
```

| 项目 | 内容 |
|------|------|
| 版本 | 0.3.4 |
| 架构 | any |
| 可执行命令 | `rebind`、`dns-rebind` |
| 安装体积 | 2.64 MB |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/rebind> |
| 包追踪 | <https://pkg.kali.org/pkg/rebind> |

## 2. 官方用法示例

> 以下为 Kali 官方工具页给出的示例与输出原文。

```text
Usage Example
Use interface eth0 (-i eth0) to conduct the rebind attack with the specified domain (-d kali.local):
root@kali:~# rebind -i eth0 -d kali.local

[+] Starting DNS server on port 53
[+] Starting attack Web server on port 80
[+] Starting callback Web server on port 81
[+] Starting proxy server on 192.168.1.202:664
[+] Services started and running!

> dns
[+] 192.168.1.202       kali.local.
[+] 192.168.1.202       www.kali.local.
[+] 192.168.1.202       ns1.kali.local.
[+] 192.168.1.202       ns2.kali.local.
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 2 个可执行命令，下面是官方页面内嵌的帮助原文。

### `rebind`

> 官方示例调用：`rebind -i eth0 -d kali.local`

```text
root@kali:~# rebind -i eth0 -d kali.local
[+] Starting DNS server on port 53
[+] Starting attack Web server on port 80
[+] Starting callback Web server on port 81
[+] Starting proxy server on 192.168.1.202:664
[+] Services started and running!
> dns
[+] 192.168.1.202       kali.local.
[+] 192.168.1.202       www.kali.local.
[+] 192.168.1.202       ns1.kali.local.
[+] 192.168.1.202       ns2.kali.local.
```

### `dns-rebind`

> 官方示例调用：`dns-rebind -h`

```text
root@kali:~# dns-rebind -h
Rebind v0.3.4
Usage: dns-rebind [OPTIONS]
	-i <interface>	Specify the network interface to bind to
	-d <fqdn>     	Specify your registered domain name
	-u <user>     	Specify the Basic Authentication user name [admin]
	-a <pass>     	Specify the Basic Authentication password [admin]
	-r <path>     	Specify the initial URL request path [/]
	-t <ip>       	Specify a comma separated list of target IP addresses [client IP]
	-n <time>     	Specify the callback interval in milliseconds [2000]
	-p <port>     	Specify the target port [80]
	-c <port>     	Specify the callback port [81]
	-C <value>    	Specify a cookie to set for the client
	-H <file>     	Specify a file of HTTP headers for the client to send to the target
Updated on: 2026-Mar-02
 Edit this page
rainbowcrack
redfang
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install rebind`，再执行 `rebind --version` 2>/dev/null || `rebind -V`
- [ ] **2.** **读官方帮助** —— `rebind -h`，需要细节时 `man rebind`
- [ ] **3.** **在自有靶场跑最小用例** —— 官方给出的调用形式是：`Usage: dns-rebind [OPTIONS]`
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/rebind/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/initial-access.md`](../../tools/by-attack/initial-access.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/rebind/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/rebind/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
