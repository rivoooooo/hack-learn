# dfwinreg

> Digital Forensics Windows Registry library for Python 3 dfWinReg, or Digital Forensics Windows Registry, provides read-only access to Windows Registry objects. The goal of dfWinReg is to provide a generic interface for accessing Windows Re…

> **功能分类**：数字取证 ｜ **Kali 包**：`dfwinreg` ｜ **官方文档**：<https://www.kali.org/tools/dfwinreg/>

## 1. 安装

```bash
sudo apt update
sudo apt install python3-dfwinreg
```

| 项目 | 内容 |
|------|------|
| 版本 | 20260411 |
| 架构 | all |
| 可执行命令 | `python3-dfwinreg` |
| 依赖 | `libjs-jquery`、`libjs-sphinxdoc`、`python3`、`python3-dfdatetime`、`python3-dtfabric`、`python3-libregf`、`python3-yaml`、`sphinx-rtd-theme-common` |
| 安装体积 | 1.05 MB |
| 官网 | <https://github.com/log2timeline/dfwinreg> |
| 源码仓库 | <https://salsa.debian.org/pkg-security-team/dfwinreg> |
| 包追踪 | <https://pkg.kali.org/pkg/dfwinreg> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
python3-dfwinreg -h          # 查看用法
man python3-dfwinreg         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

> 官方页面未内嵌该工具的 help 原文，请在本机执行：

```bash
python3-dfwinreg -h
```

## 4. 实践清单

按顺序做完这五步，就能把工具从「装上」推进到「会用」：

- [ ] **1.** **装好并确认版本** —— `sudo apt install python3-dfwinreg`，再执行 `python3-dfwinreg --version` 2>/dev/null || `python3-dfwinreg -V`
- [ ] **2.** **读官方帮助** —— `python3-dfwinreg -h`，需要细节时 `man python3-dfwinreg`
- [ ] **3.** **在自有靶场跑最小用例** —— 用 `python3-dfwinreg -h` 里最简单的那个子命令试一次
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/dfwinreg/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/dfwinreg/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/dfwinreg/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
