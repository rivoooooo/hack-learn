# ldeep

> In-depth ldap enumeration utility ldeep is an in-depth ldap enumeration utility that can either run against an Active Directory LDAP server or locally on saved files.

> **功能分类**：通用工具 ｜ **Kali 包**：`ldeep` ｜ **官方文档**：<https://www.kali.org/tools/ldeep/>

## 1. 安装

```bash
sudo apt update
sudo apt install ldeep
```

| 项目 | 内容 |
|------|------|
| 版本 | 2.0.3 |
| 架构 | all |
| 可执行命令 | `ldeep` |
| 依赖 | `gcc`、`krb5-config`、`libkrb5-dev`、`python3`、`python3-commandparse`、`python3-cryptography`、`python3-dev`、`python3-dnspython`、`python3-gssapi`、`python3-ldap3-bleeding-edge`、`python3-oscrypto`、`python3-pycryptodome` 等 |
| 安装体积 | 254 KB |
| 官网 | <https://github.com/franc-pentest/ldeep> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/ldeep> |
| 包追踪 | <https://pkg.kali.org/pkg/ldeep> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
ldeep -h          # 查看用法
man ldeep         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `ldeep`

> 官方示例调用：`ldeep -h`

```text
root@kali:~# ldeep -h
usage: ldeep - 2.0.3 [-h] [-o OUTFILE] [--security_desc]
                     {ldap,cache,protections} ...
options:
  -h, --help            show this help message and exit
  -o, --outfile OUTFILE
                        Store the results in a file
  --security_desc       Enable the retrieval of security descriptors in ldeep
                        results
Mode:
  Available modes
  {ldap,cache,protections}
                        Backend engine to retrieve data
Updated on: 2026-Jun-17
 Edit this page
kerberoast
legba
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install ldeep`，再执行 `ldeep --version` 2>/dev/null || `ldeep -V`
- [ ] **2.** **读官方帮助** —— `ldeep -h`，需要细节时 `man ldeep`
- [ ] **3.** **在自有靶场跑最小用例** —— 用 `ldeep -h` 里最简单的那个子命令试一次
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/ldeep/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/discovery.md`](../../tools/by-attack/discovery.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/ldeep/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/ldeep/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
