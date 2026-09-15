# impacket-scripts

> Links to useful impacket scripts examples This package contains links to useful impacket scripts. It’s a separate package to keep impacket package from Debian and have the useful scripts in the path for Kali.

> **功能分类**：信息搜集 ｜ **Kali 包**：`impacket-scripts` ｜ **官方文档**：<https://www.kali.org/tools/impacket-scripts/>

## 1. 安装

```bash
sudo apt update
sudo apt install impacket-scripts
```

| 项目 | 内容 |
|------|------|
| 版本 | 1.1 |
| 架构 | all |
| 可执行命令 | `impacket-scripts` |
| 依赖 | `python3-dnspython`、`python3-dsinternals`、`python3-impacket`、`python3-ldap3`、`python3-ldapdomaindump`、`python3-pcapy` |
| 安装体积 | 65 KB |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/impacket-scripts> |
| 包追踪 | <https://pkg.kali.org/pkg/impacket-scripts> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
impacket-scripts -h          # 查看用法
man impacket-scripts         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `impacket-DumpNTLMInfo`

官方给出的调用示例：`impacket-DumpNTLMInfo -h`

```text
root@kali:~# impacket-DumpNTLMInfo -h
Impacket v0.14.0.dev0 - Copyright Fortra, LLC and its affiliated companies
usage: DumpNTLMInfo.py [-h] [-debug] [-ts] [-target-ip ip address]
                       [-port destination port] [-protocol [protocol]]
                       target
Do ntlm authentication and parse information.
positional arguments:
  target                <targetName or address>
options:
  -h, --help            show this help message and exit
  -debug                Turn DEBUG output ON
  -ts                   Adds timestamp to every logging output
  -target-ip ip address
                        IP Address of the target machine. If omitted it will
                        use whatever was specified as target. This is useful
                        when target is the NetBIOS name and you cannot resolve
                        it
  -port destination port
                        Destination port to connect to SMB/RPC Server
  -protocol [protocol]  Protocol to use (SMB or RPC). Default is SMB, port 135
                        uses RPC normally.
impacket-Get-GPPPassword
```

### `impacket-Get-GPPPassword`

官方给出的调用示例：`impacket-Get-GPPPassword -h`

```text
root@kali:~# impacket-Get-GPPPassword -h
Impacket v0.14.0.dev0 - Copyright Fortra, LLC and its affiliated companies
usage: Get-GPPPassword.py [-h] [-xmlfile XMLFILE] [-share SHARE]
                          [-base-dir BASE_DIR] [-ts] [-debug]
                          [-hashes LMHASH:NTHASH] [-no-pass] [-k]
                          [-aesKey hex key] [-dc-ip ip address]
                          [-target-ip ip address] [-port [destination port]]
                          target
Group Policy Preferences passwords finder and decryptor.
positional arguments:
  target                [[domain/]username[:password]@]<targetName or address>
                        or LOCAL (if you want to parse local files)
options:
  -h, --help            show this help message and exit
  -xmlfile XMLFILE      Group Policy Preferences XML files to parse
  -share SHARE          SMB Share
  -base-dir BASE_DIR    Directory to search in (Default: /)
  -ts                   Adds timestamp to every logging output
  -debug                Turn DEBUG output ON
authentication:
  -hashes LMHASH:NTHASH
                        NTLM hashes, format is LMHASH:NTHASH
  -no-pass              Don't ask for password (useful for -k)
  -k                    Use Kerberos authentication. Grabs credentials from
                        ccache file (KRB5CCNAME) based on target parameters.
                        If valid credentials cannot be found, it will use the
                        ones specified in the command line
  -aesKey hex key       AES key to use for Kerberos Authentication (128 or 256
                        bits)
connection:
  -dc-ip ip address     IP Address of the domain controller. If omitted it
                        will use the domain part (FQDN) specified in the
                        target parameter
  -target-ip ip address
                        IP Address of the target machine. If omitted it will
                        use whatever was specified as target. This is useful
                        when target is the NetBIOS name and you cannot resolve
                        it
  -port [destination port]
                        Destination port to connect to SMB Server
impacket-GetADComputers
```

