# peass-ng

> Privilege Escalation Awesome Scripts SUITE Privilege escalation tools for Windows and Linux/Unix* and MacOS. These tools search for possible local privilege escalation paths that you could exploit and print them to you with nice colors so …

> **功能分类**：漏洞分析 ｜ **Kali 包**：`peass-ng` ｜ **官方文档**：<https://www.kali.org/tools/peass-ng/>

## 1. 安装

```bash
sudo apt update
sudo apt install peass
```

| 项目 | 内容 |
|------|------|
| 版本 | 20260824.e872d65c |
| 架构 | all |
| 可执行命令 | `peass`、`linpeas`、`winpeas` |
| 依赖 | `kali-defaults`、`linpeas` |
| 安装体积 | 89.58 MB |
| 官网 | <https://github.com/carlospolop/PEASS-ng> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/peass-ng> |
| 包追踪 | <https://pkg.kali.org/pkg/peass-ng> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
peass -h          # 查看用法
man peass         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 3 个可执行命令，下面是官方页面内嵌的帮助原文。

### `linpeas`

官方给出的调用示例：`linpeas -h`

```text
root@kali:~# linpeas -h
> peass ~ Privilege Escalation Awesome Scripts SUITE
/usr/share/peass/linpeas
|-- linpeas.sh
|-- linpeas_darwin_amd64
|-- linpeas_darwin_arm64
|-- linpeas_fat.sh
|-- linpeas_linux_386
|-- linpeas_linux_amd64
|-- linpeas_linux_arm
|-- linpeas_linux_arm64
`-- linpeas_small.sh
```

### `peass`

官方给出的调用示例：`peass -h`

```text
root@kali:~# peass -h
> peass ~ Privilege Escalation Awesome Scripts SUITE
/usr/share/peass/
|-- linpeas
|   |-- linpeas.sh
|   |-- linpeas_darwin_amd64
|   |-- linpeas_darwin_arm64
|   |-- linpeas_fat.sh
|   |-- linpeas_linux_386
|   |-- linpeas_linux_amd64
|   |-- linpeas_linux_arm
|   |-- linpeas_linux_arm64
|   `-- linpeas_small.sh
`-- winpeas
    |-- winPEAS.bat
    |-- winPEAS.ps1
    |-- winPEASany.exe
    |-- winPEASany_ofs.exe
    |-- winPEASx64.exe
    |-- winPEASx64_ofs.exe
    |-- winPEASx86.exe
    `-- winPEASx86_ofs.exe
```

### `winpeas`

官方给出的调用示例：`winpeas -h`

```text
root@kali:~# winpeas -h
> peass ~ Privilege Escalation Awesome Scripts SUITE
/usr/share/peass/winpeas
|-- winPEAS.bat
|-- winPEAS.ps1
|-- winPEASany.exe
|-- winPEASany_ofs.exe
|-- winPEASx64.exe
|-- winPEASx64_ofs.exe
|-- winPEASx86.exe
`-- winPEASx86_ofs.exe
Learn more with
OffSec
Want to learn more about peass-ng? get access to in-depth training and hands-on labs:
PEN-200: 17.1.5. Windows Privilege Escalation: 17.1.5. Automated Enumeration
PEN-200: 18.1.3. Linux Privilege Escalation: Automated Enumeration
PEN-200 course
Updated on: 2026-Aug-25
 Edit this page
pdf-parser
penelope
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install peass`，再执行 `peass --version` 2>/dev/null || `peass -V`
- [ ] **2.** **读官方帮助** —— `peass -h`，需要细节时 `man peass`
- [ ] **3.** **在自有靶场跑最小用例** —— 用 `peass -h` 里最简单的那个子命令试一次
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/peass-ng/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- **精讲教程**（含原理、参数详解、靶场实操与输出解读）：[linpeas](../../tools/tutorials/08-后渗透/linpeas.md)
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/privilege-escalation.md`](../../tools/by-attack/privilege-escalation.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/peass-ng/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/peass-ng/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
