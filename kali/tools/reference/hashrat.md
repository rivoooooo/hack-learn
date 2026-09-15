# hashrat

> Hashing tool supporting several hashes and recursivity Hashrat is a hash-generation utility that supports the md5, sha1, sha256, sha512, whirlpool, jh-244, jh256, jh-384 and jh-512 hash functions, and also the HMAC versions of those functi…

> **功能分类**：事件响应 ｜ **Kali 包**：`hashrat` ｜ **官方文档**：<https://www.kali.org/tools/hashrat/>

## 1. 安装

```bash
sudo apt update
sudo apt install hashrat
```

| 项目 | 内容 |
|------|------|
| 版本 | 1.25 |
| 架构 | any |
| 可执行命令 | `hashrat` |
| 依赖 | `libc6`、`libssl3t64`、`zlib1g` |
| 安装体积 | 513 KB |
| 官网 | <https://github.com/ColumPaget/Hashrat/> |
| 源码仓库 | <https://salsa.debian.org/pkg-security-team/hashrat> |
| 包追踪 | <https://pkg.kali.org/pkg/hashrat> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
hashrat -h          # 查看用法
man hashrat         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `hashrat`

官方给出的调用示例：`hashrat --help`

```text
root@kali:~# hashrat --help
Hashrat: version 1.25
Author: Colum Paget
Email:
[email protected]
Credits:
	Thanks for bug reports/advice to: Stephan Hegel, Michael Shigorin <
[email protected]
> and Joao Eriberto Mota Filho <
[email protected]
>
	Thanks to the people who invented the hash functions!
	MD5: Ronald Rivest
	Whirlpool: Vincent Rijmen, Paulo S. L. M. Barreto
	JH: Hongjun Wu
	SHA: The NSA (thanks, but please stop reading my email. It's kinda creepy.).
	Special thanks to Professor Hongjun Wu for taking the time to confirm that his JH algorithm is free for use in GPL programs.
	Special, special thanks to Joao Eriberto Mota Filho for doing a LOT of work to make hashrat debian ready!
Usage:
    hashrat [options] [path to hash]...
    hashrat -c [options] [input file of hashes]...
Options:
  --help          Print this help
  -help           Print this help
  -?              Print this help
  --version       Print program version
  -version        Print program version
  -list-hashes    Print a list of hashes that can be used with the '-type' option
  -type <hash>    specify a hash type to use. This supports hashes coming from other subsystems, such as openssl. It also supports 'chaining' hash types like so: -type sha256,whirl
  -md5            Use md5 hash algorithmn
  -sha1           Use sha1 hash algorithmn
  -sha256         Use sha256 hash algorithmn
  -sha384         Use sha384 hash algorithmn
  -sha512         Use sha512 hash algorithmn
  -whirl          Use whirlpool hash algorithmn
  -whirlpool      Use whirlpool hash algorithmn
  -jh224          Use jh-224 hash algorithmn
  -jh256          Use jh-256 hash algorithmn
  -jh384          Use jh-384 hash algorithmn
  -jh512          Use jh-512 hash algorithmn
  -hmac           HMAC using specified hash algorithm
  -totp <secret>  TOTP code with secret, defaults to google-authenticator compatible setup
  -totp <url>     TOTP code from supplied otpauth url (option can distinguish between secret and url)
  -digits <n>     produce otp codes with <n> digits
  -period <n>     produce otp codes with period/lifetime of <n> seconds
  -8              Encode with octal instead of hex
  -10             Encode with decimal instead of hex
  -H              Encode with UPPERCASE hexadecimal
  -HEX            Encode with UPPERCASE hexadecimal
  -32             Encode with base32 instead of hex
  -base32         Encode with base32 instead of hex
  -c32            Encode with Crockford base32 instead of hex
  -w32            Encode with word-safe base32 instead of hex
  -z32            Encode with zbase32 instead of hex
  -64             Encode with base64 instead of hex
  -base64         Encode with base64 instead of hex
  -i64            Encode with base64 with rearranged characters
  -p64            Encode with base64 with a-z,A-Z and _-, for best compatibility with 'allowed characters' in websites.
  -r64            Encode with base64 with a-z,A-Z and _-, rfc4648 compatible.
  -rfc4648        Encode with base64 with a-z,A-Z and _-, rfc4648 compatible.
  -x64            Encode with XXencode style base64.
  -u64            Encode with UUencode style base64.
  -g64            Encode with GEDCOM style base64.
  -a85            Encode with ASCII85.
  -z85            Encode with ZEROMQ variant of ASCII85.
  -t              Output hashes in traditional md5sum, shaXsum format
  -trad           Output hashes in traditional md5sum, shaXsum format
  -bsd            Output hashes in bsdsum format
  -tag            Output hashes in bsdsum format
  --tag           Output hashes in bsdsum format
  -r              Recurse into directories when hashing files
  -hid            Show hidden (starting with .) files
  -hidden         Show hidden (starting with .) files
  -f <listfile>   Hash files listed in <listfile>
  -i <patterns>   Only hash items matching a comma-seperated list of shell patterns
  -x <patterns>   Exclude items matching a comma-sepearted list of shell patterns
  -X <file>       Exclude items matching shell patters stored in <file>
  -name  <patterns> Only hash items matching a comma-seperated list of shell patterns (-name aka 'find')
  -mtime <days>   Only hash items <days> old. Has the same format as the find command, e.g. -10 is younger than ten days, +10 is older than ten, and 10 is ten days old
  -mmin  <mins>   Only hash items <min> minutes old. Has the same format as the find command, e.g. -10 is younger than ten mins, +10 is older than ten, and 10 is ten mins old
  -myear <years>  Only hash items <years> old. Has the same format as the find command, e.g. -10 is younger than ten years, +10 is older than ten, and 10 is ten years old
  -exec           In CHECK or MATCH mode only examine executable files.
  -dups           Search for duplicate files.
  -rename         Rename files to <name>-<hash>.<extn>.
  -n <length>     Truncate hashes to <length> bytes
  -segment <length> Break hash up into segments of <length> chars seperated by '-'
  -c              CHECK hashes against list from file (or stdin)
  -cf             CHECK hashes against list but only show failures
  -C <dir>        Recursively CHECK directory against list of files on stdin
  -Cf <dir>       Recursively CHECK directory against list but only show failures
  -m              MATCH files from a list read from stdin.
  -lm             Read hashes from stdin, upload them to a memcached server (requires the -memcached option).
  -memcached <server> Specify memcached server. (Overrides reading list from stdin if used with -m, -c or -cf).
  -mcd <server>   Specify memcached server. (Overrides reading list from stdin if used with -m, -c or -cf).
  -h <script>     Script to run when a file fails CHECK mode, or is found in MATCH mode.
  -hook <script>  Script to run when a file fails CHECK mode, or is found in FIND mode
  -color          Use ANSI color codes on output when checking hashes.
  -strict         Strict mode: when checking, check file mtime, owner, group, and inode as well as its hash
  -S              Strict mode: when checking, check file mtime, owner, group, and inode as well as its hash
  -d              dereference (follow) symlinks
  -fs             Stay on one file system
  -dir            DirMode: Read all files in directory and create one hash for them!
  -dirmode        DirMode: Read all files in directory and create one hash for them!
  -devmode        DevMode: read from a file EVEN IF IT'S A DEVNODE
  -lines          Read lines from stdin and hash each line independantly.
  -rawlines       Read lines from stdin and hash each line independantly, INCLUDING any trailing whitespace. (This is compatible with 'echo text | md5sum')
  -rl             Read lines from stdin and hash each line independantly, INCLUDING any trailing whitespace. (This is compatible with 'echo text | md5sum')
  -cgi            Run in HTTP CGI mode
  -cgi            Run in HTTP CGI mode
  -xdialog        Run in 'xdialog' (zenity, yad or qarama) mode
  -dialog-types <list> Specify a list of dialog commands and use the first found on the system. Default is 'yad,zenity,qarma'
  -iprefix <prefix> String to prefix all input before hashing
  -oprefix <prefix> Prefix to add to the front of output hashes
  -net            Treat 'file' arguments as either ssh or http URLs, and pull files over the network and then hash them (Allows hashing of files on remote machines).
                  URLs are in the format ssh://[username]:[password]@[host]:[port] or http://[username]:[password]@[host]:[port]..
  -idfile <path>  Path to an ssh private key file to use to authenticate INSTEAD OF A PASSWORD when pulling files via ssh.
  -xattr          Use eXtended file ATTRibutes. In hash mode, store hashes in the file attributes, in check mode compare against hashes stored in file attributes.
  -txattr         Use TRUSTED eXtended file ATTRibutes. In hash mode, store hashes in 'trusted' file attributes. 'trusted' attributes can only be read and written by root. Under freebsd this menas SYSTEM attributes.
  -attrs          comma-separated list of filesystem attribute names to be set to the value of the hash.
  -cache          Use hashes stored in 'user' xattr if they're younger than the mtime of the file. This speeds up outputting hashes. Also do not update xattr of a file if it already matches.
  -u <types>      Update. In checking mode, update hashes for the files as you go. <types> is a comma-separated list of things to update, which can be 'xattr' 'memcached' or a file name. This will update these targets with the hash that was found at the time of checking.
  -hide-input     When reading data from stdin in linemode, set the terminal to not echo characters, thus hiding typed input.
  -star-input     When reading data from stdin in linemode replace characters with stars.
  -xsel           Update X11 clipboard and primary selections to the current hash. This works using Xterm command sequences. The xterm resource 'allowWindowOps' must be set to 'true' for this to work.
  -clip           Update X11 clipboard to the current hash. This works using the 'xsel', 'xclip' or 'pbcopy' commands, or if none of those are installed falls back to Xterm clipboard as in the '-xsel' option .
  -qr             Display the current hash as a qrcode. This requires the 'qrencode' command to be installed, and also an image viewer like fim, feh, or imagemagick display to be installed.
  -qrcode         Display the current hash as a qrcode. This requires the 'qrencode' command to be installed, and also an image viewer like fim, feh, or imagemagick display to be installed.
  -clipcmd <cmds> Comma separated list of clipboard-setter commands to use instead of the defaults.
  -viewcmd <cmds> Comma separated list of image-viewer commands to use instead of the defaults.
Hashrat can also detect if it's being run under any of the following names (e.g., via symlinks)
  md5sum          run with '-trad -md5'
  shasum          run with '-trad -sha1'
  sha1sum         run with '-trad -sha1'
  sha256sum       run with '-trad -sha256'
  sha384sum       run with '-trad -sha384'
  sha512sum       run with '-trad -sha512'
  jh224sum        run with '-trad -jh224'
  jh256sum        run with '-trad -jh256'
  jh384sum        run with '-trad -jh384'
  jh512sum        run with '-trad -jh512'
  whirlpoolsum    run with '-trad -whirl'
  hashrat.cgi     run in web-enabled 'cgi mode'
Updated on: 2025-Dec-09
 Edit this page
hashid
hekatomb
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install hashrat`，再执行 `hashrat --version` 2>/dev/null || `hashrat -V`
- [ ] **2.** **读官方帮助** —— `hashrat -h`，需要细节时 `man hashrat`
- [ ] **3.** **在自有靶场跑最小用例** —— 官方给出的调用形式是：`Usage:`
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/hashrat/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/hashrat/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/hashrat/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
