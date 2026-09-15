# ridenum

> Null session RID cycle attack tool Rid Enum is a RID cycling attack that attempts to enumerate user accounts through null sessions and the SID to RID enum. If you specify a password file, it will automatically attempt to brute force the us…

> **功能分类**：通用工具 ｜ **Kali 包**：`ridenum` ｜ **官方文档**：<https://www.kali.org/tools/ridenum/>

## 1. 安装

```bash
sudo apt update
sudo apt install ridenum
```

| 项目 | 内容 |
|------|------|
| 版本 | 1.7 |
| 架构 | all |
| 可执行命令 | `ridenum` |
| 依赖 | `python3`、`python3-pexpect` |
| 安装体积 | 32 KB |
| 官网 | <https://github.com/trustedsec/ridenum> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/ridenum> |
| 包追踪 | <https://pkg.kali.org/pkg/ridenum> |

## 2. 官方用法示例

> 以下为 Kali 官方工具页给出的示例与输出原文。

```text
Usage Example
Connect to the remote server (192.168.1.236) and cycle from RID 500 to 50000 (500 50000), using the given password file (/tmp/passes.txt):
root@kali:~# ridenum 192.168.1.236 500 50000 /tmp/passes.txt
[*] Attempting lsaquery first...This will enumerate the base domain SID
[*] Successfully enumerated base domain SID.. Moving on to extract via RID
[*] Enumerating user accounts.. This could take a little while.
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `ridenum`

官方给出的调用示例：`ridenum 192.168.1.236 500 50000 /tmp/passes.txt`

```text
root@kali:~# ridenum 192.168.1.236 500 50000 /tmp/passes.txt
[*] Attempting lsaquery first...This will enumerate the base domain SID
[*] Successfully enumerated base domain SID.. Moving on to extract via RID
[*] Enumerating user accounts.. This could take a little while.
```

### `ridenum（示例）`

官方给出的调用示例：`ridenum -h`

```text
root@kali:~# ridenum -h
.______       __   _______         _______ .__   __.  __    __  .___  ___.
|   _  \     |  | |       \       |   ____||  \ |  | |  |  |  | |   \/   |
|  |_)  |    |  | |  .--.  |      |  |__   |   \|  | |  |  |  | |  \  /  |
|      /     |  | |  |  |  |      |   __|  |  . `  | |  |  |  | |  |\/|  |
|  |\  \----.|  | |  '--'  |      |  |____ |  |\   | |  `--'  | |  |  |  |
| _| `._____||__| |_______/  _____|_______||__| \__|  \______/  |__|  |__|
                            |______|
Written by: David Kennedy (ReL1K)
Company: https://www.trustedsec.com
Twitter: @TrustedSec
Twitter: @HackingDave
Rid Enum is a RID cycling attack that attempts to enumerate user accounts through
null sessions and the SID to RID enum. If you specify a password file, it will
automatically attempt to brute force the user accounts when its finished enumerating.
- RIDENUM is open source and uses all standard python libraries minus python-pexpect. -
You can also specify an already dumped username file, it needs to be in the DOMAINNAME\\USERNAME
format.
Example: ./ridenum.py 192.168.1.50 500 50000 /root/dict.txt /root/user.txt
Usage: ./ridenum.py <server_ip> <start_rid> <end_rid> <optional_username> <optional_password> <optional_password_file> <optional_username_filename>
Updated on: 2025-Dec-09
 Edit this page
rephrase
rifiuti
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install ridenum`，再执行 `ridenum --version` 2>/dev/null || `ridenum -V`
- [ ] **2.** **读官方帮助** —— `ridenum -h`，需要细节时 `man ridenum`
- [ ] **3.** **在自有靶场跑最小用例** —— 官方给出的调用形式是：`Usage: ./ridenum.py <server_ip> <start_rid> <end_rid> <optional_username> <optional_password> <optional_password_file> <optional_username_filename>`
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/ridenum/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/ridenum/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/ridenum/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
