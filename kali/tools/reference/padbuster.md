# padbuster

> Script for performing Padding Oracle attacks PadBuster is a Perl script for automating Padding Oracle Attacks. PadBuster provides the capability to decrypt arbitrary ciphertext, encrypt arbitrary plaintext, and perform automated response a…

> **功能分类**：Web 应用 ｜ **Kali 包**：`padbuster` ｜ **官方文档**：<https://www.kali.org/tools/padbuster/>

## 1. 安装

```bash
sudo apt update
sudo apt install padbuster
```

| 项目 | 内容 |
|------|------|
| 版本 | 0.3.3 |
| 架构 | all |
| 可执行命令 | `padbuster` |
| 依赖 | `libcompress-raw-zlib-perl`、`libcrypt-ssleay-perl`、`libnet-ssleay-perl`、`libwww-perl`、`perl` |
| 安装体积 | 40 KB |
| 官网 | <https://github.com/GDSSecurity/PadBuster> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/padbuster> |
| 包追踪 | <https://pkg.kali.org/pkg/padbuster> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
padbuster -h          # 查看用法
man padbuster         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `padbuster`

> 官方示例调用：`padbuster -h`

```text
root@kali:~# padbuster -h
Possible precedence problem between ! and string eq at /usr/bin/padbuster line 677.
Option headers requires an argument
    Use: padbuster URL EncryptedSample BlockSize [options]
  Where: URL = The target URL (and query string if applicable)
         EncryptedSample = The encrypted value you want to test. Must
                           also be present in the URL, PostData or a Cookie
         BlockSize = The block size being used by the algorithm
Options:
	 -auth [username:password]: HTTP Basic Authentication
	 -bruteforce: Perform brute force against the first block
	 -ciphertext [Bytes]: CipherText for Intermediate Bytes (Hex-Encoded)
         -cookies [HTTP Cookies]: Cookies (name1=value1; name2=value2)
         -encoding [0-4]: Encoding Format of Sample (Default 0)
                          0=Base64, 1=Lower HEX, 2=Upper HEX
                          3=.NET UrlToken, 4=WebSafe Base64
         -encodedtext [Encoded String]: Data to Encrypt (Encoded)
         -error [Error String]: Padding Error Message
         -headers [HTTP Headers]: Custom Headers (name1::value1;name2::value2)
	 -interactive: Prompt for confirmation on decrypted bytes
	 -intermediate [Bytes]: Intermediate Bytes for CipherText (Hex-Encoded)
	 -log: Generate log files (creates folder PadBuster.DDMMYY)
	 -noencode: Do not URL-encode the payload (encoded by default)
	 -noiv: Sample does not include IV (decrypt first block)
         -plaintext [String]: Plain-Text to Encrypt
         -post [Post Data]: HTTP Post Data String
	 -prefix [Prefix]: Prefix bytes to append to each sample (Encoded)
	 -proxy [address:port]: Use HTTP/S Proxy
	 -proxyauth [username:password]: Proxy Authentication
	 -resume [Block Number]: Resume at this block number
	 -usebody: Use response body content for response analysis phase
         -verbose: Be Verbose
         -veryverbose: Be Very Verbose (Debug Only)
Updated on: 2026-Aug-25
 Edit this page
pacu
patator
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install padbuster`，再执行 `padbuster --version` 2>/dev/null || `padbuster -V`
- [ ] **2.** **读官方帮助** —— `padbuster -h`，需要细节时 `man padbuster`
- [ ] **3.** **在自有靶场跑最小用例** —— 用 `padbuster -h` 里最简单的那个子命令试一次
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/padbuster/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/defense-evasion.md`](../../tools/by-attack/defense-evasion.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/padbuster/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/padbuster/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
