# netexec

> Network Execution Tool NetExec (AKA nxc) is a network service exploitation tool that helps automate assessing the security of large networks. NetExec is the continuation of CrackMapExec, which was maintained by mpgn over the years, but dis…

> **功能分类**：Top 10 常用 ｜ **Kali 包**：`netexec` ｜ **官方文档**：<https://www.kali.org/tools/netexec/>

## 1. 安装

```bash
sudo apt update
sudo apt install netexec
```

| 项目 | 内容 |
|------|------|
| 版本 | 1.5.1 |
| 架构 | all |
| 可执行命令 | `netexec`、`nxc`、`nxcdb` |
| 依赖 | `bloodhound.py`、`certipy-ad`、`libkrb5-dev`、`python3`、`python3-aardwolf`、`python3-aioconsole`、`python3-aiosqlite`、`python3-argcomplete`、`python3-asyauth`、`python3-bs4`、`python3-dateutil`、`python3-dploot` 等 |
| 安装体积 | 3.60 MB |
| 官网 | <https://github.com/Pennyw0rth/NetExec> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/netexec> |
| 包追踪 | <https://pkg.kali.org/pkg/netexec> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
netexec -h          # 查看用法
man netexec         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 3 个可执行命令，下面是官方页面内嵌的帮助原文。

### `netexec`

> 官方示例调用：`netexec -h`

```text
root@kali:~# netexec -h
usage: netexec [-h] [--version] [-t THREADS] [--timeout TIMEOUT]
               [--jitter INTERVAL] [--no-progress] [--log LOG] [--verbose |
               --debug] [-6] [--dns-server DNS_SERVER] [--dns-tcp]
               [--dns-timeout DNS_TIMEOUT]
               {rdp,vnc,wmi,winrm,ftp,ssh,smb,ldap,mssql,nfs} ...
     .   .
    .|   |.     _   _          _     _____
    ||   ||    | \ | |   ___  | |_  | ____| __  __   ___    ___
    \\( )//    |  \| |  / _ \ | __| |  _|   \ \/ /  / _ \  / __|
    .=[ ]=.    | |\  | |  __/ | |_  | |___   >  <  |  __/ | (__
   / /˙-˙\ \   |_| \_|  \___|  \__| |_____| /_/\_\  \___|  \___|
   ˙ \   / ˙
     ˙   ˙
    The network execution tool
    Maintained as an open source project by @NeffIsBack, @MJHallenbeck, @_zblurx
    For documentation and usage examples, visit: https://www.netexec.wiki/
    Version : 1.5.1
    Codename: Yippie-Ki-Yay
    Commit  : Kali Linux
options:
  -h, --help            show this help message and exit
Generic Options:
  --version             Display nxc version
  -t, --threads THREADS
                        set how many concurrent threads to use
  --timeout TIMEOUT     max timeout in seconds of each thread
  --jitter INTERVAL     sets a random delay between each authentication
Output Options:
  --no-progress         do not displaying progress bar during scan
  --log LOG             export result into a custom file
  --verbose             enable verbose output
  --debug               enable debug level information
DNS:
  -6                    Enable force IPv6
  --dns-server DNS_SERVER
                        Specify DNS server (default: Use hosts file & System DNS)
  --dns-tcp             Use TCP instead of UDP for DNS queries
  --dns-timeout DNS_TIMEOUT
                        DNS query timeout in seconds
Available Protocols:
  {rdp,vnc,wmi,winrm,ftp,ssh,smb,ldap,mssql,nfs}
    rdp                 own stuff using RDP
    vnc                 own stuff using VNC
    wmi                 own stuff using WMI
    winrm               own stuff using WINRM
    ftp                 own stuff using FTP
    ssh                 own stuff using SSH
    smb                 own stuff using SMB
    ldap                own stuff using LDAP
    mssql               own stuff using MSSQL
    nfs                 own stuff using NFS
```

### `nxc`

> 官方示例调用：`nxc -h`

```text
root@kali:~# nxc -h
usage: nxc [-h] [--version] [-t THREADS] [--timeout TIMEOUT]
           [--jitter INTERVAL] [--no-progress] [--log LOG] [--verbose |
           --debug] [-6] [--dns-server DNS_SERVER] [--dns-tcp]
           [--dns-timeout DNS_TIMEOUT]
           {rdp,vnc,wmi,winrm,ftp,ssh,smb,ldap,mssql,nfs} ...
     .   .
    .|   |.     _   _          _     _____
    ||   ||    | \ | |   ___  | |_  | ____| __  __   ___    ___
    \\( )//    |  \| |  / _ \ | __| |  _|   \ \/ /  / _ \  / __|
    .=[ ]=.    | |\  | |  __/ | |_  | |___   >  <  |  __/ | (__
   / /˙-˙\ \   |_| \_|  \___|  \__| |_____| /_/\_\  \___|  \___|
   ˙ \   / ˙
     ˙   ˙
    The network execution tool
    Maintained as an open source project by @NeffIsBack, @MJHallenbeck, @_zblurx
    For documentation and usage examples, visit: https://www.netexec.wiki/
    Version : 1.5.1
    Codename: Yippie-Ki-Yay
    Commit  : Kali Linux
options:
  -h, --help            show this help message and exit
Generic Options:
  --version             Display nxc version
  -t, --threads THREADS
                        set how many concurrent threads to use
  --timeout TIMEOUT     max timeout in seconds of each thread
  --jitter INTERVAL     sets a random delay between each authentication
Output Options:
  --no-progress         do not displaying progress bar during scan
  --log LOG             export result into a custom file
  --verbose             enable verbose output
  --debug               enable debug level information
DNS:
  -6                    Enable force IPv6
  --dns-server DNS_SERVER
                        Specify DNS server (default: Use hosts file & System DNS)
  --dns-tcp             Use TCP instead of UDP for DNS queries
  --dns-timeout DNS_TIMEOUT
                        DNS query timeout in seconds
Available Protocols:
  {rdp,vnc,wmi,winrm,ftp,ssh,smb,ldap,mssql,nfs}
    rdp                 own stuff using RDP
    vnc                 own stuff using VNC
    wmi                 own stuff using WMI
    winrm               own stuff using WINRM
    ftp                 own stuff using FTP
    ssh                 own stuff using SSH
    smb                 own stuff using SMB
    ldap                own stuff using LDAP
    mssql               own stuff using MSSQL
    nfs                 own stuff using NFS
```

### `nxcdb`

> 官方示例调用：`nxcdb -h`

```text
root@kali:~# nxcdb -h
usage: nxcdb [-h] [-gw] [-cw CREATE_WORKSPACE] [-sw SET_WORKSPACE]
NXCDB is a database navigator for NXC
options:
  -h, --help            show this help message and exit
  -gw, --get-workspace  get the current workspace
  -cw, --create-workspace CREATE_WORKSPACE
                        create a new workspace
  -sw, --set-workspace SET_WORKSPACE
                        set the current workspace
Updated on: 2026-Aug-25
 Edit this page
net-snmp
netscanner
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install netexec`，再执行 `netexec --version` 2>/dev/null || `netexec -V`
- [ ] **2.** **读官方帮助** —— `netexec -h`，需要细节时 `man netexec`
- [ ] **3.** **在自有靶场跑最小用例** —— 用 `netexec -h` 里最简单的那个子命令试一次
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/netexec/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- **精讲教程**（含原理、参数详解、靶场实操与输出解读）：[netexec](../../tools/tutorials/08-后渗透/netexec.md)
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/defense-evasion.md`](../../tools/by-attack/defense-evasion.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/netexec/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/netexec/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
