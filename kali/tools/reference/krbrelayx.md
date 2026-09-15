# krbrelayx

> Kerberos relaying and unconstrained delegation abuse toolkit Kerberos relaying and unconstrained delegation abuse toolkit. This tool can add/remove/modify Service Principal Names on accounts in AD over LDAP.

> **功能分类**：通用工具 ｜ **Kali 包**：`krbrelayx` ｜ **官方文档**：<https://www.kali.org/tools/krbrelayx/>

## 1. 安装

```bash
sudo apt update
sudo apt install krbrelayx
```

| 项目 | 内容 |
|------|------|
| 版本 | 0.0~git20260311.10b45a3 |
| 架构 | all |
| 可执行命令 | `krbrelayx`、`addspn`、`dnstool`、`printerbug` |
| 依赖 | `python3`、`python3-dnspython`、`python3-impacket`、`python3-ldap3`、`addspn` |
| 安装体积 | 172 KB |
| 官网 | <https://github.com/dirkjanm/krbrelayx> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/krbrelayx> |
| 包追踪 | <https://pkg.kali.org/pkg/krbrelayx> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
krbrelayx -h          # 查看用法
man krbrelayx         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 4 个可执行命令，下面是官方页面内嵌的帮助原文。

### `addspn`

官方给出的调用示例：`addspn -h`

```text
root@kali:~# addspn -h
usage: addspn.py [-h] [-u USERNAME] [-p PASSWORD] [-t TARGET] [-T TARGETTYPE]
                 [-s SPN] [-r] [-c] [-q] [-a] [-k] [-dc-ip ip address]
                 [-aesKey hex key]
                 HOSTNAME
Add an SPN to a user/computer account
Required options:
  HOSTNAME              Hostname/ip or ldap://host:port connection string to
                        connect to
Main options:
  -h, --help            show this help message and exit
  -u, --user USERNAME   DOMAIN\username for authentication
  -p, --password PASSWORD
                        Password or LM:NTLM hash, will prompt if not specified
  -t, --target TARGET   Computername or username to target (FQDN or COMPUTER$
                        name, if unspecified user with -u is target)
  -T, --target-type TARGETTYPE
                        Target type (samname or hostname) If unspecified, will
                        assume it's a hostname if there is a . in the name and
                        a SAM name otherwise.
  -s, --spn SPN         servicePrincipalName to add (for example:
                        http/host.domain.local or cifs/host.domain.local)
  -r, --remove          Remove the SPN instead of add it
  -c, --clear           Clear, i.e. remove all SPNs
  -q, --query           Show the current target SPNs instead of modifying
                        anything
  -a, --additional      Add the SPN via the msDS-AdditionalDnsHostName
                        attribute
  -k, --kerberos        Use Kerberos authentication. Grabs credentials from
                        ccache file (KRB5CCNAME) based on target parameters.
                        If valid credentials cannot be found, it will use the
                        ones specified in the command line
  -dc-ip ip address     IP Address of the domain controller. If omitted it
                        will use the domain part (FQDN) specified in the
                        target parameter
  -aesKey hex key       AES key to use for Kerberos Authentication (128 or 256
                        bits)
```

### `dnstool`

官方给出的调用示例：`dnstool -h`

```text
root@kali:~# dnstool -h
usage: dnstool.py [-h] [-u USERNAME] [-p PASSWORD] [--forest] [--legacy]
                  [--zone ZONE] [--print-zones] [--print-zones-dn] [--tcp]
                  [-k] [-port port] [-force-ssl] [-dc-ip ip address]
                  [-dns-ip ip address] [-aesKey hex key] [-r TARGETRECORD]
                  [-a {add,modify,query,remove,resurrect,ldapdelete}] [-t {A}]
                  [-d RECORDDATA] [--allow-multiple] [--ttl TTL]
                  HOSTNAME
Query/modify DNS records for Active Directory integrated DNS via LDAP
Required options:
  HOSTNAME              Hostname/ip or ldap://host:port connection string to
                        connect to
Main options:
  -h, --help            show this help message and exit
  -u, --user USERNAME   DOMAIN\username for authentication.
  -p, --password PASSWORD
                        Password or LM:NTLM hash, will prompt if not specified
  --forest              Search the ForestDnsZones instead of DomainDnsZones
  --legacy              Search the System partition (legacy DNS storage)
  --zone ZONE           Zone to search in (if different than the current
                        domain)
  --print-zones         Only query all zones on the DNS server, no other
                        modifications are made
  --print-zones-dn      Query and print the Distinguished Names of all zones
                        on the DNS server
  --tcp                 use DNS over TCP
  -k, --kerberos        Use Kerberos authentication. Grabs credentials from
                        ccache file (KRB5CCNAME) based on target parameters.
                        If valid credentials cannot be found, it will use the
                        ones specified in the command line
  -port port            LDAP port, default value is 389
  -force-ssl            Force SSL when connecting to LDAP server
  -dc-ip ip address     IP Address of the domain controller. If omitted it
                        will use the domain part (FQDN) specified in the
                        target parameter
  -dns-ip ip address    IP Address of a DNS Server
  -aesKey hex key       AES key to use for Kerberos Authentication (128 or 256
                        bits)
Record options:
  -r, --record TARGETRECORD
                        Record to target (FQDN)
  -a, --action {add,modify,query,remove,resurrect,ldapdelete}
                        Action to perform. Options: add (add a new record),
                        modify (modify an existing record), query (show
                        existing), remove (mark record for cleanup from DNS
                        cache), delete (delete from LDAP). Default: query
  -t, --type {A}        Record type to add (Currently only A records
                        supported)
  -d, --data RECORDDATA
                        Record data (IP address)
  --allow-multiple      Allow multiple A records for the same name
  --ttl TTL             TTL for record (default: 180)
```

