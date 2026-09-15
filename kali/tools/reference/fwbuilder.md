# fwbuilder

> Firewall administration tool GUI Firewall Builder consists of an object-oriented GUI and a set of policy compilers for various firewall platforms. In Firewall Builder, firewall policy is a set of rules, each rule consists of abstract objec…

> **功能分类**：防护 ｜ **Kali 包**：`fwbuilder` ｜ **官方文档**：<https://www.kali.org/tools/fwbuilder/>

## 1. 安装

```bash
sudo apt update
sudo apt install fwbuilder
```

| 项目 | 内容 |
|------|------|
| 版本 | 5.3.7 |
| 架构 | any |
| 可执行命令 | `fwbuilder`、`fwb_compile_all`、`fwb_iosacl`、`fwb_ipf`、`fwb_ipfw`、`fwb_ipt`、`fwb_pf`、`fwb_pix`、`fwb_procurve_acl`、`fwbedit`、`fwbuilder-common`、`fwbuilder-doc` |
| 依赖 | `fwbuilder-common`、`libc6`、`libgcc-s1`、`libqt5core5t64` |
| 安装体积 | 39.82 MB |
| 官网 | <https://github.com/fwbuilder/fwbuilder/> |
| 源码仓库 | <https://salsa.debian.org/debian/fwbuilder> |
| 包追踪 | <https://pkg.kali.org/pkg/fwbuilder> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
fwbuilder -h          # 查看用法
man fwbuilder         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 12 个可执行命令，下面是官方页面内嵌的帮助原文。

### `man`

> 官方示例调用：`man fwb_compile_all`

```text
root@kali:~# man fwb_compile_all
fwb_compile_all(1)              Firewall Builder             fwb_compile_all(1)
NAME
     fwb_compile_all - Wrapper script that compiles policies for multiple fire-
     wall objects
SYNOPSIS
     fwb_compile_all -ffile.xml [-dwdir] [-av] [obj[ obj ...]]
DESCRIPTION
     fwb_compile_all  is  a  wrapper  script that compiles policies for several
     firewall objects in one batch job. This script takes a  list  of  firewall
     object  names on the command line (or '-a' command line option, see below)
     and calls policy compiler for each one. The  script  correctly  determines
     which policy compiler is needed depending on the firewall platform of each
     object.
OPTIONS
     -a     The  script processes all firewall objects in the "/Firewalls" sub-
            tree.
     -d wdirSpecify working directory.  Compiler  creates  file  with  iptables
            script in this directory.  If this parameter is missing, then ipta-
            bles script will be placed in the current working directory.
     -f FILESpecify the name of the data file to be processed.
     -v     Script  passes this option to the compiler, this makes it print di-
            agnostic messages indicating its progress.
URL
     Firewall Builder home page is located at the following URL: http://www.fw-
     builder.org/
BUGS
     Please report bugs using bug tracking system on SourceForge:
     http://sourceforge.net/tracker/?group_id=5314&atid=105314
SEE ALSO
     fwbuilder(1), fwb_ipt(1) fwb_ipf(1) fwb_pf(1) fwbedit(1), fwblookup(1)
FWB                                                          fwb_compile_all(1)
```

### `man fwb_iosacl`

> 官方示例调用：`man fwb_iosacl`

