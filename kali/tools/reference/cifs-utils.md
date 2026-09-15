# cifs-utils

> Common Internet File System utilities The SMB/CIFS protocol provides support for cross-platform file sharing with Microsoft Windows, OS X, and other Unix systems. This package provides utilities for managing mounts of CIFS network file sys…

> **功能分类**：通用工具 ｜ **Kali 包**：`cifs-utils` ｜ **官方文档**：<https://www.kali.org/tools/cifs-utils/>

## 1. 安装

```bash
sudo apt update
sudo apt install cifs-utils
```

| 项目 | 内容 |
|------|------|
| 版本 | 7.4 |
| 架构 | linux-any |
| 可执行命令 | `cifs-utils`、`cifs.idmap`、`cifs.upcall`、`cifscreds`、`getcifsacl`、`mount.cifs`、`mount.smb3`、`setcifsacl`、`smb2-quota`、`smbinfo` |
| 依赖 | `libc6`、`libcap-ng0`、`libgssapi-krb5-2`、`libkeyutils1`、`libkrb5-3`、`libpam0g`、`libtalloc2`、`libwbclient0`、`python3`、`cifs.idmap` |
| 安装体积 | 351 KB |
| 官网 | <https://wiki.samba.org/index.php/LinuxCIFS_utils> |
| 源码仓库 | <https://salsa.debian.org/samba-team/cifs-utils> |
| 包追踪 | <https://pkg.kali.org/pkg/cifs-utils> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
cifs-utils -h          # 查看用法
man cifs-utils         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 10 个可执行命令，下面是官方页面内嵌的帮助原文。

### `cifs.idmap`

官方给出的调用示例：`cifs.idmap -h`

```text
root@kali:~# cifs.idmap -h
Usage: cifs.idmap [-h] [-v] [-t timeout] key_serial
```

### `man`

官方给出的调用示例：`man cifs.upcall`

