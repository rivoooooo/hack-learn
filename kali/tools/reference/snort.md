# snort

> Flexible Network Intrusion Detection System Snort is a libpcap-based packet sniffer/logger which can be used as a lightweight network intrusion detection system. It features rules-based logging and can perform content searching/matching in…

> **功能分类**：通用工具 ｜ **Kali 包**：`snort` ｜ **官方文档**：<https://www.kali.org/tools/snort/>

## 1. 安装

```bash
sudo apt update
sudo apt install snort
```

| 项目 | 内容 |
|------|------|
| 版本 | 3.12.2.0 |
| 架构 | any |
| 可执行命令 | `snort`、`appid_detector_builder.sh`、`show_flows`、`snort2lua`、`u2boat`、`u2spewfoo`、`snort-common`、`snort-common-libraries`、`snort-doc`、`snort-rules-default` |
| 依赖 | `adduser` |
| 安装体积 | 11.15 MB |
| 官网 | <https://www.snort.org/> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/snort> |
| 包追踪 | <https://pkg.kali.org/pkg/snort> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
snort -h          # 查看用法
man snort         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 10 个可执行命令，下面是官方页面内嵌的帮助原文。

### `appid_detector_builder.sh`

官方给出的调用示例：`appid_detector_builder.sh -h`

```text
root@kali:~# appid_detector_builder.sh -h
Snort Application Id - Detector Creation Tool
Enter below, the AppId string to be associated with the Detector.
(e.g. "CNN.com", "Yahoo!", "Avira Download/Update", etc.)
AppId strings MUST NOT INCLUDE tab, backslash, apostrophe, or double-quote.
```

### `show_flows`

官方给出的调用示例：`show_flows -h`

```text
root@kali:~# show_flows -h
Usage:
	show_flows -h - print this help
	show_flows -v - print the version
	show_flows -f <filename> -r <src ip> -t <dst ip> -s <src port> -d <dst port> -p <protocol>
```

### `snort`

官方给出的调用示例：`snort -h`

```text
root@kali:~# snort -h
Snort has several options to get more help:
-? list command line options (same as --help)
--help this overview of help
--help-commands [<module prefix>] output matching commands
--help-config [<module prefix>] output matching config options
--help-counts [<module prefix>] output matching peg counts
--help-limits print the int upper bounds denoted by max*
--help-module <module> output description of given module
--help-modules list all available modules with brief help
--help-modules-json dump description of all available modules in JSON format
--help-plugins list all available plugins with brief help
--help-options [<option prefix>] output matching command line options
--help-signals dump available control signals
--list-buffers output available inspection buffers
--list-builtin [<module prefix>] output matching builtin rules
--list-gids [<module prefix>] output matching generators
--list-modules [<module type>] list all known modules
--list-plugins list all known modules
--show-plugins list module and plugin versions
--help* and --list* options preempt other processing so should be last on the
command line since any following options are ignored.  To ensure options like
--markup and --plugin-path take effect, place them ahead of the help or list
options.
Options that filter output based on a matching prefix, such as --help-config
won't output anything if there is no match.  If no prefix is given, everything
matches.
Report bugs to
[email protected]
.
```

### `snort2lua`

官方给出的调用示例：`snort2lua -h`

```text
root@kali:~# snort2lua -h
Usage: snort2lua [OPTIONS]... -c <snort_conf> ...
Converts the Snort configuration file specified by the -c or --conf-file
options into a Snort++ configuration file
Options:
-?                  show usage
-h                  this overview of snort2lua
-a                  default option.  print all data
-c <snort_conf>     The Snort <snort_conf> file to convert
-d                  print the differences, and only the differences, between the
                    Snort and Snort++ configurations to the <out_file>
-e <error_file>     output all errors to <error_file>
-i                  if <snort_conf> file contains any <include_file> or
                    <policy_file> (i.e. 'include path/to/conf/other_conf'), do
                    NOT parse those files
-m                  add a remark to the end of every converted rule
-o <out_file>       output the new Snort++ lua configuration to <out_file>
-q                  quiet mode. Only output valid configuration information to
                    the <out_file>
-r <rule_file>      output any converted rule to <rule_file>
-s                  when parsing <include_file>, write <include_file>'s rules to
                    <rule_file>. Meaningless if '-i' provided
-t                  when parsing <include_file>, write <include_file>'s
                    information, excluding rules, to <out_file>. Meaningless if
                    '-i' provided
-V                  Print the current Snort2Lua version
--bind-wizard       Add default wizard to bindings
--bind-port         Convert port bindings
--conf-file         Same as '-c'. A Snort <snort_conf> file which will be
                    converted
--dont-parse-includes
                    Same as '-p'. if <snort_conf> file contains any
                    <include_file> or <policy_file> (i.e. 'include
                    path/to/conf/other_conf'), do NOT parse those files
--dont-convert-max-sessions
                    do not convert max_tcp, max_udp, max_icmp, max_ip to
                    max_session
--error-file=<error_file>
                    Same as '-e'. output all errors to <error_file>
--help              Same as '-h'. this overview of snort2lua
--ips-policy-pattern  Convert config bindings matching this path to ips policy
                    bindings
--markup            print help in asciidoc compatible format
--output-file=<out_file>
                    Same as '-o'. output the new Snort++ lua configuration to
                    <out_file>
--print-all         Same as '-a'. default option.  print all data
--print-differences  Same as '-d'. output the differences, and only the
                    differences, between the Snort and Snort++ configurations to
                    the <out_file>
--quiet             Same as '-q'. quiet mode. Only output valid configuration
                    information to the <out_file>
--remark            same as '-m'.  add a remark to the end of every converted
                    rule
--rule-file=<rule_file>
                    Same as '-r'. output any converted rule to <rule_file>
--single-conf-file  Same as '-t'. when parsing <include_file>, write
                    <include_file>'s information, excluding rules, to
                    <out_file>
--single-rule-file  Same as '-s'. when parsing <include_file>, write
                    <include_file>'s rules to <rule_file>.
--version           Same as '-V'. Print the current Snort2Lua version
Required option:
	A Snort configuration file to convert. Set with either '-c' or '--conf-file'
Default values:
	<out_file>   =  snort.lua
	<rule_file>  =  <out_file> = snort.lua.  Rules are written to the 'local_rules' variable in the <out_file>
	<error_file> =  snort.rej.  This file will not be created in quiet mode.
```

