# ddrescue

> Data recovery and protection tool When your disk has crashed and you try to copy it over to another one, standard Unix tools like cp, cat, and dd will abort on every I/O error, dd_rescue does not. It optimizes copying by using large blocks…

> **功能分类**：数字取证 ｜ **Kali 包**：`ddrescue` ｜ **官方文档**：<https://www.kali.org/tools/ddrescue/>

## 1. 安装

```bash
sudo apt update
sudo apt install ddrescue
```

| 项目 | 内容 |
|------|------|
| 版本 | 1.99.13 |
| 架构 | amd64 |
| 可执行命令 | `ddrescue`、`dd_rescue` |
| 依赖 | `libc6`、`liblzo2-2`、`libssl3t64`、`dd_rescue` |
| 安装体积 | 411 KB |
| 官网 | <http://www.garloff.de/kurt/linux/ddrescue/> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/ddrescue> |
| 包追踪 | <https://pkg.kali.org/pkg/ddrescue> |

## 2. 官方用法示例

> 以下为 Kali 官方工具页给出的示例与输出原文。

```text
Usage Example
Start at position 100 of the input file (-s 100 /var/log/messages) and write, beginning at position 0 of the destination file (-S 0 /tmp/ddrescue-out):
root@kali:~# dd_rescue -s 100 /var/log/messages -S 0 /tmp/ddrescue-out
dd_rescue: (info): Using softbs=65536, hardbs=4096
dd_rescue: (info) expect to copy 1766kB from /var/log/messages
dd_rescue: (info): ipos:      1024.1k, opos:      1024.0k, xferd:      1024.0k
                   errs:      0, errxfer:         0.0k, succxfer:      1024.0k
             +curr.rate:  1122807kB/s, avg.rate:  1018906kB/s, avg.load:  0.0%
             >.......................-.................<  57%  ETA:  0:00:00
dd_rescue: (info): read /var/log/messages (1767.0k): EOF
dd_rescue: (info): Summary for /var/log/messages -> /tmp/ddrescue-out:
dd_rescue: (info): ipos:      1767.0k, opos:      1767.0k, xferd:      1767.0k
                   errs:      0, errxfer:         0.0k, succxfer:      1767.0k
             +curr.rate:   352945kB/s, avg.rate:   568151kB/s, avg.load:  0.0%
             >.......................-................-< 100%  ETA:  0:00:00
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 2 个可执行命令，下面是官方页面内嵌的帮助原文。

### `dd_rescue`

> 官方示例调用：`dd_rescue -s 100 /var/log/messages -S 0 /tmp/ddrescue-out`

```text
root@kali:~# dd_rescue -s 100 /var/log/messages -S 0 /tmp/ddrescue-out
dd_rescue: (info): Using softbs=65536, hardbs=4096
dd_rescue: (info) expect to copy 1766kB from /var/log/messages
dd_rescue: (info): ipos:      1024.1k, opos:      1024.0k, xferd:      1024.0k
                   errs:      0, errxfer:         0.0k, succxfer:      1024.0k
             +curr.rate:  1122807kB/s, avg.rate:  1018906kB/s, avg.load:  0.0%
             >.......................-.................<  57%  ETA:  0:00:00
dd_rescue: (info): read /var/log/messages (1767.0k): EOF
dd_rescue: (info): Summary for /var/log/messages -> /tmp/ddrescue-out:
dd_rescue: (info): ipos:      1767.0k, opos:      1767.0k, xferd:      1767.0k
                   errs:      0, errxfer:         0.0k, succxfer:      1767.0k
             +curr.rate:   352945kB/s, avg.rate:   568151kB/s, avg.load:  0.0%
             >.......................-................-< 100%  ETA:  0:00:00
