# impacket

> Python3 module to easily build and dissect network protocols Impacket is a collection of Python3 classes focused on providing access to network packets. Impacket allows Python3 developers to craft and decode network packets in simple and c…

> **功能分类**：信息搜集 ｜ **Kali 包**：`impacket` ｜ **官方文档**：<https://www.kali.org/tools/impacket/>

## 1. 安装

```bash
sudo apt update
sudo apt install python3-impacket
```

| 项目 | 内容 |
|------|------|
| 版本 | 0.13.0 |
| 架构 | all |
| 可执行命令 | `python3-impacket`、`impacket-netview`、`impacket-rpcdump`、`impacket-samrdump`、`impacket-secretsdump`、`impacket-wmiexec` |
| 依赖 | `python3`、`python3-charset-normalizer`、`python3-flask`、`python3-ldap3`、`python3-ldapdomaindump`、`python3-openssl`、`python3-pyasn1`、`python3-pyasn1-modules`、`python3-pycryptodome`、`python3-six`、`impacket-netview` |
| 安装体积 | 7.31 MB |
| 官网 | <https://github.com/SecureAuthCorp/impacket> |
| 源码仓库 | <https://salsa.debian.org/python-team/packages/impacket> |
| 包追踪 | <https://pkg.kali.org/pkg/impacket> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
python3-impacket -h          # 查看用法
man python3-impacket         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 6 个可执行命令，下面是官方页面内嵌的帮助原文。

### `impacket-netview`

> 官方示例调用：`impacket-netview -h`

```text
root@kali:~# impacket-netview -h
Impacket v0.14.0.dev0 - Copyright Fortra, LLC and its affiliated companies
usage: netview.py [-h] [-user USER] [-users USERS] [-target TARGET]
                  [-targets TARGETS] [-noloop] [-delay DELAY]
                  [-max-connections MAX_CONNECTIONS] [-ts] [-debug]
                  [-hashes LMHASH:NTHASH] [-no-pass] [-k] [-aesKey hex key]
                  [-dc-ip ip address]
                  identity
positional arguments:
  identity              [domain/]username[:password]
options:
  -h, --help            show this help message and exit
  -user USER            Filter output by this user
  -users USERS          input file with list of users to filter to output for
  -target TARGET        target system to query info from. If not specified
                        script will run in domain mode.
  -targets TARGETS      input file with targets system to query info from (one
                        per line). If not specified script will run in domain
                        mode.
  -noloop               Stop after the first probe
  -delay DELAY          seconds delay between starting each batch probe
                        (default 10 seconds)
  -max-connections MAX_CONNECTIONS
                        Max amount of connections to keep opened (default
                        1000)
  -ts                   Adds timestamp to every logging output
  -debug                Turn DEBUG output ON
authentication:
  -hashes LMHASH:NTHASH
                        NTLM hashes, format is LMHASH:NTHASH
  -no-pass              don't ask for password (useful for -k)
  -k                    Use Kerberos authentication. Grabs credentials from
                        ccache file (KRB5CCNAME) based on target parameters.
                        If valid credentials cannot be found, it will use the
                        ones specified in the command line
  -aesKey hex key       AES key to use for Kerberos Authentication (128 or 256
                        bits)
  -dc-ip ip address     IP Address of the domain controller. If ommited it use
                        the domain part (FQDN) specified in the target
                        parameter
```

### `impacket-rpcdump`

> 官方示例调用：`impacket-rpcdump -h`

```text
root@kali:~# impacket-rpcdump -h
Impacket v0.14.0.dev0 - Copyright Fortra, LLC and its affiliated companies
usage: rpcdump.py [-h] [-debug] [-ts] [-target-ip ip address]
                  [-port [destination port]] [-hashes LMHASH:NTHASH]
                  target
Dumps the remote RPC enpoints information via epmapper.
positional arguments:
  target                [[domain/]username[:password]@]<targetName or address>
options:
  -h, --help            show this help message and exit
  -debug                Turn DEBUG output ON
  -ts                   Adds timestamp to every logging output
connection:
  -target-ip ip address
                        IP Address of the target machine. If ommited it will
                        use whatever was specified as target. This is useful
                        when target is the NetBIOS name and you cannot resolve
                        it
  -port [destination port]
                        Destination port to connect to RPC Endpoint Mapper
authentication:
  -hashes LMHASH:NTHASH
                        NTLM hashes, format is LMHASH:NTHASH
```

