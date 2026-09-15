# chntpw

> NT SAM password recovery utility This little program provides a way to view information and change user passwords in a Windows NT/2000 user database file. Old passwords need not be known since they are overwritten. In addition it also cont…

> **功能分类**：口令攻击 ｜ **Kali 包**：`chntpw` ｜ **官方文档**：<https://www.kali.org/tools/chntpw/>

## 1. 安装

```bash
sudo apt update
sudo apt install chntpw
```

| 项目 | 内容 |
|------|------|
| 版本 | 140201 |
| 架构 | any |
| 可执行命令 | `chntpw`、`reged`、`sampasswd`、`samunlock`、`samusrgrp` |
| 依赖 | `libc6` |
| 安装体积 | 487 KB |
| 官网 | <http://pogostick.net/~pnh/ntpasswd/> |
| 源码仓库 | <https://salsa.debian.org/debian/chntpw> |
| 包追踪 | <https://pkg.kali.org/pkg/chntpw> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
chntpw -h          # 查看用法
man chntpw         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 5 个可执行命令，下面是官方页面内嵌的帮助原文。

### `chntpw`

> 官方示例调用：`chntpw -h`

```text
root@kali:~# chntpw -h
chntpw: change password of a user in a Windows SAM file,
or invoke registry editor. Should handle both 32 and 64 bit windows and
all version from NT3.x to Win8.1
chntpw [OPTIONS] <samfile> [systemfile] [securityfile] [otherreghive] [...]
 -h          This message
 -u <user>   Username or RID (0x3e9 for example) to interactively edit
 -l          list all users in SAM file and exit
 -i          Interactive Menu system
 -e          Registry editor. Now with full write support!
 -d          Enter buffer debugger instead (hex editor),
 -v          Be a little more verbose (for debuging)
 -L          For scripts, write names of changed files to /tmp/changed
 -N          No allocation mode. Only same length overwrites possible (very safe mode)
 -E          No expand mode, do not expand hive file (safe mode)
Usernames can be given as name or RID (in hex with 0x first)
See readme file on how to get to the registry files, and what they are.
Source/binary freely distributable under GPL v2 license. See README for details.
NOTE: This program is somewhat hackish! You are on your own!
```

### `reged`

> 官方示例调用：`reged -h`

```text
root@kali:~# reged -h
reged version 0.1 140201, (c) Petter N Hagen
Modes:
-x <registryhivefile> <prefixstring> <key> <output.reg>
   Xport. Where <prefixstring> for example is HKEY_LOCAL_MACHINE\SOFTWARE
   <key> is key to dump (recursively), \ or \\ means all keys in hive
   Only one .reg and one hive file supported at the same time
-I <registryhivefile> <prefixstring> <input.reg>
   Import from .reg file. Where <prefixstring> for example is HKEY_LOCAL_MACHINE\SOFTWARE
   Only one .reg and one hive file supported at the same time
-e <registryhive> ...
   Interactive edit one or more of registry files
Options:
-L : Log changed filenames to /tmp/changed, also auto-saves
-C : Auto-save (commit) changed hives without asking
-N : No allocate mode, only allow edit of existing values with same size
-E : No expand mode, do not expand hive file (safe mode)
-t : Debug trace of allocated blocks
-v : Some more verbose messages
```

### `sampasswd`

> 官方示例调用：`sampasswd -h`

```text
root@kali:~# sampasswd -h
sampasswd version 0.2 140201, (c) Petter N Hagen
sampasswd  [-r|-l] [-H] -u <user> <samhive>
Reset password or list users in SAM database
Mode:
   -r = reset users password
   -l = list users in sam
Parameters:
   <user> can be given as a username or a RID in hex with 0x in front
   Example:
   -r -u theboss -> resets password of user named 'theboss' if found
   -r -u 0x3ea -> resets password for user with RID 0x3ea (hex)
   -r -a -> Reset password of all users in administrators group (0x220)
   -r -f -> Reset password of admin user with lowest RID
            not counting built-in admin (0x1f4) unless it is the only admin
   Usernames with international characters usually fails to be found,
   please use RID number instead
   If success, there will be no output, and exit code is 0
Options:
   -H : For list: Human readable listing (default is parsable table)
   -H : For reset: Will output confirmation message if success
   -N : No allocate mode, only allow edit of existing values with same size
   -E : No expand mode, do not expand hive file (safe mode)
   -t : Debug trace of allocated blocks
   -v : Some more verbose messages/debug
```

### `samunlock`

> 官方示例调用：`samunlock -h`

```text
root@kali:~# samunlock -h
samunlock version 0.1 141018, (c) Adrian Gibanel
samunlock  [-U|-l] [-H] -u <user> <samhive>
Unlock user or list users in SAM database
Mode:
   -U = Unlock user
   -l = list users in sam
Parameters:
   <user> can be given as a username or a RID in hex with 0x in front
   Example:
   -U -u theboss -> Unlocks user named 'theboss' if found
   -U -u 0x3ea -> Unlocks user with RID 0x3ea (hex)
   -U -f -> Unlocks admin user with lowest RID
            not counting built-in admin (0x1f4) unless it is the only admin
   Usernames with international characters usually fails to be found,
   please use RID number instead
   If success, there will be no output, and exit code is 0
Options:
   -H : For list: Human readable listing (default is parsable table)
   -H : For unlock: Will output confirmation message if success
   -N : No allocate mode, only allow edit of existing values with same size
   -E : No expand mode, do not expand hive file (safe mode)
   -t : Debug trace of allocated blocks
   -v : Some more verbose messages/debug
```

### `samusrgrp`

> 官方示例调用：`samusrgrp -h`

```text
root@kali:~# samusrgrp -h
samusrgrp version 0.2 140201, (c) Petter N Hagen
samusrgrp  [-a|-r] -u <user> -g <groupid> <samhive>
Add or remove a (local) user to/from a group
Mode:   -a = add user to group
   -r = remove user from group
   -l = list groups
   -L = list groups and also their members
   -s = Print machine SID
Parameters:
   <user> can be given as a username or a RID in hex with 0x in front
   <group> is the group number, in hex with 0x in front
   Example:
   -a -u theboss -g 0x220 -> add user named 'theboss' group hex 220 (administrators)
   -a -u 0x3ea -g 0x221 -> add user with RID (hex) 3ea group hex 221 (users)
   -r -u 0x3ff -g 0x220 -> remove user RID 0x3ff from grp 0x220
   Usernames with international characters usually fails to be found,
   please use RID number instead
   If success, there will be no output, and exit code is 0
   Also, success if user already in (or not in if -r) the group
Options:
   -H : Human readable output, else parsable
   -N : No allocate mode, only allow edit of existing values with same size
   -E : No expand mode, do not expand hive file (safe mode)
   -t : Debug trace of allocated blocks
   -v : Some more verbose messages/debug
Multi call binary, if program is named:
  samusrtogrp -- Assume -a mode: Add a user into a group
  samusrfromgrp -- Assume -r mode: Remove user from a group
Updated on: 2026-May-25
 Edit this page
cherrytree
cifs-utils
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install chntpw`，再执行 `chntpw --version` 2>/dev/null || `chntpw -V`
- [ ] **2.** **读官方帮助** —— `chntpw -h`，需要细节时 `man chntpw`
- [ ] **3.** **在自有靶场跑最小用例** —— 用 `chntpw -h` 里最简单的那个子命令试一次
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/chntpw/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/credential-access.md`](../../tools/by-attack/credential-access.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/chntpw/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/chntpw/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
