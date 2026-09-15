# gvm

> Remote network security auditor - metapackage and useful scripts The Greenbone Vulnerability Manager is a modular security auditing tool, used for testing remote systems for vulnerabilities that should be fixed. This package installs all t…

> **功能分类**：漏洞分析 ｜ **Kali 包**：`gvm` ｜ **官方文档**：<https://www.kali.org/tools/gvm/>

## 1. 安装

```bash
sudo apt update
sudo apt install gvm
```

| 项目 | 内容 |
|------|------|
| 版本 | 25.04.3 |
| 架构 | all |
| 可执行命令 | `gvm`、`gvm-check-setup`、`gvm-setup`、`gvm-start`、`gvm-stop` |
| 依赖 | `gsad`、`gvmd`、`notus-scanner`、`openvas-scanner`、`ospd-openvas`、`psmisc`、`rsync`、`xsltproc`、`gvm-check-setup` |
| 安装体积 | 48 KB |
| 官网 | <https://www.greenbone.net/> |
| 源码仓库 | <https://salsa.debian.org/pkg-security-team/gvm> |
| 包追踪 | <https://pkg.kali.org/pkg/gvm> |

## 2. 官方用法示例

> 以下为 Kali 官方工具页给出的示例与输出原文。

```text
Screenshots
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 5 个可执行命令，下面是官方页面内嵌的帮助原文。

### `gvm-check-setup`

> 官方示例调用：`gvm-check-setup -h`

```text
root@kali:~# gvm-check-setup -h
gvm-check-setup 25.04.0
 This script is provided and maintained by Debian and Kali.
  Test completeness and readiness of GVM-25.04.0
Step 1: Checking OpenVAS (Scanner)...
        OK: OpenVAS Scanner is present in version 23.45.1.
        OK: Notus Scanner is present in version 22.7.2.
        ERROR: No CA certificate file for Server found.
        FIX: Run 'sudo runuser -u _gvm -- gvm-manage-certs -a -f'.
 ERROR: Your GVM-25.04.0 installation is not yet complete!
Please follow the instructions marked with FIX above and run this
script again.
 IMPORTANT NOTE: this script is provided and maintained by Debian and Kali.
 If you find any issue in this script, please report it directly to Debian or Kali
```

### `gvm-setup`

> 官方示例调用：`gvm-setup -h`

```text
root@kali:~# gvm-setup -h
This script is provided and maintained by Debian and Kali.
 If you find any issue in this script, please report it directly to Debian or Kali
[>] Starting PostgreSQL service
[>] Creating GVM's certificate files
[>] Creating PostgreSQL database
[i] User _gvm already exists in PostgreSQL
[*] Creating database
[*] Creating permissions
[*] Applying permissions
[*] Creating extension uuid-ossp
[*] Creating extension pgcrypto
[*] Creating extension pg-gvm
[>] Migrating database
[>] Checking for GVM admin user
[*] Creating user admin for gvm
[*] Please note the generated admin password
[*]
[*] Configure Feed Import Owner
[*] Define Feed Import Owner
[*] Update GVM feeds
Running as root. Switching to user '_gvm' and group '_gvm'.
Trying to acquire lock on /var/lib/openvas/feed-update.lock
Acquired lock on /var/lib/openvas/feed-update.lock
```

### `gvm-start`

> 官方示例调用：`gvm-start -h`

```text
root@kali:~# gvm-start -h
[>] Please wait for the GVM services to start.
[>]
[>] You might need to refresh your browser once it opens.
[>]
[>]  Web UI (Greenbone Security Assistant): https://127.0.0.1:9392
```

### `gvm-stop`

> 官方示例调用：`gvm-stop -h`

```text
root@kali:~# gvm-stop -h
[>] Stopping GVM services
* gsad.service - Greenbone Security Assistant daemon (gsad)
     Loaded: loaded (/usr/lib/systemd/system/gsad.service; disabled; preset: disabled)
     Active: inactive (dead)
       Docs: man:gsad(8)
             https://www.greenbone.net
