# sfuzz

> Black Box testing utilities In the same vein as the Generic Protocol Framework, sfuzz is a really simple to use black box testing suite called Simple Fuzzer (what else would you expect?). The goal is to provide a simple to use, but fairly …

> **功能分类**：漏洞分析 ｜ **Kali 包**：`sfuzz` ｜ **官方文档**：<https://www.kali.org/tools/sfuzz/>

## 1. 安装

```bash
sudo apt update
sudo apt install sfuzz
```

| 项目 | 内容 |
|------|------|
| 版本 | 0.7.0 |
| 架构 | any |
| 可执行命令 | `sfuzz`、`sfo` |
| 依赖 | `libc6`、`sfo` |
| 安装体积 | 191 KB |
| 官网 | <http://aconole.brad-x.com/programs/sfuzz.html> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/sfuzz> |
| 包追踪 | <https://pkg.kali.org/pkg/sfuzz> |

## 2. 官方用法示例

> 以下为 Kali 官方工具页给出的示例与输出原文。

```text
Usage Example
Fuzz the target server (-S 192.168.1.1) on port 10443 (-p 10443) with TCP output mode (-T), using the basic HTTP config (-f /usr/share/sfuzz/sfuzz-sample/basic.http):
root@kali:~# sfuzz -S 192.168.1.1 -p 10443 -T -f /usr/share/sfuzz/sfuzz-sample/basic.http
[12:53:47] dumping options:
    filename: </usr/share/sfuzz/sfuzz-sample/basic.http>
    state:    <8>
    lineno:   <56>
    literals:  [74]
    sequences: [34]
    symbols: [0]
    req_del:  <200>
    mseq_len: <10024>
    plugin: <none>
    s_syms: <0>
    literal[1] = [AREALLYBADSTRING]
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 2 个可执行命令，下面是官方页面内嵌的帮助原文。

### `sfuzz`

> 官方示例调用：`sfuzz -S 192.168.1.1 -p 10443 -T -f /usr/share/sfuzz/sfuzz-sample/basic.http`

```text
root@kali:~# sfuzz -S 192.168.1.1 -p 10443 -T -f /usr/share/sfuzz/sfuzz-sample/basic.http
[12:53:47] dumping options:
    filename: </usr/share/sfuzz/sfuzz-sample/basic.http>
    state:    <8>
    lineno:   <56>
    literals:  [74]
    sequences: [34]
    symbols: [0]
    req_del:  <200>
    mseq_len: <10024>
    plugin: <none>
    s_syms: <0>
    literal[1] = [AREALLYBADSTRING]
```

### `sfo`

> 官方示例调用：`sfo -h`

```text
root@kali:~# sfo -h
 [sfo] === spawning!
[] Attempting to spawn a monitored task.
[SFUZZ-ORACLE] attached [680382].
[680382] Exited (possibly normal), status[255]
 [sfo] === spawning!
[] Attempting to spawn a monitored task.
[SFUZZ-ORACLE] attached [680383].
[680383] Exited (possibly normal), status[255]
 [sfo] === spawning!
[] Attempting to spawn a monitored task.
[SFUZZ-ORACLE] attached [680384].
[680384] Exited (possibly normal), status[255]
 [sfo] === spawning!
[] Attempting to spawn a monitored task.
[SFUZZ-ORACLE] attached [680385].
[680385] Exited (possibly normal), status[255]
 [sfo] === spawning!
[] Attempting to spawn a monitored task.
[SFUZZ-ORACLE] attached [680393].
[680393] Exited (possibly normal), status[255]
 [sfo] === spawning!
[] Attempting to spawn a monitored task.
[SFUZZ-ORACLE] attached [680408].
[680408] Exited (possibly normal), status[255]
 [sfo] === spawning!
[] Attempting to spawn a monitored task.
[SFUZZ-ORACLE] attached [680454].
[680454] Exited (possibly normal), status[255]
 [sfo] === spawning!
[] Attempting to spawn a monitored task.
[SFUZZ-ORACLE] attached [680463].
[680463] Exited (possibly normal), status[255]
 [sfo] === spawning!
[] Attempting to spawn a monitored task.
[SFUZZ-ORACLE] attached [680468].
[680468] Exited (possibly normal), status[255]
 [sfo] === spawning!
[] Attempting to spawn a monitored task.
[SFUZZ-ORACLE] attached [680470].
[680470] Exited (possibly normal), status[255]
 [sfo] === spawning!
[] Attempting to spawn a monitored task.
[SFUZZ-ORACLE] attached [680475].
[680475] Exited (possibly normal), status[255]
 [sfo] === spawning!
