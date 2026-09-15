# gparted

> GNOME partition editor GParted uses libparted to detect and manipulate devices and partition tables while several (optional) filesystem tools provide support for filesystems not included in libparted.

> **功能分类**：数字取证 ｜ **Kali 包**：`gparted` ｜ **官方文档**：<https://www.kali.org/tools/gparted/>

## 1. 安装

```bash
sudo apt update
sudo apt install gparted
```

| 项目 | 内容 |
|------|------|
| 版本 | 1.8.0 |
| 架构 | any |
| 可执行命令 | `gparted`、`gparted-common` |
| 依赖 | `gparted-common`、`libatkmm-1.6-1v5`、`libc6`、`libcairomm-1.0-1v5`、`libgcc-s1`、`libglib2.0-0t64`、`libglibmm-2.4-1t64`、`libgtk-3-0t64`、`libgtkmm-3.0-1t64`、`libpangomm-1.4-1v5`、`libparted-fs-resize0t64`、`libparted2t64` 等 |
| 安装体积 | 2.25 MB |
| 官网 | <https://gparted.org> |
| 源码仓库 | <https://salsa.debian.org/debian/gparted> |
| 包追踪 | <https://pkg.kali.org/pkg/gparted> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
gparted -h          # 查看用法
man gparted         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 2 个可执行命令，下面是官方页面内嵌的帮助原文。

### `man`

> 官方示例调用：`man gparted`

```text
root@kali:~# man gparted
GPARTED(8)                       GParted Manual                      GPARTED(8)
NAME
     gparted - GNOME Partition Editor for manipulating disk partitions.
SYNOPSIS
     gparted [device]...
DESCRIPTION
     The  gparted application is the GNOME partition editor for creating, reor-
     ganizing, and deleting disk partitions.
     A disk device can be subdivided into one or more partitions.  The  gparted
     application enables you to change the partition organization on a disk de-
     vice while preserving the contents of the partition.
     With gparted you can accomplish the following tasks:
     - Create a partition table on a disk device.
     - Enable and disable partition flags such as boot and hidden.
     -  Perform  actions  with partitions such as create, delete, resize, move,
     check, label, copy, and paste.
     More documentation can be found in the application help manual, and online
     at:
     https://gparted.org
EXAMPLES
     You can run gparted from a command line and specify one or more  disk  de-
     vices.
     For  example,  to start gparted with the devices /dev/sda and /dev/sdc you
     would use the following command:
     gparted /dev/sda /dev/sdc
NOTES
     Editing partitions has the potential to cause LOSS of DATA.
     The gparted application is designed to enable you to edit partitions while
     reducing the risk of data loss.  The application is carefully  tested  and
     is  used  by  the GParted project team.  However, loss of data might occur
     due to software bugs, hardware problems, or power failure.
     You can help to reduce the risk of data loss by not mounting or unmounting
     partitions outside of the gparted application while gparted is running.
     You are advised to BACKUP your DATA before using the gparted application.
REPORTING BUGS
     Report bugs at:
     https://gparted.org/bugs.php
AUTHOR
     Manual page written by Curtis Gedak <
[email protected]
>
SEE ALSO
     parted(8), fdisk(8), mkfs(8), ntfsprogs(8)
gparted                          Jan 16th, 2011                      GPARTED(8)
```

## 4. 实践清单

按顺序做完这五步，就能把工具从「装上」推进到「会用」：

- [ ] **1.** **装好并确认版本** —— `sudo apt install gparted`，再执行 `gparted --version` 2>/dev/null || `gparted -V`
- [ ] **2.** **读官方帮助** —— `gparted -h`，需要细节时 `man gparted`
- [ ] **3.** **在自有靶场跑最小用例** —— 用 `gparted -h` 里最简单的那个子命令试一次
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/gparted/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/gparted/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/gparted/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
