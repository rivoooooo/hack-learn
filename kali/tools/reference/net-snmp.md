# net-snmp

> SNMP (Simple Network Management Protocol) trap library The Simple Network Management Protocol (SNMP) provides a framework for the exchange of management information between agents (servers) and clients. The Net-SNMP trap library contains f…

> **功能分类**：信息搜集 ｜ **Kali 包**：`net-snmp` ｜ **官方文档**：<https://www.kali.org/tools/net-snmp/>

## 1. 安装

```bash
sudo apt update
sudo apt install libnetsnmptrapd45
```

| 项目 | 内容 |
|------|------|
| 版本 | 5.9.5.2 |
| 架构 | any |
| 可执行命令 | `libnetsnmptrapd45`、`libsnmp-base`、`libsnmp-dev`、`mib2c`、`mib2c-update`、`net-snmp-config`、`libsnmp-perl`、`libsnmp45`、`snmp`、`agentxtrap`、`encode_keychange`、`fixproc`、`snmp-bridge-mib`、`snmpbulkget`、`snmpbulkwalk`、`snmpcheck`、`snmpconf`、`snmpdelta`、`snmpdf`、`snmpget`、`snmpgetnext`、`snmpinform`、`snmpnetstat`、`snmpping`、`snmpps`、`snmpset`、`snmpstatus`、`snmptable`、`snmptest`、`snmptls`、`snmptranslate`、`snmptrap`、`snmpusm`、`snmpvacm`、`snmpwalk`、`snmpd`、`net-snmp-create-v3-user`、`snmptrapd`、`traptoemail`、`tkmib` |
| 依赖 | `libc6`、`libmariadb3`、`libsnmp-base`、`libsnmp45`、`libsnmp-base` |
| 安装体积 | 74 KB |
| 官网 | <https://net-snmp.sourceforge.net/> |
| 源码仓库 | <https://salsa.debian.org/debian/net-snmp> |
| 包追踪 | <https://pkg.kali.org/pkg/net-snmp> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
libnetsnmptrapd45 -h          # 查看用法
man libnetsnmptrapd45         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 40 个可执行命令，下面是官方页面内嵌的帮助原文。

### `mib2c`

> 官方示例调用：`mib2c -h`

```text
root@kali:~# mib2c -h
/usr/bin/mib2c [-h] [-c configfile] [-f prefix] mibNode
  -h		This message.
  -c configfile	Specifies the configuration file to use
		that dictates what the output of mib2c will look like.
  -I PATH	Specifies a path to look for configuration files in
  -f prefix	Specifies the output prefix to use.  All code
		will be put into prefix.c and prefix.h
  -d		debugging output (don't do it.  trust me.)
  -S VAR=VAL	Set $VAR variable to $VAL
  -i		Don't run indent on the resulting code
  -s		Don't look for mibNode.sed and run sed on the resulting code
  mibNode	The name of the top level mib node you want to
		generate code for.  By default, the code will be stored in
		mibNode.c and mibNode.h (use the -f flag to change this)
```

### `mib2c-update`

> 官方示例调用：`mib2c-update -h`

```text
root@kali:~# mib2c-update -h
Starting regneration of ipAddressTable using mib2c.mfd.conf at 2026-09-14_07.10
Creating patch for your custom code
   no custom code!
mib2c -h -c mib2c.mfd.conf  ipAddressTable
/usr/bin/mib2c [-h] [-c configfile] [-f prefix] mibNode
  -h		This message.
  -c configfile	Specifies the configuration file to use
		that dictates what the output of mib2c will look like.
  -I PATH	Specifies a path to look for configuration files in
  -f prefix	Specifies the output prefix to use.  All code
		will be put into prefix.c and prefix.h
  -d		debugging output (don't do it.  trust me.)
  -S VAR=VAL	Set $VAR variable to $VAL
  -i		Don't run indent on the resulting code
  -s		Don't look for mibNode.sed and run sed on the resulting code
  mibNode	The name of the top level mib node you want to
		generate code for.  By default, the code will be stored in
		mibNode.c and mibNode.h (use the -f flag to change this)
```

### `net-snmp-config`

> 官方示例调用：`net-snmp-config -h`

```text
root@kali:~# net-snmp-config -h
unknown option -h
Usage:
  net-snmp-config [--cflags] [--agent-libs] [--libs] [--version]
                  ... [see below for complete flag list]
    --version         displays the net-snmp version number
    --indent-options  displays the indent options from the Coding Style
    --debug-tokens    displays a example command line to search to source
                      code for a list of available debug tokens
  SNMP Setup commands:
    --create-snmpv3-user creates a SNMPv3 user in Net-SNMP config file.
                         See net-snmp-create-v3-user --help for list of
                         accepted options.
  These options produce the various compilation flags needed when
  building external SNMP applications:
    --base-lib-cflags lists additional compilation flags needed for linking
                      against libsnmp
    --base-cflags     lists additional compilation flags needed
    --cflags          lists additional compilation flags needed
                      (includes -I. and extra developer warning flags)
  These options produce the various link flags needed when
  building external SNMP applications:
    --libs            lists libraries needed for building applications
    --agent-libs      lists libraries needed for building subagents
  These options produce various link flags broken down into parts.
  (Most of the time the simple options above should be used.)
    --libdir              path to netsnmp libraries
    --base-agent-libs     netsnmp specific agent libraries
    --netsnmp-libs        netsnmp specific libraries (with path)
    --netsnmp-agent-libs  netsnmp specific agent libraries (with path)
    --ldflags             link flags for external libraries
    --external-libs       external libraries needed by netsnmp libs
    --external-agent-libs external libraries needed by netsnmp agent libs
  These options produce various link flags used when linking an
  external application against an uninstalled build directory.
    --build-includes      include path to build/source includes
    --build-lib-dirs      link path to libraries
    --build-lib-deps      path to libraries for dependency target
    --build-command       command to compile $3... to $2
  Automated subagent building (produces an OUTPUTNAME binary file):
  [this feature has not been tested very well yet.  use at your risk.]
    --compile-subagent OUTPUTNAME [--norm] [--cflags flags]
                                  [--ldflags flags] mibmodule1.c [...]]
         --norm           leave the generated .c file around to read.
         --cflags flags   extra cflags to use (e.g. -I...).
         --ldflags flags  extra ld flags to use (e.g. -L... -l...).
  Details on how the net-snmp package was compiled:
    --configure-options   display original configure arguments
    --prefix              display the installation prefix
    --snmpd-module-list   display the modules compiled into the agent
    --default-mibs        display default list of MIBs
    --default-mibdirs     display default list of MIB directories
    --snmpconfpath        display default SNMPCONFPATH
    --persistent-directory display default persistent directory
    --perlprog            display path to perl for the perl modules
```

### `agentxtrap`

> 官方示例调用：`agentxtrap -h`

