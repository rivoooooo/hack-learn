# zsh

> Shell with lots of features Zsh is a UNIX command interpreter (shell) usable as an interactive login shell and as a shell script command processor. Of the standard shells, zsh most closely resembles ksh but includes many enhancements. Zsh …

> **功能分类**：报告与记录 ｜ **Kali 包**：`zsh` ｜ **官方文档**：<https://www.kali.org/tools/zsh/>

## 1. 安装

```bash
sudo apt update
sudo apt install zsh
```

| 项目 | 内容 |
|------|------|
| 版本 | 5.9.2 |
| 架构 | any |
| 可执行命令 | `zsh`、`rzsh`、`zsh-common`、`zsh-dev`、`zsh-doc`、`zsh-static` |
| 依赖 | `debianutils`、`libc6`、`libcap2`、`libtinfo6`、`zsh-common`、`rzsh` |
| 安装体积 | 2.51 MB |
| 官网 | <https://www.zsh.org/> |
| 源码仓库 | <https://salsa.debian.org/debian/zsh> |
| 包追踪 | <https://pkg.kali.org/pkg/zsh> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
zsh -h          # 查看用法
man zsh         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 6 个可执行命令，下面是官方页面内嵌的帮助原文。

### `rzsh`

> 官方示例调用：`rzsh --help`

```text
root@kali:~# rzsh --help
Usage: rzsh [<options>] [<argument> ...]
Special options:
  --help     show this message, then exit
  --version  show zsh version number, then exit
  -b         end option processing, like --
  -c         take first argument as a command to execute
  -o OPTION  set an option by name (see below)
Normal options are named.  An option may be turned on by
`-o OPTION', `--OPTION', `+o no_OPTION' or `+-no-OPTION'.  An
option may be turned off by `-o no_OPTION', `--no-OPTION',
`+o OPTION' or `+-OPTION'.  Options are listed below only in
`--OPTION' or `--no-OPTION' form.
Named options:
  --aliases
  --aliasfuncdef
  --allexport
  --alwayslastprompt
  --alwaystoend
  --appendcreate
  --appendhistory
  --autocd
  --autocontinue
  --autolist
  --automenu
  --autonamedirs
  --autoparamkeys
  --autoparamslash
  --autopushd
  --autoremoveslash
  --autoresume
  --badpattern
  --banghist
  --bareglobqual
  --bashautolist
  --bashrematch
  --beep
  --bgnice
  --braceccl
  --bsdecho
  --caseglob
  --casematch
  --casepaths
  --cbases
  --cdablevars
  --cdsilent
  --chasedots
  --chaselinks
  --checkjobs
  --checkrunningjobs
  --clobber
  --clobberempty
  --combiningchars
  --completealiases
  --completeinword
  --continueonerror
  --correct
  --correctall
  --cprecedences
  --cshjunkiehistory
  --cshjunkieloops
  --cshjunkiequotes
  --cshnullcmd
  --cshnullglob
  --debugbeforecmd
  --dvorak
  --emacs
  --equals
  --errexit
  --errreturn
  --evallineno
  --exec
  --extendedglob
  --extendedhistory
  --flowcontrol
  --forcefloat
  --functionargzero
  --glob
  --globalexport
  --globalrcs
  --globassign
  --globcomplete
  --globdots
  --globstarshort
  --globsubst
  --hashcmds
  --hashdirs
  --hashexecutablesonly
  --hashlistall
  --histallowclobber
  --histbeep
  --histexpiredupsfirst
  --histfcntllock
  --histfindnodups
  --histignorealldups
  --histignoredups
  --histignorespace
  --histlexwords
  --histnofunctions
  --histnostore
  --histreduceblanks
  --histsavebycopy
  --histsavenodups
  --histsubstpattern
  --histverify
  --hup
  --ignorebraces
  --ignoreclosebraces
  --ignoreeof
  --incappendhistory
  --incappendhistorytime
  --interactive
  --interactivecomments
  --ksharrays
  --kshautoload
  --kshglob
  --kshoptionprint
  --kshtypeset
  --kshzerosubscript
  --listambiguous
  --listbeep
  --listpacked
  --listrowsfirst
  --listtypes
  --localloops
  --localoptions
  --localpatterns
  --localtraps
  --login
  --longlistjobs
  --magicequalsubst
  --mailwarning
  --markdirs
  --menucomplete
  --monitor
  --multibyte
  --multifuncdef
  --multios
  --nomatch
  --notify
  --nullglob
  --numericglobsort
  --octalzeroes
  --overstrike
  --pathdirs
  --pathscript
  --pipefail
  --posixaliases
  --posixargzero
  --posixbuiltins
  --posixcd
  --posixidentifiers
  --posixjobs
  --posixstrings
  --posixtraps
  --printeightbit
  --printexitvalue
  --privileged
  --promptbang
  --promptcr
  --promptpercent
  --promptsp
  --promptsubst
  --pushdignoredups
  --pushdminus
  --pushdsilent
  --pushdtohome
  --rcexpandparam
  --rcquotes
  --rcs
  --recexact
  --rematchpcre
  --restricted
  --rmstarsilent
  --rmstarwait
  --sharehistory
  --shfileexpansion
  --shglob
  --shinstdin
  --shnullcmd
  --shoptionletters
  --shortloops
  --shortrepeat
  --shwordsplit
  --singlecommand
  --singlelinezle
  --sourcetrace
  --sunkeyboardhack
  --transientrprompt
  --trapsasync
  --typesetsilent
  --typesettounset
  --unset
  --verbose
  --vi
  --warncreateglobal
  --warnnestedvar
  --xtrace
  --zle