```

### `dd_rescue -h`

> 官方示例调用：`dd_rescue -h`

```text
root@kali:~# dd_rescue -h
dd_rescue Version 1.99.13,
[email protected]
, GNU GPL v2/v3
 (DD_RESCUE_1_99_13)
 (compiled May 21 2025 11:21:52 by gcc (Debian 14.2.0-19) 14.2.0)
 (features: O_DIRECT dl/libfallocate fallocate splice fitrim xattr rdrnd sse4.2)
dd_rescue is free software. It's protected by the terms of GNU GPL v2 or v3
 (at your option).
dd_rescue copies data from one file (or device or pipe) to others.
USAGE: dd_rescue [options] infile outfile
Options: -s ipos    start position in  input file (default=0),
         -S opos    start position in output file (def=ipos),
         -b softbs  block size for copy operation (def=131072, 1048576 for -d),
         -B hardbs  fallback block size in case of errs (def=4096, 512 for -d),
         -e maxerr  exit after maxerr errors (def=0=infinite),
         -m maxxfer maximum amount of data to be transferred (def=0=inf),
         -M         avoid extending outfile,
         -x         count opos from the end of outfile (eXtend),
         -y syncsz  frequency of fsync calls in bytes (def=512*softbs),
         -l logfile name of a file to log errors and summary to (def=""),
         -o bbfile  name of a file to log bad blocks numbers (def=""),
         -r         reverse direction copy (def=forward),
         -R         repeatedly write same block (def if infile is /dev/zero),
         -t         truncate output file at start (def=no),
         -T         truncate output file at last pos (def=no),
         -u         undo writes by deleting outfile and issuing fstrim
         -d/D       use O_DIRECT for input/output (def=no),
         -k         use efficient in-kernel zerocopy splice,
         -P         use fallocate to preallocate target space,
         -L plug1[=par1[:par2]][,plug2[,..]]    load plugins,
         -w         abort on Write errors (def=no),
         -W         read target block and avoid Writes if identical (def=no),
         -a         detect zero-filled blocks and write spArsely (def=no),
         -A         Always write blocks, zeroed if err (def=no),
         -i         interactive: ask before overwriting data (def=no),
         -f         force: skip some sanity checks (def=no),
         -p         preserve: preserve ownership, perms, times, attrs (def=no),
         -C limit   rateControl: avoid xfer data faster than limit B/s
         -Y oname   Secondary output file (multiple possible),
         -F off[-off]r/rep[,off[-off]w/rep[,...]]  fault injection (hardbs off) r/w
         -q         quiet operation,
         -v         verbose operation,
         -c 0/1     switch off/on colors (def=auto),
         -V         display version and exit,
         -h         display this help and exit.
Instead of infile, -z/Z SEED or -z/Z SEEDFILE may be specified, taking the PRNG
 from libc or frandom (RC4 based) as input. SEED = 0 means a time based seed;
 Using /dev/urandom as SEEDFILE gives good pseudo random numbers.
Likewise, -3 SEED/SEEDFILE will overwrite ofile 3 times (r,ir,0, BSI M7.15).
 With -4 SEED/SEEDFILE you get an additional random pass (r,ir,r2,0).
 With -2 SEED/SEEDFILE you only get one random pass (r,0).
Sizes may be given in units b(=512), k(=1024), M(=1024^2) or G(1024^3) bytes
This program is useful to rescue data in case of I/O errors, because
 it does not normally abort or truncate the output.
It may also help data protection by securely overwriting data.
There are plugins for compression, hashing and encryption.
Have a look a the man page for more details and long options.
Updated on: 2026-Aug-25
 Edit this page
dc3dd
defectdojo
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install ddrescue`，再执行 `ddrescue --version` 2>/dev/null || `ddrescue -V`
- [ ] **2.** **读官方帮助** —— `ddrescue -h`，需要细节时 `man ddrescue`
- [ ] **3.** **在自有靶场跑最小用例** —— 用 `ddrescue -h` 里最简单的那个子命令试一次
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/ddrescue/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/forensics.md`](../../tools/by-attack/forensics.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/ddrescue/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/ddrescue/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
