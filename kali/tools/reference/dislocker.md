# dislocker

> Read/write encrypted BitLocker volumes Dislocker has been designed to read BitLocker encrypted partitions under a Linux system. The driver used to read volumes encrypted in Windows system versions of the Vista to 10 and BitLocker-To-Go enc…

> **功能分类**：通用工具 ｜ **Kali 包**：`dislocker` ｜ **官方文档**：<https://www.kali.org/tools/dislocker/>

## 1. 安装

```bash
sudo apt update
sudo apt install dislocker
```

| 项目 | 内容 |
|------|------|
| 版本 | 0.7.3 |
| 架构 | any |
| 可执行命令 | `dislocker`、`dislocker-bek`、`dislocker-file`、`dislocker-find`、`dislocker-fuse`、`dislocker-metadata`、`libdislocker0-dev`、`libdislocker0.7t64` |
| 依赖 | `libc6`、`libdislocker0.7t64`、`libfuse3-4`、`libruby3.3` |
| 安装体积 | 95 KB |
| 官网 | <https://github.com/Aorimn/dislocker> |
| 源码仓库 | <https://salsa.debian.org/pkg-security-team/dislocker> |
| 包追踪 | <https://pkg.kali.org/pkg/dislocker> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
dislocker -h          # 查看用法
man dislocker         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 8 个可执行命令，下面是官方页面内嵌的帮助原文。

### `dislocker`

官方给出的调用示例：`dislocker -h`

```text
root@kali:~# dislocker -h
dislocker by Romain Coltel, v0.7.3 (compiled for Linux/x86_64)
Usage: dislocker [-hqrsv] [-l LOG_FILE] [-O OFFSET] [-V VOLUME DECRYPTMETHOD -F[N]] [-- ARGS...]
    with DECRYPTMETHOD = -p[RECOVERY_PASSWORD]|-f BEK_FILE|-u[USER_PASSWORD]|-k FVEK_FILE|-K VMK_FILE|-c
Options:
    -c, --clearkey        decrypt volume using a clear key (default)
    -f, --bekfile BEKFILE
                          decrypt volume using the bek file (on USB key)
    -F, --force-block=[N] force use of metadata block number N (1, 2 or 3)
    -h, --help            print this help and exit
    -k, --fvek FVEK_FILE  decrypt volume using the FVEK directly
    -K, --vmk VMK_FILE    decrypt volume using the VMK directly
    -l, --logfile LOG_FILE
                          put messages into this file (stdout by default)
    -O, --offset OFFSET   BitLocker partition offset, in bytes (default is 0)
    -p, --recovery-password=[RECOVERY_PASSWORD]
                          decrypt volume using the recovery password method
    -q, --quiet           do NOT display anything
    -r, --readonly        do not allow one to write on the BitLocker volume
    -s, --stateok         do not check the volume's state, assume it's ok to mount it
    -u, --user-password=[USER_PASSWORD]
                          decrypt volume using the user password method
    -v, --verbosity       increase verbosity (CRITICAL errors are displayed by default)
    -V, --volume VOLUME   volume to get metadata and keys from
    --                    end of program options, beginning of FUSE's ones
  ARGS are any arguments you want to pass to FUSE. You need to pass at least
the mount-point.
```

### `dislocker-bek`

官方给出的调用示例：`dislocker-bek -h`

```text
root@kali:~# dislocker-bek -h
Usage: dislocker-bek [-h] [-f file.bek]
  Reads .BEK files and prints information about them
```

### `dislocker-file`

官方给出的调用示例：`dislocker-file -h`

