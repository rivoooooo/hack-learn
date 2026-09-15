# truecrack

> Bruteforce password cracker for TrueCrypt volumes TrueCrack is a bruteforce password cracker for TrueCrypt (Copyright) volume. It is optimazed with Nvidia Cuda technology. It works with PBKDF2 (defined in PKCS5 v2.0) based on RIPEMD160 Key…

> **功能分类**：口令攻击 ｜ **Kali 包**：`truecrack` ｜ **官方文档**：<https://www.kali.org/tools/truecrack/>

## 1. 安装

```bash
sudo apt update
sudo apt install truecrack
```

| 项目 | 内容 |
|------|------|
| 版本 | 3.6 |
| 架构 | any |
| 可执行命令 | `truecrack` |
| 依赖 | `libc6` |
| 安装体积 | 2.61 MB |
| 官网 | <https://github.com/lvaccaro/truecrack> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/truecrack> |
| 包追踪 | <https://pkg.kali.org/pkg/truecrack> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
truecrack -h          # 查看用法
man truecrack         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `truecrack`

官方给出的调用示例：`truecrack -t truecrypt_vol -k ripemd160 -w passes.txt`

```text
root@kali:~# truecrack -t truecrypt_vol -k ripemd160 -w passes.txt
TrueCrack v3.0
Website: http://code.google.com/p/truecrack
Contact us:
[email protected]
Found password:     "s3cr3t"
Password length:    "7"
Total computations: "78"
```

### `truecrack（示例）`

官方给出的调用示例：`truecrack -h`

```text
root@kali:~# truecrack -h
TrueCrack v3.6
Website: https://github.com/lvaccaro/truecrack
Contact us:
[email protected]
Bruteforce password cracker for Truecrypt volume. Optimazed with Nvidia Cuda technology.
Based on TrueCrypt, freely available at http://www.truecrypt.org/
Copyright (c) 2011 by Luca Vaccaro.
Usage for Dictionary attack:
 truecrack -t truecrypt_file -w passwords_file [-k ripemd160 | -k sha512 | -k whirlpool] [-e aes | -e serpent | -e twofish] [-a blocks] [-b] [-H] [-r number]
Usage for Alphabet attack:
 truecrack -t truecrypt_file -c alphabet [-s minlength] -m maxlength [-p string] [-k ripemd160 | -k sha512 | -k whirlpool] [-e aes | -e serpent | -e twofish] [-a blocks] [-b] [-H] [-r number]
Options:
 -h --help					Display this information.
 -t --truecrypt <truecrypt_file>		Truecrypt volume file.
 -k --key <ripemd160 | sha512 | whirlpool>	Key derivation function (default ripemd160).
 -e --encryption <aes | serpent | twofish>	Encryption algorithm (default aes).
 -a --aggressive <blocks>			Number of parallel computations (board dependent).
 -w --wordlist <wordlist_file>			File of words, for Dictionary attack.
 -c --charset <alphabet>			Alphabet generator, for Alphabet attack.
 -s --startlength <minlength>			Starting length of passwords, for Alphabet attack (default 1).
 -m --maxlength <maxlength>			Maximum length of passwords, for Alphabet attack.
 -p --prefix <string>				Prefix the first part of the password, for Alphabet attack.
 -r --restore <number>				Restore the computation.
 -b --backup					Backup header instead of volume header.
 -H --hidden					Hidden Truecrypt volume.
 -v --verbose					Show computation messages.
Sample for Dictionary attack:
 truecrack -t volume.tc -w dictionary.txt
Sample for Alphabet attack:
 truecrack -t volume.tc -c "1234567890" -s 4 -m 6
Updated on: 2026-Mar-02
 Edit this page
tnscmd10g
whois
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install truecrack`，再执行 `truecrack --version` 2>/dev/null || `truecrack -V`
- [ ] **2.** **读官方帮助** —— `truecrack -h`，需要细节时 `man truecrack`
- [ ] **3.** **在自有靶场跑最小用例** —— 官方给出的调用形式是：`Usage for Dictionary attack:`
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/truecrack/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/credential-access.md`](../../tools/by-attack/credential-access.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/truecrack/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/truecrack/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
