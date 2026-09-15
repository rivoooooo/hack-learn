# zsh-autosuggestions

> Fish-like fast/unobtrusive autosuggestions for zsh As you type commands, you will see a completion offered after the cursor in a muted gray color. If you press the right-arrow key or End with the cursor at the end of the buffer, it will ac…

> **功能分类**：通用工具 ｜ **Kali 包**：`zsh-autosuggestions` ｜ **官方文档**：<https://www.kali.org/tools/zsh-autosuggestions/>

## 1. 安装

```bash
sudo apt update
sudo apt install zsh-autosuggestions
```

| 项目 | 内容 |
|------|------|
| 版本 | 0.7.1 |
| 架构 | all |
| 可执行命令 | `zsh-autosuggestions` |
| 依赖 | `zsh` |
| 安装体积 | 46 KB |
| 官网 | <https://github.com/zsh-users/zsh-autosuggestions> |
| 源码仓库 | <https://salsa.debian.org/debian/zsh-autosuggestions> |
| 包追踪 | <https://pkg.kali.org/pkg/zsh-autosuggestions> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
zsh-autosuggestions -h          # 查看用法
man zsh-autosuggestions         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

> 官方页面未内嵌该工具的 help 原文，请在本机执行：

```bash
zsh-autosuggestions -h
```

## 4. 实践清单

按顺序做完这五步，就能把工具从「装上」推进到「会用」：

- [ ] **1.** **装好并确认版本** —— `sudo apt install zsh-autosuggestions`，再执行 `zsh-autosuggestions --version` 2>/dev/null || `zsh-autosuggestions -V`
- [ ] **2.** **读官方帮助** —— `zsh-autosuggestions -h`，需要细节时 `man zsh-autosuggestions`
- [ ] **3.** **在自有靶场跑最小用例** —— 用 `zsh-autosuggestions -h` 里最简单的那个子命令试一次
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/zsh-autosuggestions/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/zsh-autosuggestions/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/zsh-autosuggestions/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
