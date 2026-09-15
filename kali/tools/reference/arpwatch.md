# arpwatch

> Ethernet/FDDI station activity monitor Arpwatch maintains a database of Ethernet MAC addresses seen on the network, with their associated IP pairs. Alerts the system administrator via e-mail if any change happens, such as new station/activ…

> **功能分类**：通用工具 ｜ **Kali 包**：`arpwatch` ｜ **官方文档**：<https://www.kali.org/tools/arpwatch/>

## 1. 安装

```bash
sudo apt update
sudo apt install arpwatch
```

| 项目 | 内容 |
|------|------|
| 版本 | 2.1a15 |
| 架构 | any |
| 可执行命令 | `arpwatch`、`arp2ethers`、`arpfetch`、`arpsnmp`、`bihourly`、`massagevendor` |
| 依赖 | `gawk`、`libc6`、`libpcap0.8t64` |
| 安装体积 | 159 KB |
| 官网 | <https://ee.lbl.gov/> |
| 源码仓库 | <https://salsa.debian.org/pkg-security-team/arpwatch> |
| 包追踪 | <https://pkg.kali.org/pkg/arpwatch> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
arpwatch -h          # 查看用法
man arpwatch         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 6 个可执行命令，下面是官方页面内嵌的帮助原文。

### `man`

> 官方示例调用：`man arp2ethers`

```text
root@kali:~# man arp2ethers
ARP2ETHERS(8)               System Manager's Manual               ARP2ETHERS(8)
NAME
     arp2ethers - convert arpwatch address database to ethers file format
SYNOPSIS
     arp2ethers [ arp.dat file ]
DESCRIPTION
     arp2ethers converts the file /var/lib/arpwatch/arp.dat (or the file speci-
     fied  on  the  command  line)  into  ethers(5)  format on stdout.  Usually
     arp.dat is an ethernet/ip database file  generated  by  arpwatch(8).   The
     arpwatch  daemon  in Debian will create different arp.dat depending on its
     configuration. All of them will be available at /var/lib/arpwatch/.
FILES
     /var/lib/arpwatch - default directory for arp.dat
     arp.dat - ethernet/ip address database
SEE ALSO
     arpwatch(8), ethers(5), rarp(8), arp(8),
BUGS
     Please send bug reports to
[email protected]
.
AUTHORS
     Original version by Craig Leres of the Lawrence Berkeley National  Labora-
     tory Network Research Group, University of California, Berkeley, CA.
     Modified for the Debian Project by Peter Kelemen, with additions from Erik
     Warmelink.
     The current version is available via anonymous ftp:
            ftp://ftp.ee.lbl.gov/arpwatch.tar.gz
     This manual page was contributed by Hugo Graumann.
                                                                  ARP2ETHERS(8)
```

### `arpfetch`

> 官方示例调用：`arpfetch -h`

```text
root@kali:~# arpfetch -h
usage: arpfetch host cname
```

### `arpsnmp`

> 官方示例调用：`arpsnmp -h`

```text
root@kali:~# arpsnmp -h
Version 2.1a15
usage: arpsnmp [-d] [-m addr ] [-f datafile] [-s sendmail_path] file [...]
```

### `arpwatch`

> 官方示例调用：`arpwatch -h`

```text
root@kali:~# arpwatch -h
Version 2.1a15
usage: arpwatch [-dN] [-f datafile] [-F "filter" ][-i interface] [-n net[/width]] [-r file] [-s sendmail_path] [-p] [-a] [-m addr] [-u username] [-Q] [-z ignorenet/ignoremask]
```

### `bihourly`

> 官方示例调用：`bihourly -h`

```text
root@kali:~# bihourly -h
cat: list: No such file or directory
cat: cname: No such file or directory
WARNING: tempfile is deprecated; consider using mktemp instead.
Version 2.1a15
usage: arpsnmp [-d] [-m addr ] [-f datafile] [-s sendmail_path] file [...]
```

### `massagevendor`

> 官方示例调用：`massagevendor -h`

```text
root@kali:~# massagevendor -h
sed: invalid option -- 'h'
Usage: sed [OPTION]... {script-only-if-no-other-script} [input-file]...
  -n, --quiet, --silent
                 suppress automatic printing of pattern space
      --debug
                 annotate program execution
  -e script, --expression=script
                 add the script to the commands to be executed
  -f script-file, --file=script-file
                 add the contents of script-file to the commands to be executed
  --follow-symlinks
                 follow symlinks when processing in place
  -i[SUFFIX], --in-place[=SUFFIX]
                 edit files in place (makes backup if SUFFIX supplied)
  -l N, --line-length=N
                 specify the desired line-wrap length for the `l' command
  --posix
                 disable all GNU extensions.
  -E, -r, --regexp-extended
                 use extended regular expressions in the script
                 (for portability use POSIX -E).
  -s, --separate
                 consider files as separate rather than as a single,
                 continuous long stream.
      --sandbox
                 operate in sandbox mode (disable e/r/w commands).
  -u, --unbuffered
                 load minimal amounts of data from the input files and flush
                 the output buffers more often
  -z, --null-data
                 separate lines by NUL characters
      --help     display this help and exit
      --version  output version information and exit
If no -e, --expression, -f, or --file option is given, then the first
non-option argument is taken as the sed script to interpret.  All
remaining arguments are names of input files; if no input files are
specified, then the standard input is read.
GNU sed home page: <https://www.gnu.org/software/sed/>.
General help using GNU software: <https://www.gnu.org/gethelp/>.
Updated on: 2026-Aug-25
 Edit this page
arping
arsenal-ng
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install arpwatch`，再执行 `arpwatch --version` 2>/dev/null || `arpwatch -V`
- [ ] **2.** **读官方帮助** —— `arpwatch -h`，需要细节时 `man arpwatch`
- [ ] **3.** **在自有靶场跑最小用例** —— 官方给出的调用形式是：`Usage: sed [OPTION]... {script-only-if-no-other-script} [input-file]...`
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/arpwatch/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/discovery.md`](../../tools/by-attack/discovery.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/arpwatch/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/arpwatch/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