### `impacket-samrdump`

> 官方示例调用：`impacket-samrdump -h`

```text
root@kali:~# impacket-samrdump -h
Impacket v0.14.0.dev0 - Copyright Fortra, LLC and its affiliated companies
usage: samrdump.py [-h] [-csv] [-ts] [-debug] [-dc-ip ip address]
                   [-target-ip ip address] [-port [destination port]]
                   [-hashes LMHASH:NTHASH] [-no-pass] [-k] [-aesKey hex key]
                   target
This script downloads the list of users for the target system.
positional arguments:
  target                [[domain/]username[:password]@]<targetName or address>
options:
  -h, --help            show this help message and exit
  -csv                  Turn CSV output
  -ts                   Adds timestamp to every logging output
  -debug                Turn DEBUG output ON
connection:
  -dc-ip ip address     IP Address of the domain controller. If ommited it use
                        the domain part (FQDN) specified in the target
                        parameter
  -target-ip ip address
                        IP Address of the target machine. If ommited it will
                        use whatever was specified as target. This is useful
                        when target is the NetBIOS name and you cannot resolve
                        it
  -port [destination port]
                        Destination port to connect to SMB Server
authentication:
  -hashes LMHASH:NTHASH
                        NTLM hashes, format is LMHASH:NTHASH
  -no-pass              don't ask for password (useful for -k)
  -k                    Use Kerberos authentication. Grabs credentials from
                        ccache file (KRB5CCNAME) based on target parameters.
                        If valid credentials cannot be found, it will use the
                        ones specified in the command line
  -aesKey hex key       AES key to use for Kerberos Authentication (128 or 256
                        bits)
```

### `impacket-secretsdump`

> 官方示例调用：`impacket-secretsdump -h`

