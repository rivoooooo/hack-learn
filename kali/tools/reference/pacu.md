# pacu

> Open Source AWS Exploitation Framework This package contains an open-source AWS exploitation framework, designed for offensive security testing against cloud environments. Created and maintained by Rhino Security Labs, Pacu allows penetrat…

> **功能分类**：通用工具 ｜ **Kali 包**：`pacu` ｜ **官方文档**：<https://www.kali.org/tools/pacu/>

## 1. 安装

```bash
sudo apt update
sudo apt install pacu
```

| 项目 | 内容 |
|------|------|
| 版本 | 1.7.0 |
| 架构 | all |
| 可执行命令 | `pacu` |
| 依赖 | `awscli`、`python3`、`python3-boto3`、`python3-botocore`、`python3-colorama`、`python3-dsnap`、`python3-freezegun`、`python3-jq`、`python3-policyuniverse`、`python3-pycognito`、`python3-qrcode`、`python3-requests` 等 |
| 安装体积 | 13.38 MB |
| 官网 | <https://rhinosecuritylabs.com/aws/pacu-open-source-aws-exploitation-framework/> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/pacu> |
| 包追踪 | <https://pkg.kali.org/pkg/pacu> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
pacu -h          # 查看用法
man pacu         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `pacu`

官方给出的调用示例：`pacu -h`

```text
root@kali:~# pacu -h
usage: pacu [-h] [--session ] [--activate-session] [--new-session ]
            [--set-keys ] [--import-keys ] [--module-name ] [--data ]
            [--module-args ] [--list-modules] [--pacu-help] [--module-info]
            [--exec] [--set-regions  [ ...]] [--whoami] [--version] [-q]
options:
  -h, --help            show this help message and exit
  --session             <session name>
  --activate-session    activate session, use session arg to set session name
  --new-session         <session name>
  --set-keys            alias, access id, secret key, token
  --import-keys         AWS profile name to import keys from
  --module-name         <module name>
  --data                <service name/all>
  --module-args         <--module-args='--regions us-east-1,us-east-1'>
  --list-modules        List arguments
  --pacu-help           List the Pacu help window
  --module-info         Get information on a specific module, use --module-
                        name
  --exec                exec module
  --set-regions  [ ...]
                        <region1 region2 ...> or <all> for all
  --whoami              Display information on current IAM user
  --version             Display Pacu version
  -q, --quiet           Do not print the banner on startup
Learn more with
OffSec
Want to learn more about pacu? get access to in-depth training and hands-on labs:
PEN-200: 25. Enumerating AWS Cloud Infrastructure
PEN-200 course
Updated on: 2026-Aug-25
 Edit this page
openvpn
padbuster
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install pacu`，再执行 `pacu --version` 2>/dev/null || `pacu -V`
- [ ] **2.** **读官方帮助** —— `pacu -h`，需要细节时 `man pacu`
- [ ] **3.** **在自有靶场跑最小用例** —— 用 `pacu -h` 里最简单的那个子命令试一次
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/pacu/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/pacu/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/pacu/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
