# wmi

> DCOM/WMI client implementation This DCOM/WMI client implementation is based on Samba4 sources. It uses RPC/DCOM mechanisms to interact with WMI services on Windows 2000/XP/2003 machines. This package contains the command line client to per…

> **功能分类**：通用工具 ｜ **Kali 包**：`wmi` ｜ **官方文档**：<https://www.kali.org/tools/wmi/>

## 1. 安装

```bash
sudo apt update
sudo apt install wmi-client
```

| 项目 | 内容 |
|------|------|
| 版本 | 1.3.16 |
| 架构 | any |
| 可执行命令 | `wmi-client`、`wmic`、`wmis` |
| 依赖 | `libc6`、`libcrypt1`、`wmic` |
| 安装体积 | 9.12 MB |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/wmi> |
| 包追踪 | <https://pkg.kali.org/pkg/wmi> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
wmi-client -h          # 查看用法
man wmi-client         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 3 个可执行命令，下面是官方页面内嵌的帮助原文。

### `wmic`

> 官方示例调用：`wmic --help`

```text
root@kali:~# wmic --help
Usage: //host query
Example: wmic -U [domain/]adminuser%password //host "select * from Win32_ComputerSystem"
  --namespace=STRING                          WMI namespace, default to
                                              root\cimv2
  --delimiter=STRING                          delimiter to use when querying
                                              multiple values, default to '|'
Help options:
  -?, --help                                  Show this help message
  --usage                                     Display brief usage message
Common samba options:
  -d, --debuglevel=DEBUGLEVEL                 Set debug level
  --debug-stderr                              Send debug output to STDERR
  -s, --configfile=CONFIGFILE                 Use alternative configuration
                                              file
  --option=name=value                         Set smb.conf option from command
                                              line
  -l, --log-basename=LOGFILEBASE              Basename for log/debug files
  --leak-report                               enable talloc leak reporting on
                                              exit
  --leak-report-full                          enable full talloc leak
                                              reporting on exit
Connection options:
  -R, --name-resolve=NAME-RESOLVE-ORDER       Use these name resolution
                                              services only
  -O, --socket-options=SOCKETOPTIONS          socket options to use
  -n, --netbiosname=NETBIOSNAME               Primary netbios name
  -W, --workgroup=WORKGROUP                   Set the workgroup name
  --realm=REALM                               Set the realm name
  -i, --scope=SCOPE                           Use this Netbios scope
  -m, --maxprotocol=MAXPROTOCOL               Set max protocol level
Authentication options:
  -U, --user=[DOMAIN\]USERNAME[%PASSWORD]     Set the network username
  -N, --no-pass                               Don't ask for a password
  --password=STRING                           Password
  -A, --authentication-file=FILE              Get the credentials from a file
  -S, --signing=on|off|required               Set the client signing state
  -P, --machine-pass                          Use stored machine account
                                              password (implies -k)
  --simple-bind-dn=STRING                     DN to use for a simple bind
  -k, --kerberos=STRING                       Use Kerberos
  --use-security-mechanisms=STRING            Restricted list of
                                              authentication mechanisms
                                              available for use with this
                                              authentication
Common samba options:
  -V, --version                               Print version
```

### `wmis`

> 官方示例调用：`wmis --help`

```text
root@kali:~# wmis --help
Usage: //host
Example: wmis -U [domain/]adminuser%password //host
Help options:
  -?, --help                                  Show this help message
  --usage                                     Display brief usage message
Common samba options:
  -d, --debuglevel=DEBUGLEVEL                 Set debug level
  --debug-stderr                              Send debug output to STDERR
  -s, --configfile=CONFIGFILE                 Use alternative configuration
                                              file
  --option=name=value                         Set smb.conf option from command
                                              line
  -l, --log-basename=LOGFILEBASE              Basename for log/debug files
  --leak-report                               enable talloc leak reporting on
                                              exit
  --leak-report-full                          enable full talloc leak
                                              reporting on exit
Connection options:
  -R, --name-resolve=NAME-RESOLVE-ORDER       Use these name resolution
                                              services only
  -O, --socket-options=SOCKETOPTIONS          socket options to use
  -n, --netbiosname=NETBIOSNAME               Primary netbios name
  -W, --workgroup=WORKGROUP                   Set the workgroup name
  --realm=REALM                               Set the realm name
  -i, --scope=SCOPE                           Use this Netbios scope
  -m, --maxprotocol=MAXPROTOCOL               Set max protocol level
Authentication options:
  -U, --user=[DOMAIN\]USERNAME[%PASSWORD]     Set the network username
  -N, --no-pass                               Don't ask for a password
  --password=STRING                           Password
  -A, --authentication-file=FILE              Get the credentials from a file
  -S, --signing=on|off|required               Set the client signing state
  -P, --machine-pass                          Use stored machine account
                                              password (implies -k)
  --simple-bind-dn=STRING                     DN to use for a simple bind
  -k, --kerberos=STRING                       Use Kerberos
  --use-security-mechanisms=STRING            Restricted list of
                                              authentication mechanisms
                                              available for use with this
                                              authentication
Common samba options:
  -V, --version                               Print version
Updated on: 2026-Mar-02
 Edit this page
witnessme
xspy
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install wmi-client`，再执行 `wmi-client --version` 2>/dev/null || `wmi-client -V`
- [ ] **2.** **读官方帮助** —— `wmi-client -h`，需要细节时 `man wmi-client`
- [ ] **3.** **在自有靶场跑最小用例** —— 官方给出的调用形式是：`Usage: //host query`
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/wmi/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/resource-development.md`](../../tools/by-attack/resource-development.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/wmi/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/wmi/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
