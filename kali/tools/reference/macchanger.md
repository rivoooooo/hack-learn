# macchanger

> Utility for manipulating the MAC address of network interfaces GNU MAC Changer is an utility that makes the maniputation of MAC addresses of network interfaces easier. MAC addresses are unique identifiers on networks, they only need to be …

> **功能分类**：无线攻击 ｜ **Kali 包**：`macchanger` ｜ **官方文档**：<https://www.kali.org/tools/macchanger/>

## 1. 安装

```bash
sudo apt update
sudo apt install macchanger
```

| 项目 | 内容 |
|------|------|
| 版本 | 1.7.0 |
| 架构 | linux-any |
| 可执行命令 | `macchanger` |
| 安装体积 | 641 KB |
| 官网 | <https://github.com/alobbs/macchanger> |
| 源码仓库 | <https://salsa.debian.org/debian/macchanger> |
| 包追踪 | <https://pkg.kali.org/pkg/macchanger> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
macchanger -h          # 查看用法
man macchanger         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `macchanger`

> 官方示例调用：`macchanger -h`

```text
root@kali:~# macchanger -h
GNU MAC Changer
Usage: macchanger [options] device
  -h,  --help                   Print this help
  -V,  --version                Print version and exit
  -s,  --show                   Print the MAC address and exit
  -e,  --ending                 Don't change the vendor bytes
  -a,  --another                Set random vendor MAC of the same kind
  -A                            Set random vendor MAC of any kind
  -p,  --permanent              Reset to original, permanent hardware MAC
  -r,  --random                 Set fully random MAC
  -l,  --list[=keyword]         Print known vendors
  -b,  --bia                    Pretend to be a burned-in-address
  -m,  --mac=XX:XX:XX:XX:XX:XX
       --mac XX:XX:XX:XX:XX:XX  Set the MAC XX:XX:XX:XX:XX:XX
Report bugs to https://github.com/alobbs/macchanger/issues
Updated on: 2025-Dec-09
 Edit this page
lynis
maryam
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install macchanger`，再执行 `macchanger --version` 2>/dev/null || `macchanger -V`
- [ ] **2.** **读官方帮助** —— `macchanger -h`，需要细节时 `man macchanger`
- [ ] **3.** **在自有靶场跑最小用例** —— 官方给出的调用形式是：`Usage: macchanger [options] device`
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/macchanger/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- **精讲教程**（含原理、参数详解、靶场实操与输出解读）：[macchanger](../../tools/tutorials/07-嗅探与欺骗/macchanger.md)
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/defense-evasion.md`](../../tools/by-attack/defense-evasion.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/macchanger/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/macchanger/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