### `impacket-GetADComputers`

官方给出的调用示例：`impacket-GetADComputers -h`

```text
root@kali:~# impacket-GetADComputers -h
Impacket v0.14.0.dev0 - Copyright Fortra, LLC and its affiliated companies
usage: GetADComputers.py [-h] [-user username] [-ts] [-debug] [-resolveIP]
                         [-hashes LMHASH:NTHASH] [-no-pass] [-k]
                         [-aesKey hex key] [-dc-ip ip address]
                         [-dc-host hostname]
                         target
Queries target domain for computer data
positional arguments:
  target                domain[/username[:password]]
options:
  -h, --help            show this help message and exit
  -user username        Requests data for specific user
  -ts                   Adds timestamp to every logging output
  -debug                Turn DEBUG output ON
  -resolveIP            Tries to resolve the IP address of computer objects,
                        by performing the nslookup on the DC.
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
connection:
  -dc-ip ip address     IP Address of the domain controller. If ommited it use
                        the domain part (FQDN) specified in the target
                        parameter
  -dc-host hostname     Hostname of the domain controller to use. If ommited,
                        the domain part (FQDN) specified in the account
                        parameter will be used
impacket-GetADUsers
```

### `impacket-GetADUsers`

官方给出的调用示例：`impacket-GetADUsers -h`

```text
root@kali:~# impacket-GetADUsers -h
Impacket v0.14.0.dev0 - Copyright Fortra, LLC and its affiliated companies
usage: GetADUsers.py [-h] [-user username] [-all] [-ts] [-debug]
                     [-hashes LMHASH:NTHASH] [-no-pass] [-k] [-aesKey hex key]
                     [-dc-ip ip address] [-dc-host hostname]
                     target
Queries target domain for users data
positional arguments:
  target                domain[/username[:password]]
options:
  -h, --help            show this help message and exit
  -user username        Requests data for specific user
  -all                  Return all users, including those with no email
                        addresses and disabled accounts. When used with -user
                        it will return user's info even if the account is
                        disabled
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
connection:
  -dc-ip ip address     IP Address of the domain controller. If ommited it use
                        the domain part (FQDN) specified in the target
                        parameter
  -dc-host hostname     Hostname of the domain controller to use. If ommited,
                        the domain part (FQDN) specified in the account
                        parameter will be used
impacket-GetLAPSPassword
```

### `impacket-GetLAPSPassword`

官方给出的调用示例：`impacket-GetLAPSPassword -h`

```text
root@kali:~# impacket-GetLAPSPassword -h
Impacket v0.14.0.dev0 - Copyright Fortra, LLC and its affiliated companies
usage: GetLAPSPassword.py [-h] [-computer computername] [-ts] [-debug]
                          [-outputfile OUTPUTFILE] [-hashes LMHASH:NTHASH]
                          [-no-pass] [-k] [-aesKey hex key]
                          [-dc-ip ip address] [-dc-host hostname] [-ldaps]
                          target
Extract LAPS passwords from LDAP
positional arguments:
  target                domain[/username[:password]]
options:
  -h, --help            show this help message and exit
  -computer computername
                        Target a specific computer by its name
  -ts                   Adds timestamp to every logging output
  -debug                Turn DEBUG output ON
  -outputfile, -o OUTPUTFILE
                        Outputs to a file.
authentication:
  -hashes LMHASH:NTHASH
                        NTLM hashes, format is LMHASH:NTHASH
  -no-pass              don't ask for password (useful for -k)
  -k                    Use Kerberos authentication. Grabs credentials from
                        ccache file (KRB5CcnAME) based on target parameters.
                        If valid credentials cannot be found, it will use the
                        ones specified in the command line
  -aesKey hex key       AES key to use for Kerberos Authentication (128 or 256
                        bits)
connection:
  -dc-ip ip address     IP Address of the domain controller. If ommited it use
                        the domain part (FQDN) specified in the target
                        parameter
  -dc-host hostname     Hostname of the domain controller to use. If ommited,
                        the domain part (FQDN) specified in the account
                        parameter will be used
  -ldaps                Enable LDAPS (LDAP over SSL). Required when querying a
                        Windows Server 2025domain controller with LDAPS
                        enforced.
impacket-GetNPUsers
```

