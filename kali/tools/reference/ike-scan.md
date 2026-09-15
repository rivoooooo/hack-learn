# ike-scan

> Discover and fingerprint IKE hosts (IPsec VPN Servers) ike-scan discovers IKE hosts and can also fingerprint them using the retransmission backoff pattern. ike-scan does two things: a) Discovery: Determine which hosts are running IKE. This…

> **功能分类**：信息搜集 ｜ **Kali 包**：`ike-scan` ｜ **官方文档**：<https://www.kali.org/tools/ike-scan/>

## 1. 安装

```bash
sudo apt update
sudo apt install ike-scan
```

| 项目 | 内容 |
|------|------|
| 版本 | 1.9.5 |
| 架构 | any |
| 可执行命令 | `ike-scan`、`psk-crack` |
| 依赖 | `libc6`、`libssl3t64` |
| 安装体积 | 4.17 MB |
| 官网 | <https://github.com/royhills/ike-scan> |
| 源码仓库 | <https://salsa.debian.org/pkg-security-team/ike-scan> |
| 包追踪 | <https://pkg.kali.org/pkg/ike-scan> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
ike-scan -h          # 查看用法
man ike-scan         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 2 个可执行命令，下面是官方页面内嵌的帮助原文。

### `ike-scan`

> 官方示例调用：`ike-scan -h`

