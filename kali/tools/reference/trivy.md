# trivy

> Comprehensive and versatile security scanner This package contains a comprehensive and versatile security scanner. Trivy has scanners that look for security issues, and targets where it can find those issues. It can find vulnerabilities, m…

> **功能分类**：通用工具 ｜ **Kali 包**：`trivy` ｜ **官方文档**：<https://www.kali.org/tools/trivy/>

## 1. 安装

```bash
sudo apt update
sudo apt install trivy
```

| 项目 | 内容 |
|------|------|
| 版本 | 0.66.0 |
| 架构 | any |
| 可执行命令 | `trivy` |
| 依赖 | `libc6` |
| 安装体积 | 229.39 MB |
| 官网 | <https://github.com/aquasecurity/trivy> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/trivy> |
| 包追踪 | <https://pkg.kali.org/pkg/trivy> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
trivy -h          # 查看用法
man trivy         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `trivy`

> 官方示例调用：`trivy -h`

```text
root@kali:~# trivy -h
Scanner for vulnerabilities in container images, file systems, and Git repositories, as well as for configuration issues and hard-coded secrets
Usage:
  trivy [global flags] command [flags] target
  trivy [command]
Examples:
  # Scan a container image
  $ trivy image python:3.4-alpine
  # Scan a container image from a tar archive
  $ trivy image --input ruby-3.1.tar
  # Scan local filesystem
  $ trivy fs .
  # Run in server mode
  $ trivy server
Scanning Commands
  config      Scan config files for misconfigurations
  filesystem  Scan local filesystem
  image       Scan a container image
  kubernetes  [EXPERIMENTAL] Scan kubernetes cluster
  repository  Scan a repository
  rootfs      Scan rootfs
  sbom        Scan SBOM for vulnerabilities and licenses
  vm          [EXPERIMENTAL] Scan a virtual machine image
Management Commands
  module      Manage modules
  plugin      Manage plugins
  vex         [EXPERIMENTAL] VEX utilities
Utility Commands
  clean       Remove cached files
  completion  Generate the autocompletion script for the specified shell
  convert     Convert Trivy JSON report into a different format
  help        Help about any command
  registry    Manage registry authentication
  server      Server mode
  version     Print the version
Flags:
      --cache-dir string          cache directory (default "/root/.cache/trivy")
  -c, --config string             config path (default "trivy.yaml")
  -d, --debug                     debug mode
  -f, --format string             version format (json)
      --generate-default-config   write the default config to trivy-default.yaml
  -h, --help                      help for trivy
      --insecure                  allow insecure server connections
  -q, --quiet                     suppress progress bar and log output
      --timeout duration          timeout (default 5m0s)
  -v, --version                   show version
Use "trivy [command] --help" for more information about a command.
Updated on: 2025-Dec-09
 Edit this page
traceroute
tundeep
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install trivy`，再执行 `trivy --version` 2>/dev/null || `trivy -V`
- [ ] **2.** **读官方帮助** —— `trivy -h`，需要细节时 `man trivy`
- [ ] **3.** **在自有靶场跑最小用例** —— 官方给出的调用形式是：`Usage:`
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/trivy/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/trivy/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/trivy/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