### `impacket-GetNPUsers`

官方给出的调用示例：`impacket-GetNPUsers -h`

```text
root@kali:~# impacket-GetNPUsers -h
Impacket v0.14.0.dev0 - Copyright Fortra, LLC and its affiliated companies
usage: GetNPUsers.py [-h] [-request] [-outputfile OUTPUTFILE]
                     [-format {hashcat,john}] [-usersfile USERSFILE] [-ts]
                     [-debug] [-hashes LMHASH:NTHASH] [-no-pass] [-k]
                     [-aesKey hex key] [-dc-ip ip address] [-dc-host hostname]
                     target
Queries target domain for users with 'Do not require Kerberos
preauthentication' set and export their TGTs for cracking
positional arguments:
  target                [[domain/]username[:password]]
options:
  -h, --help            show this help message and exit
  -request              Requests TGT for users and output them in JtR/hashcat
                        format (default False)
  -outputfile OUTPUTFILE
                        Output filename to write ciphers in JtR/hashcat format
  -format {hashcat,john}
                        format to save the AS_REQ of users without pre-
                        authentication. Default is hashcat
  -usersfile USERSFILE  File with user per line to test
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
connection:
  -dc-ip ip address     IP Address of the domain controller. If ommited it use
                        the domain part (FQDN) specified in the target
                        parameter
  -dc-host hostname     Hostname of the domain controller to use. If ommited,
                        the domain part (FQDN) specified in the account
                        parameter will be used
impacket-GetUserSPNs
```

### `impacket-GetUserSPNs`

官方给出的调用示例：`impacket-GetUserSPNs -h`

```text
root@kali:~# impacket-GetUserSPNs -h
Impacket v0.14.0.dev0 - Copyright Fortra, LLC and its affiliated companies
usage: GetUserSPNs.py [-h] [-target-domain TARGET_DOMAIN]
                      [-no-preauth NO_PREAUTH] [-stealth] [-machine-only]
                      [-usersfile USERSFILE] [-request]
                      [-request-user username | -request-machine machinename]
                      [-save] [-outputfile OUTPUTFILE] [-ts] [-debug]
                      [-hashes LMHASH:NTHASH] [-no-pass] [-k]
                      [-aesKey hex key] [-dc-ip ip address]
                      [-dc-host hostname]
                      target
Queries target domain for SPNs that are running under a user account
positional arguments:
  target                domain[/username[:password]]
options:
  -h, --help            show this help message and exit
  -target-domain TARGET_DOMAIN
                        Domain to query/request if different than the domain
                        of the user. Allows for Kerberoasting across trusts.
  -no-preauth NO_PREAUTH
                        account that does not require preauth, to obtain
                        Service Ticket through the AS
  -stealth              Removes the (servicePrincipalName=*) filter from the
                        LDAP query for added stealth. May cause huge memory
                        consumption / errors on large domains.
  -machine-only         Queries for machine accounts only, by adjusting
                        `objectCategory=person` to `objectCategory=computer`.
                        Active Directory may limit results to 1,000 objects by
                        default. LDAP paging is required to retrieve more.
  -usersfile USERSFILE  File with user per line to test
  -request              Requests TGS for users and output them in JtR/hashcat
                        format (default False)
  -request-user username
                        Requests TGS for the SPN associated to the user
                        specified (just the username, no domain needed)
  -request-machine machinename
                        Requests TGS for the SPN associated to the machine
                        specified. Example: `workstation01$`
  -save                 Saves TGS requested to disk. Format is
                        <username>.ccache. Auto selects -request
  -outputfile OUTPUTFILE
                        Output filename to write ciphers in JtR/hashcat
                        format. Auto selects -request
  -ts                   Adds timestamp to every logging output.
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
connection:
  -dc-ip ip address     IP Address of the domain controller. If ommited it use
                        the domain part (FQDN) specified in the target
                        parameter. Ignoredif -target-domain is specified.
  -dc-host hostname     Hostname of the domain controller to use. If ommited,
                        the domain part (FQDN) specified in the account
                        parameter will be used
impacket-addcomputer
```

