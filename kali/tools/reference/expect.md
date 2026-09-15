# expect

> Automates interactive applications Expect is a tool for automating interactive applications according to a script. Following the script, Expect knows what can be expected from a program and what the correct response should be. Expect is al…

> **功能分类**：通用工具 ｜ **Kali 包**：`expect` ｜ **官方文档**：<https://www.kali.org/tools/expect/>

## 1. 安装

```bash
sudo apt update
sudo apt install expect
```

| 项目 | 内容 |
|------|------|
| 版本 | 5.45.4 |
| 架构 | any |
| 可执行命令 | `expect`、`autoexpect`、`autopasswd`、`cryptdir`、`decryptdir`、`dislocate`、`expect8.6`、`expect9.0`、`expect_autoexpect`、`expect_autopasswd`、`expect_cryptdir`、`expect_decryptdir`、`expect_dislocate`、`expect_kibitz`、`expect_lpunlock`、`expect_mkpasswd`、`expect_multixterm`、`expect_passmass`、`expect_rftp`、`expect_rlogin-cwd`、`expect_timed-read`、`expect_timed-run`、`expect_tknewsbiff`、`expect_tkpasswd`、`expect_unbuffer`、`expect_weather`、`expect_xkibitz`、`expect_xpstat`、`kibitz`、`lpunlock`、`multixterm`、`passmass`、`rlogin-cwd`、`timed-read`、`timed-run`、`tknewsbiff`、`tkpasswd`、`unbuffer`、`xkibitz`、`xpstat`、`tcl-expect`、`tcl-expect-dev` |
| 依赖 | `libc6`、`libtcl8.6`、`libtcl9.0`、`tcl-expect`、`tcl8.6`、`tcl9.0`、`autoexpect` |
| 安装体积 | 324 KB |
| 官网 | <https://core.tcl.tk/expect/> |
| 源码仓库 | <https://salsa.debian.org/tcltk-team/expect> |
| 包追踪 | <https://pkg.kali.org/pkg/expect> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
expect -h          # 查看用法
man expect         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 42 个可执行命令，下面是官方页面内嵌的帮助原文。

### `autoexpect`

官方给出的调用示例：`autoexpect -h`

```text
root@kali:~# autoexpect -h
autoexpect started, file is script.exp
autoexpect done, file is script.exp
```

### `autopasswd`

官方给出的调用示例：`autopasswd -h`

```text
root@kali:~# autopasswd -h
spawn passwd -h
Usage: passwd [options] [LOGIN]
Options:
  -a, --all                     report password status on all accounts
  -d, --delete                  delete the password for the named account
  -e, --expire                  force expire the password for the named account
  -h, --help                    display this help message and exit
  -k, --keep-tokens             change password only if expired
  -i, --inactive INACTIVE       set password inactive after expiration
                                to INACTIVE
  -l, --lock                    lock the password of the named account
  -n, --mindays MIN_DAYS        set minimum number of days before password
                                change to MIN_DAYS
  -q, --quiet                   quiet mode
  -r, --repository REPOSITORY   change password in REPOSITORY repository
  -R, --root CHROOT_DIR         directory to chroot into
  -P, --prefix PREFIX_DIR       directory prefix
  -S, --status                  report password status on the named account
  -u, --unlock                  unlock the password of the named account
  -w, --warndays WARN_DAYS      set expiration warning days to WARN_DAYS
  -x, --maxdays MAX_DAYS        set maximum number of days before password
                                change to MAX_DAYS
  -s, --stdin                   read new token from stdin
```

### `cryptdir`

官方给出的调用示例：`cryptdir -h`

```text
root@kali:~# cryptdir -h
This example requires the mcrypt package.
```

### `decryptdir`

官方给出的调用示例：`decryptdir -h`

```text
root@kali:~# decryptdir -h
This example requires the mcrypt package.
```

### `dislocate`

官方给出的调用示例：`dislocate -h`

```text
root@kali:~# dislocate -h
bad flag "-h": must be -console, -ignore, -leaveopen, -noecho, -nottycopy, -nottyinit, -open, or -pty
    while executing
"spawn -h"
    ("eval" body line 1)
    invoked from within
"eval spawn $argv"
    (procedure "child" line 11)
    invoked from within
"child $datearg $argv"
    invoked from within
"if {$argc} {
    # initial creation occurs before fork because if we do it after
    # then either the child or the parent may have to spin retrying
 ..."
    (file "/usr/bin/dislocate" line 264)
```

### `expect`

官方给出的调用示例：`expect -h`

```text
root@kali:~# expect -h
expect: invalid option -- 'h'
usage: expect [-div] [-c cmds] [[-f] cmdfile] [args]
```

### `expect8.6`

官方给出的调用示例：`expect8.6 -h`

```text
root@kali:~# expect8.6 -h
expect8.6: invalid option -- 'h'
usage: expect [-div] [-c cmds] [[-f] cmdfile] [args]
```

### `expect9.0`

官方给出的调用示例：`expect9.0 -h`

```text
root@kali:~# expect9.0 -h
expect9.0: invalid option -- 'h'
usage: expect [-div] [-c cmds] [[-f] cmdfile] [args]
```

### `expect_autoexpect`

官方给出的调用示例：`expect_autoexpect -h`

```text
root@kali:~# expect_autoexpect -h
autoexpect started, file is script.exp
autoexpect done, file is script.exp
```

### `expect_autopasswd`

官方给出的调用示例：`expect_autopasswd -h`

```text
root@kali:~# expect_autopasswd -h
spawn passwd -h
Usage: passwd [options] [LOGIN]
Options:
  -a, --all                     report password status on all accounts
  -d, --delete                  delete the password for the named account
  -e, --expire                  force expire the password for the named account
  -h, --help                    display this help message and exit
  -k, --keep-tokens             change password only if expired
  -i, --inactive INACTIVE       set password inactive after expiration
                                to INACTIVE
  -l, --lock                    lock the password of the named account
  -n, --mindays MIN_DAYS        set minimum number of days before password
                                change to MIN_DAYS
  -q, --quiet                   quiet mode
  -r, --repository REPOSITORY   change password in REPOSITORY repository
  -R, --root CHROOT_DIR         directory to chroot into
  -P, --prefix PREFIX_DIR       directory prefix
  -S, --status                  report password status on the named account
  -u, --unlock                  unlock the password of the named account
  -w, --warndays WARN_DAYS      set expiration warning days to WARN_DAYS
  -x, --maxdays MAX_DAYS        set maximum number of days before password
                                change to MAX_DAYS
  -s, --stdin                   read new token from stdin
```

## 4. 实践清单

按顺序做完这五步，就能把工具从「装上」推进到「会用」：

- [ ] **1.** **装好并确认版本** —— `sudo apt install expect`，再执行 `expect --version` 2>/dev/null || `expect -V`
- [ ] **2.** **读官方帮助** —— `expect -h`，需要细节时 `man expect`
- [ ] **3.** **在自有靶场跑最小用例** —— 官方给出的调用形式是：`Usage: passwd [options] [LOGIN]`
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/expect/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/expect/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/expect/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
