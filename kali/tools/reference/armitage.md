# armitage

> Cyber attack management for Metasploit Armitage is a scriptable red team collaboration tool for Metasploit that visualizes targets, recommends exploits, and exposes the advanced post- exploitation features in the framework.

> **功能分类**：漏洞利用 ｜ **Kali 包**：`armitage` ｜ **官方文档**：<https://www.kali.org/tools/armitage/>

## 1. 安装

```bash
sudo apt update
sudo apt install armitage
```

| 项目 | 内容 |
|------|------|
| 版本 | 20221206 |
| 架构 | all |
| 可执行命令 | `armitage`、`teamserver` |
| 依赖 | `metasploit-framework`、`openjdk-11-jre`、`teamserver` |
| 安装体积 | 10.95 MB |
| 官网 | <https://github.com/r00t0v3rr1d3/armitage> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/armitage> |
| 包追踪 | <https://pkg.kali.org/pkg/armitage> |

## 2. 官方用法示例

> 以下为 Kali 官方工具页给出的示例与输出原文。

```text
Usage Example
root@kali:~# armitage
[*] Starting msfrpcd for you.

teamserver Usage Example
Start teamserver on the external IP (192.168.1.202) and set the server password (s3cr3t):
root@kali:~# teamserver 192.168.1.202 s3cr3t
[*] Generating X509 certificate and keystore (for SSL)
[*] Starting RPC daemon
[*] MSGRPC starting on 127.0.0.1:55554 (NO SSL):Msg...
[*] MSGRPC backgrounding at 2014-05-14 15:05:46 -0400...
[*] sleeping for 20s (to let msfrpcd initialize)
[*] Starting Armitage team server
[-] Java 1.6 is not supported with this tool. Please upgrade to Java 1.7
[*] Use the following connection details to connect your clients:
    Host: 192.168.1.202
    Port: 55553
    User: msf
    Pass: s3cr3t

[*] Fingerprint (check for this string when you connect):
    a3b60bef430037a6b628d9011924341b8c09081
[+] multi-player metasploit... ready to go
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 2 个可执行命令，下面是官方页面内嵌的帮助原文。

### `armitage`

```text
root@kali:~# armitage
[*] Starting msfrpcd for you.
teamserver Usage Example
Start teamserver on the external IP (
192.168.1.202
) and set the server password (
s3cr3t
):
```

### `teamserver`

官方给出的调用示例：`teamserver 192.168.1.202 s3cr3t`

```text
root@kali:~# teamserver 192.168.1.202 s3cr3t
[*] Generating X509 certificate and keystore (for SSL)
[*] Starting RPC daemon
[*] MSGRPC starting on 127.0.0.1:55554 (NO SSL):Msg...
[*] MSGRPC backgrounding at 2014-05-14 15:05:46 -0400...
[*] sleeping for 20s (to let msfrpcd initialize)
[*] Starting Armitage team server
[-] Java 1.6 is not supported with this tool. Please upgrade to Java 1.7
[*] Use the following connection details to connect your clients:
    Host: 192.168.1.202
    Port: 55553
    User: msf
    Pass: s3cr3t
[*] Fingerprint (check for this string when you connect):
    a3b60bef430037a6b628d9011924341b8c09081
[+] multi-player metasploit... ready to go
```

### `teamserver（示例）`

官方给出的调用示例：`teamserver -h`

```text
root@kali:~# teamserver -h
[*] You must provide: <external IP address> <team password>
    <external IP address> must be reachable by Armitage
          clients on port 55553
    <team password> is a shared password your team uses to
          authenticate to the Armitage team server
Updated on: 2025-Dec-09
 Edit this page
apple-bleee
asleap
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install armitage`，再执行 `armitage --version` 2>/dev/null || `armitage -V`
- [ ] **2.** **读官方帮助** —— `armitage -h`，需要细节时 `man armitage`
- [ ] **3.** **在自有靶场跑最小用例** —— 用 `armitage -h` 里最简单的那个子命令试一次
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/armitage/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/execution.md`](../../tools/by-attack/execution.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/armitage/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/armitage/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
