# reglookup

> Utility to analysis for Windows NT-based registry RegLookup is a system to direct analysis of Windows NT-based registry files providing command line tools, a C API, and a Python module for accessing registry data structures. The project ha…

> **功能分类**：数字取证 ｜ **Kali 包**：`reglookup` ｜ **官方文档**：<https://www.kali.org/tools/reglookup/>

## 1. 安装

```bash
sudo apt update
sudo apt install reglookup
```

| 项目 | 内容 |
|------|------|
| 版本 | 1.0.1 |
| 架构 | any |
| 可执行命令 | `libregfi-dev`、`libregfi1t64`、`python3-pyregfi`、`reglookup`、`reglookup-recover`、`reglookup-timeline`、`reglookup-doc` |
| 依赖 | `libc6`、`libregfi1t64`、`libtalloc2` |
| 安装体积 | 87 KB |
| 官网 | <https://web.archive.org/web/20240804024044/http://projects.sentinelchicken.org/reglookup/> |
| 源码仓库 | <https://salsa.debian.org/pkg-security-team/reglookup> |
| 包追踪 | <https://pkg.kali.org/pkg/reglookup> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
libregfi-dev -h          # 查看用法
man libregfi-dev         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 7 个可执行命令，下面是官方页面内嵌的帮助原文。

### `man`

> 官方示例调用：`man reglookup`

