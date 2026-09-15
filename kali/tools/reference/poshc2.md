# poshc2

> Proxy aware C2 framework This package contains a proxy aware C2 framework used to aid penetration testers with red teaming, post-exploitation and lateral movement. PoshC2 is primarily written in Python3 and follows a modular format to enab…

> **功能分类**：通用工具 ｜ **Kali 包**：`poshc2` ｜ **官方文档**：<https://www.kali.org/tools/poshc2/>

## 1. 安装

```bash
sudo apt update
sudo apt install poshc2
```

| 项目 | 内容 |
|------|------|
| 版本 | 9.0 |
| 架构 | all |
| 可执行命令 | `poshc2` |
| 依赖 | `espeak`、`graphviz`、`libjs-bootstrap4`、`libjs-jquery`、`mingw-w64`、`mingw-w64-common`、`mingw-w64-i686-dev`、`mingw-w64-tools`、`mingw-w64-x86-64-dev`、`mono-devel`、`postgresql`、`python3` 等 |
| 安装体积 | 89.72 MB |
| 官网 | <https://github.com/nettitude/PoshC2> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/poshc2> |
| 包追踪 | <https://pkg.kali.org/pkg/poshc2> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
poshc2 -h          # 查看用法
man poshc2         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `fpc`

> 官方示例调用：`fpc -h`

```text
root@kali:~# fpc -h
No PoshC2 project set, please run posh-project
posh
```

### `posh`

> 官方示例调用：`posh -h`

```text
root@kali:~# posh -h
PoshC2 current project file does not exist, please run posh-project
posh-api-server
```

### `posh-api-server`

> 官方示例调用：`posh-api-server -h`

```text
root@kali:~# posh-api-server -h
No PoshC2 project set, please run posh-project
posh-config
```

### `posh-config`

> 官方示例调用：`posh-config -h`

```text
root@kali:~# posh-config -h
No PoshC2 project set, please run posh-project
posh-cookie-decrypter
```

### `posh-cookie-decrypter`

> 官方示例调用：`posh-cookie-decrypter -h`

```text
root@kali:~# posh-cookie-decrypter -h
PoshC2 current project file does not exist, please run posh-project
posh-log
```

### `posh-log`

> 官方示例调用：`posh-log -h`

```text
root@kali:~# posh-log -h
No PoshC2 project set, please run posh-project
posh-project
```

### `posh-project`

> 官方示例调用：`posh-project -h`

```text
root@kali:~# posh-project -h
[*] Usage: posh-project -n <new-project-name>
[*] Usage: posh-project -s <project-to-switch-to>
[*] Usage: posh-project -l (lists projects)
[*] Usage: posh-project -d <project-to-delete>
[*] Usage: posh-project -c (shows current project)
[*] Usage: posh-project -g (quietly shows current project directory for scripting)
posh-server
```

### `posh-server`

> 官方示例调用：`posh-server -h`

```text
root@kali:~# posh-server -h
No PoshC2 project set, please run posh-project
posh-service
```

### `posh-service`

> 官方示例调用：`posh-service -h`

```text
root@kali:~# posh-service -h
No PoshC2 project set, please run posh-project
posh-stop-service
Updated on: 2025-Dec-09
 Edit this page
polenum
powercat
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install poshc2`，再执行 `poshc2 --version` 2>/dev/null || `poshc2 -V`
- [ ] **2.** **读官方帮助** —— `poshc2 -h`，需要细节时 `man poshc2`
- [ ] **3.** **在自有靶场跑最小用例** —— 用 `poshc2 -h` 里最简单的那个子命令试一次
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/poshc2/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/poshc2/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/poshc2/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