### `krbrelayx`

官方给出的调用示例：`krbrelayx -h`

```text
root@kali:~# krbrelayx -h
usage: krbrelayx.py [-h] [-debug] [-t TARGET] [-tf TARGETSFILE] [-w]
                    [-ip INTERFACE_IP] [-r SMBSERVER] [-l LOOTDIR]
                    [-f {ccache,kirbi}] [-codec CODEC] [-no-smb2support]
                    [-wh WPAD_HOST] [-wa WPAD_AUTH_NUM] [-6] [-p PASSWORD]
                    [-hp HEXPASSWORD] [-s USERNAME] [-hashes LMHASH:NTHASH]
                    [-aesKey hex key] [-dc-ip ip address] [-e FILE]
                    [-c COMMAND] [--enum-local-admins] [--no-dump] [--no-da]
                    [--no-acl] [--no-validate-privs]
                    [--escalate-user ESCALATE_USER]
                    [--add-computer [COMPUTERNAME]] [--delegate-access]
                    [--sid] [--dump-laps] [--dump-gmsa] [--dump-adcs] [--adcs]
                    [--template TEMPLATE] [--altname ALTNAME] [-v TARGET]
Kerberos relay and unconstrained delegation abuse tool. By @_dirkjan /
dirkjanm.io
Main options:
  -h, --help            show this help message and exit
  -debug                Turn DEBUG output ON
  -t, --target TARGET   Target to attack, since this is Kerberos, only
                        HOSTNAMES are valid. Example: smb://server:445 If
                        unspecified, will store tickets for later use.
  -tf TARGETSFILE       File that contains targets by hostname or full URL,
                        one per line
  -w                    Watch the target file for changes and update target
                        list automatically (only valid with -tf)
  -ip, --interface-ip INTERFACE_IP
                        IP address of interface to bind SMB and HTTP servers
  -r SMBSERVER          Redirect HTTP requests to a file:// path on SMBSERVER
  -l, --lootdir LOOTDIR
                        Loot directory in which gathered loot (TGTs or dumps)
                        will be stored (default: current directory).
  -f, --format {ccache,kirbi}
                        Format to store tickets in. Valid: ccache (Impacket)
                        or kirbi (Mimikatz format) default: ccache
  -codec CODEC          Sets encoding used (codec) from the target's output
                        (default "utf-8"). If errors are detected, run
                        chcp.com at the target, map the result with
                        https://docs.python.org/2.4/lib/standard-
                        encodings.html and then execute ntlmrelayx.py again
                        with -codec and the corresponding codec
  -no-smb2support       Disable SMB2 Support
  -wh, --wpad-host WPAD_HOST
                        Enable serving a WPAD file for Proxy Authentication
                        attack, setting the proxy host to the one supplied.
  -wa, --wpad-auth-num WPAD_AUTH_NUM
                        Prompt for authentication N times for clients without
                        MS16-077 installed before serving a WPAD file.
  -6, --ipv6            Listen on both IPv6 and IPv4
Kerberos Keys (of your account with unconstrained delegation):
  -p, --krbpass PASSWORD
                        Account password
  -hp, --krbhexpass HEXPASSWORD
                        Hex-encoded password
  -s, --krbsalt USERNAME
                        Case sensitive (!) salt. Used to calculate Kerberos
                        keys.Only required if specifying password instead of
                        keys.
  -hashes LMHASH:NTHASH
                        NTLM hashes, format is LMHASH:NTHASH
  -aesKey hex key       AES key to use for Kerberos Authentication (128 or 256
                        bits)
  -dc-ip ip address     IP Address of the domain controller. If ommited it use
                        the domain part (FQDN) specified in the target
                        parameter
SMB attack options:
  -e FILE               File to execute on the target system. If not
                        specified, hashes will be dumped (secretsdump.py must
                        be in the same directory)
  -c COMMAND            Command to execute on target system. If not specified,
                        hashes will be dumped (secretsdump.py must be in the
                        same directory).
  --enum-local-admins   If relayed user is not admin, attempt SAMR lookup to
                        see who is (only works pre Win 10 Anniversary)
LDAP attack options:
  --no-dump             Do not attempt to dump LDAP information
  --no-da               Do not attempt to add a Domain Admin
  --no-acl              Disable ACL attacks
  --no-validate-privs   Do not attempt to enumerate privileges, assume
                        permissions are granted to escalate a user via ACL
                        attacks
  --escalate-user ESCALATE_USER
                        Escalate privileges of this user instead of creating a
                        new one
  --add-computer [COMPUTERNAME]
                        Attempt to add a new computer account
  --delegate-access     Delegate access on relayed computer account to the
                        specified account
  --sid                 Use a SID to delegate access rather than an account
                        name
  --dump-laps           Attempt to dump any LAPS passwords readable by the
                        user
  --dump-gmsa           Attempt to dump any gMSA passwords readable by the
                        user
  --dump-adcs           Attempt to dump ADCS enrollment services and
                        certificate templates info
AD CS attack options:
  --adcs                Enable AD CS relay attack
  --template TEMPLATE   AD CS template. Defaults to Machine or User whether
                        relayed account name ends with `$`. Relaying a DC
                        should require specifying `DomainController`
  --altname ALTNAME     Subject Alternative Name to use when performing ESC1
                        or ESC6 attacks.
  -v, --victim TARGET   Victim username or computername$, to request the
                        correct certificate name.
```