```text
root@kali:~# man cifs.upcall
CIFS.UPCALL(8)              System Manager's Manual              CIFS.UPCALL(8)
NAME
     cifs.upcall  -  Userspace  upcall  helper  for Common Internet File System
     (CIFS)
SYNOPSIS
        cifs.upcall [--trust-dns|-t] [--version|-v] [--legacy-uid|-l]
               [--krb5conf=/path/to/krb5.conf|-k            /path/to/krb5.conf]
               [--keytab=/path/to/keytab|-K    /path/to/keytab]    [--expire|-e
               nsecs] {keyid}
DESCRIPTION
     This tool is part of the cifs-utils suite.
     cifs.upcall is a userspace  helper  program  for  the  linux  CIFS  client
     filesystem. There are a number of activities that the kernel cannot easily
     do  itself.  This  program is a callout program that does these things for
     the kernel and then returns the result.
     cifs.upcall is generally intended to be run  when  the  kernel  calls  re-
     quest-key(8)  for a particular key type. While it can be run directly from
     the command-line, it's not generally intended to be run that way.
OPTIONS
     -c     This option is deprecated and is currently ignored.
     --no-env-probe|-E
            Normally, cifs.upcall will probe the environment variable space  of
            the  process  that initiated the upcall in order to fetch the value
            of $KRB5CCNAME. This can assist the program with finding credential
            caches in non-default locations. If this option is  set,  then  the
            program  won't  do  this and will rely on finding credcaches in the
            default locations specified in krb5.conf. Note that this  is  never
            performed  when the uid is 0. The default credcache location is al-
            ways used when the uid is 0, regardless of the environment variable
            setting in the process.
     --krb5conf|-k=/path/to/krb5.conf
            This option allows administrators to set an alternate location  for
            the krb5.conf file that cifs.upcall will use.
     --keytab=|-K=/path/to/keytab
            This  option  allows  administrators to specify a keytab file to be
            used. When a user has  no  credential  cache  already  established,
            cifs.upcall  will  attempt  to use this keytab to acquire them. The
            default is the system-wide keytab /etc/krb5.keytab.
     --trust-dns|-t
            With krb5 upcalls, the name used as the host portion of the service
            principal defaults to the hostname portion of the UNC. This  option
            allows the upcall program to reverse resolve the network address of
            the server in order to get the hostname.
            This  is less secure than not trusting DNS. When using this option,
            it's possible that an attacker could get control of DNS  and  trick
            the  client  into  mounting  a  different  server  altogether. It's
            preferable to instead add server principals to the  KDC  for  every
            possible  hostname,  but  this  option  exists for cases where that
            isn't possible. The  default  is  to  not  trust  reverse  hostname
            lookups in this fashion.
     --legacy-uid|-l
            Traditionally,  the kernel has sent only a single uid= parameter to
            the upcall for the SPNEGO upcall  that's  used  to  determine  what
            user's  credential cache to use.  This parameter is affected by the
            uid= mount option, which also governs the ownership of files on the
            mount.
            Newer kernels send a creduid= option as well, which  contains  what
            uid  it thinks actually owns the credentials that it's looking for.
            At mount time, this is generally set to the real uid  of  the  user
            doing  the mount. For multisession mounts, it's set to the fsuid of
            the mount user. Set this option if you want cifs.upcall to use  the
            older uid= parameter instead of the creduid= parameter.
     --expire|-e
            Override default timeout value (600 seconds) for dns_resolver key.
     --version|-v
            Print version number and exit.
ENVIRONMENT VARIABLES
     GSS_USE_PROXY="yes"
            Enable  usage  of  gssproxy for credential retrieval. This includes
            keytab based client initiation as well  as  (Resource  Based)  Con-
            strained Delegation.  See gssproxy-mech(8).
CONFIGURATION FOR KEYCTL
     cifs.upcall  is  designed to be called from the kernel via the request-key
     callout program. This requires that request-key be told where and  how  to
     call  this program.  The current cifs.upcall program handles two different
     key types:
     cifs.spnego
            This keytype is for retrieving kerberos session keys
     dns_resolver
            This key type is for resolving hostnames into IP addresses. Support
            for this key type may eventually be deprecated (see below).
            To make this program useful for CIFS, you'll need to set up entries
            for them in request-key.conf(5). Here's an example of an entry  for
            each key type:
               #OPERATION  TYPE           D C PROGRAM ARG1 ARG2...
               #=========  =============  = = ================================
               create      cifs.spnego    * * /usr/sbin/cifs.upcall %k
               create      dns_resolver   * * /usr/sbin/cifs.upcall %k
            See request-key.conf(5) for more info on each field.
            The keyutils package has also started including a dns_resolver han-
            dling  program  as  well that is preferred over the one in cifs.up-
            call. If you are using a keyutils version equal to or greater  than
            1.5,  you  should  use  key.dns_resolver to handle the dns_resolver
            keytype instead of cifs.upcall. See  key.dns_resolver(8)  for  more
            info.
SEE ALSO
     request-key.conf(5), mount.cifs(8), key.dns_resolver(8)
AUTHOR
     Igor Mammedov wrote the cifs.upcall program.
     Jeff Layton authored this manpage.
     The maintainer of the Linux CIFS VFS is Steve French.
     The  Linux  CIFS  Mailing list is the preferred place to ask questions re-
     garding these programs.
                                                                 CIFS.UPCALL(8)
```

### `cifscreds`

官方给出的调用示例：`cifscreds -h`

```text
root@kali:~# cifscreds -h
cifscreds: invalid option -- 'h'
Usage:
	cifscreds add [-u username] [-d] <host|domain> [-t timeout]
	cifscreds clear [-u username] [-d] <host|domain>
	cifscreds clearall
	cifscreds update [-u username] [-d] <host|domain>
```

### `getcifsacl`

官方给出的调用示例：`getcifsacl --help`

```text
root@kali:~# getcifsacl --help
getcifsacl: invalid option -- '-'
getcifsacl: Display CIFS/NTFS ACL in a security descriptor of a file object
Usage: getcifsacl [option] <file_name1> [<file_name2>,<file_name3>,...]
Valid options:
	-h	Display this help text
	-v	Version of the program
	-R 	recurse into subdirectories
	-r	Display raw values of the ACE fields
Refer to getcifsacl(1) manpage for details
```

### `mount.cifs`

官方给出的调用示例：`mount.cifs -h`

