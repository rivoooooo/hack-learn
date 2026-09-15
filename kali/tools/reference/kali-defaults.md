# kali-defaults

> Kali default settings This package implements various default settings within Kali. The size of this package (including its dependencies) should be rather limited because it is included in all Kali images, even minimalistic ones such as co…

> **功能分类**：信息搜集 ｜ **Kali 包**：`kali-defaults` ｜ **官方文档**：<https://www.kali.org/tools/kali-defaults/>

## 1. 安装

```bash
sudo apt update
sudo apt install kali-defaults
```

| 项目 | 内容 |
|------|------|
| 版本 | 2026.3.2 |
| 架构 | all |
| 可执行命令 | `kali-defaults`、`kali-check-apt-sources`、`kali-deprecated`、`kali-motd`、`kali-service-start`、`kali-service-stop`、`kali-setup`、`kali-treecd`、`kali-winexec`、`kali-defaults-desktop` |
| 安装体积 | 375 KB |
| 官网 | <https://www.kali.org> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/kali-defaults> |
| 包追踪 | <https://pkg.kali.org/pkg/kali-defaults> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
kali-defaults -h          # 查看用法
man kali-defaults         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 10 个可执行命令，下面是官方页面内嵌的帮助原文。

### `kali-deprecated`

官方给出的调用示例：`kali-deprecated -h`

```text
root@kali:~# kali-deprecated -h
[-] ERROR: Missing commands. /usr/bin/kali-deprecated <old-command> <new-command> [<url>]
```

### `kali-service-start`

官方给出的调用示例：`kali-service-start -h`