### `man`

官方给出的调用示例：`man u2boat`

```text
root@kali:~# man u2boat
U2BOAT(1)                   General Commands Manual                   U2BOAT(1)
NAME
     u2boat - Unified2 Binary Output & Alert Tool
SYNOPSIS
     u2boat [-t type] <infile> <outfile>
DESCRIPTION
     This  manual  page documents briefly the u2boat command.  This manual page
     was written for the Debian distribution because the original program  does
     not have a manual page.
     u2boat  is a utility that converts Snort's Unified2 logs to other formats.
     It was introduced in Snort due to the lack of  support  for  formats  that
     were present in the Snort 2.8.x releases.  Unified2 logs to other formats.
OPTIONS
     -t type
            Type  specifies  the type of output that the program should create.
            The only current valid option is 'pcap'
SEE ALSO
     snort (8)
AUTHOR
     This program was written by Ryan Jordan.
     This  manual  page  was  written  by  Javier  Fernandez-Sanguino  <jfs@de-
     bian.org>, for the Debian GNU/Linux system (but may be used by others).
                               12th December 2014                     U2BOAT(1)
```

### `man（示例）`

官方给出的调用示例：`man u2spewfoo`

```text
root@kali:~# man u2spewfoo
U2SPEWFOO(1)                General Commands Manual                U2SPEWFOO(1)
NAME
     u2spewfoo -  tool for dumping the contents of unified2 files to stdout
SYNOPSIS
     u2boat <infile>
DESCRIPTION
     This  manual  page  documents  briefly the u2spewfoo command.  This manual
     page was written for the Debian distribution because the original  program
     does not have a manual page.
     u2spewfoo  is  a lightweight tool for dumping the contents of Snort's Uni-
     fied2 log files to stdout. In order to use it Snort first has to  be  con-
     figured to use this format in its configuration file.
     The  tool will take the log file and dump the information on the events in
     Standard output. This information includes the event and relevant informa-
     tion about it (such as IP addresses and ports, the time the event was  de-
     tected, etc.) as well as the packet that triggered the event (if Snort has
     been configured to store a packet capture associated with events).
EXAMPLES
     To  use  it  run  it  against  a  unified2  log file by running: u2spewfoo
     snort.log
     The following is a sample output of this tool:
     (Event)
         sensor id: 0    event id: 4 event second: 1299698138    event microsecond: 146591
         sig id: 1   gen id: 1   revision: 0  classification: 0
         priority: 0 ip source: 10.1.2.3 ip destination: 10.9.8.7
         src port: 60710 dest port: 80   protocol: 6 impact_flag: 0  blocked: 0
     Packet
         sensor id: 0    event id: 4 event second: 1299698138
         packet second: 1299698138   packet microsecond: 146591
         linktype: 1 packet_length: 54
     [    0] 02 09 08 07 06 05 02 01 02 03 04 05 08 00 45 00  ..............E.
     [   16] 00 28 00 06 00 00 40 06 5C B7 0A 01 02 03 0A 09  .(....@........
     [   32] 08 07 ED 26 00 50 00 00 00 62 00 00 00 2D 50 10  ...&.P...b...-P.
     [   48] 01 00 A2 BB 00 00                                ......
     (ExtraDataHdr)
         event type: 4   event length: 33
     (ExtraData)
         sensor id: 0    event id: 2 event second: 1299698138
         type: 9 datatype: 1 bloblength: 9   HTTP URI: /
     (ExtraDataHdr)
         event type: 4   event length: 78
     (ExtraData)
         sensor id: 0    event id: 2 event second: 1299698138
         type: 10    datatype: 1 bloblength: 12  HTTP Hostname: example.com
SEE ALSO
     snort (8)
AUTHOR
     This program was written by Adam Keeton.
     This  manual  page  was  written  by  Javier  Fernandez-Sanguino  <jfs@de-
     bian.org>, for the Debian GNU/Linux system (but may be used by others).
                               12th December 2014                  U2SPEWFOO(1)
```

## 4. 实践清单

按顺序做完这五步，就能把工具从「装上」推进到「会用」：

- [ ] **1.** **装好并确认版本** —— `sudo apt install snort`，再执行 `snort --version` 2>/dev/null || `snort -V`
- [ ] **2.** **读官方帮助** —— `snort -h`，需要细节时 `man snort`
- [ ] **3.** **在自有靶场跑最小用例** —— 官方给出的调用形式是：`Usage:`
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/snort/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- **精讲教程**（含原理、参数详解、靶场实操与输出解读）：[snort](../../tools/tutorials/02-漏洞分析/snort.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/snort/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/snort/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
