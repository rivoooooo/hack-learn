# ftester

> Tool for testing firewalls and Intrusion Detection System (IDS) The Firewall Tester (FTester) is a tool designed for testing firewall filtering policies and Intrusion Detection System (IDS) capabilities. Features: firewall testing IDS test…

> **功能分类**：信息搜集 ｜ **Kali 包**：`ftester` ｜ **官方文档**：<https://www.kali.org/tools/ftester/>

## 1. 安装

```bash
sudo apt update
sudo apt install ftester
```

| 项目 | 内容 |
|------|------|
| 版本 | 1.0 |
| 架构 | all |
| 可执行命令 | `ftester`、`freport`、`ftest`、`ftestd` |
| 依赖 | `libnet-pcap-perl`、`libnet-rawip-perl`、`libnetpacket-perl`、`perl`、`freport` |
| 安装体积 | 91 KB |
| 官网 | <https://dev.inversepath.com/ftester/> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/ftester> |
| 包追踪 | <https://pkg.kali.org/pkg/ftester> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
ftester -h          # 查看用法
man ftester         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 4 个可执行命令，下面是官方页面内嵌的帮助原文。

### `freport`

> 官方示例调用：`freport -h`

```text
root@kali:~# freport -h
Usage /usr/bin/freport ftest.log ftestd.log at /usr/bin/freport line 15.
```

### `ftest`

> 官方示例调用：`ftest --help`

```text
root@kali:~# ftest --help
/usr/bin/ftest version [unknown] calling Getopt::Std::getopts (version 1.14 [paranoid]),
running under Perl version 5.42.2.
Usage: ftest [-OPTIONS [-MORE_OPTIONS]] [--] [PROGRAM_ARG1 ...]
The following single-character options are accepted:
	With arguments: -c -d -e -f -g -k -m -p -s -t
	Boolean (without arguments): -F -r -v
Options may be merged together.  -- stops processing of options.
Space is not required between options and their arguments.
  [Now continuing due to backward compatibility and excessive paranoia.
   See 'perldoc Getopt::Std' about $Getopt::Std::STANDARD_HELP_VERSION.]
FTester client v1.0
Copyright (C) 2001-2006 Andrea Barisani <
[email protected]
>
Configuration options:
  -f <conf_file>
  -c <source_ip>:<source_port>:<dest_ip>:<dest_port>:<flags>:<protocol>:<tos>
  -v <verbose>
Timing options:
  -d <delay, 0.25 = 250 ms>
  -s <sleep time, 1 = 1 s>
Evasion options:
  -e <evasion method>
  -t <ids_ttl>
Connection options:
  -r <reset connection>
  -F <end connection>
  -g <IP fragments number, es. 4|IP fragments size, es. 16b>
  -p <TCP segments number, es. 4|TCP segments size, es 6b>
  -k <cksum value, es. 60000>
  -m <marker>
```

## 4. 实践清单

按顺序做完这五步，就能把工具从「装上」推进到「会用」：

- [ ] **1.** **装好并确认版本** —— `sudo apt install ftester`，再执行 `ftester --version` 2>/dev/null || `ftester -V`
- [ ] **2.** **读官方帮助** —— `ftester -h`，需要细节时 `man ftester`
- [ ] **3.** **在自有靶场跑最小用例** —— 官方给出的调用形式是：`Usage /usr/bin/freport ftest.log ftestd.log at /usr/bin/freport line 15.`
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/ftester/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/defense-evasion.md`](../../tools/by-attack/defense-evasion.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/ftester/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/ftester/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
