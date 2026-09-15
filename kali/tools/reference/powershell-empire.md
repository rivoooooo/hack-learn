# powershell-empire

> PowerShell and Python post-exploitation agent This package contains a post-exploitation framework that includes a pure-PowerShell2.0 Windows agent, and a pure Python Linux/OS X agent. It is the merge of the previous PowerShell Empire and P…

> **功能分类**：通用工具 ｜ **Kali 包**：`powershell-empire` ｜ **官方文档**：<https://www.kali.org/tools/powershell-empire/>

## 1. 安装

```bash
sudo apt update
sudo apt install powershell-empire
```

| 项目 | 内容 |
|------|------|
| 版本 | 6.6.0 |
| 架构 | all |
| 可执行命令 | `powershell-empire`、`starkiller`、`starkiller-start`、`starkiller-stop` |
| 依赖 | `default-mysql-server`、`git`、`kali-defaults`、`pyinstaller`、`python3`、`python3-aiofiles`、`python3-alembic`、`python3-bcrypt`、`python3-cryptography`、`python3-docopt`、`python3-donut`、`python3-dropbox` 等 |
| 安装体积 | 50.34 MB |
| 官网 | <https://github.com/BC-SECURITY/Empire> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/powershell-empire> |
| 包追踪 | <https://pkg.kali.org/pkg/powershell-empire> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
powershell-empire -h          # 查看用法
man powershell-empire         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 4 个可执行命令，下面是官方页面内嵌的帮助原文。

### `powershell-empire`

官方给出的调用示例：`powershell-empire -h`

```text
root@kali:~# powershell-empire -h
usage: empire.py [-h] {server,setup} ...
positional arguments:
  {server,setup}
    server        Launch Empire Server
    setup         Setup the data directories for Empire
options:
  -h, --help      show this help message and exit
```

### `starkiller`

官方给出的调用示例：`starkiller -h`

```text
root@kali:~# starkiller -h
┏━(Message from Kali developers)
┃
┃ The command starkiller is deprecated. Please use starkiller-start instead.
┃
┗━
```

### `starkiller-start`

官方给出的调用示例：`starkiller-start --help`

```text
root@kali:~# starkiller-start --help
┏━(Message from Kali developers)
┃
┃ Please wait for the powershell-empire service to start
┃ ......
┃ [*] Web UI: http://127.0.0.1:1337
┃ [i] You might need to refresh your browser once it opens
┃
┃  Default credentials:
┃    user: empireadmin
┃    password: password123
┃
┗━
```

### `starkiller-stop`

官方给出的调用示例：`starkiller-stop -h`

```text
root@kali:~# starkiller-stop -h
┏━(Message from Kali developers)
┃
┃ Service status:
┃   * powershell-empire.service - Powershell-Empire service
┃        Loaded: loaded (/usr/lib/systemd/system/powershell-empire.service; 5:185mdisabled; preset: 5:185mdisabled)
┃        Active: inactive (dead)
┃
┃   Sep 14 07:29:50 kali powershell-empire[565245]: [INFO]: Shutting down
┃   Sep 14 07:29:50 kali powershell-empire[565245]: [INFO]: Waiting for application shutdown.
┃   Sep 14 07:29:50 kali powershell-empire[565245]: [INFO]: Empire shutting down...
┃   Sep 14 07:29:50 kali powershell-empire[565245]: [INFO]: Shutting down listeners...
┃   Sep 14 07:29:50 kali powershell-empire[565245]: [INFO]: Shutting down plugins...
┃   Sep 14 07:29:50 kali powershell-empire[565245]: [INFO]: Shutting down SocketIO...
┃   Sep 14 07:29:50 kali powershell-empire[565245]: [INFO]: Application shutdown complete.
┃   Sep 14 07:29:50 kali powershell-empire[565245]: [INFO]: Finished server process [565245]
┃   Sep 14 07:29:50 kali systemd[1]: powershell-empire.service: Deactivated successfully.
┃   Sep 14 07:29:50 kali systemd[1]: powershell-empire.service: Consumed 2.321s CPU time over 3.394s wall clock time, 176.3M memory peak.
┃
┗━
Learn more with
OffSec
Want to learn more about powershell-empire? get access to in-depth training and hands-on labs:
Rule Creation and Refinement Skill Path: 3.3.1. Network Detections: C2 Infrastructure
MITRE D3FEND - Detect: 9.3.1. Network Detections: C2 Infrastructure
MITRE ATT&CK - Detect: 4.3.1. Network Detections: C2 Infrastructure
PowerShell Empire
Updated on: 2026-Aug-25
 Edit this page
pocsuite3
procps
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install powershell-empire`，再执行 `powershell-empire --version` 2>/dev/null || `powershell-empire -V`
- [ ] **2.** **读官方帮助** —— `powershell-empire -h`，需要细节时 `man powershell-empire`
- [ ] **3.** **在自有靶场跑最小用例** —— 用 `powershell-empire -h` 里最简单的那个子命令试一次
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/powershell-empire/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- **精讲教程**（含原理、参数详解、靶场实操与输出解读）：[powershell-empire](../../tools/tutorials/08-后渗透/powershell-empire.md)
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/command-and-control.md`](../../tools/by-attack/command-and-control.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/powershell-empire/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/powershell-empire/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
