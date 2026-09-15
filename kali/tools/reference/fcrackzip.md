# fcrackzip

> Password cracker for zip archives fcrackzip is a fast password cracker partly written in assembler. It is able to crack password protected zip files with brute force or dictionary based attacks, optionally testing with unzip its results. I…

> **功能分类**：口令攻击 ｜ **Kali 包**：`fcrackzip` ｜ **官方文档**：<https://www.kali.org/tools/fcrackzip/>

## 1. 安装

```bash
sudo apt update
sudo apt install fcrackzip
```

| 项目 | 内容 |
|------|------|
| 版本 | 1.0 |
| 架构 | any |
| 可执行命令 | `fcrackzip`、`fcrackzipinfo` |
| 依赖 | `libc6` |
| 安装体积 | 80 KB |
| 官网 | <http://oldhome.schmorp.de/marc/fcrackzip.html> |
| 源码仓库 | <https://salsa.debian.org/pkg-security-team/fcrackzip> |
| 包追踪 | <https://pkg.kali.org/pkg/fcrackzip> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
fcrackzip -h          # 查看用法
man fcrackzip         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 2 个可执行命令，下面是官方页面内嵌的帮助原文。

### `fcrackzip`

> 官方示例调用：`fcrackzip -h`

```text
root@kali:~# fcrackzip -h
fcrackzip version 1.0, a fast/free zip password cracker
written by Marc Lehmann <
[email protected]
> You can find more info on
http://www.goof.com/pcg/marc/
USAGE: fcrackzip
          [-b|--brute-force]            use brute force algorithm
          [-D|--dictionary]             use a dictionary
          [-B|--benchmark]              execute a small benchmark
          [-c|--charset characterset]   use characters from charset
          [-h|--help]                   show this message
          [--version]                   show the version of this program
          [-V|--validate]               sanity-check the algorithm
          [-v|--verbose]                be more verbose
          [-p|--init-password string]   use string as initial password/file
          [-l|--length min-max]         check password with length min to max
          [-u|--use-unzip]              use unzip to weed out wrong passwords
          [-m|--method num]             use method number "num" (see below)
          [-2|--modulo r/m]             only calculcate 1/m of the password
          file...                    the zipfiles to crack
methods compiled in (* = default):
 0: cpmask
 1: zip1
*2: zip2, USE_MULT_TAB
```

### `fcrackzipinfo`

> 官方示例调用：`fcrackzipinfo --help`

```text
root@kali:~# fcrackzipinfo --help
fcrackzip version 1.0, zipinfo - tell me about a zip file
written by Marc Lehmann <
[email protected]
> You can find more info on
http://www.goof.com/pcg/marc/
USAGE: zipinfo file...                the zipfiles to parse
Updated on: 2025-Dec-09
 Edit this page
fatcat
fiked
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install fcrackzip`，再执行 `fcrackzip --version` 2>/dev/null || `fcrackzip -V`
- [ ] **2.** **读官方帮助** —— `fcrackzip -h`，需要细节时 `man fcrackzip`
- [ ] **3.** **在自有靶场跑最小用例** —— 用 `fcrackzip -h` 里最简单的那个子命令试一次
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/fcrackzip/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/credential-access.md`](../../tools/by-attack/credential-access.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/fcrackzip/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/fcrackzip/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
