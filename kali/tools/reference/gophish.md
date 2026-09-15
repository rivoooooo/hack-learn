# gophish

> Open-Source Phishing Toolkit This package contains an open-source phishing toolkit designed for businesses and penetration testers. It provides the ability to quickly and easily setup and execute phishing engagements and security awareness…

> **功能分类**：通用工具 ｜ **Kali 包**：`gophish` ｜ **官方文档**：<https://www.kali.org/tools/gophish/>

## 1. 安装

```bash
sudo apt update
sudo apt install gophish
```

| 项目 | 内容 |
|------|------|
| 版本 | 0.12.1 |
| 架构 | any |
| 可执行命令 | `gophish`、`gophish-start`、`gophish-stop` |
| 依赖 | `adduser`、`kali-defaults`、`libc6`、`libsqlite3-0`、`sudo` |
| 安装体积 | 57.53 MB |
| 官网 | <https://getgophish.com/> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/gophish> |
| 包追踪 | <https://pkg.kali.org/pkg/gophish> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
gophish -h          # 查看用法
man gophish         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 3 个可执行命令，下面是官方页面内嵌的帮助原文。

### `gophish`

官方给出的调用示例：`gophish -h`

```text
root@kali:~# gophish -h
┏━(Message from Kali developers)
┃
┃ The command gophish is deprecated. Please use gophish-start instead.
┃
┗━
```

### `gophish-start`

官方给出的调用示例：`gophish-start -h`

```text
root@kali:~# gophish-start -h
┏━(Message from Kali developers)
┃
┃ [*] Web UI: https://127.0.0.1:3333
┃ [i] You might need to refresh your browser once it opens
┃
┃  Default credentials:
┃    user: admin
┃    password: kali-gophish
┃
┗━
```

### `gophish-stop`

官方给出的调用示例：`gophish-stop -h`

```text
root@kali:~# gophish-stop -h
┏━(Message from Kali developers)
┃
┃ Service status:
┃   * gophish.service - Gophish service
┃        Loaded: loaded (/usr/lib/systemd/system/gophish.service; 5:185mdisabled; preset: 5:185mdisabled)
┃        Active: inactive (dead)
┃
┃   Sep 14 05:53:29 kali gophish[247770]: time="2026-09-14T05:53:29-04:00" level=info msg="127.0.0.1 - - [14/Sep/2026:05:53:29 -0400] \"GET /login?next=%2F HTTP/2.0\" 200 2564 \"\" \"curl/8.21.0\""
┃   Sep 14 05:53:30 kali gophish[247770]: 2026/09/14 05:53:30 http: TLS handshake error from 127.0.0.1:33112: unexpected EOF
┃   Sep 14 05:53:30 kali gophish[247770]: time="2026-09-14T05:53:30-04:00" level=info msg="127.0.0.1 - - [14/Sep/2026:05:53:30 -0400] \"GET / HTTP/2.0\" 307 51 \"\" \"curl/8.21.0\""
┃   Sep 14 05:53:30 kali gophish[247770]: time="2026-09-14T05:53:30-04:00" level=info msg="127.0.0.1 - - [14/Sep/2026:05:53:30 -0400] \"GET /login?next=%2F HTTP/2.0\" 200 2564 \"\" \"curl/8.21.0\""
┃   Sep 14 05:53:30 kali gophish[247770]: 2026/09/14 05:53:30 http: TLS handshake error from 127.0.0.1:33126: unexpected EOF
┃   Sep 14 05:53:30 kali gophish[247770]: time="2026-09-14T05:53:30-04:00" level=info msg="127.0.0.1 - - [14/Sep/2026:05:53:30 -0400] \"GET / HTTP/2.0\" 307 51 \"\" \"curl/8.21.0\""
┃   Sep 14 05:53:30 kali gophish[247770]: time="2026-09-14T05:53:30-04:00" level=info msg="127.0.0.1 - - [14/Sep/2026:05:53:30 -0400] \"GET /login?next=%2F HTTP/2.0\" 200 2564 \"\" \"curl/8.21.0\""
┃   Sep 14 05:53:30 kali systemd[1]: Stopping gophish.service - Gophish service...
┃   Sep 14 05:53:30 kali systemd[1]: gophish.service: Deactivated successfully.
┃   Sep 14 05:53:30 kali systemd[1]: Stopped gophish.service - Gophish service.
┃
┗━
Updated on: 2026-Aug-25
 Edit this page
gnuradio
goshs
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install gophish`，再执行 `gophish --version` 2>/dev/null || `gophish -V`
- [ ] **2.** **读官方帮助** —— `gophish -h`，需要细节时 `man gophish`
- [ ] **3.** **在自有靶场跑最小用例** —— 用 `gophish -h` 里最简单的那个子命令试一次
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/gophish/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- **精讲教程**（含原理、参数详解、靶场实操与输出解读）：[gophish](../../tools/tutorials/11-社会工程与报告/gophish.md)
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/initial-access.md`](../../tools/by-attack/initial-access.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/gophish/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/gophish/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