[] Attempting to spawn a monitored task.
[SFUZZ-ORACLE] attached [680487].
[680487] Exited (possibly normal), status[255]
 [sfo] === spawning!
[] Attempting to spawn a monitored task.
[SFUZZ-ORACLE] attached [680505].
[680505] Exited (possibly normal), status[255]
 [sfo] === spawning!
[] Attempting to spawn a monitored task.
[SFUZZ-ORACLE] attached [680506].
[680506] Exited (possibly normal), status[255]
 [sfo] === spawning!
[] Attempting to spawn a monitored task.
[SFUZZ-ORACLE] attached [680507].
[680507] Exited (possibly normal), status[255]
 [sfo] === spawning!
[] Attempting to spawn a monitored task.
[SFUZZ-ORACLE] attached [680508].
[680508] Exited (possibly normal), status[255]
 [sfo] === spawning!
[] Attempting to spawn a monitored task.
[SFUZZ-ORACLE] attached [680509].
[680509] Exited (possibly normal), status[255]
 [sfo] === spawning!
[] Attempting to spawn a monitored task.
[SFUZZ-ORACLE] attached [680518].
[680518] Exited (possibly normal), status[255]
 [sfo] === spawning!
[] Attempting to spawn a monitored task.
[SFUZZ-ORACLE] attached [680519].
[680519] Exited (possibly normal), status[255]
 [sfo] === spawning!
[] Attempting to spawn a monitored task.
[SFUZZ-ORACLE] attached [680520].
[680520] Exited (possibly normal), status[255]
 [sfo] === spawning!
[] Attempting to spawn a monitored task.
[SFUZZ-ORACLE] attached [680521].
[680521] Exited (possibly normal), status[255]
 [sfo] === spawning!
[] Attempting to spawn a monitored task.
[SFUZZ-ORACLE] attached [680522].
[680522] Exited (possibly normal), status[255]
 [sfo] === spawning!
[] Attempting to spawn a monitored task.
[SFUZZ-ORACLE] attached [680524].
[680524] Exited (possibly normal), status[255]
 [sfo] === spawning!
[] Attempting to spawn a monitored task.
[SFUZZ-ORACLE] attached [680525].
[680525] Exited (possibly normal), status[255]
 [sfo] === spawning!
[] Attempting to spawn a monitored task.
[SFUZZ-ORACLE] attached [680526].
[680526] Exited (possibly normal), status[255]
 [sfo] === spawning!
[] Attempting to spawn a monitored task.
[SFUZZ-ORACLE] attached [680527].
[680527] Exited (possibly normal), status[255]
 [sfo] === spawning!
[] Attempting to spawn a monitored task.
[SFUZZ-ORACLE] attached [680536].
[680536] Exited (possibly normal), status[255]
 [sfo] === spawning!
[] Attempting to spawn a monitored task.
[SFUZZ-ORACLE] attached [680537].
[680537] Exited (possibly normal), status[255]
 [sfo] === spawning!
[] Attempting to spawn a monitored task.
[SFUZZ-ORACLE] attached [68053
```

### `sfuzz -h`

> 官方示例调用：`sfuzz -h`

```text
root@kali:~# sfuzz -h
		Simple Fuzzer
By:	 Aaron Conole
version: 0.7.0
url:	 http://aconole.brad-x.com/programs/sfuzz.html
EMAIL:
[email protected]
Build-prefix: /usr
	-h	 This message.
	-V	 Version information.
networking / output:
	-v	 Verbose output
	-q	 Silent output mode (generally for CLI fuzzing)
	-X	 prints the output in hex
	-b	 Begin fuzzing at the test specified.
	-e	 End testing on failure.
	-t	 Wait time for reading the socket
	-S	 Remote host
	-p	 Port
	-T|-U|-O TCP|UDP|Output mode
	-R	 Refrain from closing connections (ie: "leak" them)
	-f	 Config File
	-L	 Log file
	-n	 Create a new logfile after each fuzz
	-r	 Trim the tailing newline
	-D	 Define a symbol and value (X=y).
	-l	 Only perform literal fuzzing
	-s	 Only perform sequence fuzzing
Updated on: 2026-Aug-25
 Edit this page
set
sharphound
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install sfuzz`，再执行 `sfuzz --version` 2>/dev/null || `sfuzz -V`
- [ ] **2.** **读官方帮助** —— `sfuzz -h`，需要细节时 `man sfuzz`
- [ ] **3.** **在自有靶场跑最小用例** —— 用 `sfuzz -h` 里最简单的那个子命令试一次
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/sfuzz/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/resource-development.md`](../../tools/by-attack/resource-development.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/sfuzz/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/sfuzz/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
