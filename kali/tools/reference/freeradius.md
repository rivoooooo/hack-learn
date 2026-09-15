# freeradius

> High-performance and highly configurable RADIUS server FreeRADIUS is a high-performance RADIUS server with support for: Authentication by local files, SQL, Kerberos, LDAP, PAM, and more. Powerful policy configuration language. Proxying and…

> **功能分类**：通用工具 ｜ **Kali 包**：`freeradius` ｜ **官方文档**：<https://www.kali.org/tools/freeradius/>

## 1. 安装

```bash
sudo apt update
sudo apt install freeradius
```

| 项目 | 内容 |
|------|------|
| 版本 | 3.2.10 |
| 架构 | any |
| 可执行命令 | `freeradius`、`checkrad`、`rad_counter`、`raddebug`、`radmin`、`rlm_sqlippool_tool`、`freeradius-common`、`freeradius-config`、`freeradius-dhcp`、`freeradius-iodbc`、`freeradius-krb5`、`freeradius-ldap`、`freeradius-memcached`、`freeradius-mysql`、`freeradius-postgresql`、`freeradius-python3`、`freeradius-redis`、`freeradius-rest`、`freeradius-utils`、`radclient`、`radconf2json`、`radcrypt`、`raddict2json`、`radeapclient`、`radlast`、`radmod2json`、`radsecret`、`radsniff`、`radsqlrelay`、`radtest`、`radwho`、`radzap`、`rlm_ippool_tool`、`smbencrypt`、`freeradius-yubikey`、`libfreeradius-dev`、`libfreeradius3` |
| 依赖 | `freeradius-common`、`freeradius-config`、`libc6`、`libcrypt1`、`libct4`、`libfreeradius3`、`libgdbm6t64`、`libjson-c5`、`libpam0g`、`libperl5.42`、`libreadline8t64`、`libsqlite3-0` 等 |
| 安装体积 | 3.38 MB |
| 官网 | <http://www.freeradius.org/> |
| 源码仓库 | <https://salsa.debian.org/debian/freeradius> |
| 包追踪 | <https://pkg.kali.org/pkg/freeradius> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
freeradius -h          # 查看用法
man freeradius         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 37 个可执行命令，下面是官方页面内嵌的帮助原文。

### `checkrad`

官方给出的调用示例：`checkrad -h`

```text
root@kali:~# checkrad -h
Usage: checkrad nas_type nas_ip nas_port login session_id
```

### `freeradius`

官方给出的调用示例：`freeradius -h`

```text
root@kali:~# freeradius -h
Usage: freeradius [options]
Options:
  -C            Check configuration and exit.
  -f            Run as a foreground process, not a daemon.
  -h            Print this help message.
  -i <ipaddr>   Listen on ipaddr ONLY.
  -l <log_file> Logging output will be written to this file.
  -m            On SIGINT or SIGQUIT clean up all used memory instead of just exiting.
  -n <name>     Read raddb/name.conf instead of raddb/radiusd.conf.
  -p <port>     Listen on port ONLY.
  -P            Always write out PID, even with -f.
  -s            Do not spawn child processes to handle requests (same as -ft).
  -t            Disable threads.
  -v            Print server version information.
  -X            Turn on full debugging (similar to -tfxxl stdout).
  -x            Turn on additional debugging (-xx gives more debugging).
```

### `rad_counter`

官方给出的调用示例：`rad_counter -h`

```text
root@kali:~# rad_counter -h
Usage: rad_counter --file=<counter filename> [OPTION...]
Query and maintain FreeRADIUS rlm_counter DB file.
Arguments:
--file=<filename>               Counter DB filename.
Options:
--user=<username>               Information for specific user.
--match=<regexp>                Information for matching users.
--reset=<number>                Reset counter to <number>.
                                If divisor is set use it,
                                else <number> means seconds.
--help                          Show this help screen.
--(hours|minutes|seconds)       Specify information divisor.
```

### `raddebug`

官方给出的调用示例：`raddebug -h`

```text
root@kali:~# raddebug -h
Illegal option -h
Usage: raddebug: [-c condition] [-d directory] [-n name] [-D dictdir]  [-i client-ip-address] [-I client-ipv6-address] [-f socket_file] [-t timeout] [-u user]
```

### `radmin`

官方给出的调用示例：`radmin -h`

