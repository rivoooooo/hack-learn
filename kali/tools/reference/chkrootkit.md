# chkrootkit

> Rootkit detector The chkrootkit security scanner searches for signs that the system is infected with a ‘rootkit’. Rootkits are a form of malware that seek to exploit security flaws to grant unauthorised access to a computer or its services…

> **功能分类**：数字取证 ｜ **Kali 包**：`chkrootkit` ｜ **官方文档**：<https://www.kali.org/tools/chkrootkit/>

## 1. 安装

```bash
sudo apt update
sudo apt install chkrootkit
```

| 项目 | 内容 |
|------|------|
| 版本 | 0.59 |
| 架构 | any |
| 可执行命令 | `chkrootkit`、`chklastlog`、`chkrootkit-daily`、`chkwtmp` |
| 依赖 | `binutils` |
| 安装体积 | 988 KB |
| 官网 | <https://www.chkrootkit.org/> |
| 源码仓库 | <https://salsa.debian.org/pkg-security-team/chkrootkit> |
| 包追踪 | <https://pkg.kali.org/pkg/chkrootkit> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
chkrootkit -h          # 查看用法
man chkrootkit         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 4 个可执行命令，下面是官方页面内嵌的帮助原文。

### `man`

官方给出的调用示例：`man chklastlog`

```text
root@kali:~# man chklastlog
CHKLASTLOG(8)               System Manager's Manual               CHKLASTLOG(8)
NAME
     chklastlog - check lastlog file for deleted entries
SYNOPSIS
     chklastlog  looks  for  users whose login has been erased from the lastlog
     database.
DESCRIPTION
     chklastlog reads all entries from /var/log/wtmp (a database of information
     about logins and logouts) and checks that every user found  in  this  file
     has  an entry in /var/log/lastlog.  It lists any users with logins in wtmp
     but no lastlogin information. This may suggest the user account  has  been
     compromised and the attacker has tried to cover their tracks.
     chklastlog  needs to be able to read /var/log/wtmp and /var/log/lastlogin.
     Normally these files are world-readable so no special privileges  are  re-
     quired.
FILES
     /var/log/wtmp
            database of logins and logouts.
     /var/log/lastlog
            database which contains info on the last login of each user.
SEE ALSO
     wtmp(5), who(1), lastlog(8), last(1)
LIMITATIONS
     wtmp  may itself be incomplete because not all programmes record their ac-
     tivity using utmp logging. See wtmp(8).
     chklastlog will not detect missing entries if the user has logged in after
     the lastlog entry was deleted.
     This program was originally designed to run on SunOS 4.x systems. On other
     systems the output is undefined.
                                  Oct 23, 2021                    CHKLASTLOG(8)
```

### `chkrootkit`

官方给出的调用示例：`chkrootkit -h`

```text
root@kali:~# chkrootkit -h
Usage: /usr/sbin/chkrootkit [options] [test ...]
Options:
        -h                show this help and exit
        -V                show version information and exit
        -l                show available tests and exit
        -d                debug
        -q                quiet mode
        -x                expert mode
        -e 'FILE1 FILE2'  exclude files/dirs from results. Must be followed by a space-separated list of files/dirs.
                          Read /usr/share/doc/chkrootkit/README.FALSE-POSITIVES first.
        -s REGEXP         filter results of sniffer test through 'grep -Ev REGEXP' to exclude expected
                          PACKET_SNIFFERs. Read /usr/share/doc/chkrootkit/README.FALSE-POSITIVES first.
        -r DIR            use DIR as the root directory
        -p DIR1:DIR2:DIRN path for the external commands used by chkrootkit
        -n                skip NFS mount points
        -T FSTYPE         skip mount points of the specified file system type
```

### `man（示例）`

官方给出的调用示例：`man chkrootkit-daily`

```text
root@kali:~# man chkrootkit-daily
chkrootkit-daily(8)         System Manager's Manual         chkrootkit-daily(8)
NAME
     chkrootkit-daily - Run chkrootkit and report results
SYNOPSIS
     chkrootkit-daily
DESCRIPTION
     chkrootkit-daily runs chkrootkit(8) and emails the results. It is intended
     to be run by the systemd(1) timer or as a cron(1) job every day.
CONFIGURATION
     All options are set and documented in /etc/chkrootkit/chkrootkit.conf.
AUTHOR
     chkrootkit-daily  and  this  manual page were written by Richard Lewis for
     the Debian project. They may be used by others.
SEE ALSO
     chkrootkit(8)
                                   2023-02-19               chkrootkit-daily(8)
```

### `man（示例）`

官方给出的调用示例：`man chkwtmp`

```text
root@kali:~# man chkwtmp
CHKWTMP(8)                  System Manager's Manual                  CHKWTMP(8)
NAME
     chkwtmp - check wtmp file deleted entries
SYNOPSIS
     chkwtmp looks for data deleted from wtmp
DESCRIPTION
     chkwtmp  examines the file /var/log/wtmp for entries which have been over-
     written (containing only null-bytes). If such entries are found  the  pro-
     gram  displays  the timestamps of the entries before and after the deleted
     entry, providing an idea of when the entry was deleted.
     chkwtmp needs to be able to read /var/log/wtmp.   Normally  this  file  is
     world-readable so no special privileges are required.
FILES
     /var/log/wtmp
            database of logins and logouts.
SEE ALSO
     wtmp(4), who(1)
LIMITATIONS
     An  entry  is  recognized  as overwritten if the time-information has been
     overwritten with null-bytes.
     This program was originally designed to run on SunOS 4.x systems. On other
     systems the output is undefined.
                                  Oct 23, 2021                       CHKWTMP(8)
Learn more with
OffSec
Want to learn more about chkrootkit? get access to in-depth training and hands-on labs:
PEN-103: 8.5.3. Securing and Monitoring Kali Linux: Detecting Changes
PEN-103 course
Updated on: 2026-Aug-25
 Edit this page
chisel-common-binaries
chromium
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install chkrootkit`，再执行 `chkrootkit --version` 2>/dev/null || `chkrootkit -V`
- [ ] **2.** **读官方帮助** —— `chkrootkit -h`，需要细节时 `man chkrootkit`
- [ ] **3.** **在自有靶场跑最小用例** —— 官方给出的调用形式是：`Usage: /usr/sbin/chkrootkit [options] [test ...]`
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/chkrootkit/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/forensics.md`](../../tools/by-attack/forensics.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/chkrootkit/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/chkrootkit/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
