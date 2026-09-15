# cloudbrute

> Awesome cloud enumerator (program) This package contains a tool to find a company (target) infrastructure, files, and apps on the top cloud providers (Amazon, Google, Microsoft, DigitalOcean, Alibaba, Vultr, Linode). The outcome is useful …

> **功能分类**：通用工具 ｜ **Kali 包**：`cloudbrute` ｜ **官方文档**：<https://www.kali.org/tools/cloudbrute/>

## 1. 安装

```bash
sudo apt update
sudo apt install cloudbrute
```

| 项目 | 内容 |
|------|------|
| 版本 | 1.0.7 |
| 架构 | any |
| 可执行命令 | `cloudbrute` |
| 依赖 | `libc6` |
| 安装体积 | 6.15 MB |
| 官网 | <https://github.com/0xsha/cloudbrute> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/cloudbrute> |
| 包追踪 | <https://pkg.kali.org/pkg/cloudbrute> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
cloudbrute -h          # 查看用法
man cloudbrute         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `cloudbrute`

> 官方示例调用：`cloudbrute -h`

```text
root@kali:~# cloudbrute -h
usage: CloudBrute [-h|--help] -d|--domain "<value>" -k|--keyword "<value>"
                  -w|--wordlist "<value>" [-c|--cloud "<value>"] [-t|--threads
                  <integer>] [-T|--timeout <integer>] [-p|--proxy "<value>"]
                  [-a|--randomagent "<value>"] [-D|--debug] [-q|--quite]
                  [-m|--mode "<value>"] [-o|--output "<value>"]
                  [-C|--configFolder "<value>"]
                  Awesome Cloud Enumerator
Arguments:
  -h  --help          Print help information
  -d  --domain        domain
  -k  --keyword       keyword used to generator urls
  -w  --wordlist      path to wordlist
  -c  --cloud         force a search, check config.yaml providers list
  -t  --threads       number of threads. Default: 80
  -T  --timeout       timeout per request in seconds. Default: 10
  -p  --proxy         use proxy list
  -a  --randomagent   user agent randomization
  -D  --debug         show debug logs. Default: false
  -q  --quite         suppress all output. Default: false
  -m  --mode          storage or app. Default: storage
  -o  --output        Output file. Default: out.txt
  -C  --configFolder  Config path. Default: /etc/cloudbrute/config
Learn more with
OffSec
Want to learn more about cloudbrute? get access to in-depth training and hands-on labs:
PEN-200: 25.2.3. Enumerating AWS Cloud Infrastructure: Service-specific Domains
Offensive Cloud Foundations: 1.2.3. Public Cloud Reconnaissance - External Probing: Service-specific Domains
PEN-200 course
Updated on: 2025-Dec-09
 Edit this page
cisco7crack
cmospwd
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install cloudbrute`，再执行 `cloudbrute --version` 2>/dev/null || `cloudbrute -V`
- [ ] **2.** **读官方帮助** —— `cloudbrute -h`，需要细节时 `man cloudbrute`
- [ ] **3.** **在自有靶场跑最小用例** —— 用 `cloudbrute -h` 里最简单的那个子命令试一次
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/cloudbrute/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/cloudbrute/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/cloudbrute/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
