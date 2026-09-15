# ophcrack

> Microsoft Windows password cracker using rainbow tables (gui) Ophcrack is a Windows password cracker based on a time-memory trade-off using rainbow tables. This is a new variant of Hellman’s original trade-off, with better performance. It …

> **功能分类**：口令攻击 ｜ **Kali 包**：`ophcrack` ｜ **官方文档**：<https://www.kali.org/tools/ophcrack/>

## 1. 安装

```bash
sudo apt update
sudo apt install ophcrack
```

| 项目 | 内容 |
|------|------|
| 版本 | 3.8.0 |
| 架构 | any |
| 可执行命令 | `ophcrack`、`ophcrack-cli` |
| 依赖 | `libc6`、`libexpat1`、`libgcc-s1`、`libqt5charts5`、`libqt5core5t64` |
| 安装体积 | 501 KB |
| 官网 | <https://ophcrack.sourceforge.net/> |
| 源码仓库 | <https://salsa.debian.org/pkg-security-team/ophcrack> |
| 包追踪 | <https://pkg.kali.org/pkg/ophcrack> |

## 2. 官方用法示例

> 以下为 Kali 官方工具页给出的示例与输出原文。

```text
Screenshots
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 2 个可执行命令，下面是官方页面内嵌的帮助原文。

### `ophcrack`

> 官方示例调用：`ophcrack -h`

```text
root@kali:~# ophcrack -h
ophcrack 3.8.0 by Objectif Securite (http://www.objectif-securite.ch)
Usage: ophcrack [OPTIONS]
Cracks Windows passwords with Rainbow tables
  -a              disable audit mode (default)
  -A              enable audit mode
  -b              disable bruteforce
  -B              enable bruteforce (default)
  -c config_file  specify the config file to use
  -D              display (lots of!) debugging information
  -d dir          specify tables base directory
  -e              do not display empty passwords
  -f file         load hashes from the specified file (pwdump or session)
  -g              disable GUI
  -h              display this information
  -i              hide usernames
  -I              show usernames (default)
  -l file         log all output to the specified file
  -n num          specify the number of threads to use
  -o file         write cracking output to file in pwdump format
  -p num          preload (0 none, 1 index, 2 index+end, 3 all default)
  -q              quiet mode
  -r              launch the cracking when ophcrack starts (GUI only)
  -s              disable session auto-saving
  -S session_file specify the file to use to automatically save the progress of the search
  -u              display statistics when cracking ends
  -t table1[,a[,b,...]][:table2[,a[,b,...]]]
                  specify which table to use in the directory given by -d
  -v              verbose
  -w dir          load hashes from encrypted SAM file in directory dir
  -x file         export data in CSV format to file
Example:	ophcrack -g -d /path/to/tables -t xp_free_fast,0,3:vista_free -f in.txt
		Launch ophcrack in command line using tables 0 and 3 in
		/path/to/tables/xp_free_fast and all tables in /path/to/tables/vista_free
		and cracks hashes from pwdump file in.txt
```

### `ophcrack-cli`

> 官方示例调用：`ophcrack-cli -h`

```text
root@kali:~# ophcrack-cli -h
ophcrack 3.8.0 by Objectif Securite (http://www.objectif-securite.ch)
Usage: ophcrack [OPTIONS]
Cracks Windows passwords with Rainbow tables
  -a              disable audit mode (default)
  -A              enable audit mode
  -b              disable bruteforce
  -B              enable bruteforce (default)
  -c config_file  specify the config file to use
  -D              display (lots of!) debugging information
  -d dir          specify tables base directory
  -e              do not display empty passwords
  -f file         load hashes from the specified file (pwdump or session)
  -g              disable GUI
  -h              display this information
  -i              hide usernames
  -I              show usernames (default)
  -l file         log all output to the specified file
  -n num          specify the number of threads to use
  -o file         write cracking output to file in pwdump format
  -p num          preload (0 none, 1 index, 2 index+end, 3 all default)
  -q              quiet mode
  -r              launch the cracking when ophcrack starts (GUI only)
  -s              disable session auto-saving
  -S session_file specify the file to use to automatically save the progress of the search
  -u              display statistics when cracking ends
  -t table1[,a[,b,...]][:table2[,a[,b,...]]]
                  specify which table to use in the directory given by -d
  -v              verbose
  -w dir          load hashes from encrypted SAM file in directory dir
  -x file         export data in CSV format to file
Example:	ophcrack -g -d /path/to/tables -t xp_free_fast,0,3:vista_free -f in.txt
		Launch ophcrack in command line using tables 0 and 3 in
		/path/to/tables/xp_free_fast and all tables in /path/to/tables/vista_free
		and cracks hashes from pwdump file in.txt
Updated on: 2025-Dec-09
 Edit this page
onesixtyone
owl
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install ophcrack`，再执行 `ophcrack --version` 2>/dev/null || `ophcrack -V`
- [ ] **2.** **读官方帮助** —— `ophcrack -h`，需要细节时 `man ophcrack`
- [ ] **3.** **在自有靶场跑最小用例** —— 官方给出的调用形式是：`Usage: ophcrack [OPTIONS]`
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/ophcrack/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- **精讲教程**（含原理、参数详解、靶场实操与输出解读）：[ophcrack](../../tools/tutorials/04-口令攻击/ophcrack.md)
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/credential-access.md`](../../tools/by-attack/credential-access.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/ophcrack/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/ophcrack/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
