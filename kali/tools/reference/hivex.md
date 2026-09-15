# hivex

> Utilities for reading and writing Windows Registry hives libhivex is a self-contained library for reading and writing Windows Registry “hive” binary files. This package contains a few command line programs that utilize libhivex.

> **功能分类**：数字取证 ｜ **Kali 包**：`hivex` ｜ **官方文档**：<https://www.kali.org/tools/hivex/>

## 1. 安装

```bash
sudo apt update
sudo apt install libhivex-bin
```

| 项目 | 内容 |
|------|------|
| 版本 | 1.3.24 |
| 架构 | any |
| 可执行命令 | `libhivex-bin`、`hivexget`、`hivexml`、`hivexsh`、`libhivex-dev`、`libhivex-ocaml`、`libhivex-ocaml-dev`、`libhivex0`、`libwin-hivex-perl`、`hivexregedit`、`python3-hivex`、`ruby-hivex` |
| 依赖 | `libc6`、`libhivex0`、`libreadline8t64`、`libxml2-16`、`hivexget` |
| 安装体积 | 244 KB |
| 官网 | <http://libguestfs.org/> |
| 源码仓库 | <https://salsa.debian.org/libvirt-team/hivex> |
| 包追踪 | <https://pkg.kali.org/pkg/hivex> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
libhivex-bin -h          # 查看用法
man libhivex-bin         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 12 个可执行命令，下面是官方页面内嵌的帮助原文。

### `man`

> 官方示例调用：`man hivexget`

```text
root@kali:~# man hivexget
hivexget(1)                     Windows Registry                    hivexget(1)
NAME
     hivexget - Get subkey from a Windows Registry binary "hive" file
SYNOPSIS
      hivexget hivefile '\Path\To\SubKey'
      hivexget hivefile '\Path\To\SubKey' name
NOTE
     This is a low-level tool.  For a more convenient way to navigate the Win-
     dows Registry in Windows virtual machines, see virt-win-reg(1).  For
     proper regedit formatting, use hivexregedit(1).
DESCRIPTION
     This program navigates through a Windows Registry binary "hive" file and
     extracts either all the (key, value) data pairs stored in that subkey or
     just the single named data item.
     In the first form:
      hivexget hivefile '\Path\To\SubKey'
     "hivefile" is some Windows Registry binary hive, and "\Path\To\Subkey" is
     a path within that hive.  NB the path is relative to the top of this hive,
     and is not the full path as you would use in Windows (eg. "HKEY_LOCAL_MA-
     CHINE\SYSTEM" is not a valid path).
     If the subkey exists, then the output lists all data pairs under this sub-
     key, in a format similar to "regedit" in Windows.
     In the second form:
      hivexget hivefile '\Path\To\SubKey' name
     "hivefile" and path are as above.  "name" is the name of the value of in-
     terest (use "@" for the default value).
     The corresponding data item is printed "raw" (ie. no processing or escap-
     ing) except:
     1.  If it's a string we will convert it from Windows UTF-16 to UTF-8, if
         this conversion is possible.  The string is printed with a single
         trailing newline.
     2.  If it's a multiple-string value, each string is printed on a separate
         line.
     3.  If it's a numeric value, it is printed as a decimal number.
SEE ALSO
     hivex(3), hivexml(1), hivexsh(1), hivexregedit(1), virt-win-reg(1),
     guestfs(3), <http://libguestfs.org/>, virt-cat(1), virt-edit(1).
AUTHORS
     Richard W.M. Jones ("rjones at redhat dot com")
COPYRIGHT
     Copyright (C) 2009 Red Hat Inc.
     This program is free software; you can redistribute it and/or modify it
     under the terms of the GNU General Public License as published by the Free
     Software Foundation; either version 2 of the License, or (at your option)
     any later version.
     This program is distributed in the hope that it will be useful, but WITH-
     OUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
     FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for
     more details.
     You should have received a copy of the GNU General Public License along
     with this program; if not, write to the Free Software Foundation, Inc., 51
     Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
hivex-1.3.24                       2026-08-02                       hivexget(1)
```

### `man hivexml`

> 官方示例调用：`man hivexml`

