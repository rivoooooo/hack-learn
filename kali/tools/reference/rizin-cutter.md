# rizin-cutter

> Reverse engineering platform powered by rizin Cutter is a free and open-source reverse engineering platform powered by rizin. It aims at being an advanced and customizable reverse engineering platform while keeping the user experience in m…

> **功能分类**：数字取证 ｜ **Kali 包**：`rizin-cutter` ｜ **官方文档**：<https://www.kali.org/tools/rizin-cutter/>

## 1. 安装

```bash
sudo apt update
sudo apt install rizin-cutter
```

| 项目 | 内容 |
|------|------|
| 版本 | 2.5.0 |
| 架构 | any |
| 可执行命令 | `librizin-cutter-dev`、`rizin-cutter`、`cutter` |
| 依赖 | `libc6`、`libcgraph8`、`libgcc-s1`、`libgvc7`、`libkf6syntaxhighlighting6`、`libpyside6-py3-6.10`、`libpython3.14`、`libqt6core5compat6`、`libqt6core6t64`、`libqt6gui6`、`libqt6network6`、`libqt6opengl6` 等 |
| 安装体积 | 10.61 MB |
| 官网 | <https://cutter.re> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/rizin-cutter> |
| 包追踪 | <https://pkg.kali.org/pkg/rizin-cutter> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
librizin-cutter-dev -h          # 查看用法
man librizin-cutter-dev         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

> 官方页面未内嵌该工具的 help 原文，请在本机执行：

```bash
librizin-cutter-dev -h
rizin-cutter -h
cutter -h
```

## 4. 实践清单

按顺序做完这五步，就能把工具从「装上」推进到「会用」：

- [ ] **1.** **装好并确认版本** —— `sudo apt install rizin-cutter`，再执行 `librizin-cutter-dev --version` 2>/dev/null || `librizin-cutter-dev -V`
- [ ] **2.** **读官方帮助** —— `librizin-cutter-dev -h`，需要细节时 `man librizin-cutter-dev`
- [ ] **3.** **在自有靶场跑最小用例** —— 用 `librizin-cutter-dev -h` 里最简单的那个子命令试一次
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/rizin-cutter/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- **精讲教程**（含原理、参数详解、靶场实操与输出解读）：[rizin](../../tools/tutorials/10-逆向工程/rizin.md)
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/resource-development.md`](../../tools/by-attack/resource-development.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/rizin-cutter/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/rizin-cutter/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
