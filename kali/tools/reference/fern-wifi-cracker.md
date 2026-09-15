# fern-wifi-cracker

> Automated Wi-Fi cracker This package contains a Wireless security auditing and attack software program written using the Python Programming Language and the Python Qt GUI library, the program is able to crack and recover WEP/WPA/WPS keys a…

> **功能分类**：无线攻击 ｜ **Kali 包**：`fern-wifi-cracker` ｜ **官方文档**：<https://www.kali.org/tools/fern-wifi-cracker/>

## 1. 安装

```bash
sudo apt update
sudo apt install fern-wifi-cracker
```

| 项目 | 内容 |
|------|------|
| 版本 | 3.6 |
| 架构 | all |
| 可执行命令 | `fern-wifi-cracker` |
| 依赖 | `aircrack-ng`、`macchanger`、`python3`、`python3-pyqt5`、`python3-scapy`、`reaver`、`subversion` |
| 安装体积 | 1.13 MB |
| 官网 | <https://github.com/savio-code/fern-wifi-cracker> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/fern-wifi-cracker> |
| 包追踪 | <https://pkg.kali.org/pkg/fern-wifi-cracker> |

## 2. 官方用法示例

> 以下为 Kali 官方工具页给出的示例与输出原文。

```text
Screenshots
fern-wifi-cracker
```

## 3. 命令与参数（官方 help / man 原文）

> 官方页面未内嵌该工具的 help 原文，请在本机执行：

```bash
fern-wifi-cracker -h
```

## 4. 实践清单

按顺序做完这五步，就能把工具从「装上」推进到「会用」：

- [ ] **1.** **装好并确认版本** —— `sudo apt install fern-wifi-cracker`，再执行 `fern-wifi-cracker --version` 2>/dev/null || `fern-wifi-cracker -V`
- [ ] **2.** **读官方帮助** —— `fern-wifi-cracker -h`，需要细节时 `man fern-wifi-cracker`
- [ ] **3.** **在自有靶场跑最小用例** —— 用 `fern-wifi-cracker -h` 里最简单的那个子命令试一次
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/fern-wifi-cracker/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/credential-access.md`](../../tools/by-attack/credential-access.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/fern-wifi-cracker/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/fern-wifi-cracker/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
