# rsmangler

> Wordlist mangling tool RSMangler will take a wordlist and perform various manipulations on it similar to those done by John the Ripper the main difference being that it will first take the input words and generate all permutations and the …

> **功能分类**：口令攻击 ｜ **Kali 包**：`rsmangler` ｜ **官方文档**：<https://www.kali.org/tools/rsmangler/>

## 1. 安装

```bash
sudo apt update
sudo apt install rsmangler
```

| 项目 | 内容 |
|------|------|
| 版本 | 1.5 |
| 架构 | all |
| 可执行命令 | `rsmangler` |
| 依赖 | `ruby` |
| 安装体积 | 24 KB |
| 官网 | <https://digi.ninja/projects/rsmangler.php> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/rsmangler> |
| 包追踪 | <https://pkg.kali.org/pkg/rsmangler> |

## 2. 官方用法示例

> 以下为 Kali 官方工具页给出的示例与输出原文。

```text
Usage Example
Use the original wordlist (cat words.txt |) and mangle words with a minimum length of 6 (-m 6) and maximum length of 8 (-x 8), using stdin as input (–file -) and redirecting the results to a new wordlist (> mangled.txt):
root@kali:~# cat words.txt | rsmangler -m 6 -x 8 --file - > mangled.txt
root@kali:~# wc -l mangled.txt
367 mangled.txt
root@kali:~# wc -l words.txt
3 words.txt
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `cat`

官方给出的调用示例：`cat words.txt | rsmangler -m 6 -x 8 --file - > mangled.txt`

```text
root@kali:~# cat words.txt | rsmangler -m 6 -x 8 --file - > mangled.txt
```

### `wc`

官方给出的调用示例：`wc -l mangled.txt`

```text
root@kali:~# wc -l mangled.txt
367 mangled.txt
```

### `wc（示例）`

官方给出的调用示例：`wc -l words.txt`

```text
root@kali:~# wc -l words.txt
3 words.txt
">
 mangled.txt):
```

### `cat（示例）`

官方给出的调用示例：`cat words.txt | rsmangler -m 6 -x 8 --file - > mangled.txt`

```text
root@kali:~# cat words.txt | rsmangler -m 6 -x 8 --file - > mangled.txt
```

### `wc（示例）`

官方给出的调用示例：`wc -l mangled.txt`

```text
root@kali:~# wc -l mangled.txt
367 mangled.txt
```

### `wc（示例）`

官方给出的调用示例：`wc -l words.txt`

```text
root@kali:~# wc -l words.txt
3 words.txt
">
 mangled.txt):
```

### `cat（示例）`

官方给出的调用示例：`cat words.txt | rsmangler -m 6 -x 8 --file - > mangled.txt`

```text
root@kali:~# cat words.txt | rsmangler -m 6 -x 8 --file - > mangled.txt
```

### `wc（示例）`

官方给出的调用示例：`wc -l mangled.txt`

```text
root@kali:~# wc -l mangled.txt
367 mangled.txt
```

### `wc（示例）`

官方给出的调用示例：`wc -l words.txt`

```text
root@kali:~# wc -l words.txt
3 words.txt
">
 mangled.txt):
```

### `cat（示例）`

官方给出的调用示例：`cat words.txt | rsmangler -m 6 -x 8 --file - > mangled.txt`

```text
root@kali:~# cat words.txt | rsmangler -m 6 -x 8 --file - > mangled.txt
```

## 4. 实践清单

按顺序做完这五步，就能把工具从「装上」推进到「会用」：

- [ ] **1.** **装好并确认版本** —— `sudo apt install rsmangler`，再执行 `rsmangler --version` 2>/dev/null || `rsmangler -V`
- [ ] **2.** **读官方帮助** —— `rsmangler -h`，需要细节时 `man rsmangler`
- [ ] **3.** **在自有靶场跑最小用例** —— 用 `rsmangler -h` 里最简单的那个子命令试一次
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/rsmangler/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/credential-access.md`](../../tools/by-attack/credential-access.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/rsmangler/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/rsmangler/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
