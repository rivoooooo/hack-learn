# redfang

> Locates non-discoverable bluetooth devices fang is a small proof-of-concept application to find non discoveredable bluetooth devices. This is done by brute forcing the last six (6) bytes of the bluetooth address of the device and doing a r…

> **功能分类**：无线攻击 ｜ **Kali 包**：`redfang` ｜ **官方文档**：<https://www.kali.org/tools/redfang/>

## 1. 安装

```bash
sudo apt update
sudo apt install redfang
```

| 项目 | 内容 |
|------|------|
| 版本 | 2.5 |
| 架构 | any |
| 可执行命令 | `redfang`、`fang` |
| 依赖 | `libbluetooth3`、`libc6`、`fang` |
| 安装体积 | 40 KB |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/redfang> |
| 包追踪 | <https://pkg.kali.org/pkg/redfang> |

## 2. 官方用法示例

> 以下为 Kali 官方工具页给出的示例与输出原文。

```text
Usage Example
Scan the given range (-r 00803789EE76-00803789EEff) and discover Bluetooth devices (-s):
root@kali:~# fang -r 00803789EE76-00803789EEff -s
redfang - the bluetooth hunter ver 2.5
(c)2003 @stake Inc
author:   Ollie Whitehouse <ollie@atstake.com>
enhanced: threads by Simon Halsall <s.halsall@eris.qinetiq.com>
enhanced: device info discovery by Stephen Kapp <skapp@atstake.com>
Scanning 138 address(es)
Address range 00:80:37:89:ee:76 -> 00:80:37:89:ee:ff
Performing Bluetooth Discovery...
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 2 个可执行命令，下面是官方页面内嵌的帮助原文。

### `fang`

官方给出的调用示例：`fang -r 00803789EE76-00803789EEff -s`

```text
root@kali:~# fang -r 00803789EE76-00803789EEff -s
redfang - the bluetooth hunter ver 2.5
(c)2003 @stake Inc
author:   Ollie Whitehouse <
[email protected]
>
enhanced: threads by Simon Halsall <
[email protected]
>
enhanced: device info discovery by Stephen Kapp <
[email protected]
>
Scanning 138 address(es)
Address range 00:80:37:89:ee:76 -> 00:80:37:89:ee:ff
Performing Bluetooth Discovery...
```

### `fang（示例）`

官方给出的调用示例：`fang -h`

```text
root@kali:~# fang -h
redfang - the bluetooth hunter ver 2.5
(c)2003 @stake Inc
author:   Ollie Whitehouse <
[email protected]
>
enhanced: threads by Simon Halsall <
[email protected]
>
enhanced: device info discovery by Stephen Kapp <
[email protected]
>
usage:
   fang [options]
options:
   -r	range      i.e. 00803789EE76-00803789EEff
   -o	filename   Output Scan to Text Logfile
     	           An address can also be manf+nnnnnn, where manf
     	           is listed with the -l option and nnnnnn is the
     	           tail of the address. All addresses must be 12
     	           characters long
   -t	timeout    The connect timeout, this is 10000 by default
     	           Which is quick and yields results, increase for
     	           reliability
   -n	num        The number of dongles
   -d	           Show debug information
   -s	           Perform Bluetooth Discovery
   -l	           Show device manufacturer codes
   -h              Display help
The devices are assumed to be hci0 to hci(n) where (n) is the number
of threads -1, this is currently not configurable but maybe at a
later date
Updated on: 2026-Mar-02
 Edit this page
rebind
rekono-kbx
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install redfang`，再执行 `redfang --version` 2>/dev/null || `redfang -V`
- [ ] **2.** **读官方帮助** —— `redfang -h`，需要细节时 `man redfang`
- [ ] **3.** **在自有靶场跑最小用例** —— 用 `redfang -h` 里最简单的那个子命令试一次
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/redfang/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/reconnaissance.md`](../../tools/by-attack/reconnaissance.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/redfang/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/redfang/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
