# pack2

> Password analysis and cracking kit 2 This package contains a replacement for iphelix’s PACK. This is a work in progress. Not all features are available and while being similar some will differ slightly. PACK was developed in order to aid i…

> **功能分类**：口令攻击 ｜ **Kali 包**：`pack2` ｜ **官方文档**：<https://www.kali.org/tools/pack2/>

## 1. 安装

```bash
sudo apt update
sudo apt install pack2
```

| 项目 | 内容 |
|------|------|
| 版本 | 0.1.0~git20200929.da4b245 |
| 架构 | any |
| 可执行命令 | `pack2`、`pack200`、`unpack200` |
| 依赖 | `libc6`、`libgcc-s1` |
| 安装体积 | 897 KB |
| 官网 | <https://github.com/hops/pack2> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/pack2> |
| 包追踪 | <https://pkg.kali.org/pkg/pack2> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
pack2 -h          # 查看用法
man pack2         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 3 个可执行命令，下面是官方页面内嵌的帮助原文。

### `pack2`

官方给出的调用示例：`pack2 -h`

```text
root@kali:~# pack2 -h
pack2 0.1.0
USAGE:
    pack2 <SUBCOMMAND>
FLAGS:
    -h, --help       Prints help information
    -V, --version    Prints version information
SUBCOMMANDS:
    cgrams        Splits each line on the charset boundry
    filtermask    Filters a wordlist by a given mask
    help          Prints this message or the help of the given subcommand(s)
    statsgen      Generates statistics from a [input] and writes masks to <output> stats are written to stderr
    unhex         Decodes $HEX[] encoded lines
```

### `pack200`

官方给出的调用示例：`pack200 -h`

```text
root@kali:~# pack200 -h
Warning: The pack200 tool is deprecated, and is planned for removal in a future JDK release.
Usage:  pack200 [-opt... | --option=value]... x.pack[.gz] y.jar
Packing Options
  -r, --repack                    repack or normalize a jar, suitable for
                                  signing with jarsigner
  -g, --no-gzip                   output a plain pack file, suitable to be
                                  compressed with a file compression utility
  --gzip                          (default) post compress the pack output
                                  with gzip
  -G, --strip-debug               remove debugging attributes (SourceFile,
                                  LineNumberTable, LocalVariableTable
                                  and LocalVariableTypeTable) while packing
  -O, --no-keep-file-order        do not transmit file ordering information
  --keep-file-order               (default) preserve input file ordering
  -S{N}, --segment-limit={N}      limit segment sizes (default unlimited)
  -E{N}, --effort={N}             packing effort (default N=5)
  -H{h}, --deflate-hint={h}       transmit deflate hint: true, false,
                                  or keep (default)
  -m{V}, --modification-time={V}  transmit modtimes: latest or keep (default)
  -P{F}, --pass-file={F}          transmit the given input element(s) unchanged
  -U{a}, --unknown-attribute={a}  unknown attribute action: error, strip,
                                  or pass (default)
  -C{N}={L}, --class-attribute={N}={L}  (user-defined attribute)
  -F{N}={L}, --field-attribute={N}={L}  (user-defined attribute)
  -M{N}={L}, --method-attribute={N}={L} (user-defined attribute)
  -D{N}={L}, --code-attribute={N}={L}   (user-defined attribute)
  -f{F}, --config-file={F}        read file F for Pack200.Packer properties
  -v, --verbose                   increase program verbosity
  -q, --quiet                     set verbosity to lowest level
  -l{F}, --log-file={F}           output to the given log file,
                                  or '-' for System.out
  -?, -h, --help                  print this help message
  -V, --version                   print program version
  -J{X}                           pass option X to underlying Java VM
Notes:
  The -P, -C, -F, -M, and -D options accumulate.
  Example attribute definition:  -C SourceFile=RUH .
  Config. file properties are defined by the Pack200 API.
  For meaning of -S, -E, -H-, -m, -U values, see Pack200 API.
  Layout definitions (like RUH) are defined by JSR 200.
Repacking mode updates the JAR file with a pack/unpack cycle:
    pack200 [-r|--repack] [-opt | --option=value]... [repackedy.jar] y.jar
Exit Status:
  0 if successful, >0 if an error occurred
Warning: The pack200 tool is deprecated, and is planned for removal in a future JDK release.
```

### `unpack200`

官方给出的调用示例：`unpack200 -h`

```text
root@kali:~# unpack200 -h
Warning: The unpack200 tool is deprecated, and is planned for removal in a future JDK release.
Usage:  unpack200 [-opt... | --option=value]... x.pack[.gz] y.jar
Unpacking Options
  -H{h}, --deflate-hint={h}     override transmitted deflate hint:
                                true, false, or keep (default)
  -r, --remove-pack-file        remove input file after unpacking
  -v, --verbose                 increase program verbosity
  -q, --quiet                   set verbosity to lowest level
  -l{F}, --log-file={F}         output to the given log file,
                                or '-' for standard output (default)
  -?, -h, --help                print this help message
  -V, --version                 print program version
Exit Status:
  0 if successful, >0 if an error occurred
Updated on: 2025-Dec-09
 Edit this page
p0f
paros
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install pack2`，再执行 `pack2 --version` 2>/dev/null || `pack2 -V`
- [ ] **2.** **读官方帮助** —— `pack2 -h`，需要细节时 `man pack2`
- [ ] **3.** **在自有靶场跑最小用例** —— 官方给出的调用形式是：`Usage:  pack200 [-opt... | --option=value]... x.pack[.gz] y.jar`
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/pack2/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/pack2/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/pack2/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
