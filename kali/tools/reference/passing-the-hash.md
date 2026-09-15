# passing-the-hash

> Patched tools to use password hashes as authentication input This package contains modified versions of Curl, Iceweasel, FreeTDS, Samba 4, WinEXE and WMI. They are installed as executables starting with the “pth-” string.

> **功能分类**：口令攻击 ｜ **Kali 包**：`passing-the-hash` ｜ **官方文档**：<https://www.kali.org/tools/passing-the-hash/>

## 1. 安装

```bash
sudo apt update
sudo apt install passing-the-hash
```

| 项目 | 内容 |
|------|------|
| 版本 | 0~2015.12.37 |
| 架构 | any |
| 可执行命令 | `passing-the-hash`、`pth-curl`、`pth-net`、`pth-rpcclient`、`pth-smbclient`、`pth-smbget`、`pth-sqsh`、`pth-winexe`、`pth-wmic`、`pth-wmis` |
| 依赖 | `libc6`、`libcrypt1`、`libgmp10`、`libgnutls30t64`、`libgssapi-krb5-2`、`libhogweed6t64`、`libidn2-0`、`libldap2`、`libnettle8t64`、`librtmp1`、`libssl3t64`、`samba-common-bin` 等 |
| 安装体积 | 13.98 MB |
| 官网 | <http://passing-the-hash.blogspot.fr> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/passing-the-hash> |
| 包追踪 | <https://pkg.kali.org/pkg/passing-the-hash> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
passing-the-hash -h          # 查看用法
man passing-the-hash         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 10 个可执行命令，下面是官方页面内嵌的帮助原文。

### `pth-curl`

官方给出的调用示例：`pth-curl -h`

```text
root@kali:~# pth-curl -h
Usage: curl [options...] <url>
 -d, --data <data>           HTTP POST data
 -f, --fail                  Fail fast with no output on HTTP errors
 -h, --help <subject>        Get help for commands
 -o, --output <file>         Write to file instead of stdout
 -O, --remote-name           Write output to file named as remote file
 -i, --show-headers          Show response headers in output
 -s, --silent                Silent mode
 -T, --upload-file <file>    Transfer local FILE to destination
 -u, --user <user:password>  Server user and password
 -A, --user-agent <name>     Send User-Agent <name> to server
 -v, --verbose               Make the operation more talkative
 -V, --version               Show version number and quit
This is not the full help; this menu is split into categories.
Use "--help category" to get an overview of all categories, which are:
auth, connection, curl, deprecated, dns, file, ftp, global, http, imap, ldap,
output, pop3, post, proxy, scp, sftp, smtp, ssh, telnet, tftp, timeout, tls,
upload, verbose.
Use "--help all" to list all options
Use "--help [option]" to view documentation for a given option
```

### `pth-net`

官方给出的调用示例：`pth-net -h`

