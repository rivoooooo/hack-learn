# princeprocessor

> Standalone password candidate generator using the PRINCE algorithm Princeprocessor is a password candidate generator and can be thought of as an advanced combinator attack. Rather than taking as input two different wordlists and then outpu…

> **功能分类**：通用工具 ｜ **Kali 包**：`princeprocessor` ｜ **官方文档**：<https://www.kali.org/tools/princeprocessor/>

## 1. 安装

```bash
sudo apt update
sudo apt install princeprocessor
```

| 项目 | 内容 |
|------|------|
| 版本 | 0.22 |
| 架构 | amd64 |
| 可执行命令 | `princeprocessor` |
| 依赖 | `libc6` |
| 安装体积 | 121 KB |
| 官网 | <https://github.com/hashcat/princeprocessor> |
| 源码仓库 | <https://salsa.debian.org/pkg-security-team/princeprocessor> |
| 包追踪 | <https://pkg.kali.org/pkg/princeprocessor> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
princeprocessor -h          # 查看用法
man princeprocessor         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `princeprocessor`

官方给出的调用示例：`princeprocessor -h`

```text
root@kali:~# princeprocessor -h
Usage: princeprocessor [options] [<] wordlist
* Startup:
  -V,  --version             Print version
  -h,  --help                Print help
* Misc:
       --keyspace            Calculate number of combinations
* Optimization:
       --pw-min=NUM          Print candidate if length is greater than NUM
       --pw-max=NUM          Print candidate if length is smaller than NUM
       --elem-cnt-min=NUM    Minimum number of elements per chain
       --elem-cnt-max=NUM    Maximum number of elements per chain
       --wl-dist-len         Calculate output length distribution from wordlist
       --wl-max=NUM          Load only NUM words from input wordlist or use 0 to disable
  -c,  --dupe-check-disable  Disable dupes check for faster initial load
       --save-pos-disable    Save the position for later resume with -s
* Resources:
  -s,  --skip=NUM            Skip NUM passwords from start (for distributed)
  -l,  --limit=NUM           Limit output to NUM passwords (for distributed)
* Files:
  -o,  --output-file=FILE    Output-file
* Amplifier:
       --case-permute        For each word in the wordlist that begins with a letter
                             generate a word with the opposite case of the first letter
Updated on: 2025-Dec-09
 Edit this page
powersploit
proxify
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install princeprocessor`，再执行 `princeprocessor --version` 2>/dev/null || `princeprocessor -V`
- [ ] **2.** **读官方帮助** —— `princeprocessor -h`，需要细节时 `man princeprocessor`
- [ ] **3.** **在自有靶场跑最小用例** —— 官方给出的调用形式是：`Usage: princeprocessor [options] [<] wordlist`
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/princeprocessor/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/princeprocessor/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/princeprocessor/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