```text
root@kali:~# kali-service-start -h
┏━(Message from Kali developers)
┃
5:245m> systemctl [OPTIONS…] COMMAND …
Query or send control commands to the system manager.
Unit Commands:
  [list-units                  List units currently in memory
    [PATTERN…]]
  list-automounts              List automount units currently in memory, ordered
    [PATTERN…]                 by path
  list-paths [PATTERN…]        List path units currently in memory, ordered by
                               path
  list-sockets                 List socket units currently in memory, ordered by
    [PATTERN…]                 address
  list-timers                  List timer units currently in memory, ordered by
    [PATTERN…]                 next elapse
  is-active PATTERN…           Check whether units are active
  is-failed [PATTERN…]         Check whether units are failed or system is in
                               degraded state
  status                       Show runtime status of one or more units
    [PATTERN…|PID…]
  show                         Show properties of one or more units/jobs or the
    [PATTERN…|JOB…]            manager
  cat PATTERN…                 Show files and drop-ins of specified units
  help PATTERN…|PID…           Show manual for one or more units
  list-dependencies            Recursively show units which are required or
    [UNIT…]                    wanted by the units or by which those units are
                               required or wanted
  start UNIT…                  Start (activate) one or more units
  stop UNIT…                   Stop (deactivate) one or more units
  reload UNIT…                 Reload one or more units
  restart UNIT…                Start or restart one or more units
  try-restart UNIT…            Restart one or more units if active
  enqueue-marked               Enqueue jobs for all marked units
  reload-or-restart            Reload one or more units if possible, otherwise
    UNIT…                      start or restart
  try-reload-or-restart        If active, reload one or more units, if
    UNIT…                      supported, otherwise restart
  isolate UNIT                 Start one unit and stop all others
  kill UNIT…                   Send signal to processes of a unit
  clean UNIT…                  Clean runtime, cache, state, logs or
                               configuration of unit
  freeze PATTERN…              Freeze execution of unit processes
  thaw PATTERN…                Resume execution of a frozen unit
  set-property UNIT            Sets one or more properties of a unit
    PROPERTY=VALUE…
  bind UNIT PATH [PATH]        Bind-mount a path from the host into a unit's
                               namespace
  mount-image UNIT PATH [PATH  Mount an image from the host into a unit's
    [OPTS]]                    namespace
  service-log-level SERVICE    Get/set logging threshold for service
    [LEVEL]
  service-log-target SERVICE   Get/set logging target for service
    [TARGET]
  reset-failed                 Reset failed state for all, one, or more units
    [PATTERN…]
  whoami [PID…]                Return unit caller or specified PIDs are part of
Unit File Commands:
  list-unit-files              List installed unit files
    [PATTERN…]
  enable                       Enable one or more unit files
    [UNIT…|PATH…]
  disable UNIT…                Disable one or more unit files
  reenable UNIT…               Reenable one or more unit files
  preset UNIT…                 Enable/disable one or more unit files based on
                               preset configuration
  preset-all                   Enable/disable all unit files based on preset
                               configuration
  is-enabled UNIT…             Check whether unit files are enabled
  mask UNIT…                   Mask one or more units
  unmask UNIT…                 Unmask one or more units
  link PATH…                   Link one or more units files into the search path
  revert UNIT…                 Revert one or more unit files to vendor version
  add-wants TARGET             Add 'Wants' dependency for the target on
    UNIT…                      specified one or more units
  add-requires TARGET          Add 'Requires' dependency for the target on
    UNIT…                      specified one or more units
  edit UNIT…                   Edit one or more unit files
  get-default                  Get the name of the default target
  set-default TARGET           Set the default target
Machine Commands:
  list-machines                List local containers and host
    [PATTERN…]
Job Commands:
  list-jobs [PATTERN…]         List jobs
  cancel [JOB…]                Cancel all, one, or more jobs
Environment Commands:
  show-environment             Dump environment
  set-environment              Set one or more environment variables
    VARIABLE=VALUE…
  unset-environment            Unset one or more environment variables
    VARIABLE…
  import-environment           Import all or some environment variables
    VARIABLE…
Manager State Commands:
  daemon-reload                Reload systemd manager configuration
  daemon-reexec                Reexecute systemd manager
  log-level [LEVEL]            Get/set logging threshold for manager
  log-target [TARGET]          Get/set logging target for manager
  service-watchdogs            Get/set service watchdog state
    [BOOL]
System Commands:
  is-system-running            Check whether system is fully running
  default                      Enter system default mode
  rescue                       Enter system rescue mode
  emergency                    Enter system emergency mode
  halt                         Shut down and halt the system
  poweroff                     Shut down and power-off the system
  reboot                       Shut down and reboot the system
  kexec                        Shut down and reboot the system with kexec
  soft-reboot                  Shut down and reboot userspace
  exit [EXIT_CODE]             Request user instance or container exit
  switch-root [ROOT            Change to a different root file system
    [INIT]]
  sleep                        Put the system to sleep (through one of the
                               operations below)
  suspend                      Suspend the system
  hibernate                    Hibernate the system
  hybrid-sleep                 Hibernate and suspend the system
  suspend-then-hibernate       Suspend the system, wake after a period of time,
                               and hibernate
Options:
  -h --help                    Show this help
     --version                 Show package version
     --system                  Connect to the system service manager
     --user                    Connect to the user service manager
  -C --capsule=NAME            Connect to service manager of specified capsule
  -H --host=[USER@]HOST        Operate on remote host
  -M --machine=CONTAINER       Operate on local container
  -t --type=TYPE               List units of a particular type
     --state=STATE             List units with particular LOAD or SUB or ACTIVE
                               state
     --failed                  Shortcut for --state=failed
  -p --property=NAME           Show only properties by this name
  -P NAME                      Equivalent to --value --property=NAME
  -a --all                     Show all properties/all units currently in
                               memory, including dead/empty ones. To list all
                               units installed on the system, use
                               'list-unit-files' instead
  -l --full                    Don't ellipsize unit names on output
  -r --recursive               Show unit list of host and local containers
     --reverse                 Show reverse dependencies with
                               'list-dependencies'
     --before                  Show units ordered before with
                               'list-dependencies'
     --after                   Show units ordered after with 'list-dependencies'
     --with-dependencies       Show unit dependencies with 'status', 'cat',
                               'list-units', and 'list-unit-files'
     --job-mode=MODE           Specify how to deal with already queued jobs,
                               when queueing a new job
  -T --show-transaction        When enqueuing a unit job, show full transaction
     --show-types              When showing sockets, explicitly show their type
     --value                   When showing properties, only print the value
     --check-inhibitors=MODE   Whether to check inhibitors before shutting down,
                               sleeping, or hibernating
  -i                           Shortcut for --check-inhibitors=no
  -s --signal=SIGNAL           Which signal to send
     --kill-whom=WHOM          Whom to send signal to
     --kill-value=INT          Signal value to enqueue
     --kill-subgroup=PATH      Send signal to sub-control group only
     --what=RESOURCES          Which types of resources to remove
     --now                     Start or stop unit after enabling or disabling it
     --dry-run                 Only print what would be done. Currently
                               supported by verbs: halt, poweroff, reboot,
                               kexec, soft-reboot, suspend, hibernate,
                               suspend-then-hibernate, hybrid-sleep, default,
                               rescue, emergency, and exit.
  -q --quiet                   Suppress output
  -v --verbose                 Show unit logs while executing operation
     --no-warn                 Suppress several warnings shown by default
     --wait                    For (re)start, wait until service stopped again.
                               For is-system-running, wait until startup is
                               completed. For kill, wait until service stopped.
     --no-block                Do not wait until operation finished
     --no-wall                 Don't send wall message before
                               halt/power-off/reboot
     --message=MESSAGE         Specify human-readable reason for system shutdown
     --no-reload               Don't reload daemon after en-/dis-abling unit
                               files
     --legend=BOOL             Enable/disable the legend (column headers and
                               hints)
     --no-pager                Do not start a pager
     --no-ask-password         Do not prompt for password
     --global                  Edit/enable/disable/mask default user unit files
                               globally
     --runtime                 Edit/enable/disable/mask unit files temporarily
                               until next reboot
  -f --force                   When enabling unit files, override existing
                               symlinks. When shutting down, execute action
                               immediately.
     --preset-mode=MODE        Apply only enable, only disable, or all presets
     --root=PATH               Edit/enable/disable/mask unit files in the
                               specified root directory
     --image=PATH              Edit/enable/disable/mask unit files in the
                               specified disk image
     --image-policy=POLICY     Specify disk image dissection policy
  -n --lines=INTEGER           Number of journal entries to show
  -o --output=STRING           Change journal output mode (short, short-precise,
                               short-iso, short-iso-precise, short-full,
                               short-monotonic, short-unix, short-delta,
                               verbose, export, json, json-pretty, json-sse,
                               cat)
     --firmware-setup          Tell the firmware to show the setup menu on next
                               boot
     --boot-loader-menu=TIME   Boot into boot loader menu on next boot
     --boot-loader-entry=NAME  Boot into a specific boot loader entry on next
                               boot
     --reboot-argument=ARG     Specify argument string to pass to reboot()
     --kernel-cmdline=CMDLINE  Append to the kernel command line when loading
                               the kernel from the booted boot loader entry
     --plain                   Print unit dependencies as a list instead of a
                               tree
     --timestamp=FORMAT        Change format of printed timestamps (pretty,
                               unix, us, utc, us+utc)
     --read-only               Create read-only bind mount
     --mkdir                   Create directory before mounting, if missing
     --marked                  Restart/reload previously marked units
     --drop-in=NAME            Edit unit files using the specified drop-in file
                               name
     --when=TIME               Schedule halt/power-off/reboot/kexec action after
```

