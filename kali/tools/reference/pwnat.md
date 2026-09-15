# pwnat

> NAT to NAT client-server communication pwnat, pronounced “poe-nat”, is a tool that allows any number of clients behind NATs to communicate with a server behind a separate NAT with no port forwarding

> **功能分类**：后渗透 ｜ **Kali 包**：`pwnat` ｜ **官方文档**：<https://www.kali.org/tools/pwnat/>

## 1. 安装

```bash
sudo apt update
sudo apt install pwnat
```

| 项目 | 内容 |
|------|------|
| 版本 | 0.3.0 |
| 架构 | any |
| 可执行命令 | `pwnat` |
| 依赖 | `libc6` |
| 安装体积 | 65 KB |
| 官网 | <https://samy.pl/pwnat/> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/pwnat> |
| 包追踪 | <https://pkg.kali.org/pkg/pwnat> |

## 2. 官方用法示例

> 以下为 Kali 官方工具页给出的示例与输出原文。

```text
Usage Example
On the server, run in server mode (-s) on port 8080 (8080.
On the client, run in client mode (-c) on local port 8000 (8000), connect to the server IP (192.168.1.202) on port 8080 (8080) and use it to connect to google.com on port 80 (google.com 80).
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `pwnat`

官方给出的调用示例：`pwnat -s 8080`

```text
root@kali:~# pwnat -s 8080
Listening on UDP 0.0.0.0:8080
```

### `pwnat（示例）`

官方给出的调用示例：`pwnat -c 8000 192.168.1.202 8080 google.com 80`

```text
root@kali:~# pwnat -c 8000 192.168.1.202 8080 google.com 80
Listening on TCP 0.0.0.0:8000
New connection(1): tcp://127.0.0.1:41318 -> udp://192.168.1.202:8080
```

### `pwnat（示例）`

官方给出的调用示例：`pwnat -h`

```text
root@kali:~# pwnat -h
usage: pwnat <-s | -c> <args>
  -c    client mode (default)
        <args>: [local ip] <local port> <proxy host> [proxy port (def:2222)] <remote host> <remote port>
  -s    server mode
        <args>: [local ip] [proxy port (def:2222)] [[allowed host]:[allowed port] ...]
  -6    use IPv6
  -v    show debug output (up to 2)
  -a    reuse address
  -p    reuse port
  -h    show this help and exit
Updated on: 2025-Dec-09
 Edit this page
ptunnel
pwncat
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install pwnat`，再执行 `pwnat --version` 2>/dev/null || `pwnat -V`
- [ ] **2.** **读官方帮助** —— `pwnat -h`，需要细节时 `man pwnat`
- [ ] **3.** **在自有靶场跑最小用例** —— 用 `pwnat -h` 里最简单的那个子命令试一次
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/pwnat/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/command-and-control.md`](../../tools/by-attack/command-and-control.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/pwnat/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/pwnat/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