```text
root@kali:~# man hivexml
hivexml(1)                      Windows Registry                     hivexml(1)
NAME
     hivexml - Convert Windows Registry binary "hive" into XML
SYNOPSIS
      hivexml [-dk] hivefile > output.xml
DESCRIPTION
     This program converts a single Windows Registry binary "hive" file into a
     self-describing XML format.
OPTIONS
     -d  Enable lots of debug messages.  If you find a Registry file that this
         program cannot parse, please enable this option and post the complete
         output and the Registry file in your bug report.
     -k  Keep going even if we find errors in the Registry file.  This skips
         over any parts of the Registry that we cannot read.
     -u  Use heuristics to tolerate certain levels of corruption within hives.
         This is unsafe but may allow to export/merge valid keys/values in an
         othewise corrupted hive.
SEE ALSO
     hivex(3), hivexget(1), hivexsh(1), hivexregedit(1), virt-win-reg(1),
     guestfs(3), <http://libguestfs.org/>, virt-cat(1), virt-edit(1).
AUTHORS
     Richard W.M. Jones ("rjones at redhat dot com")
COPYRIGHT
     Copyright (C) 2009 Red Hat Inc.
     This program is free software; you can redistribute it and/or modify it
     under the terms of the GNU General Public License as published by the Free
     Software Foundation; either version 2 of the License, or (at your option)
     any later version.
     This program is distributed in the hope that it will be useful, but WITH-
     OUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
     FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for
     more details.
     You should have received a copy of the GNU General Public License along
     with this program; if not, write to the Free Software Foundation, Inc., 51
     Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
hivex-1.3.24                       2026-08-02                        hivexml(1)
```

### `man hivexsh`

> 官方示例调用：`man hivexsh`

