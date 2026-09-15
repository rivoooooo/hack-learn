# isr-evilgrade

> Evilgrade framework Evilgrade is a modular framework that allows the user to take advantage of poor upgrade implementations by injecting fake updates. It comes with pre-made binaries (agents), a working default configuration for fast pente…

> **功能分类**：嗅探与欺骗 ｜ **Kali 包**：`isr-evilgrade` ｜ **官方文档**：<https://www.kali.org/tools/isr-evilgrade/>

## 1. 安装

```bash
sudo apt update
sudo apt install isr-evilgrade
```

| 项目 | 内容 |
|------|------|
| 版本 | 2.0.9 |
| 架构 | all |
| 可执行命令 | `isr-evilgrade`、`evilgrade` |
| 依赖 | `libdata-dump-perl`、`libdigest-md5-file-perl`、`librpc-xml-perl`、`perl`、`evilgrade` |
| 安装体积 | 13.14 MB |
| 官网 | <https://github.com/infobyte/evilgrade> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/isr-evilgrade> |
| 包追踪 | <https://pkg.kali.org/pkg/isr-evilgrade> |

## 2. 官方用法示例

> 以下为 Kali 官方工具页给出的示例与输出原文。

```text
Usage Example
root@kali:~# evilgrade
[DEBUG] - Loading module: modules/allmynotes.pm
[DEBUG] - Loading module: modules/notepadplus.pm
[DEBUG] - Loading module: modules/nokia.pm
[DEBUG] - Loading module: modules/winscp.pm
[DEBUG] - Loading module: modules/jet.pm
[DEBUG] - Loading module: modules/sunjava.pm
[DEBUG] - Loading module: modules/bbappworld.pm
[DEBUG] - Loading module: modules/gom.pm
[DEBUG] - Loading module: modules/ccleaner.pm
[DEBUG] - Loading module: modules/superantispyware.pm
[DEBUG] - Loading module: modules/winupdate.pm
[DEBUG] - Loading module: modules/vidbox.pm
[DEBUG] - Loading module: modules/atube.pm
[DEBUG] - Loading module: modules/winzip.pm
[DEBUG] - Loading module: modules/apt.pm
[DEBUG] - Loading module: modules/mirc.pm
[DEBUG] - Loading module: modules/filezilla.pm
[DEBUG] - Loading module: modules/dap.pm
[DEBUG] - Loading module: modules/flip4mac.pm
[DEBUG] - Loading module: modules/divxsuite.pm
[DEBUG] - Loading module: modules/opera.pm
[DEBUG] - Loading module: modules/yahoomsn.pm
[DEBUG] - Loading module: modules/linkedin.pm
[DEBUG] - Loading module: modules/techtracker.pm
[DEBUG] - Loading module: modules/fcleaner.pm
[DEBUG] - Loading module: modules/appleupdate.pm
[DEBUG] - Loading module: modules/trillian.pm
[DEBUG] - Loading module: modules/sunbelt.pm
[DEBUG] - Loading module: modules/growl.pm
[DEBUG] - Loading module: modules/vmware.pm
[DEBUG] - Loading module: modules/panda_antirootkit.pm
[DEBUG] - Loading module: modules/orbit.pm
[DEBUG] - Loading module: modules/teamviewer.pm
[DEBUG] - Loading module: modules/blackberry.pm
[DEBUG] - Loading module: modules/miranda.pm
[DEBUG] - Loading module: modules/clamwin.pm
[DEBUG] - Loading module: modules/jetphoto.pm
[DEBUG] - Loading module: modules/istat.pm
[DEBUG] - Loading module: modules/nokiasoftware.pm
[DEBUG] - Loading module: modules/getjar.pm
[DEBUG] - Loading module: modules/sparkle.pm
[DEBUG] - Loading module: modules/cpan.pm
[DEBUG] - Loading module: modules/cygwin.pm
[DEBUG] - Loading module: modules/express_talk.pm
[DEBUG] - Loading module: modules/openoffice.pm
[DEBUG] - Loading module: modules/osx.pm
[DEBUG] - Loading module: modules/flashget.pm
[DEBUG] - Loading module: modules/amsn.pm
[DEBUG] - Loading module: modules/isopen.pm
[DEBUG] - Loading module: modules/apptapp.pm
[DEBUG] - Loading module: modules/googleanalytics.pm
[DEBUG] - Loading module: modules/autoit3.pm
[DEBUG] - Loading module: modules/ubertwitter.pm
[DEBUG] - Loading module: modules/photoscape.pm
[DEBUG] - Loading module: modules/quicktime.pm
[DEBUG] - Loading module: modules/itunes.pm
[DEBUG] - Loading module: modules/winamp.pm
[DEBUG] - Loading module: modules/skype.pm
[DEBUG] - Loading module: modules/virtualbox.pm
[DEBUG] - Loading module: modules/bsplayer.pm
[DEBUG] - Loading module: modules/freerip.pm
[DEBUG] - Loading module: modules/paintnet.pm
[DEBUG] - Loading module: modules/speedbit.pm
            _ _                     _
           (_) |                   | |
  _____   ___| | __ _ _ __ __ _  __| | ___
 / _ \ \ / / | |/ _` | '__/ _` |/ _` |/ _ \
|  __/\ V /| | | (_| | | | (_| | (_| |  __/
 \___| \_/ |_|_|\__, |_|  \__,_|\__,_|\___|
                __/ |
                |___/
