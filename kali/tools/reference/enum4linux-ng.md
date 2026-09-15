# enum4linux-ng

> Next generation version of enum4linux Next generation version of enum4linux (a Windows/Samba enumeration tool) with additional features like JSON/YAML export. Aimed for security professionals and CTF players.

> **功能分类**：通用工具 ｜ **Kali 包**：`enum4linux-ng` ｜ **官方文档**：<https://www.kali.org/tools/enum4linux-ng/>

## 1. 安装

```bash
sudo apt update
sudo apt install enum4linux-ng
```

| 项目 | 内容 |
|------|------|
| 版本 | 1.3.10 |
| 架构 | all |
| 可执行命令 | `enum4linux-ng` |
| 依赖 | `python3`、`python3-impacket`、`python3-ldap3`、`python3-yaml`、`samba-common-bin`、`smbclient` |
| 安装体积 | 193 KB |
| 官网 | <https://github.com/cddmp/enum4linux-ng> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/enum4linux-ng> |
| 包追踪 | <https://pkg.kali.org/pkg/enum4linux-ng> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
enum4linux-ng -h          # 查看用法
man enum4linux-ng         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `enum4linux-ng`

官方给出的调用示例：`enum4linux-ng -h`

```text
root@kali:~# enum4linux-ng -h
ENUM4LINUX - next generation (v1.3.10)
usage: enum4linux-ng [-h] [-A] [-As] [-U] [-G] [-Gm] [-S] [-C] [-P] [-O] [-L]
                     [-I] [-R [BULK_SIZE]] [-N] [-w DOMAIN] [-u USER] [-p PW |
                     -K TICKET_FILE | -H NTHASH] [--local-auth] [-d]
                     [-k USERS] [-r RANGES] [-s SHARES_FILE] [-t TIMEOUT] [-v]
                     [--keep] [-oJ OUT_JSON_FILE | -oY OUT_YAML_FILE |
                     -oA OUT_FILE]
                     host
This tool is a rewrite of Mark Lowe's enum4linux.pl, a tool for enumerating
information from Windows and Samba systems. It is mainly a wrapper around the
Samba tools nmblookup, net, rpcclient and smbclient. Other than the original
tool it allows to export enumeration results as YAML or JSON file, so that it
can be further processed with other tools. The tool tries to do a 'smart'
enumeration. It first checks whether SMB or LDAP is accessible on the target.
Depending on the result of this check, it will dynamically skip checks (e.g.
LDAP checks if LDAP is not running). If SMB is accessible, it will always
check whether a session can be set up or not. If no session can be set up, the
tool will stop enumeration. The enumeration process can be interupted with
CTRL+C. If the options -oJ or -oY are provided, the tool will write out the
current enumeration state to the JSON or YAML file, once it receives SIGINT
triggered by CTRL+C. The tool was made for security professionals and CTF
players. Illegal use is prohibited.
positional arguments:
  host
options:
  -h, --help         show this help message and exit
  -A                 Do all simple enumeration including nmblookup (-U -G -S
                     -P -O -N -I -L). This option is enabled if you don't
                     provide any other option.
  -As                Do all simple short enumeration without NetBIOS names
                     lookup (-U -G -S -P -O -I -L)
  -U                 Get users via RPC
  -G                 Get groups via RPC
  -Gm                Get groups with group members via RPC
  -S                 Get shares via RPC
  -C                 Get services via RPC
  -P                 Get password policy information via RPC
  -O                 Get OS information via RPC
  -L                 Get additional domain info via LDAP/LDAPS (for DCs only)
  -I                 Get printer information via RPC
  -R [BULK_SIZE]     Enumerate users via RID cycling. Optionally specify the
                     lookup request size (BULK_SIZE).
  -N                 Do an NetBIOS names lookup (similar to nbtstat) and try
                     to retrieve workgroup from output
  -w DOMAIN          Specify workgroup/domain manually (usually found
                     automatically)
  -u USER            Specify username to use (default "")
  -p PW              Specify password to use (default "")
  -K TICKET_FILE     Try to authenticate with Kerberos, only useful in Active
                     Directory environment (Note: DNS must be setup correctly
                     for this option to work
  -H NTHASH          Try to authenticate with hash
  --local-auth       Authenticate locally to target
  -d                 Get detailed information for users and groups, applies to
                     -U, -G and -R
  -k USERS           User(s) that exists on remote system (default:
                     administrator,guest,krbtgt,domain admins,root,bin,none).
                     Used to get sid with "lookupsids"
  -r RANGES          RID ranges to enumerate (default: 500-550,1000-1050)
  -s SHARES_FILE     Brute force guessing for shares
  -t TIMEOUT         Sets connection timeout in seconds (default: 10s)
  -v                 Verbose, show full samba tools commands being run (net,
                     rpcclient, etc.)
  --keep             Don't delete the Samba configuration file created during
                     tool run after enumeration (useful with -v)
  -oJ OUT_JSON_FILE  Writes output to JSON file (extension is added
                     automatically)
  -oY OUT_YAML_FILE  Writes output to YAML file (extension is added
                     automatically)
  -oA OUT_FILE       Writes output to YAML and JSON file (extensions are added
                     automatically)
Updated on: 2026-Mar-02
 Edit this page
emailharvester
exiflooter
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install enum4linux-ng`，再执行 `enum4linux-ng --version` 2>/dev/null || `enum4linux-ng -V`
- [ ] **2.** **读官方帮助** —— `enum4linux-ng -h`，需要细节时 `man enum4linux-ng`
- [ ] **3.** **在自有靶场跑最小用例** —— 用 `enum4linux-ng -h` 里最简单的那个子命令试一次
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/enum4linux-ng/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- **精讲教程**（含原理、参数详解、靶场实操与输出解读）：[enum4linux](../../tools/tutorials/01-信息搜集/enum4linux.md)
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/discovery.md`](../../tools/by-attack/discovery.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/enum4linux-ng/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/enum4linux-ng/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