```text
root@kali:~# pth-net -h
Usage:
  Use 'net help rpc' to get more extensive information about 'net rpc' commands.
  Use 'net help rap' to get more extensive information about 'net rap' commands.
  Use 'net help ads' to get more extensive information about 'net ads' commands.
  Use 'net help file' to get more information about 'net file' commands.
  Use 'net help share' to get more information about 'net share' commands.
  Use 'net help session' to get more information about 'net session' commands.
  Use 'net help server' to get more information about 'net server' commands.
  Use 'net help domain' to get more information about 'net domain' commands.
  Use 'net help printq' to get more information about 'net printq' commands.
  Use 'net help user' to get more information about 'net user' commands.
  Use 'net help group' to get more information about 'net group' commands.
  Use 'net help groupmap' to get more information about 'net groupmap' commands.
  Use 'net help sam' to get more information about 'net sam' commands.
  Use 'net help validate' to get more information about 'net validate' commands.
  Use 'net help groupmember' to get more information about 'net groupmember' commands.
  Use 'net help admin' to get more information about 'net admin' commands.
  Use 'net help service' to get more information about 'net service' commands.
  Use 'net help password' to get more information about 'net password' commands.
  Use 'net help primarytrust' to get more extensive information about 'net primarytrust' commands.
  Use 'net help changetrustpw' to get more information about 'net changetrustpw'.
  net [options] changesecretpw
    Change the ADS domain member machine account password in secrets.tdb.
    Do NOT use this function unless you know what it does.
    Requires the -f flag to work.
  net -U user[%%password] [-W domain] setauthuser
    Set the auth user, password (and optionally domain
    Will prompt for password if not given.
  net setauthuser delete
    Delete the existing auth user settings.
  net getauthuser
    Get the current winbind auth user settings.
  Use 'net help time' to get more information about 'net time' commands.
  Use 'net help lookup' to get more information about 'net lookup' commands.
  Use 'net help g_lock' to get more information about 'net g_lock' commands.
  Use 'net help join' to get more information about 'net join'.
  Use 'net help offlinejoin' to get more information about 'net offlinejoin'.
  Use 'net help dom' to get more information about 'net dom' commands.
  Use 'net help cache' to get more information about 'net cache' commands.
  net getlocalsid
  net setlocalsid S-1-5-21-x-y-z
  net setdomainsid S-1-5-21-x-y-z
  net getdomainsid
  net maxrid
  Use 'net help idmap to get more information about 'net idmap' commands.
  Use 'net help status' to get more information about 'net status' commands.
  Use 'net help usershare to get more information about 'net usershare' commands.
  Use 'net help usersidlist' to get more information about 'net usersidlist'.
  Use 'net help conf' to get more information about 'net conf' commands.
  Use 'net help registry' to get more information about 'net registry' commands.
  Use 'net help eventlog' to get more information about 'net eventlog' commands.
  Use 'net help printing' to get more information about 'net printing' commands.
  Use 'net help serverid' to get more information about 'net serverid' commands.
  Use 'net help notify' to get more information about 'net notify' commands.
  Use 'net help tdb' to get more information about 'net tdb' commands.
  Use 'net help vfs' to get more information about 'net vfs' commands.
  Use 'net help witness' to get more information about 'net witness' commands.
  Use 'net help help' to list usage information for 'net' commands.
```

### `pth-rpcclient`

官方给出的调用示例：`pth-rpcclient --help`

```text
root@kali:~# pth-rpcclient --help
Usage: rpcclient [OPTION...] BINDING-STRING|HOST
Options:
  -c, --command=COMMANDS                       Execute semicolon separated cmds
  -I, --dest-ip=IP                             Specify destination IP address
  -p, --port=PORT                              Specify port number
Help options:
  -?, --help                                   Show this help message
      --usage                                  Display brief usage message
Common Samba options:
  -d, --debuglevel=DEBUGLEVEL                  Set debug level
      --debug-stdout                           Send debug output to standard
                                               output
  -s, --configfile=CONFIGFILE                  Use alternative configuration
                                               file
      --option=name=value                      Set smb.conf option from
                                               command line
  -l, --log-basename=LOGFILEBASE               Basename for log/debug files
      --leak-report                            enable talloc leak reporting on
                                               exit
      --leak-report-full                       enable full talloc leak
                                               reporting on exit
Connection options:
  -R, --name-resolve=NAME-RESOLVE-ORDER        Use these name resolution
                                               services only
  -O, --socket-options=SOCKETOPTIONS           socket options to use
  -m, --max-protocol=MAXPROTOCOL               Set max protocol level
  -n, --netbiosname=NETBIOSNAME                Primary netbios name
      --netbios-scope=SCOPE                    Use this Netbios scope
  -W, --workgroup=WORKGROUP                    Set the workgroup name
      --realm=REALM                            Set the realm name
Credential options:
  -U, --user=[DOMAIN/]USERNAME[%PASSWORD]      Set the network username
  -N, --no-pass                                Don't ask for a password
      --password=STRING                        Password
      --pw-nt-hash                             The supplied password is the NT
                                               hash
  -A, --authentication-file=FILE               Get the credentials from a file
  -P, --machine-pass                           Use stored machine account
                                               password
      --simple-bind-dn=DN                      DN to use for a simple bind
      --use-kerberos=desired|required|off      Use Kerberos authentication
      --use-krb5-ccache=CCACHE                 Credentials cache location for
                                               Kerberos
      --use-winbind-ccache                     Use the winbind ccache for
                                               authentication
      --client-protection=sign|encrypt|off     Configure used protection for
                                               client connections
Deprecated legacy options:
  -k, --kerberos                               DEPRECATED: Migrate to
                                               --use-kerberos
Version options:
  -V, --version                                Print version
```

