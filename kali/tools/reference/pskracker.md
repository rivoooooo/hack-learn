# pskracker

> Collection of WPA/WPA2/WPS default keys generators/pingens This package contains a collection of WPA/WPA2/WPS default algorithms/password generators/pingens written in C. This is useful for testing/auditing wireless networks and contains b…

> **功能分类**：通用工具 ｜ **Kali 包**：`pskracker` ｜ **官方文档**：<https://www.kali.org/tools/pskracker/>

## 1. 安装

```bash
sudo apt update
sudo apt install pskracker
```

| 项目 | 内容 |
|------|------|
| 版本 | 0.3.1 |
| 架构 | amd64 |
| 可执行命令 | `pskracker`、`pskracker-data` |
| 依赖 | `libc6`、`pskracker-data` |
| 安装体积 | 37 KB |
| 官网 | <https://github.com/soxrok2212/PSKracker> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/pskracker> |
| 包追踪 | <https://pkg.kali.org/pkg/pskracker> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
pskracker -h          # 查看用法
man pskracker         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 2 个可执行命令，下面是官方页面内嵌的帮助原文。

### `pskracker`

> 官方示例调用：`pskracker -h`

```text
root@kali:~# pskracker -h
 PSKracker 0.2.1 WiFi Security Auditing Toolkit
 Copyright (c) 2017-2019, soxrok2212 <
[email protected]
>
 Usage: pskracker <arguments>
 Required Arguments:
	-t, --target	: Target model number
 Optional Arguments:
	-b, --bssid	: BSSID of target
	-W, --wps	: Output possible WPS pin(s) only
	-G, --guest	: Output possible guest WPA key(s) only
	-s, --serial	: Serial number
	-f, --force	: Force full output
	-h, --help	: Display help/usage
 Example:
 pskracker -t <target model> -b <bssid> -s <serial number>
```

## 4. 实践清单

按顺序做完这五步，就能把工具从「装上」推进到「会用」：

- [ ] **1.** **装好并确认版本** —— `sudo apt install pskracker`，再执行 `pskracker --version` 2>/dev/null || `pskracker -V`
- [ ] **2.** **读官方帮助** —— `pskracker -h`，需要细节时 `man pskracker`
- [ ] **3.** **在自有靶场跑最小用例** —— 官方给出的调用形式是：`Usage: pskracker <arguments>`
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/pskracker/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/pskracker/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/pskracker/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
