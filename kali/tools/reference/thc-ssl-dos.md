# thc-ssl-dos

> Stress tester for the SSL handshake THC-SSL-DOS is a tool to verify the performance of SSL. Establishing a secure SSL connection requires 15x more processing power on the server than on the client. THC-SSL-DOS exploits this asymmetric prop…

> **功能分类**：漏洞分析 ｜ **Kali 包**：`thc-ssl-dos` ｜ **官方文档**：<https://www.kali.org/tools/thc-ssl-dos/>

## 1. 安装

```bash
sudo apt update
sudo apt install thc-ssl-dos
```

| 项目 | 内容 |
|------|------|
| 版本 | 1.4 |
| 架构 | any |
| 可执行命令 | `thc-ssl-dos` |
| 依赖 | `libc6`、`libpcap0.8t64`、`libssl3t64`、`openssl` |
| 安装体积 | 35 KB |
| 官网 | <http://www.thc.org/thc-ssl-dos/> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/thc-ssl-dos> |
| 包追踪 | <https://pkg.kali.org/pkg/thc-ssl-dos> |

## 2. 官方用法示例

> 以下为 Kali 官方工具页给出的示例与输出原文。

```text
Usage Example
Using 100 connections (-l 100), flood the target IP (192.168.1.208) and port (443):
root@kali:~# thc-ssl-dos -l 100 192.168.1.208 443 --accept
     ______________ ___  _________
     \__    ___/   |   \ \_   ___ \
       |    | /    ~    \/    \  \/
       |    | \    Y    /\     \____
       |____|  \___|_  /  \______  /
                     \/          \/
            http://www.thc.org

          Twitter @hackerschoice

Greetingz: the french underground

Waiting for script kiddies to piss off................
The force is with those who read the source...
Handshakes 0 [0.00 h/s], 1 Conn, 0 Err
Handshakes 2 [2.90 h/s], 6 Conn, 0 Err
Handshakes 25 [22.42 h/s], 13 Conn, 0 Err
Handshakes 70 [43.97 h/s], 20 Conn, 0 Err
Handshakes 125 [56.51 h/s], 27 Conn, 0 Err
Handshakes 185 [62.09 h/s], 33 Conn, 0 Err
Handshakes 262 [74.56 h/s], 41 Conn, 0 Err
Handshakes 365 [104.93 h/s], 47 Conn, 0 Err
Handshakes 496 [131.23 h/s], 54 Conn, 0 Err
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `thc-ssl-dos`

官方给出的调用示例：`thc-ssl-dos -l 100 192.168.1.208 443 --accept`

```text
root@kali:~# thc-ssl-dos -l 100 192.168.1.208 443 --accept
     ______________ ___  _________
     \__    ___/   |   \ \_   ___ \
       |    | /    ~    \/    \  \/
       |    | \    Y    /\     \____
       |____|  \___|_  /  \______  /
                     \/          \/
            http://www.thc.org
          Twitter @hackerschoice
Greetingz: the french underground
Waiting for script kiddies to piss off................
The force is with those who read the source...
Handshakes 0 [0.00 h/s], 1 Conn, 0 Err
Handshakes 2 [2.90 h/s], 6 Conn, 0 Err
Handshakes 25 [22.42 h/s], 13 Conn, 0 Err
Handshakes 70 [43.97 h/s], 20 Conn, 0 Err
Handshakes 125 [56.51 h/s], 27 Conn, 0 Err
Handshakes 185 [62.09 h/s], 33 Conn, 0 Err
Handshakes 262 [74.56 h/s], 41 Conn, 0 Err
Handshakes 365 [104.93 h/s], 47 Conn, 0 Err
Handshakes 496 [131.23 h/s], 54 Conn, 0 Err
```

### `thc-ssl-dos（示例）`

官方给出的调用示例：`thc-ssl-dos -h`

```text
root@kali:~# thc-ssl-dos -h
     ______________ ___  _________
     \__    ___/   |   \ \_   ___ \
       |    | /    ~    \/    \  \/
       |    | \    Y    /\     \____
       |____|  \___|_  /  \______  /
                     \/          \/
            http://www.thc.org
          Twitter @hackerschoice
Greetingz: the french underground
Updated on: 2026-Mar-02
 Edit this page
thc-pptp-bruter
tnscmd10g
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install thc-ssl-dos`，再执行 `thc-ssl-dos --version` 2>/dev/null || `thc-ssl-dos -V`
- [ ] **2.** **读官方帮助** —— `thc-ssl-dos -h`，需要细节时 `man thc-ssl-dos`
- [ ] **3.** **在自有靶场跑最小用例** —— 用 `thc-ssl-dos -h` 里最简单的那个子命令试一次
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/thc-ssl-dos/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/impact.md`](../../tools/by-attack/impact.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/thc-ssl-dos/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/thc-ssl-dos/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
