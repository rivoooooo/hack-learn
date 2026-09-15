# witnessme

> Web Inventory tool This package contains a Web Inventory tool inspired by Eyewitness, its also written to be extensible allowing you to create custom functionality that can take advantage of the headless browser it drives in the back-end.

> **功能分类**：识别与指纹 ｜ **Kali 包**：`witnessme` ｜ **官方文档**：<https://www.kali.org/tools/witnessme/>

## 1. 安装

```bash
sudo apt update
sudo apt install witnessme
```

| 项目 | 内容 |
|------|------|
| 版本 | 1.5.0 |
| 架构 | all |
| 可执行命令 | `witnessme`、`wmapi`、`wmdb` |
| 依赖 | `python3`、`python3-aiodns`、`python3-aiosqlite`、`python3-fastapi`、`python3-jinja2`、`python3-lxml`、`python3-prompt-toolkit`、`python3-pydantic`、`python3-pyppeteer`、`python3-python-multipart`、`python3-terminaltables3`、`python3-uvicorn` 等 |
| 安装体积 | 402 KB |
| 官网 | <https://github.com/byt3bl33d3r/WitnessMe> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/witnessme> |
| 包追踪 | <https://pkg.kali.org/pkg/witnessme> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
witnessme -h          # 查看用法
man witnessme         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 3 个可执行命令，下面是官方页面内嵌的帮助原文。

### `witnessme`

官方给出的调用示例：`witnessme -h`

```text
root@kali:~# witnessme -h
usage: witnessme [-h] [--threads THREADS] [--timeout TIMEOUT] [-d] [-v]
                 {screenshot,grab} ...
WitnessMe!
positional arguments:
  {screenshot,grab}
options:
  -h, --help         show this help message and exit
  --threads THREADS  Number of concurrent browser tab(s) to open
                     [WARNING: This can cause huge RAM consumption if set to high values] (default: 15)
  --timeout TIMEOUT  Timeout for each connection attempt in seconds (default: 15)
  -d, --debug        Enable debug output (default: False)
  -v, --version      show program's version number and exit
```

### `wmapi`

官方给出的调用示例：`wmapi -h`

```text
root@kali:~# wmapi -h
usage: wmapi [-h] [host] [port]
positional arguments:
  host        IP to bind to (default: 127.0.0.1)
  port        port to bind to (default: 8000)
options:
  -h, --help  show this help message and exit
```

## 4. 实践清单

按顺序做完这五步，就能把工具从「装上」推进到「会用」：

- [ ] **1.** **装好并确认版本** —— `sudo apt install witnessme`，再执行 `witnessme --version` 2>/dev/null || `witnessme -V`
- [ ] **2.** **读官方帮助** —— `witnessme -h`，需要细节时 `man witnessme`
- [ ] **3.** **在自有靶场跑最小用例** —— 用 `witnessme -h` 里最简单的那个子命令试一次
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/witnessme/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/services-and-other-tools.md`](../../tools/by-attack/services-and-other-tools.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/witnessme/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/witnessme/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
