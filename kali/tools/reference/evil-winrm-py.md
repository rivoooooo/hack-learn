# evil-winrm-py

> Execute commands on remote Windows machines using WinRM Python-based tool for executing commands on remote Windows machines using the WinRM (Windows Remote Management) protocol. It provides an interactive shell with enhanced features like …

> **功能分类**：通用工具 ｜ **Kali 包**：`evil-winrm-py` ｜ **官方文档**：<https://www.kali.org/tools/evil-winrm-py/>

## 1. 安装

```bash
sudo apt update
sudo apt install evil-winrm-py
```

| 项目 | 内容 |
|------|------|
| 版本 | 1.6.0 |
| 架构 | all |
| 可执行命令 | `evil-winrm-py`、`ewp` |
| 依赖 | `python3`、`python3-kerberos`、`python3-prompt-toolkit`、`python3-pypsrp`、`python3-tqdm` |
| 安装体积 | 133 KB |
| 官网 | <https://github.com/adityatelange/evil-winrm-py> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/evil-winrm-py> |
| 包追踪 | <https://pkg.kali.org/pkg/evil-winrm-py> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
evil-winrm-py -h          # 查看用法
man evil-winrm-py         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 2 个可执行命令，下面是官方页面内嵌的帮助原文。

### `evil-winrm-py`

官方给出的调用示例：`evil-winrm-py -h`

```text
root@kali:~# evil-winrm-py -h
          _ _            _
  _____ _(_| |_____ __ _(_)_ _  _ _ _ __ ___ _ __ _  _
 / -_\ V | | |___\ V  V | | ' \| '_| '  |___| '_ | || |
 \___|\_/|_|_|    \_/\_/|_|_||_|_| |_|_|_|  | .__/\_, |
                                            |_|   |__/  v1.6.0
usage: evil-winrm-py [-h] -i IP [-u USER] [-p PASSWORD] [-H HASH]
                     [--priv-key-pem PRIV_KEY_PEM] [--cert-pem CERT_PEM]
                     [--uri URI] [--ua UA] [--port PORT]
                     [--spn-prefix SPN_PREFIX] [--spn-hostname SPN_HOSTNAME]
                     [-k] [--no-pass] [--ssl] [--log] [--debug] [--no-colors]
                     [--version]
options:
  -h, --help            show this help message and exit
  -i, --ip IP           remote host IP or hostname
  -u, --user USER       username
  -p, --password PASSWORD
                        password
  -H, --hash HASH       nthash
  --priv-key-pem PRIV_KEY_PEM
                        local path to private key PEM file
  --cert-pem CERT_PEM   local path to certificate PEM file
  --uri URI             wsman URI (default: /wsman)
  --ua UA               user agent for the WinRM client (default: "Microsoft WinRM Client")
  --port PORT           remote host port (default 5985)
  --spn-prefix SPN_PREFIX
                        specify spn prefix
  --spn-hostname SPN_HOSTNAME
                        specify spn hostname
  -k, --kerberos        use kerberos authentication
  --no-pass             do not prompt for password
  --ssl                 use ssl
  --log                 log session to file
  --debug               enable debug logging
  --no-colors           disable colors
  --version             show version
For more information about this project, visit https://github.com/adityatelange/evil-winrm-py
For user guide, visit https://github.com/adityatelange/evil-winrm-py/blob/main/docs/usage.md
```

### `ewp`

官方给出的调用示例：`ewp -h`

```text
root@kali:~# ewp -h
          _ _            _
  _____ _(_| |_____ __ _(_)_ _  _ _ _ __ ___ _ __ _  _
 / -_\ V | | |___\ V  V | | ' \| '_| '  |___| '_ | || |
 \___|\_/|_|_|    \_/\_/|_|_||_|_| |_|_|_|  | .__/\_, |
                                            |_|   |__/  v1.6.0
usage: ewp [-h] -i IP [-u USER] [-p PASSWORD] [-H HASH]
           [--priv-key-pem PRIV_KEY_PEM] [--cert-pem CERT_PEM] [--uri URI]
           [--ua UA] [--port PORT] [--spn-prefix SPN_PREFIX]
           [--spn-hostname SPN_HOSTNAME] [-k] [--no-pass] [--ssl] [--log]
           [--debug] [--no-colors] [--version]
options:
  -h, --help            show this help message and exit
  -i, --ip IP           remote host IP or hostname
  -u, --user USER       username
  -p, --password PASSWORD
                        password
  -H, --hash HASH       nthash
  --priv-key-pem PRIV_KEY_PEM
                        local path to private key PEM file
  --cert-pem CERT_PEM   local path to certificate PEM file
  --uri URI             wsman URI (default: /wsman)
  --ua UA               user agent for the WinRM client (default: "Microsoft WinRM Client")
  --port PORT           remote host port (default 5985)
  --spn-prefix SPN_PREFIX
                        specify spn prefix
  --spn-hostname SPN_HOSTNAME
                        specify spn hostname
  -k, --kerberos        use kerberos authentication
  --no-pass             do not prompt for password
  --ssl                 use ssl
  --log                 log session to file
  --debug               enable debug logging
  --no-colors           disable colors
  --version             show version
For more information about this project, visit https://github.com/adityatelange/evil-winrm-py
For user guide, visit https://github.com/adityatelange/evil-winrm-py/blob/main/docs/usage.md
Updated on: 2026-May-25
 Edit this page
ettercap
faraday-cli
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install evil-winrm-py`，再执行 `evil-winrm-py --version` 2>/dev/null || `evil-winrm-py -V`
- [ ] **2.** **读官方帮助** —— `evil-winrm-py -h`，需要细节时 `man evil-winrm-py`
- [ ] **3.** **在自有靶场跑最小用例** —— 用 `evil-winrm-py -h` 里最简单的那个子命令试一次
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/evil-winrm-py/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- **精讲教程**（含原理、参数详解、靶场实操与输出解读）：[evil-winrm](../../tools/tutorials/08-后渗透/evil-winrm.md)
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/defense-evasion.md`](../../tools/by-attack/defense-evasion.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/evil-winrm-py/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/evil-winrm-py/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