```text
root@kali:~# agentxtrap -h
USAGE: agentxtrap [OPTIONS] TRAP-PARAMETERS
  Version:  5.9.5.2
  Web:      http://www.net-snmp.org/
  Email:
[email protected]
OPTIONS:
  -h			display this help message
  -V			display package version number
  -m MIB[:...]		load given list of MIBs (ALL loads everything)
  -M DIR[:...]		look in given list of directories for MIBs
  -D[TOKEN[,...]]	turn on debugging output for the specified TOKENs
			   (ALL gives extremely verbose debugging output)
  -d			dump all traffic
  -P MIBOPTS		Toggle various defaults controlling mib parsing:
			  u:  allow the use of underlines in MIB symbols
			  c:  disallow the use of "--" to terminate comments
			  d:  save the DESCRIPTIONs of the MIB objects
			  e:  disable errors when MIB symbols conflict
			  w:  enable warnings when MIB symbols conflict
			  W:  enable detailed warnings when MIB symbols conflict
			  R:  replace MIB symbols from latest module
  -L LOGOPTS		Toggle various defaults controlling logging:
			  e:           log to standard error
			  o:           log to standard output
			  n:           don't log at all
			  f file:      log to the specified file
			  s facility:  log to syslog (via the specified facility)
			  (variants)
			  [EON] pri:   log to standard error, output or /dev/null for level 'pri' and above
			  [EON] p1-p2: log to standard error, output or /dev/null for levels 'p1' to 'p2'
			  [FS] pri token:    log to file/syslog for level 'pri' and above
			  [FS] p1-p2 token:  log to file/syslog for levels 'p1' to 'p2'
  -c context
  -U uptime
  -x ADDRESS		use ADDRESS as AgentX address
TRAP-PARAMETERS:
  trapoid [OID TYPE VALUE] ...
```

### `encode_keychange`

> 官方示例调用：`encode_keychange -h`

```text
root@kali:~# encode_keychange -h
Usage: encode_keychange [-fhPvV] -t (md5|sha1) [-O "<old_passphrase>"][-N "<new_passphrase>"][-E [0x]<engineID>]
    -E [0x]<engineID>		EngineID used for kul generation.
    -f				Force passphrases to be read from stdin.
    -h				Help.
    -N "<new_passphrase>"	Passphrase used to generate new Ku.
    -O "<old_passphrase>"	Passphrase used to generate old Ku.
    -P				Turn off prompt indicators.
    -t md5 | sha1		HMAC hash transform type.
    -v				Verbose.
    -V				Visible.  Echo passphrases to terminal.
Only -t is mandatory.  The transform is used to convert P=>Ku, convert
    Ku=>Kul, and to hash the old Kul with the random bits.
    Passphrase will be taken from the first successful source as follows:
	a) Commandline options,
	b) The file "/root/.snmp/passphrase.ek",
	c) stdin  -or-  User input from the terminal.
-f will require reading from the stdin/terminal, ignoring a) and b).
    -P will prevent prompts for passphrases to stdout from being printed.
    <engineID> is interpreted as a hex string when preceded by "0x",
    otherwise it is created to contain "text".  If nothing is given,
    <engineID> is constructed from the first IP address for the local host.
```

### `man`

> 官方示例调用：`man fixproc`

```text
root@kali:~# man fixproc
fixproc(1)                          Net-SNMP                         fixproc(1)
NAME
     fixproc - Fixes a process by performing the specified action.
SYNOPSIS
     fixproc [-min n] [-max n] [-check | -kill | -restart | -exist | -fix] proc
     ...
DESCRIPTION
     Fixes  a process named "proc" by performing the specified action.  The ac-
     tions can be check, kill, restart, exist, or fix.  The action is specified
     on the command line or is read from a default  database,  which  describes
     the  default action to take for each process.  The database format and the
     meaning of each action are described below.
OPTIONS
     -min n
            minimum number of processes that should be running, defaults to 1
     -max n
            maximum number of processes that should be running, defaults to 1
     -check
            check process against database /local/etc/fixproc.conf.
     -kill  kill process, wait 5 seconds, kill -9 if still exist
     -restart
            kill process, wait 5 seconds, kill -9 if still  exist,  then  start
            again
     -exist
            checks if proc exists in ps && (min <= num. of processes <= max)
     -fix   check process against database /local/etc/fixproc.conf. Perform de-
            fined action, if check fails.
V5.9.5.2                          16 Nov 2006                        fixproc(1)
```

### `snmp-bridge-mib`

> 官方示例调用：`snmp-bridge-mib -h`