```text
root@kali:~# man fwb_iosacl
fwb_pix(1)                      Firewall Builder                     fwb_pix(1)
NAME
     fwb_ipt - Policy compiler for Cisco IOS ACL
SYNOPSIS
     fwb_iosacl [-vV] [-d wdir] [-4] [-6] [-i] -f data_file.xml object_name
DESCRIPTION
     fwb_iosacl  is firewall policy compiler component of Firewall Builder (see
     fwbuilder(1)). Compiler reads objects definitions and firewall description
     from the data file specified with  "-f"  option  and  generates  resultant
     Cisco IOS ACL configuration file. The configuration is written to the file
     with  the name the same as the name of the firewall object, plus extension
     ".fw". Compiler generates extended access lists for Cisco routers  running
     IOS  v12.x  using  "ip access-list <name>" syntax. Compiler also generates
     "ip access-group" commands to assign access lists to interfaces. Generated
     ACL configuration can be uploaded to the router manually or using built-in
     installer in the fwbuilder(1) GUI.
     The data file and the name of the firewall objects must  be  specified  on
     the command line. Other command line parameters are optional.
OPTIONS
     -4     Generate  iptables script for IPv4 part of the policy. If any rules
            of the firewall refer to IPv6 addresses, compiler will  skip  these
            rules.   Options  "-4" and "-6" are exclusive. If neither option is
            used, compiler tries to generate both parts of the script, although
            generation of the IPv6 part is controlled  by  the  option  "Enable
            IPv6  support"  in  the  "IPv6" tab of the firewall object advanced
            settings dialog.  This option is off by default.
     -6     Generate iptables script for IPv6 part of the policy. If any  rules
            of  the  firewall refer to IPv6 addresses, compiler will skip these
            rules.
     -f FILESpecify the name of the data file to be processed.
     -d wdirSpecify working directory. Compiler creates file with ACL  configu-
            ration  in this directory.  If this parameter is missing, then gen-
            erated ACL will be placed in the current working directory.
     -v     Be verbose: compiler prints diagnostic messages when it works.
     -V     Print version number and quit.
     -i     When this option is present, the last argument on the command  line
            is supposed to be firewall object ID rather than its name
URL
     Firewall Builder home page is located at the following URL: http://www.fw-
     builder.org/
BUGS
     Please report bugs using bug tracking system on SourceForge:
     http://sourceforge.net/tracker/?group_id=5314&atid=105314
SEE ALSO
     fwbuilder(1), fwb_pix(1), fwb_ipfw(1), fwb_ipf(1), fwb_ipt(1) fwb_pf(1)
FWB                                                                  fwb_pix(1)
```

### `fwb_ipf`

> 官方示例调用：`fwb_ipf -h`

```text
root@kali:~# fwb_ipf -h
Firewall Builder:  policy compiler for ipfilter
Version 5.3.7
Usage: fwb_ipf [-x] [-v] [-V] [-f filename.xml] [-o output.fw] [-d destdir] [-m] firewall_object_name
```

### `fwb_ipfw`

> 官方示例调用：`fwb_ipfw -h`

```text
root@kali:~# fwb_ipfw -h
Firewall Builder:  policy compiler for ipfw
Version 5.3.7
Usage: fwb_ipfw [-x] [-v] [-V] [-f filename.xml] [-o output.fw] [-d destdir] [-m] firewall_object_name
```

### `fwb_ipt`

> 官方示例调用：`fwb_ipt -h`

```text
root@kali:~# fwb_ipt -h
Firewall Builder:  policy compiler for Linux 2.4.x and 2.6.x iptables
Version 5.3.7
Usage: fwb_ipt [-x level] [-v] [-V] [-q] [-f filename.xml] [-d destdir] [-D datadir ] [-m] [-4|-6] firewall_object_name
```

### `fwb_pf`

> 官方示例调用：`fwb_pf -h`

```text
root@kali:~# fwb_pf -h
Firewall Builder:  policy compiler for OpenBSD PF
Version 5.3.7
Usage: fwb_pf [-x] [-v] [-V] [-f filename.xml] [-o output.fw] [-d destdir] [-D datadir] [-m] [-4|-6] firewall_object_name
```

### `fwb_pix`

> 官方示例调用：`fwb_pix -h`

```text
root@kali:~# fwb_pix -h
Firewall Builder:  policy compiler for Cisco PIX firewall (with support for FWSM)
Copyright 2002-2009 NetCitadel, LLC
Version 5.3.7
Usage: fwb_pix [-tvV] [-f filename.xml] [-d destdir] [-o output.fw] firewall_object_name
```

### `fwb_procurve_acl`

> 官方示例调用：`fwb_procurve_acl -h`

```text
root@kali:~# fwb_procurve_acl -h
Firewall Builder:  policy compiler for HP ProCurve ACL
Copyright 2010 NetCitadel, LLC
Version 5.3.7
Usage: fwb_procurve_acl [-tvV] [-f filename.xml] [-d destdir] [-o output.fw] firewall_object_name
```

### `fwbedit`

> 官方示例调用：`fwbedit -h`

