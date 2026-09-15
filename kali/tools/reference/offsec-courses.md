# offsec-courses

> Resources for OffSec’s AWAE/WEB-300 This is Kali Linux, the most advanced penetration testing and security auditing distribution. This metapackage depends on the resources required for OffSec’s AWAE/WEB-300/OSWE.

> **功能分类**：通用工具 ｜ **Kali 包**：`offsec-courses` ｜ **官方文档**：<https://www.kali.org/tools/offsec-courses/>

## 1. 安装

```bash
sudo apt update
sudo apt install offsec-awae
```

| 项目 | 内容 |
|------|------|
| 版本 | 2026.3.0 |
| 架构 | any |
| 可执行命令 | `offsec-awae`、`offsec-awae-python2`、`offsec-exp100`、`offsec-exp301`、`offsec-pen300`、`offsec-pwk` |
| 依赖 | `burpsuite` |
| 安装体积 | 34 KB |
| 官网 | <https://www.kali.org> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/offsec-courses> |
| 包追踪 | <https://pkg.kali.org/pkg/offsec-courses> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
offsec-awae -h          # 查看用法
man offsec-awae         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

> 官方页面未内嵌该工具的 help 原文，请在本机执行：

```bash
offsec-awae -h
offsec-awae-python2 -h
offsec-exp100 -h
offsec-exp301 -h
offsec-pen300 -h
offsec-pwk -h
```

## 4. 实践清单

按顺序做完这五步，就能把工具从「装上」推进到「会用」：

- [ ] **1.** **装好并确认版本** —— `sudo apt install offsec-awae`，再执行 `offsec-awae --version` 2>/dev/null || `offsec-awae -V`
- [ ] **2.** **读官方帮助** —— `offsec-awae -h`，需要细节时 `man offsec-awae`
- [ ] **3.** **在自有靶场跑最小用例** —— 用 `offsec-awae -h` 里最简单的那个子命令试一次
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/offsec-courses/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/offsec-courses/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/offsec-courses/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
