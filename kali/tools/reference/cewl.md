# cewl

> Custom word list generator CeWL (Custom Word List generator) is a ruby app which spiders a given URL, up to a specified depth, and returns a list of words which can then be used for password crackers such as John the Ripper. Optionally, Ce…

> **功能分类**：口令攻击 ｜ **Kali 包**：`cewl` ｜ **官方文档**：<https://www.kali.org/tools/cewl/>

## 1. 安装

```bash
sudo apt update
sudo apt install cewl
```

| 项目 | 内容 |
|------|------|
| 版本 | 6.2.1 |
| 架构 | all |
| 可执行命令 | `cewl`、`fab-cewl` |
| 依赖 | `ruby`、`ruby-mime`、`ruby-mime-types`、`ruby-mini-exiftool`、`ruby-net-http-digest-auth`、`ruby-nokogiri`、`ruby-spider`、`ruby-zip` |
| 安装体积 | 81 KB |
| 官网 | <https://github.com/digininja/CeWL> |
| 源码仓库 | <https://salsa.debian.org/pkg-security-team/cewl> |
| 包追踪 | <https://pkg.kali.org/pkg/cewl> |

## 2. 官方用法示例

> 以下为 Kali 官方工具页给出的示例与输出原文。

```text
Usage Example
Scan to a depth of 2 (-d 2) and use a minimum word length of 5 (-m 5), save the words to a file (-w docswords.txt), targeting the given URL (https://example.com):
root@kali:~# cewl -d 2 -m 5 -w docswords.txt https://example.com
CeWL 5.4.3 (Arkanoid) Robin Wood (robin@digi.ninja) (https://digi.ninja/)
root@kali:~# wc -l docswords.txt
13 docswords.txt
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 2 个可执行命令，下面是官方页面内嵌的帮助原文。

### `cewl`

> 官方示例调用：`cewl -d 2 -m 5 -w docswords.txt https://example.com`

```text
root@kali:~# cewl -d 2 -m 5 -w docswords.txt https://example.com
CeWL 5.4.3 (Arkanoid) Robin Wood (
[email protected]
) (https://digi.ninja/)
```

### `wc`

> 官方示例调用：`wc -l docswords.txt`

```text
root@kali:~# wc -l docswords.txt
13 docswords.txt
```

### `cewl -h`

> 官方示例调用：`cewl -h`

```text
root@kali:~# cewl -h
CeWL 6.2.1 (More Fixes) Robin Wood (
[email protected]
) (https://digi.ninja/)
Usage: cewl [OPTIONS] ... <url>
    OPTIONS:
	-h, --help: Show help.
	-k, --keep: Keep the downloaded file.
	-d <x>,--depth <x>: Depth to spider to, default 2.
	-m, --min_word_length: Minimum word length, default 3.
	-x, --max_word_length: Maximum word length, default unset.
	-o, --offsite: Let the spider visit other sites.
	--exclude: A file containing a list of paths to exclude
	--allowed: A regex pattern that path must match to be followed
	-w, --write: Write the output to the file.
	-u, --ua <agent>: User agent to send.
	-n, --no-words: Don't output the wordlist.
	-g <x>, --groups <x>: Return groups of words as well
	--lowercase: Lowercase all parsed words
	--with-numbers: Accept words with numbers in as well as just letters
	--convert-umlauts: Convert common ISO-8859-1 (Latin-1) umlauts (ä-ae, ö-oe, ü-ue, ß-ss)
	-a, --meta: include meta data.
	--meta_file file: Output file for meta data.
	-e, --email: Include email addresses.
	--email_file <file>: Output file for email addresses.
	--meta-temp-dir <dir>: The temporary directory used by exiftool when parsing files, default /tmp.
	-c, --count: Show the count for each word found.
	-v, --verbose: Verbose.
	--debug: Extra debug information.
	Authentication
	--auth_type: Digest or basic.
	--auth_user: Authentication username.
	--auth_pass: Authentication password.
	Proxy Support
	--proxy_host: Proxy host.
	--proxy_port: Proxy port, default 8080.
	--proxy_username: Username for proxy, if required.
	--proxy_password: Password for proxy, if required.
	Headers
	--header, -H: In format name:value - can pass multiple.
    <url>: The site to spider.
```

### `fab-cewl`

> 官方示例调用：`fab-cewl -h`

```text
root@kali:~# fab-cewl -h
```

## 4. 实践清单

按顺序做完这五步，就能把工具从「装上」推进到「会用」：

- [ ] **1.** **装好并确认版本** —— `sudo apt install cewl`，再执行 `cewl --version` 2>/dev/null || `cewl -V`
- [ ] **2.** **读官方帮助** —— `cewl -h`，需要细节时 `man cewl`
- [ ] **3.** **在自有靶场跑最小用例** —— 官方给出的调用形式是：`Usage: cewl [OPTIONS] ... <url>`
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/cewl/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- **精讲教程**（含原理、参数详解、靶场实操与输出解读）：[cewl](../../tools/tutorials/04-口令攻击/cewl.md)
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/credential-access.md`](../../tools/by-attack/credential-access.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/cewl/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/cewl/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
