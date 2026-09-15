# spray

> Password Spraying tool for Active Directory Credentials This package contains a Password Spraying tool for Active Directory Credentials. The script will password spray a target over a period of time. It requires password policy as input so…

> **功能分类**：通用工具 ｜ **Kali 包**：`spray` ｜ **官方文档**：<https://www.kali.org/tools/spray/>

## 1. 安装

```bash
sudo apt update
sudo apt install spray
```

| 项目 | 内容 |
|------|------|
| 版本 | 2.1 |
| 架构 | all |
| 可执行命令 | `spray` |
| 依赖 | `curl`、`smbclient` |
| 安装体积 | 39.01 MB |
| 官网 | <https://github.com/Greenwolf/Spray> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/spray> |
| 包追踪 | <https://pkg.kali.org/pkg/spray> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
spray -h          # 查看用法
man spray         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `spray`

> 官方示例调用：`spray -h`

```text
root@kali:~# spray -h
Spray 2.1 the Password Sprayer by Jacob Wilkin(Greenwolf)
This script will password spray a target over a period of time
It requires password policy as input so accounts are not locked out
Usage: spray -smb <targetIP> <usernameList> <passwordList> <AttemptsPerLockoutPeriod> <LockoutPeriodInMinutes> <Domain>
Example: spray -smb 192.168.0.1 users.txt passwords.txt 1 35 CORPORATION
To password spray an OWA portal, a file must be created of the POST request with Username:
[email protected]
, and Password: spraypassword
Usage: spray -owa <targetIP> <usernameList> <passwordList> <AttemptsPerLockoutPeriod> <LockoutPeriodInMinutes> <RequestFile>
Example: spray -owa 192.168.0.1 usernames.txt passwords.txt 1 35 post-request.txt
To password spray an lync service, a lync autodiscover url or a url that returns the www-authenticate header must be provided along with a list of email addresses
Usage: spray -lync <lyncDiscoverOrAutodiscoverUrl> <emailAddressList> <passwordList> <AttemptsPerLockoutPeriod> <LockoutPeriodInMinutes>
Example: spray -lync https://lyncdiscover.company.com/ emails.txt passwords.txt 1 35\n
Example: spray -lync https://lyncweb.company.com/Autodiscover/AutodiscoverService.svc/root/oauth/user emails.txt passwords.txt 1 35
To password spray an CISCO Web VPN a target portal or server hosting a portal must be provided
Usage: spray -cisco <targetURL> <usernameList> <passwordList> <AttemptsPerLockoutPeriod> <LockoutPeriodInMinutes>
Example: spray -cicso 192.168.0.1 usernames.txt passwords.txt 1 35
It is also possible to update the supplied 2016/2017 password list to the current year
Usage: spray -passupdate <passwordList>
Example: spray -passupdate passwords.txt
An optional company name can also be provided to add to the list:
Usage: spray -passupdate <passwordList> <CompanyName>
Example: spray -passupdate passwords.txt Company
A username list can also be generated from a list of common names:
Usage: spray -genusers <firstnames> <lastnames> "<<fi><li><fn><ln>>"
Example: spray -genusers english-first-1000.txt english-last-1000.txt "<fi><ln>"
Example: spray -genusers english-first-1000.txt english-last-1000.txt "<fn>.<ln>"
Updated on: 2025-Dec-09
 Edit this page
spooftooph
sprayingtoolkit
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install spray`，再执行 `spray --version` 2>/dev/null || `spray -V`
- [ ] **2.** **读官方帮助** —— `spray -h`，需要细节时 `man spray`
- [ ] **3.** **在自有靶场跑最小用例** —— 官方给出的调用形式是：`Usage: spray -smb <targetIP> <usernameList> <passwordList> <AttemptsPerLockoutPeriod> <LockoutPeriodInMinutes> <Domain>`
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/spray/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/spray/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/spray/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
