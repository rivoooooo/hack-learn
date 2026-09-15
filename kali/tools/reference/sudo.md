# sudo

> Provide limited super user privileges to specific users Sudo is a program designed to allow a sysadmin to give limited root privileges to users and log root activity. The basic philosophy is to give as few privileges as possible but still …

> **功能分类**：信息搜集 ｜ **Kali 包**：`sudo` ｜ **官方文档**：<https://www.kali.org/tools/sudo/>

## 1. 安装

```bash
sudo apt update
sudo apt install sudo
```

| 项目 | 内容 |
|------|------|
| 版本 | 1.9.17p2 |
| 架构 | any |
| 可执行命令 | `libnss-sudo`、`sudo`、`cvtsudoers`、`sudo_logsrvd`、`sudo_sendlog`、`sudoedit`、`sudoreplay`、`visudo`、`sudo-ldap` |
| 依赖 | `libapparmor1`、`libaudit1`、`libc6`、`libpam-modules`、`libpam0g`、`libselinux1`、`libssl3t64` |
| 安装体积 | 6.61 MB |
| 官网 | <https://www.sudo.ws/> |
| 源码仓库 | <https://salsa.debian.org/sudo-team/sudo> |
| 包追踪 | <https://pkg.kali.org/pkg/sudo> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
libnss-sudo -h          # 查看用法
man libnss-sudo         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 9 个可执行命令，下面是官方页面内嵌的帮助原文。

### `cvtsudoers`

官方给出的调用示例：`cvtsudoers -h`

```text
root@kali:~# cvtsudoers -h
cvtsudoers - convert between sudoers file formats
usage: cvtsudoers [-ehMpV] [-b dn] [-c conf_file ] [-d deftypes] [-f output_format] [-i input_format] [-I increment] [-m filter] [-o output_file] [-O start_point] [-P padding] [-s sections] [input_file]
Options:
  -b, --base=dn              the base DN for sudo LDAP queries
  -c, --config=conf_file     the path to the configuration file
  -d, --defaults=deftypes    only convert Defaults of the specified types
  -e, --expand-aliases       expand aliases when converting
  -f, --output-format=format set output format: JSON, LDIF or sudoers
  -i, --input-format=format  set input format: LDIF or sudoers
  -I, --increment=num        amount to increase each sudoOrder by
  -h, --help                 display help message and exit
  -m, --match=filter         only convert entries that match the filter
  -M, --match-local          match filter uses passwd and group databases
  -o, --output=output_file   write converted sudoers to output_file
  -O, --order-start=num      starting point for first sudoOrder
  -p, --prune-matches        prune non-matching users, groups and hosts
  -P, --padding=num          base padding for sudoOrder increment
  -s, --suppress=sections    suppress output of certain sections
  -V, --version              display version information and exit
```

### `sudo`

官方给出的调用示例：`sudo -h`

```text
root@kali:~# sudo -h
sudo - execute a command as another user
usage: sudo -h | -K | -k | -V
usage: sudo -v [-ABkNnS] [-g group] [-h host] [-p prompt] [-u user]
usage: sudo -l [-ABkNnS] [-g group] [-h host] [-p prompt] [-U user]
            [-u user] [command [arg ...]]
usage: sudo [-ABbEHkNnPS] [-r role] [-t type] [-C num] [-D directory]
            [-g group] [-h host] [-p prompt] [-R directory] [-T timeout]
            [-u user] [VAR=value] [-i | -s] [command [arg ...]]
usage: sudo -e [-ABkNnS] [-r role] [-t type] [-C num] [-D directory]
            [-g group] [-h host] [-p prompt] [-R directory] [-T timeout]
            [-u user] file ...
Options:
  -A, --askpass                 use a helper program for password prompting
  -b, --background              run command in the background
  -B, --bell                    ring bell when prompting
  -C, --close-from=num          close all file descriptors >= num
  -D, --chdir=directory         change the working directory before running
                                command
  -E, --preserve-env            preserve user environment when running command
      --preserve-env=list       preserve specific environment variables
  -e, --edit                    edit files instead of running a command
  -g, --group=group             run command as the specified group name or ID
  -H, --set-home                set HOME variable to target user's home dir
  -h, --help                    display help message and exit
  -h, --host=host               run command on host (if supported by plugin)
  -i, --login                   run login shell as the target user; a command
                                may also be specified
  -K, --remove-timestamp        remove timestamp file completely
  -k, --reset-timestamp         invalidate timestamp file
  -l, --list                    list user's privileges or check a specific
                                command; use twice for longer format
  -n, --non-interactive         non-interactive mode, no prompts are used
  -P, --preserve-groups         preserve group vector instead of setting to
                                target's
  -p, --prompt=prompt           use the specified password prompt
  -R, --chroot=directory        change the root directory before running command
  -r, --role=role               create SELinux security context with specified
                                role
  -S, --stdin                   read password from standard input
  -s, --shell                   run shell as the target user; a command may
                                also be specified
  -t, --type=type               create SELinux security context with specified
                                type
  -T, --command-timeout=timeout terminate command after the specified time limit
  -U, --other-user=user         in list mode, display privileges for user
  -u, --user=user               run command (or edit file) as specified user
                                name or ID
  -V, --version                 display version information and exit
  -v, --validate                update user's timestamp without running a
                                command
  --                            stop processing command line arguments
```

