# apktool

> Tool for reverse engineering Android apk files A tool for reverse engineering 3rd party, closed, binary Android apps. It can decode resources to nearly original form and rebuild them after making some modifications; it makes possible to de…

> **功能分类**：数字取证 ｜ **Kali 包**：`apktool` ｜ **官方文档**：<https://www.kali.org/tools/apktool/>

## 1. 安装

```bash
sudo apt update
sudo apt install apktool
```

| 项目 | 内容 |
|------|------|
| 版本 | 2.7.0 |
| 架构 | any |
| 可执行命令 | `apktool` |
| 依赖 | `aapt`、`android-framework-res` |
| 安装体积 | 269 KB |
| 官网 | <https://ibotpeaches.github.io/Apktool/> |
| 源码仓库 | <https://salsa.debian.org/android-tools-team/apktool> |
| 包追踪 | <https://pkg.kali.org/pkg/apktool> |

## 2. 官方用法示例

> 以下为 Kali 官方工具页给出的示例与输出原文。

```text
Usage Example
Use debug mode (d) to decode the given apk file (/root/SdkControllerApp.apk):
root@kali:~# apktool d Facebook\ Lite_v121.0.0.8.97_apkpure.com.apk
I: Using Apktool 2.3.4-dirty on Facebook Lite_v121.0.0.8.97_apkpure.com.apk
I: Loading resource table...
I: Decoding AndroidManifest.xml with resources...
I: Loading resource table from file: /root/.local/share/apktool/framework/1.apk
I: Regular manifest package...
I: Decoding file-resources...
I: Decoding values */* XMLs...
I: Baksmaling classes.dex...
I: Copying assets and libs...
I: Copying unknown files...
I: Copying original files...
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `apktool`

官方给出的调用示例：`apktool d Facebook\ Lite_v121.0.0.8.97_apkpure.com.apk`

```text
root@kali:~# apktool d Facebook\ Lite_v121.0.0.8.97_apkpure.com.apk
I: Using Apktool 2.3.4-dirty on Facebook Lite_v121.0.0.8.97_apkpure.com.apk
I: Loading resource table...
I: Decoding AndroidManifest.xml with resources...
I: Loading resource table from file: /root/.local/share/apktool/framework/1.apk
I: Regular manifest package...
I: Decoding file-resources...
I: Decoding values */* XMLs...
I: Baksmaling classes.dex...
I: Copying assets and libs...
I: Copying unknown files...
I: Copying original files...
```

### `apktool（示例）`

官方给出的调用示例：`apktool -h`

```text
root@kali:~# apktool -h
Apktool v2.7.0-dirty - a tool for reengineering Android apk files
with smali v2.5.2.git2771eae-debian and baksmali v2.5.2.git2771eae-debian
Copyright 2010 Ryszard Wi?niewski <
[email protected]
>
Copyright 2010 Connor Tumbleson <
[email protected]
>
usage: apktool
 -advance,--advanced   prints advance information.
 -version,--version    prints the version then exits
usage: apktool if|install-framework [options] <framework.apk>
 -p,--frame-path <dir>   Stores framework files into <dir>.
 -t,--tag <tag>          Tag frameworks using <tag>.
usage: apktool d[ecode] [options] <file_apk>
 -f,--force              Force delete destination directory.
 -o,--output <dir>       The name of folder that gets written. Default is apk.out
 -p,--frame-path <dir>   Uses framework files located in <dir>.
 -r,--no-res             Do not decode resources.
 -s,--no-src             Do not decode sources.
 -t,--frame-tag <tag>    Uses framework files tagged by <tag>.
usage: apktool b[uild] [options] <app_path>
 -f,--force-all          Skip changes detection and build all files.
 -o,--output <dir>       The name of apk that gets written. Default is dist/name.apk
 -p,--frame-path <dir>   Uses framework files located in <dir>.
For additional info, see: https://ibotpeaches.github.io/Apktool/
For smali/baksmali info, see: https://github.com/JesusFreke/smali
Updated on: 2026-May-25
 Edit this page
aircrack-ng
assetfinder
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install apktool`，再执行 `apktool --version` 2>/dev/null || `apktool -V`
- [ ] **2.** **读官方帮助** —— `apktool -h`，需要细节时 `man apktool`
- [ ] **3.** **在自有靶场跑最小用例** —— 用 `apktool -h` 里最简单的那个子命令试一次
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/apktool/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/resource-development.md`](../../tools/by-attack/resource-development.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/apktool/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/apktool/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
