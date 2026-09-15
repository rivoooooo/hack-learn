# blue-hydra

> Bluetooth device discovery service BlueHydra is a Bluetooth device discovery service built on top of the bluez library. BlueHydra makes use of ubertooth where available and attempts to track both classic and low energy (LE) bluetooth devic…

> **功能分类**：无线攻击 ｜ **Kali 包**：`blue-hydra` ｜ **官方文档**：<https://www.kali.org/tools/blue-hydra/>

## 1. 安装

```bash
sudo apt update
sudo apt install blue-hydra
```

| 项目 | 内容 |
|------|------|
| 版本 | 1.9.21 |
| 架构 | any |
| 可执行命令 | `blue-hydra`、`blue_hydra`、`rfkill-reset`、`test-discovery` |
| 依赖 | `bluez-test-scripts`、`libc6`、`libruby3.3`、`libsqlite3-0`、`python3`、`ruby`、`blue_hydra` |
| 安装体积 | 8.98 MB |
| 官网 | <https://github.com/ZeroChaos-/blue_hydra> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/blue-hydra> |
| 包追踪 | <https://pkg.kali.org/pkg/blue-hydra> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
blue-hydra -h          # 查看用法
man blue-hydra         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 4 个可执行命令，下面是官方页面内嵌的帮助原文。

### `blue_hydra`

官方给出的调用示例：`blue_hydra -h`

```text
root@kali:~# blue_hydra -h
Usage: BlueHydra [options]
    -d, --daemonize                  Suppress output and run in daemon mode
    -z, --demo                       Hide mac addresses in CLI UI
    -p, --pulse                      Send results to hermes
        --pulse-debug                Store results in a file for review
        --no-db                      Keep db in ram only
        --rssi-api                   Open 127.0.0.1:1124 to allow other processes to poll for seen devices and rssi
        --no-info                    For the purposes for fox hunting, don't info scan.  Some info may be missing, but there will be less gaps during tracking
        --mohawk-api                 For the purposes of making a hat to cover a mohawk, shit out the ui as json at /dev/shm/blue_hydra.json
    -v, --version                    Show version and quit
    -h, --help                       Show this message
```

### `rfkill-reset`

官方给出的调用示例：`rfkill-reset --help`

```text
root@kali:~# rfkill-reset --help
rfkill error: rfkill: invalid option -- 'E'
Try 'rfkill --help' for more information.
Unable to automagically fix
```

### `test-discovery`

官方给出的调用示例：`test-discovery -h`

```text
root@kali:~# test-discovery -h
Usage: test-discovery [options]
Options:
  -i DEV_ID, --device=DEV_ID
  -t TIMEOUT, --timeout=TIMEOUT
  -h, --help            show this help message and exit
Updated on: 2026-Aug-25
 Edit this page
bloodyad
bluez
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install blue-hydra`，再执行 `blue-hydra --version` 2>/dev/null || `blue-hydra -V`
- [ ] **2.** **读官方帮助** —— `blue-hydra -h`，需要细节时 `man blue-hydra`
- [ ] **3.** **在自有靶场跑最小用例** —— 官方给出的调用形式是：`Usage: BlueHydra [options]`
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/blue-hydra/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/blue-hydra/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/blue-hydra/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
