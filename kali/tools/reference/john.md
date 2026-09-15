# john

> Active password cracking tool John the Ripper is a tool designed to help systems administrators to find weak (easy to guess or crack through brute force) passwords, and even automatically mail users warning them about it, if it is desired.…

> **功能分类**：信息搜集 ｜ **Kali 包**：`john` ｜ **官方文档**：<https://www.kali.org/tools/john/>

## 1. 安装

```bash
sudo apt update
sudo apt install john
```

| 项目 | 内容 |
|------|------|
| 版本 | 1.9.0 |
| 架构 | any |
| 可执行命令 | `john` |
| 依赖 | `john-data`、`libc6`、`libcrypt1`、`libgmp10`、`libgomp1`、`libpcap0.8t64`、`libssl3t64`、`zlib1g` |
| 安装体积 | 78.67 MB |
| 官网 | <https://github.com/openwall/john> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/john> |
| 包追踪 | <https://pkg.kali.org/pkg/john> |

## 2. 官方用法示例

> 以下为 Kali 官方工具页给出的示例与输出原文。

```text
Usage Example
Using a wordlist (–wordlist=/usr/share/john/password.lst), apply mangling rules (–rules) and attempt to crack the password hashes in the given file (unshadowed.txt):
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `mailer`

```text
root@kali:~# mailer
Usage: /usr/sbin/mailer PASSWORD-FILE
Unique
```

### `unique`

```text
root@kali:~# unique
Usage: unique [-v] [-inp=fname] [-cut=len] [-mem=num] OUTPUT-FILE [-ex_file=FNAME2] [-ex_file_only=FNAME2]
       reads from stdin 'normally', but can be overridden by optional -inp=
       If -ex_file=XX is used, then data from file XX is also used to
       unique the data, but nothing is ever written to XX. Thus, any data in
       XX, will NOT output into OUTPUT-FILE (for making iterative dictionaries)
       -ex_file_only=XX assumes the file is 'unique', and only checks against XX
       -cut=len  Will trim each input lines to 'len' bytes long, prior to running
       the unique algorithm. The 'trimming' is done on any -ex_file[_only] file
       -mem=num.  A number that overrides the UNIQUE_HASH_LOG value from within
       params.h.  The default is 21.  This can be raised, up to 25 (memory usage
       doubles each number).  If you go TOO large, unique will swap and thrash and
       work VERY slow
       -v is for 'verbose' mode, outputs line counts during the run
