# Kali 工具精讲教程

共 **108** 篇工具教程，按攻击阶段组织。每篇包含：解决什么问题 → 工作原理 → 参数详解 → 靶场实操 → 输出解读 → 常见坑 → 防御视角。

> ⚠️ 所有实操步骤仅适用于**你自己的靶场或获得授权的目标**。

## 教程统计

| 阶段 | 目录 | 篇数 | 说明 |
|------|------|------|------|
| 信息搜集 | [01-信息搜集/](01-信息搜集/) | 16 | 被动/主动侦察：端口、服务、DNS、OSINT、SMB 枚举 |
| 漏洞分析 | [02-漏洞分析/](02-漏洞分析/) | 11 | 漏洞扫描、模糊测试与应用安全检测 |
| Web 应用 | [03-Web应用/](03-Web应用/) | 10 | Web 代理、目录爆破、注入与 Web 漏洞利用 |
| 口令攻击 | [04-口令攻击/](04-口令攻击/) | 13 | 在线爆破、离线破解、字典生成 |
| 无线攻击 | [05-无线攻击/](05-无线攻击/) | 8 | Wi-Fi 监听、握手抓取与破解 |
| 漏洞利用 | [06-漏洞利用/](06-漏洞利用/) | 5 | EXP 框架、Payload 生成与投递 |
| 嗅探与欺骗 | [07-嗅探与欺骗/](07-嗅探与欺骗/) | 7 | 流量抓取、中间人与名称解析投毒 |
| 后渗透 | [08-后渗透/](08-后渗透/) | 13 | 提权、凭据获取、横向移动与隧道 |
| 数字取证 | [09-数字取证/](09-数字取证/) | 10 | 磁盘/内存/文件取证与证据分析 |
| 逆向工程 | [10-逆向工程/](10-逆向工程/) | 7 | 反汇编、调试与二进制分析 |
| 社会工程与报告 | [11-社会工程与报告/](11-社会工程与报告/) | 4 | 钓鱼演练与测试报告输出 |
| 基础设施与 C2 | [12-基础设施与C2/](12-基础设施与C2/) | 4 | C2 框架、重定向器与 Payload 托管 |

## 怎么用

1. **零基础**：按上表顺序从上往下读（01 → 12），对应一次渗透测试的自然流程。
2. **补工具**：直接按工具名找对应的分类目录。
3. **查参数**：每个教程的「核心参数详解」一节可直接当速查表用。
4. **没写到的工具**：本目录只精讲重点工具；全部 780 个工具包的卡片在
   [`../catalog/`](../catalog/) 与 [`../by-attack/`](../by-attack/)，
   每张卡片含包名、命令、依赖、安装命令与官方文档链接。

## 官方重点工具覆盖情况

