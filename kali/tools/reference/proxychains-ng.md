# proxychains-ng

> Runtime shared library for proxychains-ng Proxychains is a UNIX program, that hooks network-related libc functions in dynamically linked programs via a preloaded DLL (dlsym(), LD_PRELOAD) and redirects the connections through SOCKS4a/5 or …

> **功能分类**：Web 应用 ｜ **Kali 包**：`proxychains-ng` ｜ **官方文档**：<https://www.kali.org/tools/proxychains-ng/>

## 1. 安装

```bash
sudo apt update
sudo apt install libproxychains4
```

| 项目 | 内容 |
|------|------|
| 版本 | 4.17 |
| 架构 | any |
| 可执行命令 | `libproxychains4`、`proxychains4`、`proxychains4-daemon` |
| 依赖 | `libc6`、`proxychains4` |
| 安装体积 | 71 KB |
| 官网 | <https://github.com/rofl0r/proxychains-ng> |
| 源码仓库 | <https://salsa.debian.org/debian/proxychains-ng> |
| 包追踪 | <https://pkg.kali.org/pkg/proxychains-ng> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
libproxychains4 -h          # 查看用法
man libproxychains4         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 3 个可执行命令，下面是官方页面内嵌的帮助原文。

### `proxychains4`

> 官方示例调用：`proxychains4 --help`

```text
root@kali:~# proxychains4 --help
Usage:	proxychains4 -q -f config_file program_name [arguments]
	-q makes proxychains quiet - this overrides the config setting
	-f allows one to manually specify a configfile to use
	for example : proxychains telnet somehost.com
More help in README file
```

### `proxychains4-daemon`

> 官方示例调用：`proxychains4-daemon -h`

```text
root@kali:~# proxychains4-daemon -h
Proxychains-NG remote dns daemon
--------------------------------
usage: proxychains4-daemon -i listenip -p port -r remotesubnet
all arguments are optional.
by default listenip is 127.0.0.1, port 1053 and remotesubnet 224.
Learn more with
OffSec
Want to learn more about proxychains-ng? get access to in-depth training and hands-on labs:
PEN-200: 19. Port Redirection and SSH Tunneling
PEN-200: 19. Port Redirection and SSH Tunneling
PEN-300: 17.1.2. Windows Lateral Movement: Reverse RDP Proxying with Metasploit
PEN-300: 18.3.4. Linux Lateral Movement: Using Kerberos with Impacket
PEN-200 course
PEN-300 course
Updated on: 2026-Aug-25
 Edit this page
proxmark3
proxytunnel
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install libproxychains4`，再执行 `libproxychains4 --version` 2>/dev/null || `libproxychains4 -V`
- [ ] **2.** **读官方帮助** —— `libproxychains4 -h`，需要细节时 `man libproxychains4`
- [ ] **3.** **在自有靶场跑最小用例** —— 官方给出的调用形式是：`Usage:	proxychains4 -q -f config_file program_name [arguments]`
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/proxychains-ng/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- **精讲教程**（含原理、参数详解、靶场实操与输出解读）：[proxychains4](../../tools/tutorials/08-后渗透/proxychains4.md)
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/command-and-control.md`](../../tools/by-attack/command-and-control.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/proxychains-ng/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/proxychains-ng/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
