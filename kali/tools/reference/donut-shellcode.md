# donut-shellcode

> Generates position-independent shellcode from memory and runs them Donut is a position-independent code that enables in-memory execution of VBScript, JScript, EXE, DLL files and dotNET assemblies. A module created by Donut can either be st…

> **功能分类**：通用工具 ｜ **Kali 包**：`donut-shellcode` ｜ **官方文档**：<https://www.kali.org/tools/donut-shellcode/>

## 1. 安装

```bash
sudo apt update
sudo apt install donut
```

| 项目 | 内容 |
|------|------|
| 版本 | 1.1 |
| 架构 | any |
| 可执行命令 | `donut`、`python-donut-doc`、`python3-donut` |
| 依赖 | `libc6`、`donut` |
| 安装体积 | 86 KB |
| 官网 | <https://github.com/TheWover/donut> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/donut-shellcode> |
| 包追踪 | <https://pkg.kali.org/pkg/donut-shellcode> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
donut -h          # 查看用法
man donut         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 3 个可执行命令，下面是官方页面内嵌的帮助原文。

### `donut`

官方给出的调用示例：`donut -h`

```text
root@kali:~# donut -h
  [ Donut shellcode generator v1 (built Feb 12 2026 14:39:18)
  [ Copyright (c) 2019-2021 TheWover, Odzhan
 usage: donut [options] <EXE/DLL/VBS/JS>
       Only the finest artisanal donuts are made of shells.
                   -MODULE OPTIONS-
       -n,--modname: <name>                    Module name for HTTP staging. If entropy is enabled, this is generated randomly.
       -s,--server: <server>                   Server that will host the Donut module. Credentials may be provided in the following format: https://username:
[email protected]
/
       -e,--entropy: <level>                   Entropy. 1=None, 2=Use random names, 3=Random names + symmetric encryption (default)
                   -PIC/SHELLCODE OPTIONS-
       -a,--arch: <arch>,--cpu: <arch>         Target architecture : 1=x86, 2=amd64, 3=x86+amd64(default).
       -o,--output: <path>                     Output file to save loader. Default is "loader.bin"
       -f,--format: <format>                   Output format. 1=Binary (default), 2=Base64, 3=C, 4=Ruby, 5=Python, 6=Powershell, 7=C#, 8=Hex
       -y,--fork: <offset>                     Create a new thread for the loader and continue execution at <offset> relative to the host process's executable.
       -x,--exit: <action>                     Exit behaviour. 1=Exit thread (default), 2=Exit process, 3=Do not exit or cleanup and block indefinitely
                   -FILE OPTIONS-
       -c,--class: <namespace.class>           Optional class name. (required for .NET DLL)
       -d,--domain: <name>                     AppDomain name to create for .NET assembly. If entropy is enabled, this is generated randomly.
       -i,--input: <path>,--file: <path>       Input file to execute in-memory.
       -m,--method: <method>,--function: <api> Optional method or function for DLL. (a method is required for .NET DLL)
       -p,--args: <arguments>                  Optional parameters/command line inside quotations for DLL method/function or EXE.
       -w,--unicode                            Command line is passed to unmanaged DLL function in UNICODE format. (default is ANSI)
       -r,--runtime: <version>                 CLR runtime version. MetaHeader used by default or v4.0.30319 if none available.
       -t,--thread                             Execute the entrypoint of an unmanaged EXE as a thread.
                   -EXTRA-
       -z,--compress: <engine>                 Pack/Compress file. 1=None
       -b,--bypass: <level>                    Bypass AMSI/WLDP/ETW : 1=None, 2=Abort on fail, 3=Continue on fail.(default)
       -k,--headers: <level>                   Preserve PE headers. 1=Overwrite (default), 2=Keep all
       -j,--decoy: <level>                     Optional path of decoy module for Module Overloading.
 examples:
    donut -ic2.dll
    donut --arch:x86 --class:TestClass --method:RunProcess --args:notepad.exe --input:loader.dll
    donut -iloader.dll -c TestClass -m RunProcess -p"calc notepad" -s http://remote_server.com/modules/
```

## 4. 实践清单

按顺序做完这五步，就能把工具从「装上」推进到「会用」：

- [ ] **1.** **装好并确认版本** —— `sudo apt install donut`，再执行 `donut --version` 2>/dev/null || `donut -V`
- [ ] **2.** **读官方帮助** —— `donut -h`，需要细节时 `man donut`
- [ ] **3.** **在自有靶场跑最小用例** —— 用 `donut -h` 里最简单的那个子命令试一次
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/donut-shellcode/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/resource-development.md`](../../tools/by-attack/resource-development.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/donut-shellcode/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/donut-shellcode/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