### `kali-service-stop`

官方给出的调用示例：`kali-service-stop -h`

```text
root@kali:~# kali-service-stop -h
┏━(Message from Kali developers)
┃
5:245m> systemctl [OPTIONS…] COMMAND …
Query or send control commands to the system manager.
Unit Commands:
  [list-units                  List units currently in memory
    [PATTERN…]]
  list-automounts              List automount units currently in memory, ordered
    [PATTERN…]                 by path
  list-paths [PATTERN…]        List path units currently in memory, ordered by
                               path
  list-sockets                 List socket units currently in memory, ordered by
    [PATTERN…]                 address
  list-timers                  List timer units currently in memory, ordered by
    [PATTERN…]                 next elapse
  is-active PATTERN…           Check whether units are active
  is-failed [PATTERN…]         Check whether units are failed or system is in
                               degraded state
  status                       Show runtime status of one or more units
    [PATTERN…|PID…]
  show                         Show properties of one or more units/jobs or the
    [PATTERN…|JOB…]            manager
  cat PATTERN…                 Show files and drop-ins of specified units
  help PATTERN…|PID…           Show manual for one or more units
  list-dependencies            Recursively show units which are required or
    [UNIT…]                    wanted by the units or by which those units are
                               required or wanted
  start UNIT…                  Start (activate) one or more units
  stop UNIT…                   Stop (deactivate) one or more units
  reload UNIT…                 Reload one or more units
  restart UNIT…                Start or restart one or more units
  try-restart UNIT…            Restart one or more units if active
  enqueue-marked               Enqueue jobs for all marked units
  reload-or-restart            Reload one or more units if possible, otherwise
    UNIT…                      start or restart
  try-reload-or-restart        If active, reload one or more units, if
    UNIT…                      supported, otherwise restart
  isolate UNIT                 Start one unit and stop all others
  kill UNIT…                   Send signal to processes of a unit
  clean UNIT…                  Clean runtime, cache, state, logs or
                               configuration of unit
  freeze PATTERN…              Freeze execution of unit processes
  thaw PATTERN…                Resume execution of a frozen unit
  set-property UNIT            Sets one or more properties of a unit
    PROPERTY=VALUE…
  bind UNIT PATH [PATH]        Bind-mount a path from the host into a unit's
                               namespace
  mount-image UNIT PATH [PATH  Mount an image from the host into a unit's
    [OPTS]]                    namespace
  service-log-level SERVICE    Get/set logging threshold for service
    [LEVEL]
  service-log-target SERVICE   Get/set logging target for service
    [TARGET]
  reset-failed                 Reset failed state for all, one, or more units
    [PATTERN…]
  whoami [PID…]                Return unit caller or specified PIDs are part of
Unit File Commands:
  list-unit-files              List installed unit files
    [PATTERN…]
  enable                       Enable one or more unit files
    [UNIT…|PATH…]
  disable UNIT…                Disable one or more unit files
  reenable UNIT…               Reenable one or more unit files
  preset UNIT…                 Enable/disable one or more unit files based on
                               preset configuration
  preset-all                   Enable/disable all unit files based on preset
                               configuration
  is-enabled UNIT…             Check whether unit files are enabled
  mask UNIT…                   Mask one or more units
  unmask UNIT…                 Unmask one or more units
  link PATH…                   Link one or more units files into the search path
  revert UNIT…                 Revert one or more unit files to vendor version
  add-wants TARGET             Add 'Wants' dependency for the target on
    UNIT…                      specified one or more units
  add-requires TARGET          Add 'Requires' dependency for the target on
    UNIT…                      specified one or more units
  edit UNIT…                   Edit one or more unit files
  get-default                  Get the name of the default target
  set-default TARGET           Set the default target
Machine Commands:
  list-machines                List local containers and host
    [PATTERN…]
Job Commands:
  list-jobs [PATTERN…]         List jobs
  cancel [JOB…]                Cancel all, one, or more jobs
Environment Commands:
  show-environment             Dump environment
  set-environment              Set one or more environment variables
    VARIABLE=VALUE…
  unset-environment            Unset one or more environment variables
    VARIABLE…
  import-environment           Import all or some environment variables
    VARIABLE…
Manager State Commands:
  daemon-reload                Reload systemd manager configuration
  daemon-reexec                Reexecute systemd manager
  log-level [LEVEL]            Get/set logging threshold for manager
  log-target [TARGET]          Get/set logging target for manager
  service-watchdogs            Get/set service watchdog state
    [BOOL]
System Commands:
  is-system-running            Check whether system is fully running
  default                      Enter system default mode
  rescue                       Enter system rescue mode
  emergency                    Enter system emergency mode
  halt                         Shut down and halt the system
  poweroff                     Shut down and power-off the system
  reboot                       Shut down and reboot the system
  kexec                        Shut down and reboot the system with kexec
  soft-reboot                  Shut down and reboot userspace
  exit [EXIT_CODE]             Request user instance or container exit
  switch-root [ROOT            Change to a different root file system
    [INIT]]
  sleep                        Put the system to sleep (through one of the
                               operations below)
  suspend                      Suspend the system
  hibernate                    Hibernate the system
  hybrid-sleep                 Hibernate and suspend the system
  suspend-then-hibernate       Suspend the system, wake after a period of time,
                               and hibernate
Options:
  -h --help                    Show this help
     --version                 Show package version
     --system                  Connect to the system service manager
     --user                    Connect to the user service manager
  -C --capsule=NAME            Connect to service manager of specified capsule
  -H --host=[USER@]HOST        Operate on remote host
  -M --machine=CONTAINER       Operate on local container
  -t --type=TYPE               List units of a particular type
     --state=STATE             List units with particular LOAD or SUB or ACTIVE
                               state
     --failed                  Shortcut for --state=failed
  -p --property=NAME           Show only properties by this name
  -P NAME                      Equivalent to --value --property=NAME
  -a --all                     Show all properties/all units currently in
                               memory, including dead/empty ones. To list all
                               units installed on the system, use
                               'list-unit-files' instead
  -l --full                    Don't ellipsize unit names on output
  -r --recursive               Show unit list of host and local containers
     --reverse                 Show reverse dependencies with
                               'list-dependencies'
     --before                  Show units ordered before with
                               'list-dependencies'
     --after                   Show units ordered after with 'list-dependencies'
     --with-dependencies       Show unit dependencies with 'status', 'cat',
                               'list-units', and 'list-unit-files'
     --job-mode=MODE           Specify how to deal with already queued jobs,
                               when queueing a new job
  -T --show-transaction        When enqueuing a unit job, show full transaction
     --show-types              When showing sockets, explicitly show their type
     --value                   When showing properties, only print the value
     --check-inhibitors=MODE   Whether to check inhibitors before shutting down,
                               sleeping, or hibernating
  -i                           Shortcut for --check-inhibitors=no
  -s --signal=SIGNAL           Which signal to send
     --kill-whom=WHOM          Whom to send signal to
     --kill-value=INT          Signal value to enqueue
     --kill-subgroup=PATH      Send signal to sub-control group only
     --what=RESOURCES          Which types of resources to remove
     --now                     Start or stop unit after enabling or disabling it
     --dry-run                 Only print what would be done. Currently
                               supported by verbs: halt, poweroff, reboot,
                               kexec, soft-reboot, suspend, hibernate,
                               suspend-then-hibernate, hybrid-sleep, default,
                               rescue, emergency, and exit.
  -q --quiet                   Suppress output
  -v --verbose                 Show unit logs while executing operation
     --no-warn                 Suppress several warnings shown by default
     --wait                    For (re)start, wait until service stopped again.
                               For is-system-running, wait until startup is
                               completed. For kill, wait until service stopped.
     --no-block                Do not wait until operation finished
     --no-wall                 Don't send wall message before
                               halt/power-off/reboot
     --message=MESSAGE         Specify human-readable reason for system shutdown
     --no-reload               Don't reload daemon after en-/dis-abling unit
                               files
     --legend=BOOL             Enable/disable the legend (column headers and
                               hints)
     --no-pager                Do not start a pager
     --no-ask-password         Do not prompt for password
     --global                  Edit/enable/disable/mask default user unit files
                               globally
     --runtime                 Edit/enable/disable/mask unit files temporarily
                               until next reboot
  -f --force                   When enabling unit files, override existing
                               symlinks. When shutting down, execute action
                               immediately.
     --preset-mode=MODE        Apply only enable, only disable, or all presets
     --root=PATH               Edit/enable/disable/mask unit files in the
                               specified root directory
     --image=PATH              Edit/enable/disable/mask unit files in the
                               specified disk image
     --image-policy=POLICY     Specify disk image dissection policy
  -n --lines=INTEGER           Number of journal entries to show
  -o --output=STRING           Change journal output mode (short, short-precise,
                               short-iso, short-iso-precise, short-full,
                               short-monotonic, short-unix, short-delta,
                               verbose, export, json, json-pretty, json-sse,
                               cat)
     --firmware-setup          Tell the firmware to show the setup menu on next
                               boot
     --boot-loader-menu=TIME   Boot into boot loader menu on next boot
     --boot-loader-entry=NAME  Boot into a specific boot loader entry on next
                               boot
     --reboot-argument=ARG     Specify argument string to pass to reboot()
     --kernel-cmdline=CMDLINE  Append to the kernel command line when loading
                               the kernel from the booted boot loader entry
     --plain                   Print unit dependencies as a list instead of a
                               tree
     --timestamp=FORMAT        Change format of printed timestamps (pretty,
                               unix, us, utc, us+utc)
     --read-only               Create read-only bind mount
     --mkdir                   Create directory before mounting, if missing
     --marked                  Restart/reload previously marked units
     --drop-in=NAME            Edit unit files using the specified drop-in file
                               name
     --when=TIME               Schedule halt/power-off/reboot/kexec action after
```

### `kali-setup`

官方给出的调用示例：`kali-setup -h`

```text
root@kali:~# kali-setup -h
┏━(Message from Kali developers)
┃
┃ The command kali-setup is deprecated. Please use kali-tweaks instead.
┃
┗━
```

## 4. 实践清单

按顺序做完这五步，就能把工具从「装上」推进到「会用」：

- [ ] **1.** **装好并确认版本** —— `sudo apt install kali-defaults`，再执行 `kali-defaults --version` 2>/dev/null || `kali-defaults -V`
- [ ] **2.** **读官方帮助** —— `kali-defaults -h`，需要细节时 `man kali-defaults`
- [ ] **3.** **在自有靶场跑最小用例** —— 用 `kali-defaults -h` 里最简单的那个子命令试一次
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/kali-defaults/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/kali-defaults/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/kali-defaults/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
