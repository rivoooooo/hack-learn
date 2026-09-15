# gtkhash

> libb2-1 libc6 libcaja-extension1 libgcrypt20 libglib2.0-0t64 libgtk-3-0t64

> **功能分类**：通用工具 ｜ **Kali 包**：`gtkhash` ｜ **官方文档**：<https://www.kali.org/tools/gtkhash/>

## 1. 安装

```bash
sudo apt update
sudo apt install gtkhash
```

| 项目 | 内容 |
|------|------|
| 版本 | 1.5 |
| 架构 | any |
| 可执行命令 | `caja-gtkhash`、`gtkhash`、`nemo-gtkhash`、`thunar-gtkhash` |
| 安装体积 | 497 KB |
| 官网 | <https://gtkhash.org> |
| 源码仓库 | <https://salsa.debian.org/debian/gtkhash> |
| 包追踪 | <https://pkg.kali.org/pkg/gtkhash> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
caja-gtkhash -h          # 查看用法
man caja-gtkhash         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 4 个可执行命令，下面是官方页面内嵌的帮助原文。

### `gtkhash`

官方给出的调用示例：`gtkhash -h`

```text
root@kali:~# gtkhash -h
Usage:
  gtkhash [OPTION…] [FILE|URI...]
Help Options:
  -h, --help                    Show help options
  --help-all                    Show all help options
  --help-gtk                    Show GTK+ Options
Application Options:
  -c, --check=DIGEST            Check against the specified digest or checksum
  -C, --check-file=FILE|URI     Check digests or checksums from the specified file
  -f, --function=FUNCTION       Enable the specified Hash Function (e.g. MD5)
  -t, --text=TEXT               Hash the specified text
  -v, --version                 Show version information
  --display=DISPLAY             X display to use
```

## 4. 实践清单

按顺序做完这五步，就能把工具从「装上」推进到「会用」：

- [ ] **1.** **装好并确认版本** —— `sudo apt install gtkhash`，再执行 `caja-gtkhash --version` 2>/dev/null || `caja-gtkhash -V`
- [ ] **2.** **读官方帮助** —— `caja-gtkhash -h`，需要细节时 `man caja-gtkhash`
- [ ] **3.** **在自有靶场跑最小用例** —— 官方给出的调用形式是：`Usage:`
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/gtkhash/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/gtkhash/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/gtkhash/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
