# beef-xss

> Browser Exploitation Framework (BeEF) BeEF is short for The Browser Exploitation Framework. It is a penetration testing tool that focuses on the web browser. Amid growing concerns about web-born attacks against clients, including mobile cl…

> **功能分类**：Web 应用 ｜ **Kali 包**：`beef-xss` ｜ **官方文档**：<https://www.kali.org/tools/beef-xss/>

## 1. 安装

```bash
sudo apt update
sudo apt install beef-xss
```

| 项目 | 内容 |
|------|------|
| 版本 | 0.6.0.0 |
| 架构 | any |
| 可执行命令 | `beef-xss`、`beef-xss-start`、`beef-xss-stop` |
| 依赖 | `adduser`、`kali-defaults`、`lsof`、`nodejs`、`ruby`、`rubygems-integration`、`xdg-utils` |
| 安装体积 | 82.72 MB |
| 官网 | <https://beefproject.com/> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/beef-xss> |
| 包追踪 | <https://pkg.kali.org/pkg/beef-xss> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
beef-xss -h          # 查看用法
man beef-xss         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 3 个可执行命令，下面是官方页面内嵌的帮助原文。

### `beef-xss`

```text
root@kali:~# beef-xss
[*] Please wait for the BeEF service to start.
[*]
[*] You might need to refresh your browser once it opens.
[*]
[*]  Web UI: http://127.0.0.1:3000/ui/panel
[*]    Hook: <script src="http://<IP>:3000/hook.js"></script>
[*] Example: <script src="http://127.0.0.1:3000/hook.js"></script>
● beef-xss.service - LSB: BeEF
   Loaded: loaded (/etc/init.d/beef-xss; generated)
   Active: active (running) since Sat 2018-11-24 18:44:53 EST; 5s ago
     Docs: man:systemd-sysv-generator(8)
  Process: 3457 ExecStart=/etc/init.d/beef-xss start (code=exited, status=0/SUCCESS)
    Tasks: 5 (limit: 4665)
   Memory: 151.9M
   CGroup: /system.slice/beef-xss.service
           └─3463 ruby /usr/share/beef-xss/beef
Nov 24 18:44:53 kali systemd[1]: Starting LSB: BeEF...
Nov 24 18:44:53 kali systemd[1]: Started LSB: BeEF.
[*] Opening Web UI (http://127.0.0.1:3000/ui/panel) in: 5... 4... 3... 2... 1...
```

### `beef-xss（示例）`

官方给出的调用示例：`beef-xss -h`

```text
root@kali:~# beef-xss -h
┏━(Message from Kali developers)
┃
┃ The command beef-xss is deprecated. Please use beef-xss-start instead.
┃
┗━
```

### `beef-xss-start`

官方给出的调用示例：`beef-xss-start -h`

```text
root@kali:~# beef-xss-start -h
[-] You are using the Default credentials
[-] (Password must be different from "beef")
[-] Please type a new password for the beef user:
```

### `beef-xss-stop`

官方给出的调用示例：`beef-xss-stop -h`

```text
root@kali:~# beef-xss-stop -h
┏━(Message from Kali developers)
┃
┃ Service status:
┃   * beef-xss.service - beef-xss
┃        Loaded: loaded (/usr/lib/systemd/system/beef-xss.service; 5:185mdisabled; preset: 5:185mdisabled)
┃        Active: inactive (dead)
┃
┗━
Learn more with
OffSec
Want to learn more about beef-xss? get access to in-depth training and hands-on labs:
PEN-200: 13.3.1. Locating Public Exploits: Exploit Frameworks
PEN-200 course
Updated on: 2026-May-25
 Edit this page
atomic-operator
btscanner
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install beef-xss`，再执行 `beef-xss --version` 2>/dev/null || `beef-xss -V`
- [ ] **2.** **读官方帮助** —— `beef-xss -h`，需要细节时 `man beef-xss`
- [ ] **3.** **在自有靶场跑最小用例** —— 用 `beef-xss -h` 里最简单的那个子命令试一次
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/beef-xss/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- **精讲教程**（含原理、参数详解、靶场实操与输出解读）：[beef-xss](../../tools/tutorials/06-漏洞利用/beef-xss.md)
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/execution.md`](../../tools/by-attack/execution.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/beef-xss/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/beef-xss/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