### `impacket-addcomputer`

官方给出的调用示例：`impacket-addcomputer -h`

```text
root@kali:~# impacket-addcomputer -h
Impacket v0.14.0.dev0 - Copyright Fortra, LLC and its affiliated companies
usage: addcomputer.py [-h] [-domain-netbios NETBIOSNAME]
                      [-computer-name COMPUTER-NAME$]
                      [-computer-pass password] [-no-add] [-delete] [-ts]
                      [-debug] [-method {SAMR,LDAPS}] [-port {139,445,636}]
                      [-baseDN DC=test,DC=local]
                      [-computer-group CN=Computers,DC=test,DC=local]
                      [-hashes LMHASH:NTHASH] [-no-pass] [-k]
                      [-aesKey hex key] [-dc-host hostname] [-dc-ip ip]
                      [domain/]username[:password]
Adds a computer account to domain
positional arguments:
  [domain/]username[:password]
                        Account used to authenticate to DC.
options:
  -h, --help            show this help message and exit
  -domain-netbios NETBIOSNAME
                        Domain NetBIOS name. Required if the DC has multiple
                        domains.
  -computer-name COMPUTER-NAME$
                        Name of computer to add.If omitted, a random
                        DESKTOP-[A-Z0-9]{8} will be used.
  -computer-pass password
                        Password to set to computerIf omitted, a random
                        [A-Za-z0-9]{32} will be used.
  -no-add               Don't add a computer, only set password on existing
                        one.
  -delete               Delete an existing computer.
  -ts                   Adds timestamp to every logging output
  -debug                Turn DEBUG output ON
  -method {SAMR,LDAPS}  Method of adding the computer.SAMR works over
                        SMB.LDAPS has some certificate requirementsand isn't
                        always available.
  -port {139,445,636}   Destination port to connect to. SAMR defaults to 445,
                        LDAPS to 636.
LDAP:
  -baseDN DC=test,DC=local
                        Set baseDN for LDAP.If ommited, the domain part (FQDN)
                        specified in the account parameter will be used.
  -computer-group CN=Computers,DC=test,DC=local
                        Group to which the account will be added.If omitted,
                        CN=Computers will be used,
authentication:
  -hashes LMHASH:NTHASH
                        NTLM hashes, format is LMHASH:NTHASH
  -no-pass              don't ask for password (useful for -k)
  -k                    Use Kerberos authentication. Grabs credentials from
                        ccache file (KRB5CCNAME) based on account parameters.
                        If valid credentials cannot be found, it will use the
                        ones specified in the command line
  -aesKey hex key       AES key to use for Kerberos Authentication (128 or 256
                        bits)
  -dc-host hostname     Hostname of the domain controller to use. If ommited,
                        the domain part (FQDN) specified in the account
                        parameter will be used
  -dc-ip ip             IP of the domain controller to use. Useful if you
                        can't translate the FQDN.specified in the account
                        parameter will be used
impacket-atexec
```

### `impacket-atexec`

官方给出的调用示例：`impacket-atexec -h`