```text
root@kali:~# snmp-bridge-mib -h
MIB search path: /root/.snmp/mibs:/usr/share/snmp/mibs:/usr/share/snmp/mibs/iana:/usr/share/snmp/mibs/ietf
Cannot find module (SNMPv2-MIB): At line 1 in (none)
Cannot find module (IF-MIB): At line 1 in (none)
Cannot find module (IP-MIB): At line 1 in (none)
Cannot find module (TCP-MIB): At line 1 in (none)
Cannot find module (UDP-MIB): At line 1 in (none)
Cannot find module (HOST-RESOURCES-MIB): At line 1 in (none)
Cannot find module (NOTIFICATION-LOG-MIB): At line 1 in (none)
Cannot find module (DISMAN-EVENT-MIB): At line 1 in (none)
Cannot find module (DISMAN-SCHEDULE-MIB): At line 1 in (none)
Cannot find module (HOST-RESOURCES-TYPES): At line 1 in (none)
Cannot find module (MTA-MIB): At line 1 in (none)
Cannot find module (NETWORK-SERVICES-MIB): At line 1 in (none)
Cannot find module (SNMPv2-TC): At line 15 in /usr/share/snmp/mibs/UCD-DISKIO-MIB.txt
Cannot find module (SNMPv2-SMI): At line 34 in /usr/share/snmp/mibs/UCD-SNMP-MIB.txt
Cannot find module (HCNUM-TC): At line 37 in /usr/share/snmp/mibs/UCD-SNMP-MIB.txt
Cannot find module (SNMPv2-TC): At line 40 in /usr/share/snmp/mibs/UCD-SNMP-MIB.txt
Did not find 'enterprises' in module #-1 (/usr/share/snmp/mibs/UCD-SNMP-MIB.txt)
Did not find 'CounterBasedGauge64' in module #-1 (/usr/share/snmp/mibs/UCD-SNMP-MIB.txt)
Did not find 'DisplayString' in module #-1 (/usr/share/snmp/mibs/UCD-SNMP-MIB.txt)
Did not find 'TruthValue' in module #-1 (/usr/share/snmp/mibs/UCD-SNMP-MIB.txt)
Cannot resolve OID in UCD-SNMP-MIB: ucdavis ::= { enterprises 2021 } at line 42 in /usr/share/snmp/mibs/UCD-SNMP-MIB.txt
Did not find 'DisplayString' in module #-1 (/usr/share/snmp/mibs/UCD-DISKIO-MIB.txt)
Did not find 'ucdExperimental' in module UCD-SNMP-MIB (/usr/share/snmp/mibs/UCD-DISKIO-MIB.txt)
Cannot resolve OID in UCD-DISKIO-MIB: ucdDiskIOMIB ::= { ucdExperimental 15 } at line 19 in /usr/share/snmp/mibs/UCD-DISKIO-MIB.txt
Cannot find module (SNMPv2-TC): At line 10 in /usr/share/snmp/mibs/UCD-DLMOD-MIB.txt
Did not find 'DisplayString' in module #-1 (/usr/share/snmp/mibs/UCD-DLMOD-MIB.txt)
Did not find 'ucdExperimental' in module UCD-SNMP-MIB (/usr/share/snmp/mibs/UCD-DLMOD-MIB.txt)
Cannot resolve OID in UCD-DLMOD-MIB: ucdDlmodMIB ::= { ucdExperimental 14 } at line 13 in /usr/share/snmp/mibs/UCD-DLMOD-MIB.txt
Cannot find module (SNMPv2-TC): At line 15 in /usr/share/snmp/mibs/LM-SENSORS-MIB.txt
Did not find 'DisplayString' in module #-1 (/usr/share/snmp/mibs/LM-SENSORS-MIB.txt)
Did not find 'ucdExperimental' in module UCD-SNMP-MIB (/usr/share/snmp/mibs/LM-SENSORS-MIB.txt)
Cannot resolve OID in LM-SENSORS-MIB: lmSensors ::= { ucdExperimental 16 } at line 37 in /usr/share/snmp/mibs/LM-SENSORS-MIB.txt
Did not find 'ucdavis' in module UCD-SNMP-MIB (/usr/share/snmp/mibs/UCD-DEMO-MIB.txt)
Cannot resolve OID in UCD-DEMO-MIB: ucdDemoMIB ::= { ucdavis 14 } at line 7 in /usr/share/snmp/mibs/UCD-DEMO-MIB.txt
Cannot find module (SNMP-TARGET-MIB): At line 1 in (none)
Cannot find module (SNMP-FRAMEWORK-MIB): At line 9 in /usr/share/snmp/mibs/NET-SNMP-AGENT-MIB.txt
Cannot find module (SNMPv2-SMI): At line 8 in /usr/share/snmp/mibs/NET-SNMP-MIB.txt
Did not find 'enterprises' in module #-1 (/usr/share/snmp/mibs/NET-SNMP-MIB.txt)
Cannot resolve OID in NET-SNMP-MIB: netSnmp ::= { enterprises 8072 } at line 10 in /usr/share/snmp/mibs/NET-SNMP-MIB.txt
Cannot find module (SNMPv2-TC): At line 21 in /usr/share/snmp/mibs/NET-SNMP-AGENT-MIB.txt
Did not find 'SnmpAdminString' in module #-1 (/usr/share/snmp/mibs/NET-SNMP-AGENT-MIB.txt)
Did not find 'netSnmpObjects' in module NET-SNMP-MIB (/usr/share/snmp/mibs/NET-SNMP-AGENT-MIB.txt)
Did not find 'netSnmpModuleIDs' in module NET-SNMP-MIB (/usr/share/snmp/mibs/NET-SNMP-AGENT-MIB.txt)
Did not find 'netSnmpNotifications' in module NET-SNMP-MIB (/usr/share/snmp/mibs/NET-SNMP-AGENT-MIB.txt)
Did not find 'netSnmpGroups' in module NET-SNMP-MIB (/usr/share/snmp/mibs/NET-SNMP-AGENT-MIB.txt)
Did not find 'DisplayString' in module #-1 (/usr/share/snmp/mibs/NET-SNMP-AGENT-MIB.txt)
Did not find 'RowStatus' in module #-1 (/usr/share/snmp/mibs/NET-SNMP-AGENT-MIB.txt)
Did not find 'TruthValue' in module #-1 (/usr/share/snmp/mibs/NET-SNMP-AGENT-MIB.txt)
Cannot resolve OID in NET-SNMP-AGENT-MIB: nsAgentNotifyGroup ::= { netSnmpGroups 9 } at line 545 in /usr/share/snmp/mibs/NET-SNMP-AGENT-MIB.txt
Cannot resolve OID in NET-SNMP-AGENT-MIB: nsTransactionGroup ::= { netSnmpGroups 8 } at line 536 in /usr/share/snmp/mibs/NET-SNMP-AGENT-MIB.txt
Cannot resolve OID in NET-SNMP-AGENT-MIB: nsConfigGroups ::= { netSnmpGroups 7 } at line 515 in /usr/share/snmp/mibs/NET-SNMP-AGENT-MIB.txt
Cannot resolve OID in NET-SNMP-AGENT-MIB: nsCacheGroup ::= { netSnmpGroups 4 } at line 505 in /usr/share/snmp/mibs/NET-SNMP-AGENT-MIB.txt
Cannot resolve OID in NET-SNMP-AGENT-MIB: nsModuleGroup ::= { netSnmpGroups 2 } at line 495 in /usr/share/snmp/mibs/NET-SNMP-AGENT-MIB.txt
Cannot resolve OID in NET-SNMP-AGENT-MIB: netSnmpAgentMIB ::= { netSnmpModuleIDs 2 } at line 24 in /usr/share/snmp/mibs/NET-SNMP-AGENT-MIB.txt
Cannot resolve OID in NET-SNMP-AGENT-MIB: nsTransactions ::= { netSnmpObjects 8 } at line 55 in /usr/share/snmp/mibs/NET-SNMP-AGENT-MIB.txt
Cannot resolve OID in NET-SNMP-AGENT-MIB: nsConfiguration ::= { netSnmpObjects 7 } at line 54 in /usr/share/snmp/mibs/NET-SNMP-AGENT-MIB.txt
Cannot resolve OID in NET-SNMP-AGENT-MIB: nsErrorHistory ::= { netSnmpObjects 6 } at line 53 in /usr/share/snmp/mibs/NET-SNMP-AGENT-MIB.txt
Cannot resolve OID in NET-SNMP-AGENT-MIB: nsCache ::= { netSnmpObjects 5 } at line 52 in /usr/share/snmp/mibs/NET-SNMP-AGENT-MIB.txt
Cannot resolve OID in NET-SNMP-AGENT-MIB: nsDLMod ::= { netSnmpObjects 4 } at line 51 in /usr/share/snmp/mibs/NET-SNMP-AGENT-MIB.txt
Cannot resolve OID in NET-SNMP-AGENT-MIB: nsExtensions ::= { netSnmpObjects 3 } at line 50 in /usr/share/snmp/mibs/NET-SNMP-AGENT-MIB.txt
Cannot resolve OID in NET-SNMP-AGENT-MIB: nsMibRegistry ::= { netSnmpObjects 2 } at line 49 in /usr/share/snmp/mibs/NET-SNMP-AGENT-MIB.txt
Cannot resolve OID in NET-SNMP-AGENT-MIB: nsVersion ::= { netSnmpObjects 1 } at line 48 in /usr/share/snmp/mibs/NET-SNMP-AGENT-MIB.txt
Cannot resolve OID in NET-SNMP-AGENT-MIB: nsNotifyRestart ::= { netSnmpNotifications 3 } at line 482 in /usr/share/snmp/mibs/NET-SNMP-AGENT-MIB.txt
Cannot resolve OID in NET-SNMP-AGENT-MIB: nsNotifyShutdown ::= { netSnmpNotifications 2 } at line 476 in /usr/share/snmp/mibs/NET-SNMP-AGENT-MIB.txt
Cannot resolve OID in NET-SNMP-AGENT-MIB: nsNotifyStart ::= { netSnmpNotifications 1 } at line 470 in /usr/share/snmp/mibs/NET-SNMP-AGENT-MIB.txt
Cannot find module (SNMP-FRAMEWORK-MIB): At line 1 in (none)
Cannot find module (SNMP-MPD-MIB): At line 1 in (none)
Cannot find module (SNMP-USER-BASED-SM-MIB): At line 1 in (none)
Cannot find module (SNMP-VIEW-BASED-ACM-MIB): At line 1 in (none)
Cannot find module (SNMP-COMMUNITY-MIB): At line 1 in (none)
Cannot find module (IPV6-ICMP-MIB): At line 1 in (none)
Cannot find module (IPV6-MIB): At line 1 in (none)
Cannot find module (IPV6-TCP-MIB): At line 1 in (none)
Cannot find module (IPV6-UDP-MIB): At line 1 in (none)
Cannot find module (IP-FORWARD-MIB): At line 1 in (none)
Cannot find module (SNMP-FRAMEWORK-MIB): At line 10 in /usr/share/snmp/mibs/NET-SNMP-PASS-MIB.txt
Cannot find module (SNMP-FRAMEWORK-MIB): At line 10 in /usr/share/snmp/mibs/NET-SNMP-EXAMPLES-MIB.txt
Cannot find module (SNMPv2-TC): At line 12 in /usr/share/snmp/mibs/NET-SNMP-EXAMPLES-MIB.txt
Cannot find module (INET-ADDRESS-MIB): At line 13 in /usr/share/snmp/mibs/NET-SNMP-EXAMPLES-MIB.txt
Did not find 'SnmpAdminString' in module #-1 (/usr/share/snmp/mibs/NET-SNMP-EXAMPLES-MIB.txt)
Did not find 'netSnmp' in module NET-SNMP-MIB (/usr/share/snmp/mibs/NET-SNMP-EXAMPLES-MIB.txt)
Did not find 'RowStatus' in module #-1 (/usr/share/snmp/mibs/NET-SNMP-EXAMPLES-MIB.txt)
Did not find 'StorageType' in module #-1 (/usr/share/snmp/mibs/NET-SNMP-EXAMPLES-MIB.txt)
Did not find 'InetAddressType' in module #-1 (/usr/share/snmp/mibs/NET-SNMP-EXAMPLES-MIB.txt)
Did not find 'InetAddress' in module #-1 (/usr/share/snmp/mibs/NET-SNMP-EXAMPLES-MIB.txt)
Cannot resolve OID in NET-SNMP-EXAMPLES-MIB: netSnmpExamples ::= { netSnmp 2 } at line 16 in /usr/share/snmp/mibs/NET-SNMP-EXAMPLES-MIB.txt
Did not find 'SnmpAdminString' in module #-1 (/usr/share/snmp/mibs/NET-SNMP-PASS-MIB.txt)
Did not find 'netSnmpExamples' in module NET-SNMP-EXAMPLES-MIB (/usr/share/snmp/mibs/NET-SNMP-PASS-MIB.txt)
Cannot resolve OID in NET-SNMP-PASS-MIB: netSnmpPassExamples ::= { netSnmpExamples 255 } at line 14 in /usr/share/snmp/mibs/NET-SNMP-PASS-MIB.txt
Cannot find module (SNMPv2-TC): At line 16 in /usr/share/snmp/mibs/NET-SNMP-EXTEND-MIB.txt
Did not find 'nsExtensions' in module NET-SNMP-AGENT-MIB (/usr/share/snmp/mibs/NET-SNMP-EXTEND-MIB.txt)
Did not find 'DisplayString' in module #-1 (/usr/share/snmp/mibs/NET-SNMP-EXTEND-MIB.txt)
Did not find 'RowStatus' in module #-1 (/usr/share/snmp/mibs/NET-SNMP-EXTEND-MIB.txt)
Did not find 'StorageType' in module #-1 (/usr/share/snmp/mibs/NET-SNMP-EXTEND-MIB.txt)
Cannot resolve OID in NET-SNMP-EXTEND-MIB: nsExtendGroups ::= { nsExtensions 3 } at line 39 in /usr/share/snmp/mibs/NET-SNMP-EXTEND-MIB.txt
Cannot resolve OID in NET-SNMP-EXTEND-MIB: nsExtendObjects ::= { nsExtensions 2 } at line 38 in /usr/share/snmp/mibs/NET-SNMP-EXTEND-MIB.txt
Cannot resolve OID in NET-SNMP-EXTEND-MIB: netSnmpExtendMIB ::= { nsExtensions 1 } at line 19 in /usr/share/snmp/mibs/NET-SNMP-EXTEND-MIB.txt
Cannot find module (SNMP-NOTIFICATION-MIB): At line 1 in (none)
Cannot find module (SNMPv2-TM): At line 1 in (none)
Cannot find module (SNMP-FRAMEWORK-MIB): At line 9 in /usr/share/snmp/mibs/NET-SNMP-VACM-MIB.txt
Cannot find module (SNMP-VIEW-BASED-ACM-MIB): At line 16 in /usr/share/snmp/mibs/NET-SNMP-VACM-MIB.txt
Cannot find module (SNMPv2-TC): At line 25 in /usr/share/snmp/mibs/NET-SNMP-VACM-MIB.txt
Did not find 'SnmpAdminString' in module #-1 (/usr/share/snmp/mibs/NET-SNMP-VACM-MIB.txt)
Did not find 'netSnmpObjects' in module NET-SNMP-MIB (/usr/share/snmp/mibs/NET-SNMP-VACM-MIB.txt)
Did not find 'netSnmpGroups' in module NET-SNMP-MIB (/usr/share/snmp/mibs/NET-SNMP-VACM-MIB.txt)
Did not find 'vacmGroupName' in module #-1 (/usr/share/snmp/mibs/NET-SNMP-VACM-MIB.txt)
Did not find 'vacmAccessContextPrefix' in module #-1 (/usr/share/snmp/mibs/NET-SNMP-VACM-MIB.txt)
Did not find 'vacmAccessSecurityModel' in module #-1 (/usr/share/snmp/mibs/NET-SNMP-VACM-MIB.txt)
Did not find 'vacmAccessSecurityLevel' in module #-1 (/usr/share/snmp/mibs/NET-SNMP-VACM-MIB.txt)
Did not find 'DisplayString' in module #-1 (/usr/share/snmp/mibs/NET-SNMP-VACM-MIB.txt)
Did not find 'RowStatus' in module #-1 (/usr/share/snmp/mibs/NET-SNMP-VACM-MIB.txt)
Did not find 'StorageType' in module #-1 (/usr/share/snmp/mibs/NET-SNMP-VACM-MIB.txt)
Cannot resolve OID in NET-SNMP-VACM-MIB: netSnmpVacmMIB ::= { netSnmpObjects 9 } at line 28 in /usr/share/snmp/mibs/NET-SNMP-VACM-MIB.txt
Cannot resolve OID in UCD-SNMP-MIB: logMatchRegExCompilation ::= { logMatchEntry 101 } at line 1916 in /usr/share/snmp/mibs/UCD-SNMP-MIB.txt
Cannot resolve OID in UCD-SNMP-MIB: logMatchErrorFlag ::= { logMatchEntry 100 } at line 1908 in /usr/share/snmp/mibs/UCD-SNMP-MIB.txt
Cannot resolve OID in UCD-SNMP-MIB: logMatchCycle ::= { logMatchEntry 11 } at line 1900 in /usr/share/snmp/mibs/UCD-SNMP-MIB.txt
Cannot resolve OID in UCD-SNMP-MIB: logMatchCount ::= { logMatchEntry 10 } at line 1892 in /usr/share/snmp/mibs/UCD-SNMP-MIB.txt
Cannot resolve OID in UCD-SNMP-MIB: logMatchCounter ::= { logMatchEntry 9 } at line 1883 in /usr/share/snmp/mibs/UCD-SNMP-MIB.txt
Cannot resolve OID in UCD-SNMP-MIB: logMatchCurrentCount ::= { logMatchEntry 8 } at line 1875 in /usr/share/snmp/mibs/UCD-SNMP-MIB.txt
Cannot resolve OID in UCD-SNMP-MIB: logMatchCurrentCounter ::= { logMatchEntry 7 } at line 1866 in /usr/share/snmp/mibs/UCD-SNMP-MIB.txt
Cannot resolve OID in UCD-SNMP-MIB: logMatchGlobalCount ::= { logMatchEntry 6 } at line 1858 in /usr/share/snmp/mibs/UCD-SNMP-MIB.txt
Cannot resolve OID in UCD-SNMP-MIB: logMatchGlobalCounter ::= { logMatchEntry 5 } at line 1850 in /usr/share/snmp/mibs/UCD-SNMP-MIB.txt
Cannot resolve OID in UCD-SNMP-MIB: logMatchRegEx ::= { logMatchEntry 4 } at line 1842 in /usr/share/snmp/mibs/UCD-SNMP-MIB.txt
Cannot resolve OID in UCD-SNMP-MIB: logMatchFilename ::= { logMatchEntry 3 } at line 1834 in /usr/share/snmp/mibs/UCD-SNMP-MIB.txt
Cannot resolve OID in UCD-SNMP-MIB: logMatchName ::= { logMatchEntry 2 } at line 1826 in /usr/share/snmp/mibs/UCD-SNMP-MIB.txt
Cannot resolve OID in UCD-SNMP-MIB: logMatchIndex ::= { logMatchEntry 1 } at line 1818 in /usr/share/snmp/mibs/UCD-SNMP-MIB.txt
Cannot resolve OID in NET-SNMP-VACM-MIB: nsVacmAccessEntry ::= { nsVacmAccessTable 1 } at line 53 in /usr/share/snmp/mibs/NET-SNMP-VACM-MIB.txt
Cannot resolve OID in UCD-SNMP-MIB: extErrFixCmd ::= { extEntry 103 } at line 416 in /usr/share/snmp/mibs/UCD-SNMP-MIB.txt
Cannot resolve OID in UCD-SNMP-MIB: extErrFix ::= { extEntry 102 } at line 405 in /usr/share/snmp/mibs/UCD-SNMP-MIB.txt
Cannot resolve OID in UCD-SNMP-MIB: extOutput ::= { extEntry 101 } at line 397 in /usr/share/snmp/mibs/UCD-SNMP-MIB.txt
Cannot resolve OID in UCD-SNMP-MIB: extResult ::= { extEntry 100 } at line 389 in /usr/share/snmp/mibs/UCD-SNMP-MIB.txt
Cannot resolve OID in UCD-SNMP-MIB: extCommand ::= { extEntry 3 } at line 381 in /usr/share/snmp/mibs/UCD-SNMP-MIB.txt
Cannot resolve OID in UCD-SNMP-MIB: extNames ::= { extEntry 2 } at line 373 in /usr/share/snmp/mibs/UCD-SNMP-MIB.txt
Cannot resolve OID in UCD-SNMP-MIB: extIndex ::= { extEntry 1 } at line 364 in /usr/share/snmp/mibs/UCD-SNMP-MIB.txt
Cannot resolve OID in UCD-DEMO-MIB: ucdDemoPublic ::= { ucdDemoMIBObjects 1 } at line 32 in /usr/share/snmp/mibs/UCD-DEMO-MIB.txt
Cannot resolve OID in UCD-DLMOD-MIB: dlmodTable ::= { ucdDlmodMIB 2 } at line 52 in /usr/share/snmp/mibs/UCD-DLMOD-MIB.txt
Cannot resolve OID in UCD-DLMOD-MIB: dlmodNextIndex ::= { ucdDlmodMIB 1 } at line 43 in /usr/share/snmp/mibs/UCD-DLMOD-MIB.txt
Cannot resolve OID in NET-SNMP-EXAMPLES-MIB: netSnmpExamples ::= { netSnmp 2 } at line 16 in /usr/share/snmp/mibs/NET-SNMP-EXAMPLES-MIB.txt
Cannot resolve OID in NET-SNMP-MIB: netSnmpConformance ::= { netSnmp 5 } at line 63 in /usr/share/snmp/mibs/NET-SNMP-MIB.txt
Cannot resolve OID in NET-SNMP-MIB: netSnmpNotificationPrefix ::= { netSnmp 4 } at line 53 in /usr/share/snmp/mibs/NET-SNMP-MIB.txt
Cannot resolve OID in NET-SNMP-MIB: netSnmpExperimental ::= { netSnmp 9999 } at line 37 in /usr/share/snmp/mibs/NET-SNMP-MIB.txt
Cannot resolve OID in NET-SNMP-MIB: netSnmpEnumerations ::= { netSnmp 3 } at line 33 in /usr/share/snmp/mibs/NET-SNMP-MIB.txt
Cannot resolve OID in NET-SNMP-MIB: netSnmpObjects ::= { netSnmp 1 } at line 31 in /usr/share/snmp/mibs/NET-SNMP-MIB.txt
Cannot resolve OID in UCD-SNMP-MIB: versionDoDebugging ::= { version 20 } at line 1177 in /usr/share/snmp/mibs/UCD-SNMP-MIB.txt
Cannot resolve OID in UCD-SNMP-MIB: versionSavePersistentData ::= { version 13 } at line 1169 in /usr/share/snmp/mibs/UCD-SNMP-MIB.txt
Cannot resolve OID in UCD-SNMP-MIB: versionRestartAgent ::= { version 12 } at line 1161 in /usr/share/snmp/mibs/UCD-SNMP-MIB.txt
Cannot resolve OID in UCD-SNMP-MIB: versionUpdateConfig ::= { version 11 } at line 1153 in /usr/share/snmp/mibs/UCD-SNMP-MIB.txt
Cannot resolve OID in UCD-SNMP-MIB: versionClearCache ::= { version 10 } at line 1145 in /usr/share/snmp/mibs/UCD-SNMP-MIB.txt
Cannot resolve OID in UCD-SNMP-MIB: versionConfigureOptions ::= { version 6 } at line 1137 in /usr/share/snmp/mibs/UCD-SNMP-MIB.txt
Cannot resolve OID in UCD-SNMP-MIB: versionIdent ::= { version 5 } at line 1129 in /usr/share/snmp/mibs/UCD-SNMP-MIB.txt
Cannot resolve OID in UCD-SNMP-MIB: versionCDate ::= { version 4 } at line 1121 in /usr/share/snmp/mibs/UCD-SNMP-MIB.txt
Cannot resolve OID in UCD-SNMP-MIB: versionDate ::= { version 3 } at line 1113 in /usr/share/snmp/mibs/UCD-SNMP-MIB.txt
Cannot resolve OID in UCD-SNMP-MIB: versionTag ::= { version 2 } at line 1105 in /usr/share/snmp/mibs/UCD-SNMP-MIB.txt
Cannot resolve OID in UCD-SNMP-MIB: versionIndex ::= { version 1 } at line 1097 in /usr/share/snmp/mibs/UCD-SNMP-MIB.txt
Cannot resolve OID in NET-SNMP-EXAMPLES-MIB: netSnmpExampleHeartbeatNotification ::= { netSnmpExampleNotificationPrefix 1 } at line 263 in /usr/share/snmp/mibs/NET-SNMP-EXAMPLES-MIB.txt
Cannot resolve OID in NET-SNMP-AGENT-MIB: nsCacheStatus ::= { nsCacheEntry 3 } at line 132 in /usr/share/snmp/mibs/NET-SNMP-AGENT-MIB.txt
Cannot resolve OID in NET-SNMP-AGENT-MIB: nsCacheTimeout ::= { nsCacheEntry 2 } at line 123 in /usr/share/snmp/mibs/NET-SNMP-AGENT-MIB.txt
Cannot resolve OID in NET-SNMP-AGENT-MIB: nsCachedOID ::= { nsCacheEntry 1 } at line 115 in /usr/share/snmp/mibs/NET-SNMP-AGENT-MIB.txt
Cannot resolve OID in UCD-SNMP-MIB: unknown ::= { ucdSnmpAgent 255 } at line 167 in /usr/share/snmp/mibs/UCD-SNMP-MIB.txt
Cannot resolve OID in UCD-SNMP-MIB: dragonfly ::= { ucdSnmpAgent 17 } at line 166 in /usr/share/snmp/mibs/UCD-SNMP-MIB.txt
Cannot resolve OID in UCD-SNMP-MIB: macosx ::= { ucdSnmpAgent 16 } at line 165 in /usr/share/snmp/mibs/UCD-SNMP-MIB.txt
Cannot resolve OID in UCD-SNMP-MIB: aix ::= { ucdSnmpAgent 15 } at line 164 in /usr/share/snmp/mibs/UCD-SNMP-MIB.txt
Cannot resolve OID in UCD-SNMP-MIB: hpux11 ::= { ucdSnmpAgent 14 } at line 163 in /usr/share/snmp/mibs/UCD-SNMP-MIB.txt
Cannot resolve OID in UCD-SNMP-MIB: win32 ::= { ucdSnmpAgent 13 } at line 162 in /usr/share/snmp/mibs/UCD-SNMP-MIB.txt
Cannot resolve OID in UCD-SNMP-MIB: openbsd ::= { ucdSnmpAgent 12 } at line 161 in /usr/share/snmp/mibs/UCD-SNMP-MIB.txt
Cannot resolve OID in UCD-SNMP-MIB: bsdi ::= { ucdSnmpAgent 11 } at line 160 in /usr/share/snmp/mibs/UCD-SNMP-MIB.txt
Cannot resolve OID in UCD-SNMP-MIB: linux ::= { ucdSnmpAgent 10 } at line 159 in /usr/share/snmp/mibs/UCD-SNMP-MIB.txt
Cannot resolve OID in UCD-SNMP-MIB: irix ::= { ucdSnmpAgent 9 } at line 158 in /usr/share/snmp/mibs/UCD-SNMP-MIB.txt
Cannot resolve OID in UCD-SNMP-MIB: freebsd ::= { ucdSnmpAgent 8 } at line 157 in /usr/share/snmp/mibs/UCD-SNMP-MIB.txt
Cannot resolve OID in UCD-SNMP-MIB: netbsd1 ::= { ucdSnmpAgent 7 } at line 156 in /usr/share/snmp/mibs/UCD-SNMP-MIB.txt
Cannot resolve OID in UCD-SNMP-MIB: hpux10 ::= { ucdSnmpAgent 6 } at line 155 in /usr/share/snmp/mibs/UCD-SNMP-MIB.txt
Cannot resolve OID in UCD-SNMP-MIB: ultrix ::= { ucdSnmpAgent 5 } at line 154 in /usr/share/snmp/mibs/UCD-SNMP-MIB.txt
Cannot resolve OID in UCD-SNMP-MIB: osf ::= { ucdSnmpAgent 4 } at line 153 in /usr/share/snmp/mibs/UCD-SNMP-MIB.txt
Cannot resolve OID in UCD-SNMP-MIB: solaris ::= { ucdSnmpAgent 3 } at line 152 in /usr/share/snmp/mibs/UCD-SNMP-MIB.txt
Cannot resolve OID in UCD-SNMP-MIB: sunos4 ::= { ucdSnmpAgent 2 } at line 151 in /usr/share/snmp/mibs/UCD-SNMP-MIB.txt
Cannot resolve OID in UCD-SNMP-MIB: hpux9 ::= { ucdSnmpAgent 1 } at line 150 in /usr/share/snmp/mibs/UCD-SNMP-MIB.txt
Cannot resolve OID in NET-SNMP-EXTEND-MIB: nsExtendOutputGroup ::= { nsExtendGroups 2 } at line 315 in /usr/share/snmp/mibs/NET-SNMP-EXTEND-MIB.txt
Cannot resolve OID in NET-SNMP-EXTEND-MIB: nsExtendConfigGroup ::= { nsExtendGroups 1 } at line 304 in /usr/share/snmp/mibs/NET-SNMP-EXTEND-MIB.txt
Cannot resolve OID in UCD-DISKIO-MIB: diskIOEntry ::= { diskIOTable 1 } at line 65 in /usr/share/snmp/mibs/UCD-DISKIO-MIB.txt
Cannot resolve OID in NET-SNMP-AGENT-MIB: nsTransactionEntry ::= { nsTransactionTable 1 } at line 350 in /usr/share/snmp/mibs/NET-SNMP-AGENT-MIB.txt
Cannot resolve OID in NET-SNMP-MIB: netSnmpGroups ::= { netSnmpConformance 2 } at line 65 in /usr/share/snmp/mibs/NET-SNMP-MIB.txt
Cannot resolve OID in NET-SNMP-MIB: netSnmpCompliances ::= { netSnmpConformance 1 } at line 64 in /usr/share/snmp/mibs/NET-SNMP-MIB.txt
Cannot resolve OID in UCD-SNMP-MIB: mrModuleName ::= { mrEntry 2 } at line 1255 in /usr/share/snmp/mibs/UCD-SNMP-MIB.txt
Cannot resolve OID in UCD-SNMP-MIB: mrIndex ::= { mrEntry 1 } at line 1247 in /usr/share/snmp/mibs/UCD-SNMP-MIB.txt
Cannot resolve OID in NET-SNMP-AGENT-MIB: nsDebugTokenEntry ::= { nsDebugTokenTable 1 } at line 193 in /usr/share/snmp/mibs/NET-SNMP-AGENT-MIB.txt
Cannot resolve OID in NET-SNMP-EXTEND-MIB: nsExtendStatus ::= { nsExtendConfigEntry 21 } at line 182 in /usr/share/snmp/mibs/NET-SNMP-EXTEND-MIB.txt
Cannot resolve OID in NET-SNMP-EXTEND-MIB: nsExtendStorage ::= { nsExtendConfigEntry 20 } at line 173 in /usr/share/snmp/mibs/NET-SNMP-EXTEND-MIB.txt
Cannot resolve OID in NET-SNMP-EXTEND-MIB: nsExtendRunType ::= { nsExtendConfigEntry 7 } at line 146 in /usr/share/snmp/mibs/NET-SNMP-EXTEND-MIB.txt
Cannot resolve OID in NET-SNMP-EXTEND-MIB: nsExtendExecType ::= { nsExtendConfigEntry 6 } at line 134 in /usr/share/snmp/mibs/NET-SNMP-EXTEND-MIB.txt
Cannot resolve OID in NET-SNMP-EXTEND-MIB: nsExtendCacheTime ::= { nsExtendConfigEntry 5 } at line 118 in /usr/share/snmp/mibs/NET-SNMP-EXTEND-MIB.txt
Cannot resolve OID in NET-SNMP-EXTEND-MIB: nsExtendInput ::= { nsExtendConfigEntry 4 } at line 109 in /usr/share/snmp/mibs/NET-SNMP-EXTEND-MIB.txt
Cannot resolve OID in NET-SNMP-EXTEND-MIB: nsExtendArgs ::= { nsExtendConfigEntry 3 } at line 100 in /usr/share/snmp/mibs/NET-SNMP-EXTEND-MIB.txt
Cannot resolve OID in NET-SNMP-EXTEND-MIB: nsExtendCommand ::= { nsExtendConfigEntry 2 } at line 92 in /usr/share/snmp/mibs/NET-SNMP-EXTEND-MIB.txt
Cannot resolve OID in NET-SNMP-EXTEND-MIB: nsExtendToken ::= { nsExtendConfigEntry 1 } at line 84 in /usr/share/snmp/mibs/NET-SNMP-EXTEND-MIB.txt
Cannot resolve OID in NET-SNMP-AGENT-MIB: nsModuleTable ::= { nsMibRegistry 1 } at line 386 in /usr/share/snmp/mibs/NET-SNMP-AGENT-MIB.txt
Cannot resolve OID in NET-SNMP-MIB: netSnmpPlaypen ::= { netSnmpExperimental 9999 } at line 46 in /usr/share/snmp/mibs/NET-SNMP-MIB.txt
Cannot resolve OID in NET-SNMP-EXAMPLES-MIB: netSnmpIETFWGEntry ::= { netSnmpIETFWGTable 1 } at line 124 in /usr/share/snmp/mibs/NET-SNMP-EXAMPLES-MIB.txt
Cannot resolve OID in UCD-SNMP-MIB: prErrFixCmd ::= { prEntry 103 } at line 324 in /usr/share/snmp/mibs/UCD-SNMP-MIB.txt
Cannot resolve OID in UCD-SNMP-MIB: prErrFix ::= { prEntry 102 } at line 313 in /usr/share/snmp/mibs/UCD-SNMP-MIB.txt
Cannot resolve OID in UCD-SNMP-MIB: prErrMessage ::= { prEntry 101 } at line 305 in /usr/share/snmp/mibs/UCD-SNMP-MIB.txt
Cannot resolve OID in UCD-SNMP-MIB: prErrorFlag ::= { prEntry 100 } at line 296 in /usr/share/snmp/mibs/UCD-SNMP-MIB.txt
Cannot resolve OID in UCD-SNMP-MIB: prCount ::= { prEntry 5 } at line 287 in /usr/share/snmp/mibs/UCD-SNMP-MIB.txt
Cannot resolve OID in UCD-SNMP-MIB: prMax ::= { prEntry 4 } at line 277 in /usr/share/snmp/mibs/UCD-SNMP-MIB.txt
Cannot resolve OID in UCD-SNMP-MIB: prMin ::= { prEntry 3 } at line 267 in /usr/share/snmp/mibs/UCD-SNMP-MIB.txt
Cannot resolve OID in UCD-SNMP-MIB: prNames ::= { prEntry 2 } at line 259 in /usr/share/snmp/mibs/UCD-SNMP-MIB.txt
Cannot resolve OID in UCD-SNMP-MIB: prIndex ::= { prEntry 1 } at line 251 in /usr/share/snmp/mibs/UCD-SNMP-MIB.txt
Cannot resolve OID in UCD-DLMOD-MIB: dlmodEntry ::= { dlmodTable 1 } at line 60 in /usr/share/snmp/mibs/UCD-DLMOD-MIB.txt
Cannot resolve OID in UCD-SNMP-MIB: memSwapErrorMsg ::= { memory 101 } at line 781 in /usr/share/snmp/mibs/UCD-SNMP-MIB.txt
Cannot resolve OID in UCD-SNMP-MIB: memSwapError ::= { memory 100 } at line 771 in /usr/share/snmp/mibs/UCD-SNMP-MIB.txt
Cannot resolve OID in UCD-SNMP-MIB: memSysAvail ::= { memory 27 } at line 755 in /usr/share/snmp/mibs/UCD-SNMP-MIB.txt
Cannot resolve OID in UCD-SNMP-MIB: memCachedX ::= { memory 26 } at line 741 in /usr/share/snmp/mibs/UCD-SNMP-MIB.txt
Cannot resolve OID in UCD-SNMP-MIB: memBufferX ::= { memory 25 } at line 727 in /usr/share/snmp/mibs/UCD-SNMP-MIB.txt
Cannot resolve OID in UCD-SNMP-MIB: memSharedX ::= { memory 24 } at line 713 in /usr/share/snmp/mibs/UCD-SNMP-MIB.txt
Cannot resolve OID in UCD-SNMP-MIB: memMinimumSwapX ::= { memory 23 } at line 698 in /usr/share/snmp/mibs/UCD-SNMP-MIB.txt
Cannot resolve OID in UCD-SNMP-MIB: memTotalFreeX ::= { memory 22 } at line 687 in /usr/share/snmp/mibs/UCD-SNMP-MIB.txt
Cannot resolve OID in UCD-SNMP-MIB: memAvailRealX ::= { memory 21 } at line 676 in /usr/share/snmp/mibs/UCD-SNMP-MIB.txt
Cannot resolve OID in UCD-SNMP-MIB: memTotalRealX ::= { memory 20 } at line 666 in /usr/share/snmp/mibs/UCD-SNMP-MIB.txt
Cannot resolve OID in UCD-SNMP-MIB: memAvailSwapX ::= { memory 19 } at line 657 in /usr/share/snmp/mibs/UCD-SNMP-MIB.txt
```

