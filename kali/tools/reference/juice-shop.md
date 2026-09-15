# juice-shop

> Insecure web application This package contains a modern and sophisticated insecure web application! It can be used in security trainings, awareness demos, CTFs and as a guinea pig for security tools! Juice Shop encompasses vulnerabilities …

> **功能分类**：通用工具 ｜ **Kali 包**：`juice-shop` ｜ **官方文档**：<https://www.kali.org/tools/juice-shop/>

## 1. 安装

```bash
sudo apt update
sudo apt install juice-shop
```

| 项目 | 内容 |
|------|------|
| 版本 | 19.1.1 |
| 架构 | amd64 |
| 可执行命令 | `juice-shop`、`juice-shop-start`、`juice-shop-stop` |
| 依赖 | `adduser`、`kali-defaults`、`libc6`、`libgcc-s1`、`libnode137`、`libstdc++6`、`lsof`、`npm`、`xdg-utils` |
| 安装体积 | 1.04 GB |
| 官网 | <https://github.com/juice-shop/juice-shop> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/juice-shop> |
| 包追踪 | <https://pkg.kali.org/pkg/juice-shop> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
juice-shop -h          # 查看用法
man juice-shop         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 3 个可执行命令，下面是官方页面内嵌的帮助原文。

### `juice-shop`

> 官方示例调用：`juice-shop -h`

```text
root@kali:~# juice-shop -h
┏━(Message from Kali developers)
┃
┃ The command juice-shop is deprecated. Please use juice-shop-start instead.
┃
┗━
```

### `juice-shop-start`

> 官方示例调用：`juice-shop-start -h`

```text
root@kali:~# juice-shop-start -h
┏━(Message from Kali developers)
┃
┃ Service status:
┃   * juice-shop.service - juice-shop web application
┃        Loaded: loaded (/usr/lib/systemd/system/juice-shop.service; 5:185mdisabled; preset: 5:185mdisabled)
┃        Active: active (running) since Tue 2026-09-08 08:53:45 EDT; 5s ago
┃    Invocation: 313913404f044809842b1c05ddacfbb4
┃      Main PID: 864797 (npm start)
┃         Tasks: 235:245m (limit: 9443)
┃        Memory: 299.4M (peak: 318.4M)
┃           CPU: 2.374s
┃        CGroup: /system.slice/juice-shop.service
┃                |-5:245m864797 "npm start"
┃                |-5:245m864818 sh -c "node build/app"
┃                `-5:245m864819 node build/app
┃
┃   Sep 08 08:53:46 kali npm[864819]: info: Required file server.js is present (OK)
┃   Sep 08 08:53:46 kali npm[864819]: info: Required file index.html is present (OK)
┃   Sep 08 08:53:46 kali npm[864819]: info: Required file styles.css is present (OK)
┃   Sep 08 08:53:46 kali npm[864819]: info: Required file main.js is present (OK)
┃   Sep 08 08:53:46 kali npm[864819]: info: Required file vendor.js is present (OK)
┃   Sep 08 08:53:46 kali npm[864819]: info: Required file tutorial.js is present (OK)
┃   Sep 08 08:53:46 kali npm[864819]: info: Required file runtime.js is present (OK)
┃   Sep 08 08:53:46 kali npm[864819]: info: Port 42000 is available (OK)
┃   Sep 08 08:53:46 kali npm[864819]: info: Chatbot training data botDefaultTrainingData.json validated (OK)
┃   Sep 08 08:53:46 kali npm[864819]: info: Domain https://www.alchemy.com/ is reachable (OK)
┃
┗━
```

### `juice-shop-stop`

> 官方示例调用：`juice-shop-stop -h`

```text
root@kali:~# juice-shop-stop -h
┏━(Message from Kali developers)
┃
┃ Service status:
┃   * juice-shop.service - juice-shop web application
┃        Loaded: loaded (/usr/lib/systemd/system/juice-shop.service; 5:185mdisabled; preset: 5:185mdisabled)
┃        Active: inactive (dead)
┃
┃   Sep 08 08:53:46 kali npm[864819]: info: Required file vendor.js is present (OK)
┃   Sep 08 08:53:46 kali npm[864819]: info: Required file tutorial.js is present (OK)
┃   Sep 08 08:53:46 kali npm[864819]: info: Required file runtime.js is present (OK)
┃   Sep 08 08:53:46 kali npm[864819]: info: Port 42000 is available (OK)
┃   Sep 08 08:53:46 kali npm[864819]: info: Chatbot training data botDefaultTrainingData.json validated (OK)
┃   Sep 08 08:53:46 kali npm[864819]: info: Domain https://www.alchemy.com/ is reachable (OK)
┃   Sep 08 08:53:51 kali systemd[1]: Stopping juice-shop.service - juice-shop web application...
┃   Sep 08 08:53:51 kali systemd[1]: juice-shop.service: Deactivated successfully.
┃   Sep 08 08:53:51 kali systemd[1]: Stopped juice-shop.service - juice-shop web application.
┃   Sep 08 08:53:51 kali systemd[1]: juice-shop.service: Consumed 2.577s CPU time over 6.308s wall clock time, 318.4M memory peak.
┃
┗━
Updated on: 2026-Aug-25
 Edit this page
jsql
kali-defaults
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install juice-shop`，再执行 `juice-shop --version` 2>/dev/null || `juice-shop -V`
- [ ] **2.** **读官方帮助** —— `juice-shop -h`，需要细节时 `man juice-shop`
- [ ] **3.** **在自有靶场跑最小用例** —— 用 `juice-shop -h` 里最简单的那个子命令试一次
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/juice-shop/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/services-and-other-tools.md`](../../tools/by-attack/services-and-other-tools.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/juice-shop/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/juice-shop/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
