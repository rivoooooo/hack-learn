# cloud-enum

> Multi-cloud open source intelligence tool cloud_enum enumerates public resources matching user requested keywords in public clouds: Amazon Web Services: Open S3 Buckets Protected S3 Buckets

> **功能分类**：通用工具 ｜ **Kali 包**：`cloud-enum` ｜ **官方文档**：<https://www.kali.org/tools/cloud-enum/>

## 1. 安装

```bash
sudo apt update
sudo apt install cloud-enum
```

| 项目 | 内容 |
|------|------|
| 版本 | 0.8 |
| 架构 | all |
| 可执行命令 | `cloud-enum`、`cloud_enum` |
| 安装体积 | 91 KB |
| 官网 | <https://github.com/initstring/cloud_enum> |
| 源码仓库 | <https://salsa.debian.org/pkg-security-team/cloud-enum> |
| 包追踪 | <https://pkg.kali.org/pkg/cloud-enum> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
cloud-enum -h          # 查看用法
man cloud-enum         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 2 个可执行命令，下面是官方页面内嵌的帮助原文。

### `cloud_enum`

官方给出的调用示例：`cloud_enum -h`

```text
root@kali:~# cloud_enum -h
usage: cloud_enum [-h] (-k KEYWORD | -kf KEYFILE) [-m MUTATIONS] [-b BRUTE]
                  [-t THREADS] [-ns NAMESERVER] [-nsf NAMESERVERFILE]
                  [-l LOGFILE] [-f FORMAT] [--disable-aws] [--disable-azure]
                  [--disable-gcp] [-qs]
Multi-cloud enumeration utility. All hail OSINT!
options:
  -h, --help            show this help message and exit
  -k, --keyword KEYWORD
                        Keyword. Can use argument multiple times.
  -kf, --keyfile KEYFILE
                        Input file with a single keyword per line.
  -m, --mutations MUTATIONS
                        Mutations. Default: /usr/lib/cloud-
                        enum/enum_tools/fuzz.txt
  -b, --brute BRUTE     List to brute-force Azure container names. Default:
                        /usr/lib/cloud-enum/enum_tools/fuzz.txt
  -t, --threads THREADS
                        Threads for HTTP brute-force. Default = 5
  -ns, --nameserver NAMESERVER
                        DNS server to use in brute-force.
  -nsf, --nameserverfile NAMESERVERFILE
                        Path to the file containing nameserver IPs
  -l, --logfile LOGFILE
                        Appends found items to specified file.
  -f, --format FORMAT   Format for log file (text,json,csv) - default: text
  --disable-aws         Disable Amazon checks.
  --disable-azure       Disable Azure checks.
  --disable-gcp         Disable Google checks.
  -qs, --quickscan      Disable all mutations and second-level scans
Learn more with
OffSec
Want to learn more about cloud-enum? get access to in-depth training and hands-on labs:
PEN-200: 25.2.3. Enumerating AWS Cloud Infrastructure: Service-specific Domains
Offensive Cloud Foundations: 1.2.3. Public Cloud Reconnaissance - External Probing: Service-specific Domains
PEN-200 course
Updated on: 2026-Aug-25
 Edit this page
clamav
cmseek
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install cloud-enum`，再执行 `cloud-enum --version` 2>/dev/null || `cloud-enum -V`
- [ ] **2.** **读官方帮助** —— `cloud-enum -h`，需要细节时 `man cloud-enum`
- [ ] **3.** **在自有靶场跑最小用例** —— 用 `cloud-enum -h` 里最简单的那个子命令试一次
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/cloud-enum/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/cloud-enum/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/cloud-enum/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
