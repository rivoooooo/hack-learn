# mssqlpwner

> Advanced and versatile pentesting tool MSSqlPwner is an advanced and versatile pentesting tool designed to seamlessly interact and pwn MSSQL servers. That tool is based on impacket, which allows attackers to authenticate to databases using…

> **功能分类**：通用工具 ｜ **Kali 包**：`mssqlpwner` ｜ **官方文档**：<https://www.kali.org/tools/mssqlpwner/>

## 1. 安装

```bash
sudo apt update
sudo apt install mssqlpwner
```

| 项目 | 内容 |
|------|------|
| 版本 | 1.3.2 |
| 架构 | all |
| 可执行命令 | `mssqlpwner` |
| 依赖 | `python3`、`python3-impacket`、`python3-prompt-toolkit`、`python3-termcolor` |
| 安装体积 | 238 KB |
| 官网 | <https://github.com/ScorpionesLabs/MSSqlPwner> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/mssqlpwner> |
| 包追踪 | <https://pkg.kali.org/pkg/mssqlpwner> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
mssqlpwner -h          # 查看用法
man mssqlpwner         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `mssqlpwner`

> 官方示例调用：`mssqlpwner -h`

```text
root@kali:~# mssqlpwner -h
usage: mssqlpwner [-h] [-port PORT] [-timeout TIMEOUT] [-db DB]
                  [-windows-auth] [-no-state] [-debug] [-hashes LMHASH:NTHASH]
                  [-no-pass] [-k] [-aesKey hex key] [-dc-ip ip address]
                  [-link-name LINK_NAME] [-max-link-depth MAX_LINK_DEPTH]
                  [-max-impersonation-depth MAX_IMPERSONATION_DEPTH]
                  [-chain-id CHAIN_ID] [-auto-yes]
                  target
                  {enumerate,set-chain,rev2self,get-rev2self-queries,get-chain-list,get-link-server-list,get-adsi-provider-list,set-link-server,exec,ntlm-relay,custom-asm,inject-custom-asm,direct-query,retrieve-password,interactive,brute} ...
TDS client implementation (SSL supported).
positional arguments:
  target                [[domain/]username[:password]@]<targetName or address>
Options:
  -h, --help            show this help message and exit
  -port PORT            target MSSQL port (default 1433)
  -timeout TIMEOUT      timeout in seconds (default 30)
  -db DB                MSSQL database instance (default None)
  -windows-auth         whether or not to use Windows Authentication (default
                        False)
  -no-state             whether or not to load existing state
  -debug                Turn DEBUG output ON
authentication:
  -hashes LMHASH:NTHASH
                        NTLM hashes, format is LMHASH:NTHASH
  -no-pass              don't ask for password (useful for -k)
  -k                    Use Kerberos authentication. Grabs credentials from
                        ccache file (KRB5CCNAME) based on target parameters.
                        If valid credentials cannot be found, it will use the
                        ones specified in the command line
  -aesKey hex key       AES key to use for Kerberos Authentication (128 or 256
                        bits)
  -dc-ip ip address     IP Address of the domain controller. If ommited it use
                        the domain part (FQDN) specified in the target
                        parameter
Choose module:
  -link-name LINK_NAME  Linked server to launch queries
  -max-link-depth MAX_LINK_DEPTH
                        Maximum links you want to depth recursively
  -max-impersonation-depth MAX_IMPERSONATION_DEPTH
                        Maximum impersonation you want to depth in each link
  -chain-id CHAIN_ID    Chain ID to use
  -auto-yes             Auto answer yes to all questions
Modules:
  {enumerate,set-chain,rev2self,get-rev2self-queries,get-chain-list,get-link-server-list,get-adsi-provider-list,set-link-server,exec,ntlm-relay,custom-asm,inject-custom-asm,direct-query,retrieve-password,interactive,brute}
    enumerate           Enumerate MSSQL server
    set-chain           Set chain ID (For interactive-mode only!)
    rev2self            Revert to SELF (For interactive-mode only!)
    get-rev2self-queries
                        Retrieve queries to revert to SELF (For interactive-
                        mode only!)
    get-chain-list      Get chain list
    get-link-server-list
                        Get linked server list
    get-adsi-provider-list
                        Get ADSI provider list
    set-link-server     Set link server (For interactive-mode only!)
    exec                Command to execute
    ntlm-relay          Steal NetNTLM hash / Relay attack
    custom-asm          Execute procedures using custom assembly
    inject-custom-asm   Code injection using custom assembly
    direct-query        Execute direct query
    retrieve-password   Retrieve password from ADSI servers
    interactive         Interactive Mode
    brute               Brute force
usage: mssqlpwner [-h] [-port PORT] [-timeout TIMEOUT] [-db DB]
                  [-windows-auth] [-no-state] [-debug] [-hashes LMHASH:NTHASH]
                  [-no-pass] [-k] [-aesKey hex key] [-dc-ip ip address]
                  [-link-name LINK_NAME] [-max-link-depth MAX_LINK_DEPTH]
                  [-max-impersonation-depth MAX_IMPERSONATION_DEPTH]
                  [-chain-id CHAIN_ID] [-auto-yes]
                  target
                  {enumerate,set-chain,rev2self,get-rev2self-queries,get-chain-list,get-link-server-list,get-adsi-provider-list,set-link-server,exec,ntlm-relay,custom-asm,inject-custom-asm,direct-query,retrieve-password,interactive,brute} ...
TDS client implementation (SSL supported).
positional arguments:
  target                [[domain/]username[:password]@]<targetName or address>
Options:
  -h, --help            show this help message and exit
  -port PORT            target MSSQL port (default 1433)
  -timeout TIMEOUT      timeout in seconds (default 30)
  -db DB                MSSQL database instance (default None)
  -windows-auth         whether or not to use Windows Authentication (default
                        False)
  -no-state             whether or not to load existing state
  -debug                Turn DEBUG output ON
authentication:
  -hashes LMHASH:NTHASH
                        NTLM hashes, format is LMHASH:NTHASH
  -no-pass              don't ask for password (useful for -k)
  -k                    Use Kerberos authentication. Grabs credentials from
                        ccache file (KRB5CCNAME) based on target parameters.
                        If valid credentials cannot be found, it will use the
                        ones specified in the command line
  -aesKey hex key       AES key to use for Kerberos Authentication (128 or 256
                        bits)
  -dc-ip ip address     IP Address of the domain controller. If ommited it use
                        the domain part (FQDN) specified in the target
                        parameter
Choose module:
  -link-name LINK_NAME  Linked server to launch queries
  -max-link-depth MAX_LINK_DEPTH
                        Maximum links you want to depth recursively
  -max-impersonation-depth MAX_IMPERSONATION_DEPTH
                        Maximum impersonation you want to depth in each link
  -chain-id CHAIN_ID    Chain ID to use
  -auto-yes             Auto answer yes to all questions
Modules:
  {enumerate,set-chain,rev2self,get-rev2self-queries,get-chain-list,get-link-server-list,get-adsi-provider-list,set-link-server,exec,ntlm-relay,custom-asm,inject-custom-asm,direct-query,retrieve-password,interactive,brute}
    enumerate           Enumerate MSSQL server
    set-chain           Set chain ID (For interactive-mode only!)
    rev2self            Revert to SELF (For interactive-mode only!)
    get-rev2self-queries
                        Retrieve queries to revert to SELF (For interactive-
                        mode only!)
    get-chain-list      Get chain list
    get-link-server-list
                        Get linked server list
    get-adsi-provider-list
                        Get ADSI provider list
    set-link-server     Set link server (For interactive-mode only!)
    exec                Command to execute
    ntlm-relay          Steal NetNTLM hash / Relay attack
    custom-asm          Execute procedures using custom assembly
    inject-custom-asm   Code injection using custom assembly
    direct-query        Execute direct query
    retrieve-password   Retrieve password from ADSI servers
    interactive         Interactive Mode
    brute               Brute force
Updated on: 2026-Aug-25
 Edit this page
mitmproxy
multiforcer
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install mssqlpwner`，再执行 `mssqlpwner --version` 2>/dev/null || `mssqlpwner -V`
- [ ] **2.** **读官方帮助** —— `mssqlpwner -h`，需要细节时 `man mssqlpwner`
- [ ] **3.** **在自有靶场跑最小用例** —— 用 `mssqlpwner -h` 里最简单的那个子命令试一次
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/mssqlpwner/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/mssqlpwner/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/mssqlpwner/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
