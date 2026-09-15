# defectdojo

> Security orchestration and vulnerability management platform This package contains a security orchestration and vulnerability management platform. DefectDojo allows you to manage your application security program, maintain product and appl…

> **功能分类**：识别与指纹 ｜ **Kali 包**：`defectdojo` ｜ **官方文档**：<https://www.kali.org/tools/defectdojo/>

## 1. 安装

```bash
sudo apt update
sudo apt install defectdojo
```

| 项目 | 内容 |
|------|------|
| 版本 | 2.37.3 |
| 架构 | amd64 |
| 可执行命令 | `defectdojo`、`defectdojo-start`、`defectdojo-stop` |
| 依赖 | `adduser`、`celery`、`kali-defaults`、`nginx`、`postgresql`、`python3-argon2`、`python3-asteval`、`python3-blackduck`、`python3-bleach`、`python3-celery`、`python3-cpe`、`python3-cvss` 等 |
| 安装体积 | 107.69 MB |
| 官网 | <https://github.com/DefectDojo/django-DefectDojo> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/defectdojo> |
| 包追踪 | <https://pkg.kali.org/pkg/defectdojo> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
defectdojo -h          # 查看用法
man defectdojo         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 3 个可执行命令，下面是官方页面内嵌的帮助原文。

### `defectdojo`

> 官方示例调用：`defectdojo -h`

```text
root@kali:~# defectdojo -h
┏━(Message from Kali developers)
┃
┃ The command defectdojo is deprecated. Please use defectdojo-start instead.
┃
┗━
```

### `defectdojo-start`

> 官方示例调用：`defectdojo-start -h`

```text
root@kali:~# defectdojo-start -h
User _defectdojo already exists in PostgreSQL
 Creating database
```

### `defectdojo-stop`

> 官方示例调用：`defectdojo-stop -h`

```text
root@kali:~# defectdojo-stop -h
┏━(Message from Kali developers)
┃
┃ Service status:
┃   * defectdojo.service - The Defect Dojo nginx service
┃        Loaded: loaded (/usr/lib/systemd/system/defectdojo.service; 5:185mdisabled; preset: 5:185mdisabled)
┃        Active: inactive (dead)
┃
┗━
Updated on: 2026-Aug-25
 Edit this page
ddrescue
dex2jar
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install defectdojo`，再执行 `defectdojo --version` 2>/dev/null || `defectdojo -V`
- [ ] **2.** **读官方帮助** —— `defectdojo -h`，需要细节时 `man defectdojo`
- [ ] **3.** **在自有靶场跑最小用例** —— 用 `defectdojo -h` 里最简单的那个子命令试一次
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/defectdojo/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/services-and-other-tools.md`](../../tools/by-attack/services-and-other-tools.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/defectdojo/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/defectdojo/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
