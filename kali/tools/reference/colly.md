# colly

> Elegant Scraper and Crawler Framework for Golang (program) This package contains a Colly Lightning Fast and Elegant Scraping Framework for Gophers. Colly provides a clean interface to write any kind of crawler/scraper/spider. With Colly yo…

> **功能分类**：通用工具 ｜ **Kali 包**：`colly` ｜ **官方文档**：<https://www.kali.org/tools/colly/>

## 1. 安装

```bash
sudo apt update
sudo apt install colly
```

| 项目 | 内容 |
|------|------|
| 版本 | 2.1.0 |
| 架构 | any |
| 可执行命令 | `colly`、`golang-github-gocolly-colly-dev` |
| 依赖 | `golang-github-antchfx-htmlquery-dev`、`golang-github-antchfx-xmlquery-dev`、`golang-github-gobwas-glob-dev`、`golang-github-jawher-mow.cli-dev`、`golang-github-kennygrant-sanitize-dev`、`golang-github-nlnwa-whatwg-url-dev`、`golang-github-puerkitobio-goquery-dev`、`golang-github-saintfish-chardet-dev`、`golang-github-temoto-robotstxt-dev`、`golang-golang-x-net-dev`、`golang-google-appengine-dev` |
| 安装体积 | 1.39 MB |
| 官网 | <https://github.com/gocolly/colly> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/colly> |
| 包追踪 | <https://pkg.kali.org/pkg/colly> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
colly -h          # 查看用法
man colly         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 2 个可执行命令，下面是官方页面内嵌的帮助原文。

### `colly`

官方给出的调用示例：`colly -h`

```text
root@kali:~# colly -h
Usage: colly COMMAND [arg...]
Scraping Framework for Gophers
Commands:
  new          Create new scraper
Run 'colly COMMAND --help' for more information on a command.
```

## 4. 实践清单

按顺序做完这五步，就能把工具从「装上」推进到「会用」：

- [ ] **1.** **装好并确认版本** —— `sudo apt install colly`，再执行 `colly --version` 2>/dev/null || `colly -V`
- [ ] **2.** **读官方帮助** —— `colly -h`，需要细节时 `man colly`
- [ ] **3.** **在自有靶场跑最小用例** —— 官方给出的调用形式是：`Usage: colly COMMAND [arg...]`
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/colly/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/colly/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/colly/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