Option aliases:
  --braceexpand            equivalent to --no-ignorebraces
  --dotglob                equivalent to --globdots
  --hashall                equivalent to --hashcmds
  --histappend             equivalent to --appendcreate
  --histexpand             equivalent to --badpattern
  --log                    equivalent to --no-histnofunctions
  --mailwarn               equivalent to --mailwarning
  --onecmd                 equivalent to --singlecommand
  --physical               equivalent to --cdsilent
  --promptvars             equivalent to --promptsubst
  --stdin                  equivalent to --shinstdin
  --trackall               equivalent to --hashcmds
Option letters:
  -0    equivalent to --completeinword
  -1    equivalent to --printexitvalue
  -2    equivalent to --no-autoresume
  -3    equivalent to --no-nomatch
  -4    equivalent to --globdots
  -5    equivalent to --notify
  -6    equivalent to --beep
```

### `zsh`

> 官方示例调用：`zsh --help`

```text
root@kali:~# zsh --help
Usage: zsh [<options>] [<argument> ...]
Special options:
  --help     show this message, then exit
  --version  show zsh version number, then exit
  -b         end option processing, like --
  -c         take first argument as a command to execute
  -o OPTION  set an option by name (see below)
Normal options are named.  An option may be turned on by
`-o OPTION', `--OPTION', `+o no_OPTION' or `+-no-OPTION'.  An
option may be turned off by `-o no_OPTION', `--no-OPTION',
`+o OPTION' or `+-OPTION'.  Options are listed below only in
`--OPTION' or `--no-OPTION' form.
Named options:
  --aliases
  --aliasfuncdef
  --allexport
  --alwayslastprompt
  --alwaystoend
  --appendcreate
  --appendhistory
  --autocd
  --autocontinue
  --autolist
  --automenu
  --autonamedirs
  --autoparamkeys
  --autoparamslash
  --autopushd
  --autoremoveslash
  --autoresume
  --badpattern
  --banghist
  --bareglobqual
  --bashautolist
  --bashrematch
  --beep
  --bgnice
  --braceccl
  --bsdecho
  --caseglob
  --casematch
  --casepaths
  --cbases
  --cdablevars
  --cdsilent
  --chasedots
  --chaselinks
  --checkjobs
  --checkrunningjobs
  --clobber
  --clobberempty
  --combiningchars
  --completealiases
  --completeinword
  --continueonerror
  --correct
  --correctall
  --cprecedences
  --cshjunkiehistory
  --cshjunkieloops
  --cshjunkiequotes
  --cshnullcmd
  --cshnullglob
  --debugbeforecmd
  --dvorak
  --emacs
  --equals
  --errexit
  --errreturn
  --evallineno
  --exec
  --extendedglob
  --extendedhistory
  --flowcontrol
  --forcefloat
  --functionargzero
  --glob
  --globalexport
  --globalrcs
  --globassign
  --globcomplete
  --globdots
  --globstarshort
  --globsubst
  --hashcmds
  --hashdirs
  --hashexecutablesonly
  --hashlistall
  --histallowclobber
  --histbeep
  --histexpiredupsfirst
  --histfcntllock
  --histfindnodups
  --histignorealldups
  --histignoredups
  --histignorespace
  --histlexwords
  --histnofunctions
  --histnostore
  --histreduceblanks
  --histsavebycopy
  --histsavenodups
  --histsubstpattern
  --histverify
  --hup
  --ignorebraces
  --ignoreclosebraces
  --ignoreeof
  --incappendhistory
  --incappendhistorytime
  --interactive
  --interactivecomments
  --ksharrays
  --kshautoload
  --kshglob
  --kshoptionprint
  --kshtypeset
  --kshzerosubscript
  --listambiguous
  --listbeep
  --listpacked
  --listrowsfirst
  --listtypes
  --localloops
  --localoptions
  --localpatterns
  --localtraps
  --login
  --longlistjobs
  --magicequalsubst
  --mailwarning
  --markdirs
  --menucomplete
  --monitor
  --multibyte
  --multifuncdef
  --multios
  --nomatch
  --notify
  --nullglob
  --numericglobsort
  --octalzeroes
  --overstrike
  --pathdirs
  --pathscript
  --pipefail
  --posixaliases
  --posixargzero
  --posixbuiltins
  --posixcd
  --posixidentifiers
  --posixjobs
  --posixstrings
  --posixtraps
  --printeightbit
  --printexitvalue
  --privileged
  --promptbang
  --promptcr
  --promptpercent
  --promptsp
  --promptsubst
  --pushdignoredups
  --pushdminus
  --pushdsilent
  --pushdtohome
  --rcexpandparam
  --rcquotes
  --rcs
  --recexact
  --rematchpcre
  --restricted
  --rmstarsilent
  --rmstarwait
  --sharehistory
  --shfileexpansion
  --shglob
  --shinstdin
  --shnullcmd
  --shoptionletters
  --shortloops
  --shortrepeat
  --shwordsplit
  --singlecommand
  --singlelinezle
  --sourcetrace
  --sunkeyboardhack
  --transientrprompt
  --trapsasync
  --typesetsilent
  --typesettounset
  --unset
  --verbose
  --vi
  --warncreateglobal
  --warnnestedvar
  --xtrace
  --zle
