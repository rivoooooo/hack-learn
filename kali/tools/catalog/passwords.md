# 按包速查：口令攻击（passwords）

> 共 **34** 个包 · 数据来源 <https://www.kali.org/tools/all-tools/>

返回 [工具总览](../index.md) · [全量清单](all-tools.md) · [按功能分类](../index.md#功能分类导航)

---

### cewl

Custom word list generator CeWL (Custom Word List generator) is a ruby app which spiders a given URL, up to a specified depth, and returns a list of words which can then be used for password crackers such as John the Ripper. Optionally, CeWL can follow external links. CeWL can also create a list of email addresses found in mailto

| 项目 | 内容 |
|------|------|
| 归入分组 | 口令攻击 |
| Kali 文档 | <https://www.kali.org/tools/cewl/> |
| 版本 | 6.2.1 |
| 包 / 命令 | `cewl`、`fab-cewl` |
| 安装 | `sudo apt install cewl` |
| 占用空间 | 81 KB |
| 依赖 | `ruby`、`ruby-mime`、`ruby-mime-types`、`ruby-mini-exiftool`、`ruby-net-http-digest-auth`、`ruby-nokogiri`、`ruby-spider`、`ruby-zip`、`cewl` |
| 官网 | <https://github.com/digininja/CeWL> |
| 源码 | <https://salsa.debian.org/pkg-security-team/cewl> |

### chntpw

NT SAM password recovery utility This little program provides a way to view information and change user passwords in a Windows NT/2000 user database file. Old passwords need not be known since they are overwritten. In addition it also contains a simple registry editor (same size data writes) and an hex-editor which enables you to

| 项目 | 内容 |
|------|------|
| 归入分组 | 口令攻击 |
| Kali 文档 | <https://www.kali.org/tools/chntpw/> |
| 版本 | 140201 |
| 包 / 命令 | `chntpw`、`reged`、`sampasswd`、`samunlock`、`samusrgrp` |
| 安装 | `sudo apt install chntpw` |
| 占用空间 | 487 KB |
| 依赖 | `libc6`、`chntpw` |
| 官网 | <http://pogostick.net/~pnh/ntpasswd/> |
| 源码 | <https://salsa.debian.org/debian/chntpw> |

### cmospwd

Decrypt BIOS passwords from CMOS CmosPwd is a cross-platform tool to decrypt password stored in CMOS used to access a computer’s BIOS setup. This application should work out of the box on most modern systems, but some more esoteric BIOSes may not be supported or may require additional steps.

| 项目 | 内容 |
|------|------|
| 归入分组 | 口令攻击 |
| Kali 文档 | <https://www.kali.org/tools/cmospwd/> |
| 版本 | 5.0 |
| 包 / 命令 | `cmospwd` |
| 安装 | `sudo apt install cmospwd` |
| 占用空间 | 65 KB |
| 依赖 | `libc6`、`cmospwd` |
| 官网 | <https://www.cgsecurity.org/wiki/CmosPwd> |
| 源码 | <https://gitlab.com/kalilinux/packages/cmospwd> |

### crackle

Crack and decrypt BLE encryption crackle exploits a flaw in the BLE pairing process that allows an attacker to guess or very quickly brute force the TK (Temporary Key). With the TK and other data collected from the pairing process, the STK (Short Term Key) and later the LTK (Long Term Key) can be collected. With the STK and LTK, all communications between the master and the slave can

| 项目 | 内容 |
|------|------|
| 归入分组 | 口令攻击 |
| 全部所属分组 | 蓝牙、口令攻击、无线攻击 |
| Kali 文档 | <https://www.kali.org/tools/crackle/> |
| 版本 | 0.1~git01282014 |
| 包 / 命令 | `crackle` |
| 安装 | `sudo apt install crackle` |
| 占用空间 | 54 KB |
| 依赖 | `libc6`、`libpcap0.8t64`、`crackle` |
| 官网 | <https://github.com/mikeryan/crackle> |
| 源码 | <https://gitlab.com/kalilinux/packages/crackle> |

### creddump7

Python tool to extract credentials and secrets from Windows registry hives This package contains a Python tool to extract various credentials and secrets from Windows registry hives. It’s based on the creddump program. Many patches and fixes have been applied by Ronnie Flathers.

| 项目 | 内容 |
|------|------|
| 归入分组 | 口令攻击 |
| 全部所属分组 | 数字取证、口令攻击、事件响应 |
| Kali 文档 | <https://www.kali.org/tools/creddump7/> |
| 版本 | 0.1 |
| 包 / 命令 | `creddump7` |
| 安装 | `sudo apt install creddump7` |
| 占用空间 | 78 KB |
| 依赖 | `python3`、`python3-pycryptodome`、`tree`、`creddump7` |
| 官网 | <https://github.com/CiscoCXSecurity/creddump7> |
| 源码 | <https://salsa.debian.org/pkg-security-team/creddump7> |

### crunch

Tool for creating wordlist Crunch is a wordlist generator where you can specify a standard character set or any set of characters to be used in generating the wordlists. The wordlists are created through combination and permutation of a set of characters. You can determine the amount of characters and list size.

| 项目 | 内容 |
|------|------|
| 归入分组 | 口令攻击 |
| Kali 文档 | <https://www.kali.org/tools/crunch/> |
| 版本 | 3.6 |
| 包 / 命令 | `crunch` |
| 安装 | `sudo apt install crunch` |
| 占用空间 | 84 KB |
| 依赖 | `libc6`、`crunch` |
| 官网 | <http://sourceforge.net/projects/crunch-wordlist/> |
| 源码 | <https://salsa.debian.org/debian/crunch> |

### fcrackzip

Password cracker for zip archives fcrackzip is a fast password cracker partly written in assembler. It is able to crack password protected zip files with brute force or dictionary based attacks, optionally testing with unzip its results. It can also crack cpmask’ed images. This package is useful for pentesters, ethical hackers and forensics

| 项目 | 内容 |
|------|------|
| 归入分组 | 口令攻击 |
| 全部所属分组 | 数字取证、口令攻击、事件响应 |
| Kali 文档 | <https://www.kali.org/tools/fcrackzip/> |
| 版本 | 1.0 |
| 包 / 命令 | `fcrackzip`、`fcrackzipinfo` |
| 安装 | `sudo apt install fcrackzip` |
| 占用空间 | 80 KB |
| 依赖 | `libc6`、`fcrackzip` |
| 官网 | <http://oldhome.schmorp.de/marc/fcrackzip.html> |
| 源码 | <https://salsa.debian.org/pkg-security-team/fcrackzip> |

### gpp-decrypt

Group Policy Preferences decrypter A simple ruby script that will decrypt a given GPP encrypted string.

| 项目 | 内容 |
|------|------|
| 归入分组 | 口令攻击 |
| Kali 文档 | <https://www.kali.org/tools/gpp-decrypt/> |
| 版本 | 0.1 |
| 包 / 命令 | `gpp-decrypt` |
| 安装 | `sudo apt install gpp-decrypt` |
| 占用空间 | 11 KB |
| 依赖 | `ruby`、`rubygems`、`gpp-decrypt` |
| 官网 | <http://carnal0wnage.attackresearch.com/2012/10/group-policy-preferences-and-getting.html> |
| 源码 | <https://gitlab.com/kalilinux/packages/gpp-decrypt> |

### hash-identifier

Tool to identify hash types Software to identify the different types of hashes used to encrypt data and especially passwords.

| 项目 | 内容 |
|------|------|
| 归入分组 | 口令攻击 |
| Kali 文档 | <https://www.kali.org/tools/hash-identifier/> |
| 版本 | 1.2 |
| 包 / 命令 | `hash-identifier` |
| 安装 | `sudo apt install hash-identifier` |
| 占用空间 | 49 KB |
| 依赖 | `python3`、`hash-identifier` |
| 官网 | <https://github.com/blackploit/hash-identifier> |
| 源码 | <https://gitlab.com/kalilinux/packages/hash-identifier> |

### hashcat

World’s fastest and most advanced password recovery utility Hashcat supports five unique modes of attack for over 300 highly-optimized hashing algorithms. hashcat currently supports CPUs, GPUs, and other hardware accelerators on Linux, and has facilities to help enable distributed password cracking. Examples of hashcat supported hashing algorithms are:

| 项目 | 内容 |
|------|------|
| 归入分组 | 口令攻击 |
| 全部所属分组 | 802.11 Wi-Fi、口令攻击、无线攻击 |
| Kali 文档 | <https://www.kali.org/tools/hashcat/> |
| 版本 | 7.1.2 |
| 包 / 命令 | `hashcat`、`hashcat-data` |
| 安装 | `sudo apt install hashcat` |
| 占用空间 | 119.52 MB |
| 依赖 | `hashcat-data`、`libc6`、`libminizip1t64`、`libxxhash0` |
| 官网 | <https://hashcat.net/hashcat/> |
| 源码 | <https://salsa.debian.org/pkg-security-team/hashcat> |

### hashcat-utils

Set of small utilities for advanced password cracking Hashcat-utils are a set of small utilities that are useful in advanced password cracking. They all are packed into multiple stand-alone binaries. All of these utils are designed to execute only one specific function.

| 项目 | 内容 |
|------|------|
| 归入分组 | 口令攻击 |
| Kali 文档 | <https://www.kali.org/tools/hashcat-utils/> |
| 版本 | 1.10 |
| 包 / 命令 | `hashcat-utils` |
| 安装 | `sudo apt install hashcat-utils` |
| 占用空间 | 511 KB |
| 依赖 | `libc6`、`perl` |
| 官网 | <https://github.com/hashcat/hashcat-utils/> |
| 源码 | <https://gitlab.com/kalilinux/packages/hashcat-utils> |

### hashid

Identify the different types of hashes used to encrypt data Identify the different types of hashes used to encrypt data and especially passwords. hashID is a tool written in Python 3.x which supports the identification of over 175 unique hash types using regular expressions. It is able to identify a single hash or parse a file and identify the hashes

| 项目 | 内容 |
|------|------|
| 归入分组 | 口令攻击 |
| Kali 文档 | <https://www.kali.org/tools/hashid/> |
| 版本 | 3.1.4 |
| 包 / 命令 | `hashid` |
| 安装 | `sudo apt install hashid` |
| 占用空间 | 83 KB |
| 依赖 | `python3`、`hashid` |
| 官网 | <https://psypanda.github.io/hashID/> |
| 源码 | <https://salsa.debian.org/pkg-security-team/hashid> |

### johnny

GUI for John the Ripper Johnny is provides a GUI for the John the Ripper password cracking tool.

| 项目 | 内容 |
|------|------|
| 归入分组 | 口令攻击 |
| Kali 文档 | <https://www.kali.org/tools/johnny/> |
| 版本 | 2.2 |
| 包 / 命令 | `johnny` |
| 安装 | `sudo apt install johnny` |
| 占用空间 | 922 KB |
| 依赖 | `john`、`libc6`、`libgcc-s1`、`libqt5core5t64` |
| 官网 | <https://openwall.info/wiki/john/johnny> |
| 源码 | <https://gitlab.com/kalilinux/packages/johnny> |

### maskprocessor

High-performance word generator with a per-position configurable charset Maskprocessor is a fast word list generator. It enumerates all combinations from a given user-defined keyspace and outputs the results. Since it supports different alphabets (which also can be combined) at different positions in the generation template (‘mask’), this approach allows a more fine-tunable generation of candidates than using ’naive’ brute force enumeration of words.

| 项目 | 内容 |
|------|------|
| 归入分组 | 口令攻击 |
| Kali 文档 | <https://www.kali.org/tools/maskprocessor/> |
| 版本 | 0.73 |
| 包 / 命令 | `maskprocessor`、`mp32`、`mp64` |
| 安装 | `sudo apt install maskprocessor` |
| 占用空间 | 44 KB |
| 依赖 | `libc6`、`mp32` |
| 官网 | <https://github.com/hashcat/maskprocessor> |
| 源码 | <https://salsa.debian.org/pkg-security-team/maskprocessor> |

### mimikatz

Uses admin rights on Windows to display passwords in plaintext Mimikatz uses admin rights on Windows to display passwords of currently logged in users in plaintext.

| 项目 | 内容 |
|------|------|
| 归入分组 | 口令攻击 |
| 全部所属分组 | 口令攻击、后渗透、Windows 资源 |
| Kali 文档 | <https://www.kali.org/tools/mimikatz/> |
| 版本 | 2.2.0 |
| 包 / 命令 | `mimikatz` |
| 安装 | `sudo apt install mimikatz` |
| 占用空间 | 2.54 MB |
| 依赖 | `kali-defaults`、`mimikatz` |
| 官网 | <https://blog.gentilkiwi.com/mimikatz> |
| 源码 | <https://gitlab.com/kalilinux/packages/mimikatz> |

### oclgausscrack

Cracks verification hashes of the Gauss Virus The goal of the program is to crack the verification hash of the encrypted payload of the Gauss Virus. Uses OpenCL to accelerate the 10k MD5 loop Uses optimizations also used in oclHashcat-plus for maximum performance Able to handle multi-GPU setups (of the same type)

| 项目 | 内容 |
|------|------|
| 归入分组 | 口令攻击 |
| 全部所属分组 | GPU 计算、口令攻击 |
| Kali 文档 | <https://www.kali.org/tools/oclgausscrack/> |
| 版本 | 1.3 |
| 包 / 命令 | `oclgausscrack`、`gausscombinator`、`gaussfilter` |
| 安装 | `sudo apt install oclgausscrack` |
| 占用空间 | 125 KB |
| 官网 | <https://github.com/jsteube/oclGaussCrack> |
| 源码 | <https://gitlab.com/kalilinux/packages/oclgausscrack> |

### ophcrack

Microsoft Windows password cracker using rainbow tables (gui) Ophcrack is a Windows password cracker based on a time-memory trade-off using rainbow tables. This is a new variant of Hellman’s original trade-off, with better performance. It recovers 99.9% of alphanumeric passwords in seconds. It works for Windows NT/2000/XP/Vista/7.

| 项目 | 内容 |
|------|------|
| 归入分组 | 口令攻击 |
| Kali 文档 | <https://www.kali.org/tools/ophcrack/> |
| 版本 | 3.8.0 |
| 包 / 命令 | `ophcrack`、`ophcrack-cli` |
| 安装 | `sudo apt install ophcrack` |
| 占用空间 | 501 KB |
| 依赖 | `libc6`、`libexpat1`、`libgcc-s1`、`libqt5charts5`、`libqt5core5t64` |
| 官网 | <https://ophcrack.sourceforge.net/> |
| 源码 | <https://salsa.debian.org/pkg-security-team/ophcrack> |

### pack

Password analysis and cracking kit PACK was developed in order to aid in a password cracking competition “Crack Me If You Can” that occurred during Defcon 2010. The goal of this toolkit is to aid in preparation for the “better than bruteforce” password attacks by analyzing common ways that people create

| 项目 | 内容 |
|------|------|
| 归入分组 | 口令攻击 |
| Kali 文档 | <https://www.kali.org/tools/pack/> |
| 版本 | 0.0.4 |
| 包 / 命令 | `pack`、`dictstat`、`jpackage`、`maskgen`、`pack200`、`policygen`、`rulegen`、`statsgen`、`unpack200` |
| 安装 | `sudo apt install pack` |
| 占用空间 | 110 KB |
| 依赖 | `kali-defaults`、`python3`、`python3-enchant`、`dictstat` |
| 官网 | <https://github.com/Hydraze/pack> |
| 源码 | <https://gitlab.com/kalilinux/packages/pack> |

### pack2

Password analysis and cracking kit 2 This package contains a replacement for iphelix’s PACK. This is a work in progress. Not all features are available and while being similar some will differ slightly. PACK was developed in order to aid in a password cracking competition “Crack Me If You Can” that occurred during Defcon 2010. The goal of this toolkit is

| 项目 | 内容 |
|------|------|
| 归入分组 | 口令攻击 |
| Kali 文档 | <https://www.kali.org/tools/pack2/> |
| 版本 | 0.1.0~git20200929.da4b245 |
| 包 / 命令 | `pack2`、`pack200`、`unpack200` |
| 安装 | `sudo apt install pack2` |
| 占用空间 | 897 KB |
| 依赖 | `libc6`、`libgcc-s1`、`pack2` |
| 官网 | <https://github.com/hops/pack2> |
| 源码 | <https://gitlab.com/kalilinux/packages/pack2> |

### passing-the-hash

Patched tools to use password hashes as authentication input This package contains modified versions of Curl, Iceweasel, FreeTDS, Samba 4, WinEXE and WMI. They are installed as executables starting with the “pth-” string.

| 项目 | 内容 |
|------|------|
| 归入分组 | 口令攻击 |
| Kali 文档 | <https://www.kali.org/tools/passing-the-hash/> |
| 版本 | 0~2015.12.37 |
| 包 / 命令 | `passing-the-hash`、`pth-curl`、`pth-net`、`pth-rpcclient`、`pth-smbclient`、`pth-smbget`、`pth-sqsh`、`pth-winexe`、`pth-wmic`、`pth-wmis` |
| 安装 | `sudo apt install passing-the-hash` |
| 占用空间 | 13.98 MB |
| 依赖 | `libc6`、`libcrypt1`、`libgmp10`、`libgnutls30t64`、`libgssapi-krb5-2`、`libhogweed6t64`、`libidn2-0`、`libldap2`、`libnettle8t64`、`librtmp1`、`libssl3t64`、`samba-common-bin` 等 |
| 官网 | <http://passing-the-hash.blogspot.fr> |
| 源码 | <https://gitlab.com/kalilinux/packages/passing-the-hash> |

### pdfcrack

PDF files password cracker PDFCrack is a simple tool for recovering passwords from pdf-documents. It should be able to handle all pdfs that uses the standard security handler but the pdf-parsing routines are a bit of a quick hack so you might stumble across some pdfs where the parser needs to be fixed to handle. The main PDFCrack features are:

| 项目 | 内容 |
|------|------|
| 归入分组 | 口令攻击 |
| Kali 文档 | <https://www.kali.org/tools/pdfcrack/> |
| 版本 | 0.21 |
| 包 / 命令 | `pdfcrack` |
| 安装 | `sudo apt install pdfcrack` |
| 占用空间 | 89 KB |
| 依赖 | `libc6`、`pdfcrack` |
| 官网 | <http://pdfcrack.sf.net> |
| 源码 | <https://salsa.debian.org/debian/pdfcrack> |

### pipal

Statistical analysis on password dumps All this tool does is to give you the stats and the information to help you analyse the passwords. The real work is done by you in interpreting the results.

| 项目 | 内容 |
|------|------|
| 归入分组 | 口令攻击 |
| 全部所属分组 | 口令攻击、报告与记录 |
| Kali 文档 | <https://www.kali.org/tools/pipal/> |
| 版本 | 3.4.0 |
| 包 / 命令 | `pipal` |
| 安装 | `sudo apt install pipal` |
| 占用空间 | 243 KB |
| 依赖 | `ruby`、`ruby-json`、`ruby-levenshtein`、`pipal` |
| 官网 | <https://www.digininja.org/projects/pipal.php> |
| 源码 | <https://gitlab.com/kalilinux/packages/pipal> |

### rainbowcrack

Rainbow table password cracker RainbowCrack is a general propose implementation of Philippe Oechslin’s faster time-memory trade-off technique. It crack hashes with rainbow tables. RainbowCrack uses time-memory tradeoff algorithm to crack hashes. It differs from the hash crackers that use brute

| 项目 | 内容 |
|------|------|
| 归入分组 | 口令攻击 |
| Kali 文档 | <https://www.kali.org/tools/rainbowcrack/> |
| 版本 | 1.8 |
| 包 / 命令 | `rainbowcrack`、`rcrack`、`rt2rtc`、`rtc2rt`、`rtgen`、`rtmerge`、`rtsort` |
| 安装 | `sudo apt install rainbowcrack` |
| 占用空间 | 497 KB |
| 依赖 | `libc6`、`libgcc-s1`、`libstdc++6`、`rcrack` |
| 官网 | <https://project-rainbowcrack.com/index.htm> |
| 源码 | <https://gitlab.com/kalilinux/packages/rainbowcrack> |

### rarcrack

Password cracker for rar archives This program uses a brute force algorithm to guess your encrypted compressed file’s password. This program can crack zip, 7z, and rar file passwords.

| 项目 | 内容 |
|------|------|
| 归入分组 | 口令攻击 |
| Kali 文档 | <https://www.kali.org/tools/rarcrack/> |
| 版本 | 0.2 |
| 包 / 命令 | `rarcrack` |
| 安装 | `sudo apt install rarcrack` |
| 占用空间 | 56 KB |
| 依赖 | `libc6`、`libxml2-16`、`rarcrack` |
| 官网 | <http://rarcrack.sourceforge.net/> |
| 源码 | <https://salsa.debian.org/salvage-team/rarcrack> |

### rcracki-mt

Version of rcrack that supports hybrid and indexed tables rcracki_mt is our modified version of rcrack which supports hybrid and indexed tables. In addition to that, it also adds multi-core support

| 项目 | 内容 |
|------|------|
| 归入分组 | 口令攻击 |
| Kali 文档 | <https://www.kali.org/tools/rcracki-mt/> |
| 版本 | 0.7.0 |
| 包 / 命令 | `rcracki-mt`、`rcracki_mt` |
| 安装 | `sudo apt install rcracki-mt` |
| 占用空间 | 406 KB |
| 依赖 | `libc6`、`libgcc-s1`、`libssl3t64`、`libstdc++6`、`rcracki_mt` |
| 官网 | <https://freerainbowtables.com/> |
| 源码 | <https://gitlab.com/kalilinux/packages/rcracki-mt> |

### rsmangler

Wordlist mangling tool RSMangler will take a wordlist and perform various manipulations on it similar to those done by John the Ripper the main difference being that it will first take the input words and generate all permutations and the acronym of the words (in order they appear in the file)

| 项目 | 内容 |
|------|------|
| 归入分组 | 口令攻击 |
| Kali 文档 | <https://www.kali.org/tools/rsmangler/> |
| 版本 | 1.5 |
| 包 / 命令 | `rsmangler` |
| 安装 | `sudo apt install rsmangler` |
| 占用空间 | 24 KB |
| 依赖 | `ruby`、`rsmangler` |
| 官网 | <https://digi.ninja/projects/rsmangler.php> |
| 源码 | <https://gitlab.com/kalilinux/packages/rsmangler> |

### samdump2

Dump Windows 2k/NT/XP password hashes This tool is designed to dump Windows 2k/NT/XP password hashes from a SAM file, using the syskey bootkey from the system hive. This package also provides the functionality of bkhive, which recovers the syskey bootkey from a Windows NT/2K/XP system hive. Syskey is a Windows feature that adds an additional encryption layer to the

| 项目 | 内容 |
|------|------|
| 归入分组 | 口令攻击 |
| 全部所属分组 | 数字取证、口令攻击、事件响应 |
| Kali 文档 | <https://www.kali.org/tools/samdump2/> |
| 版本 | 3.0.0 |
| 包 / 命令 | `samdump2` |
| 安装 | `sudo apt install samdump2` |
| 占用空间 | 43 KB |
| 依赖 | `libc6`、`libssl3t64`、`samdump2` |
| 官网 | <https://ophcrack.sourceforge.net/> |
| 源码 | <https://salsa.debian.org/pkg-security-team/samdump2> |

### seclists

Collection of multiple types of security lists SecLists is a collection of multiple types of lists used during security assessments. List types include usernames, passwords, URLs, sensitive data grep strings, fuzzing payloads, and many more. The goal is to enable a security tester to pull this repo onto a new testing box and have access to every type of list that may be needed.

| 项目 | 内容 |
|------|------|
| 归入分组 | 口令攻击 |
| Kali 文档 | <https://www.kali.org/tools/seclists/> |
| 版本 | 2025.3 |
| 包 / 命令 | `seclists` |
| 安装 | `sudo apt install seclists` |
| 占用空间 | 1.80 GB |
| 依赖 | `kali-defaults`、`seclists` |
| 官网 | <https://github.com/danielmiessler/SecLists> |
| 源码 | <https://gitlab.com/kalilinux/packages/seclists> |

### sipcrack

SIP login dumper/cracker The tools contained in this package offer support for pcap files, wordlists and many more to extract all needed information and bruteforce the passwords for the sniffed accounts. sipdump - Dump SIP digest authentications to a file. sipcrack - Bruteforce the user password using the dump file

| 项目 | 内容 |
|------|------|
| 归入分组 | 口令攻击 |
| 全部所属分组 | 口令攻击、VoIP |
| Kali 文档 | <https://www.kali.org/tools/sipcrack/> |
| 版本 | 0.2 |
| 包 / 命令 | `sipcrack`、`sipdump` |
| 安装 | `sudo apt install sipcrack` |
| 占用空间 | 72 KB |
| 依赖 | `libc6`、`libpcap0.8t64`、`libssl3t64`、`sipcrack` |
| 官网 | <http://www.remote-exploit.org/codes_sipcrack.html> |
| 源码 | <https://salsa.debian.org/debian/sipcrack> |

### statsprocessor

Word generator based on per-position Markov chains Statsprocessor is a word generator based on per-position Markov chains packed into a single stand-alone binary. It generates candidate words based on a Hashcat format .hcstat file by using this information to determine which letter is following which letter based on the analysis of the original input dictionary used to generate the .hcstat. The resulting words can then, for

| 项目 | 内容 |
|------|------|
| 归入分组 | 口令攻击 |
| Kali 文档 | <https://www.kali.org/tools/statsprocessor/> |
| 版本 | 0.11 |
| 包 / 命令 | `statsprocessor`、`sp32`、`sp64` |
| 安装 | `sudo apt install statsprocessor` |
| 占用空间 | 45 KB |
| 依赖 | `libc6`、`sp32` |
| 官网 | <https://github.com/hashcat/statsprocessor> |
| 源码 | <https://salsa.debian.org/pkg-security-team/statsprocessor> |

### sucrack

Multithreaded su bruteforcer sucrack is a multithreaded Linux/UNIX tool for cracking local user accounts via wordlist bruteforcing su. This tool comes in handy when you’ve gained access to a low-privilege user account but are allowed to su to other users. Many su implementations require a pseudo terminal to be attached in order to take the

| 项目 | 内容 |
|------|------|
| 归入分组 | 口令攻击 |
| Kali 文档 | <https://www.kali.org/tools/sucrack/> |
| 版本 | 1.2.3 |
| 包 / 命令 | `sucrack` |
| 安装 | `sudo apt install sucrack` |
| 占用空间 | 49 KB |
| 依赖 | `libc6`、`sucrack` |
| 官网 | <https://labs.portcullis.co.uk/tools/sucrack/> |
| 源码 | <https://salsa.debian.org/pkg-security-team/sucrack> |

### thc-pptp-bruter

THC PPTP Brute Force Brute force program against pptp vpn endpoints (tcp port 1723). Fully standalone. Supports latest MSChapV2 authentication. Tested against Windows and Cisco gateways. Exploits a weakness in Microsoft’s anti-brute force implementation which makes it possible to try 300 passwords the second.

| 项目 | 内容 |
|------|------|
| 归入分组 | 口令攻击 |
| Kali 文档 | <https://www.kali.org/tools/thc-pptp-bruter/> |
| 版本 | 0.1.4 |
| 包 / 命令 | `thc-pptp-bruter` |
| 安装 | `sudo apt install thc-pptp-bruter` |
| 占用空间 | 47 KB |
| 依赖 | `libc6`、`libssl3t64`、`thc-pptp-bruter` |
| 官网 | <http://www.thc.org/releases.php> |
| 源码 | <https://gitlab.com/kalilinux/packages/thc-pptp-bruter> |

### tree

Displays an indented directory tree, in color Tree is a recursive directory listing command that produces a depth indented listing of files, which is colorized ala dircolors if the LS_COLORS environment variable is set and output is to tty.

| 项目 | 内容 |
|------|------|
| 归入分组 | 口令攻击 |
| 全部所属分组 | 数字取证、口令攻击、事件响应 |
| Kali 文档 | <https://www.kali.org/tools/tree/> |
| 版本 | 2.3.2 |
| 包 / 命令 | `tree` |
| 安装 | `sudo apt install tree` |
| 占用空间 | 135 KB |
| 依赖 | `libc6`、`tree` |
| 官网 | <http://oldmanprogrammer.net/source.php?dir=projects/tree> |
| 源码 | <https://salsa.debian.org/debian/tree-packaging> |

### truecrack

Bruteforce password cracker for TrueCrypt volumes TrueCrack is a bruteforce password cracker for TrueCrypt (Copyright) volume. It is optimazed with Nvidia Cuda technology. It works with PBKDF2 (defined in PKCS5 v2.0) based on RIPEMD160 Key derivation function and XTS block cipher mode of operation

| 项目 | 内容 |
|------|------|
| 归入分组 | 口令攻击 |
| 全部所属分组 | 数字取证、GPU 计算、口令攻击、事件响应 |
| Kali 文档 | <https://www.kali.org/tools/truecrack/> |
| 版本 | 3.6 |
| 包 / 命令 | `truecrack` |
| 安装 | `sudo apt install truecrack` |
| 占用空间 | 2.61 MB |
| 依赖 | `libc6`、`truecrack` |
| 官网 | <https://github.com/lvaccaro/truecrack> |
| 源码 | <https://gitlab.com/kalilinux/packages/truecrack> |
