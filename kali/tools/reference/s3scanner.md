# s3scanner

> Tool to find open S3 buckets and dump their contents This package contains a tool to find open S3 buckets and dump their contents. The features are: zap Multi-threaded scanning telescope Supports tons of S3-compatible APIs female_detective…

> **功能分类**：通用工具 ｜ **Kali 包**：`s3scanner` ｜ **官方文档**：<https://www.kali.org/tools/s3scanner/>

## 1. 安装

```bash
sudo apt update
sudo apt install s3scanner
```

| 项目 | 内容 |
|------|------|
| 版本 | 3.0.0 |
| 架构 | any |
| 可执行命令 | `s3scanner` |
| 依赖 | `libc6` |
| 安装体积 | 17.85 MB |
| 官网 | <https://github.com/sa7mon/s3scanner> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/s3scanner> |
| 包追踪 | <https://pkg.kali.org/pkg/s3scanner> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
s3scanner -h          # 查看用法
man s3scanner         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `s3scanner`

官方给出的调用示例：`s3scanner -h`

```text
root@kali:~# s3scanner -h
INPUT: (1 required)
  -bucket        string  Name of bucket to check.
  -bucket-file   string  File of bucket names to check.
  -mq                    Connect to RabbitMQ to get buckets. Requires config file key "mq". Default: "false"
OUTPUT:
  -db       Save results to a Postgres database. Requires config file key "db.uri". Default: "false"
  -json     Print logs to stdout in JSON format instead of human-readable. Default: "false"
OPTIONS:
  -enumerate           Enumerate bucket objects (can be time-consuming). Default: "false"
  -provider    string  Object storage provider: aws, custom, digitalocean, dreamhost, gcp, linode - custom requires config file. Default: "aws"
  -threads     int     Number of threads to scan with. Default: "4"
DEBUG:
  -verbose     Enable verbose logging. Default: "false"
  -version     Print version Default: "false"
If config file is required these locations will be searched for config.yml: "." "/etc/s3scanner/" "$HOME/.s3scanner/"
Updated on: 2025-Dec-09
 Edit this page
ruby-pedump
sakis3g
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install s3scanner`，再执行 `s3scanner --version` 2>/dev/null || `s3scanner -V`
- [ ] **2.** **读官方帮助** —— `s3scanner -h`，需要细节时 `man s3scanner`
- [ ] **3.** **在自有靶场跑最小用例** —— 用 `s3scanner -h` 里最简单的那个子命令试一次
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/s3scanner/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/s3scanner/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/s3scanner/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