```text
root@kali:~# mount.cifs -h
Usage:  mount.cifs <remotetarget> <dir> -o <options>
Mount the remote target, specified as a UNC name, to a local directory.
Options:
	user=<arg>
	pass=<arg>
	dom=<arg>
Less commonly used options:
	credentials=<filename>,guest,perm,noperm,setuids,nosetuids,rw,ro,
	sep=<char>,iocharset=<codepage>,suid,nosuid,exec,noexec,serverino,
	noserverino,mapchars,nomapchars,nolock,servernetbiosname=<SRV_RFC1001NAME>
	cache=<strict|none|loose>,nounix,cifsacl,sec=<authentication mechanism>,
	sign,seal,fsc,snapshot=<token|time>,nosharesock,persistenthandles,
	resilienthandles,rdma,vers=<smb_dialect>,cruid,password2=<alt password>
Options not needed for servers supporting CIFS Unix extensions
	(e.g. unneeded for mounts to most Samba versions):
	uid=<uid>,gid=<gid>,dir_mode=<mode>,file_mode=<mode>,sfu,
	mfsymlinks,idsfromsid
Rarely used options:
	port=<tcpport>,rsize=<size>,wsize=<size>,unc=<unc_name>,ip=<ip_address>,
	dev,nodev,nouser_xattr,netbiosname=<OUR_RFC1001NAME>,hard,soft,intr,
	nointr,ignorecase,noposixpaths,noacl,prefixpath=<path>,nobrl,
	echo_interval=<seconds>,actimeo=<seconds>,max_credits=<credits>,
	bsize=<size>
Options are described in more detail in the manual page
	man 8 mount.cifs
To display the version number of the mount helper:
	mount.cifs -V
```

### `mount.smb3`

官方给出的调用示例：`mount.smb3 -h`

```text
root@kali:~# mount.smb3 -h
Usage:  mount.smb3 <remotetarget> <dir> -o <options>
Mount the remote target, specified as a UNC name, to a local directory.
Options:
	user=<arg>
	pass=<arg>
	dom=<arg>
Less commonly used options:
	credentials=<filename>,guest,perm,noperm,setuids,nosetuids,rw,ro,
	sep=<char>,iocharset=<codepage>,suid,nosuid,exec,noexec,serverino,
	noserverino,mapchars,nomapchars,nolock,servernetbiosname=<SRV_RFC1001NAME>
	cache=<strict|none|loose>,nounix,cifsacl,sec=<authentication mechanism>,
	sign,seal,fsc,snapshot=<token|time>,nosharesock,persistenthandles,
	resilienthandles,rdma,vers=<smb_dialect>,cruid,password2=<alt password>
Options not needed for servers supporting CIFS Unix extensions
	(e.g. unneeded for mounts to most Samba versions):
	uid=<uid>,gid=<gid>,dir_mode=<mode>,file_mode=<mode>,sfu,
	mfsymlinks,idsfromsid
Rarely used options:
	port=<tcpport>,rsize=<size>,wsize=<size>,unc=<unc_name>,ip=<ip_address>,
	dev,nodev,nouser_xattr,netbiosname=<OUR_RFC1001NAME>,hard,soft,intr,
	nointr,ignorecase,noposixpaths,noacl,prefixpath=<path>,nobrl,
	echo_interval=<seconds>,actimeo=<seconds>,max_credits=<credits>,
	bsize=<size>
Options are described in more detail in the manual page
	man 8 mount.smb3
To display the version number of the mount helper:
	mount.smb3 -V
```

### `setcifsacl`

官方给出的调用示例：`setcifsacl -h`

