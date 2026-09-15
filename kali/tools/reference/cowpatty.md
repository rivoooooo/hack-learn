# cowpatty

> Brute-force WPA dictionary attack If you are auditing WPA-PSK or WPA2-PSK networks, you can use this tool to identify weak passphrases that were used to generate the PMK. Supply a libpcap capture file that includes the 4-way handshake, a d…

> **功能分类**：无线攻击 ｜ **Kali 包**：`cowpatty` ｜ **官方文档**：<https://www.kali.org/tools/cowpatty/>

## 1. 安装

```bash
sudo apt update
sudo apt install cowpatty
```

| 项目 | 内容 |
|------|------|
| 版本 | 4.8 |
| 架构 | any |
| 可执行命令 | `cowpatty`、`genpmk` |
| 依赖 | `libc6`、`libpcap0.8t64`、`libssl3t64` |
| 安装体积 | 73 KB |
| 官网 | <https://www.willhackforsushi.com/?page_id=50> |
| 源码仓库 | <https://salsa.debian.org/pkg-security-team/cowpatty> |
| 包追踪 | <https://pkg.kali.org/pkg/cowpatty> |

## 2. 官方用法示例

> 以下为 Kali 官方工具页给出的示例与输出原文。

```text
Usage Example
Use the provided dictionary file (-f /usr/share/wordlists/nmap.lst) to generate a hashfile, saving it to a file (-d cowpatty_dict) for the given ESSID (-s securenet):
root@kali:~# genpmk -f /usr/share/wordlists/nmap.lst -d cowpatty_dict -s securenet
genpmk 1.3 - WPA-PSK precomputation attack. \&lt;jwright@hasborg.com\&gt;
File cowpatty_dict does not exist, creating.
key no. 1000: pinkgirl
1641 passphrases tested in 3.60 seconds: 456.00 passphrases/second

cowpatty Usage Example
Use the provided hashfile (-d cowpatty_dict), read the packet capture (-r Kismet-20181113-13-37-00-1.pcapdump), and crack the password for the given ESSID (-s 6F36E6):
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 2 个可执行命令，下面是官方页面内嵌的帮助原文。

### `genpmk`

> 官方示例调用：`genpmk -f /usr/share/wordlists/nmap.lst -d cowpatty_dict -s securenet`

```text
root@kali:~# genpmk -f /usr/share/wordlists/nmap.lst -d cowpatty_dict -s securenet
genpmk 1.3 - WPA-PSK precomputation attack. \&lt;
[email protected]
\&gt;
File cowpatty_dict does not exist, creating.
key no. 1000: pinkgirl
1641 passphrases tested in 3.60 seconds: 456.00 passphrases/second
cowpatty Usage Example
Use the provided hashfile (
-d cowpatty_dict
), read the packet capture (
-r Kismet-20181113-13-37-00-1.pcapdump
), and crack the password for the given ESSID (
-s 6F36E6
):
```

### `cowpatty`

> 官方示例调用：`cowpatty -d cowpatty_dict -r Kismet-20181113-13-37-00-1.pcapdump -s 6F36E6`

```text
root@kali:~# cowpatty -d cowpatty_dict -r Kismet-20181113-13-37-00-1.pcapdump -s 6F36E6
cowpatty 4.8 - WPA-PSK dictionary attack. <
[email protected]
>
Collected all necessary data to mount crack against WPA2/PSK passphrase.
Starting dictionary attack. Please be patient.
The PSK is "12345678".
5 passphrases tested in 0.00 seconds: 50000.00 passphrases/second
```

### `cowpatty -h`

> 官方示例调用：`cowpatty -h`

```text
root@kali:~# cowpatty -h
cowpatty 4.8 - WPA-PSK dictionary attack. <
[email protected]
>
Usage: cowpatty [options]
	-f 	Dictionary file
	-d 	Hash file (genpmk)
	-r 	Packet capture file
	-s 	Network SSID (enclose in quotes if SSID includes spaces)
	-c 	Check for valid 4-way frames, does not crack
	-h 	Print this help information and exit
	-v 	Print verbose information (more -v for more verbosity)
	-V 	Print program version and exit
```

### `genpmk -h`

> 官方示例调用：`genpmk -h`

```text
root@kali:~# genpmk -h
genpmk 1.3 - WPA-PSK precomputation attack. <
[email protected]
>
Usage: genpmk [options]
	-f 	Dictionary file
	-d 	Output hash file
	-s 	Network SSID
	-h 	Print this help information and exit
	-v 	Print verbose information (more -v for more verbosity)
	-V 	Print program version and exit
After precomputing the hash file, run cowpatty with the -d argument.
Learn more with
OffSec
Want to learn more about cowpatty? get access to in-depth training and hands-on labs:
PEN-210: 7.5. Cracking Authentication Hashes: coWPAtty
PEN-210 course
Updated on: 2025-Dec-09
 Edit this page
copy-router-config
crackle
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install cowpatty`，再执行 `cowpatty --version` 2>/dev/null || `cowpatty -V`
- [ ] **2.** **读官方帮助** —— `cowpatty -h`，需要细节时 `man cowpatty`
- [ ] **3.** **在自有靶场跑最小用例** —— 官方给出的调用形式是：`Usage: cowpatty [options]`
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/cowpatty/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- **精讲教程**（含原理、参数详解、靶场实操与输出解读）：[cowpatty](../../tools/tutorials/04-口令攻击/cowpatty.md)
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/credential-access.md`](../../tools/by-attack/credential-access.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/cowpatty/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/cowpatty/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