### `snmpbulkget`

> 官方示例调用：`snmpbulkget -h`

```text
root@kali:~# snmpbulkget -h
USAGE: snmpbulkget [OPTIONS] AGENT OID [OID]...
  Version:  5.9.5.2
  Web:      http://www.net-snmp.org/
  Email:
[email protected]
OPTIONS:
  -h, --help		display this help message
  -H			display configuration file directives understood
  -v 1|2c|3		specifies SNMP version to use
  -V, --version		display package version number
SNMP Version 1 or 2c specific
  -c COMMUNITY		set the community string
SNMP Version 3 specific
  -a PROTOCOL		set authentication protocol (MD5|SHA|SHA-224|SHA-256|SHA-384|SHA-512)
  -A PASSPHRASE		set authentication protocol pass phrase
  -e ENGINE-ID		set security engine ID (e.g. 800000020109840301)
  -E ENGINE-ID		set context engine ID (e.g. 800000020109840301)
  -l LEVEL		set security level (noAuthNoPriv|authNoPriv|authPriv)
  -n CONTEXT		set context name (e.g. bridge1)
  -u USER-NAME		set security name (e.g. bert)
  -x PROTOCOL		set privacy protocol (DES|AES|AES-192|AES-256)
  -X PASSPHRASE		set privacy protocol pass phrase
  -Z BOOTS,TIME		set destination engine boots/time
General communication options
  -r RETRIES		set the number of retries
  -t TIMEOUT		set the request timeout (in seconds)
Debugging
  -d			dump input/output packets in hexadecimal
  -D[TOKEN[,...]]	turn on debugging output for the specified TOKENs
			   (ALL gives extremely verbose debugging output)
General options
  -m MIB[:...]		load given list of MIBs (ALL loads everything)
  -M DIR[:...]		look in given list of directories for MIBs
    (default: $HOME/.snmp/mibs:/usr/share/snmp/mibs:/usr/share/snmp/mibs/iana:/usr/share/snmp/mibs/ietf)
  -P MIBOPTS		Toggle various defaults controlling MIB parsing:
			  u:  allow the use of underlines in MIB symbols
			  c:  disallow the use of "--" to terminate comments
			  d:  save the DESCRIPTIONs of the MIB objects
			  e:  disable errors when MIB symbols conflict
			  w:  enable warnings when MIB symbols conflict
			  W:  enable detailed warnings when MIB symbols conflict
			  R:  replace MIB symbols from latest module
  -O OUTOPTS		Toggle various defaults controlling output display:
			  0:  print leading 0 for single-digit hex characters
			  a:  print all strings in ascii format
			  b:  do not break OID indexes down
			  e:  print enums numerically
			  E:  escape quotes in string indices
			  f:  print full OIDs on output
			  n:  print OIDs numerically
			  p PRECISION:  display floating point values with specified PRECISION (printf format string)
			  q:  quick print for easier parsing
			  Q:  quick print with equal-signs
			  s:  print only last symbolic element of OID
			  S:  print MIB module-id plus last element
			  t:  print timeticks unparsed as numeric integers
			  T:  print human-readable text along with hex strings
			  u:  print OIDs using UCD-style prefix suppression
			  U:  don't print units
			  v:  print values only (not OID = value)
			  x:  print all strings in hex format
			  X:  extended index format
  -I INOPTS		Toggle various defaults controlling input parsing:
			  b:  do best/regex matching to find a MIB node
			  h:  don't apply DISPLAY-HINTs
			  r:  do not check values for range/type legality
			  R:  do random access to OID labels
			  u:  top-level OIDs must have '.' prefix (UCD-style)
			  s SUFFIX:  Append all textual OIDs with SUFFIX before parsing
			  S PREFIX:  Prepend all textual OIDs with PREFIX before parsing
  -L LOGOPTS		Toggle various defaults controlling logging:
			  e:           log to standard error
			  o:           log to standard output
			  n:           don't log at all
			  f file:      log to the specified file
			  s facility:  log to syslog (via the specified facility)
			  (variants)
			  [EON] pri:   log to standard error, output or /dev/null for level 'pri' and above
			  [EON] p1-p2: log to standard error, output or /dev/null for levels 'p1' to 'p2'
			  [FS] pri token:    log to file/syslog for level 'pri' and above
			  [FS] p1-p2 token:  log to file/syslog for levels 'p1' to 'p2'
  -C APPOPTS		Set various application specific behaviours:
			  n<NUM>:  set non-repeaters to <NUM>
			  r<NUM>:  set max-repeaters to <NUM>
```

