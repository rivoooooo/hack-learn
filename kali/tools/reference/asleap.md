# asleap

> A tool for exploiting Cisco LEAP networks Demonstrates a serious deficiency in proprietary Cisco LEAP networks.

> **功能分类**：无线攻击 ｜ **Kali 包**：`asleap` ｜ **官方文档**：<https://www.kali.org/tools/asleap/>

## 1. 安装

```bash
sudo apt update
sudo apt install asleap
```

| 项目 | 内容 |
|------|------|
| 版本 | 2.3~git20201128.254acab |
| 架构 | any |
| 可执行命令 | `asleap`、`genkeys` |
| 依赖 | `libc6`、`libpcap0.8t64` |
| 安装体积 | 235 KB |
| 官网 | <https://www.willhackforsushi.com/> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/asleap> |
| 包追踪 | <https://pkg.kali.org/pkg/asleap> |

## 2. 官方用法示例

> 以下为 Kali 官方工具页给出的示例与输出原文。

```text
Usage Example
Read in a dictionary file (-r /usr/share/wordlists/nmap.lst), provide an output filename (-f asleap.dat), and an output index filename (-n asleap.idx):
root@kali:~# genkeys -r /usr/share/wordlists/nmap.lst -f asleap.dat -n asleap.idx
genkeys 2.2 - generates lookup file for asleap. <jwright@hasborg.com>
Generating hashes for passwords (this may take some time) ...Done.
5085 hashes written in 0.29 seconds:  17463.18 hashes/second
Starting sort (be patient) ...Done.
Completed sort in 16254 compares.
Creating index file (almost finished) ...Done.
asleap Usage Examples

Read a capture file (-r leap.dump), provide the hashfile filename (-f asleap.dat), the hashfile index (-n asleap.idx), and skip the authentication check (-s):
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 2 个可执行命令，下面是官方页面内嵌的帮助原文。

### `genkeys`

官方给出的调用示例：`genkeys -r /usr/share/wordlists/nmap.lst -f asleap.dat -n asleap.idx`

```text
root@kali:~# genkeys -r /usr/share/wordlists/nmap.lst -f asleap.dat -n asleap.idx
genkeys 2.2 - generates lookup file for asleap. <
[email protected]
>
Generating hashes for passwords (this may take some time) ...Done.
5085 hashes written in 0.29 seconds:  17463.18 hashes/second
Starting sort (be patient) ...Done.
Completed sort in 16254 compares.
Creating index file (almost finished) ...Done.
asleap Usage Examples
Read a capture file (-r leap.dump), provide the hashfile filename (
-f asleap.dat)
, the hashfile index (
-n asleap.idx
), and skip the authentication check
(-s
):
```

### `asleap`

官方给出的调用示例：`asleap -r leap.dump -f asleap.dat -n asleap.idx -s`

```text
root@kali:~# asleap -r leap.dump -f asleap.dat -n asleap.idx -s
asleap 2.2 - actively recover LEAP/PPTP passwords. <
[email protected]
>
Captured LEAP exchange information:
    username:          qa_leap
    challenge:         0786aea0215bc30a
    response:          7f6a14f11eeb980fda11bf83a142a8744f00683ad5bc5cb6
    hash bytes:        4a39
    NT hash:           a1fc198bdbf5833a56fb40cdd1a64a39
    password:          qaleap
Crack a challenge (
-C 58:16:d5:ac:4b:dc:e4:0f
) and response (
-R 50:ae:a3:0a:10:9e:28:f9:33:1b:44:b1:3d:9e:20:91:85:e8:2e:c3:c5:4c:00:23
) from freeradius, using a wordlist (
-W password.lst
):
```

### `asleap（示例）`

官方给出的调用示例：`asleap -C 58:16:d5:ac:4b:dc:e4:0f -R 50:ae:a3:0a:10:9e:28:f9:33:1b:44:b1:3d:9e:20:91:85:e8:2e:c3:c5:4c:00:23 -W password.lst`

```text
root@kali:~# asleap -C 58:16:d5:ac:4b:dc:e4:0f -R 50:ae:a3:0a:10:9e:28:f9:33:1b:44:b1:3d:9e:20:91:85:e8:2e:c3:c5:4c:00:23 -W password.lst
asleap 2.2 - actively recover LEAP/PPTP passwords. <
[email protected]
>
Using wordlist mode with "password.lst".
    hash bytes:        586c
    NT hash:           8846f7eaee8fb117ad06bdd830b7586c
    password:          password
```

### `asleap（示例）`

官方给出的调用示例：`asleap -h`

```text
root@kali:~# asleap -h
asleap 2.3 - actively recover LEAP/PPTP passwords. <
[email protected]
>
Usage: asleap [options]
	-r 	Read from a libpcap file
	-i 	Interface to capture on
	-f 	Dictionary file with NT hashes
	-n 	Index file for NT hashes
	-s 	Skip the check to make sure authentication was successful
	-h 	Output this help information and exit
	-v 	Print verbose information (more -v for more verbosity)
	-V 	Print program version and exit
	-C 	Challenge value in colon-delimited bytes
	-R 	Response value in colon-delimited bytes
	-W 	ASCII dictionary file (special purpose)
```

### `genkeys（示例）`

官方给出的调用示例：`genkeys -h`

```text
root@kali:~# genkeys -h
genkeys 2.3 - generates lookup file for asleap. <
[email protected]
>
Usage: genkeys [options]
	-r 	Input dictionary file, one word per line
	-f 	Output pass+hash filename
	-n 	Output index filename
	-h 	Last 2 hash bytes to filter with (optional)
Learn more with
OffSec
Want to learn more about asleap? get access to in-depth training and hands-on labs:
PEN-210: 11.3. Attacking WPA Enterprise: Attack
PEN-210 course
Updated on: 2025-Dec-09
 Edit this page
armitage
autopsy
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install asleap`，再执行 `asleap --version` 2>/dev/null || `asleap -V`
- [ ] **2.** **读官方帮助** —— `asleap -h`，需要细节时 `man asleap`
- [ ] **3.** **在自有靶场跑最小用例** —— 官方给出的调用形式是：`Usage: asleap [options]`
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/asleap/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/reconnaissance.md`](../../tools/by-attack/reconnaissance.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/asleap/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/asleap/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
