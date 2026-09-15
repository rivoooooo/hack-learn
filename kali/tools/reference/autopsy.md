# autopsy

> Graphical interface to SleuthKit The Autopsy Forensic Browser is a graphical interface to the command line digital forensic analysis tools in The Sleuth Kit. Together, The Sleuth Kit and Autopsy provide many of the same features as commerc…

> **功能分类**：数字取证 ｜ **Kali 包**：`autopsy` ｜ **官方文档**：<https://www.kali.org/tools/autopsy/>

## 1. 安装

```bash
sudo apt update
sudo apt install autopsy
```

| 项目 | 内容 |
|------|------|
| 版本 | 2.24 |
| 架构 | all |
| 可执行命令 | `autopsy` |
| 依赖 | `binutils`、`perl`、`sleuthkit` |
| 安装体积 | 1.00 MB |
| 官网 | <https://www.sleuthkit.org/autopsy/> |
| 源码仓库 | <https://salsa.debian.org/debian/autopsy> |
| 包追踪 | <https://pkg.kali.org/pkg/autopsy> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
autopsy -h          # 查看用法
man autopsy         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `autopsy`

官方给出的调用示例：`autopsy -h`

```text
root@kali:~# autopsy -h
Invalid flag: -h
usage: /usr/bin/autopsy [-c] [-C] [-d evid_locker] [-i device filesystem mnt] [-p port] [remoteaddr]
  -c: force a cookie in the URL
  -C: force NO cookie in the URL
  -d dir: specify the evidence locker directory
  -i device filesystem mnt: Specify info for live analysis
  -p port: specify the server port (default: 9999)
  remoteaddr: specify the host with the browser (default: localhost)
Learn more with
OffSec
Want to learn more about autopsy? get access to in-depth training and hands-on labs:
Digital Forensics Foundations: 3. Computer Forensics
Updated on: 2025-Dec-09
 Edit this page
asleap
b374k
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install autopsy`，再执行 `autopsy --version` 2>/dev/null || `autopsy -V`
- [ ] **2.** **读官方帮助** —— `autopsy -h`，需要细节时 `man autopsy`
- [ ] **3.** **在自有靶场跑最小用例** —— 用 `autopsy -h` 里最简单的那个子命令试一次
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/autopsy/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- **精讲教程**（含原理、参数详解、靶场实操与输出解读）：[autopsy](../../tools/tutorials/09-数字取证/autopsy.md)
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/forensics.md`](../../tools/by-attack/forensics.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/autopsy/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/autopsy/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
