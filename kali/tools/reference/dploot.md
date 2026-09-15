# dploot

> root@kali:~# dploot -h dploot (https://github.com/zblurx/dploot) v3.1.2 by @_zblurx usage: dploot [-h] {backupkey,blob,browser,certificates,credentials,machinecertificates,machinecredentials,machinemasterkeys,machinetriage,machinevaults,ma…

> **功能分类**：Top 10 常用 ｜ **Kali 包**：`dploot` ｜ **官方文档**：<https://www.kali.org/tools/dploot/>

## 1. 安装

```bash
sudo apt update
sudo apt install dploot
```

| 项目 | 内容 |
|------|------|
| 版本 | 3.1.2 |
| 架构 | all |
| 可执行命令 | `python3-dploot`、`dploot` |
| 官网 | <https://github.com/zblurx/dploot> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/dploot> |
| 包追踪 | <https://pkg.kali.org/pkg/dploot> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
python3-dploot -h          # 查看用法
man python3-dploot         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 2 个可执行命令，下面是官方页面内嵌的帮助原文。

### `dploot`

官方给出的调用示例：`dploot -h`

```text
root@kali:~# dploot -h
dploot (https://github.com/zblurx/dploot) v3.1.2 by @_zblurx
usage: dploot [-h]
              {backupkey,blob,browser,certificates,credentials,machinecertificates,machinecredentials,machinemasterkeys,machinetriage,machinevaults,masterkeys,mobaxterm,rdg,sccm,triage,vaults,wam,wifi} ...
DPAPI looting locally remotely in Python
positional arguments:
  {backupkey,blob,browser,certificates,credentials,machinecertificates,machinecredentials,machinemasterkeys,machinetriage,machinevaults,masterkeys,mobaxterm,rdg,sccm,triage,vaults,wam,wifi}
                        Action
    backupkey           Backup Keys from domain controller
    blob                Decrypt DPAPI blob. Can fetch masterkeys on target
    browser             Dump users credentials and cookies saved in browser
                        from local or remote target
    certificates        Dump users certificates from local or remote target
    credentials         Dump users Credential Manager blob from local or
                        remote target
    machinecertificates
                        Dump system certificates from local or remote target
    machinecredentials  Dump system credentials from local or remote target
    machinemasterkeys   Dump system masterkey from local or remote target
    machinetriage       Loot SYSTEM Masterkeys (if not set), SYSTEM
                        credentials, SYSTEM certificates and SYSTEM vaults
                        from local or remote target
    machinevaults       Dump system vaults from local or remote target
    masterkeys          Dump users masterkey from local or remote target
    mobaxterm           Dump Passwords and Credentials from MobaXterm
    rdg                 Dump users saved password information for
                        RDCMan.settings from local or remote target
    sccm                Dump SCCM secrets (NAA, Collection variables, tasks
                        sequences credentials) from local or remote target
    triage              Loot Masterkeys (if not set), credentials, rdg,
                        certificates, browser and vaults from local or remote
                        target
    vaults              Dump users Vaults blob from local or remote target
    wam                 Dump users cached azure tokens from local or remote
                        target
    wifi                Dump wifi profiles from local or remote target
options:
  -h, --help            show this help message and exit
Updated on: 2025-Dec-09
 Edit this page
dotdotpwn
driftnet
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install dploot`，再执行 `python3-dploot --version` 2>/dev/null || `python3-dploot -V`
- [ ] **2.** **读官方帮助** —— `python3-dploot -h`，需要细节时 `man python3-dploot`
- [ ] **3.** **在自有靶场跑最小用例** —— 用 `python3-dploot -h` 里最简单的那个子命令试一次
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/dploot/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/dploot/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/dploot/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
