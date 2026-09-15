# parted

> Disk partition manipulator GNU Parted is a program that allows you to create, destroy, resize, move, and copy disk partitions. This is useful for creating space for new operating systems, reorganizing disk usage, and copying data to new ha…

> **功能分类**：数字取证 ｜ **Kali 包**：`parted` ｜ **官方文档**：<https://www.kali.org/tools/parted/>

## 1. 安装

```bash
sudo apt update
sudo apt install parted
```

| 项目 | 内容 |
|------|------|
| 版本 | 3.7 |
| 架构 | any |
| 可执行命令 | `libparted-dev`、`libparted-fs-resize0-udeb`、`libparted-fs-resize0t64`、`libparted-i18n`、`libparted2-udeb`、`libparted2t64`、`parted`、`partprobe`、`parted-doc`、`parted-udeb` |
| 依赖 | `libc6`、`libparted2t64`、`libreadline8t64`、`libtinfo6`、`libuuid1` |
| 安装体积 | 122 KB |
| 官网 | <https://www.gnu.org/software/parted> |
| 源码仓库 | <https://salsa.debian.org/parted-team/parted> |
| 包追踪 | <https://pkg.kali.org/pkg/parted> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
libparted-dev -h          # 查看用法
man libparted-dev         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 10 个可执行命令，下面是官方页面内嵌的帮助原文。

### `parted`

> 官方示例调用：`parted -h`

```text
root@kali:~# parted -h
Usage: parted [OPTION]... [DEVICE [COMMAND [PARAMETERS]...]...]
Apply COMMANDs with PARAMETERS to DEVICE.  If no COMMAND(s) are given, run in
interactive mode.
OPTIONs:
  -h, --help                      displays this help message
  -l, --list                      lists partition layout on all block devices
  -m, --machine                   displays machine parseable output
  -j, --json                      displays JSON output
  -s, --script                    never prompts for user intervention
  -f, --fix                       in script mode, fix instead of abort when asked
  -v, --version                   displays the version
  -a, --align=[none|cyl|min|opt]  alignment for new partitions
COMMANDs:
  align-check TYPE N                       check partition N for TYPE(min|opt)
        alignment
  help [COMMAND]                           print general help, or help on
        COMMAND
  mklabel,mktable LABEL-TYPE               create a new disklabel (partition
        table)
  mkpart PART-TYPE [FS-TYPE] START END     make a partition
  name NUMBER NAME                         name partition NUMBER as NAME
  print [devices|free|list,all]            display the partition table, or
        available devices, or free space, or all found partitions
  quit                                     exit program
  rescue START END                         rescue a lost partition near START
        and END
  resizepart NUMBER END                    resize partition NUMBER
  rm NUMBER                                delete partition NUMBER
  select DEVICE                            choose the device to edit
  disk_set FLAG STATE                      change the FLAG on selected device
  disk_toggle [FLAG]                       toggle the state of FLAG on selected
        device
  set NUMBER FLAG STATE                    change the FLAG on partition NUMBER
  toggle [NUMBER [FLAG]]                   toggle the state of FLAG on partition
        NUMBER
  type NUMBER TYPE-ID or TYPE-UUID         type set TYPE-ID or TYPE-UUID of
        partition NUMBER
  unit UNIT                                set the default unit to UNIT
  version                                  display the version number and
        copyright information of GNU Parted
Report bugs to
[email protected]
```

### `partprobe`

> 官方示例调用：`partprobe -h`

```text
root@kali:~# partprobe -h
Usage: partprobe [OPTION] [DEVICE]...
Inform the operating system about partition table changes.
  -d, --dry-run    do not actually inform the operating system
  -s, --summary    print a summary of contents
  -h, --help       display this help and exit
  -v, --version    output version information and exit
When no DEVICE is given, probe all partitions.
Report bugs to <
[email protected]
>.
```

## 4. 实践清单

按顺序做完这五步，就能把工具从「装上」推进到「会用」：

- [ ] **1.** **装好并确认版本** —— `sudo apt install parted`，再执行 `libparted-dev --version` 2>/dev/null || `libparted-dev -V`
- [ ] **2.** **读官方帮助** —— `libparted-dev -h`，需要细节时 `man libparted-dev`
- [ ] **3.** **在自有靶场跑最小用例** —— 官方给出的调用形式是：`Usage: parted [OPTION]... [DEVICE [COMMAND [PARAMETERS]...]...]`
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/parted/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/parted/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/parted/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
