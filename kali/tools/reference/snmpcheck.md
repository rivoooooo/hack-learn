# snmpcheck

> SNMP service enumeration tool Like to snmpwalk, snmpcheck allows you to enumerate the SNMP devices and places the output in a very human readable friendly format. It could be useful for penetration testing or systems monitoring.

> **功能分类**：信息搜集 ｜ **Kali 包**：`snmpcheck` ｜ **官方文档**：<https://www.kali.org/tools/snmpcheck/>

## 1. 安装

```bash
sudo apt update
sudo apt install snmpcheck
```

| 项目 | 内容 |
|------|------|
| 版本 | 1.9 |
| 架构 | all |
| 可执行命令 | `snmpcheck`、`snmp-check` |
| 依赖 | `libnet-snmp-perl`、`libnumber-bytes-human-perl`、`perl`、`ruby`、`ruby-snmp`、`snmp-check` |
| 安装体积 | 46 KB |
| 官网 | <http://www.nothink.org/codes/snmpcheck/index.php> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/snmpcheck> |
| 包追踪 | <https://pkg.kali.org/pkg/snmpcheck> |

## 2. 官方用法示例

> 以下为 Kali 官方工具页给出的示例与输出原文。

```text
Usage Example
Scan the target host (192.168.1.2) using the public SNMP community string (-c public):
root@kali:~# snmp-check 192.168.1.2 -c public
snmp-check v1.9 - SNMP enumerator
Copyright (c) 2005-2015 by Matteo Cantoni (www.nothink.org)

[+] Try to connect to 192.168.1.2:161 using SNMPv1 and community 'public'

[*] System information:

  Host IP address               : 192.168.1.2
  Hostname                      : ...retracted...
  Description                   : ...retracted...
  Contact                       : ...retracted...
  Location                      : ...retracted...
  Uptime snmp                   : -
  Uptime system                 : 3 days, 00:13:51.05
  System date                   : -

[*] Network information:

[...]

[*] Network interfaces:

[...]

[*] Network IP:

[...]

[*] Routing information:

[...]

[*] TCP connections and listening ports:

[...]

[*] Listening UDP ports:

[...]

root@kali:~#
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 2 个可执行命令，下面是官方页面内嵌的帮助原文。

### `snmp-check`

官方给出的调用示例：`snmp-check 192.168.1.2 -c public`

```text
root@kali:~# snmp-check 192.168.1.2 -c public
snmp-check v1.9 - SNMP enumerator
Copyright (c) 2005-2015 by Matteo Cantoni (www.nothink.org)
[+] Try to connect to 192.168.1.2:161 using SNMPv1 and community 'public'
[*] System information:
  Host IP address               : 192.168.1.2
  Hostname                      : ...retracted...
  Description                   : ...retracted...
  Contact                       : ...retracted...
  Location                      : ...retracted...
  Uptime snmp                   : -
  Uptime system                 : 3 days, 00:13:51.05
  System date                   : -
[*] Network information:
[...]
[*] Network interfaces:
[...]
[*] Network IP:
[...]
[*] Routing information:
[...]
[*] TCP connections and listening ports:
[...]
[*] Listening UDP ports:
[...]
```

### ``

```text
root@kali:~#
```

### `snmp-check（示例）`

官方给出的调用示例：`snmp-check -h`

```text
root@kali:~# snmp-check -h
snmp-check v1.9 - SNMP enumerator
Copyright (c) 2005-2015 by Matteo Cantoni (www.nothink.org)
 Usage: snmp-check [OPTIONS] <target IP address>
  -p --port        : SNMP port. Default port is 161;
  -c --community   : SNMP community. Default is public;
  -v --version     : SNMP version (1,2c). Default is 1;
  -w --write       : detect write access (separate action by enumeration);
  -d --disable_tcp : disable TCP connections enumeration!
  -t --timeout     : timeout in seconds. Default is 5;
  -r --retries     : request retries. Default is 1;
  -i --info        : show script version;
  -h --help        : show help menu;
Updated on: 2025-Dec-09
 Edit this page
sniffjoke
spooftooph
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install snmpcheck`，再执行 `snmpcheck --version` 2>/dev/null || `snmpcheck -V`
- [ ] **2.** **读官方帮助** —— `snmpcheck -h`，需要细节时 `man snmpcheck`
- [ ] **3.** **在自有靶场跑最小用例** —— 官方给出的调用形式是：`Usage: snmp-check [OPTIONS] <target IP address>`
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/snmpcheck/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/discovery.md`](../../tools/by-attack/discovery.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/snmpcheck/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/snmpcheck/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