```text
root@kali:~# man hivexsh
hivexsh(1)                      Windows Registry                     hivexsh(1)
NAME
     hivexsh - Windows Registry hive shell
SYNOPSIS
      hivexsh [-options] [hivefile]
DESCRIPTION
     This program provides a simple shell for navigating Windows Registry
     'hive' files.  It uses the hivex library for access to these binary files.
     Firstly you will need to provide a hive file from a Windows operating sys-
     tem.  The hive files are usually located in "C:\Windows\System32\Config"
     and have names like "software", "system" etc (without any file extension).
     For more information about hive files, read hivex(3).  For information
     about downloading files from virtual machines, read virt-cat(1) and guest-
     fish(1).
     You can provide the name of the hive file to examine on the command line.
     For example:
      hivexsh software
     Or you can start "hivexsh" without any arguments, and immediately use the
     "load" command to load a hive:
      $ hivexsh
      Welcome to hivexsh, the hivex interactive shell for examining
      Windows Registry binary hive files.
      Type: 'help' for help with commands
            'quit' to quit the shell
      > load software
      software\>
     Navigate through the hive's keys using the "cd" command, as if it con-
     tained a filesystem, and use "ls" to list the subkeys of the current key.
     Other commands are listed below.
OPTIONS
     -d  Enable lots of debug messages.  If you find a Registry file that this
         program cannot parse, please enable this option and post the complete
         output and the Registry hive file in your bug report.
     -f filename
         Read commands from "filename" instead of stdin.  To write a hivexsh
         script, use:
          #!/usr/bin/hivexsh -f
     -u  Use heuristics to tolerate certain levels of corruption within hives.
         This is unsafe but may allow to export/merge valid keys/values in an
         othewise corrupted hive.
     -w  If this option is given, then writes are allowed to the hive (see
         "commit" command below, and the discussion of modifying hives in
         "WRITING TO HIVE FILES" in hivex(3)).
         Important Note: Even if you specify this option, nothing is written to
         a hive unless you call the "commit" command.  If you exit the shell
         without committing, all changes will be discarded.
         If this option is not given, then write commands are disabled.
COMMANDS
     add name
         Add a subkey named "name" below the current node.  The name may con-
         tain spaces and punctuation characters, and does not need to be
         quoted.
         The new key will have no subkeys and no values (see "setval").
         There must be no existing subkey called "name", or this command will
         fail.  To replace an existing subkey, delete it first like this:
          cd name
          del
     cd path
         Change to the subkey "path".  Use Windows-style backslashes to sepa-
         rate path elements, and start with a backslash in order to start from
         the root of the hive.  For example:
          cd \Classes\*
         moves from the root node, to the "Classes" node, to the "*" node.  If
         you were already at the root node, you could do this instead:
          cd Classes\*
         or even:
          cd Classes
          cd *
         Path elements (node names) are matched case insensitively, and charac-
         ters like space, "*", and "?" have no special significance.
         "cd .." may be used to go to the parent directory.
         "cd" without any arguments prints the current path.
         Be careful with "cd \" since the readline library has an undocumented
         behaviour where it will think the final backslash is a continuation
         (it reads the next line of input and appends it).  Put a single space
         after the backslash.
     close | unload
         Close the currently loaded hive.
         If you modified the hive, all uncommitted writes are lost when you
         call this command (or if the shell exits).  You have to call "commit"
         to write changes.
     commit [newfile]
         Commit changes to the hive.  If the optional "newfile" parameter is
         supplied, then the hive is written to that file, else the original
         file is overwritten.
         Note that you have to specify the "-w" flag, otherwise no writes are
         allowed.
     del Delete the current node and everything beneath it.  The current direc-
         tory is moved up one level (as if you did "cd ..") after this command.
         You cannot delete the root node.
     exit | quit
         Exit the shell.
     load hivefile
         Load the binary hive named "hivefile".  The currently loaded hive, if
         any, is closed.  The current directory is changed back to the root
         node.
     ls  List the subkeys of the current hive Registry key.  Note this command
         does not take any arguments.
     lsval [key]
         List the (key, value) pairs of the current hive Registry key.  If no
         argument is given then all pairs are displayed.  If "key" is given,
         then the value of the named key is displayed.  If "@" is given, then
         the value of the default key is displayed.
     setval nrvals
         This command replaces all (key, value) pairs at the current node with
         the values in subsequent input.  "nrvals" is the number of values (ie.
         (key, value) pairs), and any existing values at this node are deleted.
         So "setval 0" just deletes any values at the current node.
         The command reads 2 * nrvals lines of input, with each pair of lines
         of input corresponding to a key and a value to add.
         For example, the following setval command replaces whatever is at the
         current node with two (key, value) pairs.  The default key is set to
         the UTF16-LE-encoded string "abcd".  The other value is named "ANum-
         ber" and is a little-endian DWORD 0x12345678.
          setval 2
          @
          string:abcd
          ANumber
          dword:12345678
         The first line of each pair is the key (the special key "@" means the
         default key, but you can also use a blank line).
         The second line of each pair is the value, which has a special format
         "type:value" with possible types summarized in the table below:
          none                 No data is stored, and the type is set to 0.
          string:abc           "abc" is stored as a UTF16-LE-encoded
                               string (type 1).  Note that only 7 bit
                               ASCII strings are supported as input.
          expandstring:...     Same as string but with type 2.
          dword:0x01234567     A DWORD (type 4) with the hex value
                               0x01234567.  You can also use decimal
                               or octal numbers here.
          qword:0x0123456789abcdef
                               A QWORD (type 11) with the hex value
                               0x0123456789abcdef.  You can also use
                               decimal or octal numbers here.
          hex:<type>:<hexbytes>
          hex:1:41,00,42,00,43,00,44,00,00,00
                               This is the generic way to enter any
                               value.  <type> is the integer value type.
                               <hexbytes> is a list of pairs of hex
                               digits which are treated as bytes.
                               (Any non-hex-digits here are ignored,
                               so you can separate bytes with commas
                               or spaces if you want).
EXAMPLE
      $ guestfish --ro -i Windows7
      ><fs> download win:c:\windows\system32\config\software software
      ><fs> quit
      $ hivexsh software
      Welcome to hivexsh, the hivex interactive shell for examining
      Windows Registry binary hive files.
      Type: 'help' for help with commands
            'quit' to quit the shell
      software\> ls
      ATI Technologies
      Classes
      Clients
      Intel
      Microsoft
      ODBC
      Policies
      RegisteredApplications
      Sonic
      Wow6432Node
      software\> quit
SEE ALSO
     hivex(3), hivexget(1), hivexml(1), virt-win-reg(1), guestfs(3),
     <http://libguestfs.org/>, virt-cat(1), virt-edit(1).
AUTHORS
     Richard W.M. Jones ("rjones at redhat dot com")
COPYRIGHT
     Copyright (C) 2009-2010 Red Hat Inc.
     This program is free software; you can redistribute it and/or modify it
     under the terms of the GNU General Public License as published by the Free
     Software Foundation; either version 2 of the License, or (at your option)
     any later version.
     This program is distributed in the hope that it will be useful, but WITH-
     OUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
     FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for
     more details.
     You should have received a copy of the GNU General Public License along
     with this program; if not, write to the Free Software Foundation, Inc., 51
     Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
hivex-1.3.24                       2026-08-02                        hivexsh(1)
```