```text
root@kali:~# man reglookup
reglookup(1)                                                       reglookup(1)
NAME
     reglookup - Windows NT+ registry reader/lookup tool
SYNOPSIS
     reglookup [options] registry-file
DESCRIPTION
     reglookup is designed to read windows registry elements and print them out
     to stdout in a CSV-like format. It has filtering options to narrow the fo-
     cus  of the output. This tool is designed to work with on Windows NT-based
     registries.
OPTIONS
     reglookup accepts the following parameters:
     -p prefix-filter
            Specify a path prefix filter. Only keys/values under this  registry
            path will be output.
     -t type-filter
            Specify a type filter. Only elements which match this registry data
            type  will  be printed. Acceptable values are: NONE, SZ, EXPAND_SZ,
            BINARY, DWORD,  DWORD_BE,  LINK,  MULTI_SZ,  RSRC_LIST,  RSRC_DESC,
            RSRC_REQ_LIST, QWORD and KEY .
     -h     Enables the printing of a column header row. (default)
     -i     Printed  values inherit the timestamp of their parent key, which is
            printed along with them. Note that this timestamp is not  necessar-
            ily  meaningful  for  any given value values because timestamps are
            saved on keys only and you cannot tell which value has  been  modi-
            fied  since  a  change to any value of a given key would update the
            time stamp.
     -H     Disables the printing of a column header row.
     -s     Adds five additional columns to output containing information  from
            key  security  descriptors and rarely used fields. The columns are:
            owner, group, sacl, dacl, class.  (This feature's  output  has  not
            been extensively tested.)
     -S     Disables the printing of security descriptor information. (default)
     -v     Verbose output.
     registry-file
            Required  argument.  Specifies the location of the registry file to
            read. The system registry files should  be  found  under:  %System-
            Root%/system32/config.
OUTPUT
     reglookup  generates  comma-separated values (CSV) and writes them to std-
     out. The format is designed to simplify parsing algorithms of other  tools
     by  quoting  CSV  special  characters  using  a common hexadecimal format.
     Specifically, special characters or non-ascii bytes are converted to "%XX"
     where XX is the hexadecimal value for the byte.
     The number of columns or fields in each line is fixed for a given  run  of
     the program, but may vary based on the command line options provided.  See
     the  header  line  for  information on which fields are available and what
     they contain.
     Some fields in some lines may contain sub-fields which require  additional
     delimiters.  If  these  sub-delimiters occur in these sub-fields, they are
     also encoded in the same way as commas or other  special  characters  are.
     Currently,  the  second,  third, and fourth level delimiters are "|", ":",
     and " ", respectively. These are particularly important to  take  note  of
     when  security  attributes  are printed. Please note that these delimiters
     may occur in fields that are not sub-delimited, and should not  be  inter-
     preted as special.
     Security  attributes  of  registry  keys have a complex structure which is
     outlined here. Each key will generally have an associated ACL (Access Con-
     trol List), which is made up of ACEs (Access Control Entries). Each ACE is
     delimited by the secondary delimiter  mentioned  above,  "|".  The  fields
     within an ACE are delimited by the third-level delimiter, ":", and consist
     of  a SID, the ACE type (ALLOW, DENY, etc), a list of access rights, and a
     list of flags. The last two fields are delimited by the  fourth-level  de-
     limiter  "  ". These final lists are simply human-readable interpretations
     of bits. The access rights abbreviations are listed below along with their
     Microsoft-assigned names:
           QRY_VAL        KEY_QUERY_VALUE
           SET_VAL        KEY_SET_VALUE
           CREATE_KEY     KEY_CREATE_SUB_KEY
           ENUM_KEYS      KEY_ENUMERATE_SUB_KEYS
           NOTIFY         KEY_NOTIFY
           CREATE_LNK     KEY_CREATE_LINK
           WOW64_64       KEY_WOW64_64KEY
           WOW64_32       KEY_WOW64_32KEY
           DELETE         DELETE
           R_CONT         READ_CONTROL
           W_DAC          WRITE_DAC
           W_OWNER        WRITE_OWNER
           SYNC      SYNCHRONIZE
           SYS_SEC        ACCESS_SYSTEM_SECURITY
           MAX_ALLWD      MAXIMUM_ALLOWED
           GEN_A          GENERIC_ALL
           GEN_X          GENERIC_EXECUTE
           GEN_W          GENERIC_WRITE
           GEN_R          GENERIC_READ
     And the meaning of each flag is:
           OI   Object Inherit
           CI   Container Inherit
           NP   Non-Propagate
           IO   Inherit Only
           IA   Inherited ACE
     Please see the following references for more information:
             http://msdn2.microsoft.com/en-gb/library/ms724878.aspx
             http://msdn2.microsoft.com/en-gb/library/aa374892.aspx
             http://msdn2.microsoft.com/en-us/library/aa772242.aspx
             http://support.microsoft.com/kb/220167
     Note that some of the bits listed above have either not been allocated  by
     Microsoft,  or  simply aren't documented. If any bits are set in the above
     two fields that aren't recognized, a hexadecimal representation of all  of
     these  mystery  bits  will be included in the output. For instance, if the
     lowest bit and third lowest bit were not recognized while being  set,  the
     number "0x5" would be included as an element in the list.
     While  the  ACL/ACE  output  format  is mostly stable at this point, minor
     changes may be introduced in future versions.
EXAMPLES
     To read and print the contents of an entire system registry file:
          reglookup /mnt/win/c/WINNT/system32/config/system
     To limit the output to just those entries under the Services key:
          reglookup -p /ControlSet002/Services /mnt/win/c/WINNT/system32/config/system
     To limit the output to all registry values of type BINARY:
          reglookup -t BINARY /mnt/win/c/WINNT/system32/config/system
     And to limit the output to BINARY values under the Services key:
          reglookup -t BINARY -p /ControlSet002/Services /mnt/win/c/WINNT/system32/config/system
BUGS
     This program has been smoke-tested against  most  current  Windows  target
     platforms,  but  a  comprehensive  test  suite has not yet been developed.
     (Please report results to the development mailing list  if  you  encounter
     any bugs. Sample registry files and/or patches are greatly appreciated.)
     The SID conversions haven't been carefully checked for accuracy.
     The  MTIME  conversions appear correctly produce the stored UTC timestamp.
     However, due to the periodicity of registry writes, and the complexity  of
     the  conversion,  a small amount of error (on the order of seconds) may be
     possible. The documentation available online from Microsoft on this  field
     is very poor.
     For   more  information  on  registry  format  details,  see:  http://sen-
     tinelchicken.com/research/registry_format/
CREDITS
     This program was initially based on editreg.c by Richard  Sharpe.  It  has
     since  been rewritten to use a modified version the regfio library written
     by Gerald Carter. Heavy modifications to the library and the original com-
     mand line interface have been done by Timothy D. Morgan.
     Please see source code for a full list of copyrights.
LICENSE
     Please see the file "LICENSE" included with this software distribution.
     This program is distributed in the hope that it will be useful, but  WITH-
     OUT  ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
     FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License  ver-
     sion 3 for more details.
SEE ALSO
     reglookup-timeline(1) reglookup-recover(1)
File Conversion Utilities        7 October 2025                    reglookup(1)
```