* gvmd.service - Greenbone Vulnerability Manager daemon (gvmd)
     Loaded: loaded (/usr/lib/systemd/system/gvmd.service; disabled; preset: disabled)
     Active: inactive (dead)
       Docs: man:gvmd(8)
Sep 14 05:56:10 kali systemd[1]: Starting gvmd.service - Greenbone Vulnerability Manager daemon (gvmd)...
Sep 14 05:56:10 kali systemd[1]: gvmd.service: Can't open PID file '/run/gvmd/gvmd.pid' (yet?) after start: No such file or directory
Sep 14 05:56:24 kali systemd[1]: gvmd.service: Deactivated successfully.
Sep 14 05:56:24 kali systemd[1]: Stopped gvmd.service - Greenbone Vulnerability Manager daemon (gvmd).
* ospd-openvas.service - OSPd Wrapper for the OpenVAS Scanner (ospd-openvas)
     Loaded: loaded (/usr/lib/systemd/system/ospd-openvas.service; disabled; preset: disabled)
     Active: inactive (dead)
       Docs: man:ospd-openvas(8)
             man:openvas(8)
Sep 14 05:56:09 kali systemd[1]: Starting ospd-openvas.service - OSPd Wrapper for the OpenVAS Scanner (ospd-openvas)...
Sep 14 05:56:10 kali systemd[1]: Started ospd-openvas.service - OSPd Wrapper for the OpenVAS Scanner (ospd-openvas).
Sep 14 05:56:24 kali systemd[1]: Stopping ospd-openvas.service - OSPd Wrapper for the OpenVAS Scanner (ospd-openvas)...
Sep 14 05:56:25 kali systemd[1]: ospd-openvas.service: Deactivated successfully.
Sep 14 05:56:25 kali systemd[1]: Stopped ospd-openvas.service - OSPd Wrapper for the OpenVAS Scanner (ospd-openvas).
Sep 14 05:56:25 kali systemd[1]: ospd-openvas.service: Consumed 1.723s CPU time over 15.525s wall clock time, 113.6M memory peak.
* notus-scanner.service - Notus Scanner
     Loaded: loaded (/usr/lib/systemd/system/notus-scanner.service; disabled; preset: disabled)
     Active: inactive (dead)
       Docs: https://github.com/greenbone/notus-scanner
Sep 14 05:56:09 kali systemd[1]: Starting notus-scanner.service - Notus Scanner...
Sep 14 05:56:09 kali systemd[1]: Started notus-scanner.service - Notus Scanner.
Sep 14 05:56:09 kali notus-scanner[260386]: 2026-09-14 05:56:09,947 notus-scanner: INFO: (notus.scanner.daemon) Starting notus-scanner version 22.7.2.
Sep 14 05:56:24 kali systemd[1]: Stopping notus-scanner.service - Notus Scanner...
Sep 14 05:56:24 kali systemd[1]: notus-scanner.service: Deactivated successfully.
Sep 14 05:56:24 kali systemd[1]: Stopped notus-scanner.service - Notus Scanner.
Learn more with
OffSec
Want to learn more about gvm? get access to in-depth training and hands-on labs:
Introduction to Vulnerability Tracking: 2.2. Scanning a Server for Vulnerabilities
Updated on: 2026-Aug-25
 Edit this page
gsocket
hcxtools
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install gvm`，再执行 `gvm --version` 2>/dev/null || `gvm -V`
- [ ] **2.** **读官方帮助** —— `gvm -h`，需要细节时 `man gvm`
- [ ] **3.** **在自有靶场跑最小用例** —— 用 `gvm -h` 里最简单的那个子命令试一次
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/gvm/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/reconnaissance.md`](../../tools/by-attack/reconnaissance.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/gvm/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/gvm/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