### `hivexregedit`

> 官方示例调用：`hivexregedit -h`

```text
root@kali:~# hivexregedit -h
Usage:
     hivexregedit --merge [--prefix prefix] [--encoding enc] \
             hivefile [regfile]
     hivexregedit --export [--prefix prefix] hivefile key > regfile
Options:
    --help
        Display help.
    --debug
        Enable debugging in the hivex library. This is useful for diagnosing
        bugs and also malformed hive files.
    --merge
         hivexregedit --merge [--prefix prefix] [--encoding enc] \
                 hivefile [regfile]
        Merge "regfile" (a regedit-format text file) into the hive
        "hivefile". If "regfile" is omitted, then the program reads from
        standard input. (Also you can give multiple input files).
        "--prefix" specifies the Windows Registry prefix. It is almost
        always necessary to use this when dealing with real hive files.
        "--encoding" specifies the encoding for unmarked strings in the
        input. It defaults to "UTF-16LE" which should work for recent
        versions of Windows. Another possibility is to use "ASCII".
    --export
         hivexregedit --export [--prefix prefix] hivefile key > regfile
        "key" is a path within the hive "hivefile". (The key should not
        contain any prefix and should be quoted to defend backslashes from
        the shell). The key is exported, recursively, to standard output in
        the textual regedit format.
        "--prefix" specifies the Windows Registry prefix. It is almost
        always necessary to use this when dealing with real hive files.
    --prefix prefix
        Hive files and Windows Registry key names are indirectly related.
        For example, inside the software hive, all keys are stored relative
        to "HKEY_LOCAL_MACHINE\SOFTWARE". Thus
        "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft" appears in the hive file as
        "\Microsoft".
        The hive format itself does not store this prefix, so you have to
        supply it based on outside knowledge. (virt-win-reg(1), amongst
        other things, already knows about this).
        Usually it is sufficient to pass the parameter "--prefix
        'HKEY_LOCAL_MACHINE\SOFTWARE'" or similar when doing merges and
        exports.
    --encoding UTF-16LE|ASCII
        When merging (only), you may need to specify the encoding for
        strings to be used in the hive file. This is explained in detail in
        "ENCODING STRINGS" in Win::Hivex::Regedit(3).
        The default is to use UTF-16LE, which should work with recent
        versions of Windows.
    --unsafe-printable-strings
        When exporting (only), assume strings are UTF-16LE and print them as
        strings instead of hex sequences. Remove the final zero codepoint
        from strings if present.
        This is unsafe and does not preserve the fidelity of strings in the
        original hive for various reasons:
        *   Assumes the original encoding is UTF-16LE. ASCII strings and
            strings in other encodings will be corrupted by this
            transformation.
        *   Assumes that everything which has type 1 or 2 is really a string
            and that everything else is not a string, but the type field in
            real hives is not reliable.
        *   Loses information about whether a zero codepoint followed the
            string in the hive or not.
        This all happens because the hive itself contains no information
        about how strings are encoded (see "ENCODING STRINGS" in
        Win::Hivex::Regedit(3)).
        You should only use this option for quick hacking and debugging of
        the hive contents, and never use it if the output is going to be
        passed into another program or stored in another hive.
    --unsafe
        Use heuristics to tolerate certain levels of corruption within
        hives.
        This is unsafe but may allow to export/merge valid keys/values in an
        othewise corrupted hive.
    --max-depth depth
        Limits the recursion depth of the export. For example, an export
        with a max depth of 1 will only include values directly under the
        specified key/prefix. A max depth of 0 will return no values.
        Exports include all child keys by default (fully recursive), which
        may take a while if the registry hive is large / bloated. This
        behavior can also be achieved by providing a negative max depth.
```

## 4. 实践清单

按顺序做完这五步，就能把工具从「装上」推进到「会用」：

- [ ] **1.** **装好并确认版本** —— `sudo apt install libhivex-bin`，再执行 `libhivex-bin --version` 2>/dev/null || `libhivex-bin -V`
- [ ] **2.** **读官方帮助** —— `libhivex-bin -h`，需要细节时 `man libhivex-bin`
- [ ] **3.** **在自有靶场跑最小用例** —— 官方给出的调用形式是：`Usage:`
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/hivex/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/hivex/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/hivex/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
