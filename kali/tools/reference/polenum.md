# polenum

> Extracts the password policy from a Windows system polenum is a Python script which uses the Impacket Library from CORE Security Technologies to extract the password policy information from a windows machine. This allows a non-windows (Lin…

> **功能分类**：信息搜集 ｜ **Kali 包**：`polenum` ｜ **官方文档**：<https://www.kali.org/tools/polenum/>

## 1. 安装

```bash
sudo apt update
sudo apt install polenum
```

| 项目 | 内容 |
|------|------|
| 版本 | 1.7 |
| 架构 | all |
| 可执行命令 | `polenum` |
| 依赖 | `python3`、`python3-impacket` |
| 安装体积 | 26 KB |
| 官网 | <https://github.com/Wh1t3Fox/polenum/> |
| 源码仓库 | <https://salsa.debian.org/pkg-security-team/polenum> |
| 包追踪 | <https://pkg.kali.org/pkg/polenum> |

## 2. 官方用法示例

> 以下为 Kali 官方工具页给出的示例与输出原文。

```text
Usage Example
Get the password policy of the system by logging in with the provided username and password (victim:s3cr3t@192.168.1.200) using SMB port 445 (445/SMB):
root@kali:~# polenum victim:s3cr3t@192.168.1.200 '445/SMB'

[+] Attaching to 192.168.1.200 using victim:s3cr3t

    [+] Trying protocol 445/SMB...

[+] Found domain(s):

    [+] WIN7-X86
    [+] Builtin

[+] Password Info for Domain: WIN7-X86

    [+] Minimum password length: None
    [+] Password history length: None
    [+] Maximum password age: Not Set
    [+] Password Complexity Flags: 000000

        [+] Domain Refuse Password Change: 0
        [+] Domain Password Store Cleartext: 0
        [+] Domain Password Lockout Admins: 0
        [+] Domain Password No Clear Change: 0
        [+] Domain Password No Anon Change: 0
        [+] Domain Password Complex: 0

    [+] Minimum password age: None
    [+] Reset Account Lockout Counter: 30 minutes
    [+] Locked Account Duration: 30 minutes
    [+] Account Lockout Threshold: None
    [+] Forced Log off Time: Not Set
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `polenum`

> 官方示例调用：`polenum victim:`

```text
root@kali:~# polenum victim:
[email protected]
 '445/SMB'
[+] Attaching to 192.168.1.200 using victim:s3cr3t
    [+] Trying protocol 445/SMB...
[+] Found domain(s):
    [+] WIN7-X86
    [+] Builtin
[+] Password Info for Domain: WIN7-X86
    [+] Minimum password length: None
    [+] Password history length: None
    [+] Maximum password age: Not Set
    [+] Password Complexity Flags: 000000
        [+] Domain Refuse Password Change: 0
        [+] Domain Password Store Cleartext: 0
        [+] Domain Password Lockout Admins: 0
        [+] Domain Password No Clear Change: 0
        [+] Domain Password No Anon Change: 0
        [+] Domain Password Complex: 0
    [+] Minimum password age: None
    [+] Reset Account Lockout Counter: 30 minutes
    [+] Locked Account Duration: 30 minutes
    [+] Account Lockout Threshold: None
    [+] Forced Log off Time: Not Set
```

### `polenum -h`

> 官方示例调用：`polenum -h`

```text
root@kali:~# polenum -h
usage: polenum [-h] [--username USERNAME] [--password PASSWORD]
               [--domain DOMAIN] [--protocols [PROTOCOLS ...]]
               [enum4linux]
positional arguments:
  enum4linux            username:password@IPaddress
options:
  -h, --help            show this help message and exit
  --username, -u USERNAME
                        The specified username
  --password, -p PASSWORD
                        The password of the user
  --domain, -d DOMAIN   The domain or IP
  --protocols [PROTOCOLS ...]
                        ['139/SMB', '445/SMB']
Updated on: 2025-Dec-09
 Edit this page
pixiewps
poshc2
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install polenum`，再执行 `polenum --version` 2>/dev/null || `polenum -V`
- [ ] **2.** **读官方帮助** —— `polenum -h`，需要细节时 `man polenum`
- [ ] **3.** **在自有靶场跑最小用例** —— 用 `polenum -h` 里最简单的那个子命令试一次
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/polenum/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/polenum/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/polenum/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
