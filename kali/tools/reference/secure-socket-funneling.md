# secure-socket-funneling

> SSF - windows binaries This package provides simple and efficient ways to forward data from multiple sockets (TCP or UDP) through a single secure TLS link to a remote computer. This package provides the 32 bits and 64 bits windows binaries…

> **功能分类**：Windows 资源 ｜ **Kali 包**：`secure-socket-funneling` ｜ **官方文档**：<https://www.kali.org/tools/secure-socket-funneling/>

## 1. 安装

```bash
sudo apt update
sudo apt install secure-socket-funneling-windows-binaries
```

| 项目 | 内容 |
|------|------|
| 版本 | 3.0.0 |
| 架构 | all |
| 可执行命令 | `secure-socket-funneling-windows-binaries` |
| 安装体积 | 30.11 MB |
| 官网 | <https://github.com/securesocketfunneling/ssf> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/secure-socket-funneling> |
| 包追踪 | <https://pkg.kali.org/pkg/secure-socket-funneling> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
secure-socket-funneling-windows-binaries -h          # 查看用法
man secure-socket-funneling-windows-binaries         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

> 官方页面未内嵌该工具的 help 原文，请在本机执行：

```bash
secure-socket-funneling-windows-binaries -h
```

## 4. 实践清单

按顺序做完这五步，就能把工具从「装上」推进到「会用」：

- [ ] **1.** **装好并确认版本** —— `sudo apt install secure-socket-funneling-windows-binaries`，再执行 `secure-socket-funneling-windows-binaries --version` 2>/dev/null || `secure-socket-funneling-windows-binaries -V`
- [ ] **2.** **读官方帮助** —— `secure-socket-funneling-windows-binaries -h`，需要细节时 `man secure-socket-funneling-windows-binaries`
- [ ] **3.** **在自有靶场跑最小用例** —— 用 `secure-socket-funneling-windows-binaries -h` 里最简单的那个子命令试一次
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/secure-socket-funneling/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/secure-socket-funneling/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/secure-socket-funneling/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