Option aliases:
  --braceexpand            equivalent to --no-ignorebraces
  --dotglob                equivalent to --globdots
  --hashall                equivalent to --hashcmds
  --histappend             equivalent to --appendcreate
  --histexpand             equivalent to --badpattern
  --log                    equivalent to --no-histnofunctions
  --mailwarn               equivalent to --mailwarning
  --onecmd                 equivalent to --singlecommand
  --physical               equivalent to --cdsilent
  --promptvars             equivalent to --promptsubst
  --stdin                  equivalent to --shinstdin
  --trackall               equivalent to --hashcmds
Option letters:
  -0    equivalent to --completeinword
  -1    equivalent to --printexitvalue
  -2    equivalent to --no-autoresume
  -3    equivalent to --no-nomatch
  -4    equivalent to --globdots
  -5    equivalent to --notify
  -6    equivalent to --beep
```

### `zsh-static`

> 官方示例调用：`zsh-static --help`

```text
root@kali:~# zsh-static --help
Usage: zsh-static [<options>] [<argument> ...]
Special options:
  --help     show this message, then exit
  --version  show zsh version number, then exit
  -b         end option processing, like --
  -c         take first argument as a command to execute
  -o OPTION  set an option by name (see below)
Normal options are named.  An option may be turned on by
`-o OPTION', `--OPTION', `+o no_OPTION' or `+-no-OPTION'.  An
option may be turned off by `-o no_OPTION', `--no-OPTION',
`+o OPTION' or `+-OPTION'.  Options are listed below only in
`--OPTION' or `--no-OPTION' form.
Named options:
  --aliases
  --aliasfuncdef
  --allexport
  --alwayslastprompt
  --alwaystoend
  --appendcreate
  --appendhistory
  --autocd
  --autocontinue
  --autolist
  --automenu
  --autonamedirs
  --autoparamkeys
  --autoparamslash
  --autopushd
  --autoremoveslash
  --autoresume
  --badpattern
  --banghist
  --bareglobqual
  --bashautolist
  --bashrematch
  --beep
  --bgnice
  --braceccl
  --bsdecho
  --caseglob
  --casematch
  --casepaths
  --cbases
  --cdablevars
  --cdsilent
  --chasedots
  --chaselinks
  --checkjobs
  --checkrunningjobs
  --clobber
  --clobberempty
  --combiningchars
  --completealiases
  --completeinword
  --continueonerror
  --correct
  --correctall
  --cprecedences
  --cshjunkiehistory
  --cshjunkieloops
  --cshjunkiequotes
  --cshnullcmd
  --cshnullglob
  --debugbeforecmd
  --dvorak
  --emacs
  --equals
  --errexit
  --errreturn
  --evallineno
  --exec
  --extendedglob
  --extendedhistory
  --flowcontrol
  --forcefloat
  --functionargzero
  --glob
  --globalexport
  --globalrcs
  --globassign
  --globcomplete
  --globdots
  --globstarshort
  --globsubst
  --hashcmds
  --hashdirs
  --hashexecutablesonly
  --hashlistall
  --histallowclobber
  --histbeep
  --histexpiredupsfirst
  --histfcntllock
  --histfindnodups
  --histignorealldups
  --histignoredups
  --histignorespace
  --histlexwords
  --histnofunctions
  --histnostore
  --histreduceblanks
  --histsavebycopy
  --histsavenodups
  --histsubstpattern
  --histverify
  --hup
  --ignorebraces
  --ignoreclosebraces
  --ignoreeof
  --incappendhistory
  --incappendhistorytime
  --interactive
  --interactivecomments
  --ksharrays
  --kshautoload
  --kshglob
  --kshoptionprint
  --kshtypeset
  --kshzerosubscript
  --listambiguous
  --listbeep
  --listpacked
  --listrowsfirst
  --listtypes
  --localloops
  --localoptions
  --localpatterns
  --localtraps
  --login
  --longlistjobs
  --magicequalsubst
  --mailwarning
  --markdirs
  --menucomplete
  --monitor
  --multibyte
  --multifuncdef
  --multios
  --nomatch
  --notify
  --nullglob
  --numericglobsort
  --octalzeroes
  --overstrike
  --pathdirs
  --pathscript
  --pipefail
  --posixaliases
  --posixargzero
  --posixbuiltins
  --posixcd
  --posixidentifiers
  --posixjobs
  --posixstrings
  --posixtraps
  --printeightbit
  --printexitvalue
  --privileged
  --promptbang
  --promptcr
  --promptpercent
  --promptsp
  --promptsubst
  --pushdignoredups
  --pushdminus
  --pushdsilent
  --pushdtohome
  --rcexpandparam
  --rcquotes
  --rcs
  --recexact
  --rematchpcre
  --restricted
  --rmstarsilent
  --rmstarwait
  --sharehistory
  --shfileexpansion
  --shglob
  --shinstdin
  --shnullcmd
  --shoptionletters
  --shortloops
  --shortrepeat
  --shwordsplit
  --singlecommand
  --singlelinezle
  --sourcetrace
  --sunkeyboardhack
  --transientrprompt
  --trapsasync
  --typesetsilent
  --typesettounset
  --unset
  --verbose
  --vi
  --warncreateglobal
  --warnnestedvar
  --xtrace
  --zle
