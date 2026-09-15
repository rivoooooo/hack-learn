# vlan

> Ifupdown legacy integration for vlan configuration This package contains legacy integration scripts for configuring vlan interfaces via ifupdown (/etc/network/interfaces). For further details see vlan-interfaces(5) man page in this package…

> **功能分类**：通用工具 ｜ **Kali 包**：`vlan` ｜ **官方文档**：<https://www.kali.org/tools/vlan/>

## 1. 安装

```bash
sudo apt update
sudo apt install vlan
```

| 项目 | 内容 |
|------|------|
| 版本 | 2.0.5 |
| 架构 | all |
| 可执行命令 | `vlan`、`vconfig` |
| 依赖 | `iproute2`、`vconfig` |
| 安装体积 | 37 KB |
| 源码仓库 | <https://salsa.debian.org/debian/vlan> |
| 包追踪 | <https://pkg.kali.org/pkg/vlan> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
vlan -h          # 查看用法
man vlan         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 2 个可执行命令，下面是官方页面内嵌的帮助原文。

### `vconfig`

官方给出的调用示例：`vconfig -h`

```text
root@kali:~# vconfig -h
Usage: add             [interface-name] [vlan_id]
       rem             [vlan-name]
       set_flag        [interface-name] [flag-num]       [0 | 1]
       set_egress_map  [vlan-name]      [skb_priority]   [vlan_qos]
       set_ingress_map [vlan-name]      [skb_priority]   [vlan_qos]
       set_name_type   [name-type]
* The [interface-name] is the name of the ethernet card that hosts
  the VLAN you are talking about.
* The vlan_id is the identifier (0-4095) of the VLAN you are operating on.
* skb_priority is the priority in the socket buffer (sk_buff).
* vlan_qos is the 3 bit priority in the VLAN header
* name-type:  VLAN_PLUS_VID (vlan0005), VLAN_PLUS_VID_NO_PAD (vlan5),
              DEV_PLUS_VID (eth0.0005), DEV_PLUS_VID_NO_PAD (eth0.5)
* FLAGS:  1 REORDER_HDR  When this is set, the VLAN device will move the
            ethernet header around to make it look exactly like a real
            ethernet device.  This may help programs such as DHCPd which
            read the raw ethernet packet and make assumptions about the
            location of bytes.  If you don't need it, don't turn it on, because
            there will be at least a small performance degradation.  Default
            is OFF.
Updated on: 2025-Dec-09
 Edit this page
villain
voiphopper
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install vlan`，再执行 `vlan --version` 2>/dev/null || `vlan -V`
- [ ] **2.** **读官方帮助** —— `vlan -h`，需要细节时 `man vlan`
- [ ] **3.** **在自有靶场跑最小用例** —— 官方给出的调用形式是：`Usage: add             [interface-name] [vlan_id]`
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/vlan/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/vlan/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/vlan/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