```text
root@kali:~# ike-scan -h
Usage: ike-scan [options] [hosts...]
Target hosts must be specified on the command line unless the --file option is
given, in which case the targets are read from the specified file instead.
The target hosts can be specified as IP addresses or hostnames. You can also
specify the target as IPnetwork/bits (e.g. 192.168.1.0/24) to specify all hosts
in the given network (network and broadcast addresses included), or
IPstart-IPend (e.g. 192.168.1.3-192.168.1.27) to specify all hosts in the
inclusive range, or IPnetwork:NetMask (e.g. 192.168.1.0:255.255.255.0) to
specify all hosts in the given network and mask.
These different options for specifying target hosts may be used both on the
command line, and also in the file specified with the --file option.
In the options below a letter or word in angle brackets like <f> denotes a
value or string that should be supplied. The corresponding text should
indicate the meaning of this value or string. When supplying the value or
string, do not include the angle brackets. Text in square brackets like [<f>]
mean that the enclosed text is optional. This is used for options which take
an optional argument.
Options:
--help or -h		Display this usage message and exit.
--file=<fn> or -f <fn>	Read hostnames or addresses from the specified file
			instead of from the command line. One name or IP
			address per line.  Use "-" for standard input.
--sport=<p> or -s <p>	Set UDP source port to <p>, default=500, 0=random.
			Some IKE implementations require the client to use
			UDP source port 500 and will not talk to other ports.
			Note that superuser privileges are normally required
			to use non-zero source ports below 1024.  Also only
			one process on a system may bind to a given source port
			at any one time. Use of the --nat-t option changes
			the default source port to 4500
--dport=<p> or -d <p>	Set UDP destination port to <p>, default=500.
			UDP port 500 is the assigned port number for ISAKMP
			and this is the port used by most if not all IKE
			implementations. Use of the --nat-t option changes
			the default destination port to 4500
--retry=<n> or -r <n>	Set total number of attempts per host to <n>,
			default=3.
--timeout=<n> or -t <n>	Set initial per host timeout to <n> ms, default=500.
			This timeout is for the first packet sent to each host.
			subsequent timeouts are multiplied by the backoff
			factor which is set with --backoff.
--bandwidth=<n> or -B <n> Set desired outbound bandwidth to <n>, default=56000
			The value is in bits per second by default.  If you
			append "K" to the value, then the units are kilobits
			per second; and if you append "M" to the value,
			the units are megabits per second.
			The "K" and "M" suffixes represent the decimal, not
			binary, multiples.  So 64K is 64000, not 65536.
--interval=<n> or -i <n> Set minimum packet interval to <n> ms.
			The packet interval will be no smaller than this number.
			The interval specified is in milliseconds by default.
			if "u" is appended to the value, then the interval
			is in microseconds, and if "s" is appended, the
			interval is in seconds.
			If you want to use up to a given bandwidth, then it is
			easier to use the --bandwidth option instead.
			You cannot specify both --interval and --bandwidth
			because they are just different ways to change the
			same underlying variable.
--backoff=<b> or -b <b>	Set timeout backoff factor to <b>, default=1.50.
			The per-host timeout is multiplied by this factor
			after each timeout.  So, if the number of retries
			is 3, the initial per-host timeout is 500ms and the
			backoff factor is 1.5, then the first timeout will be
			500ms, the second 750ms and the third 1125ms.
--verbose or -v		Display verbose progress messages.
			Use more than once for greater effect:
			1 - Show when each pass is completed and when
			    packets with invalid cookies are received.
			2 - Show each packet sent and received and when
			    hosts are removed from the list.
			3 - Display the host, Vendor ID and backoff lists
			    before scanning starts.
--quiet or -q		Don't decode the returned packet.
			This prints less protocol information so the
			output lines are shorter.
--multiline or -M	Split the payload decode across multiple lines.
			With this option, the decode for each payload is
			printed on a separate line starting with a TAB.
			This option makes the output easier to read, especially
			when there are many payloads.
--lifetime=<s> or -l <s> Set IKE lifetime to <s> seconds, default=28800.
			RFC 2407 specifies 28800 as the default, but some
			implementations may require different values.
			If you specify this as a a decimal integer, e.g.
			86400, then the attribute will use a 4-byte value.
			If you specify it as a hex number, e.g. 0xFF, then
			the attribute will use the appropriate size value
			(one byte for this example).
			If you specify the string "none" then no lifetime
			attribute will be added at all.
			You can use this option more than once in conjunction
			with the --trans options to produce multiple transform
			payloads with different lifetimes.  Each --trans option
			will use the previously specified lifetime value.
--lifesize=<s> or -z <s> Set IKE lifesize to <s> Kilobytes, default=0.
			If you specify this as a a decimal integer, e.g.
			86400, then the attribute will use a 4-byte value.
			If you specify it as a hex number, e.g. 0xFF, then
			the attribute will use the appropriate size value
			(one byte for this example).
			You can use this option more than once in conjunction
			with the --trans options to produce multiple transform
			payloads with different lifesizes.  Each --trans option
			will use the previously specified lifesize value.
--auth=<n> or -m <n>	Set auth. method to <n>, default=1 (PSK).
			RFC defined values are 1 to 5.  See RFC 2409 Appendix A.
			Checkpoint hybrid mode is 64221.
			GSS (Windows "Kerberos") is 65001.
			XAUTH uses 65001 to 65010.
			This is not applicable to IKEv2.
--version or -V		Display program version and exit.
--vendor=<v> or -e <v>	Set vendor id string to hex value <v>.
			You can use this option more than once to send
			multiple vendor ID payloads.
--trans=<t> or -a <t>	Use custom transform <t> instead of default set.
			You can use this option more than once to send
			an arbitrary number of custom transforms.
			There are two ways to specify the transform:
			The new way, where you specify the attribute/value
			pairs, and the old way where you specify the values
			for a fixed list of attributes.
			For the new method, the transform <t> is specified as
			(attr=value, attr=value, ...)
			Where "attr" is the attribute number, and "value" is
			the value to assign to that attribute.
			For a basic attribute, specify the value as a decimal
			number; for a variable length attribute, specify the
			value as a hex number prefixed with 0x. You can specify
			an arbitary number of attribute/value pairs.
			See RFC 2409 Appendix A for details of the attributes
			and values.
			Note that brackets are special to some shells, so you
			may need to quote them, e.g.
			--trans="(1=1,2=2,3=3,4=4)". For example,
			--trans=(1=1,2=2,3=1,4=2) specifies
			Enc=DES-CBC, Hash=SHA1, Auth=shared key, DH Group=2;
			--trans=(1=7,14=128,2=1,3=3,4=5) specifies
			Enc=AES/128, Hash=MD5, Auth=RSA sig, DH Group=5 and
			--trans=(1=5,2=1,3=1,4=1,11=1,12=0x00007080) specifies
			Enc=3DES-CBC, Hash=MD5, Auth=shared key, DH Group=1,
			Lifetime=28800 seconds as a 4-byte variable attribute.
			For the old method, the transform <t> is specified as
			enc[/len],hash,auth,group.
			Where enc is the encryption algorithm,
			len is the key length for variable length ciphers,
			hash is the hash algorithm, and group is the DH Group.
			For example, --trans=5,2,1,2 specifies
			Enc=3DES-CBC, Hash=SHA1, Auth=shared key, DH Group=2;
			and --trans=7/256,1,1,5 specifies
			Enc=AES-256, Hash=MD5, Auth=shared key, DH Group=5.
			This option is not yet supported for IKEv2.
--showbackoff[=<n>] or -o[<n>]	Display the backoff fingerprint table.
			Display the backoff table to fingerprint the IKE
			implementation on the remote hosts.
			The optional argument specifies time to wait in seconds
			after receiving the last packet, default=60.
			If you are using the short form of the option (-o)
			then the value must immediately follow the option
			letter with no spaces, e.g. -o25 not -o 25.
--fuzz=<n> or -u <n>	Set pattern matching fuzz to <n> ms, default=500.
			This sets the maximum acceptable difference between
			the observed backoff times and the reference times in
			the backoff patterns file.  Larger values allow for
			higher variance but also increase the risk of
			false positive identifications.
			Any per-pattern-entry fuzz specifications in the
			patterns file will override the value set here.
--patterns=<f> or -p <f> Use IKE backoff patterns file <f>,
			default=/usr/share/ike-scan/ike-backoff-patterns.
			This specifies the name of the file containing
			IKE backoff patterns.  This file is only used when
			--showbackoff is specified.
--vidpatterns=<f> or -I <f> Use Vendor ID patterns file <f>,
			default=/usr/share/ike-scan/ike-vendor-ids.
			This specifies the name of the file containing
			Vendor ID patterns.  These patterns are used for
			Vendor ID fingerprinting.
--aggressive or -A	Use IKE Aggressive Mode (The default is Main Mode)
			If you specify --aggressive, then you may also
			specify --dhgroup, --id and --idtype.  If you use
			custom transforms with aggressive mode with the --trans
			option, note that all transforms should have the same
			DH Group and this should match the group specified
			with --dhgroup or the default if --dhgroup is not used.
--id=<id> or -n <id>	Use <id> as the identification value.
			This option is only applicable to Aggressive Mode.
			<id> can be specified as a string, e.g. --id=test or as
			a hex value with a leading "0x", e.g. --id=0xdeadbeef.
--idtype=<n> or -y <n>	Use identification type <n>.  Default 3 (ID_USER_FQDN).
			This option is only applicable to Aggressive Mode.
			See RFC 2407 4.6.2 for details of Identification types.
--dhgroup=<n> or -g <n>	Use Diffie Hellman Group <n>.  Default 2.
			This option is only applicable to Aggressive Mode and
			IKEv2.  For both of these, it is used to determine the
			size of the key exchange payload.
			If you use Aggressive Mode with custom transforms, then
			you will normally need to use the --dhgroup option
			unless you are using the default DH group.
			Acceptable values are 1,2,5,14,15,16,17,18,19,20,21.
--gssid=<n> or -G <n>	Use GSS ID <n> where <n> is a hex string.
			This uses transform attribute type 16384 as specified
			in draft-ietf-ipsec-isakmp-gss-auth-07.txt, although
			Windows-2000 has been observed to use 32001 as well.
			For Windows 2000, you'll need to use --auth=65001 to
			specify Kerberos (GSS) authentication.
--random or -R		Randomise the host list.
			This option randomises the order of the hosts in the
			host list, so the IKE probes are sent to the hosts in
			a random order.  It uses the Knuth shuffle algorithm.
--tcp[=<n>] or -T[<n>]	Use TCP transport instead of UDP.
			This allows you to test a host running IKE over TCP.
			You won't normally need this option because the vast
			majority of IPsec systems only support IKE over UDP.
			The optional value <n> specifies the type of IKE over
			TCP.  There are currently two possible values:
			1 = RAW IKE over TCP as used by Checkpoint (default);
			2 = Encapsulated IKE over TCP as used by Cisco.
			If you are using the short form of the option (-T)
```