### `sudo_logsrvd`

官方给出的调用示例：`sudo_logsrvd -h`

```text
root@kali:~# sudo_logsrvd -h
sudo_logsrvd - sudo log server
usage: sudo_logsrvd [-n] [-f conf_file] [-R percentage]
Options:
  -f, --file            path to configuration file
  -h, --help            display help message and exit
  -n, --no-fork         do not fork, run in the foreground
  -R, --random-drop     percent chance connections will drop
  -V, --version         display version information and exit
```

### `sudo_sendlog`

官方给出的调用示例：`sudo_sendlog --help`

```text
root@kali:~# sudo_sendlog --help
sudo_sendlog - send sudo I/O log to remote server
usage: sudo_sendlog [-AnV] [-b ca_bundle] [-c cert_file] [-h host] [-i iolog-id] [-k key_file] [-p port] [-r restart-point] [-R reject-reason] [-s stop-point] [-t number] /path/to/iolog
Options:
      --help            display help message and exit
  -A, --accept          only send an accept event (no I/O)
  -b, --ca-bundle       certificate bundle file to verify server's cert against
  -c, --cert            certificate file for TLS handshake
  -h, --host            host to send logs to
  -i, --iolog_id        remote ID of I/O log to be resumed
  -k, --key             private key file
  -n, --no-verify       do not verify server certificate
  -p, --port            port to use when connecting to host
  -r, --restart         restart previous I/O log transfer
  -R, --reject          reject the command with the given reason
  -s, --stop-after        stop transfer after reaching this time
  -t, --test            test audit server by sending selected I/O log n times in parallel
  -V, --version         display version information and exit
```

### `sudoedit`

官方给出的调用示例：`sudoedit -h`

```text
root@kali:~# sudoedit -h
sudoedit - edit files as another user
usage: sudoedit -h | -V
usage: sudoedit [-ABkNnS] [-r role] [-t type] [-C num] [-D directory]
                [-g group] [-h host] [-p prompt] [-R directory] [-T timeout]
                [-u user] file ...
Options:
  -A, --askpass                 use a helper program for password prompting
  -B, --bell                    ring bell when prompting
  -C, --close-from=num          close all file descriptors >= num
  -D, --chdir=directory         change the working directory before running
                                command
  -g, --group=group             run command as the specified group name or ID
  -h, --help                    display help message and exit
  -h, --host=host               run command on host (if supported by plugin)
  -k, --reset-timestamp         invalidate timestamp file
  -n, --non-interactive         non-interactive mode, no prompts are used
  -p, --prompt=prompt           use the specified password prompt
  -R, --chroot=directory        change the root directory before running command
  -r, --role=role               create SELinux security context with specified
                                role
  -S, --stdin                   read password from standard input
  -t, --type=type               create SELinux security context with specified
                                type
  -T, --command-timeout=timeout terminate command after the specified time limit
  -u, --user=user               run command (or edit file) as specified user
                                name or ID
  -V, --version                 display version information and exit
  --                            stop processing command line arguments
```

### `sudoreplay`

官方给出的调用示例：`sudoreplay -h`

```text
root@kali:~# sudoreplay -h
sudoreplay - replay sudo session logs
usage: sudoreplay [-hnRS] [-d dir] [-m num] [-s num] ID
usage: sudoreplay [-h] [-d dir] -l [search expression]
Options:
  -d, --directory=dir    specify directory for session logs
  -f, --filter=filter    specify which I/O type(s) to display
  -h, --help             display help message and exit
  -l, --list             list available session IDs, with optional expression
  -m, --max-wait=num     max number of seconds to wait between events
  -n, --non-interactive  no prompts, session is sent to the standard output
  -R, --no-resize        do not attempt to re-size the terminal
  -S, --suspend-wait     wait while the command was suspended
  -s, --speed=num        speed up or slow down output
  -V, --version          display version information and exit
```

### `visudo`

官方给出的调用示例：`visudo -h`

```text
root@kali:~# visudo -h
visudo - safely edit the sudoers file
usage: visudo [-chqsV] [[-f] sudoers ]
Options:
  -c, --check              check-only mode
  -f, --file=sudoers       specify sudoers file location
  -h, --help               display help message and exit
  -I, --no-includes        do not edit include files
  -q, --quiet              less verbose (quiet) syntax error messages
  -s, --strict             strict syntax checking
  -V, --version            display version information and exit
```

## 4. 实践清单

按顺序做完这五步，就能把工具从「装上」推进到「会用」：

- [ ] **1.** **装好并确认版本** —— `sudo apt install sudo`，再执行 `libnss-sudo --version` 2>/dev/null || `libnss-sudo -V`
- [ ] **2.** **读官方帮助** —— `libnss-sudo -h`，需要细节时 `man libnss-sudo`
- [ ] **3.** **在自有靶场跑最小用例** —— 用 `libnss-sudo -h` 里最简单的那个子命令试一次
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/sudo/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/sudo/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/sudo/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