-------------------------------------------
---------------------  www.infobytesec.com
- 63 modules available.

evilgrade>config skype
evilgrade(skype)>start
evilgrade(skype)>
[17/5/2014:12:52:11] - [WEBSERVER] - Webserver ready. Waiting for connections ...

evilgrade(skype)>
[17/5/2014:12:52:11] - [DNSSERVER] - DNS Server Ready. Waiting for Connections ...

evilgrade(skype)>
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 2 个可执行命令，下面是官方页面内嵌的帮助原文。

### `evilgrade`

```text
root@kali:~# evilgrade
[DEBUG] - Loading module: modules/allmynotes.pm
[DEBUG] - Loading module: modules/notepadplus.pm
[DEBUG] - Loading module: modules/nokia.pm
[DEBUG] - Loading module: modules/winscp.pm
[DEBUG] - Loading module: modules/jet.pm
[DEBUG] - Loading module: modules/sunjava.pm
[DEBUG] - Loading module: modules/bbappworld.pm
[DEBUG] - Loading module: modules/gom.pm
[DEBUG] - Loading module: modules/ccleaner.pm
[DEBUG] - Loading module: modules/superantispyware.pm
[DEBUG] - Loading module: modules/winupdate.pm
[DEBUG] - Loading module: modules/vidbox.pm
[DEBUG] - Loading module: modules/atube.pm
[DEBUG] - Loading module: modules/winzip.pm
[DEBUG] - Loading module: modules/apt.pm
[DEBUG] - Loading module: modules/mirc.pm
[DEBUG] - Loading module: modules/filezilla.pm
[DEBUG] - Loading module: modules/dap.pm
[DEBUG] - Loading module: modules/flip4mac.pm
[DEBUG] - Loading module: modules/divxsuite.pm
[DEBUG] - Loading module: modules/opera.pm
[DEBUG] - Loading module: modules/yahoomsn.pm
[DEBUG] - Loading module: modules/linkedin.pm
[DEBUG] - Loading module: modules/techtracker.pm
[DEBUG] - Loading module: modules/fcleaner.pm
[DEBUG] - Loading module: modules/appleupdate.pm
[DEBUG] - Loading module: modules/trillian.pm
[DEBUG] - Loading module: modules/sunbelt.pm
[DEBUG] - Loading module: modules/growl.pm
[DEBUG] - Loading module: modules/vmware.pm
[DEBUG] - Loading module: modules/panda_antirootkit.pm
[DEBUG] - Loading module: modules/orbit.pm
[DEBUG] - Loading module: modules/teamviewer.pm
[DEBUG] - Loading module: modules/blackberry.pm
[DEBUG] - Loading module: modules/miranda.pm
[DEBUG] - Loading module: modules/clamwin.pm
[DEBUG] - Loading module: modules/jetphoto.pm
[DEBUG] - Loading module: modules/istat.pm
[DEBUG] - Loading module: modules/nokiasoftware.pm
[DEBUG] - Loading module: modules/getjar.pm
[DEBUG] - Loading module: modules/sparkle.pm
[DEBUG] - Loading module: modules/cpan.pm
[DEBUG] - Loading module: modules/cygwin.pm
[DEBUG] - Loading module: modules/express_talk.pm
[DEBUG] - Loading module: modules/openoffice.pm
[DEBUG] - Loading module: modules/osx.pm
[DEBUG] - Loading module: modules/flashget.pm
[DEBUG] - Loading module: modules/amsn.pm
[DEBUG] - Loading module: modules/isopen.pm
[DEBUG] - Loading module: modules/apptapp.pm
[DEBUG] - Loading module: modules/googleanalytics.pm
[DEBUG] - Loading module: modules/autoit3.pm
[DEBUG] - Loading module: modules/ubertwitter.pm
[DEBUG] - Loading module: modules/photoscape.pm
[DEBUG] - Loading module: modules/quicktime.pm
[DEBUG] - Loading module: modules/itunes.pm
[DEBUG] - Loading module: modules/winamp.pm
[DEBUG] - Loading module: modules/skype.pm
[DEBUG] - Loading module: modules/virtualbox.pm
[DEBUG] - Loading module: modules/bsplayer.pm
[DEBUG] - Loading module: modules/freerip.pm
[DEBUG] - Loading module: modules/paintnet.pm
[DEBUG] - Loading module: modules/speedbit.pm
            _ _                     _
           (_) |                   | |
  _____   ___| | __ _ _ __ __ _  __| | ___
 / _ \ \ / / | |/ _` | '__/ _` |/ _` |/ _ \
|  __/\ V /| | | (_| | | | (_| | (_| |  __/
 \___| \_/ |_|_|\__, |_|  \__,_|\__,_|\___|
                __/ |
                |___/