```text
root@kali:~# setcifsacl -h
setcifsacl: Alter components of CIFS/NTFS security descriptor of a file object
Usage: setcifsacl option [<list_of_ACEs>|<SID>] <file_name>
Valid options:
	-v	Version of the program
	-U	Used in combination with -a, -D, -M, -S in order to
		apply the actions to SALC (aUdit ACL); if not specified,
		the actions apply to DACL
	-a	Add ACE(s), separated by a comma, to an ACL
	setcifsacl -a "ACL:Administrator:ALLOWED/0x0/FULL" <file_name>
	-A	Add ACE(s) and reorder, separated by a comma, to an ACL
	setcifsacl -A "ACL:Administrator:ALLOWED/0x0/FULL" <file_name>
	-D	Delete ACE(s), separated by a comma, from an ACL
	setcifsacl -D "ACL:Administrator:DENIED/0x0/D" <file_name>
	-M	Modify ACE(s), separated by a comma, in an ACL
	setcifsacl -M "ACL:user1:ALLOWED/0x0/0x1e01ff" <file_name>
	-S	Replace existing ACL with ACE(s), separated by a comma
	setcifsacl -S "ACL:Administrator:ALLOWED/0x0/D" <file_name>
	-o	Set owner using specified SID (name or raw format)
	setcifsacl -o "Administrator" <file_name>
	-g	Set group using specified SID (name or raw format)
	setcifsacl -g "Administrators" <file_name>
Refer to setcifsacl(1) manpage for details
```

### `smb2-quota`

官方给出的调用示例：`smb2-quota -h`

```text
root@kali:~# smb2-quota -h
usage: smb2-quota [-h] [-t] [-c] [-l] <filename>
Please specify an action to perform.
positional arguments:
  <filename>     filename on a share
options:
  -h, --help     show this help message and exit
  -t, --tabular  print quota information in tabular format
  -c, --csv      print quota information in csv format
  -l, --list     print quota information in list format
```

### `smbinfo`

官方给出的调用示例：`smbinfo -h`

```text
root@kali:~# smbinfo -h
usage: smbinfo [-h] [-V]
               {fileaccessinfo,filealigninfo,fileallinfo,filebasicinfo,fileeainfo,filefsfullsizeinfo,fileinternalinfo,filemodeinfo,filepositioninfo,filestandardinfo,filestreaminfo,fsctl-getobjid,getcompression,setcompression,list-snapshots,quota,secdesc,keys,gettconinfo} ...
Display SMB-specific file information using cifs IOCTL
positional arguments:
  {fileaccessinfo,filealigninfo,fileallinfo,filebasicinfo,fileeainfo,filefsfullsizeinfo,fileinternalinfo,filemodeinfo,filepositioninfo,filestandardinfo,filestreaminfo,fsctl-getobjid,getcompression,setcompression,list-snapshots,quota,secdesc,keys,gettconinfo}
                        sub-commands help
    fileaccessinfo      Prints FileAccessInfo for a cifs file
    filealigninfo       Prints FileAlignInfo for a cifs file
    fileallinfo         Prints FileAllInfo for a cifs file
    filebasicinfo       Prints FileBasicInfo for a cifs file
    fileeainfo          Prints FileEAInfo for a cifs file
    filefsfullsizeinfo  Prints FileFsFullSizeInfo for a cifs file
    fileinternalinfo    Prints FileInternalInfo for a cifs file
    filemodeinfo        Prints FileModeInfo for a cifs file
    filepositioninfo    Prints FilePositionInfo for a cifs file
    filestandardinfo    Prints FileStandardInfo for a cifs file
    filestreaminfo      Prints FileStreamInfo for a cifs file
    fsctl-getobjid      Prints the objectid of the file and GUID of the
                        underlying volume.
    getcompression      Prints the compression setting for the file
    setcompression      Sets the compression level for the file
    list-snapshots      List the previous versions of the volume that backs
                        this file
    quota               Prints the quota for a cifs file
    secdesc             Prints the security descriptor for a cifs file
    keys                Prints the decryption information needed to view
                        encrypted network traces
    gettconinfo         Prints TCON Id and Session Id for a cifs file
options:
  -h, --help            show this help message and exit
  -V, --verbose         verbose output
Updated on: 2026-May-25
 Edit this page
chntpw
command-not-found
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install cifs-utils`，再执行 `cifs-utils --version` 2>/dev/null || `cifs-utils -V`
- [ ] **2.** **读官方帮助** —— `cifs-utils -h`，需要细节时 `man cifs-utils`
- [ ] **3.** **在自有靶场跑最小用例** —— 官方给出的调用形式是：`Usage: cifs.idmap [-h] [-v] [-t timeout] key_serial`
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/cifs-utils/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- **精讲教程**（含原理、参数详解、靶场实操与输出解读）：[set](../../tools/tutorials/11-社会工程与报告/set.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/cifs-utils/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/cifs-utils/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