john Usage Example
Using a wordlist (
–wordlist=/usr/share/john/password.lst
), apply mangling rules (
–rules
) and attempt to crack the password hashes in the given file (
unshadowed.txt
):
```

### `john`

> 官方示例调用：`john --wordlist=/usr/share/john/password.lst --rules unshadowed.txt`

```text
root@kali:~# john --wordlist=/usr/share/john/password.lst --rules unshadowed.txt
Warning: detected hash type "sha512crypt", but the string is also recognized as "crypt"
Use the "--format=crypt" option to force loading these as that type instead
Loaded 1 password hash (sha512crypt [64/64])
toor             (root)
guesses: 1  time: 0:00:00:07 DONE (Mon May 19 08:13:05 2014)  c/s: 482  trying: 1701d - andrew
Use the "--show" option to display all of the cracked passwords reliably
kali@kali:~$ echo -n test2 | md5sum
ad0234829205b9033196ba818f7a872b  -
kali@kali:~$ echo -n test2 | md5sum | awk '{print $1}'
ad0234829205b9033196ba818f7a872b
kali@kali:~$ echo -n test2 | md5sum | awk '{print $1}' > hash
kali@kali:~$
kali@kali:~$ for x in $(seq 0 9); do echo test$x >> wordlists; done
kali@kali:~$ grep test2 wordlists
test2
kali@kali:~$ wc -l wordlists
10 wordlists
kali@kali:~$
kali@kali:~$ john --list=formats | grep -i 'md5'
descrypt, bsdicrypt, md5crypt, md5crypt-long, bcrypt, scrypt, LM, AFS,
aix-ssha512, andOTP, ansible, argon2, as400-des, as400-ssha1, asa-md5,
dahua, dashlane, diskcryptor, Django, django-scrypt, dmd5, dmg, dominosec,
mschapv2-naive, krb5pa-md5, mssql, mssql05, mssql12, multibit, mysqlna,
mysql-sha1, mysql, net-ah, nethalflm, netlm, netlmv2, net-md5, netntlmv2,
netntlm, netntlm-naive, net-sha1, nk, notes, md5ns, nsec3, NT, o10glogon,
PBKDF2-HMAC-MD4, PBKDF2-HMAC-MD5, PBKDF2-HMAC-SHA1, PBKDF2-HMAC-SHA256,
PHPS2, pix-md5, PKZIP, po, postgres, PST, PuTTY, pwsafe, qnx, RACF,
Raw-Keccak, Raw-Keccak-256, Raw-MD4, Raw-MD5, Raw-MD5u, Raw-SHA1,
Stribog-256, Stribog-512, STRIP, SunMD5, SybaseASE, Sybase-PROP, tacacs-plus,
tcp-md5, telegram, tezos, Tiger, tc_aes_xts, tc_ripemd160, tc_ripemd160boot,
ZipMonster, plaintext, has-160, HMAC-MD5, HMAC-SHA1, HMAC-SHA224,
kali@kali:~$
kali@kali:~$ john  --format=raw-md5 --wordlist=wordlists hash
Created directory: /home/g0tmi1k/.john
Using default input encoding: UTF-8
Loaded 1 password hash (Raw-MD5 [MD5 128/128 AVX 4x3])
Warning: no OpenMP support for this hash type, consider --fork=2
Press 'q' or Ctrl-C to abort, almost any other key for status
Warning: Only 10 candidates left, minimum 12 needed for performance.
test2            (?)
1g 0:00:00:00 DONE (2021-11-04 10:30) 100.0g/s 1000p/s 1000c/s 1000C/s test0..test9
Use the "--show --format=Raw-MD5" options to display all of the cracked passwords reliably
Session completed
kali@kali:~$
unique Usage Example
Using verbose mode (
-v
), read a list of passwords (
-inp=allwords.txt
) and save only unique words to a file (
uniques.txt
):
```

### `unique -v -inp=allwords.txt uniques.txt`

> 官方示例调用：`unique -v -inp=allwords.txt uniques.txt`

```text
root@kali:~# unique -v -inp=allwords.txt uniques.txt
Total lines read 6089 Unique lines written 5083
```

### `man`

> 官方示例调用：`man SIPdump`

```text
root@kali:~# man SIPdump
SIPDUMP(1)                  General Commands Manual                  SIPDUMP(1)
NAME
     sipdump - Part of SIPcrack, A suite of tools to sniff and crack the digest
     authentications within the SIP protocol.
SYNOPSIS
     sipdump [options] <dump_file>
DESCRIPTION
     This manual page documents briefly the sipdump tool
     Session Initiation Protocol (SIP) is a protocol developed by the IETF MMU-
     SIC  Working  Group  and is a proposed standard for initiating, modifying,
     and terminating an interactive user session that involves multimedia  ele-
     ments  such  as video, voice, instant messaging, online games, and virtual
     reality.
     In November 2000, SIP was accepted as a 3GPP signaling protocol and perma-
     nent element of the IMS architecture.  It is one of the leading signalling
     protocols for Voice over IP, along with H.323. In most VOIP solutions  SIP
     is  used to authenticate the SIPclient.  The protocol is documented inside
     the RFC at www.ietf.org/rfc/rfc3261.txt
     SIPcrack is a SIP login sniffer/cracker that contains 2 programs:  sipdump
     to  capture  the digest authentication and sipcrack to bruteforce the hash
     using a wordlist or standard input.
     sipdump dumps SIP digest authentications. If a login is found, the sniffed
     login is written to the dump file.  See 'sipdump -h' for options.
     sipcrack bruteforces the user's password with the dump file  generated  by
     sipdump. If a password is found, the sniffed and cracked login will be up-
     dated in the dump file.
     See 'sipcrack -h' for options.
OPTIONS
     A summary of options is included below.
     -i interface,
            interface to listen on
     -p pcap_file,
            use pcap data file
     -m,    enter login data manually
     -f libpcap_filer ,
            set libpcap filter
EXAMPLE
     sipdump -i eth0 logins.dump
     sipcrack -w mywordlist.txt logins.dump
SEE ALSO
     sipcrack(1).
AUTHOR
     sipdump was written by Martin J. Muench <