```text
root@kali:~# impacket-atexec -h
Impacket v0.14.0.dev0 - Copyright Fortra, LLC and its affiliated companies
usage: atexec.py [-h] [-session-id SESSION_ID] [-ts] [-silentcommand] [-debug]
                 [-codec CODEC] [-hashes LMHASH:NTHASH] [-no-pass] [-k]
                 [-aesKey hex key] [-dc-ip ip address] [-keytab KEYTAB]
                 target [command ...]
positional arguments:
  target                [[domain/]username[:password]@]<targetName or address>
  command               command to execute at the target
options:
  -h, --help            show this help message and exit
  -session-id SESSION_ID
                        an existed logon session to use (no output, no
                        cmd.exe)
  -ts                   adds timestamp to every logging output
  -silentcommand        does not execute cmd.exe to run given command (no
                        output)
  -debug                Turn DEBUG output ON
  -codec CODEC          Sets encoding used (codec) from the target's output
                        (default "utf-8"). If errors are detected, run
                        chcp.com at the target, map the result with https://do
                        cs.python.org/3/library/codecs.html#standard-encodings
                        and then execute wmiexec.py again with -codec and the
                        corresponding codec
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
  -dc-ip ip address     IP Address of the domain controller. If omitted it
                        will use the domain part (FQDN) specified in the
                        target parameter
  -keytab KEYTAB        Read keys for SPN from keytab file
impacket-changepasswd
```

### `impacket-changepasswd`

官方给出的调用示例：`impacket-changepasswd -h`

```text
root@kali:~# impacket-changepasswd -h
Impacket v0.14.0.dev0 - Copyright Fortra, LLC and its affiliated companies
usage: changepasswd.py [-h] [-ts] [-debug] [-newpass NEWPASS |
                       -newhashes LMHASH:NTHASH] [-hashes LMHASH:NTHASH]
                       [-no-pass] [-altuser ALTUSER] [-altpass ALTPASS |
                       -althash ALTHASH]
                       [-protocol {smb-samr,rpc-samr,kpasswd,ldap}] [-reset]
                       [-k] [-aesKey hex key] [-dc-ip ip address]
                       target
Change or reset passwords over different protocols.
positional arguments:
  target                [[domain/]username[:password]@]<hostname or address>
options:
  -h, --help            show this help message and exit
  -ts                   adds timestamp to every logging output
  -debug                turn DEBUG output ON
New credentials for target:
  -newpass NEWPASS      new password
  -newhashes LMHASH:NTHASH
                        new NTLM hashes, format is NTHASH or LMHASH:NTHASH
Authentication (target user whose password is changed):
  -hashes LMHASH:NTHASH
                        NTLM hashes, format is NTHASH or LMHASH:NTHASH
  -no-pass              Don't ask for password (useful for Kerberos, -k)
Authentication (optional, privileged user performing the change):
  -altuser ALTUSER      Alternative username
  -altpass ALTPASS      Alternative password
  -althash, -althashes ALTHASH
                        Alternative NT hash, format is NTHASH or LMHASH:NTHASH
Method of operations:
  -protocol, -p {smb-samr,rpc-samr,kpasswd,ldap}
                        Protocol to use for password change/reset
  -reset, -admin        Try to reset the password with privileges (may bypass
                        some password policies)
Kerberos authentication:
  Applicable to the authenticating user (-altuser if defined, else target)
  -k                    Use Kerberos authentication. Grabs credentials from
                        ccache file (KRB5CCNAME) based on target parameters.
                        If valid credentials cannot be found, it will use the
                        ones specified in the command line
  -aesKey hex key       AES key to use for Kerberos Authentication (128 or 256
                        bits)
  -dc-ip ip address     IP Address of the domain controller, for Kerberos. If
                        omitted it will use the domain part (FQDN) specified
                        in the target parameter
impacket-dacledit
```

## 4. 实践清单

按顺序做完这五步，就能把工具从「装上」推进到「会用」：

- [ ] **1.** **装好并确认版本** —— `sudo apt install impacket-scripts`，再执行 `impacket-scripts --version` 2>/dev/null || `impacket-scripts -V`
- [ ] **2.** **读官方帮助** —— `impacket-scripts -h`，需要细节时 `man impacket-scripts`
- [ ] **3.** **在自有靶场跑最小用例** —— 用 `impacket-scripts -h` 里最简单的那个子命令试一次
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/impacket-scripts/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- **精讲教程**（含原理、参数详解、靶场实操与输出解读）：[impacket](../../tools/tutorials/08-后渗透/impacket.md)
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/defense-evasion.md`](../../tools/by-attack/defense-evasion.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/impacket-scripts/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/impacket-scripts/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
