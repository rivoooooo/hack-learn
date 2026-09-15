# ivre

> Network recon framework IVRE or DRUNK This package contains IVRE (Instrument de veille sur les réseaux extérieurs) or DRUNK (Dynamic Recon of UNKnown networks), a network recon framework, including tools for passive recon (flow analytics r…

> **功能分类**：通用工具 ｜ **Kali 包**：`ivre` ｜ **官方文档**：<https://www.kali.org/tools/ivre/>

## 1. 安装

```bash
sudo apt update
sudo apt install ivre
```

| 项目 | 内容 |
|------|------|
| 版本 | 0.9.21 |
| 架构 | all |
| 可执行命令 | `ivre`、`ivre-doc` |
| 依赖 | `libjs-sphinxdoc`、`python3`、`python3-bottle`、`python3-cryptography`、`python3-dbus`、`python3-matplotlib`、`python3-mysqldb`、`python3-openssl`、`python3-pil`、`python3-psycopg2`、`python3-pymongo`、`python3-sqlalchemy` 等 |
| 安装体积 | 18.15 MB |
| 官网 | <https://ivre.rocks> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/ivre> |
| 包追踪 | <https://pkg.kali.org/pkg/ivre> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
ivre -h          # 查看用法
man ivre         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 2 个可执行命令，下面是官方页面内嵌的帮助原文。

### `ivre`

> 官方示例调用：`ivre -h`

```text
root@kali:~# ivre -h
IVRE - Network recon framework
Copyright 2011 - 2024 Pierre LALET <
[email protected]
>
Version 0.9.21+kali
Python 3.14.6 (main, Jun 10 2026, 18:54:31) [GCC 15.2.0]
Linux kali 7.1.5+kali-amd64 #1 SMP PREEMPT_DYNAMIC Kali 7.1.5-1kali1 (2026-07-29) x86_64
```

## 4. 实践清单

按顺序做完这五步，就能把工具从「装上」推进到「会用」：

- [ ] **1.** **装好并确认版本** —— `sudo apt install ivre`，再执行 `ivre --version` 2>/dev/null || `ivre -V`
- [ ] **2.** **读官方帮助** —— `ivre -h`，需要细节时 `man ivre`
- [ ] **3.** **在自有靶场跑最小用例** —— 用 `ivre -h` 里最简单的那个子命令试一次
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/ivre/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/ivre/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/ivre/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