Kali 官网 [Top 100 工具](<https://www.kali.org/tools/top-100/>) 页面收录了 **44** 个重点包。本目录的教程覆盖情况（脚本自动比对）：

**44 / 44** 个已有深度教程。

| 包 | 说明 | 本库教程 |
|----|------|----------|
| `aircrack-ng` | Wireless WEP/WPA cracking utilities aircrack-ng is an 802.11a/b/g WEP/… | [aircrack-ng](05-无线攻击/aircrack-ng.md) |
| `beef-xss` | Browser Exploitation Framework (BeEF) BeEF is short for The Browser Ex… | [beef-xss](06-漏洞利用/beef-xss.md) |
| `binwalk` | Tool library for analyzing binary blobs and executable code Binwalk is… | [binwalk](09-数字取证/binwalk.md) |
| `bloodhound` | Six Degrees of Domain Admin, BloodHound CE This package contains Blood… | [bloodhound](08-后渗透/bloodhound.md) |
| `bulk-extractor` | Extracts information without parsing filesystem bulk_extractor is a C+… | [bulk-extractor](09-数字取证/bulk-extractor.md) |
| `cewl` | Custom word list generator CeWL (Custom Word List generator) is a ruby… | [cewl](04-口令攻击/cewl.md) |
| `cowpatty` | Brute-force WPA dictionary attack If you are auditing WPA-PSK or WPA2-… | [cowpatty](04-口令攻击/cowpatty.md) |
| `crackmapexec` | Swiss army knife for pentesting networks This package is a swiss army … | [crackmapexec](08-后渗透/crackmapexec.md) |
| `dex2jar` | Tools to work with android .dex and java .class files dex2jar contains… | [dex2jar](10-逆向工程/dex2jar.md) |
| `dirb` | URL bruteforcing tool DIRB is a Web Content Scanner. It looks for exis… | [dirb](03-Web应用/dirb.md) |
| `dvwa` | Damn Vulnerable Web Application This package contains a PHP/MySQL web … | [dvwa](03-Web应用/dvwa.md) |
| `ettercap` | Multipurpose sniffer/content filter for man in the middle attacks root… | [ettercap](07-嗅探与欺骗/ettercap.md) |
| `exploitdb` | Searchable Exploit Database archive Searchable archive from The Exploi… | [searchsploit](02-漏洞分析/searchsploit.md) |
| `gophish` | Open-Source Phishing Toolkit This package contains an open-source phis… | [gophish](11-社会工程与报告/gophish.md) |
| `hashcat` | World’s fastest and most advanced password recovery utility Hashcat su… | [hashcat](04-口令攻击/hashcat.md) |
| `hexstrike-ai` | AI-Powered MCP Cybersecurity Automation Platform This package contains… | [hexstrike-ai](12-基础设施与C2/hexstrike-ai.md) |
| `hydra` | Very fast network logon cracker Hydra is a parallelized login cracker … | [hydra](04-口令攻击/hydra.md) |
| `impacket-scripts` | Links to useful impacket scripts examples This package contains links … | [impacket](08-后渗透/impacket.md) |
| `john` | Active password cracking tool John the Ripper is a tool designed to he… | [john](04-口令攻击/john.md) |
| `kismet` | Wireless network and device detector (metapackage) Kismet is a wireles… | [kismet](05-无线攻击/kismet.md) |
| `ligolo-ng` | Advanced, yet simple, tunneling/pivoting tool that uses a TUN interfac… | [ligolo-ng](08-后渗透/ligolo-ng.md) |
| `metasploit-framework` | Framework for exploit development and vulnerability research The Metas… | [metasploit-framework](06-漏洞利用/metasploit-framework.md) |
| `netcat` | TCP/IP swiss army knife A simple Unix utility which reads and writes d… | [netcat](06-漏洞利用/netcat.md) |
| `netexec` | Network Execution Tool NetExec (AKA nxc) is a network service exploita… | [netexec](08-后渗透/netexec.md) |
| `nikto` | Web server security scanner Nikto is a pluggable web server and CGI sc… | [nikto](02-漏洞分析/nikto.md) |
| `nmap` | The Network Mapper Nmap is a utility for network exploration or securi… | [nmap](01-信息搜集/nmap.md) |
| `powershell` | PowerShell is an automation and configuration management platform. It … | [powershell-empire](08-后渗透/powershell-empire.md) |
| `rainbowcrack` | Rainbow table password cracker RainbowCrack is a general propose imple… | [rainbowcrack](04-口令攻击/rainbowcrack.md) |
| `reaver` | Brute force attack tool against Wi-Fi Protected Setup PIN number Reave… | [reaver](05-无线攻击/reaver.md) |
| `recon-ng` | Web Reconnaissance framework written in Python Recon-ng is a full-feat… | [recon-ng](01-信息搜集/recon-ng.md) |
| `responder` | LLMNR/NBT-NS/mDNS Poisoner This package contains Responder/MultiRelay,… | [responder](07-嗅探与欺骗/responder.md) |
| `scapy` | Interactive packet manipulation tool root@kali:~# scapy -h Usage: scap… | [scapy](07-嗅探与欺骗/scapy.md) |
| `sliver` | Implant framework This package contains a general purpose cross-platfo… | [sliver](12-基础设施与C2/sliver.md) |
| `snort` | Flexible Network Intrusion Detection System Snort is a libpcap-based p… | [snort](02-漏洞分析/snort.md) |
| `spiderfoot` | OSINT collection and reconnaissance tool This package contains an open… | [spiderfoot](01-信息搜集/spiderfoot.md) |
| `sqlmap` | Automatic SQL injection tool sqlmap goal is to detect and take advanta… | [sqlmap](03-Web应用/sqlmap.md) |
| `steghide` | Steganography hiding tool Steghide is steganography program which hide… | [steghide](09-数字取证/steghide.md) |
| `testdisk` | Partition scanner and disk recovery tool TestDisk checks the partition… | [testdisk](09-数字取证/testdisk.md) |
| `theharvester` | Tool for gathering e-mail accounts and subdomain names from public sou… | [theharvester](01-信息搜集/theharvester.md) |
| `tiger` | Security auditing and intrusion detection tools for Linux TIGER, or th… | [tiger](02-漏洞分析/tiger.md) |
| `web-cache-vulnerability-scanner` | Go-based CLI tool for testing for web cache poisoning Web Cache Vulner… | [web-cache-vulnerability-scanner](02-漏洞分析/web-cache-vulnerability-scanner.md) |
| `wireshark` | Network traffic analyzer - graphical interface Wireshark is a network … | [wireshark](07-嗅探与欺骗/wireshark.md) |
| `yara` | Pattern matching swiss knife for malware researchers YARA is a tool ai… | [yara](02-漏洞分析/yara.md) |
| `zaproxy` | Testing tool for finding vulnerabilities in web applications The OWASP… | [zaproxy](03-Web应用/zaproxy.md) |

> 没有教程的包并非没有收录——它们在 [`../catalog/`](../catalog/) 里有完整卡片（包名、命令、依赖、安装方式、官方链接）。

## 工具清单

### 信息搜集（[01-信息搜集/](01-信息搜集/)）

被动/主动侦察：端口、服务、DNS、OSINT、SMB 枚举

| 教程 | 内容 |
|------|------|
| [amass](01-信息搜集/amass.md) | amass（OWASP 攻击面测绘与资产发现） |
| [arp-scan](01-信息搜集/arp-scan.md) | arp-scan（二层 ARP 主机发现与网卡指纹） |
| [dnsenum](01-信息搜集/dnsenum.md) | dnsenum（多线程 DNS 信息枚举与非连续网段发现） |
| [dnsrecon](01-信息搜集/dnsrecon.md) | dnsrecon（DNS 枚举与域传输检测） |
| [enum4linux](01-信息搜集/enum4linux.md) | enum4linux（Windows / Samba 枚举的瑞士军刀） |
| [fierce](01-信息搜集/fierce.md) | fierce（轻量 DNS 扫描与非连续 IP 空间发现） |
| [hping3](01-信息搜集/hping3.md) | hping3（自定义 TCP/IP 数据包构造与发送） |
| [masscan](01-信息搜集/masscan.md) | masscan（互联网级高速端口扫描） |
| [nbtscan](01-信息搜集/nbtscan.md) | nbtscan（NetBIOS 名字表扫描） |
| [netdiscover](01-信息搜集/netdiscover.md) | netdiscover（主动／被动 ARP 侦察） |
| [nmap](01-信息搜集/nmap.md) | nmap（端口扫描与资产测绘的基准工具） |
| [recon-ng](01-信息搜集/recon-ng.md) | recon-ng（模块化 Web 侦察框架） |
| [smbclient](01-信息搜集/smbclient.md) | smbclient（SMB/CIFS 共享访问客户端） |
| [spiderfoot](01-信息搜集/spiderfoot.md) | spiderfoot（OSINT 自动化与攻击面测绘） |
| [theharvester](01-信息搜集/theharvester.md) | theHarvester（OSINT 收集：邮箱、子域、主机与员工信息） |
| [whatweb](01-信息搜集/whatweb.md) | whatweb（Web 指纹识别） |

### 漏洞分析（[02-漏洞分析/](02-漏洞分析/)）

漏洞扫描、模糊测试与应用安全检测

| 教程 | 内容 |
|------|------|
| [fping](02-漏洞分析/fping.md) | fping（批量 ICMP 存活探测） |
| [ike-scan](02-漏洞分析/ike-scan.md) | ike-scan（IPsec VPN / IKE 服务发现与指纹） |
| [lynis](02-漏洞分析/lynis.md) | lynis（Unix/Linux 系统安全审计） |
| [nikto](02-漏洞分析/nikto.md) | nikto（Web 服务器漏洞扫描） |
| [nuclei](02-漏洞分析/nuclei.md) | nuclei（基于模板的漏洞扫描器） |
| [openssl](02-漏洞分析/openssl.md) | openssl（TLS/SSL 诊断与证书分析） |
| [searchsploit](02-漏洞分析/searchsploit.md) | searchsploit（本地 Exploit-DB 检索） |
| [snort](02-漏洞分析/snort.md) | snort（网络入侵检测 / 防御系统） |
| [tiger](02-漏洞分析/tiger.md) | tiger（Linux 主机安全审计与 HIDS） |
| [web-cache-vulnerability-scanner](02-漏洞分析/web-cache-vulnerability-scanner.md) | web-cache-vulnerability-scanner（Web 缓存投毒 / 缓存欺骗扫描） |
| [yara](02-漏洞分析/yara.md) | yara（恶意样本模式匹配） |

### Web 应用（[03-Web应用/](03-Web应用/)）

Web 代理、目录爆破、注入与 Web 漏洞利用

| 教程 | 内容 |
|------|------|
| [commix](03-Web应用/commix.md) | commix（自动化 OS 命令注入检测与利用） |
| [dirb](03-Web应用/dirb.md) | dirb（经典 Web 目录爆破） |
| [dvwa](03-Web应用/dvwa.md) | dvwa（Damn Vulnerable Web Application：Web 漏洞靶场） |
| [ffuf](03-Web应用/ffuf.md) | ffuf（快速 Web Fuzzer） |
| [gobuster](03-Web应用/gobuster.md) | gobuster（目录、DNS 与虚拟主机爆破） |
| [sqlmap](03-Web应用/sqlmap.md) | sqlmap（自动化 SQL 注入检测与利用） |
| [wafw00f](03-Web应用/wafw00f.md) | wafw00f（Web 应用防火墙指纹识别） |
| [wfuzz](03-Web应用/wfuzz.md) | wfuzz（Web 模糊测试与爆破框架） |
| [wpscan](03-Web应用/wpscan.md) | wpscan（WordPress 黑盒漏洞扫描） |
| [zaproxy](03-Web应用/zaproxy.md) | zaproxy（OWASP ZAP：Web 应用安全测试代理） |

### 口令攻击（[04-口令攻击/](04-口令攻击/)）

在线爆破、离线破解、字典生成

| 教程 | 内容 |
|------|------|
| [cewl](04-口令攻击/cewl.md) | CeWL（网站词汇爬取字典生成器） |
| [cowpatty](04-口令攻击/cowpatty.md) | cowpatty（WPA/WPA2-PSK 离线字典攻击） |
| [crunch](04-口令攻击/crunch.md) | crunch（字典生成器） |
| [hash-identifier](04-口令攻击/hash-identifier.md) | hash-identifier（哈希类型识别） |
| [hashcat](04-口令攻击/hashcat.md) | hashcat（GPU 加速哈希破解器） |
| [hydra](04-口令攻击/hydra.md) | hydra（在线登录爆破器） |
| [john](04-口令攻击/john.md) | John the Ripper（离线哈希破解器） |
| [medusa](04-口令攻击/medusa.md) | medusa（并行模块化登录爆破器） |
| [ncrack](04-口令攻击/ncrack.md) | ncrack（Nmap 风格的网络认证爆破器） |
| [ophcrack](04-口令攻击/ophcrack.md) | Ophcrack（彩虹表 Windows 口令破解器） |
| [patator](04-口令攻击/patator.md) | patator（模块化万能爆破框架） |
| [rainbowcrack](04-口令攻击/rainbowcrack.md) | rainbowcrack（彩虹表：时间-内存权衡破解） |
| [wordlists](04-口令攻击/wordlists.md) | wordlists / SecLists（Kali 字典库） |

### 无线攻击（[05-无线攻击/](05-无线攻击/)）

Wi-Fi 监听、握手抓取与破解

| 教程 | 内容 |
|------|------|
| [aircrack-ng](05-无线攻击/aircrack-ng.md) | aircrack-ng（无线审计套件总览） |
| [aireplay-ng](05-无线攻击/aireplay-ng.md) | aireplay-ng（802.11 帧注入与攻击） |
| [airmon-ng](05-无线攻击/airmon-ng.md) | airmon-ng（无线网卡监听模式管理） |
| [airodump-ng](05-无线攻击/airodump-ng.md) | airodump-ng（802.11 抓包与侦察） |
| [bettercap](05-无线攻击/bettercap.md) | bettercap（模块化 MITM 与无线侦察框架） |
| [kismet](05-无线攻击/kismet.md) | Kismet（无线网络侦测与 WIDS） |
| [reaver](05-无线攻击/reaver.md) | Reaver（WPS PIN 攻击） |
| [wifite](05-无线攻击/wifite.md) | Wifite2（无线审计自动化） |

### 漏洞利用（[06-漏洞利用/](06-漏洞利用/)）

EXP 框架、Payload 生成与投递

| 教程 | 内容 |
|------|------|
| [beef-xss](06-漏洞利用/beef-xss.md) | BeEF（浏览器利用框架） |
| [metasploit-framework](06-漏洞利用/metasploit-framework.md) | Metasploit Framework（漏洞利用框架） |
| [msfvenom](06-漏洞利用/msfvenom.md) | msfvenom（Payload 生成器） |
| [netcat](06-漏洞利用/netcat.md) | netcat（TCP/IP 瑞士军刀） |
| [searchsploit](06-漏洞利用/searchsploit.md) | searchsploit（Exploit-DB 本地检索） |

### 嗅探与欺骗（[07-嗅探与欺骗/](07-嗅探与欺骗/)）

流量抓取、中间人与名称解析投毒

| 教程 | 内容 |
|------|------|
| [ettercap](07-嗅探与欺骗/ettercap.md) | Ettercap（交换网络嗅探与 MITM） |
| [macchanger](07-嗅探与欺骗/macchanger.md) | MAC changer（网卡 MAC 地址修改） |
| [mitmproxy](07-嗅探与欺骗/mitmproxy.md) | mitmproxy（HTTP/HTTPS 中间人代理） |
| [responder](07-嗅探与欺骗/responder.md) | Responder（名称解析投毒与凭据捕获） |
| [scapy](07-嗅探与欺骗/scapy.md) | scapy（Python 数据包构造与嗅探） |
| [tcpdump](07-嗅探与欺骗/tcpdump.md) | tcpdump（命令行抓包） |
| [wireshark](07-嗅探与欺骗/wireshark.md) | Wireshark / tshark（网络协议分析） |

### 后渗透（[08-后渗透/](08-后渗透/)）

提权、凭据获取、横向移动与隧道

| 教程 | 内容 |
|------|------|
| [bloodhound](08-后渗透/bloodhound.md) | BloodHound CE（AD 攻击路径图谱） |
| [chisel](08-后渗透/chisel.md) | Chisel（HTTP 隧道 / 内网穿透） |
| [crackmapexec](08-后渗透/crackmapexec.md) | CrackMapExec（Windows/AD 批量评估「瑞士军刀」） |
| [evil-winrm](08-后渗透/evil-winrm.md) | Evil-WinRM（WinRM 交互式 Shell） |
| [impacket](08-后渗透/impacket.md) | Impacket（Windows 协议攻击工具箱） |
| [ligolo-ng](08-后渗透/ligolo-ng.md) | Ligolo-ng（TUN 隧道 / 内网路由穿透） |
| [linpeas](08-后渗透/linpeas.md) | LinPEAS / WinPEAS（PEASS-ng 提权枚举套件） |
| [linux-exploit-suggester](08-后渗透/linux-exploit-suggester.md) | Linux Exploit Suggester（LES，Linux 内核漏洞匹配） |
| [mimikatz](08-后渗透/mimikatz.md) | Mimikatz（Windows 凭据提取利器） |
| [netexec](08-后渗透/netexec.md) | NetExec（NetExec / `nxc`，CrackMapExec 的官方后继） |
| [powershell-empire](08-后渗透/powershell-empire.md) | PowerShell Empire（PowerShell / Python 后渗透代理框架） |
| [proxychains4](08-后渗透/proxychains4.md) | Proxychains4（把任意 TCP 工具塞进代理链） |
| [weevely](08-后渗透/weevely.md) | Weevely（PHP 隐蔽 WebShell 与后利用框架） |

### 数字取证（[09-数字取证/](09-数字取证/)）

磁盘/内存/文件取证与证据分析

| 教程 | 内容 |
|------|------|
| [autopsy](09-数字取证/autopsy.md) | Autopsy（Sleuth Kit 图形化取证界面） |
| [binwalk](09-数字取证/binwalk.md) | binwalk（二进制/固件结构分析） |
| [bulk-extractor](09-数字取证/bulk-extractor.md) | bulk_extractor（无文件系统解析的特征提取） |
| [dcfldd](09-数字取证/dcfldd.md) | dcfldd（取证级磁盘镜像获取） |
| [exiftool](09-数字取证/exiftool.md) | ExifTool（元数据读取与写入） |
| [foremost](09-数字取证/foremost.md) | Foremost（文件雕刻 / File Carving） |
| [scalpel](09-数字取证/scalpel.md) | Scalpel（高速文件雕刻） |
| [sleuthkit](09-数字取证/sleuthkit.md) | The Sleuth Kit（TSK，文件系统取证命令行套件） |
| [steghide](09-数字取证/steghide.md) | steghide（隐写：把数据藏进图片和音频） |
| [testdisk](09-数字取证/testdisk.md) | testdisk（分区恢复 / PhotoRec 文件雕刻） |

### 逆向工程（[10-逆向工程/](10-逆向工程/)）

反汇编、调试与二进制分析

| 教程 | 内容 |
|------|------|
| [dex2jar](10-逆向工程/dex2jar.md) | dex2jar（Android dex ↔ jar / smali 转换工具集） |
| [gdb](10-逆向工程/gdb.md) | GDB（GNU 调试器） |
| [ghidra](10-逆向工程/ghidra.md) | Ghidra（软件逆向工程框架 / 反编译器） |
| [ltrace](10-逆向工程/ltrace.md) | ltrace（库函数调用跟踪） |
| [objdump](10-逆向工程/objdump.md) | objdump（反汇编与目标文件分析） |
| [radare2](10-逆向工程/radare2.md) | Radare2（逆向工程框架） |
| [rizin](10-逆向工程/rizin.md) | Rizin（radare2 社区分叉 · 含 Cutter 图形界面） |

### 社会工程与报告（[11-社会工程与报告/](11-社会工程与报告/)）

钓鱼演练与测试报告输出

| 教程 | 内容 |
|------|------|
| [cherrytree](11-社会工程与报告/cherrytree.md) | CherryTree（层级笔记 / 报告草稿） |
| [dradis](11-社会工程与报告/dradis.md) | Dradis（协作式渗透测试报告平台） |
| [gophish](11-社会工程与报告/gophish.md) | Gophish（钓鱼演练平台） |
| [set](11-社会工程与报告/set.md) | SET（Social-Engineer Toolkit，社工攻击工具包） |

### 基础设施与 C2（[12-基础设施与C2/](12-基础设施与C2/)）

C2 框架、重定向器与 Payload 托管

| 教程 | 内容 |
|------|------|
| [apache2](12-基础设施与C2/apache2.md) | Apache HTTP Server（重定向器与 Payload 托管） |
| [hexstrike-ai](12-基础设施与C2/hexstrike-ai.md) | hexstrike-ai（AI 驱动的安全工具编排 / MCP 平台） |
| [sliver](12-基础设施与C2/sliver.md) | Sliver（现代化 C2 / 植入体框架） |
| [socat](12-基础设施与C2/socat.md) | socat（万能中继 / 重定向器） |

## 相关

- [工具总览](../index.md) —— 按攻击阶段与按包两种查法
- [按包速查卡片](../catalog/all-tools.md) —— 全量 780 个包
- [靶场搭建](../../labs/README.md) —— 练习环境
- [Kali 官方文档精读](../../docs/) —— 系统层知识
