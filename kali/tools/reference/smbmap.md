# smbmap

> Handy SMB enumeration tool SMBMap allows users to enumerate samba share drives across an entire domain. List share drives, drive permissions, share contents, upload/download functionality, file name auto-download pattern matching, and even…

> **功能分类**：信息搜集 ｜ **Kali 包**：`smbmap` ｜ **官方文档**：<https://www.kali.org/tools/smbmap/>

## 1. 安装

```bash
sudo apt update
sudo apt install smbmap
```

| 项目 | 内容 |
|------|------|
| 版本 | 1.10.7 |
| 架构 | all |
| 可执行命令 | `smbmap` |
| 依赖 | `python3`、`python3-impacket`、`python3-pyasn1`、`python3-termcolor` |
| 安装体积 | 134 KB |
| 官网 | <https://github.com/ShawnDEvans/smbmap> |
| 源码仓库 | <https://salsa.debian.org/pkg-security-team/smbmap> |
| 包追踪 | <https://pkg.kali.org/pkg/smbmap> |

## 2. 官方用法示例

> 以下为 Kali 官方工具页给出的示例与输出原文。

```text
Usage Examples
Check for shares on the specified host with the username and password provided:
root@kali:~# smbmap -u victim -p s3cr3t -H 192.168.86.61
[+] Finding open SMB ports....
[+] User SMB session establishd on 192.168.86.61...
[+] IP: 192.168.86.61:445   Name: win7-x86.lan
    Disk                                                    Permissions
    ----                                                    -----------
    ADMIN$                                              NO ACCESS
    C$                                                  NO ACCESS
    IPC$                                                NO ACCESS
    Users                                               READ ONLY
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `smbmap`

> 官方示例调用：`smbmap -u victim -p s3cr3t -H 192.168.86.61`

```text
root@kali:~# smbmap -u victim -p s3cr3t -H 192.168.86.61
[+] Finding open SMB ports....
[+] User SMB session establishd on 192.168.86.61...
[+] IP: 192.168.86.61:445   Name: win7-x86.lan
    Disk                                                    Permissions
    ----                                                    -----------
    ADMIN$                                              NO ACCESS
    C$                                                  NO ACCESS
    IPC$                                                NO ACCESS
    Users                                               READ ONLY
