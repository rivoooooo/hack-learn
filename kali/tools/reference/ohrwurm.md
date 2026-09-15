# ohrwurm

> RTP fuzzer ohrwurm is a small and simple RTP fuzzer that has been successfully tested on a small number of SIP phones. Features: - reads SIP messages to get information of the RTP port numbers

> **功能分类**：漏洞分析 ｜ **Kali 包**：`ohrwurm` ｜ **官方文档**：<https://www.kali.org/tools/ohrwurm/>

## 1. 安装

```bash
sudo apt update
sudo apt install ohrwurm
```

| 项目 | 内容 |
|------|------|
| 版本 | 0.1 |
| 架构 | any |
| 可执行命令 | `ohrwurm` |
| 依赖 | `dsniff`、`libc6`、`libpcap0.8t64` |
| 安装体积 | 33 KB |
| 官网 | <http://mazzoo.de/blog/2006/08/25#ohrwurm> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/ohrwurm> |
| 包追踪 | <https://pkg.kali.org/pkg/ohrwurm> |

## 2. 官方用法示例

> 以下为 Kali 官方工具页给出的示例与输出原文。

```text
Usage Example
Fuzz two hosts (-a 192.168.1.123 -b 192.168.1.15), both on port 6970 (-A 6970 -B 6970), through interface eth0 (-i eth0):
root@kali:~# ohrwurm -a 192.168.1.123 -b 192.168.1.15 -A 6970 -B 6970 -i eth0
ohrwurm-0.1
using random seed 2978455466
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `ohrwurm`

> 官方示例调用：`ohrwurm -a 192.168.1.123 -b 192.168.1.15 -A 6970 -B 6970 -i eth0`

```text
root@kali:~# ohrwurm -a 192.168.1.123 -b 192.168.1.15 -A 6970 -B 6970 -i eth0
ohrwurm-0.1
using random seed 2978455466
```

### `ohrwurm -h`

> 官方示例调用：`ohrwurm -h`

```text
root@kali:~# ohrwurm -h
ohrwurm-0.1
usage: ohrwurm -a <IP target a> -b <IP target b> [-s <randomseed>] [-e <bit error ratio in %>] [-i <interface>] [-A <RTP port a> -B <RTP port b>]
	-a <IPv4 address A in dot-decimal notation> SIP phone A
	-b <IPv4 address B in dot-decimal notation> SIP phone B
	-s <integer> randomseed (default: read from /dev/urandom)
	-e <double> bit error ratio in % (default: 1.230000)
	-i <interfacename> network interface (default: eth0)
	-t suppress RTCP packets (default: dont suppress)
	-A <port number> of RTP port on IP a (requires -B)
	-B <port number> of RTP port on IP b (requires -A)
	   note: using -A and -B skips SIP sniffing, any RTP can be fuzzed
Updated on: 2025-Dec-09
 Edit this page
odat
onesixtyone
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install ohrwurm`，再执行 `ohrwurm --version` 2>/dev/null || `ohrwurm -V`
- [ ] **2.** **读官方帮助** —— `ohrwurm -h`，需要细节时 `man ohrwurm`
- [ ] **3.** **在自有靶场跑最小用例** —— 用 `ohrwurm -h` 里最简单的那个子命令试一次
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/ohrwurm/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/discovery.md`](../../tools/by-attack/discovery.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/ohrwurm/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/ohrwurm/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
