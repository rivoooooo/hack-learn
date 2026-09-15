# rev-proxy-grapher

> Reverse proxy grapher This package contains a useful little tool that will generate a nice graphviz graph illustrating your reverse proxy flow. It takes a manually curated YAML file describing the topology of your network, proxy definition…

> **功能分类**：通用工具 ｜ **Kali 包**：`rev-proxy-grapher` ｜ **官方文档**：<https://www.kali.org/tools/rev-proxy-grapher/>

## 1. 安装

```bash
sudo apt update
sudo apt install rev-proxy-grapher
```

| 项目 | 内容 |
|------|------|
| 版本 | 0~git20180301 |
| 架构 | all |
| 可执行命令 | `rev-proxy-grapher` |
| 依赖 | `python3`、`python3-netaddr`、`python3-nmap`、`python3-pydotplus`、`python3-yaml` |
| 安装体积 | 207 KB |
| 官网 | <https://github.com/mricon/rev-proxy-grapher> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/rev-proxy-grapher> |
| 包追踪 | <https://pkg.kali.org/pkg/rev-proxy-grapher> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
rev-proxy-grapher -h          # 查看用法
man rev-proxy-grapher         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `rev-proxy-grapher`

官方给出的调用示例：`rev-proxy-grapher -h`

```text
root@kali:~# rev-proxy-grapher -h
usage: rev-proxy-grapher [-h] --topology TOPOLOGY [--resolve-dns]
                         [--nmap-xml NMAP_XML [NMAP_XML ...]]
                         [--limit-ext LIMIT_EXT [LIMIT_EXT ...]] [--font FONT]
                         [--fontsize FONTSIZE] [--ranksep RANKSEP] [--out OUT]
                         [--verbose]
Draw a nice graph of your external to internal proxies
options:
  -h, --help            show this help message and exit
  --topology TOPOLOGY   File describing the proxies and the topology of your
                        networks
  --resolve-dns         Attempt to resolve DNS for all IPs (default: False)
  --nmap-xml NMAP_XML [NMAP_XML ...]
                        Get additional node details from these nmap XML scan
                        files (default: ())
  --limit-ext LIMIT_EXT [LIMIT_EXT ...]
                        Only include these source IPs or networks (default:
                        ())
  --font FONT           Font to use in the graph (default: droid sans,dejavu
                        sans,helvetica)
  --fontsize FONTSIZE   Font size to use in the graph (default: 11)
  --ranksep RANKSEP     Node separation between columns (default: 1)
  --out OUT             Write graph into this file, guessing the output format
                        by extension (default: graph.png)
  --verbose             Be more verbose (default: False)
Updated on: 2026-Mar-13
 Edit this page
pompem
shellter
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install rev-proxy-grapher`，再执行 `rev-proxy-grapher --version` 2>/dev/null || `rev-proxy-grapher -V`
- [ ] **2.** **读官方帮助** —— `rev-proxy-grapher -h`，需要细节时 `man rev-proxy-grapher`
- [ ] **3.** **在自有靶场跑最小用例** —— 用 `rev-proxy-grapher -h` 里最简单的那个子命令试一次
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/rev-proxy-grapher/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/rev-proxy-grapher/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/rev-proxy-grapher/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