### `snmpbulkwalk`

> 官方示例调用：`snmpbulkwalk -h`

```text
root@kali:~# snmpbulkwalk -h
USAGE: snmpbulkwalk [OPTIONS] AGENT [OID]
  Version:  5.9.5.2
  Web:      http://www.net-snmp.org/
  Email:
[email protected]
OPTIONS:
  -h, --help		display this help message
  -H			display configuration file directives understood
  -v 1|2c|3		specifies SNMP version to use
  -V, --version		display package version number
SNMP Version 1 or 2c specific
  -c COMMUNITY		set the community string
SNMP Version 3 specific
  -a PROTOCOL		set authentication protocol (MD5|SHA|SHA-224|SHA-256|SHA-384|SHA-512)
  -A PASSPHRASE		set authentication protocol pass phrase
  -e ENGINE-ID		set security engine ID (e.g. 800000020109840301)
  -E ENGINE-ID		set context engine ID (e.g. 800000020109840301)
  -l LEVEL		set security level (noAuthNoPriv|authNoPriv|authPriv)
  -n CONTEXT		set context name (e.g. bridge1)
  -u USER-NAME		set security name (e.g. bert)
  -x PROTOCOL		set privacy protocol (DES|AES|AES-192|AES-256)
  -X PASSPHRASE		set privacy protocol pass phrase
  -Z BOOTS,TIME		set destination engine boots/time
General communication options
  -r RETRIES		set the number of retries
  -t TIMEOUT		set the request timeout (in seconds)
Debugging
  -d			dump input/output packets in hexadecimal
  -D[TOKEN[,...]]	turn on debugging output for the specified TOKENs
			   (ALL gives extremely verbose debugging output)
General options
  -m MIB[:...]		load given list of MIBs (ALL loads everything)
  -M DIR[:...]		look in given list of directories for MIBs
    (default: $HOME/.snmp/mibs:/usr/share/snmp/mibs:/usr/share/snmp/mibs/iana:/usr/share/snmp/mibs/ietf)
  -P MIBOPTS		Toggle various defaults controlling MIB parsing:
			  u:  allow the use of underlines in MIB symbols
			  c:  disallow the use of "--" to terminate comments
			  d:  save the DESCRIPTIONs of the MIB objects
			  e:  disable errors when MIB symbols conflict
			  w:  enable warnings when MIB symbols conflict
			  W:  enable detailed warnings when MIB symbols conflict
			  R:  replace MIB symbols from latest module
  -O OUTOPTS		Toggle various defaults controlling output display:
			  0:  print leading 0 for single-digit hex characters
			  a:  print all strings in ascii format
			  b:  do not break OID indexes down
			  e:  print enums numerically
			  E:  escape quotes in string indices
			  f:  print full OIDs on output
			  n:  print OIDs numerically
			  p PRECISION:  display floating point values with specified PRECISION (printf format string)
			  q:  quick print for easier parsing
			  Q:  quick print with equal-signs
			  s:  print only last symbolic element of OID
			  S:  print MIB module-id plus last element
			  t:  print timeticks unparsed as numeric integers
			  T:  print human-readable text along with hex strings
			  u:  print OIDs using UCD-style prefix suppression
			  U:  don't print units
			  v:  print values only (not OID = value)
			  x:  print all strings in hex format
			  X:  extended index format
  -I INOPTS		Toggle various defaults controlling input parsing:
			  b:  do best/regex matching to find a MIB node
			  h:  don't apply DISPLAY-HINTs
			  r:  do not check values for range/type legality
			  R:  do random access to OID labels
			  u:  top-level OIDs must have '.' prefix (UCD-style)
			  s SUFFIX:  Append all textual OIDs with SUFFIX before parsing
			  S PREFIX:  Prepend all textual OIDs with PREFIX before parsing
  -L LOGOPTS		Toggle various defaults controlling logging:
			  e:           log to standard error
			  o:           log to standard output
			  n:           don't log at all
			  f file:      log to the specified file
			  s facility:  log to syslog (via the specified facility)
			  (variants)
			  [EON] pri:   log to standard error, output or /dev/null for level 'pri' and above
			  [EON] p1-p2: log to standard error, output or /dev/null for levels 'p1' to 'p2'
			  [FS] pri token:    log to file/syslog for level 'pri' and above
			  [FS] p1-p2 token:  log to file/syslog for levels 'p1' to 'p2'
  -C APPOPTS		Set various application specific behaviours:
			  c:       do not check returned OIDs are increasing
			  i:       include given OIDs in the search range
			  n<NUM>:  set non-repeaters to <NUM>
			  p:       print the number of variables found
			  r<NUM>:  set max-repeaters to <NUM>
```

