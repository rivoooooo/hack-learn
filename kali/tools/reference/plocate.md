# plocate

> Much faster locate plocate is a locate(1) based on posting lists, giving much faster searches on a much smaller index. It is a drop-in replacement for mlocate in nearly all aspects, and is fast on SSDs and non-SSDs alike.

> **功能分类**：通用工具 ｜ **Kali 包**：`plocate` ｜ **官方文档**：<https://www.kali.org/tools/plocate/>

## 1. 安装

```bash
sudo apt update
sudo apt install plocate
```

| 项目 | 内容 |
|------|------|
| 版本 | 1.1.24 |
| 架构 | any |
| 可执行命令 | `plocate`、`plocate-build`、`updatedb.plocate` |
| 依赖 | `adduser`、`libc6`、`libgcc-s1`、`libstdc++6`、`liburing2`、`libzstd1` |
| 安装体积 | 572 KB |
| 官网 | <https://plocate.sesse.net/> |
| 包追踪 | <https://pkg.kali.org/pkg/plocate> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
plocate -h          # 查看用法
man plocate         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 3 个可执行命令，下面是官方页面内嵌的帮助原文。

### `plocate`

官方给出的调用示例：`plocate -h`

```text
root@kali:~# plocate -h
Usage: plocate [OPTION]... PATTERN...
  -b, --basename         search only the file name portion of path names
  -c, --count            print number of matches instead of the matches
  -d, --database DBPATH  search for files in DBPATH
                         (default is /var/lib/plocate/plocate.db)
  -i, --ignore-case      search case-insensitively
  -l, --limit LIMIT      stop after LIMIT matches
  -0, --null             delimit matches by NUL instead of newline
  -N, --literal          do not quote filenames, even if printing to a tty
  -r, --regexp           interpret patterns as basic regexps (slow)
      --regex            interpret patterns as extended regexps (slow)
  -w, --wholename        search the entire path name (default; see -b)
      --help             print this help
      --version          print version information
```

### `plocate-build`

官方给出的调用示例：`plocate-build -h`

```text
root@kali:~# plocate-build -h
Usage: plocate-build MLOCATE_DB PLOCATE_DB
Generate plocate index from mlocate.db, typically /var/lib/mlocate/mlocate.db.
Normally, the destination should be /var/lib/mlocate/plocate.db.
  -b, --block-size SIZE  number of filenames to store in each block (default 32)
  -p, --plaintext        input is a plaintext file, not an mlocate database
  -l, --require-visibility FLAG  check visibility before reporting files
      --help             print this help
      --version          print version information
```

### `updatedb.plocate`

官方给出的调用示例：`updatedb.plocate -h`

```text
root@kali:~# updatedb.plocate -h
Usage: updatedb [OPTION]...
Update a plocate database.
  -f, --add-prunefs FS           omit also FS (space-separated)
  -n, --add-prunenames NAMES     omit also NAMES (space-separated)
  -e, --add-prunepaths PATHS     omit also PATHS (space-separated)
      --add-single-prunepath PATH  omit also PATH
  -U, --database-root PATH       the subtree to store in database (default "/")
  -h, --help                     print this help
  -o, --output FILE              database to update (default
                                 `/var/lib/plocate/plocate.db')
  -b, --block-size SIZE          number of filenames to store
                                 in each block (default 32)
      --config-file FILE         configuration file (default `/etc/updatedb.conf')
      --prune-bind-mounts FLAG   omit bind mounts (default "no")
      --prunefs FS               filesystems to omit from database
      --prunenames NAMES         directory names to omit from database
      --prunepaths PATHS         paths to omit from database
  -l, --require-visibility FLAG  check visibility before reporting files
                                 (default "yes")
  -v, --verbose                  print paths of files as they are found
  -V, --version                  print version information
The configuration defaults to values read from `/etc/updatedb.conf',
or from a file specified with --config-file.
Report bugs to
[email protected]
.
Learn more with
OffSec
Want to learn more about plocate? get access to in-depth training and hands-on labs:
Web Application Assessment Essentials: 1.6.2. Linux Basics I: Linux File Management with Wildcards
Updated on: 2026-Mar-02
 Edit this page
peirates
pnscan
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install plocate`，再执行 `plocate --version` 2>/dev/null || `plocate -V`
- [ ] **2.** **读官方帮助** —— `plocate -h`，需要细节时 `man plocate`
- [ ] **3.** **在自有靶场跑最小用例** —— 官方给出的调用形式是：`Usage: plocate [OPTION]... PATTERN...`
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/plocate/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/plocate/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/plocate/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