### `man reglookup-recover`

> 官方示例调用：`man reglookup-recover`

```text
root@kali:~# man reglookup-recover
reglookup(1)                                                       reglookup(1)
NAME
     reglookup-recover - Windows NT+ registry deleted data recovery tool
SYNOPSIS
     reglookup-recover [options] registry-file
DESCRIPTION
     reglookup-recover  attempts  to  scour a Windows registry hive for deleted
     data structures and outputs those found in a CSV-like format.
OPTIONS
     reglookup-recover accepts the following parameters:
     -v     Verbose output.
     -h     Enables the printing of a column header row. (default)
     -H     Disables the printing of a column header row.
     -l     Display cells which could not  be  interpreted  as  valid  registry
            structures at the end of the output.
     -L     Do  not  display cells which could not be interpreted as valid reg-
            istry structures. This is the default behavior.
     -r     Display raw cell contents for cells which were interpreted  as  in-
            tact  data  structures.  This  additional output will appear on the
            same line as the interpreted data.
     -R     Do not display raw cell contents for cells which  were  interpreted
            as intact data structures. This is the default behavior.
     registry-file
            Required  argument.  Specifies the location of the registry file to
            read. The system registry files should  be  found  under:  %System-
            Root%/system32/config.
OUTPUT
     reglookup-recover generates a comma-separated values (CSV) like output and
     writes  it  to  stdout.  For more information on the syntax of the general
     format, see reglookup(1).
     This tool is new and the output format, particularly the included columns,
     may change in future revisions. When  this  format  stablizes,  additional
     documentation will be included here.
EXAMPLES
     To dump the recoverable contents of a system registry hive:
          reglookup-recover /mnt/win/c/WINDOWS/system32/config/system
     Extract  all  available unallocated data, including unparsable unallocated
     space and the raw data associated with parsed  cells  in  a  user-specific
     registry:
          reglookup-recover -r -l '/mnt/win/c/Documents and Settings/user/NTUSER.DAT'
BUGS
     This  program  has  been  smoke-tested against most current Windows target
     platforms, but a comprehensive test suite  has  not  yet  been  developed.
     (Please  report  results  to the development mailing list if you encounter
     any bugs. Sample registry files and/or patches are greatly appreciated.)
     This program is new as of RegLookup release 0.9.0 and should be considered
     unstable.
     For more information on registry format details  and  the  recovery  algo-
     rithm, see:
     http://sentinelchicken.com/research/registry_format/           http://sen-
     tinelchicken.com/research/registry_recovery/
CREDITS
     This program was written by Timothy D. Morgan.
LICENSE
     Please see the file "LICENSE" included with this software distribution.
     This program is distributed in the hope that it will be useful, but  WITH-
     OUT  ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
     FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License  ver-
     sion 3 for more details.
SEE ALSO
     reglookup-timeline(1) reglookup-recover(1)
File Conversion Utilities        7 October 2025                    reglookup(1)
```

### `reglookup-timeline`

> 官方示例调用：`reglookup-timeline -h`

```text
root@kali:~# reglookup-timeline -h
MTIME,FILE,PATH
```

## 4. 实践清单

按顺序做完这五步，就能把工具从「装上」推进到「会用」：

- [ ] **1.** **装好并确认版本** —— `sudo apt install reglookup`，再执行 `libregfi-dev --version` 2>/dev/null || `libregfi-dev -V`
- [ ] **2.** **读官方帮助** —— `libregfi-dev -h`，需要细节时 `man libregfi-dev`
- [ ] **3.** **在自有靶场跑最小用例** —— 用 `libregfi-dev -h` 里最简单的那个子命令试一次
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/reglookup/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/forensics.md`](../../tools/by-attack/forensics.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/reglookup/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/reglookup/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
