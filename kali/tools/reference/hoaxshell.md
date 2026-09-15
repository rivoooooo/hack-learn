# hoaxshell

> Windows reverse shell payload generator and handler that abuses http(s) Hoaxshell is a Windows reverse shell payload generator and handler that abuses the http(s) protocol to establish a beacon-like reverse shell

> **功能分类**：通用工具 ｜ **Kali 包**：`hoaxshell` ｜ **官方文档**：<https://www.kali.org/tools/hoaxshell/>

## 1. 安装

```bash
sudo apt update
sudo apt install hoaxshell
```

| 项目 | 内容 |
|------|------|
| 版本 | 0.0~git20250119.e1bba89 |
| 架构 | all |
| 可执行命令 | `hoaxshell` |
| 依赖 | `python3`、`python3-ipython`、`python3-pyperclip` |
| 安装体积 | 84 KB |
| 官网 | <https://github.com/t3l3machus/hoaxshell/> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages//hoaxshell> |
| 包追踪 | <https://pkg.kali.org/pkg/hoaxshell> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
hoaxshell -h          # 查看用法
man hoaxshell         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `hoaxshell`

> 官方示例调用：`hoaxshell -h`

```text
root@kali:~# hoaxshell -h
usage: hoaxshell.py [-h] [-s SERVER_IP] [-c CERTFILE] [-k KEYFILE] [-p PORT]
                    [-f FREQUENCY] [-i] [-H HEADER] [-x EXEC_OUTFILE] [-r]
                    [-o] [-v SERVER_VERSION] [-g] [-t] [-cm] [-lt] [-ng] [-u]
                    [-q]
options:
  -h, --help            show this help message and exit
  -s, --server-ip SERVER_IP
                        Your hoaxshell server ip address or domain.
  -c, --certfile CERTFILE
                        Path to your ssl certificate.
  -k, --keyfile KEYFILE
                        Path to the private key for your certificate.
  -p, --port PORT       Your hoaxshell server port (default: 8080 over http, 443 over https).
  -f, --frequency FREQUENCY
                        Frequency of cmd execution queue cycle (A low value creates a faster shell but produces more http traffic. *Less than 0.8 will cause trouble. default: 0.8s).
  -i, --invoke-restmethod
                        Generate payload using the 'Invoke-RestMethod' instead of the default 'Invoke-WebRequest' utility.
  -H, --Header HEADER   Hoaxshell utilizes a non-standard header to transfer the session id between requests. A random name is given to that header by default. Use this option to set a custom header name.
  -x, --exec-outfile EXEC_OUTFILE
                        Provide a filename (absolute path) on the victim machine to write and execute commands from instead of using "Invoke-Expression". The path better be quoted. Be careful when using special chars in the path (e.g. $env:USERNAME) as they must be properly escaped. See usage examples for details. CAUTION: you won't be able to change directory with this method. Your commands must include ablsolute paths to files etc.
  -r, --raw-payload     Generate raw payload instead of base64 encoded.
  -o, --obfuscate       Obfuscate generated payload.
  -v, --server-version SERVER_VERSION
                        Provide a value for the "Server" response header (default: Microsoft-IIS/10)
  -g, --grab            Attempts to restore a live session (default: false).
  -t, --trusted-domain  If you own a domain, use this option to generate a shorter and less detectable https payload by providing your DN with -s along with a trusted certificate (-c cert.pem -k privkey.pem). See usage examples for more details.
  -cm, --constraint-mode
                        Generate a payload that works even if the victim is configured to run PS in Constraint Language mode. By using this option, you sacrifice a bit of your reverse shell's stdout decoding accuracy.
  -lt, --localtunnel    Generate Payload with localtunnel
  -ng, --ngrok          Generate Payload with Ngrok
  -u, --update          Pull the latest version from the original repo.
  -q, --quiet           Do not print the banner on startup.
Usage examples:
  - Basic shell session over http:
      hoaxshell -s <your_ip>
  - Recommended usage to avoid detection (over http):
     # Hoaxshell utilizes an http header to transfer shell session info. By default, the header is given a random name which can be detected by regex-based AV rules.
     # Use -H to provide a standard or custom http header name to avoid detection.
     hoaxshell -s <your_ip> -i -H "Authorization"
     # The same but with --exec-outfile (-x)
     hoaxshell -s <your_ip> -i -H "Authorization" -x "C:\Users\\\$env:USERNAME\.local\hack.ps1"
  - Encrypted shell session over https with a trusted certificate:
     hoaxshell -s <your.domain.com> -t -c </path/to/cert.pem> -k <path/to/key.pem>
  - Encrypted shell session over https with a self-signed certificate (Not recommended):
     # First you need to generate self-signed certificates:
     openssl req -x509 -newkey rsa:2048 -keyout key.pem -out cert.pem -days 365
     hoaxshell -s <your_ip> -c </path/to/cert.pem> -k <path/to/key.pem>
  - Encrypted shell session with reverse proxy tunneling tools:
     hoaxshell -lt
	 OR
     hoaxshell -ng
Updated on: 2026-May-25
 Edit this page
hashcat
instaloader
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install hoaxshell`，再执行 `hoaxshell --version` 2>/dev/null || `hoaxshell -V`
- [ ] **2.** **读官方帮助** —— `hoaxshell -h`，需要细节时 `man hoaxshell`
- [ ] **3.** **在自有靶场跑最小用例** —— 官方给出的调用形式是：`Usage examples:`
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/hoaxshell/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/command-and-control.md`](../../tools/by-attack/command-and-control.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/hoaxshell/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/hoaxshell/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