-------------------------------------------
---------------------  www.infobytesec.com
- 63 modules available.
evilgrade>config skype
evilgrade(skype)>start
evilgrade(skype)>
[17/5/2014:12:52:11] - [WEBSERVER] - Webserver ready. Waiting for connections ...
evilgrade(skype)>
[17/5/2014:12:52:11] - [DNSSERVER] - DNS Server Ready. Waiting for Connections ...
evilgrade(skype)>
```

### `evilgrade（示例）`

官方给出的调用示例：`evilgrade -h`

```text
root@kali:~# evilgrade -h
[DEBUG] - Loading module: modules/orbit.pm
[DEBUG] - Loading module: modules/sparkle.pm
[DEBUG] - Loading module: modules/soapui.pm
[DEBUG] - Loading module: modules/timedoctor.pm
[DEBUG] - Loading module: modules/trillian.pm
[DEBUG] - Loading module: modules/inteldriver.pm
[DEBUG] - Loading module: modules/amsn.pm
[DEBUG] - Loading module: modules/divxsuite.pm
[DEBUG] - Loading module: modules/freerip.pm
[DEBUG] - Loading module: modules/openoffice.pm
[DEBUG] - Loading module: modules/winscp.pm
[DEBUG] - Loading module: modules/openbazaar.pm
[DEBUG] - Loading module: modules/linkedin.pm
[DEBUG] - Loading module: modules/port.pm
[DEBUG] - Loading module: modules/speedbit.pm
[DEBUG] - Loading module: modules/vmware.pm
[DEBUG] - Loading module: modules/flashget.pm
[DEBUG] - Loading module: modules/jdtoolkit.pm
[DEBUG] - Loading module: modules/winupdate.pm
[DEBUG] - Loading module: modules/vidbox.pm
[DEBUG] - Loading module: modules/bsplayer.pm
[DEBUG] - Loading module: modules/yahoomsn.pm
[DEBUG] - Loading module: modules/getjar.pm
[DEBUG] - Loading module: modules/notepadplus.pm
[DEBUG] - Loading module: modules/itunes.pm
[DEBUG] - Loading module: modules/cpan.pm
[DEBUG] - Loading module: modules/lenovoapk.pm
[DEBUG] - Loading module: modules/mirc.pm
[DEBUG] - Loading module: modules/ubertwitter.pm
[DEBUG] - Loading module: modules/nokiasoftware.pm
[DEBUG] - Loading module: modules/lenovo.pm
[DEBUG] - Loading module: modules/keepass.pm
[DEBUG] - Loading module: modules/miranda.pm
[DEBUG] - Loading module: modules/gom.pm
[DEBUG] - Loading module: modules/atube.pm
[DEBUG] - Loading module: modules/virtualbox.pm
[DEBUG] - Loading module: modules/sunbelt.pm
[DEBUG] - Loading module: modules/blackberry.pm
[DEBUG] - Loading module: modules/growl.pm
[DEBUG] - Loading module: modules/flip4mac.pm
[DEBUG] - Loading module: modules/samsung.pm
[DEBUG] - Loading module: modules/fsecure_client.pm
[DEBUG] - Loading module: modules/techtracker.pm
[DEBUG] - Loading module: modules/istat.pm
[DEBUG] - Loading module: modules/sparkle2.pm
[DEBUG] - Loading module: modules/jetphoto.pm
[DEBUG] - Loading module: modules/clamwin.pm
[DEBUG] - Loading module: modules/skype.pm
[DEBUG] - Loading module: modules/apt.pm
[DEBUG] - Loading module: modules/allmynotes.pm
[DEBUG] - Loading module: modules/appstore.pm
[DEBUG] - Loading module: modules/autoit3.pm
[DEBUG] - Loading module: modules/ccleaner.pm
[DEBUG] - Loading module: modules/safari.pm
[DEBUG] - Loading module: modules/nokia.pm
[DEBUG] - Loading module: modules/opera.pm
[DEBUG] - Loading module: modules/teamviewer.pm
[DEBUG] - Loading module: modules/paintnet.pm
[DEBUG] - Loading module: modules/filezilla.pm
[DEBUG] - Loading module: modules/osx.pm
[DEBUG] - Loading module: modules/dap.pm
[DEBUG] - Loading module: modules/winzip.pm
[DEBUG] - Loading module: modules/googleanalytics.pm
[DEBUG] - Loading module: modules/asus.pm
[DEBUG] - Loading module: modules/cygwin.pm
[DEBUG] - Loading module: modules/acer.pm
[DEBUG] - Loading module: modules/sunjava.pm
[DEBUG] - Loading module: modules/winamp.pm
[DEBUG] - Loading module: modules/isopen.pm
[DEBUG] - Loading module: modules/appleupdate.pm
[DEBUG] - Loading module: modules/superantispyware.pm
[DEBUG] - Loading module: modules/fcleaner.pm
[DEBUG] - Loading module: modules/lenovofirmware.pm
[DEBUG] - Loading module: modules/apptapp.pm
[DEBUG] - Loading module: modules/jet.pm
[DEBUG] - Loading module: modules/panda_antirootkit.pm
[DEBUG] - Loading module: modules/express_talk.pm
[DEBUG] - Loading module: modules/bbappworld.pm
[DEBUG] - Loading module: modules/photoscape.pm
[DEBUG] - Loading module: modules/quicktime.pm
            _ _                     _
           (_) |                   | |
  _____   ___| | __ _ _ __ __ _  __| | ___
 / _ \ \ / / | |/ _` | '__/ _` |/ _` |/ _ \
|  __/\ V /| | | (_| | | | (_| | (_| |  __/
 \___| \_/ |_|_|\__, |_|  \__,_|\__,_|\___|
                __/ |
                |___/
-------------------------------------------
---------------------  www.infobytesec.com
- 80 modules available.
evilgrade>
Updated on: 2026-Aug-25
 Edit this page
intrace
ivre
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install isr-evilgrade`，再执行 `isr-evilgrade --version` 2>/dev/null || `isr-evilgrade -V`
- [ ] **2.** **读官方帮助** —— `isr-evilgrade -h`，需要细节时 `man isr-evilgrade`
- [ ] **3.** **在自有靶场跑最小用例** —— 用 `isr-evilgrade -h` 里最简单的那个子命令试一次
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/isr-evilgrade/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/execution.md`](../../tools/by-attack/execution.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/isr-evilgrade/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/isr-evilgrade/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
