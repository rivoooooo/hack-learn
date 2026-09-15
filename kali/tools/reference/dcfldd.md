# dcfldd

> Enhanced version of dd for forensics and security dcfldd was initially developed at Department of Defense Computer Forensics Lab (DCFL). This tool is based on the dd program with the following additional features: Hashing on-the-fly: dcfld…

> **功能分类**：数字取证 ｜ **Kali 包**：`dcfldd` ｜ **官方文档**：<https://www.kali.org/tools/dcfldd/>

## 1. 安装

```bash
sudo apt update
sudo apt install dcfldd
```

| 项目 | 内容 |
|------|------|
| 版本 | 1.9.3 |
| 架构 | any |
| 可执行命令 | `dcfldd` |
| 依赖 | `libc6` |
| 安装体积 | 113 KB |
| 官网 | <https://github.com/resurrecting-open-source-projects/dcfldd> |
| 源码仓库 | <https://salsa.debian.org/debian/dcfldd> |
| 包追踪 | <https://pkg.kali.org/pkg/dcfldd> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
dcfldd -h          # 查看用法
man dcfldd         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `dcfldd`

> 官方示例调用：`dcfldd --help`

```text
root@kali:~# dcfldd --help
Usage: dcfldd [OPTION]...
Enhanced version of dd for forensics and security.
  bs=BYTES            force ibs=BYTES and obs=BYTES (default=32768)
  cbs=BYTES           convert BYTES bytes at a time
  conv=KEYWORDS       convert the file as per the comma separated keyword list
  count=BLOCKS        copy only BLOCKS input blocks
  limit=BYTES         similar to count but using BYTES instead of BLOCKS
  ibs=BYTES           read BYTES bytes at a time
  if=FILE             read from FILE instead of stdin
  obs=BYTES           write BYTES bytes at a time
  of=FILE             write to FILE instead of stdout
  of:=COMMAND         exec and write output to process COMMAND
  seek=BLOCKS         skip BLOCKS obs-sized blocks at start of output
  skip=BLOCKS         skip BLOCKS ibs-sized blocks at start of input
  pattern=HEX         use the specified binary pattern as input
  textpattern=TEXT    use repeating TEXT as input
  errlog=FILE         send error messages to FILE as well as stderr
  hash=NAME           do hash calculation (md5, sha1, sha256, sha384 or sha512)
  hashlog=FILE        send hash output to FILE instead of stderr
  hashwindow=BYTES    perform a hash on every BYTES amount of data
  hashlog:=COMMAND    exec and write hashlog to process COMMAND
  ALGORITHMlog:=COMMAND    also works in the same fashion of hashlog:=COMMAND
  hashconv=[before|after]  perform the hashing before or after the conversions
  hashformat=FORMAT        display each hashwindow according to FORMAT
  totalhashformat=FORMAT   display the total hash value according to FORMAT
  status=[on|off]          display a continual status message on stderr
  statusinterval=N         update the status message every N blocks
  sizeprobe=[if|of|BYTES]  what to use as value to percentage indicator
  split=BYTES              write every BYTES amount of data to a new file
  splitformat=[TEXT|MAC|WIN]  the file extension format for split operation
  vf=FILE                  verify that FILE matches the specified input
  verifylog=FILE           send verify results to FILE instead of stderr
  verifylog:=COMMAND       exec and write verify results to process COMMAND
  diffwr=[on|off]          only write to output if destination block content differs
  --help              display this help and exit
  --version           output version information and exit
Read the manpage dcfldd(1) for more details about each option and to see
some examples.
Report bugs at
https://github.com/resurrecting-open-source-projects/dcfldd/issues
Updated on: 2025-Dec-09
 Edit this page
dbd
dirbuster
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install dcfldd`，再执行 `dcfldd --version` 2>/dev/null || `dcfldd -V`
- [ ] **2.** **读官方帮助** —— `dcfldd -h`，需要细节时 `man dcfldd`
- [ ] **3.** **在自有靶场跑最小用例** —— 官方给出的调用形式是：`Usage: dcfldd [OPTION]...`
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/dcfldd/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- **精讲教程**（含原理、参数详解、靶场实操与输出解读）：[dcfldd](../../tools/tutorials/09-数字取证/dcfldd.md)
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/forensics.md`](../../tools/by-attack/forensics.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/dcfldd/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/dcfldd/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