```text
root@kali:~# impacket-secretsdump -h
Impacket v0.14.0.dev0 - Copyright Fortra, LLC and its affiliated companies
usage: secretsdump.py [-h] [-ts] [-debug] [-system SYSTEM] [-bootkey BOOTKEY]
                      [-security SECURITY] [-sam SAM] [-ntds NTDS]
                      [-resumefile RESUMEFILE] [-skip-sam] [-skip-security]
                      [-outputfile OUTPUTFILE] [-use-vss] [-rodcNo RODCNO]
                      [-rodcKey RODCKEY] [-use-keylist]
                      [-exec-method [{smbexec,wmiexec,mmcexec}]]
                      [-use-remoteSSWMI] [-use-remoteSSWMI-NTDS]
                      [-remoteSSWMI-remote-volume REMOTESSWMI_REMOTE_VOLUME]
                      [-remoteSSWMI-local-path REMOTESSWMI_LOCAL_PATH]
                      [-just-dc-user USERNAME] [-ldapfilter LDAPFILTER]
                      [-just-dc] [-just-dc-ntlm] [-skip-user SKIP_USER]
                      [-pwd-last-set] [-user-status] [-history]
                      [-hashes LMHASH:NTHASH] [-no-pass] [-k]
                      [-aesKey hex key] [-keytab KEYTAB] [-dc-ip ip address]
                      [-target-ip ip address]
                      target
Performs various techniques to dump secrets from the remote machine without
executing any agent there.
positional arguments:
  target                [[domain/]username[:password]@]<targetName or address>
                        or LOCAL (if you want to parse local files)
options:
  -h, --help            show this help message and exit
  -ts                   Adds timestamp to every logging output
  -debug                Turn DEBUG output ON
  -system SYSTEM        SYSTEM hive to parse (only binary REGF, as .reg text
                        file lacks the metadata to compute the bootkey)
  -bootkey BOOTKEY      bootkey for SYSTEM hive
  -security SECURITY    SECURITY hive to parse
  -sam SAM              SAM hive to parse
  -ntds NTDS            NTDS.DIT file to parse
  -resumefile RESUMEFILE
                        resume file name to resume NTDS.DIT session dump (only
                        available to DRSUAPI approach). This file will also be
                        used to keep updating the session's state
  -skip-sam             Do NOT parse the SAM hive on remote system
  -skip-security        Do NOT parse the SECURITY hive on remote system
  -outputfile OUTPUTFILE
                        base output filename. Extensions will be added for
                        sam, secrets, cached and ntds
  -use-vss              Use the NTDSUTIL VSS method instead of default DRSUAPI
  -rodcNo RODCNO        Number of the RODC krbtgt account (only avaiable for
                        Kerb-Key-List approach)
  -rodcKey RODCKEY      AES key of the Read Only Domain Controller (only
                        avaiable for Kerb-Key-List approach)
  -use-keylist          Use the Kerb-Key-List method instead of default
                        DRSUAPI
  -exec-method [{smbexec,wmiexec,mmcexec}]
                        Remote exec method to use at target (only when using
                        -use-vss). Default: smbexec
  -use-remoteSSWMI      Remotely create Shadow Snapshot via WMI and download
                        SAM, SYSTEM and SECURITY from it, the parse locally
  -use-remoteSSWMI-NTDS
                        Dump NTDS.DIT also when using the Remote Shadow
                        Snapshot Method via WMI. Use it with dumping from a
                        DC. IMPORTANT: this flag only works when also using
                        -use-remoteSSWMI
  -remoteSSWMI-remote-volume REMOTESSWMI_REMOTE_VOLUME
                        Remote Volume to perform the Shadow Snapshot and
                        download SAM, SYSTEM and SECURITY. It defaults to C:\
  -remoteSSWMI-local-path REMOTESSWMI_LOCAL_PATH
                        Path where download SAM, SYSTEM and SECURITY from
                        Shadow Snapshot. It defaults to current path
display options:
  -just-dc-user USERNAME
                        Extract only NTDS.DIT data for the user specified.
                        Only available for DRSUAPI approach. Implies also
                        -just-dc switch
  -ldapfilter LDAPFILTER
                        Extract only NTDS.DIT data for specific users based on
                        an LDAP filter. Only available for DRSUAPI approach.
                        Implies also -just-dc switch
  -just-dc              Extract only NTDS.DIT data (NTLM hashes and Kerberos
                        keys)
  -just-dc-ntlm         Extract only NTDS.DIT data (NTLM hashes only)
  -skip-user SKIP_USER  Do NOT extract NTDS.DIT data for the user specified.
                        Can provide comma-separated list of users to skip, or
                        text file with one user per line
  -pwd-last-set         Shows pwdLastSet attribute for each NTDS.DIT account.
                        Doesn't apply to -outputfile data
  -user-status          Display whether or not the user is disabled
  -history              Dump password history, and LSA secrets OldVal
authentication:
  -hashes LMHASH:NTHASH
                        NTLM hashes, format is LMHASH:NTHASH
  -no-pass              don't ask for password (useful for -k)
  -k                    Use Kerberos authentication. Grabs credentials from
                        ccache file (KRB5CCNAME) based on target parameters.
                        If valid credentials cannot be found, it will use the
                        ones specified in the command line
  -aesKey hex key       AES key to use for Kerberos Authentication (128 or 256
                        bits)
  -keytab KEYTAB        Read keys for SPN from keytab file
connection:
  -dc-ip ip address     IP Address of the domain controller. If ommited it use
                        the domain part (FQDN) specified in the target
                        parameter
  -target-ip ip address
                        IP Address of the target machine. If omitted it will
                        use whatever was specified as target. This is useful
                        when target is the NetBIOS name and you cannot resolve
                        it
```