### `printerbug`

官方给出的调用示例：`printerbug -h`

```text
root@kali:~# printerbug -h
usage: printerbug.py [-h] [--verbose] [-target-file file]
                     [-port [destination port]] [-timeout timeout] [-no-ping]
                     [-hashes LMHASH:NTHASH] [-no-pass] [-k]
                     [-dc-ip ip address] [-target-ip ip address]
                     target attackerhost
positional arguments:
  target                [[domain/]username[:password]@]<targetName or address>
  attackerhost          hostname to connect to
options:
  -h, --help            show this help message and exit
  --verbose             Switch verbosity to DEBUG
connection:
  -target-file file     Use the targets in the specified file instead of the
                        one on the command line (you must still specify
                        something as target name)
  -port [destination port]
                        Destination port to connect to SMB Server
  -timeout timeout      Specify a timeout for the TCP ping check
  -no-ping              Specify if a TCP ping should be done before
                        connectionNOT recommended since SMB timeouts default
                        to 300 secs and the TCP ping assures connectivity to
                        the SMB port
authentication:
  -hashes LMHASH:NTHASH
                        NTLM hashes, format is LMHASH:NTHASH
  -no-pass              don't ask for password (useful when proxying through
                        ntlmrelayx)
  -k                    Use Kerberos authentication. Grabs credentials from
                        ccache file (KRB5CCNAME) based on target parameters.
                        If valid credentials cannot be found, it will use the
                        ones specified in the command line
  -dc-ip ip address     IP Address of the domain controller. If omitted it
                        will use the domain part (FQDN) specified in the
                        target parameter
  -target-ip ip address
                        IP Address of the target machine. If omitted it will
                        use whatever was specified as target. This is useful
                        when target is the NetBIOS name or Kerberos name and
                        you cannot resolve it
Updated on: 2026-May-25
 Edit this page
joplin
kustomize
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install krbrelayx`，再执行 `krbrelayx --version` 2>/dev/null || `krbrelayx -V`
- [ ] **2.** **读官方帮助** —— `krbrelayx -h`，需要细节时 `man krbrelayx`
- [ ] **3.** **在自有靶场跑最小用例** —— 用 `krbrelayx -h` 里最简单的那个子命令试一次
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/krbrelayx/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/credential-access.md`](../../tools/by-attack/credential-access.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/krbrelayx/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/krbrelayx/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
