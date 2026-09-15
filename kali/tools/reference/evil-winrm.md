# evil-winrm

> Ultimate WinRM shell for hacking/pentesting This package contains the ultimate WinRM shell for hacking/pentesting. WinRM (Windows Remote Management) is the Microsoft implementation of WS-Management Protocol. A standard SOAP based protocol …

> **功能分类**：通用工具 ｜ **Kali 包**：`evil-winrm` ｜ **官方文档**：<https://www.kali.org/tools/evil-winrm/>

## 1. 安装

```bash
sudo apt update
sudo apt install evil-winrm
```

| 项目 | 内容 |
|------|------|
| 版本 | 4.1 |
| 架构 | all |
| 可执行命令 | `evil-winrm` |
| 依赖 | `ruby`、`ruby-benchmark`、`ruby-csv`、`ruby-fileutils`、`ruby-logger`、`ruby-stringio`、`ruby-syslog`、`ruby-winrm`、`ruby-winrm-fs` |
| 安装体积 | 176 KB |
| 官网 | <https://github.com/Hackplayers/evil-winrm> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/evil-winrm> |
| 包追踪 | <https://pkg.kali.org/pkg/evil-winrm> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
evil-winrm -h          # 查看用法
man evil-winrm         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `evil-winrm`

> 官方示例调用：`evil-winrm -h`

```text
root@kali:~# evil-winrm -h
Evil-WinRM shell v4.1
Usage: evil-winrm -i IP -u USER [-s SCRIPTS_PATH] [-e EXES_PATH] [-P PORT] [-a USERAGENT] [-p PASS] [-H HASH] [-U URL] [-S] [-c PUBLIC_KEY_PATH ] [-k PRIVATE_KEY_PATH ] [-r REALM] [-K TICKET_FILE] [--spn SPN_PREFIX] [-l]
    -S, --ssl                        Enable ssl
    -c, --pub-key PUBLIC_KEY_PATH    Local path to public key certificate
    -k, --priv-key PRIVATE_KEY_PATH  Local path to private key certificate
    -r, --realm DOMAIN               Kerberos auth, it has to be set also in /etc/krb5.conf file using this format -> CONTOSO.COM = { kdc = fooserver.contoso.com }
    -s, --scripts PS_SCRIPTS_PATH    Powershell scripts local path
        --spn SPN_PREFIX             SPN prefix for Kerberos auth (default HTTP)
    -K, --ccache TICKET_FILE         Path to Kerberos ticket file (ccache or kirbi format, auto-detected)
    -e, --executables EXES_PATH      C# executables local path
    -i, --ip IP                      Remote host IP or hostname. FQDN for Kerberos auth (required)
    -U, --url URL                    Remote url endpoint (default /wsman)
    -u, --user USER                  Username (required if not using kerberos)
    -p, --password PASS              Password
    -H, --hash HASH                  NTHash
    -P, --port PORT                  Remote host port (default 5985)
    -a, --user-agent USERAGENT       Specify connection user-agent (default Microsoft WinRM Client)
    -V, --version                    Show version
    -n, --no-colors                  Disable colors
    -N, --no-rpath-completion        Disable remote path completion
    -l, --log                        Log the WinRM session
    -h, --help                       Display this help message
Learn more with
OffSec
Want to learn more about evil-winrm? get access to in-depth training and hands-on labs:
PEN-200: 17.1.4. Windows Privilege Escalation: Information Goldmine PowerShell
SOC-200: 5. Windows Client-Side Attacks
PEN-200 course
SOC-200 course
Updated on: 2026-Aug-25
 Edit this page
ethtool
exiv2
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install evil-winrm`，再执行 `evil-winrm --version` 2>/dev/null || `evil-winrm -V`
- [ ] **2.** **读官方帮助** —— `evil-winrm -h`，需要细节时 `man evil-winrm`
- [ ] **3.** **在自有靶场跑最小用例** —— 官方给出的调用形式是：`Usage: evil-winrm -i IP -u USER [-s SCRIPTS_PATH] [-e EXES_PATH] [-P PORT] [-a USERAGENT] [-p PASS] [-H HASH] [-U URL] [-S] [-c PUBLIC_KEY_PATH ] [-k PRIVATE_KEY_PATH ] [-r REALM] [-K TICKET_FILE] [--spn SPN_PREFIX] [-l]`
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/evil-winrm/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- **精讲教程**（含原理、参数详解、靶场实操与输出解读）：[evil-winrm](../../tools/tutorials/08-后渗透/evil-winrm.md)
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/defense-evasion.md`](../../tools/by-attack/defense-evasion.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/evil-winrm/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/evil-winrm/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
