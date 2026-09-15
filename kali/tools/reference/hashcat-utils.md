# hashcat-utils

> Set of small utilities for advanced password cracking Hashcat-utils are a set of small utilities that are useful in advanced password cracking. They all are packed into multiple stand-alone binaries. All of these utils are designed to exec…

> **功能分类**：口令攻击 ｜ **Kali 包**：`hashcat-utils` ｜ **官方文档**：<https://www.kali.org/tools/hashcat-utils/>

## 1. 安装

```bash
sudo apt update
sudo apt install hashcat-utils
```

| 项目 | 内容 |
|------|------|
| 版本 | 1.10 |
| 架构 | any |
| 可执行命令 | `hashcat-utils` |
| 依赖 | `libc6`、`perl` |
| 安装体积 | 511 KB |
| 官网 | <https://github.com/hashcat/hashcat-utils/> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/hashcat-utils> |
| 包追踪 | <https://pkg.kali.org/pkg/hashcat-utils> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
hashcat-utils -h          # 查看用法
man hashcat-utils         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

> 官方页面未内嵌该工具的 help 原文，请在本机执行：

```bash
hashcat-utils -h
```

## 4. 实践清单

按顺序做完这五步，就能把工具从「装上」推进到「会用」：

- [ ] **1.** **装好并确认版本** —— `sudo apt install hashcat-utils`，再执行 `hashcat-utils --version` 2>/dev/null || `hashcat-utils -V`
- [ ] **2.** **读官方帮助** —— `hashcat-utils -h`，需要细节时 `man hashcat-utils`
- [ ] **3.** **在自有靶场跑最小用例** —— 用 `hashcat-utils -h` 里最简单的那个子命令试一次
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/hashcat-utils/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- **精讲教程**（含原理、参数详解、靶场实操与输出解读）：[hashcat](../../tools/tutorials/04-口令攻击/hashcat.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/hashcat-utils/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/hashcat-utils/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
