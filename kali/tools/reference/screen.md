# screen

> Terminal multiplexer with VT100/ANSI terminal emulation GNU Screen is a terminal multiplexer that runs several separate “screens” on a single physical character-based terminal. Each virtual terminal emulates a DEC VT100 plus several ANSI X…

> **功能分类**：无线攻击 ｜ **Kali 包**：`screen` ｜ **官方文档**：<https://www.kali.org/tools/screen/>

## 1. 安装

```bash
sudo apt update
sudo apt install screen
```

| 项目 | 内容 |
|------|------|
| 版本 | 5.0.2 |
| 架构 | any |
| 可执行命令 | `screen`、`screen-udeb` |
| 依赖 | `debianutils`、`libc6`、`libpam0g`、`libtinfo6`、`ncurses-term` |
| 安装体积 | 1007 KB |
| 官网 | <https://savannah.gnu.org/projects/screen> |
| 源码仓库 | <https://salsa.debian.org/debian/screen> |
| 包追踪 | <https://pkg.kali.org/pkg/screen> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
screen -h          # 查看用法
man screen         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 2 个可执行命令，下面是官方页面内嵌的帮助原文。

### `screen`

> 官方示例调用：`screen -h`

```text
root@kali:~# screen -h
Use: screen [-opts] [cmd [args]]
 or: screen -r [host.tty]
Options:
-4            Resolve hostnames only to IPv4 addresses.
-6            Resolve hostnames only to IPv6 addresses.
-a            Force all capabilities into each window's termcap.
-A -[r|R]     Adapt all windows to the new display width & height.
-c file       Read configuration file instead of '.screenrc'.
-d (-r)       Detach the elsewhere running screen (and reattach here).
-dmS name     Start as daemon: Screen session in detached mode.
-D (-r)       Detach and logout remote (and reattach here).
-D -RR        Do whatever is needed to get a screen session.
-e xy         Change command characters.
-f            Flow control on, -fn = off, -fa = auto.
-h lines      Set the size of the scrollback history buffer.
-i            Interrupt output sooner when flow control is on.
-ls [match]   or
-list         Do nothing, just list our SocketDir [on possible matches].
-L            Turn on output logging.
-Logfile file Set logfile name.
-m            ignore $STY variable, do create a new screen session.
-O            Choose optimal output rather than exact vt100 emulation.
-p window     Preselect the named window if it exists.
-P            Tell screen to enable authentication.
-q            Quiet startup. Exits with non-zero return code if unsuccessful.
-Q            Commands will send the response to the stdout of the querying process.
-r [session]  Reattach to a detached screen process.
-R            Reattach if possible, otherwise start a new session.
-s shell      Shell to execute rather than $SHELL.
-S sockname   Name this session <pid>.sockname instead of <pid>.<tty>.<host>.
-t title      Set title. (window's name).
-T term       Use term as $TERM for windows, rather than "screen".
-U            Tell screen to use UTF-8 encoding.
-v            Print "Screen version 5.0.2 (build on 2026-08-25 08:57:57) ".
-wipe [match] Do nothing, just clean up SocketDir [on possible matches].
-x            Attach to a not detached screen. (Multi display mode).
-X            Execute <cmd> as a screen command in the specified session.
```

## 4. 实践清单

按顺序做完这五步，就能把工具从「装上」推进到「会用」：

- [ ] **1.** **装好并确认版本** —— `sudo apt install screen`，再执行 `screen --version` 2>/dev/null || `screen -V`
- [ ] **2.** **读官方帮助** —— `screen -h`，需要细节时 `man screen`
- [ ] **3.** **在自有靶场跑最小用例** —— 用 `screen -h` 里最简单的那个子命令试一次
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/screen/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/screen/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/screen/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