### `pth-smbclient`

官方给出的调用示例：`pth-smbclient --help`

```text
root@kali:~# pth-smbclient --help
Usage: smbclient [OPTIONS] service <password>
  -M, --message=HOST                           Send message
  -I, --ip-address=IP                          Use this IP to connect to
  -E, --stderr                                 Write messages to stderr
                                               instead of stdout
  -L, --list=HOST                              Get a list of shares available
                                               on a host
  -T, --tar=<c|x>IXFvgbNan                     Command line tar
  -D, --directory=DIR                          Start from directory
  -c, --command=STRING                         Execute semicolon separated
                                               commands
  -b, --send-buffer=BYTES                      Changes the transmit/send buffer
  -t, --timeout=SECONDS                        Changes the per-operation
                                               timeout
  -p, --port=PORT                              Port to connect to
  -g, --grepable                               Produce grepable output
  -q, --quiet                                  Suppress help message
  -B, --browse                                 Browse SMB servers using DNS
Help options:
  -?, --help                                   Show this help message
      --usage                                  Display brief usage message
Common Samba options:
  -d, --debuglevel=DEBUGLEVEL                  Set debug level
      --debug-stdout                           Send debug output to standard
                                               output
  -s, --configfile=CONFIGFILE                  Use alternative configuration
                                               file
      --option=name=value                      Set smb.conf option from
                                               command line
  -l, --log-basename=LOGFILEBASE               Basename for log/debug files
      --leak-report                            enable talloc leak reporting on
                                               exit
      --leak-report-full                       enable full talloc leak
                                               reporting on exit
Connection options:
  -R, --name-resolve=NAME-RESOLVE-ORDER        Use these name resolution
                                               services only
  -O, --socket-options=SOCKETOPTIONS           socket options to use
  -m, --max-protocol=MAXPROTOCOL               Set max protocol level
  -n, --netbiosname=NETBIOSNAME                Primary netbios name
      --netbios-scope=SCOPE                    Use this Netbios scope
  -W, --workgroup=WORKGROUP                    Set the workgroup name
      --realm=REALM                            Set the realm name
Credential options:
  -U, --user=[DOMAIN/]USERNAME[%PASSWORD]      Set the network username
  -N, --no-pass                                Don't ask for a password
      --password=STRING                        Password
      --pw-nt-hash                             The supplied password is the NT
                                               hash
  -A, --authentication-file=FILE               Get the credentials from a file
  -P, --machine-pass                           Use stored machine account
                                               password
      --simple-bind-dn=DN                      DN to use for a simple bind
      --use-kerberos=desired|required|off      Use Kerberos authentication
      --use-krb5-ccache=CCACHE                 Credentials cache location for
                                               Kerberos
      --use-winbind-ccache                     Use the winbind ccache for
                                               authentication
      --client-protection=sign|encrypt|off     Configure used protection for
                                               client connections
Deprecated legacy options:
  -k, --kerberos                               DEPRECATED: Migrate to
                                               --use-kerberos
Version options:
  -V, --version                                Print version
```

### `pth-smbget`

官方给出的调用示例：`pth-smbget --help`

