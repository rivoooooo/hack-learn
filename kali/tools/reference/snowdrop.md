# snowdrop

> Plain text watermarking and watermark recovery Snowdrop provides reliable, difficult to remove steganographic watermarking of text documents (internal memos, draft research papers, advisories and other writing) and C sources (limited distr…

> **功能分类**：通用工具 ｜ **Kali 包**：`snowdrop` ｜ **官方文档**：<https://www.kali.org/tools/snowdrop/>

## 1. 安装

```bash
sudo apt update
sudo apt install snowdrop
```

| 项目 | 内容 |
|------|------|
| 版本 | 0.02b |
| 架构 | any |
| 可执行命令 | `snowdrop`、`sd-c`、`sd-eng`、`sd-engf` |
| 依赖 | `libc6`、`libssl3t64`、`sd-c` |
| 安装体积 | 194 KB |
| 官网 | <http://lcamtuf.coredump.cx/> |
| 源码仓库 | <https://salsa.debian.org/pkg-security-team/snowdrop/tree/debian/master> |
| 包追踪 | <https://pkg.kali.org/pkg/snowdrop> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
snowdrop -h          # 查看用法
man snowdrop         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 4 个可执行命令，下面是官方页面内嵌的帮助原文。

### `sd-c`

官方给出的调用示例：`sd-c -h`

```text
root@kali:~# sd-c -h
snowdrop 0.02b: text watermarking / watermark recovery by
[email protected]
[*] Weak 32-bit watermarking used (use -6 to change it).
Usage: sd-c [ -6 ] -e origfile newfile
       sd-c [ -6 ] -l
       sd-c [ -6 ] -i origfile newfile "Recipient" [ "Comment" ]
First method of calling the program (with -e option) enables watermark
extraction mode. In this mode, file passed as a first parameter must be
the original document used to generate second file (or its portions).
Second method (-l) simply lists the contents of the watermark database
for the module you're now running.
Third method (-i) enables watermark injection mode. File 'origfile' is
modified and saved as 'newfile'. Mandatory parameter is the recipient
identifier. Optional comment can be added for your reference.
Additional parameter -6 enables strong, 64-bit watermarking that is suitable
for providing public documentation of watermarked document abuse.
```

### `sd-eng`

官方给出的调用示例：`sd-eng -h`

```text
root@kali:~# sd-eng -h
snowdrop 0.02b: text watermarking / watermark recovery by
[email protected]
[*] Weak 32-bit watermarking used (use -6 to change it).
Usage: sd-eng [ -6 ] -e origfile newfile
       sd-eng [ -6 ] -l
       sd-eng [ -6 ] -i origfile newfile "Recipient" [ "Comment" ]
First method of calling the program (with -e option) enables watermark
extraction mode. In this mode, file passed as a first parameter must be
the original document used to generate second file (or its portions).
Second method (-l) simply lists the contents of the watermark database
for the module you're now running.
Third method (-i) enables watermark injection mode. File 'origfile' is
modified and saved as 'newfile'. Mandatory parameter is the recipient
identifier. Optional comment can be added for your reference.
Additional parameter -6 enables strong, 64-bit watermarking that is suitable
for providing public documentation of watermarked document abuse.
This module supports SD_SYNONYMS environment variable that should
point to an alternative 'synonyms' file, if necessary. Make sure
to keep the copy of used alternative file for further reference.
```

### `sd-engf`

官方给出的调用示例：`sd-engf -h`

```text
root@kali:~# sd-engf -h
snowdrop 0.02b: text watermarking / watermark recovery by
[email protected]
[*] Weak 32-bit watermarking used (use -6 to change it).
Usage: sd-engf [ -6 ] -e origfile newfile
       sd-engf [ -6 ] -l
       sd-engf [ -6 ] -i origfile newfile "Recipient" [ "Comment" ]
First method of calling the program (with -e option) enables watermark
extraction mode. In this mode, file passed as a first parameter must be
the original document used to generate second file (or its portions).
Second method (-l) simply lists the contents of the watermark database
for the module you're now running.
Third method (-i) enables watermark injection mode. File 'origfile' is
modified and saved as 'newfile'. Mandatory parameter is the recipient
identifier. Optional comment can be added for your reference.
Additional parameter -6 enables strong, 64-bit watermarking that is suitable
for providing public documentation of watermarked document abuse.
This module supports SD_SYNONYMS environment variable that should
point to an alternative 'synonyms' file, if necessary. Make sure
to keep the copy of used alternative file for further reference.
Updated on: 2026-May-25
 Edit this page
snort
sparrow-wifi
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install snowdrop`，再执行 `snowdrop --version` 2>/dev/null || `snowdrop -V`
- [ ] **2.** **读官方帮助** —— `snowdrop -h`，需要细节时 `man snowdrop`
- [ ] **3.** **在自有靶场跑最小用例** —— 官方给出的调用形式是：`Usage: sd-c [ -6 ] -e origfile newfile`
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/snowdrop/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/snowdrop/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/snowdrop/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
