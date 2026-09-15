# cisco-ocs

> Mass Cisco scanner A mass Cisco scanning tool.

> **功能分类**：漏洞分析 ｜ **Kali 包**：`cisco-ocs` ｜ **官方文档**：<https://www.kali.org/tools/cisco-ocs/>

## 1. 安装

```bash
sudo apt update
sudo apt install cisco-ocs
```

| 项目 | 内容 |
|------|------|
| 版本 | 0.2 |
| 架构 | any |
| 可执行命令 | `cisco-ocs` |
| 依赖 | `libc6` |
| 安装体积 | 25 KB |
| 官网 | <http://hacklab.altervista.org/> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/cisco-ocs> |
| 包追踪 | <https://pkg.kali.org/pkg/cisco-ocs> |

## 2. 官方用法示例

> 以下为 Kali 官方工具页给出的示例与输出原文。

```text
Usage Example
Attempt to exploit Cisco devices in the given IP range (192.168.99.200 192.168.99.202):
root@kali:~# cisco-ocs 192.168.99.200 192.168.99.202
********************************* OCS v 0.2 **********************************
****                                                                      ****
****                           coded by OverIP                            ****
****                           overip@gmail.com                           ****
****                           under GPL License                          ****
****                                                                      ****
****             usage: ./ocs xxx.xxx.xxx.xxx yyy.yyy.yyy.yyy             ****
****                                                                      ****
****                   xxx.xxx.xxx.xxx = range start IP                   ****
****                    yyy.yyy.yyy.yyy = range end IP                    ****
****                                                                      ****
******************************************************************************


-192.168.99.200
  |Logging... 192.168.99.200
  |Router not vulnerable.


-192.168.99.201
  |Logging... 192.168.99.201
  |Router not vulnerable.


-192.168.99.202
  |Logging... 192.168.99.202
  |Router not vulnerable.
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `cisco-ocs`

> 官方示例调用：`cisco-ocs 192.168.99.200 192.168.99.202`

```text
root@kali:~# cisco-ocs 192.168.99.200 192.168.99.202
********************************* OCS v 0.2 **********************************
****                                                                      ****
****                           coded by OverIP                            ****
****
[email protected]
                           ****
****                           under GPL License                          ****
****                                                                      ****
****             usage: ./ocs xxx.xxx.xxx.xxx yyy.yyy.yyy.yyy             ****
****                                                                      ****
****                   xxx.xxx.xxx.xxx = range start IP                   ****
****                    yyy.yyy.yyy.yyy = range end IP                    ****
****                                                                      ****
******************************************************************************
-192.168.99.200
  |Logging... 192.168.99.200
  |Router not vulnerable.
-192.168.99.201
  |Logging... 192.168.99.201
  |Router not vulnerable.
-192.168.99.202
  |Logging... 192.168.99.202
  |Router not vulnerable.
```

### `cisco-ocs -h`

> 官方示例调用：`cisco-ocs -h`

```text
root@kali:~# cisco-ocs -h
********************************* OCS v 0.2 **********************************
****                                                                      ****
****                           coded by OverIP                            ****
****
[email protected]
                           ****
****                           under GPL License                          ****
****                                                                      ****
****             usage: ./ocs xxx.xxx.xxx.xxx yyy.yyy.yyy.yyy             ****
****                                                                      ****
****                   xxx.xxx.xxx.xxx = range start IP                   ****
****                    yyy.yyy.yyy.yyy = range end IP                    ****
****                                                                      ****
******************************************************************************
use: cisco-ocs IP IP
Updated on: 2026-Mar-02
 Edit this page
cisco-global-exploiter
commix
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install cisco-ocs`，再执行 `cisco-ocs --version` 2>/dev/null || `cisco-ocs -V`
- [ ] **2.** **读官方帮助** —— `cisco-ocs -h`，需要细节时 `man cisco-ocs`
- [ ] **3.** **在自有靶场跑最小用例** —— 用 `cisco-ocs -h` 里最简单的那个子命令试一次
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/cisco-ocs/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/discovery.md`](../../tools/by-attack/discovery.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/cisco-ocs/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/cisco-ocs/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