```text
root@kali:~# pth-smbget --help
Usage: smbget [OPTION...]
  -a, --guest                                  Work as user guest
  -e, --encrypt                                Encrypt SMB transport
  -r, --resume                                 Automatically resume aborted
                                               files
  -u, --update                                 Download only when remote file
                                               is newer than local file or
                                               local file is missing
      --recursive                              Recursively download files
  -b, --blocksize=INT                          Change number of bytes in a
                                               block
  -o, --outputfile=STRING                      Write downloaded data to
                                               specified file
      --stdout                                 Write data to stdout
  -D, --dots                                   Show dots as progress indication
  -q, --quiet                                  Be quiet
  -v, --verbose                                Be verbose
      --limit-rate=INT                         Limit download speed to this
                                               many KB/s
Help options:
  -?, --help                                   Show this help message
      --usage                                  Display brief usage message
Common Samba options:
  -d, --debuglevel=DEBUGLEVEL                  Set debug level
      --debug-stdout                           Send debug output to standard
                                               output
  -s, --configfile=CONFIGFILE                  Use alternative configuration
                                               file
      --option=name=value                      Set smb.conf option from
                                               command line
  -l, --log-basename=LOGFILEBASE               Basename for log/debug files
      --leak-report                            enable talloc leak reporting on
                                               exit
      --leak-report-full                       enable full talloc leak
                                               reporting on exit
Connection options:
  -R, --name-resolve=NAME-RESOLVE-ORDER        Use these name resolution
                                               services only
  -O, --socket-options=SOCKETOPTIONS           socket options to use
  -m, --max-protocol=MAXPROTOCOL               Set max protocol level
  -n, --netbiosname=NETBIOSNAME                Primary netbios name
      --netbios-scope=SCOPE                    Use this Netbios scope
  -W, --workgroup=WORKGROUP                    Set the workgroup name
      --realm=REALM                            Set the realm name
Credential options:
  -U, --user=[DOMAIN/]USERNAME[%PASSWORD]      Set the network username
  -N, --no-pass                                Don't ask for a password
      --password=STRING                        Password
      --pw-nt-hash                             The supplied password is the NT
                                               hash
  -A, --authentication-file=FILE               Get the credentials from a file
  -P, --machine-pass                           Use stored machine account
                                               password
      --simple-bind-dn=DN                      DN to use for a simple bind
      --use-kerberos=desired|required|off      Use Kerberos authentication
      --use-krb5-ccache=CCACHE                 Credentials cache location for
                                               Kerberos
      --use-winbind-ccache                     Use the winbind ccache for
                                               authentication
      --client-protection=sign|encrypt|off     Configure used protection for
                                               client connections
Deprecated legacy options:
  -k, --kerberos                               DEPRECATED: Migrate to
                                               --use-kerberos
Version options:
  -V, --version                                Print version
```

### `pth-sqsh`

官方给出的调用示例：`pth-sqsh --help`

```text
root@kali:~# pth-sqsh --help
Use: sqsh [-a count] [-A packet_size] [-b] [-B] [-c [cmdend]] [-C sql]
          [-d severity] [-D database] [-e] [-E editor] [-f severity]
          [-G TDS version] [-h] [-H hostname] [-i filename] [-I interfaces]
          [-J charset] [-k keywords] [-K keytab] [-l level|flags]
          [-L var=value] [-m style] [-n {on|off}] [-N appname] [-o filename]
          [-p] [-P [password]] [-Q query_timeout] [-r [sqshrc]]
          [-R principal] [-s colsep] [-S server] [-t [filter]]
          [-T login_timeout] [-U username] [-v] [-V [bcdimoqru]] [-w width]
          [-X] [-y directory] [-z language] [-Z [secmech]]
          [--appname        appname] [--clientapplname clientapplname]
          [--clienthostname clienthostname] [--clientname     clientname]
          [--hostname       hostname] [--help          ] [--version       ]
 -a  Max. # of errors before abort       -p  Display performance stats
 -A  Adjust TDS packet size              -P  Sybase password (NULL)
 -b  Suppress banner message on startup  -Q  Query timeout period in seconds
 -B  Turn off file buffering on startup  -r  Specify name of .sqshrc
 -c  Alias for the 'go' command          -R  Network security server principal
 -C  Send sql statement to server        -s  Alternate column separator (\t)
 -d  Min. severity level to display      -S  Name of Sybase server ($DSQUERY)
 -D  Change database context on startup  -t  Filter batches through program
 -e  Echo batch prior to executing       -T  Login timeout period in seconds
 -E  Replace default editor (vi)         -U  Name of Sybase user
 -f  Min. severity level for failure     -v  Display current version and exit
 -G  TDS version to use                  -V  Request network security services
 -h  Disable headers and footers         -w  Adjust result display width
 -H  Set the client hostname             -X  Enable client password encryption
 -i  Read input from file                -y  Override value of $SYBASE
 -I  Alternate interfaces file           -z  Alternate display language
 -J  Client character set                -Z  Network security mechanism
 -k  Specify alternate keywords file     --appname         Set application name
 -K  Network security keytab file (DCE)  --clientapplname  Set client appl name
 -l  Set debugging level                 --clienthostname  Set client host name
 -L  Set the value of a given variable   --clientname      Set client name
 -m  Set display mode                    --hostname        Set hostname
 -n  Set chained transaction mode        --help            Show help text only
 -N  Set application name (sqsh-3.0)     --version         Show version only
 -o  Direct all output to file
```