```text
root@kali:~# fwbedit -h
Firewall Builder:  general purpose object tree editing tool
Version 5.3.7
Usage: fwbedit command [options]
Command is one of:
      new         create new object
      delete      delete object
      modify      modify object
      list        print object
      add         add object to a group
      remove      remove object from a group
      upgrade     upgrade data file
      checktree   check object tree and repair if necessary
      merge       merge one data file into another
      import      import firewall configuration (iptables, CIsco IOS,
                  Cisco PIX, ASA and FWSM)
Type   'fwbedit command' to get summary of options for the command
```

### `man fwbuilder`

> 官方示例调用：`man fwbuilder`

```text
root@kali:~# man fwbuilder
fwbuilder(1)                    Firewall Builder                   fwbuilder(1)
NAME
     fwbuilder - Multiplatform firewall configuration tool
SYNOPSIS
     /usr/bin/fwbuilder  [-ffile.fwb]  [-d]  [-h] [-ofile] [-Pobject_name] [-r]
     [-v]
DESCRIPTION
     fwbuilder is the  Graphic  User  Interface  (GUI)  component  of  Firewall
     Builder.
     Firewall Builder consists of a GUI and set of policy compilers for various
     firewall  platforms. It helps users maintain a database of objects and al-
     lows policy editing using simple drag-and-drop operations.  GUI  generates
     firewall  description in the form of XML file, which compilers then inter-
     pret and generate platform-specific code. Several algorithms are  provided
     for  automated  network objects discovery and bulk import of data. The GUI
     and policy compilers are completely independent, this provides for a  con-
     sistent abstract model and the same GUI for different firewall platforms.
     Firewall  Builder supports firewalls based on iptables (Linux kernel 2.4.x
     and 2.6.x, see fwb_ipt(1)), ipfilter (variety of platforms including *BSD,
     Solaris  and  others,  see  fwb_ipf(1)),  pf  (OpenBSD  and  FreeBSD,  see
     fwb_pf(1)),  ipfw (FreeBSD and others), Cisco PIX (v6.x and 7.x) and Cisco
     IOS extended access lists.
OPTIONS
     -f FILESpecify the name of the file to be loaded when program starts.
     -r     When this command line option is given in combination with -f file,
            the program automatically opens RCS head revision of  the  file  if
            file is in RCS. If file is not in RCS, this option does nothing and
            the file is opened as usual.
     -d     Turns  on  debug mode. Note that in this mode the program generates
            lots of output on standard error. This is used for debugging.
     -h     Prints brief help message
     -o fileSpecify the name of the file for the print output, see option "-P".
     -P object_name
            Print rules and objects for the firewall object  "object_name"  and
            immediately  exit.  The  program does not go into interactive mode.
            Print output will be placed in the file specified with "-o" option.
            If file name is not given with option "-o", print output is  stored
            in the file "print.pdf" in the current directory.
FILES
     $HOME/.qt/firewallbuilder2rc
            Fwbuilder v2.1 stores user preferences in this file.
     $HOME/.config/netcitadel.com/Firewall Builder.conf
            Fwbuilder v3.0 stores user preferences in this file.
URL
     Firewall Builder home page is located at the following URL: http://www.fw-
     builder.org/
BUGS
     Please report bugs using bug tracking system on SourceForge:
     http://sourceforge.net/tracker/?group_id=5314&atid=105314
SEE ALSO
     fwblookup(1), fwb_ipt(1), fwb_ipf(1), fwb_pf(1)
FWB                                                                fwbuilder(1)
```

## 4. 实践清单

按顺序做完这五步，就能把工具从「装上」推进到「会用」：

- [ ] **1.** **装好并确认版本** —— `sudo apt install fwbuilder`，再执行 `fwbuilder --version` 2>/dev/null || `fwbuilder -V`
- [ ] **2.** **读官方帮助** —— `fwbuilder -h`，需要细节时 `man fwbuilder`
- [ ] **3.** **在自有靶场跑最小用例** —— 官方给出的调用形式是：`Usage: fwb_ipf [-x] [-v] [-V] [-f filename.xml] [-o output.fw] [-d destdir] [-m] firewall_object_name`
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/fwbuilder/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/fwbuilder/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/fwbuilder/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
