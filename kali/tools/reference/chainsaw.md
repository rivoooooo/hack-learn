# chainsaw

> Rapidly search and hunt through Windows forensic artefacts Chainsaw provides a powerful ‘first-response’ capability to quickly identify threats within Windows forensic artefacts such as Event Logs and the MFT files. Chainsaw offers a gener…

> **功能分类**：通用工具 ｜ **Kali 包**：`chainsaw` ｜ **官方文档**：<https://www.kali.org/tools/chainsaw/>

## 1. 安装

```bash
sudo apt update
sudo apt install chainsaw
```

| 项目 | 内容 |
|------|------|
| 版本 | 2.16.5 |
| 架构 | amd64 |
| 可执行命令 | `chainsaw` |
| 依赖 | `libc6`、`libgcc-s1` |
| 安装体积 | 9.84 MB |
| 官网 | <https://github.com/WithSecureLabs/chainsaw> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/chainsaw> |
| 包追踪 | <https://pkg.kali.org/pkg/chainsaw> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
chainsaw -h          # 查看用法
man chainsaw         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `chainsaw`

> 官方示例调用：`chainsaw -h`

```text
root@kali:~# chainsaw -h
Rapidly work with Forensic Artefacts
Usage: chainsaw [OPTIONS] <COMMAND>
Commands:
  dump     Dump artefacts into a different format
  hunt     Hunt through artefacts using detection rules for threat detection
  lint     Lint provided rules to ensure that they load correctly
  search   Search through forensic artefacts for keywords or patterns
  analyse  Perform various analyses on artefacts
  help     Print this message or the help of the given subcommand(s)
Options:
      --no-banner                  Hide Chainsaw's banner
      --num-threads <NUM_THREADS>  Limit the thread number (default: num of CPUs)
  -v...                            Print verbose output
  -h, --help                       Print help
  -V, --version                    Print version
Examples:
    Hunt with Sigma and Chainsaw Rules:
        ./chainsaw hunt evtx_attack_samples/ -s sigma/ --mapping mappings/sigma-event-logs-all.yml -r rules/
    Hunt with Sigma rules and output in JSON:
        ./chainsaw hunt evtx_attack_samples/ -s sigma/ --mapping mappings/sigma-event-logs-all.yml --json
    Search for the case-insensitive word 'mimikatz':
        ./chainsaw search mimikatz -i evtx_attack_samples/
    Search for Powershell Script Block Events (EventID 4014):
        ./chainsaw search -t 'Event.System.EventID: =4104' evtx_attack_samples/
Updated on: 2026-Aug-25
 Edit this page
certipy-ad
chisel
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install chainsaw`，再执行 `chainsaw --version` 2>/dev/null || `chainsaw -V`
- [ ] **2.** **读官方帮助** —— `chainsaw -h`，需要细节时 `man chainsaw`
- [ ] **3.** **在自有靶场跑最小用例** —— 官方给出的调用形式是：`Usage: chainsaw [OPTIONS] <COMMAND>`
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/chainsaw/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/chainsaw/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/chainsaw/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