### `pth-winexe`

官方给出的调用示例：`pth-winexe --help`

```text
root@kali:~# pth-winexe --help
Usage: winexe [OPTION]... //HOST[:PORT] COMMAND
Options:
      --uninstall                              Uninstall winexe service after
                                               remote execution
      --reinstall                              Reinstall winexe service before
                                               remote execution
      --runas=[DOMAIN\]USERNAME%PASSWORD       Run as the given user (BEWARE:
                                               this password is sent in
                                               cleartext over the network!)
      --runas-file=FILE                        Run as user options defined in
                                               a file
      --interactive=0|1                        Desktop interaction: 0 -
                                               disallow, 1 - allow. If allow,
                                               also use the --system switch
                                               (Windows requirement). Vista
                                               does not support this option.
      --ostype=0|1|2                           OS type: 0 - 32-bit, 1 -
                                               64-bit, 2 - winexe will decide.
                                               Determines which version
                                               (32-bit or 64-bit) of service
                                               will be installed.
Help options:
  -?, --help                                   Show this help message
      --usage                                  Display brief usage message
Common Samba options:
  -d, --debuglevel=DEBUGLEVEL                  Set debug level
      --debug-stdout                           Send debug output to standard
                                               output
  -s, --configfile=CONFIGFILE                  Use alternative configuration
                                               file
      --option=name=value                      Set smb.conf option from
                                               command line
  -l, --log-basename=LOGFILEBASE               Basename for log/debug files
      --leak-report                            enable talloc leak reporting on
                                               exit
      --leak-report-full                       enable full talloc leak
                                               reporting on exit
Credential options:
  -U, --user=[DOMAIN/]USERNAME[%PASSWORD]      Set the network username
  -N, --no-pass                                Don't ask for a password
      --password=STRING                        Password
      --pw-nt-hash                             The supplied password is the NT
                                               hash
  -A, --authentication-file=FILE               Get the credentials from a file
  -P, --machine-pass                           Use stored machine account
                                               password
      --simple-bind-dn=DN                      DN to use for a simple bind
      --use-kerberos=desired|required|off      Use Kerberos authentication
      --use-krb5-ccache=CCACHE                 Credentials cache location for
                                               Kerberos
      --use-winbind-ccache                     Use the winbind ccache for
                                               authentication
      --client-protection=sign|encrypt|off     Configure used protection for
                                               client connections
Version options:
  -V, --version                                Print version
```

### `pth-wmic`

官方给出的调用示例：`pth-wmic --help`

