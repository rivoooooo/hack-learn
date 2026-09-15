# bruteforce-salted-openssl

> Try to find the passphrase for files encrypted with OpenSSL bruteforce-salted-openssl try to find the passphrase or password of a file that was encrypted with the openssl command. It can be used in two ways: - Try all possible passwords gi…

> **功能分类**：通用工具 ｜ **Kali 包**：`bruteforce-salted-openssl` ｜ **官方文档**：<https://www.kali.org/tools/bruteforce-salted-openssl/>

## 1. 安装

```bash
sudo apt update
sudo apt install bruteforce-salted-openssl
```

| 项目 | 内容 |
|------|------|
| 版本 | 1.5.0 |
| 架构 | any |
| 可执行命令 | `bruteforce-salted-openssl` |
| 依赖 | `libc6`、`libssl3t64` |
| 安装体积 | 57 KB |
| 官网 | <https://github.com/glv2/bruteforce-salted-openssl> |
| 源码仓库 | <https://salsa.debian.org/pkg-security-team/bruteforce-salted-openssl> |
| 包追踪 | <https://pkg.kali.org/pkg/bruteforce-salted-openssl> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
bruteforce-salted-openssl -h          # 查看用法
man bruteforce-salted-openssl         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `bruteforce-salted-openssl`

> 官方示例调用：`bruteforce-salted-openssl --help`

```text
root@kali:~# bruteforce-salted-openssl --help
bruteforce-salted-openssl 1.5.0
Usage: bruteforce-salted-openssl [options] <filename>
Options:
  -1           Stop the program after finding the first password candidate.
  -a           List the available cipher and digest algorithms.
  -B <file>    Search using binary passwords (instead of character passwords).
               Write candidates to <file>.
  -b <string>  Beginning of the password.
                 default: ""
  -c <cipher>  Cipher for decryption.
                 default: aes-256-cbc
  -D           Display salt, key and iv along with the tested password.
  -d <digest>  Digest for key and initialization vector generation.
                 default: sha256
  -e <string>  End of the password.
                 default: ""
  -f <file>    Read the passwords from a file instead of generating them.
  -h           Show help and quit.
  -i <n>       With -K, set the PBKDF2 iteration count to <n>.
                 default: 10000
  -K           Use PKCS5_PBKDF2_HMAC to derive the key.
  -L <n>       Limit the maximum number of tested passwords to <n>.
  -l <length>  Minimum password length (beginning and end included).
                 default: 1
  -M <string>  Consider the decryption as successful when the data starts
               with <string>. Without this option, the decryption is considered
               as successful when the data contains mostly printable ASCII
               characters (at least 90%).
  -m <length>  Maximum password length (beginning and end included).
                 default: 8
  -N           Ignore decryption errors (similar to openssl -nopad).
  -n           Ignore salt (similar to openssl -nosalt).
  -p <n>       Preview and check the first N decrypted bytes for the magic string.
               If the magic string is present, try decrypting the rest of the data.
                 default: 1024
  -s <string>  Password character set.
               default: "0123456789ABCDEFGHIJKLMNOPQRSTU
                         VWXYZabcdefghijklmnopqrstuvwxyz"
  -t <n>       Number of threads to use.
                 default: 1
  -v <n>       Print progress info every n seconds.
  -w <file>    Restore the state of a previous session if the file exists,
               then write the state to the file regularly (~ every minute).
Sending a USR1 signal to a running bruteforce-salted-openssl process
makes it print progress info to standard error and continue.
Error: unknown option: '-'.
Updated on: 2026-Mar-02
 Edit this page
blueranger
bytecode-viewer
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install bruteforce-salted-openssl`，再执行 `bruteforce-salted-openssl --version` 2>/dev/null || `bruteforce-salted-openssl -V`
- [ ] **2.** **读官方帮助** —— `bruteforce-salted-openssl -h`，需要细节时 `man bruteforce-salted-openssl`
- [ ] **3.** **在自有靶场跑最小用例** —— 官方给出的调用形式是：`Usage: bruteforce-salted-openssl [options] <filename>`
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/bruteforce-salted-openssl/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/bruteforce-salted-openssl/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/bruteforce-salted-openssl/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