[email protected]
>
     This  manual  page  was  written  by  Sebastian  Castillo  Builes <castil-
[email protected]
>, for the Debian project (but may be used by others).
                                 April 29, 2008                      SIPDUMP(1)
base64conv
```

### `base64conv`

> 官方示例调用：`base64conv -h`

```text
root@kali:~# base64conv -h
base64conv: invalid option -- 'h'
Usage: base64conv [-l] [-i intype] [-o outtype] [-q] [-w] [-e] [-f flag] [data[data ...] | < stdin]
 - data must match input_type i.e. if hex, then data should be in hex
 - if data is not present, then base64conv will read data from std input)
 - if data read from stdin, max size of any line is 256k
  -q will only output resultant string. No extra junk text
  -e turns on buffer overwrite error checking logic
  -l performs a 'length' test
  -r ifname  process whole file ifname (this is the input file)
  -w ofname  The output filename for whole file processing
             NOTE, -r and -w have to be used as a pair
Input/Output types:
  raw      raw data byte
  hex      hexadecimal string (for input, case does not matter)
  mime     base64 mime encoding
  crypt    base64 crypt character set encoding
  cryptBS  base64 crypt encoding, byte swapped
Flags (note more than 1 -f command switch can be given at one time):
  HEX_UPCASE         output or length UPCASED (input case auto handled)
  HEX_LOCASE         output or length locased (input case auto handled)
  MIME_TRAIL_EQ      output mime adds = chars (input = auto handled)
  CRYPT_TRAIL_DOTS   output crypt adds . chars (input . auto handled)
  MIME_PLUS_TO_DOT   mime converts + to . (passlib encoding)
  MIME_DASH_UNDER    mime convert +/ into -_ (passlib encoding)
bitlocker2john
```

### `bitlocker2john`

> 官方示例调用：`bitlocker2john -h`

```text
root@kali:~# bitlocker2john -h
Usage: bitlocker2john -i <Image of encrypted memory unit>
Options:
  -h		Show this help
  -i		Image path of encrypted memory unit encrypted with BitLocker
calc_stat
```

### `calc_stat`

> 官方示例调用：`calc_stat -h`

```text
root@kali:~# calc_stat -h
Usage: calc_stat [-p] dictionary_file statfile
	-p: include non printable and 8-bit characters
cprepair
```

### `cprepair`

> 官方示例调用：`cprepair -h`

```text
root@kali:~# cprepair -h
Codepage repair (c) magnum 2014-2019
Input can be a mix of codepages, UTF-8 and double-encoded UTF-8, and with
a mix of Windows (CRLF) and Unix (LF) line endings, or missing line endings
on last lines.  If no file name is given, STDIN is used.
Output is UTF-8 with LF line endings and no silly BOM.
Usage: cprepair [options] [file(s)]
Options:
 -i <cp>   Codepage to assume for 8-bit input. Default is CP1252 (MS Latin-1)
 -f <cp>   Alternate codepage when no ASCII letters (a-z, A-Z) seen (default
           is to not treat them differently)
 -n        Do not guess (leave 8-bit as-is)
 -s        Suppress lines that does not need fixing.
 -d        Debug (show conversions).
 -l        List supported encodings.
 -p        Only convert stuff after first ':' (.pot file).
 -P        Suppress output lines with unprintable ASCII and, when used together
           with -n option, also suppress lines with invalid UTF-8
dmg2john
eapmd5tojohn
```

### `eapmd5tojohn`

> 官方示例调用：`eapmd5tojohn -h`

```text
root@kali:~# eapmd5tojohn -h
Usage: eapmd5tojohn -r <pcap file>
genmkvpwd
```

## 4. 实践清单

按顺序做完这五步，就能把工具从「装上」推进到「会用」：

- [ ] **1.** **装好并确认版本** —— `sudo apt install john`，再执行 `john --version` 2>/dev/null || `john -V`
- [ ] **2.** **读官方帮助** —— `john -h`，需要细节时 `man john`
- [ ] **3.** **在自有靶场跑最小用例** —— 官方给出的调用形式是：`Usage: /usr/sbin/mailer PASSWORD-FILE`
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/john/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- **精讲教程**（含原理、参数详解、靶场实操与输出解读）：[john](../../tools/tutorials/04-口令攻击/john.md)
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/credential-access.md`](../../tools/by-attack/credential-access.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/john/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/john/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