Option aliases:
  --braceexpand            equivalent to --no-ignorebraces
  --dotglob                equivalent to --globdots
  --hashall                equivalent to --hashcmds
  --histappend             equivalent to --appendcreate
  --histexpand             equivalent to --badpattern
  --log                    equivalent to --no-histnofunctions
  --mailwarn               equivalent to --mailwarning
  --onecmd                 equivalent to --singlecommand
  --physical               equivalent to --cdsilent
  --promptvars             equivalent to --promptsubst
  --stdin                  equivalent to --shinstdin
  --trackall               equivalent to --hashcmds
Option letters:
  -0    equivalent to --completeinword
  -1    equivalent to --printexitvalue
  -2    equivalent to --no-autoresume
  -3    equivalent to --no-nomatch
  -4    equivalent to --globdots
  -5    equivalent to --notify
  -6    equivalent to --beep
```

## 4. 实践清单

按顺序做完这五步，就能把工具从「装上」推进到「会用」：

- [ ] **1.** **装好并确认版本** —— `sudo apt install zsh`，再执行 `zsh --version` 2>/dev/null || `zsh -V`
- [ ] **2.** **读官方帮助** —— `zsh -h`，需要细节时 `man zsh`
- [ ] **3.** **在自有靶场跑最小用例** —— 官方给出的调用形式是：`Usage: rzsh [<options>] [<argument> ...]`
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/zsh/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/zsh/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/zsh/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
