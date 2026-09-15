# 按包速查：通用工具（utils）

> 共 **345** 个包 · 数据来源 <https://www.kali.org/tools/all-tools/>

返回 [工具总览](../index.md) · [全量清单](all-tools.md) · [按功能分类](../index.md#功能分类导航)

---

### adaptixc2

Extensible post-exploitation and adversarial emulation framework Adaptix is an extensible post-exploitation and adversarial emulation framework made for authorized penetration testing. The Adaptix server is written in Golang and to allow operator flexibility.

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/adaptixc2/> |
| 版本 | 1.1~git20260208.6605760 |
| 包 / 命令 | `adaptixc2`、`adaptixclient`、`adaptixserver` |
| 安装 | `sudo apt install adaptixc2` |
| 占用空间 | 128.68 MB |
| 依赖 | `libc6`、`libgcc-s1`、`libqt6core6t64`、`libqt6gui6`、`libqt6network6`、`libqt6qml6`、`libqt6sql6`、`libqt6websockets6`、`libqt6widgets6`、`libstdc++6`、`qt6-base-private-abi`、`adaptixclient` 等 |
| 官网 | <https://github.com/Adaptix-Framework/AdaptixC2> |
| 源码 | <https://gitlab.com/kalilinux/packages/adaptixc2> |

### altdns

Subdomain discovery through alterations and permutations This package contains a DNS recon tool that allows for the discovery of subdomains that conform to patterns. Altdns takes in words that could be present in subdomains under a domain (such as test, dev, staging) as well as takes in a list of subdomains that you know of. From these two lists that are provided as input to altdns, the tool then

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/altdns/> |
| 版本 | 1.0.2 |
| 包 / 命令 | `altdns` |
| 安装 | `sudo apt install altdns` |
| 占用空间 | 46 KB |
| 依赖 | `python3`、`python3-configargparse`、`python3-dnspython`、`python3-termcolor`、`python3-tldextract`、`altdns` |
| 官网 | <https://github.com/infosec-au/altdns> |
| 源码 | <https://salsa.debian.org/pkg-security-team/altdns> |

### amap

Next-generation scanning tool for pentesters AMAP stands for Application MAPper. It is a next-generation scanning tool for pentesters. It attempts to identify applications even if they are running on a different port than normal. It also identifies non-ascii based applications. This is achieved by sending trigger packets, and looking up the responses in a list of

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/amap/> |
| 版本 | 5.4 |
| 包 / 命令 | `amap`、`amap6`、`amapcrap` |
| 安装 | `sudo apt install amap` |
| 占用空间 | 282 KB |
| 依赖 | `libc6`、`libssl3t64`、`amap` |
| 官网 | <https://www.thc.org> |
| 源码 | <https://gitlab.com/kalilinux/packages/amap> |

### android-sdk-meta

Software development kit for Android platform The Android SDK includes a variety of tools that help you develop mobile applications for the Android platform. The tools are classified into 3 groups: SDK Tools, Platform-tools and Build-tools. SDK Tools are platform independent and are required no matter which Android platform you are developing on. It is the base toolset of Android SDK.

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/android-sdk-meta/> |
| 版本 | 28.0.2 |
| 包 / 命令 | `android-sdk`、`android-sdk-build-tools`、`android-sdk-build-tools-common`、`android-sdk-common`、`android-sdk-platform-tools`、`android-sdk-platform-tools-common` |
| 安装 | `sudo apt install android-sdk` |
| 占用空间 | 28 KB |
| 依赖 | `android-sdk-build-tools`、`android-sdk-common`、`android-sdk-platform-tools`、`proguard-cli`、`android-sdk-build-tools` |
| 源码 | <https://salsa.debian.org/android-tools-team/android-sdk-meta> |

### apple-bleee

Scripts to show what an attacker get from Apple devices This package contains experimental scripts. They are PoCs that show what an attacker get from Apple devices if they sniff Bluetooth traffic. To use these scripts you will need a Bluetooth adapter for sending BLE messages and Wi-Fi card supporting active monitor mode with frame injection for communication using AWDL (AirDrop).

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/apple-bleee/> |
| 版本 | 0.1.5 |
| 包 / 命令 | `apple-bleee` |
| 安装 | `sudo apt install apple-bleee` |
| 占用空间 | 23.54 MB |
| 依赖 | `kali-defaults`、`python3`、`python3-bluez`、`python3-bs4`、`python3-ctypescrypto`、`python3-fleep`、`python3-libarchive-c`、`python3-netifaces`、`python3-pil`、`python3-prettytable`、`python3-pycryptodome`、`python3-requests` 等 |
| 官网 | <https://github.com/hexway/apple_bleee> |
| 源码 | <https://gitlab.com/kalilinux/packages/apple-bleee> |

### arjun

HTTP parameter discovery suite This package can find query parameters for URL endpoints. Web applications use parameters (or queries) to accept user input, take the following example into consideration. http://api.example.com/v1/userinfo?id=751634589 This URL seems to load user information for a specific user id, but what if

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/arjun/> |
| 版本 | 2.2.7 |
| 包 / 命令 | `arjun` |
| 安装 | `sudo apt install arjun` |
| 占用空间 | 348 KB |
| 依赖 | `python3`、`python3-dicttoxml`、`python3-ratelimit`、`python3-requests`、`arjun` |
| 官网 | <https://github.com/s0md3v/Arjun> |
| 源码 | <https://salsa.debian.org/pkg-security-team/arjun> |

### arp-scan

Arp scanning and fingerprinting tool arp-scan is a command-line tool that uses the ARP protocol to discover and fingerprint IP hosts on the local network. It is available for Linux and BSD under the GPL licence

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/arp-scan/> |
| 版本 | 1.10.0 |
| 包 / 命令 | `arp-scan`、`arp-fingerprint`、`get-iab`、`get-oui` |
| 安装 | `sudo apt install arp-scan` |
| 占用空间 | 1.53 MB |
| 依赖 | `libc6`、`libcap2`、`libpcap0.8t64`、`arp-fingerprint` |
| 官网 | <https://github.com/royhills/arp-scan> |
| 源码 | <https://salsa.debian.org/pkg-security-team/arp-scan> |

### arpwatch

Ethernet/FDDI station activity monitor Arpwatch maintains a database of Ethernet MAC addresses seen on the network, with their associated IP pairs. Alerts the system administrator via e-mail if any change happens, such as new station/activity, flip-flops, changed and re-used old addresses. If you want to maintain a list authorized MAC addresses manually, take a look

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/arpwatch/> |
| 版本 | 2.1a15 |
| 包 / 命令 | `arpwatch`、`arp2ethers`、`arpfetch`、`arpsnmp`、`bihourly`、`massagevendor` |
| 安装 | `sudo apt install arpwatch` |
| 占用空间 | 159 KB |
| 依赖 | `gawk`、`libc6`、`libpcap0.8t64` |
| 官网 | <https://ee.lbl.gov/> |
| 源码 | <https://salsa.debian.org/pkg-security-team/arpwatch> |

### arsenal-ng

Go-based command library equipped with 200+ cybersecurity cheat-sheets Inspired by arsenal, rewritten from scratch with a focus on simplicity, speed and developer experience. The classic launcher, evolved. Fast, Go-based command library equipped with 200+ cybersecurity cheat-sheets. Just install and start hacking.

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/arsenal-ng/> |
| 版本 | 1.6 |
| 包 / 命令 | `arsenal-ng` |
| 安装 | `sudo apt install arsenal-ng` |
| 占用空间 | 5.85 MB |
| 依赖 | `libc6`、`arsenal-ng` |
| 官网 | <https://github.com/halilkirazkaya/arsenal-ng> |
| 源码 | <https://gitlab.com/kalilinux/packages/arsenal-ng> |

### atftp

Advanced TFTP client Interactive client for the Trivial File Transfer Protocol (TFTP). Its usage is mainly for testing and debugging the atftp server. A TFTP client is usually implemented in UEFI/BIOS and bootstrap programs like pxelinux when booting from LAN. The atftp client also supports non-interactive invocation for easy use in scripts.

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/atftp/> |
| 版本 | 0.8.1 |
| 包 / 命令 | `atftp`、`atftpd`、`in.tftpd` |
| 安装 | `sudo apt install atftp` |
| 占用空间 | 93 KB |
| 依赖 | `libc6`、`libreadline8t64`、`atftp` |
| 官网 | <https://sourceforge.net/projects/atftp> |
| 源码 | <https://salsa.debian.org/debian/atftp> |

### atomic-operator

root@kali:~# atomic-operator -h INFO: Showing help with the command 'atomic-operator -- --help'. NAME

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/atomic-operator/> |
| 版本 | 0.9.1 |
| 包 / 命令 | `python3-atomic-operator`、`atomic-operator` |
| 安装 | `sudo apt install atomic-operator` |
| 官网 | <https://github.com/swimlane/atomic-operator> |
| 源码 | <https://gitlab.com/kalilinux/packages/atomic-operator> |

### autorecon

Multi-threaded network reconnaissance tool AutoRecon is a multi-threaded network reconnaissance tool which performs automated enumeration of services. It is intended as a time-saving tool for use in CTFs and other penetration testing environments (e.g. OSCP). It may also be useful in real-world engagements.

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/autorecon/> |
| 版本 | 0.0~git20251116.e7e98f6 |
| 包 / 命令 | `autorecon` |
| 安装 | `sudo apt install autorecon` |
| 占用空间 | 1.24 MB |
| 依赖 | `curl`、`dirb`、`dirsearch`、`dnsrecon`、`enum4linux`、`enum4linux-ng`、`ffuf`、`gobuster`、`impacket-scripts`、`nbtscan`、`nikto`、`nmap` 等 |
| 官网 | <https://github.com/Tib3rius/AutoRecon> |
| 源码 | <https://gitlab.com/kalilinux/packages/autorecon> |

### axel

Light command line download accelerator Axel tries to accelerate the downloading process by using multiple connections for one file, similar to DownThemAll and other famous programs. It can also use multiple mirrors for one download. Using Axel, you will get files faster from Internet. So, Axel can speed up a download up to 60% (approximately, according to some tests).

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/axel/> |
| 版本 | 2.17.14 |
| 包 / 命令 | `axel` |
| 安装 | `sudo apt install axel` |
| 占用空间 | 223 KB |
| 依赖 | `libc6`、`libssl3t64`、`axel` |
| 官网 | <https://github.com/axel-download-accelerator/axel> |
| 源码 | <https://salsa.debian.org/debian/axel> |

### azurehound

BloodHound data collector for Microsoft Azure (program) This package contains the BloodHound data collector for Microsoft Azure.

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/azurehound/> |
| 版本 | 3.1.0 |
| 包 / 命令 | `azurehound` |
| 安装 | `sudo apt install azurehound` |
| 占用空间 | 13.07 MB |
| 依赖 | `libc6`、`azurehound` |
| 官网 | <https://github.com/SpecterOps/AzureHound> |
| 源码 | <https://gitlab.com/kalilinux/packages/azurehound> |

### b374k

Remote management tool This package contains PHP Shell is a useful tool for system or web administrator to do remote management without using cpanel, connecting using ssh, ftp etc. All actions take place within a web browser Features: File manager (view, edit, rename, delete, upload, download, archiver, etc)

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/b374k/> |
| 版本 | 3.2.3 |
| 包 / 命令 | `b374k` |
| 安装 | `sudo apt install b374k` |
| 占用空间 | 494 KB |
| 依赖 | `kali-defaults`、`php-cli`、`b374k` |
| 官网 | <https://github.com/b374k/b374k> |
| 源码 | <https://gitlab.com/kalilinux/packages/b374k> |

### berate-ap

Script for orchestrating mana rogue Wi-Fi Access Points This package contains a script for orchestrating mana rogue Wi-Fi Access Points. It can also handle regular hostapd AP and create AP easily.

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/berate-ap/> |
| 版本 | 0.4.6 |
| 包 / 命令 | `berate-ap`、`berate_ap` |
| 安装 | `sudo apt install berate-ap` |
| 占用空间 | 103 KB |
| 依赖 | `hostapd-mana`、`iproute2`、`iw`、`procps`、`berate_ap` |
| 官网 | <https://github.com/sensepost/berate_ap> |
| 源码 | <https://gitlab.com/kalilinux/packages/berate-ap> |

### bettercap-ui

Bettercap’s web UI This package contains the bettercap’s web UI.

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/bettercap-ui/> |
| 版本 | 1.3.0 |
| 包 / 命令 | `bettercap-ui` |
| 安装 | `sudo apt install bettercap-ui` |
| 占用空间 | 18.90 MB |
| 依赖 | `bettercap`、`bettercap-caplets` |
| 官网 | <https://github.com/bettercap/ui> |
| 源码 | <https://gitlab.com/kalilinux/packages/bettercap-ui> |

### bind9

Internet Domain Name Server The Berkeley Internet Name Domain (BIND 9) implements an Internet domain name server. BIND 9 is the most widely-used name server software on the Internet, and is supported by the Internet Software Consortium, www.isc.org .

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/bind9/> |
| 版本 | 9.20.27 |
| 包 / 命令 | `bind9`、`arpaname`、`ddns-confgen`、`dnssec-importkey`、`named`、`named-journalprint`、`named-nzd2nzf`、`named-rrchecker`、`nsec3hash`、`tsig-keygen`、`bind9-dev`、`bind9-dnsutils`、`delv`、`dig`、`dnstap-read`、`mdig`、`nslookup`、`nsupdate`、`bind9-doc`、`bind9-host`、`host`、`bind9-libs`、`bind9-utils`、`dnssec-cds`、`dnssec-dsfromkey`、`dnssec-keyfromlabel`、`dnssec-keygen`、`dnssec-ksr`、`dnssec-revoke`、`dnssec-settime`、`dnssec-signzone`、`dnssec-verify`、`named-checkconf`、`named-checkzone`、`named-compilezone`、`rndc`、`rndc-confgen` |
| 安装 | `sudo apt install bind9` |
| 占用空间 | 904 KB |
| 依赖 | `adduser`、`bind9-libs`、`bind9-utils` |
| 官网 | <https://www.isc.org/downloads/bind/> |
| 源码 | <https://salsa.debian.org/dns-team/bind9> |

### bing-ip2hosts

Enumerate hostnames for an IP using bing.com This package contains a Bing.com web scraper that discovers hostnames by IP address. Bing is the flagship Microsoft search engine formerly known as MSN Search and Live Search. It provides a feature unique to search engines - it allows searching by IP address. Bing-ip2hosts uses this feature.

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/bing-ip2hosts/> |
| 版本 | 1.0.5 |
| 包 / 命令 | `bing-ip2hosts` |
| 安装 | `sudo apt install bing-ip2hosts` |
| 占用空间 | 29 KB |
| 依赖 | `bind9-dnsutils`、`wget`、`bing-ip2hosts` |
| 官网 | <https://www.morningstarsecurity.com/research/bing-ip2hosts> |
| 源码 | <https://gitlab.com/kalilinux/packages/bing-ip2hosts> |

### bloodhound

Six Degrees of Domain Admin, BloodHound CE This package contains BloodHound Community Edition, a single page Javascript web application. BloodHound uses graph theory to reveal the hidden and often unintended relationships within an Active Directory environment. Attackers can use BloodHound to easily identify highly complex attack paths that would otherwise

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/bloodhound/> |
| 版本 | 9.7.0~rc4 |
| 包 / 命令 | `bloodhound`、`bloodhound-setup`、`bloodhound-start`、`bloodhound-stop` |
| 安装 | `sudo apt install bloodhound` |
| 占用空间 | 297.32 MB |
| 依赖 | `curl`、`kali-defaults`、`neo4j`、`postgresql`、`bloodhound` |
| 官网 | <https://github.com/SpecterOps/BloodHound> |
| 源码 | <https://gitlab.com/kalilinux/packages/bloodhound> |

### bloodhound-ce-python

Python based ingestor for BloodHound CE This package contains a Python based ingestor for BloodHound CE, based on Impacket. This tool is only compatible with BloodHound CE. For legacy Bloodhound (<= 4.3.1) use bloodhound-python package.

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/bloodhound-ce-python/> |
| 版本 | 1.9.1 |
| 包 / 命令 | `bloodhound-ce-python` |
| 安装 | `sudo apt install bloodhound-ce-python` |
| 占用空间 | 357 KB |
| 依赖 | `python3`、`python3-dnspython`、`python3-impacket`、`python3-ldap3`、`python3-pyasn1`、`bloodhound-ce-python` |
| 官网 | <https://github.com/dirkjanm/BloodHound.py/tree/bloodhound-ce> |
| 源码 | <https://gitlab.com/kalilinux/packages/bloodhound-ce-python> |

### bloodyad

Active Directory privilege escalation framework bloodyAD can perform specific LDAP calls to a domain controller in order to perform AD privesc. It supports authentication using cleartext passwords, pass-the-hash, pass-the-ticket or certificates and binds to LDAP services of a domain controller to perform AD privesc. Exchange of sensitive information without LDAPS is supported. It is also

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/bloodyad/> |
| 版本 | 2.5.5 |
| 包 / 命令 | `bloodyad` |
| 安装 | `sudo apt install bloodyad` |
| 占用空间 | 54.80 MB |
| 依赖 | `python3`、`bloodyad` |
| 官网 | <https://github.com/CravateRouge/bloodyAD> |
| 源码 | <https://gitlab.com/kalilinux/packages/bloodyAD> |

### bopscrk

Generate smart and powerful wordlists Targeted-attack wordlist creator: introduce personal info related to target, combines every word and transforms results into possible passwords. The lyricpass module allows one to search lyrics related to artists and include them to the wordlists.

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/bopscrk/> |
| 版本 | 2.4.7 |
| 包 / 命令 | `bopscrk` |
| 安装 | `sudo apt install bopscrk` |
| 占用空间 | 101 KB |
| 依赖 | `python3`、`python3-alive-progress`、`python3-requests`、`bopscrk` |
| 官网 | <https://github.com/r3nt0n/bopscrk/> |
| 源码 | <https://gitlab.com/kalilinux/packages/bopscrk> |

### bpf-linker

Simplify building modern BPF programs This package contains bpd-linker which can be used to statically link multiple BPF object files together and optionally perform optimizations needed to target older kernels. It operates on LLVM bitcode, so the inputs must be bitcode files (.bc) or object files with embedded bitcode (.o), optionally stored inside ar archives (.a).

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/bpf-linker/> |
| 版本 | 0.9.14 |
| 包 / 命令 | `bpf-linker` |
| 安装 | `sudo apt install bpf-linker` |
| 占用空间 | 3.40 MB |
| 依赖 | `libc6`、`libgcc-s1`、`bpf-linker` |
| 官网 | <https://github.com/aya-rs/bpf-linker> |
| 源码 | <https://gitlab.com/kalilinux/packages/bpf-linker> |

### bruteforce-luks

Try to find a password of a LUKS encrypted volume The program is used to try discovery a password for encrypted LUKS volume used to security reasons. It works trying decrypt at least one of the key slots by trying all the possible passwords. It is used in forensics and is especially useful if you know something about the password (i.e. you forgot a part of your password but still remember most of it).

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/bruteforce-luks/> |
| 版本 | 1.4.0 |
| 包 / 命令 | `bruteforce-luks` |
| 安装 | `sudo apt install bruteforce-luks` |
| 占用空间 | 47 KB |
| 依赖 | `libc6`、`libcryptsetup12`、`bruteforce-luks` |
| 官网 | <https://github.com/glv2/bruteforce-luks> |
| 源码 | <https://salsa.debian.org/pkg-security-team/bruteforce-luks> |

### bruteforce-salted-openssl

Try to find the passphrase for files encrypted with OpenSSL bruteforce-salted-openssl try to find the passphrase or password of a file that was encrypted with the openssl command. It can be used in two ways: - Try all possible passwords given a charset. - Try all passwords in a file (dictionary). bruteforce-salted-openssl have the following features:

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/bruteforce-salted-openssl/> |
| 版本 | 1.5.0 |
| 包 / 命令 | `bruteforce-salted-openssl` |
| 安装 | `sudo apt install bruteforce-salted-openssl` |
| 占用空间 | 57 KB |
| 依赖 | `libc6`、`libssl3t64`、`bruteforce-salted-openssl` |
| 官网 | <https://github.com/glv2/bruteforce-salted-openssl> |
| 源码 | <https://salsa.debian.org/pkg-security-team/bruteforce-salted-openssl> |

### bruteforce-wallet

Try to find the password of an encrypted wallet file bruteforce-wallet try to find the password of an encrypted Peercoin (or Bitcoin, Litecoin, etc…) wallet file. It can be used in two ways: - Try all possible passwords given a charset. - Try all passwords in a file (dictionary).

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/bruteforce-wallet/> |
| 版本 | 1.5.4 |
| 包 / 命令 | `bruteforce-wallet` |
| 安装 | `sudo apt install bruteforce-wallet` |
| 占用空间 | 52 KB |
| 依赖 | `libc6`、`libdb5.3t64`、`libssl3t64`、`bruteforce-wallet` |
| 官网 | <https://github.com/glv2/bruteforce-wallet> |
| 源码 | <https://salsa.debian.org/pkg-security-team/bruteforce-wallet> |

### bruteshark

Network Forensic Analysis Tool (NFAT) This package contains a Network Forensic Analysis Tool (NFAT) that performs deep processing and inspection of network traffic (mainly PCAP files, but it also capable of directly live capturing from a network interface). It includes: password extracting, building a network map, reconstruct TCP sessions, extract hashes of encrypted passwords and even convert them to a

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/bruteshark/> |
| 版本 | 1.2.5 |
| 包 / 命令 | `bruteshark`、`brutesharkcli` |
| 安装 | `sudo apt install bruteshark` |
| 占用空间 | 93.29 MB |
| 依赖 | `libc6`、`libgcc1`、`libgssapi-krb5-2`、`libpcap0.8t64`、`libstdc++6`、`zlib1g`、`brutesharkcli` |
| 官网 | <https://github.com/odedshimon/BruteShark> |
| 源码 | <https://gitlab.com/kalilinux/packages/bruteshark> |

### brutespray

Bruteforcing from various scanner output Brutespray has been re-written in Golang, eliminating the requirement for additional tools. This enhanced version is more extensive and operates at a significantly faster pace than its Python counterpart. As of now, Brutespray accepts input from Nmap’s GNMAP/XML output, newline-separated JSON files, Nexpose’s XML Export feature, Nessus exports in .nessus format, and various

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/brutespray/> |
| 版本 | 2.2.2 |
| 包 / 命令 | `brutespray` |
| 安装 | `sudo apt install brutespray` |
| 占用空间 | 24.46 MB |
| 依赖 | `libc6`、`brutespray` |
| 官网 | <https://github.com/x90skysn3k/brutespray> |
| 源码 | <https://gitlab.com/kalilinux/packages/brutespray> |

### caido

Security auditing toolkit (desktop) This package contains caido desktop, a security auditing toolkit.

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/caido/> |
| 版本 | 0.58.3 |
| 包 / 命令 | `caido` |
| 安装 | `sudo apt install caido` |
| 占用空间 | 468.86 MB |
| 官网 | <https://github.com/caido/caido> |
| 源码 | <https://gitlab.com/kalilinux/packages/caido> |

### caido-cli

Security auditing toolkit (CLI) This package contains caido CLI, a security auditing toolkit.

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/caido-cli/> |
| 版本 | 0.58.3 |
| 包 / 命令 | `caido-cli` |
| 安装 | `sudo apt install caido-cli` |
| 占用空间 | 118.41 MB |
| 依赖 | `libc6`、`libgcc-s1`、`caido-cli` |
| 官网 | <https://github.com/caido/caido> |
| 源码 | <https://gitlab.com/kalilinux/packages/caido-cli> |

### caldera

Scalable Automated Adversary Emulation Platform This package contains a cyber security framework designed to easily automate adversary emulation, assist manual red-teams, and automate incident response.

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/caldera/> |
| 版本 | 5.3.0 |
| 包 / 命令 | `caldera` |
| 安装 | `sudo apt install caldera` |
| 占用空间 | 69.94 MB |
| 依赖 | `adduser`、`curl`、`git`、`golang-go`、`python3`、`python3-aioftp`、`python3-aiohttp`、`python3-aiohttp-apispec`、`python3-aiohttp-jinja2`、`python3-aiohttp-security`、`python3-aiohttp-session`、`python3-asyncssh` 等 |
| 官网 | <https://github.com/mitre/caldera> |
| 源码 | <https://gitlab.com/kalilinux/packages/caldera> |

### calico

Networking and network security solution for Kubernetes This package contains the command line tool for calico. Calico is a widely adopted, battle-tested open source networking and network security solution for Kubernetes, virtual machines, and bare-metal workloads.

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/calico/> |
| 版本 | 3.32.1 |
| 包 / 命令 | `calicoctl` |
| 安装 | `sudo apt install calicoctl` |
| 占用空间 | 64.69 MB |
| 依赖 | `libc6`、`calicoctl` |
| 官网 | <https://github.com/projectcalico/calico> |
| 源码 | <https://gitlab.com/kalilinux/packages/calico> |

### certgraph

Tool to crawl the graph of certificate Alternate Names This package contains a tool to crawl the graph of certificate Alternate Names. CertGraph crawls SSL certificates creating a directed graph where each domain is a node and the certificate alternative names for that domain’s certificate are the edges to other domain nodes. New domains are printed as they are found. In Detailed mode upon completion the Graph’s adjacency list is

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/certgraph/> |
| 版本 | 20180911 |
| 包 / 命令 | `certgraph` |
| 安装 | `sudo apt install certgraph` |
| 占用空间 | 6.37 MB |
| 依赖 | `libc6`、`certgraph` |
| 官网 | <https://github.com/lanrat/certgraph> |
| 源码 | <https://gitlab.com/kalilinux/packages/certgraph> |

### certi

Tool to ask certificates to ADCS and discover templates Certi is an utility to play with ADCS, allows one to request tickets and collect information about related objects. Basically, it’s the impacket copy of Certify.

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/certi/> |
| 版本 | 0.0~git20230127.6cfa656 |
| 包 / 命令 | `certi` |
| 安装 | `sudo apt install certi` |
| 占用空间 | 118 KB |
| 依赖 | `python3`、`python3-cryptography`、`python3-impacket`、`certi` |
| 官网 | <https://github.com/zer1t0/certi> |
| 源码 | <https://gitlab.com/kalilinux/packages/certi> |

### chainsaw

Rapidly search and hunt through Windows forensic artefacts Chainsaw provides a powerful ‘first-response’ capability to quickly identify threats within Windows forensic artefacts such as Event Logs and the MFT files. Chainsaw offers a generic and fast method of searching through event logs for keywords, and by identifying threats using built-in support for Sigma

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/chainsaw/> |
| 版本 | 2.16.5 |
| 包 / 命令 | `chainsaw` |
| 安装 | `sudo apt install chainsaw` |
| 占用空间 | 9.84 MB |
| 依赖 | `libc6`、`libgcc-s1`、`chainsaw` |
| 官网 | <https://github.com/WithSecureLabs/chainsaw> |
| 源码 | <https://gitlab.com/kalilinux/packages/chainsaw> |

### changeme

Default credential scanner This package contains a default credential scanner. Commercial vulnerability scanners miss common default credentials. Getting default credentials added to commercial scanners is often difficult and slow. changeme is designed to be simple to add new credentials without having to write any code or modules. changeme keeps credential data separate from code. All credentials are stored

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/changeme/> |
| 版本 | 1.2.3 |
| 包 / 命令 | `changeme` |
| 安装 | `sudo apt install changeme` |
| 占用空间 | 314 KB |
| 依赖 | `python3`、`python3-cerberus`、`python3-jinja2`、`python3-libnmap`、`python3-logutils`、`python3-lxml`、`python3-memcache`、`python3-netaddr`、`python3-paramiko`、`python3-psycopg2`、`python3-pymongo`、`python3-pyodbc` 等 |
| 官网 | <https://github.com/ztgrace/changeme> |
| 源码 | <https://salsa.debian.org/pkg-security-team/changeme> |

### chaosreader

Trace network sessions and export it to html format Chaosreader traces TCP/UDP/others sessions and fetches application data from snoop or tcpdump logs (or other libpcap compatible programs). This is a type of “any-snarf” program, as it will fetch telnet sessions, FTP files, HTTP transfers (HTML, GIF, JPEG etc) and SMTP emails from the captured data inside network traffic logs. A html index file is created to that links to all the

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/chaosreader/> |
| 版本 | 0.96 |
| 包 / 命令 | `chaosreader` |
| 安装 | `sudo apt install chaosreader` |
| 占用空间 | 230 KB |
| 依赖 | `libnet-dns-perl`、`perl`、`chaosreader` |
| 官网 | <https://www.brendangregg.com/chaosreader.html> |
| 源码 | <https://salsa.debian.org/pkg-security-team/chaosreader> |

### cherrytree

Hierarchical note taking application CherryTree is a hierarchical note taking application, featuring rich text, syntax highlighting, images handling, hyperlinks, import/export with support for multiple formats, support for multiple languages, and more.

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/cherrytree/> |
| 版本 | 1.2.0 |
| 包 / 命令 | `cherrytree` |
| 安装 | `sudo apt install cherrytree` |
| 占用空间 | 11.00 MB |
| 依赖 | `desktop-file-utils`、`libatkmm-1.6-1v5`、`libc6`、`libcairo2`、`libcairomm-1.0-1v5`、`libcurl4t64`、`libfmt10`、`libfribidi0`、`libgcc-s1`、`libglib2.0-0t64`、`libglibmm-2.4-1t64`、`libgspell-1-3` 等 |
| 官网 | <https://www.giuspen.net/cherrytree/> |
| 源码 | <https://salsa.debian.org/debian/cherrytree> |

### chisel

Fast TCP/UDP tunnel over HTTP (program) This package contains a fast TCP/UDP tunnel, transported over HTTP, secured via SSH. Single executable including both client and server. Chisel is mainly useful for passing through firewalls, though it can also be used to provide a secure endpoint into your network.

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/chisel/> |
| 版本 | 1.12.0~rc2 |
| 包 / 命令 | `chisel` |
| 安装 | `sudo apt install chisel` |
| 占用空间 | 10.17 MB |
| 依赖 | `libc6`、`chisel` |
| 官网 | <https://github.com/jpillora/chisel> |
| 源码 | <https://gitlab.com/kalilinux/packages/chisel> |

### chisel-common-binaries

Prebuilt binaries for chisel This package contains a fast TCP/UDP tunnel, transported over HTTP, secured via SSH. Single executable including both client and server. Chisel is mainly useful for passing through firewalls, though it can also be used to provide a secure endpoint into your network.

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/chisel-common-binaries/> |
| 版本 | 1.12.0~rc3 |
| 包 / 命令 | `chisel-common-binaries` |
| 安装 | `sudo apt install chisel-common-binaries` |
| 占用空间 | 108.26 MB |
| 官网 | <https://github.com/jpillora/chisel> |
| 源码 | <https://gitlab.com/kalilinux/packages/chisel> |

### chromium

Web browser Web browser that aims to build a safer, faster, and more stable internet browsing experience. This package contains the web browser component.

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/chromium/> |
| 版本 | 150.0.7871.181 |
| 包 / 命令 | `chromium`、`chromium-common`、`chromium-driver`、`chromedriver`、`chromium-headless-shell`、`chromium-l10n`、`chromium-sandbox`、`chromium-shell` |
| 安装 | `sudo apt install chromium` |
| 占用空间 | 300.51 MB |
| 依赖 | `chromium-common`、`libasound2t64`、`libatk-bridge2.0-0t64`、`libatk1.0-0t64`、`libatspi2.0-0t64`、`libc6`、`libcairo2`、`libcups2t64`、`libdav1d7`、`libdbus-1-3`、`libdouble-conversion3`、`libexpat1` 等 |
| 官网 | <http://www.chromium.org/Home> |
| 源码 | <https://salsa.debian.org/chromium-team/chromium> |

### cifs-utils

Common Internet File System utilities The SMB/CIFS protocol provides support for cross-platform file sharing with Microsoft Windows, OS X, and other Unix systems. This package provides utilities for managing mounts of CIFS network file systems.

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/cifs-utils/> |
| 版本 | 7.4 |
| 包 / 命令 | `cifs-utils`、`cifs.idmap`、`cifs.upcall`、`cifscreds`、`getcifsacl`、`mount.cifs`、`mount.smb3`、`setcifsacl`、`smb2-quota`、`smbinfo` |
| 安装 | `sudo apt install cifs-utils` |
| 占用空间 | 351 KB |
| 依赖 | `libc6`、`libcap-ng0`、`libgssapi-krb5-2`、`libkeyutils1`、`libkrb5-3`、`libpam0g`、`libtalloc2`、`libwbclient0`、`python3`、`cifs.idmap` |
| 官网 | <https://wiki.samba.org/index.php/LinuxCIFS_utils> |
| 源码 | <https://salsa.debian.org/samba-team/cifs-utils> |

### cilium-cli

Cilium CLI (program) This package contains a CLI to install, manage & troubleshoot Kubernetes clusters running Cilium.

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/cilium-cli/> |
| 版本 | 0.19.1 |
| 包 / 命令 | `cilium-cli`、`cilium` |
| 安装 | `sudo apt install cilium-cli` |
| 占用空间 | 186.62 MB |
| 依赖 | `libc6`、`cilium` |
| 官网 | <https://github.com/cilium/cilium-cli> |
| 源码 | <https://gitlab.com/kalilinux/packages/cilium-cli> |

### ciphey

root@kali:~# ciphey --help Usage: ciphey [OPTIONS] [TEXT_STDIN] Ciphey - Automated Decryption Tool Documentation: https://github.com/Ciphey/Ciphey/wiki Discord (support here, we're online most of the day): https://discord.ciphey.online/

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/ciphey/> |
| 版本 | 5.14.0 |
| 包 / 命令 | `python3-ciphey`、`ciphey` |
| 安装 | `sudo apt install ciphey` |
| 官网 | <https://github.com/Ciphey/Ciphey> |
| 源码 | <https://gitlab.com/kalilinux/packages/ciphey> |

### cisco7crack

Crypt and decrypt the cisco type 7 passwords This tool is used to crack Cisco Type 7 passwords. Can be used to encrypt and decrypt Cisco device passwords. Originally designed in order to allow quick decryption of stored passwords, Type 7 passwords are not a secure form of password storage. There are many tools available that can easily decrypt these passwords. Use of Type 7

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/cisco7crack/> |
| 版本 | 0.0~git20121221.f1c21dd |
| 包 / 命令 | `cisco7crack` |
| 安装 | `sudo apt install cisco7crack` |
| 占用空间 | 28 KB |
| 依赖 | `libc6`、`cisco7crack` |
| 官网 | <https://github.com/madrisan/cisco7crack> |
| 源码 | <https://salsa.debian.org/pkg-security-team/cisco7crack> |

### cloud-enum

Multi-cloud open source intelligence tool cloud_enum enumerates public resources matching user requested keywords in public clouds: Amazon Web Services: Open S3 Buckets Protected S3 Buckets

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/cloud-enum/> |
| 版本 | 0.8 |
| 包 / 命令 | `cloud-enum`、`cloud_enum` |
| 安装 | `sudo apt install cloud-enum` |
| 占用空间 | 91 KB |
| 官网 | <https://github.com/initstring/cloud_enum> |
| 源码 | <https://salsa.debian.org/pkg-security-team/cloud-enum> |

### cloudbrute

Awesome cloud enumerator (program) This package contains a tool to find a company (target) infrastructure, files, and apps on the top cloud providers (Amazon, Google, Microsoft, DigitalOcean, Alibaba, Vultr, Linode). The outcome is useful for bug bounty hunters, red teamers, and penetration testers alike. The complete writeup is available here

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/cloudbrute/> |
| 版本 | 1.0.7 |
| 包 / 命令 | `cloudbrute` |
| 安装 | `sudo apt install cloudbrute` |
| 占用空间 | 6.15 MB |
| 依赖 | `libc6`、`cloudbrute` |
| 官网 | <https://github.com/0xsha/cloudbrute> |
| 源码 | <https://gitlab.com/kalilinux/packages/cloudbrute> |

### cmseek

CMS Detection and Exploitation suite This package contains a CMS Detection and Exploitation suite. It scans WordPress, Joomla, Drupal and over 180 other CMSs. A content management system (CMS) manages the creation and modification of digital content. It typically supports multiple users in a collaborative environment.

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/cmseek/> |
| 版本 | 1.1.3 |
| 包 / 命令 | `cmseek` |
| 安装 | `sudo apt install cmseek` |
| 占用空间 | 400 KB |
| 依赖 | `python3`、`python3-requests`、`cmseek` |
| 官网 | <https://github.com/Tuhinshubhra/CMSeeK> |
| 源码 | <https://gitlab.com/kalilinux/packages/cmseek> |

### cntlm

Fast NTLM authentication proxy with tunneling Cntlm is a fast and efficient NTLM proxy, with support for TCP/IP tunneling, authenticated connection caching, ACLs, proper daemon logging and behaviour and much more. It has up to ten times faster responses than similar NTLM proxies, while using by orders or magnitude less RAM and CPU. Manual page contains detailed information.

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/cntlm/> |
| 版本 | 0.94.0 |
| 包 / 命令 | `cntlm` |
| 安装 | `sudo apt install cntlm` |
| 占用空间 | 703 KB |
| 依赖 | `libc6`、`libgssapi-krb5-2` |
| 官网 | <https://github.com/versat/cntlm/> |
| 源码 | <https://salsa.debian.org/debian/cntlm> |

### code-oss

Open Source package of vscode This package contains code-oss, a code editor with what developers need for their core edit-build-debug cycle. It provides comprehensive code editing, navigation, and understanding support along with lightweight debugging, a rich extensibility model, and lightweight integration with existing tools. This package is built from Microsoft open source code named code-oss.

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/code-oss/> |
| 版本 | 1.101.1 |
| 包 / 命令 | `code-oss`、`code`、`vscode` |
| 安装 | `sudo apt install code-oss` |
| 占用空间 | 2.43 GB |
| 依赖 | `nodejs`、`code` |
| 官网 | <https://github.com/microsoft/vscode> |
| 源码 | <https://gitlab.com/kalilinux/packages/code-oss> |

### coercer

Coerce a Windows server to authenticate on an arbitrary machine A Python script to automatically coerce a Windows server to authenticate on an arbitrary machine through many methods.

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/coercer/> |
| 版本 | 2.4.3 |
| 包 / 命令 | `coercer` |
| 安装 | `sudo apt install coercer` |
| 占用空间 | 241 KB |
| 依赖 | `python3`、`python3-impacket`、`python3-jinja2`、`python3-xlsxwriter`、`coercer` |
| 官网 | <https://github.com/p0dalirius/Coercer> |
| 源码 | <https://gitlab.com/kalilinux/packages/coercer> |

### colly

Elegant Scraper and Crawler Framework for Golang (program) This package contains a Colly Lightning Fast and Elegant Scraping Framework for Gophers. Colly provides a clean interface to write any kind of crawler/scraper/spider. With Colly you can easily extract structured data from websites, which can be used for a wide range of applications, like data mining, data

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/colly/> |
| 版本 | 2.1.0 |
| 包 / 命令 | `colly`、`golang-github-gocolly-colly-dev` |
| 安装 | `sudo apt install colly` |
| 占用空间 | 1.39 MB |
| 依赖 | `golang-github-antchfx-htmlquery-dev`、`golang-github-antchfx-xmlquery-dev`、`golang-github-gobwas-glob-dev`、`golang-github-jawher-mow.cli-dev`、`golang-github-kennygrant-sanitize-dev`、`golang-github-nlnwa-whatwg-url-dev`、`golang-github-puerkitobio-goquery-dev`、`golang-github-saintfish-chardet-dev`、`golang-github-temoto-robotstxt-dev`、`golang-golang-x-net-dev`、`golang-google-appengine-dev` |
| 官网 | <https://github.com/gocolly/colly> |
| 源码 | <https://gitlab.com/kalilinux/packages/colly> |

### command-not-found

Suggest installation of packages in interactive bash sessions This package will install a handler for command_not_found that looks up programs not currently installed but available from the repositories.

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/command-not-found/> |
| 版本 | 23.04.0 |
| 包 / 命令 | `command-not-found`、`update-command-not-found` |
| 安装 | `sudo apt install command-not-found` |
| 占用空间 | 524 KB |
| 依赖 | `apt-file`、`lsb-release`、`python3`、`python3-apt`、`command-not-found` |
| 源码 | <https://gitlab.com/kalilinux/packages/command-not-found> |

### cosign

Code signing/transparency for containers and binaries (program) Signing OCI containers (and other artifacts) using Sigstore Cosign supports: “Keyless signing” with the Sigstore public good Fulcio certificate authority and Rekor transparency log (default) Hardware and KMS signing

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/cosign/> |
| 版本 | 3.1.1 |
| 包 / 命令 | `cosign`、`golang-github-sigstore-cosign-dev` |
| 安装 | `sudo apt install cosign` |
| 占用空间 | 84.77 MB |
| 依赖 | `libc6`、`cosign` |
| 官网 | <https://github.com/sigstore/cosign> |
| 源码 | <https://salsa.debian.org/go-team/packages/cosign> |

### covenant-kbx

.NET command and control framework This package contains Covenant: .NET command and control framework that aims to highlight the attack surface of .NET, make the use of offensive .NET tradecraft easier, and serve as a collaborative command and control platform for red teamers. Covenant is an ASP.NET Core, cross-platform application that includes a

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/covenant-kbx/> |
| 版本 | 0.6 |
| 包 / 命令 | `covenant-kbx` |
| 安装 | `sudo apt install covenant-kbx` |
| 占用空间 | 25.13 MB |
| 官网 | <https://github.com/cobbr/Covenant> |
| 源码 | <https://gitlab.com/kalilinux/packages/covenant-kbx> |

### crack

Password guessing program (crypt() variant) Crack is program designed to quickly locate vulnerabilities in Unix (or other) password files by scanning the contents of a password file, looking for users who have misguidedly chosen a weak login password. This package provides the runtime files for the crypt() version.

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/crack/> |
| 版本 | 5.0a |
| 包 / 命令 | `crack` |
| 安装 | `sudo apt install crack` |
| 占用空间 | 153 KB |
| 依赖 | `crack-common`、`libc6`、`libcrypt1` |
| 官网 | <https://alecmuffett.com/alecm/software/crack/> |
| 源码 | <https://salsa.debian.org/pkg-security-team/crack> |

### crackmapexec

Swiss army knife for pentesting networks This package is a swiss army knife for pentesting Windows/Active Directory environments. From enumerating logged on users and spidering SMB shares to executing psexec style attacks, auto-injecting Mimikatz/Shellcode/DLL’s into memory using Powershell, dumping the NTDS.dit and more.

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/crackmapexec/> |
| 版本 | 5.4.0 |
| 包 / 命令 | `crackmapexec`、`cmedb` |
| 安装 | `sudo apt install crackmapexec` |
| 占用空间 | 2.29 MB |
| 依赖 | `python3`、`python3-aardwolf`、`python3-aioconsole`、`python3-bs4`、`python3-dsinternals`、`python3-impacket`、`python3-lsassy`、`python3-masky`、`python3-msgpack`、`python3-neo4j`、`python3-paramiko`、`python3-pylnk3` 等 |
| 官网 | <https://github.com/mpgn/CrackMapExec> |
| 源码 | <https://gitlab.com/kalilinux/packages/crackmapexec> |

### cri-tools

Command line tool used for creating OCI images This package contains a series of debugging and validation tools for Kubelet CRI, which includes: crictl: CLI for kubelet CRI. critest: validation test suites for kubelet CRI.

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/cri-tools/> |
| 版本 | 1.36.0 |
| 包 / 命令 | `cri-tools`、`crictl`、`critest` |
| 安装 | `sudo apt install cri-tools` |
| 占用空间 | 53.62 MB |
| 官网 | <https://github.com/kubernetes-sigs/cri-tools> |
| 源码 | <https://gitlab.com/kalilinux/packages/cri-tools> |

### crlfuzz

Fast tool to scan CRLF vulnerability written in Go CRLFuzz is a tool to scan for CRLF vulnerabilities in a fast way using Go

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/crlfuzz/> |
| 版本 | 1.4.1 |
| 包 / 命令 | `crlfuzz` |
| 安装 | `sudo apt install crlfuzz` |
| 占用空间 | 5.48 MB |
| 依赖 | `libc6`、`crlfuzz` |
| 官网 | <https://github.com/dwisiswant0/crlfuzz> |
| 源码 | <https://gitlab.com/kalilinux/packages/crlfuzz> |

### crowbar

Brute forcing tool This package contains Crowbar (formally known as Levye). It is a brute forcing tool that can be used during penetration tests. It was developed to brute force some protocols in a different manner according to other popular brute forcing tools. As an example, while most brute forcing tools use username and password for SSH brute force, Crowbar uses SSH key(s). This allows for any private keys

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/crowbar/> |
| 版本 | 4.2 |
| 包 / 命令 | `crowbar` |
| 安装 | `sudo apt install crowbar` |
| 占用空间 | 450 KB |
| 依赖 | `freerdp3-x11`、`openvpn`、`python3`、`python3-nmap`、`python3-paramiko`、`vncviewer`、`crowbar` |
| 官网 | <https://github.com/galkan/crowbar> |
| 源码 | <https://gitlab.com/kalilinux/packages/crowbar> |

### cryptcat

Lightweight version netcat extended with twofish encryption Cryptcat is a simple Unix utility which reads and writes data across network connections, using TCP or UDP protocol while encrypting the data being transmitted. It is designed to be a reliable “back-end” tool that can be used directly or easily driven by other programs and scripts. At the same time, it is a

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/cryptcat/> |
| 版本 | 20031202 |
| 包 / 命令 | `cryptcat` |
| 安装 | `sudo apt install cryptcat` |
| 占用空间 | 80 KB |
| 依赖 | `libc6`、`libgcc-s1`、`libstdc++6`、`cryptcat` |
| 官网 | <http://farm9.com/content/Free_Tools/cryptcat_linux2.tar> |
| 源码 | <https://gitlab.com/kalilinux/packages/cryptcat> |

### cupid-wpa

Fork of hostapd to exploit hertbleed vulnerability on wireless networks cupid-hostapd provide a binary of the same name that has been patched to exploit the heartbleed vulnerability over EAP TLS tunneled protocols (EAP-PEAP, EAP-TLS, EAP-TTLS) in use in wireless networks. With cupid-hostapd you can setup a fake wireless network to exploit the vulnerability of terminals that try to connect to it.

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/cupid-wpa/> |
| 版本 | 2.1 |
| 包 / 命令 | `cupid-hostapd`、`cupid-hostapd_cli`、`cupid-wpasupplicant`、`cupid-wpa_cli`、`cupid-wpa_passphrase`、`cupid-wpa_supplicant` |
| 安装 | `sudo apt install cupid-hostapd` |
| 占用空间 | 752 KB |
| 依赖 | `libc6`、`libnl-3-200`、`libnl-genl-3-200`、`libunsafessl1.0.2`、`cupid-hostapd` |
| 官网 | <https://github.com/lgrangeia/cupid/> |
| 源码 | <https://gitlab.com/kalilinux/packages/cupid-wpa> |

### dalfox

Powerful open-source XSS scanner and utility focused on automation Dalfox is a powerful open-source tool that focuses on automation, making it ideal for quickly scanning for XSS flaws and analyzing parameters. Its advanced testing engine and niche features are designed to streamline the process of detecting and verifying vulnerabilities.

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/dalfox/> |
| 版本 | 3.2.2 |
| 包 / 命令 | `dalfox` |
| 安装 | `sudo apt install dalfox` |
| 占用空间 | 13.96 MB |
| 依赖 | `libc6`、`libgcc-s1`、`dalfox` |
| 官网 | <https://github.com/hahwul/dalfox> |
| 源码 | <https://gitlab.com/kalilinux/packages/dalfox> |

### dbeaver

Universal Database Manager and SQL Client This package contains DBeaver Community Edition. It’s Free multi-platform database tool for developers, SQL programmers, database administrators and analysts. Supports all popular databases: MySQL, PostgreSQL, SQLite, Oracle, DB2, SQL Server, Sybase, Teradata, Cassandra.

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/dbeaver/> |
| 版本 | 26.1.3 |
| 包 / 命令 | `dbeaver` |
| 安装 | `sudo apt install dbeaver` |
| 占用空间 | 101.18 MB |
| 依赖 | `default-jre`、`dbeaver` |
| 官网 | <http://dbeaver.jkiss.org/> |
| 源码 | <https://gitlab.com/kalilinux/packages/dbeaver> |

### detect-it-easy

Program for determining types of files Detect It Easy (DiE) is a powerful tool for file type identification, popular among malware analysts, cybersecurity experts, and reverse engineers worldwide. Supporting both signature-based and heuristic analysis, DiE enables efficient file inspections across a broad range of platforms, including Windows, Linux, and MacOS. Its adaptable, script-driven detection architecture

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/detect-it-easy/> |
| 版本 | 3.21 |
| 包 / 命令 | `detect-it-easy`、`die`、`diec`、`diel` |
| 安装 | `sudo apt install detect-it-easy` |
| 占用空间 | 41.40 MB |
| 依赖 | `libc6`、`libgcc-s1`、`libqt5concurrent5t64`、`libqt5core5t64` |
| 官网 | <https://github.com/horsicq/Detect-It-Easy> |
| 源码 | <https://gitlab.com/kalilinux/packages/detectiteasy> |

### dirsearch

Web path scanner This package contains is a command-line tool designed to brute force directories and files in webservers. As a feature-rich tool, dirsearch gives users the opportunity to perform a complex web content discovering, with many vectors for the wordlist, high accuracy, impressive performance, advanced connection/request settings, modern

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/dirsearch/> |
| 版本 | 0.4.3 |
| 包 / 命令 | `dirsearch` |
| 安装 | `sudo apt install dirsearch` |
| 占用空间 | 447 KB |
| 依赖 | `python3`、`python3-bs4`、`python3-certifi`、`python3-cffi`、`python3-chardet`、`python3-charset-normalizer`、`python3-colorama`、`python3-cryptography`、`python3-defusedxml`、`python3-idna`、`python3-jinja2`、`python3-markupsafe` 等 |
| 官网 | <https://github.com/maurosoria/dirsearch> |
| 源码 | <https://salsa.debian.org/pkg-security-team/dirsearch> |

### dislocker

Read/write encrypted BitLocker volumes Dislocker has been designed to read BitLocker encrypted partitions under a Linux system. The driver used to read volumes encrypted in Windows system versions of the Vista to 10 and BitLocker-To-Go encrypted partitions, that’s USB/FAT32 partitions. The software works with driver composed of a library, with multiple binaries

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/dislocker/> |
| 版本 | 0.7.3 |
| 包 / 命令 | `dislocker`、`dislocker-bek`、`dislocker-file`、`dislocker-find`、`dislocker-fuse`、`dislocker-metadata`、`libdislocker0-dev`、`libdislocker0.7t64` |
| 安装 | `sudo apt install dislocker` |
| 占用空间 | 95 KB |
| 依赖 | `libc6`、`libdislocker0.7t64`、`libfuse3-4`、`libruby3.3`、`dislocker` |
| 官网 | <https://github.com/Aorimn/dislocker> |
| 源码 | <https://salsa.debian.org/pkg-security-team/dislocker> |

### dnscat2

DNS tunnel (metapackage) This tool is designed to create an encrypted command-and-control (C&C) channel over the DNS protocol, which is an effective tunnel out of almost every network.

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/dnscat2/> |
| 版本 | 0.07 |
| 包 / 命令 | `dnscat2`、`dnscat2-client`、`dnscat`、`dnscat2-server` |
| 安装 | `sudo apt install dnscat2` |
| 占用空间 | 16 KB |
| 依赖 | `dnscat2-client`、`dnscat2-server`、`dnscat2-client` |
| 官网 | <https://github.com/iagox86/dnscat2> |
| 源码 | <https://gitlab.com/kalilinux/packages/dnscat2> |

### dnsgen

DNS generator This package provides a generator of a combination of domain names from the provided input. Combinations are created based on wordlist. Custom words are extracted per execution.

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/dnsgen/> |
| 版本 | 1.0.4 |
| 包 / 命令 | `dnsgen` |
| 安装 | `sudo apt install dnsgen` |
| 占用空间 | 37 KB |
| 依赖 | `python3`、`python3-click`、`python3-tldextract`、`dnsgen` |
| 官网 | <https://github.com/ProjectAnte/dnsgen> |
| 源码 | <https://gitlab.com/kalilinux/packages/dnsgen> |

### dnstwist

Domain name permutation engine dnstwist generates a list of similarly looking domain names for a given domain name and performs DNS queries for them (A, AAAA, NS and MX). For MX records it checks whether there is an active mail server which could be used to intercept misdirected emails. Additionally it estimates webpage similarity based on fuzzy hashes.

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/dnstwist/> |
| 版本 | 0~20250130 |
| 包 / 命令 | `dnstwist` |
| 安装 | `sudo apt install dnstwist` |
| 占用空间 | 489 KB |
| 依赖 | `python3`、`dnstwist` |
| 官网 | <https://github.com/elceef/dnstwist> |
| 源码 | <https://salsa.debian.org/pkg-security-team/dnstwist> |

### dnsx

Perform multiple dns queries This package contains a fast and multi-purpose DNS toolkit allow to run multiple probes using retryabledns library, that allows you to perform multiple DNS queries of your choice with a list of user supplied resolvers, additionally supports DNS wildcard filtering like shuffledns (

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/dnsx/> |
| 版本 | 1.3.1 |
| 包 / 命令 | `dnsx` |
| 安装 | `sudo apt install dnsx` |
| 占用空间 | 27.80 MB |
| 依赖 | `libc6`、`dnsx` |
| 官网 | <https://github.com/projectdiscovery/dnsx> |
| 源码 | <https://gitlab.com/kalilinux/packages/dnsx> |

### donut-shellcode

Generates position-independent shellcode from memory and runs them Donut is a position-independent code that enables in-memory execution of VBScript, JScript, EXE, DLL files and dotNET assemblies. A module created by Donut can either be staged from a HTTP server or embedded directly in the loader itself. The module is optionally encrypted using the Chaskey block cipher and a 128-bit randomly generated key. After the file is loaded and

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/donut-shellcode/> |
| 版本 | 1.1 |
| 包 / 命令 | `donut`、`python-donut-doc`、`python3-donut` |
| 安装 | `sudo apt install donut` |
| 占用空间 | 86 KB |
| 依赖 | `libc6`、`donut` |
| 官网 | <https://github.com/TheWover/donut> |
| 源码 | <https://gitlab.com/kalilinux/packages/donut-shellcode> |

### doona

Network fuzzer forked from bed Doona is a fork of the Bruteforce Exploit Detector Tool (BED). BED is a program which is designed to check daemons for potential buffer overflows, format string bugs etc.

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/doona/> |
| 版本 | 1.0 |
| 包 / 命令 | `doona` |
| 安装 | `sudo apt install doona` |
| 占用空间 | 128 KB |
| 依赖 | `perl`、`doona` |
| 官网 | <https://github.com/wireghoul/doona> |
| 源码 | <https://salsa.debian.org/pkg-security-team/doona> |

### dos2unix

Convert text file line endings between CRLF and LF This package contains utilities dos2unix, unix2dos, mac2unix, unix2mac to convert the line endings of text files between UNIX (LF), DOS (CRLF) and Mac (CR) formats. Text files under Windows and DOS typically have two ASCII characters at the end of each line: CR (carriage return) followed by LF (line

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/dos2unix/> |
| 版本 | 7.5.4 |
| 包 / 命令 | `dos2unix`、`mac2unix`、`unix2dos`、`unix2mac` |
| 安装 | `sudo apt install dos2unix` |
| 占用空间 | 1.54 MB |
| 依赖 | `libc6`、`dos2unix` |
| 官网 | <https://waterlan.home.xs4all.nl/dos2unix.html> |
| 源码 | <https://salsa.debian.org/debian/dos2unix> |

### dscan

Wrapper around nmap This package provides a wrapper around nmap, and distribute scans across several hosts. It aggregates / splits address ranges, uses a configuration file where scan configuration can be adjusted, supports resume.

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/dscan/> |
| 版本 | 0.1.5 |
| 包 / 命令 | `dscan`、`dscan-doc` |
| 安装 | `sudo apt install dscan` |
| 占用空间 | 95 KB |
| 依赖 | `python3`、`python3-libnmap`、`dscan` |
| 官网 | <https://github.com/0x4E0x650x6F/dscan> |
| 源码 | <https://gitlab.com/kalilinux/packages/dscan> |

### dufflebag

Search exposed EBS volumes for secrets (program) Dufflebag is a tool that searches through public Elastic Block Storage (EBS) snapshots for secrets that may have been accidentally left in. The tool is organized as an Elastic Beanstalk (“EB”, not to be confused with EBS) application, and definitely won’t work if you try to run it on your own machine.

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/dufflebag/> |
| 版本 | 0.0~git20200205.9a01942 |
| 包 / 命令 | `dufflebag` |
| 安装 | `sudo apt install dufflebag` |
| 占用空间 | 5.90 MB |
| 依赖 | `golang-any`、`golang-github-aws-aws-sdk-go-dev`、`golang-github-deckarep-golang-set-dev`、`golang-lukechampine-blake3-dev`、`make`、`sensible-utils`、`zip`、`dufflebag` |
| 官网 | <https://github.com/BishopFox/dufflebag> |
| 源码 | <https://gitlab.com/kalilinux/packages/dufflebag> |

### dumpsterdiver

Tool to analyze big volumes of data in search of hardcoded secrets This package contains a tool, which can analyze big volumes of data in search of hardcoded secrets like keys (e.g. AWS Access Key, Azure Share Key or SSH keys) or passwords. Additionally, it allows creating a simple search rules with basic conditions (e.g. report only csv files including at least 10 email addresses).

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/dumpsterdiver/> |
| 版本 | 0~git20210628.058087e |
| 包 / 命令 | `dumpsterdiver` |
| 安装 | `sudo apt install dumpsterdiver` |
| 占用空间 | 44 KB |
| 依赖 | `python3`、`python3-colorama`、`python3-passwordmeter`、`python3-termcolor`、`python3-yaml` |
| 官网 | <https://github.com/securing/DumpsterDiver> |
| 源码 | <https://gitlab.com/kalilinux/packages/dumpsterdiver> |

### dvwa

Damn Vulnerable Web Application This package contains a PHP/MySQL web application that is damn vulnerable. Its main goal is to be an aid for security professionals to test their skills and tools in a legal environment, help web developers better understand the processes of securing web applications and to aid both students & teachers to learn about web application security in a controlled class room environment.

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/dvwa/> |
| 版本 | 2.5 |
| 包 / 命令 | `dvwa`、`dvwa-start`、`dvwa-stop` |
| 安装 | `sudo apt install dvwa` |
| 占用空间 | 1.70 MB |
| 依赖 | `adduser`、`apache2`、`kali-defaults`、`libapache2-mod-php`、`mariadb-server`、`nginx`、`php8.4`、`php8.4-fpm`、`php8.4-gd`、`php8.4-mysql`、`sudo`、`dvwa-start` |
| 官网 | <https://github.com/digininja/DVWA> |
| 源码 | <https://gitlab.com/kalilinux/packages/dvwa> |

### dwarf2json

Utility to generat volatility 3 Intermediate Symbol File (ISF) JSON This package contains a Go utility that processes files containing symbol and type information to generate Volatilty3 Intermediate Symbol File (ISF) JSON output suitable for Linux and macOS analysis.

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/dwarf2json/> |
| 版本 | 0.6.0~git20200714 |
| 包 / 命令 | `dwarf2json` |
| 安装 | `sudo apt install dwarf2json` |
| 占用空间 | 2.53 MB |
| 依赖 | `libc6`、`dwarf2json` |
| 官网 | <https://github.com/volatilityfoundation/dwarf2json> |
| 源码 | <https://gitlab.com/kalilinux/packages/dwarf2json> |

### eaphammer

Toolkit for targeted evil twin attacks against WPA2-Enterprise networks This package contains a toolkit for performing targeted evil twin attacks against WPA2-Enterprise networks. It is designed to be used in full scope wireless assessments and red team engagements. As such, focus is placed on providing an easy-to-use interface that can be leveraged to execute powerful wireless attacks with minimal manual configuration. To illustrate just how

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/eaphammer/> |
| 版本 | 1.14.0 |
| 包 / 命令 | `eaphammer` |
| 安装 | `sudo apt install eaphammer` |
| 占用空间 | 11.41 MB |
| 依赖 | `apache2`、`asleap`、`dnsmasq`、`hcxdumptool`、`hcxtools`、`iptables`、`libc6`、`libnl-3-200`、`libnl-genl-3-200`、`python3`、`python3-bs4`、`python3-flask-cors` 等 |
| 官网 | <https://github.com/s0lst1c3/eaphammer> |
| 源码 | <https://gitlab.com/kalilinux/packages/eaphammer> |

### eksctl

Official CLI for Amazon EKS (program) eksctl is a simple CLI tool for creating clusters on EKS - Amazon’s new managed Kubernetes service for EC2. It is written in Go, and uses CloudFormation. You can create a cluster in minutes with just one command –

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/eksctl/> |
| 版本 | 0.230.0 |
| 包 / 命令 | `eksctl` |
| 安装 | `sudo apt install eksctl` |
| 占用空间 | 146.11 MB |
| 官网 | <https://github.com/weaveworks/eksctl> |
| 源码 | <https://gitlab.com/kalilinux/packages/eksctl> |

### email2phonenumber

OSINT tool to obtain a target’s phone number by having their email address This package contains an OSINT tool that allows you to obtain a target’s phone number just by having their email address. This tool helps automate discovering someone’s phone number by abusing password reset design weaknesses and publicly available data. It supports 3 main functions:

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/email2phonenumber/> |
| 版本 | 0~git20220216 |
| 包 / 命令 | `email2phonenumber` |
| 安装 | `sudo apt install email2phonenumber` |
| 占用空间 | 72 KB |
| 依赖 | `python3`、`python3-bs4`、`python3-certifi`、`python3-chardet`、`python3-idna`、`python3-requests`、`python3-soupsieve`、`python3-urllib3`、`email2phonenumber` |
| 官网 | <https://github.com/martinvigo/email2phonenumber> |
| 源码 | <https://gitlab.com/kalilinux/packages/email2phonenumber> |

### emailharvester

Email addresses harvester This package contains EmailHarvester, a tool to retrieve Domain email addresses from Search Engines. Features: Retrieve Domain email addresses from popular Search engines (Google, Bing, Yahoo, ASK, Baidu, Dogpile, Exalead) Export results to txt and xml files

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/emailharvester/> |
| 版本 | 1.3.2 |
| 包 / 命令 | `emailharvester` |
| 安装 | `sudo apt install emailharvester` |
| 占用空间 | 70 KB |
| 依赖 | `python3`、`python3-colorama`、`python3-requests`、`python3-termcolor`、`python3-validators`、`emailharvester` |
| 官网 | <https://github.com/maldevel/EmailHarvester> |
| 源码 | <https://gitlab.com/kalilinux/packages/emailharvester> |

### enum4linux-ng

Next generation version of enum4linux Next generation version of enum4linux (a Windows/Samba enumeration tool) with additional features like JSON/YAML export. Aimed for security professionals and CTF players.

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/enum4linux-ng/> |
| 版本 | 1.3.10 |
| 包 / 命令 | `enum4linux-ng` |
| 安装 | `sudo apt install enum4linux-ng` |
| 占用空间 | 193 KB |
| 依赖 | `python3`、`python3-impacket`、`python3-ldap3`、`python3-yaml`、`samba-common-bin`、`smbclient`、`enum4linux-ng` |
| 官网 | <https://github.com/cddmp/enum4linux-ng> |
| 源码 | <https://gitlab.com/kalilinux/packages/enum4linux-ng> |

### evil-ssdp

Spoof SSDP replies to phish for NTLM hashes on a network This tool responds to SSDP multicast discover requests, posing as a generic UPNP device on a local network. Your spoofed device will magically appear in Windows Explorer on machines in your local network. Users who are tempted to open the device are shown a configurable webpage.

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/evil-ssdp/> |
| 版本 | 0.8~beta |
| 包 / 命令 | `evil-ssdp` |
| 安装 | `sudo apt install evil-ssdp` |
| 占用空间 | 100 KB |
| 依赖 | `python3`、`evil-ssdp` |
| 官网 | <https://github.com/initstring/evil-ssdp> |
| 源码 | <https://gitlab.com/kalilinux/packages/evil-ssdp> |

### evil-winrm

Ultimate WinRM shell for hacking/pentesting This package contains the ultimate WinRM shell for hacking/pentesting. WinRM (Windows Remote Management) is the Microsoft implementation of WS-Management Protocol. A standard SOAP based protocol that allows hardware and operating systems from different vendors to interoperate. Microsoft included it in their Operating Systems in order to make life easier to system

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/evil-winrm/> |
| 版本 | 4.1 |
| 包 / 命令 | `evil-winrm` |
| 安装 | `sudo apt install evil-winrm` |
| 占用空间 | 176 KB |
| 依赖 | `ruby`、`ruby-benchmark`、`ruby-csv`、`ruby-fileutils`、`ruby-logger`、`ruby-stringio`、`ruby-syslog`、`ruby-winrm`、`ruby-winrm-fs`、`evil-winrm` |
| 官网 | <https://github.com/Hackplayers/evil-winrm> |
| 源码 | <https://gitlab.com/kalilinux/packages/evil-winrm> |

### evil-winrm-py

Execute commands on remote Windows machines using WinRM Python-based tool for executing commands on remote Windows machines using the WinRM (Windows Remote Management) protocol. It provides an interactive shell with enhanced features like file upload/download, command history, and colorized output. It supports various authentication methods including NTLM, Pass-the-Hash, Certificate, and Kerberos.

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/evil-winrm-py/> |
| 版本 | 1.6.0 |
| 包 / 命令 | `evil-winrm-py`、`ewp` |
| 安装 | `sudo apt install evil-winrm-py` |
| 占用空间 | 133 KB |
| 依赖 | `python3`、`python3-kerberos`、`python3-prompt-toolkit`、`python3-pypsrp`、`python3-tqdm`、`evil-winrm-py` |
| 官网 | <https://github.com/adityatelange/evil-winrm-py> |
| 源码 | <https://gitlab.com/kalilinux/packages/evil-winrm-py> |

### evilginx2

Man-in-the-middle attack framework This package contains a man-in-the-middle attack framework used for phishing login credentials along with session cookies, which in turn allows to bypass 2-factor authentication protection. This tool is a successor to Evilginx, released in 2017, which used a custom version of nginx HTTP server to provide man-in-the-middle functionality to act

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/evilginx2/> |
| 版本 | 3.3.0 |
| 包 / 命令 | `evilginx2` |
| 安装 | `sudo apt install evilginx2` |
| 占用空间 | 10.13 MB |
| 依赖 | `libc6`、`evilginx2` |
| 官网 | <https://github.com/kgretzky/evilginx2> |
| 源码 | <https://gitlab.com/kalilinux/packages/evilginx2> |

### exiflooter

Finds geolocation on all image urls and directories ExifLooter finds geolocation on all image urls and directories also integrates with OpenStreetMap.

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/exiflooter/> |
| 版本 | 1.0.0 |
| 包 / 命令 | `exiflooter` |
| 安装 | `sudo apt install exiflooter` |
| 占用空间 | 6.06 MB |
| 依赖 | `libc6`、`libimage-exiftool-perl`、`exiflooter` |
| 官网 | <https://github.com/aydinnyunus/exiflooter> |
| 源码 | <https://gitlab.com/kalilinux/packages/exiflooter> |

### expect

Automates interactive applications Expect is a tool for automating interactive applications according to a script. Following the script, Expect knows what can be expected from a program and what the correct response should be. Expect is also useful for testing these same applications. And by adding Tk, you can also wrap interactive applications in X11 GUIs. An interpreted language provides branching and high-level control

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/expect/> |
| 版本 | 5.45.4 |
| 包 / 命令 | `expect`、`autoexpect`、`autopasswd`、`cryptdir`、`decryptdir`、`dislocate`、`expect8.6`、`expect9.0`、`expect_autoexpect`、`expect_autopasswd`、`expect_cryptdir`、`expect_decryptdir`、`expect_dislocate`、`expect_kibitz`、`expect_lpunlock`、`expect_mkpasswd`、`expect_multixterm`、`expect_passmass`、`expect_rftp`、`expect_rlogin-cwd`、`expect_timed-read`、`expect_timed-run`、`expect_tknewsbiff`、`expect_tkpasswd`、`expect_unbuffer`、`expect_weather`、`expect_xkibitz`、`expect_xpstat`、`kibitz`、`lpunlock`、`multixterm`、`passmass`、`rlogin-cwd`、`timed-read`、`timed-run`、`tknewsbiff`、`tkpasswd`、`unbuffer`、`xkibitz`、`xpstat`、`tcl-expect`、`tcl-expect-dev` |
| 安装 | `sudo apt install expect` |
| 占用空间 | 324 KB |
| 依赖 | `libc6`、`libtcl8.6`、`libtcl9.0`、`tcl-expect`、`tcl8.6`、`tcl9.0`、`autoexpect` |
| 官网 | <https://core.tcl.tk/expect/> |
| 源码 | <https://salsa.debian.org/tcltk-team/expect> |

### exploitdb-bin-sploits

The Exploit Database’s archive of binary exploits Searchable binary exploits from The Exploit Database. https://www.exploit-db.com

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/exploitdb-bin-sploits/> |
| 版本 | 20221122 |
| 包 / 命令 | `exploitdb-bin-sploits`、`exploitdb-bin-sploit` |
| 安装 | `sudo apt install exploitdb-bin-sploits` |
| 占用空间 | 1.07 GB |
| 依赖 | `kali-defaults`、`exploitdb-bin-sploit` |
| 官网 | <https://www.exploit-db.com> |
| 源码 | <https://gitlab.com/kalilinux/packages/exploitdb-bin-sploits> |

### exploitdb-papers

The Exploit Database’s archive of papers & ezines Searchable papers & ezines archives from The Exploit Database. https://www.exploit-db.com/papers

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/exploitdb-papers/> |
| 版本 | 20221122 |
| 包 / 命令 | `exploitdb-papers` |
| 安装 | `sudo apt install exploitdb-papers` |
| 占用空间 | 2.74 GB |
| 依赖 | `kali-defaults`、`exploitdb-papers` |
| 官网 | <https://www.exploit-db.com> |
| 源码 | <https://gitlab.com/kalilinux/packages/exploitdb-papers> |

### faraday-agent-dispatcher

Helper to develop integrations with Faraday (Python 3) This package contains Faraday Agents Dispatcher. It helps user develop integrations with Faraday written in any language. This package installs the library for Python 3.

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/faraday-agent-dispatcher/> |
| 版本 | 3.2.1 |
| 包 / 命令 | `faraday-agent-dispatcher`、`faraday-dispatcher` |
| 安装 | `sudo apt install faraday-agent-dispatcher` |
| 占用空间 | 284 KB |
| 依赖 | `python3`、`python3-aiohttp`、`python3-click`、`python3-faraday-agent-parameters-types`、`python3-faraday-plugins`、`python3-gvm`、`python3-itsdangerous`、`python3-psutil`、`python3-requests`、`python3-socketio`、`python3-syslog-rfc5424-formatter`、`python3-websockets` 等 |
| 官网 | <https://github.com/infobyte/faraday_agent_dispatcher> |
| 源码 | <https://gitlab.com/kalilinux/packages/faraday-agent-dispatcher> |

### faraday-cli

Faraday on the terminal This package contains the official client that make automating your security workflows, easier.

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/faraday-cli/> |
| 版本 | 2.2.2 |
| 包 / 命令 | `faraday-cli` |
| 安装 | `sudo apt install faraday-cli` |
| 占用空间 | 812 KB |
| 依赖 | `faraday`、`python3`、`python3-arrow`、`python3-click`、`python3-cmd2`、`python3-colorama`、`python3-faraday-plugins`、`python3-httpx`、`python3-jsonschema`、`python3-log-symbols`、`python3-packaging`、`python3-py-sneakers` 等 |
| 官网 | <https://github.com/infobyte/faraday-cli> |
| 源码 | <https://gitlab.com/kalilinux/packages/faraday-cli> |

### fatcat

FAT filesystem explore, extract, repair, and forensic tool fatcat is a tool to explore, extract, repair and forensic FAT filesystem. Its features: - Get information about FAT filesystem; - Explore FAT file system; - Read file or extract directories;

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/fatcat/> |
| 版本 | 1.1.1 |
| 包 / 命令 | `fatcat` |
| 安装 | `sudo apt install fatcat` |
| 占用空间 | 141 KB |
| 依赖 | `libc6`、`libgcc-s1`、`libstdc++6`、`fatcat` |
| 官网 | <https://github.com/Gregwar/fatcat> |
| 源码 | <https://salsa.debian.org/pkg-security-team/fatcat> |

### ffuf

Fast web fuzzer written in Go (program) ffuf is a fast web fuzzer written in Go that allows typical directory discovery, virtual host discovery (without DNS records) and GET and POST parameter fuzzing. This program is useful for pentesters, ethical hackers and forensics experts. It also can be used for security tests.

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/ffuf/> |
| 版本 | 2.2.1 |
| 包 / 命令 | `ffuf` |
| 安装 | `sudo apt install ffuf` |
| 占用空间 | 9.48 MB |
| 依赖 | `libc6`、`ffuf` |
| 官网 | <https://github.com/ffuf/ffuf> |
| 源码 | <https://salsa.debian.org/debian/ffuf/> |

### finalrecon

Fast and simple Python script for web reconnaissance A fast and simple Python script for web reconnaissance that follows a modular structure and provides detailed information on various areas.

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/finalrecon/> |
| 版本 | 1.1.8 |
| 包 / 命令 | `finalrecon` |
| 安装 | `sudo apt install finalrecon` |
| 占用空间 | 420 KB |
| 依赖 | `python3`、`python3-aiodns`、`python3-aiohttp`、`python3-bs4`、`python3-cryptography`、`python3-dnspython`、`python3-lxml`、`python3-requests`、`python3-tldextract`、`finalrecon` |
| 官网 | <https://github.com/thewhiteh4t/FinalRecon> |
| 源码 | <https://gitlab.com/kalilinux/packages/finalrecon> |

### findomain

Fastest and most complete solution for domain recognition Findomain is fastest and most complete solution for domain recognition. It supports screenshoting, port scanning, HTTP checks, data imports from other tools, subdomain monitoring, alerts via Discord, Slack & Telegram, multiple API Keys for sourcing and much more.

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/findomain/> |
| 版本 | 10.0.1 |
| 包 / 命令 | `findomain` |
| 安装 | `sudo apt install findomain` |
| 占用空间 | 18.61 MB |
| 依赖 | `chromium`、`libc6`、`libgcc-s1`、`postgresql`、`findomain` |
| 官网 | <https://github.com/Findomain/Findomain> |
| 源码 | <https://gitlab.com/kalilinux/packages/findomain> |

### firefox-developer-edition-kbx

Mozilla Firefox web browser - Developer Edition - en-US Firefox is a powerful, extensible web browser with support for modern web application technologies. This is the Developer Edition, running in a container with help from kaboxer, localized for en-US

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/firefox-developer-edition-kbx/> |
| 版本 | 0~2023.05.1 |
| 包 / 命令 | `firefox-developer-edition-en-us-kbx` |
| 安装 | `sudo apt install firefox-developer-edition-en-us-kbx` |
| 占用空间 | 35 KB |
| 官网 | <https://www.mozilla.org/en-US/firefox/developer/> |
| 源码 | <https://gitlab.com/kalilinux/packages/firefox-developer-edition-kbx> |

### fluxion

Security auditing and social-engineering research tool Fluxion is a security auditing and social-engineering research tool. It is a remake of linset by vk496 with (hopefully) fewer bugs and more functionality. The script attempts to retrieve the WPA/WPA2 key from a target access point by means of a social engineering (phishing) attack. It’s compatible with the latest release of Kali (rolling). Fluxion’s attacks’ setup is mostly manual,

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/fluxion/> |
| 版本 | 6.31 |
| 包 / 命令 | `fluxion` |
| 安装 | `sudo apt install fluxion` |
| 占用空间 | 24.30 MB |
| 依赖 | `7zip`、`aircrack-ng`、`bc`、`cowpatty`、`curl`、`dsniff`、`gawk`、`hostapd`、`isc-dhcp-server`、`iw`、`lighttpd`、`macchanger` 等 |
| 官网 | <https://github.com/FluxionNetwork/fluxion> |
| 源码 | <https://gitlab.com/kalilinux/packages/fluxion> |

### framework2

Metasploit Framework 2 Version 2 of the Metasploit Framework. No longer updated but still useful, particularly for shellcode.

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/framework2/> |
| 版本 | 2.0 |
| 包 / 命令 | `framework2` |
| 安装 | `sudo apt install framework2` |
| 占用空间 | 7.82 MB |
| 依赖 | `kali-defaults`、`perl`、`framework2` |
| 官网 | <https://www.metasploit.com> |
| 源码 | <https://gitlab.com/kalilinux/packages/framework2> |

### freeradius

High-performance and highly configurable RADIUS server FreeRADIUS is a high-performance RADIUS server with support for: Authentication by local files, SQL, Kerberos, LDAP, PAM, and more. Powerful policy configuration language. Proxying and replicating requests by any criteria. Support for many EAP types; TLS, PEAP, TTLS, etc.

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/freeradius/> |
| 版本 | 3.2.10 |
| 包 / 命令 | `freeradius`、`checkrad`、`rad_counter`、`raddebug`、`radmin`、`rlm_sqlippool_tool`、`freeradius-common`、`freeradius-config`、`freeradius-dhcp`、`freeradius-iodbc`、`freeradius-krb5`、`freeradius-ldap`、`freeradius-memcached`、`freeradius-mysql`、`freeradius-postgresql`、`freeradius-python3`、`freeradius-redis`、`freeradius-rest`、`freeradius-utils`、`radclient`、`radconf2json`、`radcrypt`、`raddict2json`、`radeapclient`、`radlast`、`radmod2json`、`radsecret`、`radsniff`、`radsqlrelay`、`radtest`、`radwho`、`radzap`、`rlm_ippool_tool`、`smbencrypt`、`freeradius-yubikey`、`libfreeradius-dev`、`libfreeradius3` |
| 安装 | `sudo apt install freeradius` |
| 占用空间 | 3.38 MB |
| 依赖 | `freeradius-common`、`freeradius-config`、`libc6`、`libcrypt1`、`libct4`、`libfreeradius3`、`libgdbm6t64`、`libjson-c5`、`libpam0g`、`libperl5.42`、`libreadline8t64`、`libsqlite3-0` 等 |
| 官网 | <http://www.freeradius.org/> |
| 源码 | <https://salsa.debian.org/debian/freeradius> |

### gdb-peda

Python Exploit Development Assistance for GDB This package contains a Python GDB script with many handy commands to help speed up exploit development process on Linux/Unix. It is also a framework for writing custom interactive Python GDB commands.

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/gdb-peda/> |
| 版本 | 1.2 |
| 包 / 命令 | `gdb-peda` |
| 安装 | `sudo apt install gdb-peda` |
| 占用空间 | 319 KB |
| 依赖 | `gdb` |
| 官网 | <https://github.com/longld/peda> |
| 源码 | <https://gitlab.com/kalilinux/packages/gdb-peda> |

### gdisk

GPT fdisk text-mode partitioning tool GPT fdisk (aka gdisk) is a text-mode partitioning tool that provides utilities for Globally Unique Identifier (GUID) Partition Table (GPT) disks. Features: Edit GUID partition table definitions

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/gdisk/> |
| 版本 | 1.0.10 |
| 包 / 命令 | `gdisk`、`cgdisk`、`fixparts`、`sgdisk` |
| 安装 | `sudo apt install gdisk` |
| 占用空间 | 967 KB |
| 依赖 | `libc6`、`libgcc-s1`、`libncursesw6`、`libpopt0`、`libstdc++6`、`libtinfo6`、`libuuid1`、`cgdisk` |
| 官网 | <http://sourceforge.net/projects/gptfdisk/> |
| 源码 | <https://salsa.debian.org/debian/gdisk> |

### gef

Modern experience for GDB with advanced debugging capabilities GEF is a set of commands for x86/64, ARM, MIPS, PowerPC and SPARC to assist exploit developers and reverse-engineers when using old school GDB. It provides additional features to GDB using the Python API to assist during the process of dynamic analysis and exploit development. Application developers will also benefit from it, as GEF lifts a great part of regular GDB obscurity,

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/gef/> |
| 版本 | 2026.01 |
| 包 / 命令 | `gef` |
| 安装 | `sudo apt install gef` |
| 占用空间 | 436 KB |
| 依赖 | `gdb`、`gef` |
| 官网 | <https://github.com/hugsy/gef> |
| 源码 | <https://gitlab.com/kalilinux/packages/gef> |

### gemini-cli

Open-source AI agent This package contains an open-source AI agent that brings the power of Gemini directly into your terminal. It provides lightweight access to Gemini, giving you the most direct path from your prompt to the model.

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/gemini-cli/> |
| 版本 | 0.58.0 |
| 包 / 命令 | `gemini-cli` |
| 安装 | `sudo apt install gemini-cli` |
| 占用空间 | 47.73 MB |
| 依赖 | `nodejs`、`gemini-cli` |
| 官网 | <https://github.com/google-gemini/gemini-cli> |
| 源码 | <https://gitlab.com/kalilinux/packages/gemini-cli> |

### getallurls

Fetch known URLs from AlienVault’s Open Threat Exchange (gau) This package contains getallurls (gau). It fetches known URLs from AlienVault’s Open Threat Exchange ( https://otx.alienvault.com ), the Wayback Machine, and Common Crawl for any given domain. Inspired by Tomnomnom’s

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/getallurls/> |
| 版本 | 1.0.7 |
| 包 / 命令 | `getallurls` |
| 安装 | `sudo apt install getallurls` |
| 占用空间 | 6.42 MB |
| 依赖 | `libc6`、`getallurls` |
| 官网 | <https://github.com/lc/gau> |
| 源码 | <https://gitlab.com/kalilinux/packages/getallurls> |

### getsploit

Command line utility for searching and downloading exploits Inspired by searchsploit, getsploit combines two features: command line search and download. It allows you to search online for the exploits across all the most popular collections, including (but not limited to): - Exploit-DB,

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/getsploit/> |
| 版本 | 2.0.2 |
| 包 / 命令 | `getsploit` |
| 安装 | `sudo apt install getsploit` |
| 占用空间 | 40 KB |
| 依赖 | `python3`、`python3-click`、`python3-httpx`、`python3-orjson`、`python3-texttable`、`getsploit` |
| 官网 | <https://github.com/vulnersCom/getsploit> |
| 源码 | <https://gitlab.com/kalilinux/packages/getsploit> |

### gitleaks

Protect and discover secrets using Gitleaks 🔑 (program) Gitleaks is a SAST tool for detecting and preventing hardcoded

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/gitleaks/> |
| 版本 | 8.26.0 |
| 包 / 命令 | `gitleaks`、`golang-github-gitleaks-gitleaks-dev` |
| 安装 | `sudo apt install gitleaks` |
| 占用空间 | 9.88 MB |
| 依赖 | `libc6`、`gitleaks` |
| 官网 | <https://github.com/gitleaks/gitleaks> |
| 源码 | <https://salsa.debian.org/go-team/packages/gitleaks> |

### gitxray

Scan GitHub repositories and contributors to collect data Gitxray (short for Git X-Ray) is a multifaceted security tool designed for use on GitHub repositories. It can serve many purposes, including OSINT and Forensics. gitxray leverages public GitHub REST APIs to gather information that would otherwise be very time-consuming to obtain manually. Additionally, it seeks out information in unconventional places.

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/gitxray/> |
| 版本 | 1.0.20 |
| 包 / 命令 | `gitxray` |
| 安装 | `sudo apt install gitxray` |
| 占用空间 | 382 KB |
| 依赖 | `python3`、`python3-requests`、`gitxray` |
| 官网 | <https://kulkansecurity.github.io/gitxray/> |
| 源码 | <https://gitlab.com/kalilinux/packages/gitxray> |

### gobuster

High-performance discovery tool for directories, DNS and cloud storage Gobuster is a high-performance tool used to brute-force and discover: URIs (directories and files) in web sites DNS subdomains (with wildcard support) Virtual Host names on target web servers Open Amazon S3 and Google Cloud Storage (GCS) buckets

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/gobuster/> |
| 版本 | 3.8.2 |
| 包 / 命令 | `gobuster` |
| 安装 | `sudo apt install gobuster` |
| 占用空间 | 9.17 MB |
| 依赖 | `libc6`、`gobuster` |
| 官网 | <https://github.com/OJ/gobuster> |
| 源码 | <https://salsa.debian.org/pkg-security-team/gobuster> |

### godoh

DNS-over-HTTPS Command & Control Proof of Concept This package contains a proof of concept Command and Control framework, written in Golang, that uses DNS-over-HTTPS as a transport medium. Currently supported providers include Google, Cloudflare but also contains the ability to use traditional DNS.

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/godoh/> |
| 版本 | 1.6 |
| 包 / 命令 | `godoh` |
| 安装 | `sudo apt install godoh` |
| 占用空间 | 7.42 MB |
| 依赖 | `libc6`、`godoh` |
| 官网 | <https://github.com/sensepost/goDoH> |
| 源码 | <https://gitlab.com/kalilinux/packages/godoh> |

### golang-github-binject-go-donut

Donut Injector in Go This package contains the Donut Injector ported to pure Go. This package provides the binary file go-donut generated by github-binject-go-donut.

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/golang-github-binject-go-donut/> |
| 版本 | 0.0~git20201215.d947cf4 |
| 包 / 命令 | `golang-github-binject-go-donut`、`go-donut`、`golang-github-binject-go-donut-dev` |
| 安装 | `sudo apt install golang-github-binject-go-donut` |
| 占用空间 | 4.76 MB |
| 依赖 | `libc6`、`go-donut` |
| 官网 | <https://github.com/Binject/go-donut> |
| 源码 | <https://gitlab.com/kalilinux/packages/golang-github-binject-go-donut> |

### goldeneye

HTTP DoS test tool GoldenEye is a HTTP DoS Test Tool. This tool can be used to test if a site is susceptible to Deny of Service (DoS) attacks. Is possible to open several parallel connections against a URL to check if the web server can be compromised. The program tests the security in networks and uses ‘HTTP Keep Alive

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/goldeneye/> |
| 版本 | 1.2.0 |
| 包 / 命令 | `goldeneye` |
| 安装 | `sudo apt install goldeneye` |
| 占用空间 | 963 KB |
| 依赖 | `python3`、`goldeneye` |
| 官网 | <https://github.com/jseidl/GoldenEye> |
| 源码 | <https://salsa.debian.org/pkg-security-team/goldeneye> |

### goofile

Command line filetype search Use this tool to search for a specific file type in a given domain.

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/goofile/> |
| 版本 | 1.6 |
| 包 / 命令 | `goofile` |
| 安装 | `sudo apt install goofile` |
| 占用空间 | 37 KB |
| 依赖 | `python3`、`python3-requests`、`goofile` |
| 官网 | <https://github.com/sosukeinu/goofile> |
| 源码 | <https://gitlab.com/kalilinux/packages/goofile> |

### google-nexus-tools

ADB and Fastboot for use with Nexus devices Nexus Tools is an installer for the Android debug/development command-line tools ADB (Android Device Bridge) and Fastboot for Mac OS X, Linux, and Google Chrome/Chromium OS.

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/google-nexus-tools/> |
| 版本 | 2.3 |
| 包 / 命令 | `google-nexus-tools`、`nexus-adb`、`nexus-fastboot` |
| 安装 | `sudo apt install google-nexus-tools` |
| 占用空间 | 1.38 MB |
| 依赖 | `lib32stdc++6`、`nexus-adb` |
| 官网 | <https://github.com/corbindavenport/nexus-tools> |
| 源码 | <https://gitlab.com/kalilinux/packages/google-nexus-tools> |

### gophish

Open-Source Phishing Toolkit This package contains an open-source phishing toolkit designed for businesses and penetration testers. It provides the ability to quickly and easily setup and execute phishing engagements and security awareness training.

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/gophish/> |
| 版本 | 0.12.1 |
| 包 / 命令 | `gophish`、`gophish-start`、`gophish-stop` |
| 安装 | `sudo apt install gophish` |
| 占用空间 | 57.53 MB |
| 依赖 | `adduser`、`kali-defaults`、`libc6`、`libsqlite3-0`、`sudo`、`gophish` |
| 官网 | <https://getgophish.com/> |
| 源码 | <https://gitlab.com/kalilinux/packages/gophish> |

### goshs

SimpleHTTPServer written in Go This tool provides a SimpleHTTPServer written in Go, enhanced with features and security. This package contains a simple http server like the Python SimpleHTTPServer but enhanced with a lot of helpful features and security in mind.

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/goshs/> |
| 版本 | 2.1.6 |
| 包 / 命令 | `goshs` |
| 安装 | `sudo apt install goshs` |
| 占用空间 | 22.84 MB |
| 依赖 | `libc6`、`goshs` |
| 官网 | <https://github.com/patrickhener/goshs> |
| 源码 | <https://gitlab.com/kalilinux/packages/goshs> |

### gospider

Fast web spider written in Go This package contains a Fast web spider written in Go. The features are: - Fast web crawling - Brute force and parse sitemap.xml - Parse robots.txt - Generate and verify link from JavaScript files

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/gospider/> |
| 版本 | 1.1.6 |
| 包 / 命令 | `gospider` |
| 安装 | `sudo apt install gospider` |
| 占用空间 | 14.67 MB |
| 依赖 | `libc6`、`gospider` |
| 官网 | <https://github.com/jaeles-project/gospider> |
| 源码 | <https://gitlab.com/kalilinux/packages/gospider> |

### gowitness

Web screenshot utility using Chrome Headless gowitness is a website screenshot utility written in Golang, that uses Chrome Headless to generate screenshots of web interfaces using the command line, with a handy report viewer to process results. Both Linux and macOS is supported, with Windows support mostly working. Inspiration for gowitness comes from Eyewitness. If you are looking for

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/gowitness/> |
| 版本 | 3.1.1 |
| 包 / 命令 | `gowitness` |
| 安装 | `sudo apt install gowitness` |
| 占用空间 | 50.22 MB |
| 依赖 | `chromium`、`libc6`、`gowitness` |
| 官网 | <https://github.com/sensepost/gowitness> |
| 源码 | <https://gitlab.com/kalilinux/packages/gowitness> |

### graudit

Grep rough audit - source code auditing tool This is a simple script and signature sets that allows you to find potential security flaws in source code using the GNU utility grep. It’s comparable to other static analysis applications like RATS, SWAAT and flaw-finder while keeping the technical requirements to a minimum and being very flexible.

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/graudit/> |
| 版本 | 4.0 |
| 包 / 命令 | `graudit` |
| 安装 | `sudo apt install graudit` |
| 占用空间 | 118 KB |
| 官网 | <https://github.com/wireghoul/graudit> |
| 源码 | <https://salsa.debian.org/pkg-security-team/graudit> |

### gsocket

Allows two machines on different networks to communicate with each other Abandon the thought of IP Addresses and Port Numbers. Instead start thinking that two programs should be able to communicate with each other as long as they know the same secret (rather than each other’s IP Address and Port Number). The Global Socket library facilitates this: It locally derives temporary session keys and IDs and connects two programs through the Global

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/gsocket/> |
| 版本 | 1.4.43 |
| 包 / 命令 | `gsocket`、`blitz`、`gs-mount`、`gs-netcat`、`gs-sftp` |
| 安装 | `sudo apt install gsocket` |
| 占用空间 | 286 KB |
| 依赖 | `libc6`、`libssl3t64`、`blitz` |
| 官网 | <https://github.com/hackerschoice/gsocket> |
| 源码 | <https://salsa.debian.org/debian/gsocket> |

### gss-ntlmssp

GSSAPI NTLMSSP Mechanism – MIT GSSAPI plugin GSS-NTLMSSP is a GSSAPI mechanism plugin that implements NTLMSSP. NTLMSSP is a Microsoft Security Provider that implements various versions and falvors of the NTLM challenge-response family. GSS-NTLMSSP, implements both NTLM and NTLMv2 and all the various security variants to the key exchange that Microsoft introduced and

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/gss-ntlmssp/> |
| 版本 | 1.3.1 |
| 包 / 命令 | `gss-ntlmssp`、`gss-ntlmssp-dev` |
| 安装 | `sudo apt install gss-ntlmssp` |
| 占用空间 | 153 KB |
| 依赖 | `libc6`、`libgssapi-krb5-2`、`libssl3t64`、`libunistring5`、`libwbclient0`、`zlib1g`、`gss-ntlmssp-dev` |
| 官网 | <https://github.com/gssapi/gss-ntlmssp/> |
| 源码 | <https://salsa.debian.org/freeipa-team/gss-ntlmssp> |

### gtkhash

libb2-1 libc6 libcaja-extension1 libgcrypt20 libglib2.0-0t64 libgtk-3-0t64

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/gtkhash/> |
| 版本 | 1.5 |
| 包 / 命令 | `caja-gtkhash`、`gtkhash`、`nemo-gtkhash`、`thunar-gtkhash` |
| 安装 | `sudo apt install gtkhash` |
| 占用空间 | 497 KB |
| 官网 | <https://gtkhash.org> |
| 源码 | <https://salsa.debian.org/debian/gtkhash> |

### h8mail

Email open source intelligence and breach hunting tool This package contains an email OSINT and breach hunting tool using different breach and reconnaissance services, or local breaches such as Troy Hunt’s “Collection1” and the infamous “Breach Compilation” torrent.

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/h8mail/> |
| 版本 | 2.5.6 |
| 包 / 命令 | `h8mail` |
| 安装 | `sudo apt install h8mail` |
| 占用空间 | 142 KB |
| 依赖 | `python3`、`python3-requests`、`h8mail` |
| 官网 | <https://github.com/khast3x/h8mail> |
| 源码 | <https://gitlab.com/kalilinux/packages/h8mail> |

### hak5-wifi-coconut

Userspace driver for the Hak5 Wi-Fi Coconut Userspace drive for USB Wi-Fi NICs and the Hak5 Wi-Fi Coconut

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/hak5-wifi-coconut/> |
| 版本 | 1.1.0 |
| 包 / 命令 | `hak5-wifi-coconut`、`wifi_coconut` |
| 安装 | `sudo apt install hak5-wifi-coconut` |
| 占用空间 | 176 KB |
| 依赖 | `firmware-mediatek`、`libc6`、`libusb-1.0-0`、`wifi_coconut` |
| 官网 | <https://hak5.org> |
| 源码 | <https://gitlab.com/kalilinux/packages/hak5-wifi-coconut> |

### havoc

Modern and malleable post-exploitation C2 framework Havoc is a modern, malleable post-exploitation command and control framework made for penetration testers, red teams, and blue teams.

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/havoc/> |
| 版本 | 0.6~git20251218.c84f775 |
| 包 / 命令 | `havoc` |
| 安装 | `sudo apt install havoc` |
| 占用空间 | 27.13 MB |
| 依赖 | `gcc-mingw-w64-i686-win32`、`gcc-mingw-w64-x86-64-win32`、`libc6`、`libgcc-s1`、`libpython3.13`、`libqt5core5t64` |
| 官网 | <https://github.com/HavocFramework/Havoc> |
| 源码 | <https://gitlab.com/kalilinux/packages/havoc> |

### hcxtools

Tools for converting captures to use with hashcat or John the Ripper Portable solution for capturing wlan traffic and conversion to hashcat formats (recommended by hashcat) and to John the Ripper formats. hcx stands for: h = hash c = capture, convert and calculate candidates

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/hcxtools/> |
| 版本 | 7.1.2 |
| 包 / 命令 | `hcxtools`、`hcxeiutool`、`hcxhash2cap`、`hcxhashtool`、`hcxpcapngtool`、`hcxpmktool`、`hcxpottool`、`hcxpsktool`、`hcxwltool`、`whoismac`、`wlancap2wpasec` |
| 安装 | `sudo apt install hcxtools` |
| 占用空间 | 636 KB |
| 依赖 | `ieee-data`、`libc6`、`libcurl4t64`、`libssl3t64`、`zlib1g`、`hcxeiutool` |
| 官网 | <https://github.com/ZerBea/hcxtools> |
| 源码 | <https://salsa.debian.org/pkg-security-team/hcxtools> |

### hekatomb

Extract and decrypt all credentials from all domain computers Hekatomb is a Python script that connects to an LDAP directory to retrieve all computers and users’ information. From there, it will download all DPAPI blobs of all users from all computers and use Domain backup keys to decrypt them.

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/hekatomb/> |
| 版本 | 1.5.14 |
| 包 / 命令 | `hekatomb` |
| 安装 | `sudo apt install hekatomb` |
| 占用空间 | 63 KB |
| 依赖 | `python3`、`python3-chardet`、`python3-dnspython`、`python3-impacket`、`python3-ldap3`、`python3-pycryptodome`、`hekatomb` |
| 官网 | <https://github.com/ProcessusT/HEKATOMB> |
| 源码 | <https://gitlab.com/kalilinux/packages/hekatomb> |

### hexstrike-ai

AI-Powered MCP Cybersecurity Automation Platform This package contains an HexStrike AI MCP v6.0 which features a multi-agent architecture with autonomous AI agents, intelligent decision-making, and vulnerability intelligence.

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/hexstrike-ai/> |
| 版本 | 0.0~git20260306.8333779 |
| 包 / 命令 | `hexstrike-ai`、`hexstrike_mcp`、`hexstrike_server` |
| 安装 | `sudo apt install hexstrike-ai` |
| 占用空间 | 2.75 MB |
| 依赖 | `mitmproxy`、`python3`、`python3-aiohttp`、`python3-bs4`、`python3-flask`、`python3-mcp`、`python3-psutil`、`python3-pwntools`、`python3-requests`、`python3-selenium`、`hexstrike_mcp` |
| 官网 | <https://github.com/0x4m4/hexstrike-ai> |
| 源码 | <https://gitlab.com/kalilinux/packages/hexstrike-ai> |

### hexwalk

Hex analyzer, editor and viewer HexWalk is an Hex editor, viewer, analyzer based on opensource projects like qhexedit2, binwalk and QT It is cross platform and has plenty of features: Advanced find patterns in binary files based on HEX, UTF8, UTF16 and regex Binwalk integration

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/hexwalk/> |
| 版本 | 1.7.1 |
| 包 / 命令 | `hexwalk` |
| 安装 | `sudo apt install hexwalk` |
| 占用空间 | 936 KB |
| 依赖 | `libc6`、`libgcc-s1`、`libqt5charts5`、`libqt5core5t64` |
| 官网 | <https://www.hexwalk.com> |
| 源码 | <https://salsa.debian.org/gcarmix/hexwalk> |

### hoaxshell

Windows reverse shell payload generator and handler that abuses http(s) Hoaxshell is a Windows reverse shell payload generator and handler that abuses the http(s) protocol to establish a beacon-like reverse shell

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/hoaxshell/> |
| 版本 | 0.0~git20250119.e1bba89 |
| 包 / 命令 | `hoaxshell` |
| 安装 | `sudo apt install hoaxshell` |
| 占用空间 | 84 KB |
| 依赖 | `python3`、`python3-ipython`、`python3-pyperclip`、`hoaxshell` |
| 官网 | <https://github.com/t3l3machus/hoaxshell/> |
| 源码 | <https://gitlab.com/kalilinux/packages//hoaxshell> |

### horst

Highly Optimized Radio Scanning Tool horst is a small, lightweight IEEE802.11 WLAN analyzer with a text interface. Its basic function is similar to tcpdump, Wireshark or Kismet, but it’s much smaller and shows different, aggregated information which is not easily available from other tools. It is made for debugging wireless LANs with a focus on getting a quick

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/horst/> |
| 版本 | 5.1 |
| 包 / 命令 | `horst` |
| 安装 | `sudo apt install horst` |
| 占用空间 | 155 KB |
| 依赖 | `libc6`、`libncurses6`、`libnl-3-200`、`libnl-genl-3-200`、`libtinfo6`、`horst` |
| 官网 | <https://github.com/br101/horst> |
| 源码 | <https://salsa.debian.org/debian/horst> |

### hostapd-mana

Featureful rogue access point This package contains a eatureful rogue access point first presented at Defcon 22.

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/hostapd-mana/> |
| 版本 | 2.6.5 |
| 包 / 命令 | `hostapd-mana`、`hostapd-mana_cli` |
| 安装 | `sudo apt install hostapd-mana` |
| 占用空间 | 1.29 MB |
| 依赖 | `libc6`、`libnl-3-200`、`libnl-genl-3-200`、`libssl3t64`、`openssl`、`ssl-cert`、`hostapd-mana` |
| 官网 | <https://github.com/sensepost/hostapd-mana> |
| 源码 | <https://gitlab.com/kalilinux/packages/hostapd-mana> |

### hosthunter

Tool to discover and extract hostnames providing a set of target IP addresses This package contains a tool to efficiently discover and extract hostnames providing a large set of target IP addresses. HostHunter utilises simple OSINT techniques to map IP addresses with virtual hostnames. It generates a CSV or TXT file containing the results of the reconnaissance. Latest version of HostHunter also takes screenshots of the targets, it is

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/hosthunter/> |
| 版本 | 1.6 |
| 包 / 命令 | `hosthunter` |
| 安装 | `sudo apt install hosthunter` |
| 占用空间 | 33 KB |
| 依赖 | `chromium-driver`、`python3`、`python3-fake-useragent`、`python3-openssl`、`python3-requests`、`python3-selenium`、`python3-urllib3`、`hosthunter` |
| 官网 | <https://github.com/SpiderLabs/HostHunter> |
| 源码 | <https://gitlab.com/kalilinux/packages/hosthunter> |

### hostsman

Cross-platform command line tool for handling hosts files cross-platform command line tool for adding, removing or listing mappings in hosts file.

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/hostsman/> |
| 版本 | 1.1.5 |
| 包 / 命令 | `hostsman` |
| 安装 | `sudo apt install hostsman` |
| 占用空间 | 51 KB |
| 依赖 | `python3`、`python3-colorama`、`python3-mock`、`python3-pygments`、`hostsman` |
| 官网 | <https://github.com/qszhuan/hostsman> |
| 源码 | <https://gitlab.com/kalilinux/packages/hostsman> |

### hotpatch

Hot patches Linux executables with .so file injection Hotpatch is a library that can be used to dynamically load a shared library (.so) file on Linux from one process into another already running process, without affecting the execution of the target process. The API is a C API, but also supported in C++.

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/hotpatch/> |
| 版本 | 0.2 |
| 包 / 命令 | `hotpatch`、`hotpatcher` |
| 安装 | `sudo apt install hotpatch` |
| 占用空间 | 221 KB |
| 依赖 | `libc6`、`hotpatcher` |
| 官网 | <https://github.com/vikasnkumar/hotpatch> |
| 源码 | <https://gitlab.com/kalilinux/packages/hotpatch> |

### htshells

Self contained htaccess shells and attacks htshells is a series of web based attacks based around the .htaccess files. Most of the attacks are centered around two attack categories. Remote code/ command execution and information disclosure. These attacks are intended for use during penetration tests or security assessments. It was created to get shell in a CMS that restricted uploads based on extension and placed each

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/htshells/> |
| 版本 | 0.1~git20131205 |
| 包 / 命令 | `htshells` |
| 安装 | `sudo apt install htshells` |
| 占用空间 | 56 KB |
| 依赖 | `kali-defaults`、`htshells` |
| 官网 | <https://github.com/wireghoul/htshells> |
| 源码 | <https://gitlab.com/kalilinux/packages/htshells> |

### httprobe

Take a list of domains and probe for working HTTP and HTTPS servers This package contains a tool to test a domains list. It takes a list of domains and probe for working http and https servers.

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/httprobe/> |
| 版本 | 0.2 |
| 包 / 命令 | `httprobe` |
| 安装 | `sudo apt install httprobe` |
| 占用空间 | 4.43 MB |
| 依赖 | `libc6`、`httprobe` |
| 官网 | <https://github.com/tomnomnom/httprobe> |
| 源码 | <https://gitlab.com/kalilinux/packages/httprobe> |

### hubble

Network, Service & Security Observability for Kubernetes using eBPF (program) Hubble is a fully distributed networking and security observability platform for cloud native workloads. It is built on top of Cilium ( https://github.com/cilium/cilium ) and eBPF (

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/hubble/> |
| 版本 | 1.19.4 |
| 包 / 命令 | `hubble` |
| 安装 | `sudo apt install hubble` |
| 占用空间 | 104.29 MB |
| 依赖 | `libc6`、`hubble` |
| 官网 | <https://github.com/cilium/hubble> |
| 源码 | <https://gitlab.com/kalilinux/packages/hubble> |

### humble

HTTP Headers Analyzer This package contains an humble, and fast, security-oriented HTTP headers analyzer.

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/humble/> |
| 版本 | 1.64 |
| 包 / 命令 | `humble` |
| 安装 | `sudo apt install humble` |
| 占用空间 | 470 KB |
| 依赖 | `publicsuffix`、`python3`、`python3-colorama`、`python3-defusedcsv`、`python3-fpdf`、`python3-requests`、`python3-tldextract`、`python3-xlsxwriter`、`humble` |
| 官网 | <https://github.com/rfc-st/humble> |
| 源码 | <https://gitlab.com/kalilinux/packages/humble> |

### hurl

Hexadecimal & URL encoder + decoder This package contains a hexadecimal & URL (en/de)coder.

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/hurl/> |
| 版本 | 2.1 |
| 包 / 命令 | `hurl` |
| 安装 | `sudo apt install hurl` |
| 占用空间 | 187 KB |
| 依赖 | `libcgi-pm-perl`、`perl` |
| 官网 | <https://github.com/fnord0/hURL> |
| 源码 | <https://gitlab.com/kalilinux/packages/hurl> |

### i2c-tools

Heterogeneous set of I2C tools for Linux This package contains a heterogeneous set of I2C tools for Linux: a bus probing tool, a chip dumper, register-level access helpers, EEPROM decoding scripts, and more.

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/i2c-tools/> |
| 版本 | 4.4 |
| 包 / 命令 | `i2c-tools`、`ddcmon`、`decode-dimms`、`decode-edid`、`decode-vaio`、`i2c-stub-from-dump`、`i2cdetect`、`i2cdump`、`i2cget`、`i2cset`、`i2ctransfer`、`libi2c-dev`、`libi2c0`、`python3-smbus` |
| 安装 | `sudo apt install i2c-tools` |
| 占用空间 | 331 KB |
| 依赖 | `libc6`、`libi2c0`、`perl` |
| 官网 | <https://www.kernel.org/pub/software/utils/i2c-tools/> |
| 源码 | <https://salsa.debian.org/aurel32/i2c-tools> |

### ibombshell

Dynamic Remote Shell This package contains a tool written in Powershell that allows you to have a prompt at any time with post-exploitation functionalities (and in some cases exploitation). It is a shell that is downloaded directly to memory providing access to a large number of pentesting features. These functionalities can be downloaded directly to memory, in the form of a Powershell function. This form

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/ibombshell/> |
| 版本 | 0~git20201107 |
| 包 / 命令 | `ibombshell` |
| 安装 | `sudo apt install ibombshell` |
| 占用空间 | 4.94 MB |
| 依赖 | `powershell`、`python3-pynput`、`python3-termcolor`、`ibombshell` |
| 官网 | <https://github.com/Telefonica/ibombshell> |
| 源码 | <https://gitlab.com/kalilinux/packages/ibombshell> |

### ident-user-enum

Query ident to determine the owner of a TCP network process This package is a simple PERL script to query the ident service (113/TCP) in order to determine the owner of the process listening on each TCP port of a target system. This can help to prioritise target service during a pentest (you might want to attack services running as root first).

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/ident-user-enum/> |
| 版本 | 1.0 |
| 包 / 命令 | `ident-user-enum` |
| 安装 | `sudo apt install ident-user-enum` |
| 占用空间 | 12 KB |
| 依赖 | `libio-socket-ip-perl`、`libnet-ident-perl`、`perl`、`ident-user-enum` |
| 官网 | <https://pentestmonkey.net/tools/user-enumeration/ident-user-enum> |
| 源码 | <https://gitlab.com/kalilinux/packages/ident-user-enum> |

### ifenslave

Configure network interfaces for parallel routing (bonding) This is a tool to attach and detach slave network interfaces to a bonding device. A bonding device will act like a normal Ethernet network device to the kernel, but will send out the packets via the slave devices using a simple round-robin scheduler. This allows for simple load-balancing, identical to “channel bonding” or “trunking” techniques used in switches.

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/ifenslave/> |
| 版本 | 2.14 |
| 包 / 命令 | `ifenslave` |
| 安装 | `sudo apt install ifenslave` |
| 占用空间 | 40 KB |
| 依赖 | `ifupdown`、`iproute2` |
| 源码 | <https://salsa.debian.org/debian/ifenslave> |

### imhex

Hex Editor for Reverse Engineers, Programmers This package contains a Hex Editor for Reverse Engineers, Programmers and people who value their retinas when working at 3 AM.

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/imhex/> |
| 版本 | 1.38.1 |
| 包 / 命令 | `imhex`、`imhex-updater` |
| 安装 | `sudo apt install imhex` |
| 占用空间 | 90.15 MB |
| 依赖 | `libbz2-1.0`、`libc6`、`libcurl4t64`、`libdbus-1-3`、`libfmt10`、`libfreetype6`、`libgcc-s1`、`libglfw3`、`liblzma5`、`libmagic1t64`、`libmbedcrypto16`、`libssh2-1t64` 等 |
| 官网 | <https://github.com/WerWolv/ImHex> |
| 源码 | <https://gitlab.com/kalilinux/packages/imhex> |

### inspy

LinkedIn enumeration tool This package contains a Python based LinkedIn enumeration tool. You will need an API key from HunterIO.

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/inspy/> |
| 版本 | 3.0.0 |
| 包 / 命令 | `inspy` |
| 安装 | `sudo apt install inspy` |
| 占用空间 | 45 KB |
| 依赖 | `python3`、`python3-bs4`、`python3-requests`、`inspy` |
| 官网 | <https://github.com/gojhonny/InSpy> |
| 源码 | <https://gitlab.com/kalilinux/packages/inspy> |

### instaloader

Instagram automatic photo downloader Instaloader downloads photos from Instagram, including public and private profiles, hashtags, user stories, feeds and saved media. How as well as comments, geotags and captions for each post. It automatically detects profile name changes and renames the

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/instaloader/> |
| 版本 | 4.15.1 |
| 包 / 命令 | `instaloader` |
| 安装 | `sudo apt install instaloader` |
| 占用空间 | 319 KB |
| 依赖 | `python3`、`python3-requests`、`instaloader` |
| 官网 | <https://github.com/instaloader/instaloader> |
| 源码 | <https://salsa.debian.org/debian/instaloader> |

### ipv6toolkit

IPv6 assessment and troubleshooting tools Included tools: addr6: An IPv6 address analysis and manipulation tool. flow6: A tool to perform a security asseessment of the IPv6 Flow Label. frag6: A tool to perform IPv6 fragmentation-based attacks and to perform a security assessment of a number of fragmentation-related aspects.

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/ipv6toolkit/> |
| 版本 | 2.2 |
| 包 / 命令 | `ipv6toolkit`、`addr6`、`blackhole6`、`flow6`、`frag6`、`icmp6`、`jumbo6`、`messi`、`mldq6`、`na6`、`ni6`、`ns6`、`path6`、`ra6`、`rd6`、`rs6`、`scan6`、`script6`、`tcp6`、`udp6` |
| 安装 | `sudo apt install ipv6toolkit` |
| 占用空间 | 3.49 MB |
| 依赖 | `ieee-data`、`libc6`、`libpcap0.8t64`、`addr6` |
| 官网 | <https://www.si6networks.com/tools/ipv6toolkit/> |
| 源码 | <https://gitlab.com/kalilinux/packages/ipv6toolkit> |

### ismtp

SMTP user enumeration and testing tool Test for SMTP user enumeration (RCPT TO and VRFY), internal spoofing, and relay.

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/ismtp/> |
| 版本 | 1.6 |
| 包 / 命令 | `ismtp` |
| 安装 | `sudo apt install ismtp` |
| 占用空间 | 40 KB |
| 依赖 | `python3`、`ismtp` |
| 官网 | <https://github.com/altjx/ipwn/> |
| 源码 | <https://gitlab.com/kalilinux/packages/ismtp> |

### ivre

Network recon framework IVRE or DRUNK This package contains IVRE (Instrument de veille sur les réseaux extérieurs) or DRUNK (Dynamic Recon of UNKnown networks), a network recon framework, including tools for passive recon (flow analytics relying on Bro, Argus, Nfdump, fingerprint analytics based on Bro and p0f and active recon. IVRE uses Nmap to run scans, can use ZMap as a pre-scanner; IVRE can also

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/ivre/> |
| 版本 | 0.9.21 |
| 包 / 命令 | `ivre`、`ivre-doc` |
| 安装 | `sudo apt install ivre` |
| 占用空间 | 18.15 MB |
| 依赖 | `libjs-sphinxdoc`、`python3`、`python3-bottle`、`python3-cryptography`、`python3-dbus`、`python3-matplotlib`、`python3-mysqldb`、`python3-openssl`、`python3-pil`、`python3-psycopg2`、`python3-pymongo`、`python3-sqlalchemy` 等 |
| 官网 | <https://ivre.rocks> |
| 源码 | <https://gitlab.com/kalilinux/packages/ivre> |

### joplin

Open source note taking and to-do application This package contains a free, open source note taking and to-do application, which can handle a large number of notes organised into notebooks. The notes are searchable, can be copied, tagged and modified either from the applications directly or from your own text editor. The notes are in Markdown format.

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/joplin/> |
| 版本 | 3.7.1 |
| 包 / 命令 | `joplin`、`joplin-cli` |
| 安装 | `sudo apt install joplin` |
| 占用空间 | 410.70 MB |
| 依赖 | `libasound2t64`、`libatk-bridge2.0-0t64`、`libatk1.0-0t64`、`libatspi2.0-0t64`、`libc6`、`libcairo2`、`libcups2t64`、`libdbus-1-3`、`libexpat1`、`libgbm1`、`libgcc-s1`、`libglib2.0-0t64` 等 |
| 官网 | <https://github.com/laurent22/joplin> |
| 源码 | <https://gitlab.com/kalilinux/packages/joplin> |

### jsp-file-browser

File browser java server page This package contains an easy to use and easy to install file browser java server page. This JSP program allows remote web-based file access and manipulation. Features: - Create, copy, move, rename and delete files and directories - Shortkeys

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/jsp-file-browser/> |
| 版本 | 1.2 |
| 包 / 命令 | `jsp-file-browser` |
| 安装 | `sudo apt install jsp-file-browser` |
| 占用空间 | 93 KB |
| 依赖 | `kali-defaults`、`jsp-file-browser` |
| 官网 | <https://www.vonloesch.de/filebrowser.html> |
| 源码 | <https://gitlab.com/kalilinux/packages/jsp-file-browser> |

### juice-shop

Insecure web application This package contains a modern and sophisticated insecure web application! It can be used in security trainings, awareness demos, CTFs and as a guinea pig for security tools! Juice Shop encompasses vulnerabilities from the entire OWASP Top Ten along with many other security flaws found in real-world applications!

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/juice-shop/> |
| 版本 | 19.1.1 |
| 包 / 命令 | `juice-shop`、`juice-shop-start`、`juice-shop-stop` |
| 安装 | `sudo apt install juice-shop` |
| 占用空间 | 1.04 GB |
| 依赖 | `adduser`、`kali-defaults`、`libc6`、`libgcc-s1`、`libnode137`、`libstdc++6`、`lsof`、`npm`、`xdg-utils`、`juice-shop` |
| 官网 | <https://github.com/juice-shop/juice-shop> |
| 源码 | <https://gitlab.com/kalilinux/packages/juice-shop> |

### kali-community-wallpapers

Transitional package to install kali-wallpapers-community The package has been renamed kali-wallpapers-community and is part of the kali-wallpapers source package now. This dummy package can be safely removed once kali-wallpapers-community is installed on the system.

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/kali-community-wallpapers/> |
| 版本 | 2025.4.1 |
| 包 / 命令 | `kali-community-wallpapers`、`kali-wallpapers-community` |
| 安装 | `sudo apt install kali-community-wallpapers` |
| 占用空间 | 119.56 MB |
| 依赖 | `kali-wallpapers-community`、`kali-wallpapers-community` |
| 源码 | <https://gitlab.com/kalilinux/packages/kali-community-wallpapers> |

### kali-meta

Metapackage with dependencies common to all Kali’s desktops This metapackage depends on Kali packages that should be installed on all desktop installations of Kali Linux. This metapackage is a dependency of all kali-desktop-* packages.

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/kali-meta/> |
| 版本 | 2026.3.8 |
| 包 / 命令 | `kali-desktop-core`、`kali-desktop-e17`、`kali-desktop-gnome`、`kali-desktop-i3`、`kali-desktop-i3-gaps`、`kali-desktop-kde`、`kali-desktop-live`、`kali-desktop-lxde`、`kali-desktop-mate`、`kali-desktop-xfce`、`kali-linux-arm`、`kali-linux-core`、`kali-linux-default`、`kali-linux-everything`、`kali-linux-firmware`、`kali-linux-firmware-graphics`、`kali-linux-headless`、`kali-linux-labs`、`kali-linux-large`、`kali-linux-nethunter`、`kali-linux-wsl`、`kali-nethunter-core`、`kali-nethunter-full`、`kali-nethunter-nano`、`kali-sbc-allwinner`、`kali-sbc-amlogic`、`kali-sbc-qualcomm`、`kali-sbc-raspberrypi`、`kali-sbc-rockchip`、`kali-system-cli`、`kali-system-core`、`kali-system-gui`、`kali-tools-802-11`、`kali-tools-bluetooth`、`kali-tools-crypto-stego`、`kali-tools-database`、`kali-tools-detect`、`kali-tools-exploitation`、`kali-tools-forensics`、`kali-tools-fuzzing`、`kali-tools-gpu`、`kali-tools-hardware`、`kali-tools-identify`、`kali-tools-information-gathering`、`kali-tools-passwords`、`kali-tools-post-exploitation`、`kali-tools-protect`、`kali-tools-recover`、`kali-tools-reporting`、`kali-tools-respond`、`kali-tools-reverse-engineering`、`kali-tools-rfid`、`kali-tools-sdr`、`kali-tools-sniffing-spoofing`、`kali-tools-social-engineering`、`kali-tools-top10`、`kali-tools-voip`、`kali-tools-vulnerability`、`kali-tools-web`、`kali-tools-windows-resources`、`kali-tools-wireless` |
| 安装 | `sudo apt install kali-desktop-core` |
| 占用空间 | 13 KB |
| 依赖 | `dbus-user-session`、`dbus-x11` |
| 官网 | <https://www.kali.org> |
| 源码 | <https://gitlab.com/kalilinux/packages/kali-meta> |

### kali-tweaks

Tool to adjust advanced configuration settings for Kali Linux This package provides tweaks for Kali Linux. This include things like: Shell configuration APT mirrors configuration Kali Linux metapackages installation and removal

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/kali-tweaks/> |
| 版本 | 2026.2.0 |
| 包 / 命令 | `kali-tweaks` |
| 安装 | `sudo apt install kali-tweaks` |
| 占用空间 | 157 KB |
| 依赖 | `kali-defaults`、`python3`、`python3-newt`、`kali-tweaks` |
| 官网 | <https://gitlab.com/kalilinux/packages/kali-tweaks> |
| 源码 | <https://gitlab.com/kalilinux/packages/kali-tweaks> |

### kali-wallpapers

Transitional package to install kali-wallpapers-legacy The package has been renamed kali-wallpapers-legacy and is part of the kali-wallpapers source package now. This dummy package can be safely removed once kali-wallpapers-legacy is installed on the system.

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/kali-wallpapers/> |
| 版本 | 2026.1.0 |
| 包 / 命令 | `kali-legacy-wallpapers`、`kali-wallpapers-2019.4`、`kali-wallpapers-2020.4`、`kali-wallpapers-2022`、`kali-wallpapers-2023`、`kali-wallpapers-2024`、`kali-wallpapers-2025`、`kali-wallpapers-2026`、`kali-wallpapers-all`、`kali-wallpapers-legacy`、`kali-wallpapers-mobile-2023` |
| 安装 | `sudo apt install kali-legacy-wallpapers` |
| 占用空间 | 12 KB |
| 依赖 | `kali-wallpapers-legacy`、`kali-wallpapers-2019.4` |
| 源码 | <https://gitlab.com/kalilinux/packages/kali-wallpapers> |

### katana

Next-generation crawling and spidering framework. A next-generation crawling and spidering framework Fast And fully configurable web crawling Standard and Headless mode JavaScript parsing / crawling Customizable automatic form filling

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/katana/> |
| 版本 | 1.7.0 |
| 包 / 命令 | `katana` |
| 安装 | `sudo apt install katana` |
| 占用空间 | 64.20 MB |
| 依赖 | `libc6`、`katana` |
| 官网 | <https://github.com/projectdiscovery/katana> |
| 源码 | <https://gitlab.com/kalilinux/packages/katana> |

### kerberoast

Tools for attacking MS Kerberos implementations This package contains a series of tools for attacking MS Kerberos implementations: extract all accounts in use as SPN using built in MS tools extract the acquired tickets from ram with Mimikatz crack with tgsrepcrack

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/kerberoast/> |
| 版本 | 0.0~git20221231.cc5aa6e |
| 包 / 命令 | `kerberoast` |
| 安装 | `sudo apt install kerberoast` |
| 占用空间 | 81 KB |
| 依赖 | `python3`、`python3-pyasn1`、`python3-scapy`、`kerberoast` |
| 官网 | <https://github.com/nidem/kerberoast> |
| 源码 | <https://gitlab.com/kalilinux/packages/kerberoast> |

### knocker

Simple and easy to use TCP security port scanner Knocker is a new, simple, and easy to use TCP security port scanner written in C, using threads. It is able to analyze hosts and the network services which are running on them.

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/knocker/> |
| 版本 | 0.7.1 |
| 包 / 命令 | `knocker` |
| 安装 | `sudo apt install knocker` |
| 占用空间 | 83 KB |
| 依赖 | `libc6`、`knocker` |
| 官网 | <http://knocker.sourceforge.net/> |
| 源码 | <https://salsa.debian.org/pkg-security-team/knocker> |

### koadic

Windows post-exploitation rootkit This package contains Koadic, or COM Command & Control. It is a Windows post-exploitation rootkit similar to other penetration testing tools such as Meterpreter and Powershell Empire. The major difference is that Koadic does most of its operations using Windows Script Host (a.k.a. JScript/VBScript), with compatibility in the core to support a default installation of Windows

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/koadic/> |
| 版本 | 0~git20210412 |
| 包 / 命令 | `koadic` |
| 安装 | `sudo apt install koadic` |
| 占用空间 | 7.51 MB |
| 依赖 | `python3`、`python3-impacket`、`python3-pyasn1`、`python3-pypykatz`、`python3-rjsmin`、`python3-tabulate`、`koadic` |
| 官网 | <https://github.com/zerosum0x0/koadic> |
| 源码 | <https://gitlab.com/kalilinux/packages/koadic> |

### krbrelayx

Kerberos relaying and unconstrained delegation abuse toolkit Kerberos relaying and unconstrained delegation abuse toolkit. This tool can add/remove/modify Service Principal Names on accounts in AD over LDAP.

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/krbrelayx/> |
| 版本 | 0.0~git20260311.10b45a3 |
| 包 / 命令 | `krbrelayx`、`addspn`、`dnstool`、`printerbug` |
| 安装 | `sudo apt install krbrelayx` |
| 占用空间 | 172 KB |
| 依赖 | `python3`、`python3-dnspython`、`python3-impacket`、`python3-ldap3`、`addspn` |
| 官网 | <https://github.com/dirkjanm/krbrelayx> |
| 源码 | <https://gitlab.com/kalilinux/packages/krbrelayx> |

### kubernetes-helm

Tool for managing Charts (helm) This package contains a tool for managing Charts. Charts are packages of pre-configured Kubernetes resources. Use Helm to: * Find and use popular software packaged as Helm Charts to run in Kubernetes * Share your own applications as Helm Charts

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/kubernetes-helm/> |
| 版本 | 4.2.3 |
| 包 / 命令 | `kubernetes-helm`、`helm` |
| 安装 | `sudo apt install kubernetes-helm` |
| 占用空间 | 61.29 MB |
| 官网 | <https://github.com/helm/helm> |
| 源码 | <https://gitlab.com/kalilinux/packages/kubernetes-helm> |

### kustomize

Customization of Kubernetes YAML configurations (program) Kustomize is a standalone binary tool for managing Kubernetes configurations without requiring templates. It allows users to customize resource configurations through overlays, making it easy to reuse and share manifests across environments. Kustomize operates natively with Kubernetes YAML, offering functionality like

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/kustomize/> |
| 版本 | 5.8.1 |
| 包 / 命令 | `golang-k8s-sigs-kustomize-dev`、`kustomize` |
| 安装 | `sudo apt install kustomize` |
| 占用空间 | 22.88 MB |
| 依赖 | `libc6`、`kustomize` |
| 官网 | <https://github.com/kubernetes-sigs/kustomize> |
| 源码 | <https://salsa.debian.org/kubernetes-team/packages/kustomize> |

### lapsdumper

Tool that dumps LAPS passwords A tool that dumps every LAPS password the account has the ability to read with a domain.

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/lapsdumper/> |
| 版本 | 0 |
| 包 / 命令 | `lapsdumper` |
| 安装 | `sudo apt install lapsdumper` |
| 占用空间 | 16 KB |
| 依赖 | `python3-ldap3`、`lapsdumper` |
| 官网 | <https://github.com/n00py/LAPSDumper> |
| 源码 | <https://gitlab.com/kalilinux/packages/lapsdumper> |

### ldeep

In-depth ldap enumeration utility ldeep is an in-depth ldap enumeration utility that can either run against an Active Directory LDAP server or locally on saved files.

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/ldeep/> |
| 版本 | 2.0.3 |
| 包 / 命令 | `ldeep` |
| 安装 | `sudo apt install ldeep` |
| 占用空间 | 254 KB |
| 依赖 | `gcc`、`krb5-config`、`libkrb5-dev`、`python3`、`python3-commandparse`、`python3-cryptography`、`python3-dev`、`python3-dnspython`、`python3-gssapi`、`python3-ldap3-bleeding-edge`、`python3-oscrypto`、`python3-pycryptodome` 等 |
| 官网 | <https://github.com/franc-pentest/ldeep> |
| 源码 | <https://gitlab.com/kalilinux/packages/ldeep> |

### legba

Multiprotocol credentials bruteforcer / password sprayer and enumerator Legba is a multiprotocol credentials bruteforcer / password sprayer and enumerator built with Rust and the Tokio asynchronous runtime in order to achieve better performances and stability while consuming less resources than similar tools.

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/legba/> |
| 版本 | 1.3.0 |
| 包 / 命令 | `legba` |
| 安装 | `sudo apt install legba` |
| 占用空间 | 27.70 MB |
| 依赖 | `libc6`、`libgcc-s1`、`legba` |
| 官网 | <https://github.com/maaaaz/webscreenshot> |
| 源码 | <https://gitlab.com/kalilinux/packages/legba> |

### libimage-exiftool-perl

Library and program to read and write meta information in multimedia files Image::ExifTool is a customizable set of Perl modules plus a full-featured command-line application called exiftool for reading and writing meta information in a wide variety of files, including the maker note information of many digital cameras by various manufacturers such as Canon, Casio, DJI, FLIR, FujiFilm, GE, HP, JVC/Victor, Kodak, Leaf, Minolta/Konica-Minolta,

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/libimage-exiftool-perl/> |
| 版本 | 13.55 |
| 包 / 命令 | `libimage-exiftool-perl`、`exiftool` |
| 安装 | `sudo apt install libimage-exiftool-perl` |
| 占用空间 | 28.50 MB |
| 依赖 | `perl`、`exiftool` |
| 官网 | <https://exiftool.org/> |
| 源码 | <https://salsa.debian.org/perl-team/modules/packages/libimage-exiftool-perl> |

### ligolo-mp

Multiplayer pivoting solution Ligolo-MP is an advanced version of Ligolo-ng, with client-server architecture, enabling pentesters to play with multiple concurrent tunnels collaboratively. It manages all your TUNs automatically, while also providing a clean GUI to track everything.

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/ligolo-mp/> |
| 版本 | 2.2.1 |
| 包 / 命令 | `ligolo-mp`、`ligolo-mp-client` |
| 安装 | `sudo apt install ligolo-mp` |
| 占用空间 | 129.38 MB |
| 官网 | <https://github.com/ttpreport/ligolo-mp> |
| 源码 | <https://gitlab.com/kalilinux/packages/ligolo-mp> |

### ligolo-ng

Advanced, yet simple, tunneling/pivoting tool that uses a TUN interface Ligolo-ng is a simple, lightweight and fast tool that allows pentesters to establish tunnels from a reverse TCP/TLS connection using a tun interface (without the need of SOCKS).

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/ligolo-ng/> |
| 版本 | 0.9.1 |
| 包 / 命令 | `ligolo-ng`、`ligolo-agent`、`ligolo-proxy` |
| 安装 | `sudo apt install ligolo-ng` |
| 占用空间 | 26.49 MB |
| 依赖 | `libc6`、`ligolo-agent` |
| 官网 | <https://github.com/nicocha30/ligolo-ng> |
| 源码 | <https://gitlab.com/kalilinux/packages/ligolo-ng> |

### ligolo-ng-common-binaries

Prebuilt binaries for Advanced ligolo-ng Ligolo-ng is a simple, lightweight and fast tool that allows pentesters to establish tunnels from a reverse TCP/TLS connection using a tun interface (without the need of SOCKS).

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/ligolo-ng-common-binaries/> |
| 版本 | 0.9.1 |
| 包 / 命令 | `ligolo-ng-common-binaries` |
| 安装 | `sudo apt install ligolo-ng-common-binaries` |
| 占用空间 | 158.37 MB |
| 官网 | <https://github.com/nicocha30/ligolo-ng> |
| 源码 | <https://gitlab.com/kalilinux/packages/ligolo-ng> |

### linkedin2username

Generate username lists for companies on LinkedIn OSINT Tool: Generate username lists from companies on LinkedIn. This is a pure web-scraper, no API key required. You use your valid LinkedIn username and password to login, it will create several lists of possible username formats for all employees of a company you point it at.

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/linkedin2username/> |
| 版本 | 0.30 |
| 包 / 命令 | `linkedin2username` |
| 安装 | `sudo apt install linkedin2username` |
| 占用空间 | 39 KB |
| 依赖 | `chromium-driver`、`python3`、`python3-requests`、`python3-selenium`、`linkedin2username` |
| 官网 | <https://github.com/initstring/linkedin2username> |
| 源码 | <https://gitlab.com/kalilinux/packages/linkedin2username> |

### linux-exploit-suggester

LES: Linux privilege escalation auditing tool This package contains a Linux privilege escalation auditing tool. It’s designed to assist in detecting security deficiencies for given Linux kernel/Linux-based machine. It provides following functionality: Assessing kernel exposure on publicly known exploits Tool assesses (using heuristics methods discussed in details here) exposure of

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/linux-exploit-suggester/> |
| 版本 | 1.1 |
| 包 / 命令 | `linux-exploit-suggester` |
| 安装 | `sudo apt install linux-exploit-suggester` |
| 占用空间 | 99 KB |
| 依赖 | `less`、`linux-exploit-suggester` |
| 官网 | <https://github.com/mzet-/linux-exploit-suggester> |
| 源码 | <https://gitlab.com/kalilinux/packages/linux-exploit-suggester> |

### llm-tools-nmap

Plugin for LLM tool hat provides Nmap network scanning capabilities This package contains a plugin for Simon Willison’s LLM tool that provides Nmap network scanning capabilities through function calling. This plugin enables LLMs to perform network discovery and security scanning tasks using the powerful Nmap tool.

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/llm-tools-nmap/> |
| 版本 | 0.0~git20250612.36818ca |
| 包 / 命令 | `llm-tools-nmap` |
| 安装 | `sudo apt install llm-tools-nmap` |
| 占用空间 | 31 KB |
| 依赖 | `llm`、`nmap`、`python3` |
| 官网 | <https://github.com/peter-hackertarget/llm-tools-nmap> |
| 源码 | <https://gitlab.com/kalilinux/packages/llm-tools-nmap> |

### maltego-teeth

Set of offensive Maltego transforms A set of transforms for Maltego to run nmap, sqlmap, and more against entitites in Maltego.

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/maltego-teeth/> |
| 版本 | 1.0 |
| 包 / 命令 | `maltego-teeth` |
| 安装 | `sudo apt install maltego-teeth` |
| 占用空间 | 122.68 MB |
| 依赖 | `maltego`、`metasploit-framework`、`nmap`、`python3`、`python3-adns`、`python3-bs4`、`python3-easygui`、`python3-levenshtein`、`python3-mechanize`、`python3-metaconfig`、`python3-msgpack`、`sqlmap` |
| 官网 | <https://www.maltego.com> |
| 源码 | <https://gitlab.com/kalilinux/packages/maltego-teeth> |

### massdns

High-performance DNS stub resolver This package contains a simple high-performance DNS stub resolver targeting those who seek to resolve a massive amount of domain names in the order of millions or even billions. Without special configuration, MassDNS is capable of resolving over 350,000 names per second using publicly available resolvers.

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/massdns/> |
| 版本 | 1.1.0 |
| 包 / 命令 | `massdns` |
| 安装 | `sudo apt install massdns` |
| 占用空间 | 128 KB |
| 依赖 | `libc6`、`massdns` |
| 官网 | <https://github.com/blechschmidt/massdns> |
| 源码 | <https://gitlab.com/kalilinux/packages/massdns> |

### mc

Midnight Commander - a powerful file manager GNU Midnight Commander is a text-mode full-screen file manager. It uses a two panel interface and a subshell for command execution. It includes an internal editor with syntax highlighting and an internal viewer with support for binary files. Also included is Virtual Filesystem (VFS), that allows files on remote systems (e.g. FTP, SSH

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/mc/> |
| 版本 | 4.8.33 |
| 包 / 命令 | `mc`、`mcdiff`、`mcedit`、`mcview`、`mc-data` |
| 安装 | `sudo apt install mc` |
| 占用空间 | 1.55 MB |
| 依赖 | `libc6`、`libext2fs2t64`、`libglib2.0-0t64`、`libgpm2`、`libslang2`、`libssh2-1t64`、`mc-data`、`mc` |
| 官网 | <https://www.midnight-commander.org> |
| 源码 | <https://salsa.debian.org/debian/mc> |

### mcp-kali-server

API bridge connecting MCP Clients to the API server This package contains a lightweight API bridge that connects MCP Clients (e.g: Claude Desktop, 5ire) to the API server which allows excuting commands on a Linux terminal. This allows the MCP to run terminal commands like nmap, nxc or any other tool, interact with web applications using tools like curl, wget, gobuster. And

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/mcp-kali-server/> |
| 版本 | 0.0~git20260317.00154c0 |
| 包 / 命令 | `mcp-kali-server`、`kali-server-mcp`、`mcp-server` |
| 安装 | `sudo apt install mcp-kali-server` |
| 占用空间 | 75 KB |
| 依赖 | `adduser`、`python3`、`python3-flask`、`python3-mcp`、`python3-requests`、`sudo`、`kali-server-mcp` |
| 官网 | <https://github.com/Wh0am123/MCP-Kali-Server> |
| 源码 | <https://gitlab.com/kalilinux/packages/mcp-kali-server> |

### mercurial

Easy-to-use, scalable distributed version control system Mercurial is a fast, lightweight Source Control Management system designed for efficient handling of very large distributed projects. Its features include: O(1) delta-compressed file storage and retrieval scheme Complete cross-indexing of files and changesets for efficient exploration

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/mercurial/> |
| 版本 | 7.2.3 |
| 包 / 命令 | `mercurial`、`chg`、`hg`、`mercurial-common`、`hg-ssh` |
| 安装 | `sudo apt install mercurial` |
| 占用空间 | 2.51 MB |
| 依赖 | `libc6`、`mercurial-common`、`python3`、`python3`、`ucf`、`chg` |
| 官网 | <https://www.mercurial-scm.org/> |
| 源码 | <https://salsa.debian.org/python-team/packages/mercurial> |

### merlin

Command & Control server & agent (metapackage) This package contains a cross-platform post-exploitation HTTP/2 Command & Control server and agent written in golang as well as an identification tool.

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/merlin/> |
| 版本 | 2.1.4 |
| 包 / 命令 | `golang-github-ne0nd0g-merlin-dev`、`merlin`、`merlin-server`、`merlinserver` |
| 安装 | `sudo apt install merlin` |
| 占用空间 | 23 KB |
| 依赖 | `merlin-agent`、`merlin-server`、`merlin-server` |
| 官网 | <https://github.com/Ne0nd0g/merlin> |
| 源码 | <https://gitlab.com/kalilinux/packages/merlin> |

### merlin-agent

Cross-platform post-exploitation HTTP/2 Command & Control agent This package contains the Agent code for Merlin post-exploitation command and control framework.

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/merlin-agent/> |
| 版本 | 2.4.3 |
| 包 / 命令 | `merlin-agent` |
| 安装 | `sudo apt install merlin-agent` |
| 占用空间 | 12.19 MB |
| 依赖 | `libc6`、`merlin-agent` |
| 官网 | <https://github.com/Ne0nd0g/merlin-agent> |
| 源码 | <https://gitlab.com/kalilinux/packages/merlin-agent> |

### metasploitmcp

MCP Server for Metasploit A Model Context Protocol (MCP) server for Metasploit Framework integration.

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/metasploitmcp/> |
| 版本 | 0.0~git20260205.afc792d |
| 包 / 命令 | `metasploitmcp` |
| 安装 | `sudo apt install metasploitmcp` |
| 占用空间 | 104 KB |
| 依赖 | `python3`、`python3-fastapi`、`python3-fastmcp`、`python3-mcp`、`python3-pymetasploit3`、`python3-uvicorn`、`metasploitmcp` |
| 官网 | <https://github.com/GH05TCREW/MetasploitMCP> |
| 源码 | <https://gitlab.com/kalilinux/packages/metasploitmcp> |

### mitm6

Pwning IPv4 via IPv6 mitm6 is a pentesting tool that exploits the default configuration of Windows to take over the default DNS server. It does this by replying to DHCPv6 messages, providing victims with a link-local IPv6 address and setting the attackers host as default DNS server.

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/mitm6/> |
| 版本 | 0.3.0 |
| 包 / 命令 | `mitm6` |
| 安装 | `sudo apt install mitm6` |
| 占用空间 | 40 KB |
| 依赖 | `python3`、`python3-netifaces`、`python3-scapy`、`python3-twisted`、`mitm6` |
| 官网 | <https://github.com/dirkjanm/mitm6> |
| 源码 | <https://gitlab.com/kalilinux/packages/mitm6> |

### mongo-tools

MongoDB tools (program) This package contains tools for MongDB: bsondump - display BSON files in a human-readable format mongoimport - Convert data from JSON, TSV or CSV and insert them into a collection mongoexport - Write an existing collection to CSV or JSON format

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/mongo-tools/> |
| 版本 | 100.9.1 |
| 包 / 命令 | `mongo-tools`、`bsondump`、`mongodump`、`mongoexport`、`mongofiles`、`mongoimport`、`mongorestore`、`mongostat` |
| 安装 | `sudo apt install mongo-tools` |
| 占用空间 | 70.59 MB |
| 依赖 | `libc6`、`bsondump` |
| 官网 | <https://github.com/mongodb/mongo-tools> |
| 源码 | <https://gitlab.com/kalilinux/packages/mongo-tools> |

### msitools

Windows Installer file manipulation tool msitools contains a number of programs to create, inspect and extract Windows Installer (.msi) files. The following tools are included: msiinfo: inspects MSI packages msibuild: builds MSI packages

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/msitools/> |
| 版本 | 0.106 |
| 包 / 命令 | `gir1.2-libmsi-1.0`、`libmsi-1.0-0`、`libmsi-dev`、`msitools`、`msibuild`、`msidiff`、`msidump`、`msiextract`、`msiinfo`、`wixl`、`wixl-heat`、`wixl-data` |
| 安装 | `sudo apt install msitools` |
| 占用空间 | 306 KB |
| 依赖 | `libc6`、`libgcab-1.0-0`、`libglib2.0-0t64`、`libmsi-1.0-0`、`msibuild` |
| 官网 | <https://wiki.gnome.org/msitools> |
| 源码 | <https://salsa.debian.org/debian/msitools> |

### mssqlpwner

Advanced and versatile pentesting tool MSSqlPwner is an advanced and versatile pentesting tool designed to seamlessly interact and pwn MSSQL servers. That tool is based on impacket, which allows attackers to authenticate to databases using clear-text passwords NTLM Hashes, and kerberos tickets. With MSSqlPwner, users can execute custom commands through various methods, including custom assembly,

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/mssqlpwner/> |
| 版本 | 1.3.2 |
| 包 / 命令 | `mssqlpwner` |
| 安装 | `sudo apt install mssqlpwner` |
| 占用空间 | 238 KB |
| 依赖 | `python3`、`python3-impacket`、`python3-prompt-toolkit`、`python3-termcolor`、`mssqlpwner` |
| 官网 | <https://github.com/ScorpionesLabs/MSSqlPwner> |
| 源码 | <https://gitlab.com/kalilinux/packages/mssqlpwner> |

### multiforcer

GPU accelerated password cracking tool A CUDA & OpenCL accelerated rainbow table implementation from the ground up, and a CUDA hash brute forcing tool with support for many hash types including MD5, SHA1, LM, NTLM, and lots more.

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/multiforcer/> |
| 版本 | 1.31 |
| 包 / 命令 | `multiforcer`、`showconfig-opencl` |
| 安装 | `sudo apt install multiforcer` |
| 占用空间 | 15.47 MB |
| 官网 | <https://sourceforge.net/projects/cryptohaze/> |
| 源码 | <https://gitlab.com/kalilinux/packages/multiforcer> |

### multimac

Create multiple MACs on an adapter Multimac is a Linux virtual ethernet tap allocator to emulate and use multiple virtual interfaces (with different MAC addresses) on a LAN using a single network adapter.

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/multimac/> |
| 版本 | 1.0.3 |
| 包 / 命令 | `multimac` |
| 安装 | `sudo apt install multimac` |
| 占用空间 | 28 KB |
| 依赖 | `libc6`、`multimac` |
| 官网 | <https://sourceforge.net/projects/multimac/> |
| 源码 | <https://gitlab.com/kalilinux/packages/multimac> |

### mxcheck

Info and security scanner for e-mail servers mxcheck is an info scanner for e-mail servers, checking: - DNS records: A, MX, PTR, SPF, MTA-STS, DKIM, DMARC - AS Number and AS Country - The support of StartTLS and the certificate - Open ports: 25, 465, 587

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/mxcheck/> |
| 版本 | 2.0.0 |
| 包 / 命令 | `mxcheck` |
| 安装 | `sudo apt install mxcheck` |
| 占用空间 | 6.79 MB |
| 依赖 | `libc6`、`mxcheck` |
| 官网 | <https://github.com/steffenfritz/mxcheck> |
| 源码 | <https://gitlab.com/kalilinux/packages/mxcheck> |

### naabu

Fast port scanner with a focus on reliability and simplicity This package contains a port scanning tool written in Go that allows you to enumerate valid ports for hosts in a fast and reliable manner. It is a really simple tool that does fast SYN/CONNECT scans on the host/list of hosts and lists all ports that return a reply. Main features are:

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/naabu/> |
| 版本 | 2.6.1 |
| 包 / 命令 | `naabu` |
| 安装 | `sudo apt install naabu` |
| 占用空间 | 33.32 MB |
| 依赖 | `libc6`、`naabu` |
| 官网 | <https://github.com/projectdiscovery/naabu> |
| 源码 | <https://gitlab.com/kalilinux/packages/naabu> |

### name-that-hash

Identify MD5, SHA256 and 300+ other hash types This package contains a utility to identify hash types. Have you ever come across a hash such as 5f4dcc3b5aa765d61d8327deb882cf99 and wondered what type of hash type that is? Name-that-hash will name it for you.

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/name-that-hash/> |
| 版本 | 1.11.0 |
| 包 / 命令 | `name-that-hash`、`nth` |
| 安装 | `sudo apt install name-that-hash` |
| 占用空间 | 123 KB |
| 依赖 | `python3`、`python3`、`python3-click`、`python3-colorama`、`python3-pygments`、`python3-rich`、`name-that-hash` |
| 官网 | <https://github.com/HashPals/Name-That-Hash> |
| 源码 | <https://gitlab.com/kalilinux/packages/name-that-hash> |

### nbtscan-unixwiz

Scanner for open NETBIOS nameservers This package contains a command-line tool that scans for open NETBIOS nameservers on a local or remote TCP/IP network, and this is a first step in finding of open shares. It is based on the functionality of the standard Windows tool nbtstat, but it operates on a range of addresses instead of just one.

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/nbtscan-unixwiz/> |
| 版本 | 1.0.35 |
| 包 / 命令 | `nbtscan-unixwiz` |
| 安装 | `sudo apt install nbtscan-unixwiz` |
| 占用空间 | 53 KB |
| 依赖 | `libc6`、`nbtscan-unixwiz` |
| 官网 | <http://unixwiz.net/tools/nbtscan.html> |
| 源码 | <https://gitlab.com/kalilinux/packages/nbtscan-unixwiz> |

### ncurses-hexedit

Edit files/disks in hex, ASCII and EBCDIC Hexedit is a file editor which allows editing and viewing a file in hexadecimal, along with its ASCII or EBCDIC text equivalent. Standard editing features include insert, delete, search (text or byte searches), highlighted changes, undo, two different viewing formats, and full screen text snapshots. Allows editing of fixed disks as well. Includes

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/ncurses-hexedit/> |
| 版本 | 0.9.7 |
| 包 / 命令 | `ncurses-hexedit`、`hexeditor` |
| 安装 | `sudo apt install ncurses-hexedit` |
| 占用空间 | 130 KB |
| 依赖 | `libc6`、`libncurses6`、`libtinfo6`、`hexeditor` |
| 官网 | <http://www.rogoyski.com/adam/programs/hexedit/> |
| 源码 | <https://salsa.debian.org/debian/ncurses-hexedit> |

### netscanner

Network scanner & diagnostic tool with modern TUI Netscanner is a network scanning tool with features like: - List HW Interfaces - Switching active Interface for scanning & packet-dumping - WiFi networks scanning - WiFi signals strength (with charts)

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/netscanner/> |
| 版本 | 0.6.43 |
| 包 / 命令 | `netscanner` |
| 安装 | `sudo apt install netscanner` |
| 占用空间 | 15.01 MB |
| 依赖 | `libc6`、`libgcc-s1`、`netscanner` |
| 官网 | <https://github.com/Chleba/netscanner> |
| 源码 | <https://gitlab.com/kalilinux/packages/netscanner> |

### netsed

Network packet-altering stream editor NetSED is a small and handy utility designed to alter, in real time, the contents of packets forwarded through your network. It is really useful for network packet alteration, forging, or manipulation. NetSED supports: black-box protocol auditing - whenever there are two or more

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/netsed/> |
| 版本 | 1.4 |
| 包 / 命令 | `netsed` |
| 安装 | `sudo apt install netsed` |
| 占用空间 | 53 KB |
| 依赖 | `libc6`、`netsed` |
| 官网 | <http://silicone.homelinux.org/projects/netsed/> |
| 源码 | <https://salsa.debian.org/debian/netsed> |

### netw-ib-ox-ag

Graphical frontend for netwox Netwag is a graphical front end for netwox which contains more than 200 tools. Netwag permits one to easily: search amongst tools proposed in netwox construct command line run tools

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/netw-ib-ox-ag/> |
| 版本 | 5.39.0 |
| 包 / 命令 | `netwag`、`netwag-doc`、`netwox`、`netwox-doc` |
| 安装 | `sudo apt install netwag` |
| 占用空间 | 328 KB |
| 依赖 | `netwox`、`tk` |
| 官网 | <http://ntwox.sourceforge.net/> |
| 源码 | <https://salsa.debian.org/debian/netw-ib-ox-ag> |

### nextnet

Pivot point discovery tool in Go This package contains a pivot point discovery tool written in Go.

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/nextnet/> |
| 版本 | 0.0.2 |
| 包 / 命令 | `nextnet` |
| 安装 | `sudo apt install nextnet` |
| 占用空间 | 2.59 MB |
| 依赖 | `libc6`、`nextnet` |
| 官网 | <https://github.com/hdm/nextnet> |
| 源码 | <https://gitlab.com/kalilinux/packages/nextnet> |

### ngrep

Grep for network traffic ngrep strives to provide most of GNU grep’s common features, applying them to the network layer. ngrep is a pcap-aware tool that will allow you to specify extended regular expressions to match against data payloads of packets. It currently recognizes TCP, UDP and ICMP across Ethernet, PPP, SLIP and null interfaces, and

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/ngrep/> |
| 版本 | 1.47 |
| 包 / 命令 | `ngrep` |
| 安装 | `sudo apt install ngrep` |
| 占用空间 | 73 KB |
| 依赖 | `libc6`、`libnet9`、`libpcap0.8t64`、`libpcre2-8-0`、`ngrep` |
| 官网 | <https://github.com/jpr5/ngrep> |
| 源码 | <https://salsa.debian.org/debian/ngrep> |

### nmapsi4

Graphical interface to nmap, the network scanner NmapSI4 is a complete Qt-based Gui with the design goal to provide a complete nmap interface for users, in order to manage all options of this power security net scanner.

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/nmapsi4/> |
| 版本 | 0.6~alpha1 |
| 包 / 命令 | `nmapsi4` |
| 安装 | `sudo apt install nmapsi4` |
| 占用空间 | 1.31 MB |
| 依赖 | `bind9-dnsutils`、`libc6`、`libgcc-s1`、`libqt6core5compat6`、`libqt6core6t64`、`libqt6dbus6`、`libqt6gui6`、`libqt6network6`、`libqt6qml6`、`libqt6quick6`、`libqt6webenginewidgets6`、`libqt6widgets6` 等 |
| 官网 | <https://www.nmapsi4.org> |
| 源码 | <https://salsa.debian.org/pkg-security-team/nmapsi4> |

### obsidian

Private and flexible writing app that adapts to the way you think Obsidian stores notes on your device, so you can access them quickly, even offline. With hundreds of plugins and themes, you can shape Obsidian to fit your way of thinking. Obsidian uses open, non-proprietary files, so you’re never

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/obsidian/> |
| 版本 | 1.7.7 |
| 包 / 命令 | `obsidian` |
| 安装 | `sudo apt install obsidian` |
| 占用空间 | 287.27 MB |
| 依赖 | `libasound2t64`、`libatk-bridge2.0-0t64`、`libatk1.0-0t64`、`libatspi2.0-0t64`、`libc6`、`libcairo2`、`libcups2t64`、`libdbus-1-3`、`libdrm2`、`libexpat1`、`libgbm1`、`libgcc-s1` 等 |
| 官网 | <https://obsidian.md/> |
| 源码 | <https://gitlab.com/kalilinux/packages/obsidian> |

### odat

Oracle Database Attacking Tool This package contains the ODAT (Oracle Database Attacking Tool), an open source penetration testing tool that tests the security of Oracle Databases remotely. Usage examples of ODAT: You have an Oracle database listening remotely and want to find valid SIDs and credentials in order to connect to the database

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/odat/> |
| 版本 | 5.1.1 |
| 包 / 命令 | `odat` |
| 安装 | `sudo apt install odat` |
| 占用空间 | 511 KB |
| 依赖 | `oracle-instantclient-basic`、`oracle-instantclient-devel`、`python3`、`python3-argcomplete`、`python3-colorlog`、`python3-cx-oracle`、`python3-libnmap`、`python3-passlib`、`python3-pyasyncore`、`python3-pycryptodome`、`python3-scapy`、`python3-termcolor` 等 |
| 官网 | <https://github.com/quentinhardy/odat> |
| 源码 | <https://gitlab.com/kalilinux/packages/odat> |

### offsec-courses

Resources for OffSec’s AWAE/WEB-300 This is Kali Linux, the most advanced penetration testing and security auditing distribution. This metapackage depends on the resources required for OffSec’s AWAE/WEB-300/OSWE.

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/offsec-courses/> |
| 版本 | 2026.3.0 |
| 包 / 命令 | `offsec-awae`、`offsec-awae-python2`、`offsec-exp100`、`offsec-exp301`、`offsec-pen300`、`offsec-pwk` |
| 安装 | `sudo apt install offsec-awae` |
| 占用空间 | 34 KB |
| 依赖 | `burpsuite` |
| 官网 | <https://www.kali.org> |
| 源码 | <https://gitlab.com/kalilinux/packages/offsec-courses> |

### oletools

Analyze MS OLE2 files and MS Office documents Tools to analyze Microsoft OLE2 files (also called Structured Storage, Compound File Binary Format or Compound Document File Format), such as Microsoft Office 97-2003 documents, MSI files or Outlook messages, mainly for malware analysis, forensics and debugging. It is based on the olefile parser.

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/oletools/> |
| 版本 | 0.60.2 |
| 包 / 命令 | `oletools`、`ezhexviewer`、`ftguess`、`mraptor`、`msodde`、`olebrowse`、`oledir`、`olefile`、`oleid`、`olemap`、`olemeta`、`oleobj`、`oletimes`、`olevba`、`pyxswf`、`rtfobj` |
| 安装 | `sudo apt install oletools` |
| 占用空间 | 1.90 MB |
| 依赖 | `python3`、`python3-colorclass`、`python3-easygui`、`python3-msoffcrypto-tool`、`python3-olefile`、`python3-pcodedmp`、`python3-pyparsing`、`ezhexviewer`、`ftguess` |
| 官网 | <https://github.com/decalage2/oletools> |
| 源码 | <https://gitlab.com/kalilinux/packages/oletools> |

### openssh

Secure shell (SSH) client, for secure access to remote machines This is the portable version of OpenSSH, a free implementation of the Secure Shell protocol as specified by the IETF secsh working group. Ssh (Secure Shell) is a program for logging into a remote machine and for executing commands on a remote machine.

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/openssh/> |
| 版本 | 10.4p1 |
| 包 / 命令 | `openssh-client`、`scp`、`sftp`、`ssh`、`ssh-add`、`ssh-agent`、`ssh-argv0`、`ssh-copy-id`、`ssh-keyscan`、`openssh-client-udeb`、`openssh-common`、`ssh-keygen`、`openssh-server`、`sshd`、`openssh-server-udeb`、`openssh-sftp-server`、`openssh-tests`、`ssh-askpass-gnome` |
| 安装 | `sudo apt install openssh-client` |
| 占用空间 | 3.50 MB |
| 依赖 | `libc6`、`libedit2`、`libselinux1`、`libssl3t64`、`openssh-common` |
| 官网 | <https://www.openssh.com/> |
| 源码 | <https://salsa.debian.org/ssh-team/openssh> |

### openssh-ssh1

Secure shell (SSH) client for legacy SSH1 protocol This is the portable version of OpenSSH, a free implementation of the Secure Shell protocol as specified by the IETF secsh working group. Ssh (Secure Shell) is a program for logging into a remote machine and for executing commands on a remote machine.

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/openssh-ssh1/> |
| 版本 | 7.5p1 |
| 包 / 命令 | `openssh-client-ssh1`、`scp1`、`ssh-keygen1`、`ssh1` |
| 安装 | `sudo apt install openssh-client-ssh1` |
| 占用空间 | 1.40 MB |
| 依赖 | `libc6`、`libselinux1`、`libssl3t64`、`zlib1g`、`scp1` |
| 官网 | <https://www.openssh.com/> |
| 源码 | <https://salsa.debian.org/ssh-team/openssh-ssh1> |

### opentaxii

TAXII server implementation from EclecticIQ This package contains a robust Python implementation of TAXII Services that delivers rich feature set and friendly pythonic API built on top of well designed application. OpenTAXII is guaranteed to be compatible with Cabby, TAXII client library.

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/opentaxii/> |
| 版本 | 0.9.3 |
| 包 / 命令 | `opentaxii`、`opentaxii-add-api-root`、`opentaxii-add-collection`、`opentaxii-create-account`、`opentaxii-delete-blocks`、`opentaxii-job-cleanup`、`opentaxii-run-dev`、`opentaxii-sync-data`、`opentaxii-update-account`、`opentaxii-doc` |
| 安装 | `sudo apt install opentaxii` |
| 占用空间 | 347 KB |
| 依赖 | `python3`、`python3-blinker`、`python3-flask`、`python3-jwt`、`python3-libtaxii`、`python3-lxml`、`python3-marshmallow`、`python3-mypy-extensions`、`python3-pytz`、`python3-six`、`python3-sqlalchemy`、`python3-stix2` 等 |
| 官网 | <https://github.com/eclecticiq/OpenTAXII> |
| 源码 | <https://gitlab.com/kalilinux/packages/opentaxii> |

### openvpn

Virtual private network daemon OpenVPN is an application to securely tunnel IP networks over a single UDP or TCP port. It can be used to access remote sites, make secure point-to-point connections, enhance wireless security, etc. OpenVPN uses all of the encryption, authentication, and certification features provided by the OpenSSL library (any cipher, key size, or

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/openvpn/> |
| 版本 | 2.7.5 |
| 包 / 命令 | `openvpn` |
| 安装 | `sudo apt install openvpn` |
| 占用空间 | 1.80 MB |
| 官网 | <https://openvpn.net/community/> |
| 源码 | <https://salsa.debian.org/debian/openvpn> |

### owl

Open Apple Wireless Direct Link (AWDL) This package contains an open implementation of the Apple Wireless Direct Link (AWDL) ad hoc protocol for Linux and macOS written in C and part of the Open Wireless Link project. OWL runs in user space and makes use of Linux’s Netlink API for Wi-Fi specific operations such as channel switching and to integrate itself in the Linux

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/owl/> |
| 版本 | 0~git20220130 |
| 包 / 命令 | `owl` |
| 安装 | `sudo apt install owl` |
| 占用空间 | 86 KB |
| 依赖 | `libc6`、`libev4t64`、`libnl-3-200`、`libnl-genl-3-200`、`libnl-route-3-200`、`libpcap0.8t64`、`radiotap-library`、`owl` |
| 官网 | <https://owlink.org/> |
| 源码 | <https://gitlab.com/kalilinux/packages/owl> |

### pacu

Open Source AWS Exploitation Framework This package contains an open-source AWS exploitation framework, designed for offensive security testing against cloud environments. Created and maintained by Rhino Security Labs, Pacu allows penetration testers to exploit configuration flaws within an AWS account, using modules to easily expand its functionality. Current modules enable a range of attacks, including user

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/pacu/> |
| 版本 | 1.7.0 |
| 包 / 命令 | `pacu` |
| 安装 | `sudo apt install pacu` |
| 占用空间 | 13.38 MB |
| 依赖 | `awscli`、`python3`、`python3-boto3`、`python3-botocore`、`python3-colorama`、`python3-dsnap`、`python3-freezegun`、`python3-jq`、`python3-policyuniverse`、`python3-pycognito`、`python3-qrcode`、`python3-requests` 等 |
| 官网 | <https://rhinosecuritylabs.com/aws/pacu-open-source-aws-exploitation-framework/> |
| 源码 | <https://gitlab.com/kalilinux/packages/pacu> |

### parsero

Robots.txt audit tool Parsero is a free script written in Python which reads the Robots.txt file of a web server and looks at the Disallow entries. The Disallow entries tell the search engines what directories or files hosted on a web server mustn’t be indexed. For example, “Disallow: /portal/login” means that the content on www.example.com/portal/login

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/parsero/> |
| 版本 | 0.81~git20140929 |
| 包 / 命令 | `parsero` |
| 安装 | `sudo apt install parsero` |
| 占用空间 | 20 KB |
| 依赖 | `python3`、`python3-bs4`、`python3-urllib3`、`parsero` |
| 官网 | <https://github.com/behindthefirewalls/Parsero> |
| 源码 | <https://gitlab.com/kalilinux/packages/parsero> |

### passdetective

CLI tool that scans shell command history This package contains a command-line tool that scans the shell command history for mistakenly written passwords, API keys, and secrets. It uses regular expressions to identify potential sensitive information and helps avoid accidentally exposing sensitive data in the command history.

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/passdetective/> |
| 版本 | 1.0.7 |
| 包 / 命令 | `passdetective` |
| 安装 | `sudo apt install passdetective` |
| 占用空间 | 3.81 MB |
| 依赖 | `libc6` |
| 官网 | <https://github.com/aydinnyunus/PassDetective> |
| 源码 | <https://gitlab.com/kalilinux/packages/passdetective> |

### patchleaks

Go from a CVE number to the exact patched code and its vulnerability analysis This package contains a tool to compare two versions of a code‑base, highlight lines changed by vendor, and explain why they matter. Feed the tool an old and a patched version; PatchLeaks spots the security fix and provides detailed description so you can validate—or weaponize—it fast.

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/patchleaks/> |
| 版本 | 0.0~git20251113.3c53291 |
| 包 / 命令 | `patchleaks` |
| 安装 | `sudo apt install patchleaks` |
| 占用空间 | 26.88 MB |
| 依赖 | `libc6`、`libjs-jquery`、`node-fortawesome-fontawesome-free` |
| 官网 | <https://github.com/hatlesswizard/PatchLeaks> |
| 源码 | <https://gitlab.com/kalilinux/packages/patchleaks> |

### payloadsallthethings

Collection of useful payloads and bypasses A list of useful payloads and bypasses for Web Application Security and Pentest/CTF.

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/payloadsallthethings/> |
| 版本 | 2.1 |
| 包 / 命令 | `payloadsallthethings` |
| 安装 | `sudo apt install payloadsallthethings` |
| 占用空间 | 7.52 MB |
| 依赖 | `kali-defaults`、`payloadsallthethings` |
| 官网 | <https://github.com/swisskyrepo/PayloadsAllTheThings> |
| 源码 | <https://gitlab.com/kalilinux/packages/payloadsallthethings> |

### peirates

Kubernetes Penetration Testing tool This package contains a Kubernetes penetration tool, enables an attacker to escalate privilege and pivot through a Kubernetes cluster. It automates known techniques to steal and collect service accounts, obtain further code execution, and gain control of the cluster.

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/peirates/> |
| 版本 | 1.1.28 |
| 包 / 命令 | `peirates` |
| 安装 | `sudo apt install peirates` |
| 占用空间 | 80.82 MB |
| 依赖 | `libc6`、`peirates` |
| 官网 | <https://github.com/inguardians/peirates> |
| 源码 | <https://gitlab.com/kalilinux/packages/peirates> |

### penelope

Advanced shell handler for penetration testing and CTFs Penelope is a modern shell handler designed for penetration testers and CTF players. It provides a highly capable alternative to basic netcat listeners, streamlining reverse and bind shell management during post-exploitation. It operates entirely using the Python standard library, requiring no external dependencies.

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/penelope/> |
| 版本 | 0.21.0 |
| 包 / 命令 | `penelope` |
| 安装 | `sudo apt install penelope` |
| 占用空间 | 228 KB |
| 依赖 | `python3`、`penelope` |
| 官网 | <https://github.com/brightio/penelope> |
| 源码 | <https://salsa.debian.org/pkg-security-team/penelope> |

### phishery

Basic Auth Credential Harvester with Word Doc Template Injector This package contains a Simple SSL Enabled HTTP server with the primary purpose of phishing credentials via Basic Authentication. The power of phishery is best demonstrated by setting a Word document’s template to a phishery URL. This causes Microsoft Word to make a request to the URL, resulting in an Authentication Dialog being shown to the end-user. The

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/phishery/> |
| 版本 | 1.0.2 |
| 包 / 命令 | `phishery` |
| 安装 | `sudo apt install phishery` |
| 占用空间 | 5.05 MB |
| 依赖 | `libc6`、`phishery` |
| 官网 | <https://github.com/ryhanson/phishery> |
| 源码 | <https://gitlab.com/kalilinux/packages/phishery> |

### photon

Incredibly fast crawler designed for open source intelligence This package includes a fast and flexible crawler designed for open source intelligence (OSINT). Photon can extract the following data while crawling: URLs (in-scope & out-of-scope) URLs with parameters (example.com/gallery.php?id=2)

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/photon/> |
| 版本 | 1.3.0 |
| 包 / 命令 | `photon` |
| 安装 | `sudo apt install photon` |
| 占用空间 | 60 KB |
| 依赖 | `python3`、`python3-requests`、`python3-socks`、`python3-tld`、`python3-urllib3`、`photon` |
| 官网 | <https://github.com/s0md3v/Photon> |
| 源码 | <https://gitlab.com/kalilinux/packages/photon> |

### phpggc

Generate payloads that exploit unsafe object deserialization PHPGGC is a library of payloads exploiting unsafe object deserialization. It also provides a command-line tool to generate them.

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/phpggc/> |
| 版本 | 0.20230428 |
| 包 / 命令 | `phpggc` |
| 安装 | `sudo apt install phpggc` |
| 占用空间 | 650 KB |
| 依赖 | `php-cli`、`phpggc` |
| 官网 | <https://github.com/ambionics/phpggc> |
| 源码 | <https://gitlab.com/kalilinux/packages/phpggc> |

### phpsploit

Stealth post-exploitation framework This package contains a remote control framework, aiming to provide a stealth interactive shell-like connection over HTTP between client and web server. It is a post-exploitation tool capable to maintain access to a compromised web server for privilege escalation purposes.

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/phpsploit/> |
| 版本 | 3.2 |
| 包 / 命令 | `phpsploit` |
| 安装 | `sudo apt install phpsploit` |
| 占用空间 | 877 KB |
| 依赖 | `php`、`python3`、`python3-extproxy`、`python3-phpserialize`、`python3-pygments`、`python3-pyparsing`、`python3-socks`、`phpsploit` |
| 官网 | <https://github.com/nil0x42/phpsploit> |
| 源码 | <https://gitlab.com/kalilinux/packages/phpsploit> |

### plocate

Much faster locate plocate is a locate(1) based on posting lists, giving much faster searches on a much smaller index. It is a drop-in replacement for mlocate in nearly all aspects, and is fast on SSDs and non-SSDs alike.

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/plocate/> |
| 版本 | 1.1.24 |
| 包 / 命令 | `plocate`、`plocate-build`、`updatedb.plocate` |
| 安装 | `sudo apt install plocate` |
| 占用空间 | 572 KB |
| 依赖 | `adduser`、`libc6`、`libgcc-s1`、`libstdc++6`、`liburing2`、`libzstd1`、`plocate` |
| 官网 | <https://plocate.sesse.net/> |

### pnscan

Multi threaded port scanner Pnscan is a multi threaded port scanner that can scan a large network very quickly. If does not have all the features that nmap have but is much faster.

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/pnscan/> |
| 版本 | 1.14.1 |
| 包 / 命令 | `pnscan`、`t_listen` |
| 安装 | `sudo apt install pnscan` |
| 占用空间 | 65 KB |
| 依赖 | `libc6`、`pnscan` |
| 官网 | <https://github.com/ptrrkssn/pnscan> |
| 源码 | <https://salsa.debian.org/pkg-security-team/pnscan> |

### pocsuite3

Open-sourced remote vulnerability testing framework Pocsuite3 is an open-sourced remote vulnerability testing and proof-of-concept development framework developed by the Knownsec 404 Team. It comes with a powerful proof-of-concept engine, many nice features for the ultimate penetration testers and security researchers.

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/pocsuite3/> |
| 版本 | 2.1.0 |
| 包 / 命令 | `pocsuite3`、`poc-console`、`pocsuite` |
| 安装 | `sudo apt install pocsuite3` |
| 占用空间 | 943 KB |
| 依赖 | `binutils`、`nasm`、`python3`、`python3-chardet`、`python3-colorama`、`python3-colorlog`、`python3-dacite`、`python3-docker`、`python3-fake-factory`、`python3-lxml`、`python3-openssl`、`python3-packaging` 等 |
| 官网 | <https://pocsuite.org> |
| 源码 | <https://salsa.debian.org/pkg-security-team/pocsuite3> |

### pompem

Exploit and Vulnerability Finder Find exploit with a system of advanced search, designed to automate the search for Exploits and Vulnerability in the most important databases facilitating the work of pentesters, ethical hackers and forensics expert. Performs searches in databases: PacketStorm security, CXSecurity, ZeroDay, Vulners, National Vulnerability Database, WPScan Vulnerability Database. This tool is essential

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/pompem/> |
| 版本 | 0.2.0 |
| 包 / 命令 | `pompem` |
| 安装 | `sudo apt install pompem` |
| 占用空间 | 54 KB |
| 依赖 | `python3`、`python3-requests`、`pompem` |
| 官网 | <https://github.com/rfunix/Pompem> |
| 源码 | <https://salsa.debian.org/pkg-security-team/pompem> |

### portspoof

Enhance OS security through a set of techniques This package contains a service to enhance OS security through a set of following techniques: * All 65535 TCP ports are always open Instead of informing an attacker that a particular port is in a CLOSED or FILTERED state Portspoof will return SYN+ACK for every port connection

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/portspoof/> |
| 版本 | 1.4 |
| 包 / 命令 | `portspoof`、`portspoof-start`、`portspoof-stop` |
| 安装 | `sudo apt install portspoof` |
| 占用空间 | 1.06 MB |
| 依赖 | `iptables`、`kali-defaults`、`libc6`、`libgcc-s1`、`libstdc++6`、`portspoof` |
| 官网 | <https://github.com/drk1wi/portspoof> |
| 源码 | <https://gitlab.com/kalilinux/packages/portspoof> |

### poshc2

Proxy aware C2 framework This package contains a proxy aware C2 framework used to aid penetration testers with red teaming, post-exploitation and lateral movement. PoshC2 is primarily written in Python3 and follows a modular format to enable users to add their own modules and tools, allowing an extendible and flexible C2 framework. Out-of-the-box PoshC2 comes PowerShell/C# and Python3 implants

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/poshc2/> |
| 版本 | 9.0 |
| 包 / 命令 | `poshc2` |
| 安装 | `sudo apt install poshc2` |
| 占用空间 | 89.72 MB |
| 依赖 | `espeak`、`graphviz`、`libjs-bootstrap4`、`libjs-jquery`、`mingw-w64`、`mingw-w64-common`、`mingw-w64-i686-dev`、`mingw-w64-tools`、`mingw-w64-x86-64-dev`、`mono-devel`、`postgresql`、`python3` 等 |
| 官网 | <https://github.com/nettitude/PoshC2> |
| 源码 | <https://gitlab.com/kalilinux/packages/poshc2> |

### powershell

PowerShell is an automation and configuration management platform. It consists of a cross-platform command-line shell and associated scripting language.

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/powershell/> |
| 版本 | 7.6.2 |
| 包 / 命令 | `powershell`、`pwsh` |
| 安装 | `sudo apt install powershell` |
| 占用空间 | 188.65 MB |
| 依赖 | `libc6`、`libgcc1`、`libgssapi-krb5-2` |
| 官网 | <https://microsoft.com/powershell> |

### powershell-empire

PowerShell and Python post-exploitation agent This package contains a post-exploitation framework that includes a pure-PowerShell2.0 Windows agent, and a pure Python Linux/OS X agent. It is the merge of the previous PowerShell Empire and Python EmPyre projects. The framework offers cryptologically-secure communications and a flexible architecture. On the PowerShell side, Empire implements the ability to run

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/powershell-empire/> |
| 版本 | 6.6.0 |
| 包 / 命令 | `powershell-empire`、`starkiller`、`starkiller-start`、`starkiller-stop` |
| 安装 | `sudo apt install powershell-empire` |
| 占用空间 | 50.34 MB |
| 依赖 | `default-mysql-server`、`git`、`kali-defaults`、`pyinstaller`、`python3`、`python3-aiofiles`、`python3-alembic`、`python3-bcrypt`、`python3-cryptography`、`python3-docopt`、`python3-donut`、`python3-dropbox` 等 |
| 官网 | <https://github.com/BC-SECURITY/Empire> |
| 源码 | <https://gitlab.com/kalilinux/packages/powershell-empire> |

### princeprocessor

Standalone password candidate generator using the PRINCE algorithm Princeprocessor is a password candidate generator and can be thought of as an advanced combinator attack. Rather than taking as input two different wordlists and then outputting all the possible two word combinations though, princeprocessor only has one input wordlist and builds “chains” of combined words. These chains can have 1 to N words from the input wordlist

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/princeprocessor/> |
| 版本 | 0.22 |
| 包 / 命令 | `princeprocessor` |
| 安装 | `sudo apt install princeprocessor` |
| 占用空间 | 121 KB |
| 依赖 | `libc6`、`princeprocessor` |
| 官网 | <https://github.com/hashcat/princeprocessor> |
| 源码 | <https://salsa.debian.org/pkg-security-team/princeprocessor> |

### proxify

Swiss Army knife Proxy tool for HTTP/HTTPS traffic capture, manipulation This package contains a Swiss Army Knife Proxy for rapid deployments. It supports multiple operations such as request/response dump, filtering and manipulation via DSL language, upstream HTTP/Socks5 proxy. Additionally a replay utility allows to import the dumped traffic (request/responses with correct domain name) into burp or any other proxy by simply setting the

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/proxify/> |
| 版本 | 0.0.5 |
| 包 / 命令 | `proxify`、`mitmrelay`、`replay-proxify` |
| 安装 | `sudo apt install proxify` |
| 占用空间 | 35.08 MB |
| 依赖 | `libc6`、`mitmrelay` |
| 官网 | <https://github.com/projectdiscovery/proxify> |
| 源码 | <https://gitlab.com/kalilinux/packages/proxify> |

### proximoth

Control Frame Attack Vulnerability Detection Tool Proximoth is a command-line tool to detect Wi-Fi devices in proximity with Control Frame Attack.

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/proximoth/> |
| 版本 | 1.0.0 |
| 包 / 命令 | `proximoth` |
| 安装 | `sudo apt install proximoth` |
| 占用空间 | 961 KB |
| 依赖 | `libc6`、`libpcap0.8t64`、`proximoth` |
| 官网 | <https://technicaluserx.gitlab.io/proximoth> |
| 源码 | <https://gitlab.com/kalilinux/packages/proximoth> |

### pskracker

Collection of WPA/WPA2/WPS default keys generators/pingens This package contains a collection of WPA/WPA2/WPS default algorithms/password generators/pingens written in C. This is useful for testing/auditing wireless networks and contains bleeding edge algorithms.

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/pskracker/> |
| 版本 | 0.3.1 |
| 包 / 命令 | `pskracker`、`pskracker-data` |
| 安装 | `sudo apt install pskracker` |
| 占用空间 | 37 KB |
| 依赖 | `libc6`、`pskracker-data`、`pskracker` |
| 官网 | <https://github.com/soxrok2212/PSKracker> |
| 源码 | <https://gitlab.com/kalilinux/packages/pskracker> |

### pspy

Monitor Linux processes without root permissions pspy is a command line tool designed to snoop on processes without need for root permissions. It allows you to see commands run by other users, cron jobs, etc. as they execute. Great for enumeration of Linux systems in CTFs. Also great to demonstrate your colleagues why passing secrets as arguments on the command line is a bad idea.

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/pspy/> |
| 版本 | 1.2.1 |
| 包 / 命令 | `pspy`、`pspy-binaries` |
| 安装 | `sudo apt install pspy` |
| 占用空间 | 9.21 MB |
| 依赖 | `libc6`、`pspy` |
| 官网 | <https://github.com/DominicBreuker/pspy> |
| 源码 | <https://gitlab.com/kalilinux/packages/pspy> |

### pwncat

Netcat on steroids This package contains Netcat on steroids with Firewall, IDS/IPS evasion, bind and reverse shell, self-injecting shell and port forwarding magic - and its fully scriptable with Python (PSE).

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/pwncat/> |
| 版本 | 0.1.2 |
| 包 / 命令 | `pwncat` |
| 安装 | `sudo apt install pwncat` |
| 占用空间 | 5.63 MB |
| 依赖 | `python3`、`pwncat` |
| 官网 | <https://github.com/cytopia/pwncat> |
| 源码 | <https://gitlab.com/kalilinux/packages/pwncat> |

### pyinstaller

Utility to bundle a Python application into a single package PyInstaller reads a Python script written by you. It analyzes your code to discover every other module and library your script needs in order to execute. Then it collects copies of all those files and puts them with your script in a single folder, or optionally in a single executable file. This package contains the executables. It depends on ‘python3-pyinstaller’,

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/pyinstaller/> |
| 版本 | 6.19.0 |
| 包 / 命令 | `pyinstaller`、`pyi-archive_viewer`、`pyi-bindepend`、`pyi-grab_version`、`pyi-makespec`、`pyi-set_version`、`python3-pyinstaller` |
| 安装 | `sudo apt install pyinstaller` |
| 占用空间 | 104 KB |
| 依赖 | `python3`、`python3-pyinstaller`、`pyi-archive_viewer` |
| 官网 | <https://pyinstaller.org/en/stable/> |
| 源码 | <https://salsa.debian.org/python-team/packages/pyinstaller> |

### pyinstxtractor

PyInstalller Extractor PyInstaller Extractor is a Python script to extract the contents of a PyInstaller generated executable file.

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/pyinstxtractor/> |
| 版本 | 2026.07 |
| 包 / 命令 | `pyinstxtractor` |
| 安装 | `sudo apt install pyinstxtractor` |
| 占用空间 | 29 KB |
| 依赖 | `python3`、`pyinstxtractor` |
| 官网 | <https://github.com/extremecoders-re/pyinstxtractor> |
| 源码 | <https://gitlab.com/kalilinux/packages/pyinstxtractor> |

### python-defaults

Package depending on all supported Python2 debugging packages The package currently depends on libpython2.7-dbg, in the future, dependencies on jython (Python2 for a JVM) and ironpython (Python2 for Mono) may be added. This package is a dependency package used as a build dependency for other packages to avoid hardcoded dependencies on specific Python2 debug packages.

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/python-defaults/> |
| 版本 | 2.7.18 |
| 包 / 命令 | `libpython-all-dbg`、`libpython-all-dev`、`libpython2-dbg`、`x86_64-linux-gnu-python2-dbg-config`、`libpython2-dev`、`x86_64-linux-gnu-python2-config`、`libpython2-stdlib`、`python-all`、`python-all-dbg`、`python-all-dev`、`python2`、`pdb2`、`pydoc2`、`pygettext2`、`python2-dbg`、`python2-dbg-config`、`python2-dev`、`python2-config`、`python2-doc`、`python2-minimal`、`pyclean`、`pycompile`、`pyversions` |
| 安装 | `sudo apt install libpython-all-dbg` |
| 占用空间 | 7 KB |
| 依赖 | `libpython2-dbg`、`libpython2.7-dbg`、`libpython-all-dev` |
| 官网 | <https://www.python.org/> |
| 源码 | <https://salsa.debian.org/cpython-team/python-defaults> |

### python-pipx

Execute binaries from Python packages in isolated environments pipx allows you to… Run the latest version of a CLI application from a package in a temporary virtual environment, leaving your system untouched after it finishes. Install packages to isolated virtual environments,

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/python-pipx/> |
| 版本 | 1.15.0 |
| 包 / 命令 | `pipx` |
| 安装 | `sudo apt install pipx` |
| 占用空间 | 4.30 MB |
| 依赖 | `python3`、`python3-argcomplete`、`python3-packaging`、`python3-platformdirs`、`python3-userpath`、`python3-venv`、`pipx` |
| 官网 | <https://github.com/pypa/pipx> |
| 源码 | <https://salsa.debian.org/python-team/packages/python-pipx> |

### python-virtualenv

Python virtual environment creator virtualenv is a tool to create isolated Python environments, each invokable with its own Python executable. Each instance can have different sets of modules, installable via pip. Virtual Python instances can also be created without root access. Since Python 3.3, a subset of it has been integrated into the standard library

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/python-virtualenv/> |
| 版本 | 21.5.1 |
| 包 / 命令 | `python3-virtualenv`、`virtualenv` |
| 安装 | `sudo apt install python3-virtualenv` |
| 占用空间 | 374 KB |
| 依赖 | `python3`、`python3-discovery`、`python3-distlib`、`python3-filelock`、`python3-pip-whl`、`python3-platformdirs`、`python3-setuptools-whl`、`virtualenv` |
| 官网 | <https://virtualenv.pypa.io/> |
| 源码 | <https://salsa.debian.org/python-team/packages/python-virtualenv> |

### qsreplace

Accept URLs on stdin, replace all query string values with a user-supplied value Accept URLs on stdin, replace all query string values with a user-supplied value, only output each combination of query string parameters once per host and path.

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/qsreplace/> |
| 版本 | 0.0.3 |
| 包 / 命令 | `qsreplace` |
| 安装 | `sudo apt install qsreplace` |
| 占用空间 | 1.75 MB |
| 官网 | <https://github.com/tomnomnom/qsreplace> |
| 源码 | <https://gitlab.com/kalilinux/packages/qsreplace> |

### quark-engine

Android Malware (Analysis | Scoring System) Quark-Engine is a full-featured Android analysis framework written in Python for hunting threat intelligence inside the APK, DEX files. Since it is rule-based, you can use the ones built-in or customize as needed. With ideas decoded from criminal law, Quark-Engine has its unique

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/quark-engine/> |
| 版本 | 26.5.1 |
| 包 / 命令 | `quark-engine`、`freshquark`、`quark` |
| 安装 | `sudo apt install quark-engine` |
| 占用空间 | 322.08 MB |
| 依赖 | `python3`、`rizin`、`freshquark` |
| 官网 | <https://github.com/ev-flow/quark-engine> |
| 源码 | <https://gitlab.com/kalilinux/packages/quark-engine> |

### raven

Python tool that extends the capabilities of the http.server Python module This package contains a Python tool that extends the capabilities of the http.server Python module by offering a self-contained file upload web server. While the common practice is to use python3 -m http.server 80 to serve files for remote client downloads, Raven addresses the need for a similar solution when you need the ability to receive files from remote clients. This becomes

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/raven/> |
| 版本 | 1.1.0 |
| 包 / 命令 | `raven` |
| 安装 | `sudo apt install raven` |
| 占用空间 | 46 KB |
| 依赖 | `python3`、`raven` |
| 官网 | <https://github.com/gh0x0st/raven> |
| 源码 | <https://salsa.debian.org/pkg-security-team/raven> |

### reconspider

OSINT Framework for scanning IP Address, Emails, Websites, Organizations This package contains Advanced Open Source Intelligence (OSINT) Framework for scanning IP Address, Emails, Websites, Organizations and find out information from different sources. ReconSpider can be used by Infosec Researchers, Penetration Testers, Bug Hunters and Cyber Crime Investigators to find deep information about their

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/reconspider/> |
| 版本 | 1.0.7 |
| 包 / 命令 | `reconspider` |
| 安装 | `sudo apt install reconspider` |
| 占用空间 | 371.90 MB |
| 依赖 | `h8mail`、`python3`、`python3-bs4`、`python3-click`、`python3-gmplot`、`python3-ip2proxy`、`python3-lxml`、`python3-nmap`、`python3-paramiko`、`python3-pil`、`python3-prompt-toolkit`、`python3-pythonping` 等 |
| 官网 | <https://github.com/bhavsec/reconspider> |
| 源码 | <https://gitlab.com/kalilinux/packages/reconspider> |

### redsnarf

Pentesting tool for retrieving credentials from Windows workstations This package contains a pentesting / redteaming tool by Ed Williams for retrieving hashes and credentials from Windows workstations, servers and domain controllers using OpSec Safe Techniques. RedSnarf functionality includes: Retrieval of local SAM hashes Enumeration of user/s running with elevated system privileges and their

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/redsnarf/> |
| 版本 | 0~git20170822 |
| 包 / 命令 | `redsnarf` |
| 安装 | `sudo apt install redsnarf` |
| 占用空间 | 12.00 MB |
| 依赖 | `creddump7`、`passing-the-hash`、`python3-docopt`、`python3-impacket`、`python3-ipy`、`python3-ldap`、`python3-libnmap`、`python3-netaddr`、`python3-pycryptodome`、`python3-pyuserinput`、`python3-smb`、`python3-termcolor` 等 |
| 官网 | <https://github.com/nccgroup/redsnarf> |
| 源码 | <https://gitlab.com/kalilinux/packages/redsnarf> |

### rekono-kbx

Automation platform for pentesting Rekono is an automation platform that combines different hacking tools to complete pentesting processes. Rekono combines other hacking tools and its results to execute complete pentesting processes against a target in an automated way. The findings obtained during the executions will be sent to the user via email or

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/rekono-kbx/> |
| 版本 | 1.6.6 |
| 包 / 命令 | `rekono-kbx`、`rekono` |
| 安装 | `sudo apt install rekono-kbx` |
| 占用空间 | 133 KB |
| 官网 | <https://github.com/pablosnt/rekono> |
| 源码 | <https://gitlab.com/kalilinux/packages/rekono-kbx> |

### rev-proxy-grapher

Reverse proxy grapher This package contains a useful little tool that will generate a nice graphviz graph illustrating your reverse proxy flow. It takes a manually curated YAML file describing the topology of your network, proxy definitions, and optionally a collection of nmap output files for additional port/service information and output a graph in any format supported by graphviz.

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/rev-proxy-grapher/> |
| 版本 | 0~git20180301 |
| 包 / 命令 | `rev-proxy-grapher` |
| 安装 | `sudo apt install rev-proxy-grapher` |
| 占用空间 | 207 KB |
| 依赖 | `python3`、`python3-netaddr`、`python3-nmap`、`python3-pydotplus`、`python3-yaml`、`rev-proxy-grapher` |
| 官网 | <https://github.com/mricon/rev-proxy-grapher> |
| 源码 | <https://gitlab.com/kalilinux/packages/rev-proxy-grapher> |

### ridenum

Null session RID cycle attack tool Rid Enum is a RID cycling attack that attempts to enumerate user accounts through null sessions and the SID to RID enum. If you specify a password file, it will automatically attempt to brute force the user accounts when its finished enumerating.

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/ridenum/> |
| 版本 | 1.7 |
| 包 / 命令 | `ridenum` |
| 安装 | `sudo apt install ridenum` |
| 占用空间 | 32 KB |
| 依赖 | `python3`、`python3-pexpect`、`ridenum` |
| 官网 | <https://github.com/trustedsec/ridenum> |
| 源码 | <https://gitlab.com/kalilinux/packages/ridenum> |

### rling

Better rli This package is similar to the rli utility found in hashcat-utils, but much, much faster. rli compares a single file against another file(s) and removes all duplicates.

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/rling/> |
| 版本 | 1.84 |
| 包 / 命令 | `rling`、`dedupe`、`getpass`、`rehex`、`splitlen` |
| 安装 | `sudo apt install rling` |
| 占用空间 | 166 KB |
| 依赖 | `libc6`、`libjudydebian1`、`zlib1g`、`dedupe`、`getpass` |
| 官网 | <https://github.com/Cynosureprime/rling> |
| 源码 | <https://gitlab.com/kalilinux/packages/rling> |

### robotstxt

Robots.txt exclusion protocol implementation for Go language This package contains a robots.txt exclusion protocol implementation for Go language (golang).

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/robotstxt/> |
| 版本 | 1.1.1 |
| 包 / 命令 | `golang-github-temoto-robotstxt-dev`、`robotstxt`、`robots.txt-check` |
| 安装 | `sudo apt install robotstxt` |
| 占用空间 | 5.17 MB |
| 依赖 | `libc6`、`robots.txt-check` |
| 官网 | <https://github.com/temoto/robotstxt> |
| 源码 | <https://gitlab.com/kalilinux/packages/robotstxt> |

### ropper

Rop gadget finder and binary information tool This package contains scripts that display info about files in different formats and find gadgets to build ROPs chains for different architectures (x86/x86_64, ARM/ARM64, MIPS, PowerPC). For disassembly ropper uses the Capstone Framework.

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/ropper/> |
| 版本 | 1.13.8 |
| 包 / 命令 | `ropper` |
| 安装 | `sudo apt install ropper` |
| 占用空间 | 402 KB |
| 依赖 | `python3`、`python3-capstone`、`python3-filebytes`、`python3-pkg-resources`、`ropper` |
| 官网 | <https://scoding.de/ropper/> |
| 源码 | <https://gitlab.com/kalilinux/packages/ropper> |

### routerkeygenpc

Router Keygen generate default WPA/WEP keys This package generates default WPA/WEP keys for the several routers: Thomson based routers ( this includes Thomson, SpeedTouch, Orange, Infinitum, BBox, DMax, BigPond, O2Wireless, Otenet, Cyta , TN_private, Blink ) DLink ( only some models )

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/routerkeygenpc/> |
| 版本 | 1.1.0 |
| 包 / 命令 | `routerkeygenpc`、`routerkeygen`、`routerkeygen-cli` |
| 安装 | `sudo apt install routerkeygenpc` |
| 占用空间 | 5.67 MB |
| 依赖 | `libc6`、`libgcc-s1`、`libqt5core5t64`、`libqt5dbus5t64` |
| 官网 | <https://github.com/routerkeygen/routerkeygenPC> |
| 源码 | <https://gitlab.com/kalilinux/packages/routerkeygenpc> |

### routersploit

Exploitation Framework for Embedded Devices This package contains an open-source exploitation framework dedicated to embedded devices. It consists of various modules that aids penetration testing operations: exploits - modules that take advantage of identified vulnerabilities. creds - modules designed to test credentials against network services.

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/routersploit/> |
| 版本 | 3.4.7 |
| 包 / 命令 | `routersploit`、`rsf.py` |
| 安装 | `sudo apt install routersploit` |
| 占用空间 | 2.22 MB |
| 依赖 | `python3`、`python3-paramiko`、`python3-pkg-resources`、`python3-pycryptodome`、`python3-pysnmp4`、`python3-requests`、`python3-zombie-telnetlib`、`routersploit` |
| 官网 | <https://github.com/threat9/routersploit> |
| 源码 | <https://gitlab.com/kalilinux/packages/routersploit> |

### rubeus

Raw Kerberos interaction and abuses Rubeus is a C# toolset for raw Kerberos interaction and abuses. It is heavily adapted from Benjamin Delpy’s Kekeo project and Vincent LE TOUX’s MakeMeEnterpriseAdmin project.

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/rubeus/> |
| 版本 | 1.6.4 |
| 包 / 命令 | `rubeus` |
| 安装 | `sudo apt install rubeus` |
| 占用空间 | 290 KB |
| 官网 | <https://github.com/GhostPack/Rubeus> |
| 源码 | <https://gitlab.com/kalilinux/packages/rubeus> |

### ruby-pedump

Dump win32 PE executable files with a pure ruby This package contains a script to dump headers, sections, extract resources of win32 PE exe,dll,etc

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/ruby-pedump/> |
| 版本 | 0.6.5 |
| 包 / 命令 | `ruby-pedump`、`pedump-ruby` |
| 安装 | `sudo apt install ruby-pedump` |
| 占用空间 | 2.41 MB |
| 依赖 | `ruby`、`ruby-awesome-print`、`ruby-iostruct`、`ruby-multipart-post`、`ruby-rainbow`、`ruby-zhexdump`、`pedump-ruby` |
| 官网 | <http://github.com/zed-0xff/pedump> |
| 源码 | <https://gitlab.com/kalilinux/packages/ruby-pedump> |

### rustscan

Modern Port Scanner The Modern Port Scanner. Find ports quickly (3 seconds at its fastest). Run scripts through our scripting engine (Python, Lua, Shell supported). Scans all 65k ports in 3 seconds. Full scripting engine support. Automatically pipe results into Nmap, or use our scripts (or write your own) to do whatever you want.

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/rustscan/> |
| 版本 | 2.4.1 |
| 包 / 命令 | `rustscan` |
| 安装 | `sudo apt install rustscan` |
| 占用空间 | 4.50 MB |
| 依赖 | `libc6`、`libgcc-s1`、`rustscan` |
| 官网 | <https://github.com/bee-san/RustScan> |
| 源码 | <https://gitlab.com/kalilinux/packages/rustscan> |

### s3scanner

Tool to find open S3 buckets and dump their contents This package contains a tool to find open S3 buckets and dump their contents. The features are: zap Multi-threaded scanning telescope Supports tons of S3-compatible APIs female_detective Scans all bucket permissions to find misconfigurations

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/s3scanner/> |
| 版本 | 3.0.0 |
| 包 / 命令 | `s3scanner` |
| 安装 | `sudo apt install s3scanner` |
| 占用空间 | 17.85 MB |
| 依赖 | `libc6`、`s3scanner` |
| 官网 | <https://github.com/sa7mon/s3scanner> |
| 源码 | <https://gitlab.com/kalilinux/packages/s3scanner> |

### sara

RouterOS Security Inspector This package contains an autonomous RouterOS configuration analyzer for finding security issues on MikroTik hardware.

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/sara/> |
| 版本 | 1.3.1 |
| 包 / 命令 | `sara` |
| 安装 | `sudo apt install sara` |
| 占用空间 | 74 KB |
| 依赖 | `python3`、`python3-colorama`、`python3-netmiko`、`python3-packaging`、`python3-requests`、`sara` |
| 官网 | <https://github.com/caster0x00/sara> |
| 源码 | <https://gitlab.com/kalilinux/packages/sara> |

### sdrangel

Qt-based SDR front-end for various devices SDR front-end supporting many hardware and software receivers/transmitter, including: RTL-SDR, BladeRF, HackRF and others. It uses Qt framework and OpenGL for graphical rendering, works on many operating systems. Supported modes:

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/sdrangel/> |
| 版本 | 7.27.2 |
| 包 / 命令 | `sdrangel`、`sdrangelbench`、`sdrangelsrv` |
| 安装 | `sudo apt install sdrangel` |
| 占用空间 | 109.88 MB |
| 依赖 | `libairspy0`、`libairspyhf1`、`libavcodec62`、`libavformat62`、`libavutil60`、`libbladerf2`、`libc6`、`libcodec2-1.2`、`libfftw3-single3`、`libflac14`、`libgcc-s1`、`libhackrf0` 等 |
| 官网 | <https://www.sdrangel.org/> |
| 源码 | <https://salsa.debian.org/debian-hamradio-team/sdrangel> |

### sendemail

Lightweight, command line SMTP email client SendEmail is a lightweight, completely command line based, SMTP email agent. It was designed to be used in bash scripts, Perl programs, and web sites, but it is also quite useful in many other contexts. SendEmail is written in Perl and is unique in that it requires no special modules. It has a straight forward interface,

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/sendemail/> |
| 版本 | 1.56 |
| 包 / 命令 | `sendemail` |
| 安装 | `sudo apt install sendemail` |
| 占用空间 | 107 KB |
| 依赖 | `libio-socket-inet6-perl`、`perl` |
| 官网 | <http://caspian.dotconf.net/menu/Software/SendEmail/> |
| 源码 | <https://github.com/mogaal/sendemail> |

### sharphound

C# Data Collector for BloodHound This package contains the pre-built SharpHound.

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/sharphound/> |
| 版本 | 2.14.0 |
| 包 / 命令 | `sharphound` |
| 安装 | `sudo apt install sharphound` |
| 占用空间 | 3.10 MB |
| 官网 | <https://github.com/SpecterOps/SharpHound> |
| 源码 | <https://gitlab.com/kalilinux/packages/sharphound> |

### sharpshooter

Payload Generation Framework SharpShooter is a payload creation framework for the retrieval and execution of arbitrary CSharp source code. SharpShooter is capable of creating payloads in a variety of formats, including HTA, JS, VBS and WSF.

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/sharpshooter/> |
| 版本 | 2.0 |
| 包 / 命令 | `sharpshooter` |
| 安装 | `sudo apt install sharpshooter` |
| 占用空间 | 538 KB |
| 依赖 | `python3`、`python3-jsmin`、`sharpshooter` |
| 官网 | <https://github.com/mdsecactivebreach/SharpShooter> |
| 源码 | <https://gitlab.com/kalilinux/packages/sharpshooter> |

### shed

Simple hex editor with a pico-style interface shed (Simple Hex Editor) is an easy application for viewing and editing files in text mode, using ncurses. The main features are: Displays each byte as ascii, hex, decimal, octal and binary; Allows changes to be input in all of the above displayed modes, with bit toggling in the binary column;

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/shed/> |
| 版本 | 1.16 |
| 包 / 命令 | `shed` |
| 安装 | `sudo apt install shed` |
| 占用空间 | 61 KB |
| 依赖 | `libc6`、`libncurses6`、`libtinfo6`、`shed` |
| 官网 | <http://shed.sf.net> |
| 源码 | <https://salsa.debian.org/pkg-security-team/shed> |

### shell-gpt

Command-line productivity tool powered by AI large language models A command-line productivity tool powered by AI large language models (LLM). This command-line tool offers streamlined generation of shell commands, code snippets, documentation, eliminating the need for external resources (like Google search). Supports Linux, macOS, Windows and compatible with all major Shells like PowerShell, CMD, Bash, Zsh, etc.

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/shell-gpt/> |
| 版本 | 1.5.1 |
| 包 / 命令 | `shell-gpt`、`sgpt` |
| 安装 | `sudo apt install shell-gpt` |
| 占用空间 | 111 KB |
| 依赖 | `python3`、`python3-distro`、`python3-openai`、`python3-prompt-toolkit`、`python3-rich`、`python3-typer`、`sgpt` |
| 官网 | <https://github.com/TheR1D/shell_gpt> |
| 源码 | <https://gitlab.com/kalilinux/packages/shell-gpt> |

### shellfire

Exploiting LFI, RFI, and command injection vulnerabilities This package contains an exploitation shell which focuses on exploiting LFI, RFI, and command injection vulnerabilities.

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/shellfire/> |
| 版本 | 0.16 |
| 包 / 命令 | `shellfire` |
| 安装 | `sudo apt install shellfire` |
| 占用空间 | 104 KB |
| 依赖 | `python3`、`python3-cryptography`、`python3-pkg-resources`、`python3-requests`、`shellfire` |
| 官网 | <https://github.com/unix-ninja/shellfire> |
| 源码 | <https://gitlab.com/kalilinux/packages/shellfire> |

### sherlock

Find usernames across social networks Sherlock relies on the site’s designers providing a unique URL for a registered username. To determine if a username is available, Sherlock queries that URL, and uses to response to understand if there is a claimed username already there. Currently, the tool is capable of locating users on more than 300 social

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/sherlock/> |
| 版本 | 0.16.0 |
| 包 / 命令 | `sherlock` |
| 安装 | `sudo apt install sherlock` |
| 占用空间 | 187 KB |
| 依赖 | `python3`、`python3-certifi`、`python3-colorama`、`python3-openpyxl`、`python3-pandas`、`python3-requests`、`python3-requests-futures`、`python3-socks`、`python3-stem`、`sherlock` |
| 官网 | <https://github.com/sherlock-project/sherlock> |
| 源码 | <https://salsa.debian.org/pkg-security-team/sherlock> |

### sickle-pdk

Payload development kit Sickle is a payload development kit originally created to aid in crafting shellcode, however it can be used in crafting payloads for other exploit types as well (non-binary). Although the current modules are mostly aimed towards assembly this tool is not limited to shellcode.

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/sickle-pdk/> |
| 版本 | 4.1.1 |
| 包 / 命令 | `sickle-pdk` |
| 安装 | `sudo apt install sickle-pdk` |
| 占用空间 | 471 KB |
| 依赖 | `python3`、`python3-capstone`、`python3-keystone-engine`、`sickle-pdk` |
| 官网 | <https://github.com/wetw0rk/sickle-pdk> |
| 源码 | <https://gitlab.com/kalilinux/packages/sickle-pdk> |

### sigma-cli

Sigma command line interface This package contains the Sigma command line interface using the pySigma library to manage, list and convert Sigma rules into query languages.

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/sigma-cli/> |
| 版本 | 3.1.0 |
| 包 / 命令 | `sigma-cli` |
| 安装 | `sudo apt install sigma-cli` |
| 占用空间 | 126 KB |
| 依赖 | `python3`、`python3-click`、`python3-colorama`、`python3-prettytable`、`python3-sigma`、`sigma-cli` |
| 官网 | <https://github.com/SigmaHQ/sigma-cli> |
| 源码 | <https://gitlab.com/kalilinux/packages/sigma-cli> |

### silenttrinity

Asynchronous, collaborative post-exploitation agent This package contains a modern, asynchronous, multiplayer & multiserver C2/post-exploitation framework powered by Python 3 and .NETs DLR. It’s the culmination of an extensive amount of research into using embedded third-party .NET scripting languages to dynamically call .NET API’s, a technique the author coined as BYOI (Bring Your Own Interpreter). The aim of this tool and

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/silenttrinity/> |
| 版本 | 0.4.6dev~20211029 |
| 包 / 命令 | `silenttrinity` |
| 安装 | `sudo apt install silenttrinity` |
| 占用空间 | 4.89 MB |
| 依赖 | `python3`、`python3-aiocmd`、`python3-aiofiles`、`python3-aiosqlite`、`python3-aiowinreg`、`python3-asciitree`、`python3-asn1crypto`、`python3-blinker`、`python3-certifi`、`python3-cffi`、`python3-chardet`、`python3-click` 等 |
| 官网 | <https://github.com/byt3bl33d3r/SILENTTRINITY> |
| 源码 | <https://gitlab.com/kalilinux/packages/silenttrinity> |

### sippts

Set of tools to audit SIP based VoIP Systems Sippts is a set of tools to audit VoIP servers and devices using SIP protocol. Sippts is programmed in Python and it allows pentesters to check the security of a VoIP server using SIP protocol.

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/sippts/> |
| 版本 | 4.1.2 |
| 包 / 命令 | `sippts`、`sippts-gui` |
| 安装 | `sudo apt install sippts` |
| 占用空间 | 762 KB |
| 依赖 | `python3`、`python3-ipy`、`python3-netifaces`、`python3-pyshark`、`python3-rel`、`python3-requests`、`python3-scapy`、`python3-websocket`、`sippts` |
| 官网 | <https://github.com/Pepelux/sippts> |
| 源码 | <https://gitlab.com/kalilinux/packages/sippts> |

### slimtoolkit

Optimization of your containers This package contains Slim(toolkit). It was called DockerSlim, and it is now just Slim (SlimToolkit). It is a tool for developers with a number of different commands (build, xray, lint, debug and others) to simplify and optimize your developer experience with containers. It makes your containers better, smaller and more secure

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/slimtoolkit/> |
| 版本 | 1.40.11 |
| 包 / 命令 | `slimtoolkit`、`slim-sensor` |
| 安装 | `sudo apt install slimtoolkit` |
| 占用空间 | 67.39 MB |
| 依赖 | `docker.io`、`libc6`、`slim-sensor` |
| 官网 | <https://github.com/slimtoolkit/slim> |
| 源码 | <https://gitlab.com/kalilinux/packages/slimtoolkit> |

### sliver

Implant framework This package contains a general purpose cross-platform implant framework that supports C2 over Mutual-TLS, HTTP(S), and DNS. Implants are dynamically compiled with unique X.509 certificates signed by a per-instance certificate authority generated when you first run the binary.

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/sliver/> |
| 版本 | 1.7.1 |
| 包 / 命令 | `sliver`、`sliver-client`、`sliver-server` |
| 安装 | `sudo apt install sliver` |
| 占用空间 | 290.89 MB |
| 官网 | <https://github.com/BishopFox/sliver> |
| 源码 | <https://gitlab.com/kalilinux/packages/sliver> |

### sn0int

Semi-automatic OSINT framework and package manager sn0int is a semi-automatic OSINT framework and package manager. It was built for IT security professionals and bug hunters to gather intelligence about a given target or about yourself. sn0int is enumerating attack surface by semi-automatically processing public information and mapping the results in a unified format for followup investigations.

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/sn0int/> |
| 版本 | 0.26.1 |
| 包 / 命令 | `sn0int` |
| 安装 | `sudo apt install sn0int` |
| 占用空间 | 16.86 MB |
| 依赖 | `libc6`、`libgcc-s1`、`libseccomp2`、`libsodium26`、`libsqlite3-0`、`publicsuffix`、`sn0int` |
| 官网 | <https://github.com/kpcyrd/sn0int> |
| 源码 | <https://gitlab.com/kalilinux/packages/sn0int> |

### snaffler-ng

SMB share credential and sensitive data scanner Impacket port of Snaffler, a post-exploitation tool that discovers readable SMB shares, walks directory trees, and identifies credentials and sensitive data on Windows file systems. Features include NTLM and Kerberos authentication, DFS namespace discovery, regex-based file and content classification with 103 built-in rules, archive

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/snaffler-ng/> |
| 版本 | 1.5.13 |
| 包 / 命令 | `snaffler-ng`、`snaffler` |
| 安装 | `sudo apt install snaffler-ng` |
| 占用空间 | 1.85 MB |
| 依赖 | `python3`、`python3-cryptography`、`python3-impacket`、`python3-rich`、`python3-tomlkit`、`python3-typer`、`snaffler` |
| 官网 | <https://github.com/totekuh/snaffler-ng> |
| 源码 | <https://gitlab.com/kalilinux/packages/snaffler-ng> |

### snmpenum

SNMP tabledump This package contains a simple Perl script to enumerate information on Machines that are running SNMP.

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/snmpenum/> |
| 版本 | 0 |
| 包 / 命令 | `snmpenum` |
| 安装 | `sudo apt install snmpenum` |
| 占用空间 | 21 KB |
| 依赖 | `libnet-snmp-perl`、`perl`、`snmpenum` |
| 官网 | <https://packetstormsecurity.com/files/download/31079/snmpenum.zip> |
| 源码 | <https://gitlab.com/kalilinux/packages/snmpenum> |

### snort

Flexible Network Intrusion Detection System Snort is a libpcap-based packet sniffer/logger which can be used as a lightweight network intrusion detection system. It features rules-based logging and can perform content searching/matching in addition to detecting a variety of other attacks and probes, such as buffer overflows, stealth port scans, CGI attacks, SMB probes, and much more.

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/snort/> |
| 版本 | 3.12.2.0 |
| 包 / 命令 | `snort`、`appid_detector_builder.sh`、`show_flows`、`snort2lua`、`u2boat`、`u2spewfoo`、`snort-common`、`snort-common-libraries`、`snort-doc`、`snort-rules-default` |
| 安装 | `sudo apt install snort` |
| 占用空间 | 11.15 MB |
| 依赖 | `adduser` |
| 官网 | <https://www.snort.org/> |
| 源码 | <https://gitlab.com/kalilinux/packages/snort> |

### snowdrop

Plain text watermarking and watermark recovery Snowdrop provides reliable, difficult to remove steganographic watermarking of text documents (internal memos, draft research papers, advisories and other writing) and C sources (limited distribution software, licensed software, or freely available code) so that: (1) leaks can be identified if the data goes public.

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/snowdrop/> |
| 版本 | 0.02b |
| 包 / 命令 | `snowdrop`、`sd-c`、`sd-eng`、`sd-engf` |
| 安装 | `sudo apt install snowdrop` |
| 占用空间 | 194 KB |
| 依赖 | `libc6`、`libssl3t64`、`sd-c` |
| 官网 | <http://lcamtuf.coredump.cx/> |
| 源码 | <https://salsa.debian.org/pkg-security-team/snowdrop/tree/debian/master> |

### sparrow-wifi

Graphical Wi-Fi Analyzer for Linux This package contains a graphical Wi-Fi analyzer for Linux. It provides a more comprehensive GUI-based replacement for tools like inSSIDer and linssid that runs specifically on Linux. In its most comprehensive use cases, sparrow-wifi integrates Wi-Fi, software-defined radio (hackrf), advanced bluetooth tools (traditional and Ubertooth), traditional GPS (via gpsd), and drone/rover GPS

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/sparrow-wifi/> |
| 版本 | 2.0 |
| 包 / 命令 | `sparrow-wifi`、`sparrowwifiagent` |
| 安装 | `sudo apt install sparrow-wifi` |
| 占用空间 | 1.94 MB |
| 依赖 | `gpsd`、`gpsd-clients`、`python3`、`python3-dateutil`、`python3-dronekit`、`python3-gps3`、`python3-manuf`、`python3-matplotlib`、`python3-numpy`、`python3-pyqt5.qsci`、`python3-pyqt5.qtchart`、`python3-requests` 等 |
| 官网 | <https://github.com/ghostop14/sparrow-wifi> |
| 源码 | <https://gitlab.com/kalilinux/packages/sparrow-wifi> |

### spire

Toolchain of APIs for establishing trust between software systems This package contains SPIRE (the SPIFFE Runtime Environment). It is a toolchain of APIs for establishing trust between software systems across a wide variety of hosting platforms. SPIRE exposes the SPIFFE Workload API, which can attest running software systems and issue SPIFFE IDs and SVIDs to them. This in turn allows two workloads to establish trust between each other,

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/spire/> |
| 版本 | 1.15.0 |
| 包 / 命令 | `spire`、`spire-agent`、`spire-server` |
| 安装 | `sudo apt install spire` |
| 占用空间 | 204.56 MB |
| 依赖 | `libc6`、`spire-agent` |
| 官网 | <https://github.com/spiffe/spire> |
| 源码 | <https://gitlab.com/kalilinux/packages/spire> |

### sploitscan

Search for CVE information SploitScan is an efficient and easy-to-use command-line tool designed to consult CVE (Common Vulnerabilities and Exposures). Extremely important for professionals, as it allows them to implement measures that prevent the exploitation of discovered vulnerabilities. Tool is capable of exporting in a single run results for JSON and CSV

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/sploitscan/> |
| 版本 | 0.14.3 |
| 包 / 命令 | `sploitscan` |
| 安装 | `sudo apt install sploitscan` |
| 占用空间 | 268 KB |
| 依赖 | `python3`、`python3-git`、`python3-jinja2`、`python3-openai`、`python3-requests`、`python3-tabulate`、`python3-tqdm`、`sploitscan` |
| 官网 | <https://github.com/xaitax/SploitScan> |
| 源码 | <https://salsa.debian.org/pkg-security-team/sploitscan> |

### spray

Password Spraying tool for Active Directory Credentials This package contains a Password Spraying tool for Active Directory Credentials. The script will password spray a target over a period of time. It requires password policy as input so accounts are not locked out. The package also provides a series of hand crafted password files for multiple languages. These have been crafted from the most common active

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/spray/> |
| 版本 | 2.1 |
| 包 / 命令 | `spray` |
| 安装 | `sudo apt install spray` |
| 占用空间 | 39.01 MB |
| 依赖 | `curl`、`smbclient`、`spray` |
| 官网 | <https://github.com/Greenwolf/Spray> |
| 源码 | <https://gitlab.com/kalilinux/packages/spray> |

### sprayhound

Password spraying tool and Bloodhound integration SprayHound is a Python library to safely password spray in Active Directory, which sets pwned users as owned in Bloodhound and detects paths to Domain Admins.

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/sprayhound/> |
| 版本 | 0.0~git20260614.4a31205 |
| 包 / 命令 | `sprayhound` |
| 安装 | `sudo apt install sprayhound` |
| 占用空间 | 69 KB |
| 依赖 | `python3`、`python3-ldap3`、`python3-neo4j`、`python3-pkg-resources`、`sprayhound` |
| 官网 | <https://github.com/Hackndo/sprayhound> |
| 源码 | <https://gitlab.com/kalilinux/packages/sprayhound> |

### sprayingtoolkit

Scripts to make password spraying attacks against Lync/S4B, OWA & O365 A set of Python scripts/utilities that tries to make password spraying attacks against Lync/S4B & OWA a lot quicker, less painful and more efficient.

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/sprayingtoolkit/> |
| 版本 | 0.0~git20201009.68f295d |
| 包 / 命令 | `sprayingtoolkit`、`atomizer`、`spindrift` |
| 安装 | `sudo apt install sprayingtoolkit` |
| 占用空间 | 79 KB |
| 依赖 | `kali-defaults`、`mitmproxy`、`python3`、`python3-boto3`、`python3-docopt`、`python3-imapclient`、`python3-lxml`、`python3-requests`、`python3-requests-ntlm`、`python3-termcolor`、`python3-urllib3`、`atomizer` |
| 官网 | <https://github.com/byt3bl33d3r/SprayingToolkit> |
| 源码 | <https://gitlab.com/kalilinux/packages/sprayingtoolkit> |

### spraykatz

Tool able to retrieve credentials on Windows machines This package contains a tool without any pretention able to retrieve credentials on Windows machines and large Active Directory environments. It simply tries to procdump machines and parse dumps remotely in order to avoid detections by antivirus software as much as possible.

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/spraykatz/> |
| 版本 | 0.9.9 |
| 包 / 命令 | `spraykatz` |
| 安装 | `sudo apt install spraykatz` |
| 占用空间 | 780 KB |
| 依赖 | `nmap`、`python3`、`python3-impacket`、`python3-lxml`、`python3-openssl`、`python3-pyasn1`、`python3-pycryptodome`、`python3-pypykatz`、`python3-wget`、`spraykatz` |
| 官网 | <https://github.com/aas-n/spraykatz> |
| 源码 | <https://gitlab.com/kalilinux/packages/spraykatz> |

### sqlmc

Check all urls of a domain for SQL injections SQLMC (SQL Injection Massive Checker) is a tool designed to scan a domain for SQL injection vulnerabilities. It crawls the given URL up to a specified depth, checks each link for SQL injection vulnerabilities, and reports its findings.

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/sqlmc/> |
| 版本 | 1.1.0 |
| 包 / 命令 | `sqlmc` |
| 安装 | `sudo apt install sqlmc` |
| 占用空间 | 65 KB |
| 依赖 | `figlet`、`python3`、`python3-aiohttp`、`python3-bs4`、`python3-pyfiglet`、`python3-tabulate`、`sqlmc` |
| 官网 | <https://github.com/malvads/sqlmc> |
| 源码 | <https://gitlab.com/kalilinux/packages/sqlmc> |

### sshuttle

Transparent proxy server for VPN over SSH Sshuttle makes it possible to access remote networks using SSH. It creates a transparent proxy server, using iptables, that will forward all the traffic through an SSH tunnel to a remote copy of sshuttle. It does not require installation on the remote server, which just needs to have Python installed.

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/sshuttle/> |
| 版本 | 1.3.2 |
| 包 / 命令 | `sshuttle` |
| 安装 | `sudo apt install sshuttle` |
| 占用空间 | 861 KB |
| 官网 | <https://github.com/sshuttle/sshuttle> |
| 源码 | <https://salsa.debian.org/debian/sshuttle> |

### sslstrip

SSL/TLS man-in-the-middle attack tool sslstrip is a tool that transparently hijacks HTTP traffic on a network, watch for HTTPS links and redirects, and then map those links into look-alike HTTP links or homograph-similar HTTPS links. It also supports modes for supplying a favicon which looks like a lock icon, selective logging, and session denial.

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/sslstrip/> |
| 版本 | 1.0 |
| 包 / 命令 | `sslstrip` |
| 安装 | `sudo apt install sslstrip` |
| 占用空间 | 60 KB |
| 依赖 | `python3`、`python3-twisted`、`sslstrip` |
| 官网 | <https://github.com/L1ghtn1ng/sslstrip> |
| 源码 | <https://gitlab.com/kalilinux/packages/sslstrip> |

### sstimap

Automatic SSTI detection tool with interactive interface SSTImap is a penetration testing software that can check websites for Code Injection and Server-Side Template Injection vulnerabilities and exploit them, giving access to the operating system itself.

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/sstimap/> |
| 版本 | 1.4 |
| 包 / 命令 | `sstimap` |
| 安装 | `sudo apt install sstimap` |
| 占用空间 | 454 KB |
| 依赖 | `python3`、`python3-html5lib`、`python3-mechanize`、`python3-requests`、`python3-urllib3`、`sstimap` |
| 官网 | <https://github.com/vladko312/SSTImap> |
| 源码 | <https://gitlab.com/kalilinux/packages/sstimap> |

### starkiller

Frontend for Powershell Empire This package contains a Frontend for Powershell Empire.

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/starkiller/> |
| 版本 | 3.5.0 |
| 包 / 命令 | `starkiller` |
| 安装 | `sudo apt install starkiller` |
| 占用空间 | 8.51 MB |
| 官网 | <https://github.com/BC-SECURITY/Starkiller> |
| 源码 | <https://gitlab.com/kalilinux/packages/starkiller> |

### stegcracker

Steganography brute-force tool StegCracker is steganography brute-force utility to uncover hidden data inside files.

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/stegcracker/> |
| 版本 | 2.1.0 |
| 包 / 命令 | `stegcracker` |
| 安装 | `sudo apt install stegcracker` |
| 占用空间 | 50 KB |
| 依赖 | `python3`、`steghide`、`stegcracker` |
| 官网 | <https://github.com/Paradoxis/StegCracker> |
| 源码 | <https://salsa.debian.org/pkg-security-team/stegcracker> |

### subfinder

Subdomain discovery tool This package contains a subdomain discovery tool that discovers valid subdomains for websites by using passive online sources. It has a simple modular architecture and is optimized for speed. subfinder is built for doing one thing only - passive subdomain enumeration, and it does that very well.

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/subfinder/> |
| 版本 | 2.16.0 |
| 包 / 命令 | `subfinder` |
| 安装 | `sudo apt install subfinder` |
| 占用空间 | 28.46 MB |
| 依赖 | `libc6`、`subfinder` |
| 官网 | <https://github.com/projectdiscovery/subfinder> |
| 源码 | <https://gitlab.com/kalilinux/packages/subfinder> |

### subjack

Subdomain Takeover tool This package contains a Subdomain Takeover tool written in Go designed to scan a list of subdomains concurrently and identify ones that are able to be hijacked. With Go’s speed and efficiency, this tool really stands out when it comes to mass-testing. Always double check the results manually to rule out false positives.

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/subjack/> |
| 版本 | 2.1 |
| 包 / 命令 | `subjack` |
| 安装 | `sudo apt install subjack` |
| 占用空间 | 10.73 MB |
| 依赖 | `libc6`、`subjack` |
| 官网 | <https://github.com/haccer/subjack> |
| 源码 | <https://gitlab.com/kalilinux/packages/subjack> |

### sublist3r

Fast subdomains enumeration tool for penetration testers This package contains a Python security tool designed to enumerate subdomains of websites using OSINT. It helps penetration testers and bug hunters collect and gather subdomains for the domain they are targeting over the network. Sublist3r enumerates subdomains using many search engines such as Google, Yahoo, Bing, Baidu, and Ask. Sublist3r also enumerates subdomains using

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/sublist3r/> |
| 版本 | 1.1 |
| 包 / 命令 | `sublist3r` |
| 安装 | `sudo apt install sublist3r` |
| 占用空间 | 1.85 MB |
| 依赖 | `python3` |
| 官网 | <https://github.com/aboul3la/Sublist3r> |
| 源码 | <https://salsa.debian.org/pkg-security-team/sublist3r> |

### syft

CLI tool for generating a SBOM from container images and filesystems This package contains a CLI tool and Go library for generating a Software Bill of Materials (SBOM) from container images and filesystems. Exceptional for vulnerability detection when used with a scanner like Grype. Generates SBOMs for container images, filesystems, archives, and more to discover packages and libraries

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/syft/> |
| 版本 | 1.51.0 |
| 包 / 命令 | `syft` |
| 安装 | `sudo apt install syft` |
| 占用空间 | 83.29 MB |
| 依赖 | `libc6`、`syft` |
| 官网 | <https://github.com/anchore/syft> |
| 源码 | <https://gitlab.com/kalilinux/packages/syft> |

### tailscale

Secure connectivity platform This package contains the tailscaled daemon and the tailscale CLI tool. The tailscaled daemon runs on Linux.

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/tailscale/> |
| 版本 | 1.94.1 |
| 包 / 命令 | `tailscale`、`tailscaled` |
| 安装 | `sudo apt install tailscale` |
| 占用空间 | 47.09 MB |
| 依赖 | `libc6`、`tailscale` |
| 官网 | <https://github.com/tailscale/tailscale> |
| 源码 | <https://gitlab.com/kalilinux/packages/tailscale> |

### teamsploit

Tools for group based penetration testing TeamSploit makes group-based penetration testing fun and easy, providing real-time collaboration and automation. TeamSploit is a suite of tools for the Metasploit Framework. TeamSploit should work with any MSF product (including OpenSource, Express, or Pro). Features include:

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/teamsploit/> |
| 版本 | 0~20151123 |
| 包 / 命令 | `teamsploit` |
| 安装 | `sudo apt install teamsploit` |
| 占用空间 | 2.26 MB |
| 依赖 | `gnome-terminal`、`metasploit-framework`、`ruby`、`teamsploit` |
| 官网 | <http://www.teamsploit.com> |
| 源码 | <https://gitlab.com/kalilinux/packages/teamsploit> |

### terraform

Tool for building, changing, and versioning infrastructure This package contains a tool for building, changing, and versioning infrastructure safely and efficiently. Terraform can manage existing and popular service providers as well as custom in-house solutions. Terraform enables you to safely and predictably create, change, and improve infrastructure. It is an open source tool that codifies APIs into declarative

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/terraform/> |
| 版本 | 1.6.3 |
| 包 / 命令 | `terraform` |
| 安装 | `sudo apt install terraform` |
| 占用空间 | 77.16 MB |
| 依赖 | `libc6`、`terraform` |
| 官网 | <https://github.com/hashicorp/terraform> |
| 源码 | <https://gitlab.com/kalilinux/packages/terraform> |

### testdisk

Partition scanner and disk recovery tool TestDisk checks the partition and boot sectors of your disks. It is very useful in forensics, recovering lost partitions. It works with : DOS/Windows FAT12, FAT16 and FAT32 NTFS ( Windows NT/2K/XP )

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/testdisk/> |
| 版本 | 7.2 |
| 包 / 命令 | `photorec`、`fidentify`、`qphotorec`、`testdisk` |
| 安装 | `sudo apt install testdisk` |
| 占用空间 | 528 KB |
| 依赖 | `libc6`、`libext2fs2t64`、`libncursesw6`、`libntfs-3g90`、`libtinfo6`、`ntfs-3g`、`testdisk` |
| 官网 | <https://www.cgsecurity.org/> |
| 源码 | <https://salsa.debian.org/pkg-security-team/testdisk> |

### testssl.sh

Command line tool to check TLS/SSL ciphers, protocols and cryptographic flaws testssl.sh is a free command line tool which checks a server’s service on any port for the support of TLS/SSL ciphers, protocols as well as recent cryptographic flaws and more. Key features Clear output: you can tell easily whether anything is good or bad

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/testssl.sh/> |
| 版本 | 3.2.4 |
| 包 / 命令 | `testssl.sh`、`testssl` |
| 安装 | `sudo apt install testssl.sh` |
| 占用空间 | 3.56 MB |
| 依赖 | `bind9-dnsutils`、`bsdextrautils`、`openssl`、`procps`、`testssl` |
| 官网 | <https://testssl.sh/> |
| 源码 | <https://salsa.debian.org/pkg-security-team/testssl.sh> |

### tetragon

EBPF-based Security Observability and Runtime Enforcement (tetra CLI) Cilium’s new Tetragon component enables powerful realtime, eBPF-based Security Observability and Runtime Enforcement. Tetragon detects and is able to react to security-significant events, such as: - Process execution events - System call activity

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/tetragon/> |
| 版本 | 1.7.0 |
| 包 / 命令 | `tetragon`、`tetra` |
| 安装 | `sudo apt install tetragon` |
| 占用空间 | 50.70 MB |
| 依赖 | `bpftool`、`libc6`、`tetra` |
| 官网 | <https://github.com/cilium/tetragon> |
| 源码 | <https://gitlab.com/kalilinux/packages/tetragon> |

### tftp-hpa

HPA’s tftp client Trivial File Transfer Protocol (TFTP) is a file transfer protocol, mainly to serve boot images over the network to other machines (PXE). tftp-hpa is an enhanced version of the BSD TFTP client and server. It possesses a number of bugfixes and enhancements over the original. This package contains the client.

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/tftp-hpa/> |
| 版本 | 5.4 |
| 包 / 命令 | `tftp-hpa`、`tftp`、`tftpd-hpa`、`in.tftpd` |
| 安装 | `sudo apt install tftp-hpa` |
| 占用空间 | 58 KB |
| 依赖 | `libc6`、`tftp` |
| 官网 | <https://git.kernel.org/pub/scm/network/tftp/tftp-hpa.git/> |
| 源码 | <https://salsa.debian.org/debian/tftp-hpa> |

### tightvnc

Virtual network computing password tool VNC stands for Virtual Network Computing. It is, in essence, a remote display system which allows you to view a computing `desktop’ environment not only on the machine where it is running, but from anywhere on the Internet and from a wide variety of machine architectures. This package provides the vncpasswd tool mandatory for the tightvncserver

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/tightvnc/> |
| 版本 | 1.3.10 |
| 包 / 命令 | `tightvncpasswd`、`tightvncserver` |
| 安装 | `sudo apt install tightvncpasswd` |
| 占用空间 | 67 KB |
| 依赖 | `libc6`、`tightvncpasswd` |
| 官网 | <https://www.tightvnc.com> |
| 源码 | <https://salsa.debian.org/debian-remote-team/tightvnc> |

### tinja

CLI tool for testing web pages for template injection TInjA is a CLI tool for testing web pages for template injection vulnerabilities and supports 44 of the most relevant template engines for eight different programming languages.

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/tinja/> |
| 版本 | 1.2.0 |
| 包 / 命令 | `tinja` |
| 安装 | `sudo apt install tinja` |
| 占用空间 | 12.62 MB |
| 依赖 | `libc6`、`tinja` |
| 官网 | <https://github.com/Hackmanit/TInjA> |
| 源码 | <https://gitlab.com/kalilinux/packages/tinja> |

### tnftp

tnftp Enhanced ftp client tnftp is what many users affectionately call the enhanced ftp client in NetBSD ( http://www.netbsd.org ).

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/tnftp/> |
| 版本 | 20260211 |
| 包 / 命令 | `ftp`、`tnftp` |
| 安装 | `sudo apt install tnftp` |
| 占用空间 | 259 KB |
| 依赖 | `libc6`、`libedit2`、`libssl3t64`、`tnftp` |
| 官网 | <https://en.wikipedia.org/wiki/Tnftp> |
| 源码 | <https://salsa.debian.org/debian/tnftp> |

### tookie-osint

OSINT information gathering tool for finding social media accounts Tookie-osint has a simple-to-use UI and is really straightforward. The main idea of Tookie-osint is to discover usernames that are requested from an input. Tookie-osint is similar to the tool called Sherlock. It discovers all the user accounts across different websites and Tookie-osint is successful at this task almost 80% of the time.

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/tookie-osint/> |
| 版本 | 4.1fix |
| 包 / 命令 | `tookie-osint` |
| 安装 | `sudo apt install tookie-osint` |
| 占用空间 | 1.12 MB |
| 依赖 | `chromium-driver`、`python3`、`python3-colorama`、`python3-requests`、`python3-selenium`、`python3-webdriver-manager`、`tookie-osint` |
| 官网 | <https://github.com/Alfredredbird/tookie-osint> |
| 源码 | <https://gitlab.com/kalilinux/packages/tookie-osint> |

### traceroute

Traces the route taken by packets over an IPv4/IPv6 network The traceroute utility displays the route used by IP packets on their way to a specified network (or Internet) host. Traceroute displays the IP number and host name (if possible) of the machines along the route taken by the packets. Traceroute is used as a network debugging tool. If you’re having network connectivity problems, traceroute will show you where the trouble is coming

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/traceroute/> |
| 版本 | 2.1.6 |
| 包 / 命令 | `traceroute`、`lft.db`、`tcptraceroute.db`、`traceproto.db`、`traceroute-nanog`、`traceroute.db`、`traceroute6.db` |
| 安装 | `sudo apt install traceroute` |
| 占用空间 | 160 KB |
| 依赖 | `libc6`、`lft.db` |
| 官网 | <https://traceroute.sourceforge.net/> |

### trivy

Comprehensive and versatile security scanner This package contains a comprehensive and versatile security scanner. Trivy has scanners that look for security issues, and targets where it can find those issues. It can find vulnerabilities, misconfigurations, secrets, SBOM in containers, Kubernetes, code repositories, clouds and more.

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/trivy/> |
| 版本 | 0.66.0 |
| 包 / 命令 | `trivy` |
| 安装 | `sudo apt install trivy` |
| 占用空间 | 229.39 MB |
| 依赖 | `libc6`、`trivy` |
| 官网 | <https://github.com/aquasecurity/trivy> |
| 源码 | <https://gitlab.com/kalilinux/packages/trivy> |

### trufflehog

Searches through git repositories for secrets This package contains a utitlity to search through git repositories for secrets, digging deep into commit history and branches. This is effective at finding secrets accidentally committed.

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/trufflehog/> |
| 版本 | 3.94.3 |
| 包 / 命令 | `trufflehog` |
| 安装 | `sudo apt install trufflehog` |
| 占用空间 | 118.50 MB |
| 依赖 | `libc6`、`trufflehog` |
| 官网 | <https://github.com/trufflesecurity/truffleHog> |
| 源码 | <https://gitlab.com/kalilinux/packages/trufflehog> |

### tundeep

Layer 2 VPN/injection tool The tool resides [almost] entirely in user space on the victim aside from the pcap requirement.

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/tundeep/> |
| 版本 | 1.1~git20190802 |
| 包 / 命令 | `tundeep` |
| 安装 | `sudo apt install tundeep` |
| 占用空间 | 49 KB |
| 依赖 | `libc6`、`libpcap0.8t64`、`zlib1g`、`tundeep` |
| 官网 | <https://www.adampalmer.me/iodigitalsec/tundeep/> |
| 源码 | <https://gitlab.com/kalilinux/packages/tundeep> |

### unblob

Accurate, fast, and easy-to-use extraction suite (Python 3) This package contains an accurate, fast, and easy-to-use extraction suite. It parses unknown binary blobs for more than 30 different archive, compression, and file-system formats, extracts their content recursively, and carves out unknown chunks that have not been accounted for. This package installs the library for Python 3.

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/unblob/> |
| 版本 | 26.6.4 |
| 包 / 命令 | `unblob` |
| 安装 | `sudo apt install unblob` |
| 占用空间 | 1.20 MB |
| 依赖 | `libc6`、`libgcc-s1`、`python3`、`python3-arpy`、`python3-attr`、`python3-click`、`python3-cryptography`、`python3-dissect.cstruct`、`python3-jefferson`、`python3-lark`、`python3-lief`、`python3-lz4` 等 |
| 官网 | <https://unblob.org/> |
| 源码 | <https://gitlab.com/kalilinux/packages/unblob> |

### unhide.rb

Forensics tool to find processes hidden by rootkits Unhide.rb is a forensics tool to find processes hidden by rootkits. It looks for active processes in many different ways. Processes found by some means but not others are considered to be “hidden”, and are reported to the user. Unhide.rb is a tentative of rewrite in Ruby of the original Unhide, which

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/unhide.rb/> |
| 版本 | 22 |
| 包 / 命令 | `unhide.rb` |
| 安装 | `sudo apt install unhide.rb` |
| 占用空间 | 31 KB |
| 依赖 | `procps`、`ruby`、`unhide.rb` |
| 官网 | <https://launchpad.net/unhide.rb> |
| 源码 | <https://salsa.debian.org/pkg-security-team/unhide.rb> |

### uro

Declutter URLs for crawling/pentesting Uro declutters a list of URLs by removing Incremental URLs, Blog posts and other similar human-written content, URLs with the same path but parameter value differences, Images, JS, CSS, and other “useless” files.

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/uro/> |
| 版本 | 1.0.2 |
| 包 / 命令 | `uro` |
| 安装 | `sudo apt install uro` |
| 占用空间 | 38 KB |
| 依赖 | `python3`、`uro` |
| 官网 | <https://github.com/s0md3v/uro> |
| 源码 | <https://gitlab.com/kalilinux/packages/uro> |

### vboot-utils

Chrome OS verified u-boot utilities This package contains a set of tools to deal with Chromebook internals, and the verified version of u-boot. Namely: bmpblk_font bmpblk_utility chromeos-tpm-recovery crossystem dev_debug_vboot dev_make_keypair dumpRSAPublicKey eficompress efidecompress enable_dev_usb_boot load_kernel_test pad_digest_utility signature_digest_utility tpm-nvsize

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/vboot-utils/> |
| 版本 | 0~R106 |
| 包 / 命令 | `cgpt`、`vboot-kernel-utils`、`futility`、`vbutil_kernel`、`vboot-utils`、`chromeos-tpm-recovery`、`crossystem`、`dev_debug_vboot` |
| 安装 | `sudo apt install vboot-utils` |
| 占用空间 | 281 KB |
| 依赖 | `flashrom`、`libc6`、`libssl3t64`、`vboot-kernel-utils`、`chromeos-tpm-recovery` |
| 官网 | <https://chromium.googlesource.com/chromiumos/platform/vboot_reference> |
| 源码 | <https://salsa.debian.org/debian/vboot-utils> |

### villain

High level C2 framework Villain is a C2 framework that can handle multiple TCP socket & HoaxShell-based reverse shells, enhance their functionality with additional features and share them among connected sibling servers.

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/villain/> |
| 版本 | 2.2.1 |
| 包 / 命令 | `villain` |
| 安装 | `sudo apt install villain` |
| 占用空间 | 326 KB |
| 依赖 | `python3`、`python3-netifaces`、`python3-pycryptodome`、`python3-pyperclip`、`python3-requests`、`villain` |
| 官网 | <https://github.com/t3l3machus/Villain> |
| 源码 | <https://gitlab.com/kalilinux/packages/villain> |

### vim

Vi IMproved - enhanced vi editor Vim is an almost compatible version of the UNIX editor Vi. Many new features have been added: multi level undo, syntax highlighting, command line history, on-line help, filename completion, block operations, folding, Unicode support, etc. This package contains a version of vim compiled with a rather

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/vim/> |
| 版本 | 9.2.0858 |
| 包 / 命令 | `vim`、`vim.basic`、`vim-common`、`helpztags`、`vim-doc`、`vim-gtk3`、`vim.gtk3`、`vim-gui-common`、`gvimtutor`、`vim-motif`、`vim.motif`、`vim-nox`、`vim.nox`、`vim-runtime`、`vimtutor`、`vim-tiny`、`vim.tiny`、`xxd` |
| 安装 | `sudo apt install vim` |
| 占用空间 | 4.06 MB |
| 依赖 | `libacl1`、`libc6`、`libgpm2`、`libselinux1`、`libsodium26`、`libtinfo6`、`vim-common`、`vim-runtime`、`vim.basic` |
| 官网 | <https://www.vim.org/> |
| 源码 | <https://salsa.debian.org/vim-team/vim> |

### vlan

Ifupdown legacy integration for vlan configuration This package contains legacy integration scripts for configuring vlan interfaces via ifupdown (/etc/network/interfaces). For further details see vlan-interfaces(5) man page in this package. Please note that this package is not necessary for most VLAN use cases with ifupdown. You only need to install it if you need to support

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/vlan/> |
| 版本 | 2.0.5 |
| 包 / 命令 | `vlan`、`vconfig` |
| 安装 | `sudo apt install vlan` |
| 占用空间 | 37 KB |
| 依赖 | `iproute2`、`vconfig` |
| 源码 | <https://salsa.debian.org/debian/vlan> |

### vopono

Run applications through VPN tunnels with temporary network namespaces vopono is a tool to run applications through VPN tunnels via temporary network namespaces. This allows you to run only a handful of applications through different VPNs simultaneously, whilst keeping your main connection as normal.

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/vopono/> |
| 版本 | 1.0.1 |
| 包 / 命令 | `vopono` |
| 安装 | `sudo apt install vopono` |
| 占用空间 | 14.74 MB |
| 依赖 | `libc6`、`libgcc-s1`、`nftables`、`vopono` |
| 官网 | <https://github.com/jamesmcm/vopono> |
| 源码 | <https://gitlab.com/kalilinux/packages/vopono> |

### vpnc

Cisco-compatible VPN client vpnc is a VPN client compatible with cisco3000 VPN Concentrator (also known as Cisco’s EasyVPN equipment). vpnc runs entirely in userspace and does not require kernel modules except for the tun driver to communicate with the network layer. It supports most of the features needed to establish connection to the

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/vpnc/> |
| 版本 | 0.5.3 |
| 包 / 命令 | `vpnc`、`cisco-decrypt`、`pcf2vpnc`、`vpnc-connect`、`vpnc-disconnect` |
| 安装 | `sudo apt install vpnc` |
| 占用空间 | 238 KB |
| 依赖 | `libc6`、`libgcrypt20`、`libgnutls30t64`、`perl`、`vpnc-scripts`、`cisco-decrypt` |
| 官网 | <https://github.com/streambinder/vpnc> |
| 源码 | <https://salsa.debian.org/pkg-security-team/vpnc> |

### vwifi-dkms

Simple Virtual Wireless Driver for Linux in DKMS format This package contains a minimal interface to provide essential functionalities, such as scanning for dummy Wi-Fi networks, establishing connections, and disconnecting from them. It is built upon the cfg80211 subsystem, which collaborates with FullMAC drivers. Currently, vwifi supports both Station Mode and Host AP Mode and is

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/vwifi-dkms/> |
| 版本 | 0.0~git20260407.11569dd |
| 包 / 命令 | `vwifi-dkms`、`vwifi-tool` |
| 安装 | `sudo apt install vwifi-dkms` |
| 占用空间 | 822 KB |
| 依赖 | `dkms`、`iw`、`vwifi-tool` |
| 官网 | <https://github.com/sysprog21/vwifi> |
| 源码 | <https://gitlab.com/kalilinux/packages/vwifi-dkms> |

### waybackpy

Access Wayback Machine’s API using Python waybackpy is a Python package and a CLI tool that interfaces with the Wayback Machine’s APIs. Internet Archive’s Wayback Machine has 3 useful public APIs. SavePageNow API (also known as Save API) CDX Server API

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/waybackpy/> |
| 版本 | 3.0.6 |
| 包 / 命令 | `waybackpy` |
| 安装 | `sudo apt install waybackpy` |
| 占用空间 | 96 KB |
| 依赖 | `python3`、`python3-click`、`python3-requests`、`python3-urllib3`、`waybackpy` |
| 官网 | <https://github.com/akamhy/waybackpy> |
| 源码 | <https://gitlab.com/kalilinux/packages/waybackpy> |

### web-cache-vulnerability-scanner

Go-based CLI tool for testing for web cache poisoning Web Cache Vulnerability Scanner (WCVS) is a fast and versatile CLI scanner for web cache poisoning and web cache deception developed by Hackmanit and Maximilian Hildebrand. The scanner supports many different web cache poisoning and web cache deception techniques, includes a crawler to identify further URLs to test, and

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/web-cache-vulnerability-scanner/> |
| 版本 | 2.0.0 |
| 包 / 命令 | `web-cache-vulnerability-scanner`、`wcvs` |
| 安装 | `sudo apt install web-cache-vulnerability-scanner` |
| 占用空间 | 6.27 MB |
| 依赖 | `libc6`、`wcvs` |
| 官网 | <https://github.com/Hackmanit/Web-Cache-Vulnerability-Scanner> |
| 源码 | <https://gitlab.com/kalilinux/packages/web-cache-vulnerability-scanner> |

### websploit

Web exploitation framework WebSploit is an open source project which is used to scan and analysis remote system in order to find various type of vulnerabilites. This tool is very powerful and supports multiple vulnerabilities.

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/websploit/> |
| 版本 | 4.0.4 |
| 包 / 命令 | `websploit` |
| 安装 | `sudo apt install websploit` |
| 占用空间 | 76 KB |
| 依赖 | `python3`、`python3-requests`、`python3-scapy`、`websploit` |
| 官网 | <https://sourceforge.net/projects/websploit/> |
| 源码 | <https://salsa.debian.org/pkg-security-team/websploit> |

### wgetpaste

Command-line interface to various online pastebin services This package contains a script that automates pasting to a number of pastebin services.

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/wgetpaste/> |
| 版本 | 2.30 |
| 包 / 命令 | `wgetpaste` |
| 安装 | `sudo apt install wgetpaste` |
| 占用空间 | 49 KB |
| 依赖 | `wget`、`wgetpaste` |
| 官网 | <http://wgetpaste.zlin.dk/> |
| 源码 | <https://gitlab.com/kalilinux/packages/wgetpaste> |

### what-is-python

Symlinks /usr/bin/python-config to python3-config Starting with the Debian 11 (bullseye) and Ubuntu 20.04 LTS (focal) releases, all python packages use explicit python3 or python2 interpreter and do not use unversioned /usr/bin/python-config at all. Some third-party code is now predominantly python3 based, yet may use /usr/bin/python-config.

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/what-is-python/> |
| 版本 | 15 |
| 包 / 命令 | `python-dev-is-python3`、`pdb`、`python-config`、`python-is-python3`、`pydoc`、`python` |
| 安装 | `sudo apt install python-dev-is-python3` |
| 占用空间 | 13 KB |
| 依赖 | `python-is-python3`、`python3-dev`、`pdb` |

### whatmask

Helper for network settings This package contains a small C program that will help you with network settings. Whatmask can work in two modes. The first mode is to invoke Whatmask with only a subnet mask as the argument. In this mode Whatmask will echo back the subnet mask in four formats, plus the

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/whatmask/> |
| 版本 | 1.2 |
| 包 / 命令 | `whatmask` |
| 安装 | `sudo apt install whatmask` |
| 占用空间 | 40 KB |
| 依赖 | `libc6`、`whatmask` |
| 官网 | <http://www.laffeycomputer.com/whatmask.html> |
| 源码 | <https://gitlab.com/kalilinux/packages/whatmask> |

### wifiphisher

Automated phishing attacks against Wi-Fi networks This package contains a security tool that mounts automated phishing attacks against Wi-Fi networks in order to obtain secret passphrases or other credentials. It is a social engineering attack that unlike other methods it does not include any brute forcing. It is an easy way for obtaining credentials from captive portals and third party login pages or WPA/WPA2 secret

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/wifiphisher/> |
| 版本 | 1.4 |
| 包 / 命令 | `wifiphisher` |
| 安装 | `sudo apt install wifiphisher` |
| 占用空间 | 7.89 MB |
| 依赖 | `cowpatty`、`dnsmasq-base`、`hostapd`、`iptables`、`net-tools`、`python3`、`python3-pbkdf2`、`python3-pyric`、`python3-roguehostapd`、`python3-scapy`、`python3-six`、`python3-tornado` 等 |
| 官网 | <https://github.com/sophron/wifiphisher> |
| 源码 | <https://gitlab.com/kalilinux/packages/wifiphisher> |

### wifipumpkin3

Powerful framework for rogue access point attack This package contains a powerful framework for rogue access point attack, written in Python, that allow and offer to security researchers, red teamers and reverse engineers to mount a wireless network to conduct a man-in-the-middle attack.

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/wifipumpkin3/> |
| 版本 | 1.1.7 |
| 包 / 命令 | `wifipumpkin3`、`captiveflask`、`evilqr3`、`phishkin3`、`sslstrip3`、`wp3` |
| 安装 | `sudo apt install wifipumpkin3` |
| 占用空间 | 29.24 MB |
| 依赖 | `hostapd`、`iptables`、`iw`、`net-tools`、`python3`、`python3-aiofiles`、`python3-bs4`、`python3-dhcplib`、`python3-dnslib`、`python3-dnspython`、`python3-flask`、`python3-flask-restful` 等 |
| 官网 | <https://github.com/P0cL4bs/wifipumpkin3> |
| 源码 | <https://gitlab.com/kalilinux/packages/wifipumpkin3> |

### wig

WebApp Information Gatherer This package contains a web application information gathering tool, which can identify numerous Content Management Systems and other administrative applications. The application fingerprinting is based on checksums and string matching of known files for different versions of CMSes. This results in a score being

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/wig/> |
| 版本 | 0.6 |
| 包 / 命令 | `wig` |
| 安装 | `sudo apt install wig` |
| 占用空间 | 6.36 MB |
| 依赖 | `python3`、`wig` |
| 官网 | <https://github.com/jekyc/wig> |
| 源码 | <https://salsa.debian.org/pkg-security-team/wig> |

### wig-ng

Utility for Wi-Fi device fingerprinting This package contains WIG (Wi-Fi Information Gathering), a utility for Wi-Fi device fingerprinting. Supported protocols and standards: Apple Wireless Direct Link (AWDL) Cisco Client Extension (CCX)

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/wig-ng/> |
| 版本 | 0.1 |
| 包 / 命令 | `wig-ng`、`wig-ng.py` |
| 安装 | `sudo apt install wig-ng` |
| 占用空间 | 334 KB |
| 依赖 | `python3`、`python3-impacket`、`python3-pcapy`、`python3-setproctitle`、`wig-ng` |
| 官网 | <https://github.com/6e726d/wig-ng> |
| 源码 | <https://gitlab.com/kalilinux/packages/wig-ng> |

### wmi

DCOM/WMI client implementation This DCOM/WMI client implementation is based on Samba4 sources. It uses RPC/DCOM mechanisms to interact with WMI services on Windows 2000/XP/2003 machines. This package contains the command line client to perform remote command execution on Windows systems.

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/wmi/> |
| 版本 | 1.3.16 |
| 包 / 命令 | `wmi-client`、`wmic`、`wmis` |
| 安装 | `sudo apt install wmi-client` |
| 占用空间 | 9.12 MB |
| 依赖 | `libc6`、`libcrypt1`、`wmic` |
| 源码 | <https://gitlab.com/kalilinux/packages/wmi> |

### wordlistraider

Tool to prepare existing wordlists This package contains a Python tool for preparing existing wordlists. It returns a selection of words that matches the passed conditions in an existing list. As an example you have a GB big wordlist and you only want passwords with a length of at least 8 characters. This optimizes word lists and saves

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/wordlistraider/> |
| 版本 | 1.0~git20200927 |
| 包 / 命令 | `wordlistraider` |
| 安装 | `sudo apt install wordlistraider` |
| 占用空间 | 30 KB |
| 依赖 | `figlet`、`python3`、`python3-colorama`、`python3-more-termcolor`、`python3-pyfiglet`、`wordlistraider` |
| 官网 | <https://github.com/GregorBiswanger/WordlistRaider> |
| 源码 | <https://gitlab.com/kalilinux/packages/wordlistraider> |

### wotmate

Reimplement the defunct PGP pathfinder with only your own keyring This package contains a reimplementation the defunct PGP pathfinder without needing anything other than your own keyring. Currently, the following tools are available: graph-paths.py: Draws the shortest path between each key you have personally signed and the target key. For simpler setups, it exactly

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/wotmate/> |
| 版本 | 0.1 |
| 包 / 命令 | `wotmate` |
| 安装 | `sudo apt install wotmate` |
| 占用空间 | 201 KB |
| 依赖 | `kali-defaults`、`python3`、`python3-pydotplus`、`wotmate` |
| 官网 | <https://github.com/mricon/wotmate> |
| 源码 | <https://gitlab.com/kalilinux/packages/wotmate> |

### wpa-sycophant

Tool to relay phase 2 authentication attempts to access corporate wireless This package contains a tool to relay phase 2 authentication attempts to access corporate wireless without cracking the password. To use this technique it is required that you run a rogue access point so that a legitimate user will connect to you so that you may relay the authentication attempt to Sycophant.

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/wpa-sycophant/> |
| 版本 | 1.0 |
| 包 / 命令 | `wpa-sycophant`、`wpa_sycophant` |
| 安装 | `sudo apt install wpa-sycophant` |
| 占用空间 | 867 KB |
| 依赖 | `libc6`、`libnl-3-200`、`libnl-genl-3-200`、`libssl3t64`、`wpa_sycophant` |
| 官网 | <https://github.com/sensepost/wpa_sycophant> |
| 源码 | <https://gitlab.com/kalilinux/packages/wpa-sycophant> |

### wpprobe

Fast WordPress plugin enumeration tool A fast WordPress plugin scanner that detects installed plugins via REST API enumeration and maps them to known vulnerabilities. Over 3000 plugins detectable without brute-force, thousands more with it.

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/wpprobe/> |
| 版本 | 0.12.11 |
| 包 / 命令 | `wpprobe` |
| 安装 | `sudo apt install wpprobe` |
| 占用空间 | 14.43 MB |
| 依赖 | `libc6`、`wpprobe` |
| 官网 | <https://github.com/Chocapikk/wpprobe> |
| 源码 | <https://gitlab.com/kalilinux/packages/wpprobe> |

### wsgidav

root@kali:~# wsgidav -h usage: wsgidav [-h] [-p PORT] [-H HOST] [-r ROOT_PATH] [--auth {anonymous,nt,pam-login}] [--server {cheroot,ext-wsgiutils,gevent,gunicorn,paste,uvicorn,wsgiref}] [--ssl-adapter {builtin,pyopenssl}] [-v | -q] [-c CONFIG_FILE | --no-config] [--browse] [-V]

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/wsgidav/> |
| 版本 | 4.3.5 |
| 包 / 命令 | `python-wsgidav-doc`、`python3-wsgidav`、`wsgidav` |
| 安装 | `sudo apt install wsgidav` |
| 官网 | <https://github.com/mar10/wsgidav> |
| 源码 | <https://gitlab.com/kalilinux/packages/wsgidav> |

### xclip

Command line interface to X selections xclip is a command line utility that is designed to run on any system with an X11 implementation. It provides an interface to X selections (“the clipboard”) from the command line. It can read data from standard in or a file and place it in an X selection for pasting into other X applications. xclip can also print an X selection to standard out, which can then be redirected to a file

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/xclip/> |
| 版本 | 0.13 |
| 包 / 命令 | `xclip`、`xclip-copyfile`、`xclip-cutfile`、`xclip-pastefile` |
| 安装 | `sudo apt install xclip` |
| 占用空间 | 62 KB |
| 依赖 | `libc6`、`libx11-6`、`libxmu6`、`xclip` |
| 官网 | <https://github.com/astrand/xclip> |
| 源码 | <https://salsa.debian.org/debian/xclip> |

### xspy

X server sniffer Sniffs keystrokes on remote or local X-Windows servers.

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/xspy/> |
| 版本 | 1.1 |
| 包 / 命令 | `xspy` |
| 安装 | `sudo apt install xspy` |
| 占用空间 | 25 KB |
| 依赖 | `libc6`、`libx11-6`、`xspy` |
| 官网 | <https://www.kali.org> |
| 源码 | <https://gitlab.com/kalilinux/packages/xspy> |

### xsrfprobe

Prime Cross Site Request Forgery Audit and Exploitation Toolkit XSRFProbe is an advanced Cross Site Request Forgery (CSRF/XSRF) Audit and Exploitation Toolkit. Equipped with a powerful crawling engine and numerous systematic checks, it is able to detect most cases of CSRF vulnerabilities, their related bypasses and further generate (maliciously) exploitable proof of concepts with each found vulnerability.

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/xsrfprobe/> |
| 版本 | 3.0.0 |
| 包 / 命令 | `xsrfprobe` |
| 安装 | `sudo apt install xsrfprobe` |
| 占用空间 | 271 KB |
| 依赖 | `python3`、`python3-bs4`、`python3-pydantic`、`python3-rapidfuzz`、`python3-requests`、`python3-selenium`、`xsrfprobe` |
| 官网 | <https://github.com/0xInfection/XSRFProbe> |
| 源码 | <https://gitlab.com/kalilinux/packages/xsrfprobe> |

### xsstrike

Most advanced XSS scanner XSStrike is a Cross Site Scripting detection suite equipped with four hand written parsers, an intelligent payload generator, a powerful fuzzing engine and an incredibly fast crawler.

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/xsstrike/> |
| 版本 | 3.1.6 |
| 包 / 命令 | `xsstrike` |
| 安装 | `sudo apt install xsstrike` |
| 占用空间 | 179 KB |
| 依赖 | `python3`、`python3-fuzzywuzzy`、`python3-requests`、`python3-tld`、`xsstrike` |
| 官网 | <https://github.com/s0md3v/XSStrike> |
| 源码 | <https://gitlab.com/kalilinux/packages/xsstrike> |

### zerofree

Zero free blocks from ext2, ext3 and ext4 file-systems Zerofree finds the unallocated blocks with non-zero value content in an ext2, ext3 or ext4 file-system and fills them with zeroes (zerofree can also work with another value than zero). This is mostly useful if the device on which this file-system resides is a disk image. In this case, depending on the type of disk image, a secondary

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/zerofree/> |
| 版本 | 1.1.1 |
| 包 / 命令 | `zerofree` |
| 安装 | `sudo apt install zerofree` |
| 占用空间 | 30 KB |
| 依赖 | `libc6`、`libext2fs2t64`、`zerofree` |
| 官网 | <https://frippery.org/uml/> |
| 源码 | <https://salsa.debian.org/debian/zerofree> |

### zim

Graphical text editor based on wiki technologies Zim is a graphical text editor used to maintain a collection of wiki pages. Each page can contain links to other pages, simple formatting and inline images. Pages are stored in a folder structure, like in an outliner, and can have attachments. Creating a new page is as easy as linking to a nonexistent page.

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/zim/> |
| 版本 | 0.76.3 |
| 包 / 命令 | `zim` |
| 安装 | `sudo apt install zim` |
| 占用空间 | 5.22 MB |
| 依赖 | `gir1.2-gtk-3.0`、`python3`、`python3-gi`、`python3-xdg`、`xdg-utils`、`zim` |
| 官网 | <https://zim-wiki.org> |
| 源码 | <https://salsa.debian.org/debian/zim> |

### zonedb

Public Zone Database (program) This package provides a free, open-source database ( http://opendatacommons.org/licenses/odbl/1.0/ ) containing a list and associated metadata of public DNS zones

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/zonedb/> |
| 版本 | 1.0.3170 |
| 包 / 命令 | `golang-github-zonedb-zonedb-dev`、`zonedb` |
| 安装 | `sudo apt install zonedb` |
| 占用空间 | 14.86 MB |
| 依赖 | `libc6`、`zonedb` |
| 官网 | <https://github.com/zonedb/zonedb> |
| 源码 | <https://gitlab.com/kalilinux/packages/zonedb> |

### zsh-autosuggestions

Fish-like fast/unobtrusive autosuggestions for zsh As you type commands, you will see a completion offered after the cursor in a muted gray color. If you press the right-arrow key or End with the cursor at the end of the buffer, it will accept the suggestion, replacing the contents of the command line buffer with the suggestion. If you invoke the forward-word widget, it will partially accept the suggestion up to the

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/zsh-autosuggestions/> |
| 版本 | 0.7.1 |
| 包 / 命令 | `zsh-autosuggestions` |
| 安装 | `sudo apt install zsh-autosuggestions` |
| 占用空间 | 46 KB |
| 依赖 | `zsh` |
| 官网 | <https://github.com/zsh-users/zsh-autosuggestions> |
| 源码 | <https://salsa.debian.org/debian/zsh-autosuggestions> |

### zsh-syntax-highlighting

Fish shell like syntax highlighting for zsh This package provides syntax highlighting for the shell zsh. It enables highlighting of commands whilst they are typed at a zsh prompt into an interactive terminal. This helps in reviewing commands before running them, particularly in catching syntax errors. This feature is inspired by the Fish shell, which provides it by default.

| 项目 | 内容 |
|------|------|
| 归入分组 | 通用工具 |
| Kali 文档 | <https://www.kali.org/tools/zsh-syntax-highlighting/> |
| 版本 | 0.8.0 |
| 包 / 命令 | `zsh-syntax-highlighting` |
| 安装 | `sudo apt install zsh-syntax-highlighting` |
| 占用空间 | 168 KB |
| 依赖 | `zsh` |
| 官网 | <https://github.com/zsh-users/zsh-syntax-highlighting/> |
| 源码 | <https://salsa.debian.org/debian/zsh-syntax-highlighting> |
