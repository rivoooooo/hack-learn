# sqlsus

> MySQL injection tool sqlsus is an open source MySQL injection and takeover tool, written in perl. Via a command line interface, you can retrieve the database(s) structure, inject your own SQL queries (even complex ones), download files fro…

> **功能分类**：Web 应用 ｜ **Kali 包**：`sqlsus` ｜ **官方文档**：<https://www.kali.org/tools/sqlsus/>

## 1. 安装

```bash
sudo apt update
sudo apt install sqlsus
```

| 项目 | 内容 |
|------|------|
| 版本 | 0.7.2 |
| 架构 | all |
| 可执行命令 | `sqlsus` |
| 依赖 | `libdbd-sqlite3-perl`、`libhtml-linkextractor-perl`、`liblwp-protocol-socks-perl`、`libterm-readline-gnu-perl`、`libwww-perl`、`perl`、`sqlite3` |
| 安装体积 | 156 KB |
| 官网 | <https://sqlsus.sourceforge.net/> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/sqlsus> |
| 包追踪 | <https://pkg.kali.org/pkg/sqlsus> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
sqlsus -h          # 查看用法
man sqlsus         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `sqlsus`

官方给出的调用示例：`sqlsus -g sqlsus.cfg`

```text
root@kali:~# sqlsus -g sqlsus.cfg
              sqlsus version 0.7.2
  Copyright (c) 2008-2011 Jérémy Ruffet (sativouf)
[+] Configuration successfully saved to sqlsus.cfg
```

### `nano`

官方给出的调用示例：`nano sqlsus.cfg`

```text
root@kali:~# nano sqlsus.cfg
```

### `sqlsus（示例）`

官方给出的调用示例：`sqlsus sqlsus.cfg`

```text
root@kali:~# sqlsus sqlsus.cfg
              sqlsus version 0.7.2
  Copyright (c) 2008-2011 Jérémy Ruffet (sativouf)
[+] Session "192.168.1.25" created
sqlsus> start
```

## 4. 实践清单

按顺序做完这五步，就能把工具从「装上」推进到「会用」：

- [ ] **1.** **装好并确认版本** —— `sudo apt install sqlsus`，再执行 `sqlsus --version` 2>/dev/null || `sqlsus -V`
- [ ] **2.** **读官方帮助** —— `sqlsus -h`，需要细节时 `man sqlsus`
- [ ] **3.** **在自有靶场跑最小用例** —— 用 `sqlsus -h` 里最简单的那个子命令试一次
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/sqlsus/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/initial-access.md`](../../tools/by-attack/initial-access.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/sqlsus/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/sqlsus/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
