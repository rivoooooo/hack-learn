# thc-pptp-bruter

> THC PPTP Brute Force Brute force program against pptp vpn endpoints (tcp port 1723). Fully standalone. Supports latest MSChapV2 authentication. Tested against Windows and Cisco gateways. Exploits a weakness in Microsoft’s anti-brute force …

> **功能分类**：口令攻击 ｜ **Kali 包**：`thc-pptp-bruter` ｜ **官方文档**：<https://www.kali.org/tools/thc-pptp-bruter/>

## 1. 安装

```bash
sudo apt update
sudo apt install thc-pptp-bruter
```

| 项目 | 内容 |
|------|------|
| 版本 | 0.1.4 |
| 架构 | any |
| 可执行命令 | `thc-pptp-bruter` |
| 依赖 | `libc6`、`libssl3t64` |
| 安装体积 | 47 KB |
| 官网 | <http://www.thc.org/releases.php> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/thc-pptp-bruter> |
| 包追踪 | <https://pkg.kali.org/pkg/thc-pptp-bruter> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
thc-pptp-bruter -h          # 查看用法
man thc-pptp-bruter         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `thc-pptp-bruter`

> 官方示例调用：`thc-pptp-bruter -h`

```text
root@kali:~# thc-pptp-bruter -h
thc-pptp-bruter [options] <remote host IP>
  -v        Verbose output / Debug output
  -W        Disable windows hack [default: enabled]
  -u <user> User [default: administrator]
  -w <file> Wordlist file [default: stdin]
  -p <n>    PPTP port [default: 1723]
  -n <n>    Number of parallel tries [default: 5]
  -l <n>    Limit to n passwords / sec [default: 100]
Windows-Hack reuses the LCP connection with the same caller-id. This
gets around MS's anti-brute forcing protection. It's enabled by default.
Updated on: 2026-Mar-02
 Edit this page
sublist3r
thc-ssl-dos
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install thc-pptp-bruter`，再执行 `thc-pptp-bruter --version` 2>/dev/null || `thc-pptp-bruter -V`
- [ ] **2.** **读官方帮助** —— `thc-pptp-bruter -h`，需要细节时 `man thc-pptp-bruter`
- [ ] **3.** **在自有靶场跑最小用例** —— 用 `thc-pptp-bruter -h` 里最简单的那个子命令试一次
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/thc-pptp-bruter/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/credential-access.md`](../../tools/by-attack/credential-access.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/thc-pptp-bruter/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/thc-pptp-bruter/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
