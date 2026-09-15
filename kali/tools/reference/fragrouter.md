# fragrouter

> IDS evasion toolkit Fragrouter is a network intrusion detection evasion toolkit.

> **功能分类**：信息搜集 ｜ **Kali 包**：`fragrouter` ｜ **官方文档**：<https://www.kali.org/tools/fragrouter/>

## 1. 安装

```bash
sudo apt update
sudo apt install fragrouter
```

| 项目 | 内容 |
|------|------|
| 版本 | 1.7 |
| 架构 | any |
| 可执行命令 | `fragrouter` |
| 依赖 | `libc6`、`libpcap0.8t64` |
| 安装体积 | 72 KB |
| 官网 | <http://www.anzen.com/research/nidsbench/fragrouter.html> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/fragrouter> |
| 包追踪 | <https://pkg.kali.org/pkg/fragrouter> |

## 2. 官方用法示例

> 以下为 Kali 官方工具页给出的示例与输出原文。

```text
Usage Example
Using interface eth0 (-i eth0), send ordered 8-byte IP fragments (-F1):
root@kali:~# fragrouter -i eth0 -F1
fragrouter: frag-1: ordered 8-byte IP fragments
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `fragrouter`

> 官方示例调用：`fragrouter -i eth0 -F1`

```text
root@kali:~# fragrouter -i eth0 -F1
fragrouter: frag-1: ordered 8-byte IP fragments
```

### `fragrouter --help`

> 官方示例调用：`fragrouter --help`

```text
root@kali:~# fragrouter --help
fragrouter: invalid option -- '-'
Version 1.6
Usage: fragrouter [-i interface] [-p] [-g hop] [-G hopcount] ATTACK
 where ATTACK is one of the following:
 -B1: base-1: normal IP forwarding
 -F1: frag-1: ordered 8-byte IP fragments
 -F2: frag-2: ordered 24-byte IP fragments
 -F3: frag-3: ordered 8-byte IP fragments, one out of order
 -F4: frag-4: ordered 8-byte IP fragments, one duplicate
 -F5: frag-5: out of order 8-byte fragments, one duplicate
 -F6: frag-6: ordered 8-byte fragments, marked last frag first
 -F7: frag-7: ordered 16-byte fragments, fwd-overwriting
 -T1: tcp-1:  3-whs, bad TCP checksum FIN/RST, ordered 1-byte segments
 -T3: tcp-3:  3-whs, ordered 1-byte segments, one duplicate
 -T4: tcp-4:  3-whs, ordered 1-byte segments, one overwriting
 -T5: tcp-5:  3-whs, ordered 2-byte segments, fwd-overwriting
 -T7: tcp-7:  3-whs, ordered 1-byte segments, interleaved null segments
 -T8: tcp-8:  3-whs, ordered 1-byte segments, one out of order
 -T9: tcp-9:  3-whs, out of order 1-byte segments
 -C2: tcbc-2: 3-whs, ordered 1-byte segments, interleaved SYNs
 -C3: tcbc-3: ordered 1-byte null segments, 3-whs, ordered 1-byte segments
 -R1: tcbt-1: 3-whs, RST, 3-whs, ordered 1-byte segments
 -I2: ins-2:  3-whs, ordered 1-byte segments, bad TCP checksums
 -I3: ins-3:  3-whs, ordered 1-byte segments, no ACK set
 -M1: misc-1: Windows NT 4 SP2 - http://www.dataprotect.com/ntfrag/
 -M2: misc-2: Linux IP chains - http://www.dataprotect.com/ipchains/
Updated on: 2026-Mar-02
 Edit this page
firefox-developer-edition-kbx
gitxray
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install fragrouter`，再执行 `fragrouter --version` 2>/dev/null || `fragrouter -V`
- [ ] **2.** **读官方帮助** —— `fragrouter -h`，需要细节时 `man fragrouter`
- [ ] **3.** **在自有靶场跑最小用例** —— 官方给出的调用形式是：`Usage: fragrouter [-i interface] [-p] [-g hop] [-G hopcount] ATTACK`
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/fragrouter/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/defense-evasion.md`](../../tools/by-attack/defense-evasion.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/fragrouter/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/fragrouter/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
