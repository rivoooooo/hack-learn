# patchleaks

> Go from a CVE number to the exact patched code and its vulnerability analysis This package contains a tool to compare two versions of a code‑base, highlight lines changed by vendor, and explain why they matter. Feed the tool an old and a p…

> **功能分类**：通用工具 ｜ **Kali 包**：`patchleaks` ｜ **官方文档**：<https://www.kali.org/tools/patchleaks/>

## 1. 安装

```bash
sudo apt update
sudo apt install patchleaks
```

| 项目 | 内容 |
|------|------|
| 版本 | 0.0~git20251113.3c53291 |
| 架构 | any |
| 可执行命令 | `patchleaks` |
| 依赖 | `libc6`、`libjs-jquery`、`node-fortawesome-fontawesome-free` |
| 安装体积 | 26.88 MB |
| 官网 | <https://github.com/hatlesswizard/PatchLeaks> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/patchleaks> |
| 包追踪 | <https://pkg.kali.org/pkg/patchleaks> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
patchleaks -h          # 查看用法
man patchleaks         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `PatchLeaks`

> 官方示例调用：`PatchLeaks -h`

```text
root@kali:~# PatchLeaks -h
Usage of PatchLeaks:
  -host string
    	Host address to bind to (default "127.0.0.1")
  -language string
    	Comma-separated list of languages to test (php,javascript,python)
  -p int
    	Port to run the server on (default: random free port)
  -t int
    	Number of threads for AI analysis (default: 1) (default 1)
  -test-real-world
    	Run real-world tests instead of starting server
```

### `patchleaks`

> 官方示例调用：`patchleaks -h`

```text
root@kali:~# patchleaks -h
Usage of patchleaks:
  -host string
    	Host address to bind to (default "127.0.0.1")
  -language string
    	Comma-separated list of languages to test (php,javascript,python)
  -p int
    	Port to run the server on (default: random free port)
  -t int
    	Number of threads for AI analysis (default: 1) (default 1)
  -test-real-world
    	Run real-world tests instead of starting server
Updated on: 2026-Mar-02
 Edit this page
owasp-mantra-ff
peirates
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install patchleaks`，再执行 `patchleaks --version` 2>/dev/null || `patchleaks -V`
- [ ] **2.** **读官方帮助** —— `patchleaks -h`，需要细节时 `man patchleaks`
- [ ] **3.** **在自有靶场跑最小用例** —— 官方给出的调用形式是：`Usage of PatchLeaks:`
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/patchleaks/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/patchleaks/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/patchleaks/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
