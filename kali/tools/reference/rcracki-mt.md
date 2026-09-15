# rcracki-mt

> Version of rcrack that supports hybrid and indexed tables rcracki_mt is our modified version of rcrack which supports hybrid and indexed tables. In addition to that, it also adds multi-core support

> **功能分类**：口令攻击 ｜ **Kali 包**：`rcracki-mt` ｜ **官方文档**：<https://www.kali.org/tools/rcracki-mt/>

## 1. 安装

```bash
sudo apt update
sudo apt install rcracki-mt
```

| 项目 | 内容 |
|------|------|
| 版本 | 0.7.0 |
| 架构 | any |
| 可执行命令 | `rcracki-mt`、`rcracki_mt` |
| 依赖 | `libc6`、`libgcc-s1`、`libssl3t64`、`libstdc++6`、`rcracki_mt` |
| 安装体积 | 406 KB |
| 官网 | <https://freerainbowtables.com/> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/rcracki-mt> |
| 包追踪 | <https://pkg.kali.org/pkg/rcracki-mt> |

## 2. 官方用法示例

> 以下为 Kali 官方工具页给出的示例与输出原文。

```text
Usage Example
Crack the password hash (-h 5d41402abc4b2a76b9719d911017c592) using 4 CPU cores (-t 4) and the specified rainbow tables (tables2/md5/):
root@kali:~# rcracki_mt -h 5d41402abc4b2a76b9719d911017c592 -t 4 tables2/md5/
Using 4 threads for pre-calculation and false alarm checking...
Found 440 rainbowtable files...

md5_mixalpha-numeric-space#1-8_0_60000x27443102_distrrtgen[p][i]_109.rti2:
Chain Position is now 27443102
192101714 bytes read, disk access time: 1.19 s
searching for 1 hash...
cryptanalysis time: 0.26 s
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 2 个可执行命令，下面是官方页面内嵌的帮助原文。

### `rcracki_mt`

> 官方示例调用：`rcracki_mt -h 5d41402abc4b2a76b9719d911017c592 -t 4 tables2/md5/`

```text
root@kali:~# rcracki_mt -h 5d41402abc4b2a76b9719d911017c592 -t 4 tables2/md5/
Using 4 threads for pre-calculation and false alarm checking...
Found 440 rainbowtable files...
md5_mixalpha-numeric-space#1-8_0_60000x27443102_distrrtgen[p][i]_109.rti2:
Chain Position is now 27443102
192101714 bytes read, disk access time: 1.19 s
searching for 1 hash...
cryptanalysis time: 0.26 s
```

### `rcracki_mt -h`

> 官方示例调用：`rcracki_mt -h`

```text
root@kali:~# rcracki_mt -h
Using 1 threads for pre-calculation and false alarm checking...
no rainbow table found
Updated on: 2025-Dec-09
 Edit this page
raven
recon-ng
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install rcracki-mt`，再执行 `rcracki-mt --version` 2>/dev/null || `rcracki-mt -V`
- [ ] **2.** **读官方帮助** —— `rcracki-mt -h`，需要细节时 `man rcracki-mt`
- [ ] **3.** **在自有靶场跑最小用例** —— 用 `rcracki-mt -h` 里最简单的那个子命令试一次
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/rcracki-mt/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/credential-access.md`](../../tools/by-attack/credential-access.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/rcracki-mt/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/rcracki-mt/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
