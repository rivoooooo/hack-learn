# dradis

> Collaboration tools for penetration testing Dradis is a tool to help you simplify reporting and collaboration. Spend more time testing and less time reporting Ensure consistent quality across your assessments Combine the output of your fav…

> **功能分类**：报告与记录 ｜ **Kali 包**：`dradis` ｜ **官方文档**：<https://www.kali.org/tools/dradis/>

## 1. 安装

```bash
sudo apt update
sudo apt install dradis
```

| 项目 | 内容 |
|------|------|
| 版本 | 5.3.0 |
| 架构 | amd64 |
| 可执行命令 | `dradis`、`dradis-start`、`dradis-stop` |
| 依赖 | `adduser`、`bundler`、`git`、`kali-defaults`、`libc6`、`libgcc-s1`、`libruby3.3`、`libssl3t64`、`libstdc++6`、`lsof`、`nodejs`、`pwgen` 等 |
| 安装体积 | 238.07 MB |
| 官网 | <https://dradis.com/ce/> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/dradis> |
| 包追踪 | <https://pkg.kali.org/pkg/dradis> |

## 2. 官方用法示例

> 以下为 Kali 官方工具页给出的示例与输出原文。

```text
service dradis start

Screenshots
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 3 个可执行命令，下面是官方页面内嵌的帮助原文。

### `dradis`

官方给出的调用示例：`dradis -h`

```text
root@kali:~# dradis -h
┏━(Message from Kali developers)
┃
┃ The command dradis is deprecated. Please use dradis-start instead.
┃
┗━
```

### `dradis-start`

官方给出的调用示例：`dradis-start -h`

```text
root@kali:~# dradis-start -h
┏━(Message from Kali developers)
┃
┃ [*] Web UI: http://127.0.0.1:3000
┃ [i] You might need to refresh your browser once it opens
┃
┗━
```

### `dradis-stop`

官方给出的调用示例：`dradis-stop -h`

```text
root@kali:~# dradis-stop -h
┏━(Message from Kali developers)
┃
┃ Service status:
┃   * dradis.service - Dradis web application
┃        Loaded: loaded (/usr/lib/systemd/system/dradis.service; 5:185mdisabled; preset: 5:185mdisabled)
┃        Active: inactive (dead)
┃
┃   Sep 14 05:33:00 kali bundle[154217]: Completed 200 OK in 21454ms (Views: 21418.0ms | ActiveRecord: 15.4ms (3 queries, 0 cached) | GC: 556.7ms)
┃   Sep 14 05:33:00 kali bundle[154217]: Completed 200 OK in 19318ms (Views: 19316.1ms | ActiveRecord: 0.2ms (1 query, 0 cached) | GC: 417.0ms)
┃   Sep 14 05:33:00 kali bundle[154217]:   Rendered layouts/_plausible.html.erb (Duration: 0.1ms | GC: 0.0ms)
┃   Sep 14 05:33:00 kali bundle[154217]:   Rendered layouts/hera/_noscript.html.erb (Duration: 0.0ms | GC: 0.0ms)
┃   Sep 14 05:33:00 kali bundle[154217]:   Rendered layout layouts/setup.html.erb (Duration: 14237.4ms | GC: 278.9ms)
┃   Sep 14 05:33:00 kali bundle[154217]: Completed 200 OK in 14242ms (Views: 14237.7ms | ActiveRecord: 0.7ms (1 query, 0 cached) | GC: 278.9ms)
┃   Sep 14 05:33:00 kali bundle[154217]: Exiting
┃   Sep 14 05:33:01 kali systemd[1]: dradis.service: Deactivated successfully.
┃   Sep 14 05:33:01 kali systemd[1]: Stopped dradis.service - Dradis web application.
┃   Sep 14 05:33:01 kali systemd[1]: dradis.service: Consumed 42.487s CPU time over 24.973s wall clock time, 767.1M memory peak.
┃
┗━
Updated on: 2026-Aug-25
 Edit this page
dnsx
dvwa
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install dradis`，再执行 `dradis --version` 2>/dev/null || `dradis -V`
- [ ] **2.** **读官方帮助** —— `dradis -h`，需要细节时 `man dradis`
- [ ] **3.** **在自有靶场跑最小用例** —— 用 `dradis -h` 里最简单的那个子命令试一次
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/dradis/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- **精讲教程**（含原理、参数详解、靶场实操与输出解读）：[dradis](../../tools/tutorials/11-社会工程与报告/dradis.md)
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/services-and-other-tools.md`](../../tools/by-attack/services-and-other-tools.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/dradis/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/dradis/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
