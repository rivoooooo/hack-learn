# amass

> In-depth DNS Enumeration and Network Mapping This package contains a tool to help information security professionals perform network mapping of attack surfaces and perform external asset discovery using open source information gathering an…

> **功能分类**：识别与指纹 ｜ **Kali 包**：`amass` ｜ **官方文档**：<https://www.kali.org/tools/amass/>

## 1. 安装

```bash
sudo apt update
sudo apt install amass
```

| 项目 | 内容 |
|------|------|
| 版本 | 5.1.1 |
| 架构 | any |
| 可执行命令 | `amass` |
| 依赖 | `libc6`、`libpostal-data`、`sudo` |
| 安装体积 | 50.57 MB |
| 官网 | <https://github.com/OWASP/Amass> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/amass> |
| 包追踪 | <https://pkg.kali.org/pkg/amass> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
amass -h          # 查看用法
man amass         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `amass`

> 官方示例调用：`amass -h`

```text
root@kali:~# amass -h
        .+++:.            :                             .+++.
      +W@@@@@@8        &+W@#               o8W8:      +W@@@@@@#.   oW@@@W#+
     &@#+   .o@##.    .@@@
[email protected]
@@o       :@@#&W8o    .@#:  .:oW+  .@#+++&#&
    +@&        &@&     #@8 +@W@&8@+     :@W.   +@8   +@:          .@8
    8@          @@     8@o  8@8  WW    .@W      W@+  .@W.          o@#:
    WW          &@o    &@:  o@+  o@+   #@.      8@o   +W@#+.        +W@8:
    #@          :@W    &@+  &@+   @8  :@o       o@o     oW@@W+        oW@8
    o@+          @@&   &@+  &@+   #@  &@.      .W@W       .+#@&         o@W.
     WW         +@W@8. &@+  :&    o@+ #@      :@W&@&         &@:  ..     :@o
     :@W:      o@# +Wo &@+        :W: +@W&o++o@W. &@&  8@#o+&@W.  #@:    o@+
      :W@@WWWW@@8       +              :&W@@@@&    &W  .o#@@W&.   :W@WWW@@&
        +o&&&&+.                                                    +oooo.
                                                                      v5.1.1
                                           OWASP Amass Project - @owaspamass
                         In-depth Attack Surface Mapping and Asset Discovery
Usage: amass [assoc|engine|enum|subs|track|viz] [options]
  -h	Show the program usage message
  -help
    	Show the program usage message
  -version
    	Print the Amass version number
Subcommands:
	assoc	Query the OAM along the walk defined by the triples
	engine	Run the Amass collection engine to populate the OAM database
	enum 	Interface with the engine that performs enumerations
	subs 	Analyze and present discovered subdomains and associated data
	track	Analyze OAM data to identify newly discovered assets
	viz  	Analyze OAM data to generate graph visualizations
Updated on: 2026-Aug-25
 Edit this page
airgeddon
apache2
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install amass`，再执行 `amass --version` 2>/dev/null || `amass -V`
- [ ] **2.** **读官方帮助** —— `amass -h`，需要细节时 `man amass`
- [ ] **3.** **在自有靶场跑最小用例** —— 官方给出的调用形式是：`Usage: amass [assoc|engine|enum|subs|track|viz] [options]`
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/amass/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- **精讲教程**（含原理、参数详解、靶场实操与输出解读）：[amass](../../tools/tutorials/01-信息搜集/amass.md)
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/reconnaissance.md`](../../tools/by-attack/reconnaissance.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/amass/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/amass/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