### `psk-crack`

> 官方示例调用：`psk-crack -h`

```text
root@kali:~# psk-crack -h
Usage: psk-crack [options] <psk-parameters-file>
<psk-parameters-file> is a file containing the parameters for the pre-shared
key cracking process in the format generated by ike-scan with the --pskcrack
(-P) option.  This file can contain one or more entries.  For multiple entries,
each one must be on a separate line.
Two SKEYID computation methods are supported: the standard method for pre-
shared keys as described in RFC 2409, and the proprietary method used by
Nortel Contivity / VPN Router systems.  The standard method is used by default,
and the Nortel method can be selected with the --norteluser option.
The program can crack either MD5 or SHA1-based hashes.  The type of hash is
automatically determined from the length of the hash (16 bytes for MD5 or
20 bytes for SHA1).  Each entry in the <psk-parameters-file> is handled
separately, so it is possible to crack a mixture of MD5 and SHA1 hashes.
By default, psk-crack will perform dictionary cracking using the default
dictionary.  The dictionary can be changed with the --dictionary (-d) option,
or brute-force cracking can be selected with the --bruteforce (-B) option.
Options:
--help or -h		Display this usage message and exit.
--version or -V		Display program version and exit.
--verbose or -v		Display verbose progress messages.
			Use more than once for increased verbosity.
--dictionary=<f> or -d <f> Set dictionary file to <f>
			default=/usr/share/ike-scan/psk-crack-dictionary.
			Use "-" for standard input.
--norteluser=<u> or -u <u> Specify username for Nortel Contivity PSK cracking.
			This option is required when cracking pre-shared keys
			on Nortel Contivity / VPN Router systems.  These
			systems use a proprietary method to calculate the hash
			that includes a hash of the username.
			This option is only needed when cracking Nortel format
			hashes, and should not be used for standard format
			hashes.
			When this option is used, all the PSK entries in the
			psk parameters file are assumed to be in Nortel format
			using the supplied username. There is currently no way
			to crack a mixture of Nortel and standard format PSK
			entries, or Nortel entries with different usernames in
			a single psk-crack run.
--bruteforce=<n> or -B <n> Select bruteforce cracking up to <n> characters.
--charset=<s> or -c <s>	Set bruteforce character set to <s>
			Default is "0123456789abcdefghijklmnopqrstuvwxyz"
Report bugs or send suggestions at https://github.com/royhills/ike-scan
See the ike-scan homepage at http://www.nta-monitor.com/tools/ike-scan/
Updated on: 2025-Dec-09
 Edit this page
ifenslave
inspy
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install ike-scan`，再执行 `ike-scan --version` 2>/dev/null || `ike-scan -V`
- [ ] **2.** **读官方帮助** —— `ike-scan -h`，需要细节时 `man ike-scan`
- [ ] **3.** **在自有靶场跑最小用例** —— 官方给出的调用形式是：`Usage: ike-scan [options] [hosts...]`
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/ike-scan/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- **精讲教程**（含原理、参数详解、靶场实操与输出解读）：[ike-scan](../../tools/tutorials/02-漏洞分析/ike-scan.md)
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/discovery.md`](../../tools/by-attack/discovery.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/ike-scan/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/ike-scan/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
