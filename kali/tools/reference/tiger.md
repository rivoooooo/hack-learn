# tiger

> Security auditing and intrusion detection tools for Linux TIGER, or the ’tiger’ scripts, is a set of tools (Bourne shell scripts and C programs) which are used to perform a security audit of different operating systems components. The tool…

> **功能分类**：识别与指纹 ｜ **Kali 包**：`tiger` ｜ **官方文档**：<https://www.kali.org/tools/tiger/>

## 1. 安装

```bash
sudo apt update
sudo apt install tiger
```

| 项目 | 内容 |
|------|------|
| 版本 | 3.2.4~rc1 |
| 架构 | any |
| 可执行命令 | `tiger`、`tigercron`、`tigexp`、`tiger-otheros` |
| 依赖 | `binutils`、`bsdutils` |
| 安装体积 | 7.61 MB |
| 官网 | <http://savannah.nongnu.org/projects/tiger/> |
| 源码仓库 | <https://git.savannah.nongnu.org/cgit/tiger.git> |
| 包追踪 | <https://pkg.kali.org/pkg/tiger> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
tiger -h          # 查看用法
man tiger         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 4 个可执行命令，下面是官方页面内嵌的帮助原文。

### `tiger`

官方给出的调用示例：`tiger -h`

```text
root@kali:~# tiger -h
Tiger UN*X security checking system
   Developed by Texas A&M University, 1994
   Updated by the Advanced Research Corporation, 1999-2002
   Further updated by Javier Fernandez-Sanguino, 2001-2018
   Contributions by Francisco Manuel Garcia Claramonte, 2009-2010
   Covered by the GNU General Public License (GPL)
Tiger, version
Usage: ./tiger [-vthqGSH]  [-B dir] [-l dir|@host] [-w dir] [-b dir] [-e|-E] [-c config] [-A arch] [-O os] [-R release]
       -v     Show the Tiger version.
       -t     Run in test mode.
       -h     Show usage (this help).
       -q     Supress messages to be as quiet as possible, only
              security messages will be shown.
       -B name
              Specify  the directory where tiger is installed.  If
              not specified, '/usr/lib/tiger' is used.
       -l name
              Specify the name of the directory where Tiger  will
              write  the  security  report.  This defaults to
              '/var/log/tiger'. The filename  of  the report will be of
              the form 'security.report.host-name.date.time.'
              If the directory  begins  with a @, the name will
              be interpreted as a tiger logging server.
       -w name
              Specify a directory to  use  for  creating  scratch
              files.  This defaults to '/var/lib/tiger/work'.
       -b name
              Specify  the directory which contains (or will con-
              tain) the binaries generated from  the  C  modules.
              If  the  systems  directories contain all the bina-
              ries, they will be used directly  from  there.   If
              not,  then  if  the  bindir  contains the binaries,
              these will be used.  If none are  found  in  either
              place,  then an attempt will be made to compile the
              C code and install the executables into the bindir.
       -c name
              Specify  an  alternate  name for the tigerrc control
              file.  The default is '/etc/tiger/tigerrc'.
       -e     This option will cause explanations to be  inserted
              into  the  security  report following each message.
              This can greatly increase the size of  the  report,
              as explanations may appear repeatedly.
       -E     This  option  indicates that a separate explanation
              report should be  created,  with  explanations  for
              each  type  of  message  only  appearing once.  The
              filename of the explanation report will be  of  the
              form 'explain.report.hostname.date.time.'
       -G     Generate the signatures (MD5 hashes and file permissions)
              for system binary files.
       -H     This option will format the report into HTML creat-
              ing local links to the problem descriptions.
       -S     This option indicates that a surface level check of
              the  configuration  files  of  any diskless clients
              served by this machine should  be  checked  at  the
              same  time.   The checks will not be as in depth as
              they would be if run on the client itself.
Overrides for values detected  by the configuration system:
       -A arch
              Specify  an  alternate  architecture for tiger
       -O os
              Specify  an  alternate  operating system for tiger
       -R release
              Specify  an  alternate  operating system release
              for tiger
Report bugs at http://savannah.nongnu.org/projects/tiger
```

### `tigercron`

官方给出的调用示例：`tigercron -h`

```text
root@kali:~# tigercron -h
Tiger, version
Usage: ./tiger [-vthqGSH]  [-B dir] [-l dir|@host] [-w dir] [-b dir] [-e|-E] [-c config] [-A arch] [-O os] [-R release]
       -v     Show the Tiger version.
       -t     Run in test mode.
       -h     Show usage (this help).
       -q     Supress messages to be as quiet as possible, only
              security messages will be shown.
       -B name
              Specify  the directory where tiger is installed.  If
              not specified, '/usr/lib/tiger' is used.
       -l name
              Specify the name of the directory where Tiger  will
              write  the  security  report.  This defaults to
              '/var/log/tiger'. The filename  of  the report will be of
              the form 'security.report.host-name.date.time.'
              If the directory  begins  with a @, the name will
              be interpreted as a tiger logging server.
       -w name
              Specify a directory to  use  for  creating  scratch
              files.  This defaults to '/var/lib/tiger/work'.
       -b name
              Specify  the directory which contains (or will con-
              tain) the binaries generated from  the  C  modules.
              If  the  systems  directories contain all the bina-
              ries, they will be used directly  from  there.   If
              not,  then  if  the  bindir  contains the binaries,
              these will be used.  If none are  found  in  either
              place,  then an attempt will be made to compile the
              C code and install the executables into the bindir.
       -c name
              Specify  an  alternate  name for the tigerrc control
              file.  The default is '/etc/tiger/tigerrc'.
       -e     This option will cause explanations to be  inserted
              into  the  security  report following each message.
              This can greatly increase the size of  the  report,
              as explanations may appear repeatedly.
       -E     This  option  indicates that a separate explanation
              report should be  created,  with  explanations  for
              each  type  of  message  only  appearing once.  The
              filename of the explanation report will be  of  the
              form 'explain.report.hostname.date.time.'
       -G     Generate the signatures (MD5 hashes and file permissions)
              for system binary files.
       -H     This option will format the report into HTML creat-
              ing local links to the problem descriptions.
       -S     This option indicates that a surface level check of
              the  configuration  files  of  any diskless clients
              served by this machine should  be  checked  at  the
              same  time.   The checks will not be as in depth as
              they would be if run on the client itself.
Overrides for values detected  by the configuration system:
       -A arch
              Specify  an  alternate  architecture for tiger
       -O os
              Specify  an  alternate  operating system for tiger
       -R release
              Specify  an  alternate  operating system release
              for tiger
Report bugs at http://savannah.nongnu.org/projects/tiger
```

### `tigexp`

官方给出的调用示例：`tigexp --help`

```text
root@kali:~# tigexp --help
```

## 4. 实践清单

按顺序做完这五步，就能把工具从「装上」推进到「会用」：

- [ ] **1.** **装好并确认版本** —— `sudo apt install tiger`，再执行 `tiger --version` 2>/dev/null || `tiger -V`
- [ ] **2.** **读官方帮助** —— `tiger -h`，需要细节时 `man tiger`
- [ ] **3.** **在自有靶场跑最小用例** —— 官方给出的调用形式是：`Usage: ./tiger [-vthqGSH]  [-B dir] [-l dir|@host] [-w dir] [-b dir] [-e|-E] [-c config] [-A arch] [-O os] [-R release]`
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/tiger/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- **精讲教程**（含原理、参数详解、靶场实操与输出解读）：[tiger](../../tools/tutorials/02-漏洞分析/tiger.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/tiger/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/tiger/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
