# crackmapexec

> Swiss army knife for pentesting networks This package is a swiss army knife for pentesting Windows/Active Directory environments. From enumerating logged on users and spidering SMB shares to executing psexec style attacks, auto-injecting M…

> **功能分类**：通用工具 ｜ **Kali 包**：`crackmapexec` ｜ **官方文档**：<https://www.kali.org/tools/crackmapexec/>

## 1. 安装

```bash
sudo apt update
sudo apt install crackmapexec
```

| 项目 | 内容 |
|------|------|
| 版本 | 5.4.0 |
| 架构 | all |
| 可执行命令 | `crackmapexec`、`cmedb` |
| 依赖 | `python3`、`python3-aardwolf`、`python3-aioconsole`、`python3-bs4`、`python3-dsinternals`、`python3-impacket`、`python3-lsassy`、`python3-masky`、`python3-msgpack`、`python3-neo4j`、`python3-paramiko`、`python3-pylnk3` 等 |
| 安装体积 | 2.29 MB |
| 官网 | <https://github.com/mpgn/CrackMapExec> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/crackmapexec> |
| 包追踪 | <https://pkg.kali.org/pkg/crackmapexec> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
crackmapexec -h          # 查看用法
man crackmapexec         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 2 个可执行命令，下面是官方页面内嵌的帮助原文。

### `cmedb`

> 官方示例调用：`cmedb -h`

```text
root@kali:~# cmedb -h
[-] Unable to find config file
```

### `crackmapexec`

> 官方示例调用：`crackmapexec -h`

```text
root@kali:~# crackmapexec -h
usage: crackmapexec [-h] [-t THREADS] [--timeout TIMEOUT] [--jitter INTERVAL]
                    [--darrell] [--verbose]
                    {rdp,winrm,ftp,ssh,smb,ldap,mssql} ...
      ______ .______           ___        ______  __  ___ .___  ___.      ___      .______    _______ ___   ___  _______   ______
     /      ||   _  \         /   \      /      ||  |/  / |   \/   |     /   \     |   _  \  |   ____|\  \ /  / |   ____| /      |
    |  ,----'|  |_)  |       /  ^  \    |  ,----'|  '  /  |  \  /  |    /  ^  \    |  |_)  | |  |__    \  V  /  |  |__   |  ,----'
    |  |     |      /       /  /_\  \   |  |     |    <   |  |\/|  |   /  /_\  \   |   ___/  |   __|    >   <   |   __|  |  |
    |  `----.|  |\  \----. /  _____  \  |  `----.|  .  \  |  |  |  |  /  _____  \  |  |      |  |____  /  .  \  |  |____ |  `----.
     \______|| _| `._____|/__/     \__\  \______||__|\__\ |__|  |__| /__/     \__\ | _|      |_______|/__/ \__\ |_______| \______|
                                                A swiss army knife for pentesting networks
                                    Forged by @byt3bl33d3r and @mpgn_x64 using the powah of dank memes
                                           Exclusive release for Porchetta Industries users
                                                       https://porchetta.industries/
                                                   Version : 5.4.0
                                                   Codename: Indestructible G0thm0g
options:
  -h, --help            show this help message and exit
  -t THREADS            set how many concurrent threads to use (default: 100)
  --timeout TIMEOUT     max timeout in seconds of each thread (default: None)
  --jitter INTERVAL     sets a random delay between each connection (default: None)
  --darrell             give Darrell a hand
  --verbose             enable verbose output
protocols:
  available protocols
  {rdp,winrm,ftp,ssh,smb,ldap,mssql}
    rdp                 own stuff using RDP
    winrm               own stuff using WINRM
    ftp                 own stuff using FTP
    ssh                 own stuff using SSH
    smb                 own stuff using SMB
    ldap                own stuff using LDAP
    mssql               own stuff using MSSQL
Learn more with
OffSec
Want to learn more about crackmapexec? get access to in-depth training and hands-on labs:
PEN-200: 23.2.1. Attacking Active Directory Authentication: Password Attacks
PEN-200 course
Updated on: 2026-Aug-25
 Edit this page
crack
cri-tools
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install crackmapexec`，再执行 `crackmapexec --version` 2>/dev/null || `crackmapexec -V`
- [ ] **2.** **读官方帮助** —— `crackmapexec -h`，需要细节时 `man crackmapexec`
- [ ] **3.** **在自有靶场跑最小用例** —— 用 `crackmapexec -h` 里最简单的那个子命令试一次
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/crackmapexec/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- **精讲教程**（含原理、参数详解、靶场实操与输出解读）：[crackmapexec](../../tools/tutorials/08-后渗透/crackmapexec.md)
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/defense-evasion.md`](../../tools/by-attack/defense-evasion.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/crackmapexec/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/crackmapexec/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
