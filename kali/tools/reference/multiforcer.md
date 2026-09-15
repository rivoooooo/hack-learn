# multiforcer

> GPU accelerated password cracking tool A CUDA & OpenCL accelerated rainbow table implementation from the ground up, and a CUDA hash brute forcing tool with support for many hash types including MD5, SHA1, LM, NTLM, and lots more.

> **功能分类**：通用工具 ｜ **Kali 包**：`multiforcer` ｜ **官方文档**：<https://www.kali.org/tools/multiforcer/>

## 1. 安装

```bash
sudo apt update
sudo apt install multiforcer
```

| 项目 | 内容 |
|------|------|
| 版本 | 1.31 |
| 架构 | amd64 |
| 可执行命令 | `multiforcer`、`showconfig-opencl` |
| 安装体积 | 15.47 MB |
| 官网 | <https://sourceforge.net/projects/cryptohaze/> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/multiforcer> |
| 包追踪 | <https://pkg.kali.org/pkg/multiforcer> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
multiforcer -h          # 查看用法
man multiforcer         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 2 个可执行命令，下面是官方页面内嵌的帮助原文。

### `showconfig-opencl`

> 官方示例调用：`showconfig-opencl -h`

```text
root@kali:~# showconfig-opencl -h
Platform ID 0:
CL_PLATFORM_NAME: Portable Computing Language
CL_PLATFORM_VENDOR: The pocl project
CL_PLATFORM_VERSION: OpenCL 3.0 PoCL 7.1+debian  Linux, None+Asserts, RELOC, SPIR-V, LLVM 21.1.8, SLEEF, DISTRO, POCL_DEBUG
Platform 0:
Device ID 0:
CL_DEVICE_NAME: cpu-penryn-AMD Ryzen 9 7950X 16-Core Processor
CL_DEVICE_VENDOR: AuthenticAMD
CL_DEVICE_AVAILABLE: Yes
CL_DEVICE_MAX_COMPUTE_UNITS: 6
CL_DEVICE_TYPE: CL_DEVICE_TYPE_CPU
CL_DEVICE_MAX_CLOCK_FREQUENCY: 4294 MHz
CL_DEVICE_GLOBAL_MEM_SIZE: 3845 MB
CL_DEVICE_LOCAL_MEM_SIZE: 1024 KB
CL_DEVICE_LOCAL_MEM_TYPE: CL_GLOBAL
CL_DEVICE_MAX_CONSTANT_BUFFER_SIZE: 1024 KB
Updated on: 2026-Aug-25
 Edit this page
mssqlpwner
net-snmp
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install multiforcer`，再执行 `multiforcer --version` 2>/dev/null || `multiforcer -V`
- [ ] **2.** **读官方帮助** —— `multiforcer -h`，需要细节时 `man multiforcer`
- [ ] **3.** **在自有靶场跑最小用例** —— 用 `multiforcer -h` 里最简单的那个子命令试一次
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/multiforcer/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/multiforcer/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/multiforcer/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
