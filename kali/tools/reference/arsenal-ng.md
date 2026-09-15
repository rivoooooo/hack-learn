# arsenal-ng

> Go-based command library equipped with 200+ cybersecurity cheat-sheets Inspired by arsenal, rewritten from scratch with a focus on simplicity, speed and developer experience. The classic launcher, evolved. Fast, Go-based command library eq…

> **功能分类**：通用工具 ｜ **Kali 包**：`arsenal-ng` ｜ **官方文档**：<https://www.kali.org/tools/arsenal-ng/>

## 1. 安装

```bash
sudo apt update
sudo apt install arsenal-ng
```

| 项目 | 内容 |
|------|------|
| 版本 | 1.6 |
| 架构 | any |
| 可执行命令 | `arsenal-ng` |
| 依赖 | `libc6` |
| 安装体积 | 5.85 MB |
| 官网 | <https://github.com/halilkirazkaya/arsenal-ng> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/arsenal-ng> |
| 包追踪 | <https://pkg.kali.org/pkg/arsenal-ng> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
arsenal-ng -h          # 查看用法
man arsenal-ng         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `arsenal-ng`

> 官方示例调用：`arsenal-ng -h`

```text
root@kali:~# arsenal-ng -h
 █████╗ ██████╗ ███████╗███████╗███╗   ██╗ █████╗ ██╗      ███╗   ██╗ ██████╗
██╔══██╗██╔══██╗██╔════╝██╔════╝████╗  ██║██╔══██╗██║      ████╗  ██║██╔════╝
███████║██████╔╝███████╗█████╗  ██╔██╗ ██║███████║██║█████╗██╔██╗ ██║██║  ███╗
██╔══██║██╔══██║╚════██║██╔══╝  ██║╚██╗██║██╔══██║██║╚════╝██║╚██╗██║██║   ██║
██║  ██║██║  ██║███████║███████╗██║ ╚████║██║  ██║███████╗ ██║ ╚████║╚██████╔╝
╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚══════╝╚═╝  ╚═══╝╚═╝  ╚═╝╚══════╝ ╚═╝  ╚═══╝ ╚═════╝  v1.6
❯ > Search commands...
  403bypasser  403bypasser - basic scan                 web, security, pentest, bypass, reconnaissance, enumeration, bugbounty
  403bypasser  403bypasser - custom wordlist scan       web, security, pentest, bypass, reconnaissance, enumeration, bugbounty
  403bypasser  403bypasser - deep scan mode             web, security, pentest, bypass, reconnaissance, enumeration, bugbounty
  403bypasser  403bypasser - authenticated scan with... web, security, pentest, bypass, reconnaissance, enumeration, bugbounty
  403bypasser  403bypasser - custom header injection    web, security, pentest, bypass, reconnaissance, enumeration, bugbounty
  403bypasser  403bypasser - proxy integration          web, security, pentest, bypass, reconnaissance, enumeration, bugbounty
  403bypasser  403bypasser - rate limit evasion         web, security, pentest, bypass, reconnaissance, enumeration, bugbounty
  403bypasser  403bypasser - full evasion suite         web, security, pentest, bypass, reconnaissance, enumeration, bugbounty
  ad-miner     AD-miner - generate standard report      active-directory, security, pentest, enumeration, bloodhound, neo4j, windows
  ad-miner     AD-miner - connection to remote neo4j    active-directory, security, pentest, enumeration, bloodhound, neo4j, windows
  ad-miner     AD-miner - resume with cache             active-directory, security, pentest, enumeration, bloodhound, neo4j, windows
 0/2926 │ ↑/↓: nav │ set key=value │ unset key │ variables │ tools │ help │ esc: quit
Updated on: 2026-Aug-25
 Edit this page
arpwatch
atftp
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install arsenal-ng`，再执行 `arsenal-ng --version` 2>/dev/null || `arsenal-ng -V`
- [ ] **2.** **读官方帮助** —— `arsenal-ng -h`，需要细节时 `man arsenal-ng`
- [ ] **3.** **在自有靶场跑最小用例** —— 用 `arsenal-ng -h` 里最简单的那个子命令试一次
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/arsenal-ng/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/services-and-other-tools.md`](../../tools/by-attack/services-and-other-tools.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/arsenal-ng/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/arsenal-ng/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
