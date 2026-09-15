# airgeddon

> Multi-use bash script for Linux systems to audit wireless networks airgeddon is a menu driven 3rd party tools wrapper to audit wireless networks with many features.

> **功能分类**：无线攻击 ｜ **Kali 包**：`airgeddon` ｜ **官方文档**：<https://www.kali.org/tools/airgeddon/>

## 1. 安装

```bash
sudo apt update
sudo apt install airgeddon
```

| 项目 | 内容 |
|------|------|
| 版本 | 12.01 |
| 架构 | any |
| 可执行命令 | `airgeddon` |
| 依赖 | `aircrack-ng`、`bash`、`gawk`、`iproute2`、`iw`、`pciutils`、`procps`、`tmux`、`xterm` |
| 安装体积 | 5.07 MB |
| 官网 | <https://github.com/v1s1t0r1sh3r3/airgeddon> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/airgeddon> |
| 包追踪 | <https://pkg.kali.org/pkg/airgeddon> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
airgeddon -h          # 查看用法
man airgeddon         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `airgeddon`

官方给出的调用示例：`airgeddon -h`

```text
root@kali:~# airgeddon -h
*********************************** Welcome ************************************
Welcome to airgeddon script v12.01
                  .__                         .___  .___
           _____  |__|______  ____   ____   __| _/__| _/____   ____
           \__  \ |  \_  __ \/ ___\_/ __ \ / __ |/ __ |/  _ \ /    \
            / __ \|  ||  | \/ /_/  >  ___// /_/ / /_/ (  <_> )   |  \
           (____  /__||__|  \___  / \___  >____ \____ |\____/|___|  /
                \/         /_____/      \/     \/    \/           \/
                             Developed by v1s1t0r
                         .   *       _.---._  *
                                   .'       '.       .
                               _.-~===========~-._          *
                           *  (___________________)     .
                       .     .      \_______/    *
                        *         .  _.---._          .
                              *    .'       '.  .
                               _.-~===========~-._ *
                           .  (___________________)       *
                            *       \_______/        .
                                   *                .
                             *       _.---._              *
                          .        .'       '.       *
                       .       _.-~===========~-._     *
                              (___________________)         .
                       *            \_______/ .
                        *         .  _.---._          .
                              *    .'       '.  .
                               _.-~===========~-._ *
                           .  (___________________)       *
                            *       \_______/        .
                         .   *       _.---._  *
                                   .'       '.       .
                               _.-~===========~-._          *
                           *  (___________________)     .
                       .     .      \_______/    *
                        *         .  _.---._          .
                              *    .'       '.  .
                               _.-~===========~-._ *
                           .  (___________________)       *
                            *       \_______/        .
                                   *                .
                             *       _.---._              *
                          .        .'       '.       *
                       .       _.-~===========~-._     *
                              (___________________)         .
                       *            \_______/ .
                        *         .  _.---._          .
                              *    .'       '.  .
                               _.-~===========~-._ *
                           .  (___________________)       *
                            *       \_______/        .
Learn more with
OffSec
Want to learn more about airgeddon? get access to in-depth training and hands-on labs:
PEN-210: 8.3. Attacking WPS Networks: WPS Attack
PEN-210 course
Updated on: 2026-Aug-25
 Edit this page
aflplusplus
amass
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install airgeddon`，再执行 `airgeddon --version` 2>/dev/null || `airgeddon -V`
- [ ] **2.** **读官方帮助** —— `airgeddon -h`，需要细节时 `man airgeddon`
- [ ] **3.** **在自有靶场跑最小用例** —— 用 `airgeddon -h` 里最简单的那个子命令试一次
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/airgeddon/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/credential-access.md`](../../tools/by-attack/credential-access.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/airgeddon/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/airgeddon/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
