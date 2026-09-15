# libsmali-java

> Assembler/disassembler for Android’s dex format smali/baksmali is an assembler/disassembler for the dex format used by dalvik, Android’s Java VM implementation. The syntax is loosely based on Jasmin’s/dedexer’s syntax and supports the full…

> **功能分类**：数字取证 ｜ **Kali 包**：`libsmali-java` ｜ **官方文档**：<https://www.kali.org/tools/libsmali-java/>

## 1. 安装

```bash
sudo apt update
sudo apt install libsmali-java
```

| 项目 | 内容 |
|------|------|
| 版本 | 2.5.2.git2771eae |
| 架构 | all |
| 可执行命令 | `libsmali-java`、`baksmali`、`smali` |
| 依赖 | `java-wrappers`、`libantlr3-runtime-java`、`libguava-java`、`libjcommander-java`、`baksmali` |
| 安装体积 | 1.57 MB |
| 官网 | <https://github.com/JesusFreke/smali> |
| 源码仓库 | <https://salsa.debian.org/android-tools-team/libsmali-java> |
| 包追踪 | <https://pkg.kali.org/pkg/libsmali-java> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
libsmali-java -h          # 查看用法
man libsmali-java         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 3 个可执行命令，下面是官方页面内嵌的帮助原文。

### `baksmali`

官方给出的调用示例：`baksmali -h`

```text
root@kali:~# baksmali -h
usage: baksmali [--version] [--help] [<command [<args>]]
Options:
  --help,-h,-? - Show usage information
  --version,-v - Print the version of baksmali and then exit
Commands:
  deodex(de,x) - Deodexes an odex/oat file
  disassemble(dis,d) - Disassembles a dex file.
  dump(du) - Prints an annotated hex dump for the given dex file
  help(h) - Shows usage information
  list(l) - Lists various objects in a dex file.
See baksmali help <command> for more information about a specific command
```

### `smali`

官方给出的调用示例：`smali -h`

```text
root@kali:~# smali -h
usage: smali [-v] [-h] [<command [<args>]]
Options:
  -h,-?,--help - Show usage information
  -v,--version - Print the version of baksmali and then exit
Commands:
  assemble(ass,as,a) - Assembles smali files into a dex file.
  help(h) - Shows usage information
See smali help <command> for more information about a specific command
Updated on: 2025-Dec-09
 Edit this page
libpst
linux-exploit-suggester
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install libsmali-java`，再执行 `libsmali-java --version` 2>/dev/null || `libsmali-java -V`
- [ ] **2.** **读官方帮助** —— `libsmali-java -h`，需要细节时 `man libsmali-java`
- [ ] **3.** **在自有靶场跑最小用例** —— 用 `libsmali-java -h` 里最简单的那个子命令试一次
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/libsmali-java/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/libsmali-java/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/libsmali-java/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
