# cisco7crack

> Crypt and decrypt the cisco type 7 passwords This tool is used to crack Cisco Type 7 passwords. Can be used to encrypt and decrypt Cisco device passwords. Originally designed in order to allow quick decryption of stored passwords, Type 7 p…

> **功能分类**：通用工具 ｜ **Kali 包**：`cisco7crack` ｜ **官方文档**：<https://www.kali.org/tools/cisco7crack/>

## 1. 安装

```bash
sudo apt update
sudo apt install cisco7crack
```

| 项目 | 内容 |
|------|------|
| 版本 | 0.0~git20121221.f1c21dd |
| 架构 | any |
| 可执行命令 | `cisco7crack` |
| 依赖 | `libc6` |
| 安装体积 | 28 KB |
| 官网 | <https://github.com/madrisan/cisco7crack> |
| 源码仓库 | <https://salsa.debian.org/pkg-security-team/cisco7crack> |
| 包追踪 | <https://pkg.kali.org/pkg/cisco7crack> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
cisco7crack -h          # 查看用法
man cisco7crack         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `cisco7crack`

> 官方示例调用：`cisco7crack -h`

```text
root@kali:~# cisco7crack -h
*** cisco7crack v2.3.4 - San Oct 19, 2002
    copyright (c) 2002 by Davide Madrisan <
[email protected]
>
    the GNU GPLv2 applies to this program and code
usage:
   cisco7crack [-q] -c [-{a|#<0..15>}] <plaintext>
   cisco7crack [-q] [-d] <ciphertext>
   cisco7crack [-h]
flags:    means:
  -c        crypt <plaintext>
  -a        display all the ways to crypt <plaintext>
  -#<n>     display the n-th way to crypt <plaintext>
  -d        decrypt <ciphertext> (default option)
  -q        cause cisco7crack to be really quiet
  -h        display this brief usage summary
examples are:
   cisco7crack -c#3 '@l1c3&b0b'
   cisco7crack -c#3 -q n0v3rb0s3
   cisco7crack 082F1C5A1A490D43000F5E033F78373B
   a=`cisco7crack -cq b@shscr1pt`  # (bash shell)
   [ $? -eq 0 ] && echo "crypt: $a" || echo "error!"
enjoy cracking the Cisco IOS pesky passwords...
for bugs and suggestions, please contact me by e-mail
Updated on: 2025-Dec-09
 Edit this page
cisco-torch
cloudbrute
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install cisco7crack`，再执行 `cisco7crack --version` 2>/dev/null || `cisco7crack -V`
- [ ] **2.** **读官方帮助** —— `cisco7crack -h`，需要细节时 `man cisco7crack`
- [ ] **3.** **在自有靶场跑最小用例** —— 用 `cisco7crack -h` 里最简单的那个子命令试一次
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/cisco7crack/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/cisco7crack/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/cisco7crack/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
