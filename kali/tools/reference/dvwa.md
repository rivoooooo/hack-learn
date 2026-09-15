# dvwa

> Damn Vulnerable Web Application This package contains a PHP/MySQL web application that is damn vulnerable. Its main goal is to be an aid for security professionals to test their skills and tools in a legal environment, help web developers …

> **功能分类**：通用工具 ｜ **Kali 包**：`dvwa` ｜ **官方文档**：<https://www.kali.org/tools/dvwa/>

## 1. 安装

```bash
sudo apt update
sudo apt install dvwa
```

| 项目 | 内容 |
|------|------|
| 版本 | 2.5 |
| 架构 | all |
| 可执行命令 | `dvwa`、`dvwa-start`、`dvwa-stop` |
| 依赖 | `adduser`、`apache2`、`kali-defaults`、`libapache2-mod-php`、`mariadb-server`、`nginx`、`php8.4`、`php8.4-fpm`、`php8.4-gd`、`php8.4-mysql`、`sudo`、`dvwa-start` |
| 安装体积 | 1.70 MB |
| 官网 | <https://github.com/digininja/DVWA> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/dvwa> |
| 包追踪 | <https://pkg.kali.org/pkg/dvwa> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
dvwa -h          # 查看用法
man dvwa         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 3 个可执行命令，下面是官方页面内嵌的帮助原文。

### `dvwa-start`

> 官方示例调用：`dvwa-start -h`

```text
root@kali:~# dvwa-start -h
┏━(Message from Kali developers)
┃
┃ Please wait for the dvwa service to start
┃
┃ [*] Web UI: http://127.0.0.1:42001
┃ [i] You might need to refresh your browser once it opens
┃
┗━
- Default User    : admin
- Default Password: password
```

### `dvwa-stop`

> 官方示例调用：`dvwa-stop -h`

```text
root@kali:~# dvwa-stop -h
┏━(Message from Kali developers)
┃
┃ Service status:
┃   * dvwa.service - The Damn Vulnerable Web Application in its own nginx server
┃        Loaded: loaded (/usr/lib/systemd/system/dvwa.service; 5:185mdisabled; preset: 5:185mdisabled)
┃        Active: inactive (dead)
┃
┃   Sep 08 08:53:28 kali sudo[863847]: pam_unix(sudo:session): session closed for user root
┃   Sep 08 08:53:28 kali systemd[1]: Started dvwa.service - The Damn Vulnerable Web Application in its own nginx server.
┃   Sep 08 08:53:31 kali systemd[1]: dvwa.service: Deactivated successfully.
┃   Sep 08 08:53:31 kali systemd[1]: dvwa.service: Consumed 1.031s CPU time over 3.096s wall clock time, 14.2M memory peak.
┃   Sep 08 08:53:31 kali systemd[1]: Starting dvwa.service - The Damn Vulnerable Web Application in its own nginx server...
┃   Sep 08 08:53:31 kali systemd[1]: Started dvwa.service - The Damn Vulnerable Web Application in its own nginx server.
┃   Sep 08 08:53:34 kali systemd[1]: dvwa.service: Deactivated successfully.
┃   Sep 08 08:53:34 kali systemd[1]: Starting dvwa.service - The Damn Vulnerable Web Application in its own nginx server...
┃   Sep 08 08:53:34 kali systemd[1]: Started dvwa.service - The Damn Vulnerable Web Application in its own nginx server.
┃   Sep 08 08:53:36 kali systemd[1]: dvwa.service: Deactivated successfully.
┃
┗━
Updated on: 2026-Aug-25
 Edit this page
dradis
eksctl
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install dvwa`，再执行 `dvwa --version` 2>/dev/null || `dvwa -V`
- [ ] **2.** **读官方帮助** —— `dvwa -h`，需要细节时 `man dvwa`
- [ ] **3.** **在自有靶场跑最小用例** —— 用 `dvwa -h` 里最简单的那个子命令试一次
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/dvwa/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- **精讲教程**（含原理、参数详解、靶场实操与输出解读）：[dvwa](../../tools/tutorials/03-Web应用/dvwa.md)
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/services-and-other-tools.md`](../../tools/by-attack/services-and-other-tools.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/dvwa/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/dvwa/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