```

### `smbmap -h`

> 官方示例调用：`smbmap -h`

```text
root@kali:~# smbmap -h
usage: smbmap [-h] (-H HOST | --host-file FILE) [-u USERNAME] [-p PASSWORD |
              --prompt] [-k] [--no-pass] [--dc-ip IP or Host] [-s SHARE]
              [-d DOMAIN] [-P PORT] [-v] [--signing] [--admin] [--no-banner]
              [--no-color] [--no-update] [--timeout SCAN_TIMEOUT] [-x COMMAND]
              [--mode CMDMODE] [-L | -r [PATH]] [-g FILE | --csv FILE]
              [--dir-only] [--no-write-check] [-q] [--depth DEPTH]
              [--exclude SHARE [SHARE ...]] [-A PATTERN] [-F PATTERN]
              [--search-path PATH] [--search-timeout TIMEOUT]
              [--download PATH] [--upload SRC DST] [--delete PATH TO FILE]
              [--skip]
    ________  ___      ___  _______   ___      ___       __         _______
   /"       )|"  \    /"  ||   _  "\ |"  \    /"  |     /""\       |   __ "\
  (:   \___/  \   \  //   |(. |_)  :) \   \  //   |    /    \      (. |__) :)
   \___  \    /\  \/.    ||:     \/   /\   \/.    |   /' /\  \     |:  ____/
    __/  \   |: \.        |(|  _  \  |: \.        |  //  __'  \    (|  /
   /" \   :) |.  \    /:  ||: |_)  :)|.  \    /:  | /   /  \   \  /|__/ \
  (_______/  |___|\__/|___|(_______/ |___|\__/|___|(___/    \___)(_______)
-----------------------------------------------------------------------------
SMBMap - Samba Share Enumerator v1.10.7 | Shawn Evans -
[email protected]
                     https://github.com/ShawnDEvans/smbmap
options:
  -h, --help            show this help message and exit
Main arguments:
  -H HOST               IP or FQDN
  --host-file FILE      File containing a list of hosts
  -u, --username USERNAME
                        Username, if omitted null session assumed
  -p, --password PASSWORD
                        Password or NTLM hash, format is LMHASH:NTHASH
  --prompt              Prompt for a password
  -s SHARE              Specify a share (default C$), ex 'C$'
  -d DOMAIN             Domain name (default WORKGROUP)
  -P PORT               SMB port (default 445)
  -v, --version         Return the OS version of the remote host
  --signing             Check if host has SMB signing disabled, enabled, or
                        required
  --admin               Just report if the user is an admin
  --no-banner           Removes the banner from the top of the output
  --no-color            Removes the color from output
  --no-update           Removes the "Working on it" message
  --timeout SCAN_TIMEOUT
                        Set port scan socket timeout. Default is .5 seconds
Kerberos settings:
  -k, --kerberos        Use Kerberos authentication
  --no-pass             Use CCache file (export KRB5CCNAME='~/current.ccache')
  --dc-ip IP or Host    IP or FQDN of DC
Command Execution:
  Options for executing commands on the specified host
  -x COMMAND            Execute a command ex. 'ipconfig /all'
  --mode CMDMODE        Set the execution method, wmi or psexec, default wmi
Shard drive Search:
  Options for searching/enumerating the share of the specified host(s)
  -L                    List all drives on the specified host, requires ADMIN
                        rights.
  -r [PATH]             Recursively list dirs and files (no share\path lists
                        the root of ALL shares), ex. 'email/backup'
  -g FILE               Output to a file in a grep friendly format, used with
                        -r (otherwise it outputs nothing), ex -g grep_out.txt
  --csv FILE            Output to a CSV file, ex --csv shares.csv
  --dir-only            List only directories, ommit files.
  --no-write-check      Skip check to see if drive grants WRITE access.
  -q                    Quiet verbose output. Only shows shares you have READ
                        or WRITE on, and suppresses file listing when
                        performing a search (-A).
  --depth DEPTH         Traverse a directory tree to a specific depth. Default
                        is 1 (root node).
  --exclude SHARE [SHARE ...]
                        Exclude share(s) from searching and listing, ex.
                        --exclude ADMIN$ C$'
  -A PATTERN            Define a file name pattern (regex) that auto downloads
                        a file on a match (requires -r), not case sensitive,
                        ex '(web|global).(asax|config)'
File Content Search:
  Options for searching the content of files (must run as root), kind of experimental
  -F PATTERN            File content search, -F '[Pp]assword' (requires admin
                        access to execute commands, and PowerShell on victim
                        host)
  --search-path PATH    Specify drive/path to search (used with -F, default
                        C:\Users), ex 'D:\HR\'
  --search-timeout TIMEOUT
                        Specifcy a timeout (in seconds) before the file search
                        job gets killed. Default is 300 seconds.
Filesystem interaction:
  Options for interacting with the specified host's filesystem
  --download PATH       Download a file from the remote system,
                        ex.'C$\temp\passwords.txt'
  --upload SRC DST      Upload a file to the remote system ex.
                        '/tmp/payload.exe C$\temp\payload.exe'
  --delete PATH TO FILE
                        Delete a remote file, ex. 'C$\temp\msf.exe'
  --skip                Skip delete file confirmation prompt
Examples:
$ smbmap -u jsmith -p password1 -d workgroup -H 192.168.0.1
$ smbmap -u jsmith -p 'aad3b435b51404eeaad3b435b51404ee:da76f2c4c96028b7a6111aef4a50a94d' -H 172.16.0.20
$ smbmap -u 'apadmin' -p 'asdf1234!' -d ACME -Hh 10.1.3.30 -x 'net group "Domain Admins" /domain'
Updated on: 2025-Dec-09
 Edit this page
slowhttptest
smtp-user-enum
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install smbmap`，再执行 `smbmap --version` 2>/dev/null || `smbmap -V`
- [ ] **2.** **读官方帮助** —— `smbmap -h`，需要细节时 `man smbmap`
- [ ] **3.** **在自有靶场跑最小用例** —— 用 `smbmap -h` 里最简单的那个子命令试一次
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/smbmap/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/defense-evasion.md`](../../tools/by-attack/defense-evasion.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/smbmap/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/smbmap/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