```text
root@kali:~# radmin -h
Usage: radmin [ args ]
  -d raddb_dir    Configuration files are in "raddbdir/*".
  -D <dictdir>    Set main dictionary directory (defaults to /usr/share/freeradius).
  -e command      Execute 'command' and then exit.
  -E              Echo commands as they are being executed.
  -f socket_file  Open socket_file directly, without reading radius.conf
  -h              Print usage help information.
  -i input_file   Read commands from 'input_file'.
  -n name         Read raddb/name.conf instead of raddb/radiusd.conf
  -q              Quiet mode.
  -v              Show program version information.
```

### `rlm_sqlippool_tool`

官方给出的调用示例：`rlm_sqlippool_tool -h`

```text
root@kali:~# rlm_sqlippool_tool -h
Usage:
  rlm_sqlippool_tool -p <pool_name> -s <range_start> -e <range_end> -t <table_name> (-d <sql_dialect> | -f <raddb_dir> [ -i <instance> ]) [ -c <capacity> ] [ -x <existing_ips_file> ]
or:
  rlm_sqlippool_tool -y <pool_defs_yaml_file> -t <table_name> (-d <dialect> | -f <raddb_dir> [ -i <instance> ]) [ -x <existing_ips_file> ]
```

### `radclient`

官方给出的调用示例：`radclient --help`

```text
root@kali:~# radclient --help
radclient: invalid option -- '-'
Usage: radclient [options] server[:port] <command> [<secret>]
  <command>              One of auth, acct, status, coa, disconnect or auto.
  -4                     Use IPv4 address of server
  -6                     Use IPv6 address of server.
  -b                     Mandate checks for Blast RADIUS issue (this is not set by default).
  -c <count>             Send each packet 'count' times.
  -d <raddb>             Set user dictionary directory (defaults to /etc/freeradius/3.0).
  -D <dictdir>           Set main dictionary directory (defaults to /usr/share/freeradius).
  -f <file>[:<file>]     Read packets from file, not stdin.
                         If a second file is provided, it will be used to verify responses
  -F                     Print the file name, packet number and reply code.
  -h                     Print usage help information.
  -n <num>               Send N requests/s
  -p <num>               Send 'num' packets from a file in parallel.
  -q                     Do not print anything out.
  -r <retries>           If timeout, retry sending the packet 'retries' times.
  -s                     Print out summary information of auth results.
  -S <file>              read secret from file, not command line.
  -t <timeout>           Wait 'timeout' seconds before retrying (may be a floating point number).
  -v                     Show program version information.
  -x                     Debugging mode.
  -P <proto>             Use proto (tcp or udp) for transport.
```

### `radconf2json`

官方给出的调用示例：`radconf2json -h`

```text
root@kali:~# radconf2json -h
Usage: radconf2json [options]
  -d <raddb>    Set raddb directory (default /etc/freeradius/3.0).
  -E            Keep `${var}` references verbatim in the JSON instead of
                resolving them at conversion time.  `$INCLUDE` still fires.
  -n <name>     Read <name>.conf instead of radiusd.conf.
  -o <file>     Write JSON to <file> (default stdout).
  -x            Enable debug output (repeatable).
  -X            Verbose debug output.
  -h            This help.
```

### `radcrypt`

官方给出的调用示例：`radcrypt -h`

```text
root@kali:~# radcrypt -h
Unknown option: h
Usage: radcrypt [--des|--md5|--check] plaintext_password [crypted_password]
```

### `raddict2json`

官方给出的调用示例：`raddict2json -h`

```text
root@kali:~# raddict2json -h
Usage: raddict2json [options]
  -D <dict>     Dictionary directory (default /usr/share/freeradius).
  -n <name>     Read <name> as the entry-point dictionary (default 'dictionary').
  -o <file>     Write JSON to <file> (default stdout).
  -x            Enable debug output.
  -h            This help.
```

## 4. 实践清单

按顺序做完这五步，就能把工具从「装上」推进到「会用」：

- [ ] **1.** **装好并确认版本** —— `sudo apt install freeradius`，再执行 `freeradius --version` 2>/dev/null || `freeradius -V`
- [ ] **2.** **读官方帮助** —— `freeradius -h`，需要细节时 `man freeradius`
- [ ] **3.** **在自有靶场跑最小用例** —— 官方给出的调用形式是：`Usage: checkrad nas_type nas_ip nas_port login session_id`
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/freeradius/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/credential-access.md`](../../tools/by-attack/credential-access.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/freeradius/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/freeradius/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