```text
root@kali:~# dislocker-file -h
dislocker by Romain Coltel, v0.7.3 (compiled for Linux/x86_64)
Usage: dislocker [-hqrsv] [-l LOG_FILE] [-O OFFSET] [-V VOLUME DECRYPTMETHOD -F[N]] [-- ARGS...]
    with DECRYPTMETHOD = -p[RECOVERY_PASSWORD]|-f BEK_FILE|-u[USER_PASSWORD]|-k FVEK_FILE|-K VMK_FILE|-c
Options:
    -c, --clearkey        decrypt volume using a clear key (default)
    -f, --bekfile BEKFILE
                          decrypt volume using the bek file (on USB key)
    -F, --force-block=[N] force use of metadata block number N (1, 2 or 3)
    -h, --help            print this help and exit
    -k, --fvek FVEK_FILE  decrypt volume using the FVEK directly
    -K, --vmk VMK_FILE    decrypt volume using the VMK directly
    -l, --logfile LOG_FILE
                          put messages into this file (stdout by default)
    -O, --offset OFFSET   BitLocker partition offset, in bytes (default is 0)
    -p, --recovery-password=[RECOVERY_PASSWORD]
                          decrypt volume using the recovery password method
    -q, --quiet           do NOT display anything
    -r, --readonly        do not allow one to write on the BitLocker volume
    -s, --stateok         do not check the volume's state, assume it's ok to mount it
    -u, --user-password=[USER_PASSWORD]
                          decrypt volume using the user password method
    -v, --verbosity       increase verbosity (CRITICAL errors are displayed by default)
    -V, --volume VOLUME   volume to get metadata and keys from
    --                    end of program options, beginning of FUSE's ones
  ARGS are any arguments you want to pass to FUSE. You need to pass at least
the mount-point.
```

### `dislocker-find`

官方给出的调用示例：`dislocker-find -h`

```text
root@kali:~# dislocker-find -h
Usage: /usr/bin/dislocker-find [-h] [files...]
  Try to find partitions which are BitLocker-encrypted. Each found is
   printed on stdout.
  If one or more file is passed as argument, /usr/bin/dislocker-find will print each
   file which is a BitLocker-encrypted volume.
  The number of partition found is returned (in $? in sh).
```

### `dislocker-fuse`

官方给出的调用示例：`dislocker-fuse -h`

```text
root@kali:~# dislocker-fuse -h
dislocker by Romain Coltel, v0.7.3 (compiled for Linux/x86_64)
Usage: dislocker [-hqrsv] [-l LOG_FILE] [-O OFFSET] [-V VOLUME DECRYPTMETHOD -F[N]] [-- ARGS...]
    with DECRYPTMETHOD = -p[RECOVERY_PASSWORD]|-f BEK_FILE|-u[USER_PASSWORD]|-k FVEK_FILE|-K VMK_FILE|-c
Options:
    -c, --clearkey        decrypt volume using a clear key (default)
    -f, --bekfile BEKFILE
                          decrypt volume using the bek file (on USB key)
    -F, --force-block=[N] force use of metadata block number N (1, 2 or 3)
    -h, --help            print this help and exit
    -k, --fvek FVEK_FILE  decrypt volume using the FVEK directly
    -K, --vmk VMK_FILE    decrypt volume using the VMK directly
    -l, --logfile LOG_FILE
                          put messages into this file (stdout by default)
    -O, --offset OFFSET   BitLocker partition offset, in bytes (default is 0)
    -p, --recovery-password=[RECOVERY_PASSWORD]
                          decrypt volume using the recovery password method
    -q, --quiet           do NOT display anything
    -r, --readonly        do not allow one to write on the BitLocker volume
    -s, --stateok         do not check the volume's state, assume it's ok to mount it
    -u, --user-password=[USER_PASSWORD]
                          decrypt volume using the user password method
    -v, --verbosity       increase verbosity (CRITICAL errors are displayed by default)
    -V, --volume VOLUME   volume to get metadata and keys from
    --                    end of program options, beginning of FUSE's ones
  ARGS are any arguments you want to pass to FUSE. You need to pass at least
the mount-point.
```

### `dislocker-metadata`

官方给出的调用示例：`dislocker-metadata -h`

```text
root@kali:~# dislocker-metadata -h
Usage: dislocker [-hov] [-V VOLUME]
    -h         print this help and exit
    -o         partition offset
    -v         increase verbosity to debug level
    -V VOLUME  volume to get metadata from
```

## 4. 实践清单

按顺序做完这五步，就能把工具从「装上」推进到「会用」：

- [ ] **1.** **装好并确认版本** —— `sudo apt install dislocker`，再执行 `dislocker --version` 2>/dev/null || `dislocker -V`
- [ ] **2.** **读官方帮助** —— `dislocker -h`，需要细节时 `man dislocker`
- [ ] **3.** **在自有靶场跑最小用例** —— 官方给出的调用形式是：`Usage: dislocker [-hqrsv] [-l LOG_FILE] [-O OFFSET] [-V VOLUME DECRYPTMETHOD -F[N]] [-- ARGS...]`
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/dislocker/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/dislocker/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/dislocker/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
