# quark-engine

> Android Malware (Analysis | Scoring System) Quark-Engine is a full-featured Android analysis framework written in Python for hunting threat intelligence inside the APK, DEX files. Since it is rule-based, you can use the ones built-in or cu…

> **功能分类**：通用工具 ｜ **Kali 包**：`quark-engine` ｜ **官方文档**：<https://www.kali.org/tools/quark-engine/>

## 1. 安装

```bash
sudo apt update
sudo apt install quark-engine
```

| 项目 | 内容 |
|------|------|
| 版本 | 26.5.1 |
| 架构 | amd64 |
| 可执行命令 | `quark-engine`、`freshquark`、`quark` |
| 依赖 | `python3`、`rizin`、`freshquark` |
| 安装体积 | 322.08 MB |
| 官网 | <https://github.com/ev-flow/quark-engine> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/quark-engine> |
| 包追踪 | <https://pkg.kali.org/pkg/quark-engine> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
quark-engine -h          # 查看用法
man quark-engine         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 3 个可执行命令，下面是官方页面内嵌的帮助原文。

### `freshquark`

> 官方示例调用：`freshquark -h`

```text
root@kali:~# freshquark -h
[*] Download the latest rules from https://github.com/quark-engine/quark-rules
[+] DONE: Complete downloading the latest quark-rules.
All the rules are saved in /root/.quark-engine/quark-rules/rules.
To specify one of the rules of Quark-Rule, use /root/.quark-engine/quark-rules/rules/<rule_name>.json as an argument.
```

### `quark`

> 官方示例调用：`quark --help`

```text
root@kali:~# quark --help
    ________                      __
    \_____  \  __ _______ _______|  | __
     /  / \  \|  |  \__  \_  __ \  |/ /
    /   \_/.  \  |  // __ \|  | \/    <
    \_____\ \_/____/(____  /__|  |__|_ \
           \__>          \/           \/ v26.5.1
                An Obfuscation-Neglect Android Malware Scoring System
Usage: quark [OPTIONS]
  Quark is an Obfuscation-Neglect Android Malware Scoring System
Options:
  -s, --summary TEXT              Show summary report. Optionally specify the
                                  name of a rule/label
  -d, --detail TEXT               Show detail report. Optionally specify the
                                  name of a rule/label
  -o, --output FILE               Output report in JSON
  -w, --webreport FILE            Generate web report
  -a, --apk FILE                  APK file  [required]
  -r, --rule PATH                 Rules directory  [default: /root/.quark-
                                  engine/quark-rules/rules]
  -g, --graph [png|json]          Create call graph to call_graph_image
                                  directory
  -c, --classification            Show rules classification
  -t, --threshold [100|80|60|40|20]
                                  Set the lower limit of the confidence
                                  threshold
  -i, --list [all|native|custom]  List classes, methods and descriptors
  -p, --permission                List Android permissions
  -l, --label [max|detailed]      Show report based on label of rules
  -C, --comparison                Behaviors comparison based on max confidence
                                  of rule labels
  --generate-rule DIRECTORY       Generate rules and output to given directory
  --core-library [androguard|rizin|radare2|shuriken]
                                  Specify the core library used to analyze an
                                  APK
  --multi-process INTEGER RANGE   Allow analyzing APK with N processes, where
                                  N doesn't exceeds the number of usable CPUs
                                  - 1 to avoid memory exhaustion.  [x>=1]
  --auto-fix-checksum             Automatically repair damaged DEX
                                  checksum/signature before analyzing
                                  (androguard only).When not provided, Quark
                                  will prompt in interactive TTY and skip in
                                  non-interactive runs.
  --version                       Show the version and exit.
  --help                          Show this message and exit.
Updated on: 2026-Aug-25
 Edit this page
qsreplace
readpe
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install quark-engine`，再执行 `quark-engine --version` 2>/dev/null || `quark-engine -V`
- [ ] **2.** **读官方帮助** —— `quark-engine -h`，需要细节时 `man quark-engine`
- [ ] **3.** **在自有靶场跑最小用例** —— 官方给出的调用形式是：`Usage: quark [OPTIONS]`
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/quark-engine/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/quark-engine/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/quark-engine/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
