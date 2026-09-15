# protos-sip

> SIP test suite The purpose of this test-suite is to evaluate implementation level security and robustness of Session Initiation Protocol (SIP) implementations.

> **功能分类**：漏洞分析 ｜ **Kali 包**：`protos-sip` ｜ **官方文档**：<https://www.kali.org/tools/protos-sip/>

## 1. 安装

```bash
sudo apt update
sudo apt install protos-sip
```

| 项目 | 内容 |
|------|------|
| 版本 | 1.0 |
| 架构 | all |
| 可执行命令 | `protos-sip` |
| 依赖 | `default-jre`、`java-wrappers` |
| 安装体积 | 2.15 MB |
| 官网 | <https://www.ee.oulu.fi/research/ouspg/PROTOS_Test-Suite_c07-sip> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/protos-sip> |
| 包追踪 | <https://pkg.kali.org/pkg/protos-sip> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
protos-sip -h          # 查看用法
man protos-sip         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `protos-sip`

官方给出的调用示例：`protos-sip -h`

```text
root@kali:~# protos-sip -h
Usage java -jar <jarfile>.jar [ [OPTIONS] | -touri <SIP-URI> ]
  -touri  <addr>        Recipient of the request
                        Example: <addr> :
[email protected]
  -fromuri <addr>       Initiator of the request
                        Default: user@kali
  -sendto <domain>      Send packets to <domain> instead of
                        domainname of -touri
  -callid <callid>      Call id to start test-case call ids from
                        Default: 0
  -dport <port>         Portnumber to send packets on host.
                        Default: 5060
  -lport <port>         Local portnumber to send packets from
                        Default: 5060
  -delay <ms>           Time to wait before sending new test-case
                        Defaults to 100 ms (milliseconds)
  -replywait <ms>       Maximum time to wait for host to reply
                        Defaults to 100 ms (milliseconds)
  -file <file>          Send file <file> instead of test-case(s)
  -help                 Display this help
  -jarfile <file>       Get data from an alternate bugcat
                        JAR-file <file>
  -showreply            Show received packets
  -showsent             Show sent packets
  -teardown             Send CANCEL/ACK
  -single <index>       Inject a single test-case <index>
  -start <index>        Inject test-cases starting from <index>
  -stop <index>         Stop test-case injection to <index>
  -maxpdusize <int>     Maximum PDU size
                        Default to 65507 bytes
  -validcase            Send valid case (case #0) after each
                        test-case and wait for a response. May
                        be used to check if the target is still
                        responding. Default: off
Updated on: 2026-Mar-02
 Edit this page
pnscan
python-defaults
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install protos-sip`，再执行 `protos-sip --version` 2>/dev/null || `protos-sip -V`
- [ ] **2.** **读官方帮助** —— `protos-sip -h`，需要细节时 `man protos-sip`
- [ ] **3.** **在自有靶场跑最小用例** —— 官方给出的调用形式是：`Usage java -jar <jarfile>.jar [ [OPTIONS] | -touri <SIP-URI> ]`
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/protos-sip/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/discovery.md`](../../tools/by-attack/discovery.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/protos-sip/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/protos-sip/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
