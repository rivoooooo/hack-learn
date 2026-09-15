# crowbar

> Brute forcing tool This package contains Crowbar (formally known as Levye). It is a brute forcing tool that can be used during penetration tests. It was developed to brute force some protocols in a different manner according to other popul…

> **功能分类**：通用工具 ｜ **Kali 包**：`crowbar` ｜ **官方文档**：<https://www.kali.org/tools/crowbar/>

## 1. 安装

```bash
sudo apt update
sudo apt install crowbar
```

| 项目 | 内容 |
|------|------|
| 版本 | 4.2 |
| 架构 | all |
| 可执行命令 | `crowbar` |
| 依赖 | `freerdp3-x11`、`openvpn`、`python3`、`python3-nmap`、`python3-paramiko`、`vncviewer` |
| 安装体积 | 450 KB |
| 官网 | <https://github.com/galkan/crowbar> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/crowbar> |
| 包追踪 | <https://pkg.kali.org/pkg/crowbar> |

## 2. 官方用法示例

> 以下为 Kali 官方工具页给出的示例与输出原文。

```text
Usage Examples
Brute force the RDP service on a single host with a specified username and wordlist, using 1 thread.
root@kali:~# crowbar -b rdp -s 192.168.86.61/32 -u victim -C /root/words.txt -n 1
2017-10-10 14:59:55 START
2017-10-10 14:59:55 Crowbar v0.3.5-dev
2017-10-10 14:59:55 Trying 192.168.86.61:3389
2017-10-10 15:00:08 RDP-SUCCESS : 192.168.86.61:3389 - victim:s3cr3t
2017-10-10 15:00:08 STOP
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `crowbar`

官方给出的调用示例：`crowbar -b rdp -s 192.168.86.61/32 -u victim -C /root/words.txt -n 1`

```text
root@kali:~# crowbar -b rdp -s 192.168.86.61/32 -u victim -C /root/words.txt -n 1
2017-10-10 14:59:55 START
2017-10-10 14:59:55 Crowbar v0.3.5-dev
2017-10-10 14:59:55 Trying 192.168.86.61:3389
2017-10-10 15:00:08 RDP-SUCCESS : 192.168.86.61:3389 - victim:s3cr3t
2017-10-10 15:00:08 STOP
```

### `crowbar（示例）`

官方给出的调用示例：`crowbar -h`

```text
root@kali:~# crowbar -h
usage: Usage: use --help for further information
Crowbar is a brute force tool which supports OpenVPN, Remote Desktop Protocol,
SSH Private Keys and VNC Keys.
positional arguments:
  options
options:
  -h, --help            show this help message and exit
  -b, --brute {openvpn,rdp,sshkey,vnckey}
                        Target service
  -s, --server SERVER   Static target
  -S, --serverfile SERVER_FILE
                        Multiple targets stored in a file
  -u, --username USERNAME [USERNAME ...]
                        Static name to login with
  -U, --usernamefile USERNAME_FILE
                        Multiple names to login with, stored in a file
  -n, --number THREAD   Number of threads to be active at once
  -l, --log FILE        Log file (only write attempts)
  -o, --output FILE     Output file (write everything else)
  -c, --passwd PASSWD   Static password to login with
  -C, --passwdfile FILE
                        Multiple passwords to login with, stored in a file
  -t, --timeout TIMEOUT
                        [SSH] How long to wait for each thread (seconds)
  -p, --port PORT       Alter the port if the service is not using the default
                        value
  -k, --keyfile KEY_FILE
                        [SSH/VNC] (Private) Key file or folder containing
                        multiple files
  -m, --config CONFIG   [OpenVPN] Configuration file
  -d, --discover        Port scan before attacking open ports
  -v, --verbose         Enable verbose output (-vv for more)
  -D, --debug           Enable debug mode
  -q, --quiet           Only display successful logins
Updated on: 2025-Dec-09
 Edit this page
crlfuzz
crunch
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install crowbar`，再执行 `crowbar --version` 2>/dev/null || `crowbar -V`
- [ ] **2.** **读官方帮助** —— `crowbar -h`，需要细节时 `man crowbar`
- [ ] **3.** **在自有靶场跑最小用例** —— 用 `crowbar -h` 里最简单的那个子命令试一次
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/crowbar/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/credential-access.md`](../../tools/by-attack/credential-access.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/crowbar/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/crowbar/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