### `snmpcheck`

> 官方示例调用：`snmpcheck -h`

```text
root@kali:~# snmpcheck -h
Usage:  snmpcheck [-x] [-n|y] [-h] [-H] [-V NUM] [-L] [-f] [[-a] HOSTS]
  -h	Display this message.
  -a	check error log file AND hosts specified on command line.
  -p	Don't try and ping-echo the host first
  -f	Only check for things I can fix
  HOSTS	check these hosts for problems.
X Options:
  -x	forces ascii base if $DISPLAY set (instead of tk).
  -H	start in hidden mode.  (hides user interface)
  -V NUM	sets the initial verbosity level of the command log (def: 1)
  -L	Show the log window at startup
  -d	Don't start by checking anything.  Just bring up the interface.
Ascii Options:
  -n	Don't ever try and fix the problems found.  Just list.
  -y	Always fix problems found.
```

## 4. 实践清单

按顺序做完这五步，就能把工具从「装上」推进到「会用」：

- [ ] **1.** **装好并确认版本** —— `sudo apt install libnetsnmptrapd45`，再执行 `libnetsnmptrapd45 --version` 2>/dev/null || `libnetsnmptrapd45 -V`
- [ ] **2.** **读官方帮助** —— `libnetsnmptrapd45 -h`，需要细节时 `man libnetsnmptrapd45`
- [ ] **3.** **在自有靶场跑最小用例** —— 官方给出的调用形式是：`Usage:`
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/net-snmp/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/net-snmp/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/net-snmp/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
