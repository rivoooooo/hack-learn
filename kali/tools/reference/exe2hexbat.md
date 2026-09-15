# exe2hexbat

> Convert EXE to bat A Python script to convert a Windows PE executable file to a batch file and vice versa.

> **功能分类**：后渗透 ｜ **Kali 包**：`exe2hexbat` ｜ **官方文档**：<https://www.kali.org/tools/exe2hexbat/>

## 1. 安装

```bash
sudo apt update
sudo apt install exe2hexbat
```

| 项目 | 内容 |
|------|------|
| 版本 | 1.5.1 |
| 架构 | all |
| 可执行命令 | `exe2hexbat`、`exe2hex` |
| 依赖 | `python3`、`exe2hex` |
| 安装体积 | 37 KB |
| 官网 | <https://github.com/g0tmi1k/exe2hex/> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/exe2hexbat> |
| 包追踪 | <https://pkg.kali.org/pkg/exe2hexbat> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
exe2hexbat -h          # 查看用法
man exe2hexbat         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 2 个可执行命令，下面是官方页面内嵌的帮助原文。

### `exe2hex`

> 官方示例调用：`exe2hex -h`

```text
root@kali:~# exe2hex -h
[*] exe2hex v1.5.1
Usage: exe2hex [options]
Options:
  -h, --help  show this help message and exit
  -x EXE      The EXE binary file to convert
  -s          Read from STDIN
  -b BAT      BAT output file (DEBUG.exe method - x86)
  -p POSH     PoSh output file (PowerShell method - x86/x64)
  -e          URL encode the output
  -r TEXT     pRefix - text to add before the command on each line
  -f TEXT     suFfix - text to add after the command on each line
  -l INT      Maximum HEX values per line
  -c          Clones and compress the file before converting (-cc for higher
              compression)
  -t          Create a Expect file, to automate to a Telnet session.
  -w          Create a Expect file, to automate to a WinEXE session.
  -v          Enable verbose mode
Updated on: 2025-Dec-09
 Edit this page
evilginx2
exploitdb-bin-sploits
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install exe2hexbat`，再执行 `exe2hexbat --version` 2>/dev/null || `exe2hexbat -V`
- [ ] **2.** **读官方帮助** —— `exe2hexbat -h`，需要细节时 `man exe2hexbat`
- [ ] **3.** **在自有靶场跑最小用例** —— 官方给出的调用形式是：`Usage: exe2hex [options]`
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/exe2hexbat/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/defense-evasion.md`](../../tools/by-attack/defense-evasion.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/exe2hexbat/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/exe2hexbat/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