### `impacket-wmiexec`

> 官方示例调用：`impacket-wmiexec -h`

```text
root@kali:~# impacket-wmiexec -h
Impacket v0.14.0.dev0 - Copyright Fortra, LLC and its affiliated companies
usage: wmiexec.py [-h] [-share SHARE] [-nooutput] [-ts] [-silentcommand]
                  [-debug] [-codec CODEC] [-shell-type {cmd,powershell}]
                  [-com-version MAJOR_VERSION:MINOR_VERSION]
                  [-hashes LMHASH:NTHASH] [-no-pass] [-k] [-aesKey hex key]
                  [-dc-ip ip address] [-target-ip ip address] [-A authfile]
                  [-keytab KEYTAB]
                  target [command ...]
Executes a semi-interactive shell using Windows Management Instrumentation.
positional arguments:
  target                [[domain/]username[:password]@]<targetName or address>
  command               command to execute at the target. If empty it will
                        launch a semi-interactive shell
options:
  -h, --help            show this help message and exit
  -share SHARE          share where the output will be grabbed from (default
                        ADMIN$)
  -nooutput             whether or not to print the output (no SMB connection
                        created)
  -ts                   Adds timestamp to every logging output
  -silentcommand        does not execute cmd.exe to run given command (no
                        output)
  -debug                Turn DEBUG output ON
  -codec CODEC          Sets encoding used (codec) from the target's output
                        (default "utf-8"). If errors are detected, run
                        chcp.com at the target, map the result with https://do
                        cs.python.org/3/library/codecs.html#standard-encodings
                        and then execute wmiexec.py again with -codec and the
                        corresponding codec
  -shell-type {cmd,powershell}
                        choose a command processor for the semi-interactive
                        shell
  -com-version MAJOR_VERSION:MINOR_VERSION
                        DCOM version, format is MAJOR_VERSION:MINOR_VERSION
                        e.g. 5.7
authentication:
  -hashes LMHASH:NTHASH
                        NTLM hashes, format is LMHASH:NTHASH
  -no-pass              don't ask for password (useful for -k)
  -k                    Use Kerberos authentication. Grabs credentials from
                        ccache file (KRB5CCNAME) based on target parameters.
                        If valid credentials cannot be found, it will use the
                        ones specified in the command line
  -aesKey hex key       AES key to use for Kerberos Authentication (128 or 256
                        bits)
  -dc-ip ip address     IP Address of the domain controller. If ommited it use
                        the domain part (FQDN) specified in the target
                        parameter
  -target-ip ip address
                        IP Address of the target machine. If omitted it will
                        use whatever was specified as target. This is useful
                        when target is the NetBIOS name and you cannot resolve
                        it
  -A authfile           smbclient/mount.cifs-style authentication file. See
                        smbclient man page's -A option.
  -keytab KEYTAB        Read keys for SPN from keytab file
Learn more with
OffSec
Want to learn more about impacket? get access to in-depth training and hands-on labs:
PEN-200: 16.3.2. Password Attacks: Passing NTLM
PEN-300: 22.2.2. Attacking Active Directory Certificate Services: NTLM Relay to ADCS HTTP Endpoints
PEN-300: 23. Attacking Active Directory: 23.1. Kerberos Delegation
PEN-200 course
PEN-300 course
Updated on: 2026-Mar-02
 Edit this page
imhex
inviteflood
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install python3-impacket`，再执行 `python3-impacket --version` 2>/dev/null || `python3-impacket -V`
- [ ] **2.** **读官方帮助** —— `python3-impacket -h`，需要细节时 `man python3-impacket`
- [ ] **3.** **在自有靶场跑最小用例** —— 用 `python3-impacket -h` 里最简单的那个子命令试一次
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/impacket/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- **精讲教程**（含原理、参数详解、靶场实操与输出解读）：[impacket](../../tools/tutorials/08-后渗透/impacket.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/impacket/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/impacket/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