```text
root@kali:~# pth-wmic --help
Usage: //host query
Example: wmic -U [domain/]adminuser%password //host "select * from Win32_ComputerSystem"
  --namespace=STRING                          WMI namespace, default to
                                              root\cimv2
  --delimiter=STRING                          delimiter to use when querying
                                              multiple values, default to '|'
Help options:
  -?, --help                                  Show this help message
  --usage                                     Display brief usage message
Common samba options:
  -d, --debuglevel=DEBUGLEVEL                 Set debug level
  --debug-stderr                              Send debug output to STDERR
  -s, --configfile=CONFIGFILE                 Use alternative configuration
                                              file
  --option=name=value                         Set smb.conf option from command
                                              line
  -l, --log-basename=LOGFILEBASE              Basename for log/debug files
  --leak-report                               enable talloc leak reporting on
                                              exit
  --leak-report-full                          enable full talloc leak
                                              reporting on exit
Connection options:
  -R, --name-resolve=NAME-RESOLVE-ORDER       Use these name resolution
                                              services only
  -O, --socket-options=SOCKETOPTIONS          socket options to use
  -n, --netbiosname=NETBIOSNAME               Primary netbios name
  -W, --workgroup=WORKGROUP                   Set the workgroup name
  --realm=REALM                               Set the realm name
  -i, --scope=SCOPE                           Use this Netbios scope
  -m, --maxprotocol=MAXPROTOCOL               Set max protocol level
Authentication options:
  -U, --user=[DOMAIN\]USERNAME[%PASSWORD]     Set the network username
  -N, --no-pass                               Don't ask for a password
  --password=STRING                           Password
  -A, --authentication-file=FILE              Get the credentials from a file
  -S, --signing=on|off|required               Set the client signing state
  -P, --machine-pass                          Use stored machine account
                                              password (implies -k)
  --simple-bind-dn=STRING                     DN to use for a simple bind
  -k, --kerberos=STRING                       Use Kerberos
  --use-security-mechanisms=STRING            Restricted list of
                                              authentication mechanisms
                                              available for use with this
                                              authentication
Common samba options:
  -V, --version                               Print version
```

### `pth-wmis`

官方给出的调用示例：`pth-wmis --help`

```text
root@kali:~# pth-wmis --help
Usage: //host
Example: wmis -U [domain/]adminuser%password //host cmd.exe /c dir c:\ > c:\windows\temp\output.txt
Help options:
  -?, --help                                  Show this help message
  --usage                                     Display brief usage message
Common samba options:
  -d, --debuglevel=DEBUGLEVEL                 Set debug level
  --debug-stderr                              Send debug output to STDERR
  -s, --configfile=CONFIGFILE                 Use alternative configuration
                                              file
  --option=name=value                         Set smb.conf option from command
                                              line
  -l, --log-basename=LOGFILEBASE              Basename for log/debug files
  --leak-report                               enable talloc leak reporting on
                                              exit
  --leak-report-full                          enable full talloc leak
                                              reporting on exit
Connection options:
  -R, --name-resolve=NAME-RESOLVE-ORDER       Use these name resolution
                                              services only
  -O, --socket-options=SOCKETOPTIONS          socket options to use
  -n, --netbiosname=NETBIOSNAME               Primary netbios name
  -W, --workgroup=WORKGROUP                   Set the workgroup name
  --realm=REALM                               Set the realm name
  -i, --scope=SCOPE                           Use this Netbios scope
  -m, --maxprotocol=MAXPROTOCOL               Set max protocol level
Authentication options:
  -U, --user=[DOMAIN\]USERNAME[%PASSWORD]     Set the network username
  -N, --no-pass                               Don't ask for a password
  --password=STRING                           Password
  -A, --authentication-file=FILE              Get the credentials from a file
  -S, --signing=on|off|required               Set the client signing state
  -P, --machine-pass                          Use stored machine account
                                              password (implies -k)
  --simple-bind-dn=STRING                     DN to use for a simple bind
  -k, --kerberos=STRING                       Use Kerberos
  --use-security-mechanisms=STRING            Restricted list of
                                              authentication mechanisms
                                              available for use with this
                                              authentication
Common samba options:
  -V, --version                               Print version
Updated on: 2025-Dec-09
 Edit this page
passdetective
payloadsallthethings
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install passing-the-hash`，再执行 `passing-the-hash --version` 2>/dev/null || `passing-the-hash -V`
- [ ] **2.** **读官方帮助** —— `passing-the-hash -h`，需要细节时 `man passing-the-hash`
- [ ] **3.** **在自有靶场跑最小用例** —— 官方给出的调用形式是：`Usage: curl [options...] <url>`
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/passing-the-hash/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/defense-evasion.md`](../../tools/by-attack/defense-evasion.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/passing-the-hash/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/passing-the-hash/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
