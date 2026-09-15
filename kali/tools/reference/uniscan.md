# uniscan

> LFI, RFI, and RCE vulnerability scanner Uniscan is a simple Remote File Include, Local File Include and Remote Command Execution vulnerability scanner.

> **功能分类**：Web 应用 ｜ **Kali 包**：`uniscan` ｜ **官方文档**：<https://www.kali.org/tools/uniscan/>

## 1. 安装

```bash
sudo apt update
sudo apt install uniscan
```

| 项目 | 内容 |
|------|------|
| 版本 | 6.3 |
| 架构 | all |
| 可执行命令 | `uniscan`、`uniscan-gui` |
| 依赖 | `libmoose-perl`、`perl`、`perl-tk` |
| 安装体积 | 1.19 MB |
| 官网 | <https://sourceforge.net/projects/uniscan/> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/uniscan> |
| 包追踪 | <https://pkg.kali.org/pkg/uniscan> |

## 2. 官方用法示例

> 以下为 Kali 官方工具页给出的示例与输出原文。

```text
Usage Example
Scan the given URL (-u http://192.168.1.202/) for vulnerabilities, enabling directory and dynamic checks (-qd):
root@kali:~# uniscan -u http://192.168.1.202/ -qd
####################################
# Uniscan project                  #
# http://uniscan.sourceforge.net/  #
####################################
V. 6.2


Scan date: 16-5-2014 16:29:48
===================================================================================================
| Domain: http://192.168.1.202/
| Server: Apache/2.2.22 (Debian)
| IP: 192.168.1.202
===================================================================================================
|
| Directory check:
| [+] CODE: 200 URL: http://192.168.1.202/joomla/
| [+] CODE: 200 URL: http://192.168.1.202/wordpress/
===================================================================================================
|
| Crawler Started:
| Plugin name: FCKeditor upload test v.1 Loaded.
| Plugin name: Web Backdoor Disclosure v.1.1 Loaded.
| Plugin name: phpinfo() Disclosure v.1 Loaded.
| Plugin name: E-mail Detection v.1.1 Loaded.
| Plugin name: Timthumb <= 1.32 vulnerability v.1 Loaded.
| Plugin name: Code Disclosure v.1.1 Loaded.
| Plugin name: Upload Form Detect v.1.1 Loaded.
| Plugin name: External Host Detect v.1.2 Loaded.
| [+] Crawling finished, 27 URL's found!
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 2 个可执行命令，下面是官方页面内嵌的帮助原文。

### `uniscan`

官方给出的调用示例：`uniscan -u http://192.168.1.202/ -qd`

```text
root@kali:~# uniscan -u http://192.168.1.202/ -qd
####################################
# Uniscan project                  #
# http://uniscan.sourceforge.net/  #
####################################
V. 6.2
Scan date: 16-5-2014 16:29:48
===================================================================================================
| Domain: http://192.168.1.202/
| Server: Apache/2.2.22 (Debian)
| IP: 192.168.1.202
===================================================================================================
|
| Directory check:
| [+] CODE: 200 URL: http://192.168.1.202/joomla/
| [+] CODE: 200 URL: http://192.168.1.202/wordpress/
===================================================================================================
|
| Crawler Started:
| Plugin name: FCKeditor upload test v.1 Loaded.
| Plugin name: Web Backdoor Disclosure v.1.1 Loaded.
| Plugin name: phpinfo() Disclosure v.1 Loaded.
| Plugin name: E-mail Detection v.1.1 Loaded.
| Plugin name: Timthumb <= 1.32 vulnerability v.1 Loaded.
| Plugin name: Code Disclosure v.1.1 Loaded.
| Plugin name: Upload Form Detect v.1.1 Loaded.
| Plugin name: External Host Detect v.1.2 Loaded.
| [+] Crawling finished, 27 URL's found!
```

### `uniscan（示例）`

官方给出的调用示例：`uniscan -h`

```text
root@kali:~# uniscan -h
####################################
# Uniscan project                  #
# http://uniscan.sourceforge.net/  #
####################################
V. 6.3
OPTIONS:
	-h 	help
	-u 	<url> example: https://www.example.com/
	-f 	<file> list of url's
	-b 	Uniscan go to background
	-q 	Enable Directory checks
	-w 	Enable File checks
	-e 	Enable robots.txt and sitemap.xml check
	-d 	Enable Dynamic checks
	-s 	Enable Static checks
	-r 	Enable Stress checks
	-i 	<dork> Bing search
	-o 	<dork> Google search
	-g 	Web fingerprint
	-j 	Server fingerprint
usage:
[1] perl ./uniscan.pl -u http://www.example.com/ -qweds
[2] perl ./uniscan.pl -f sites.txt -bqweds
[3] perl ./uniscan.pl -i uniscan
[4] perl ./uniscan.pl -i "ip:xxx.xxx.xxx.xxx"
[5] perl ./uniscan.pl -o "inurl:test"
[6] perl ./uniscan.pl -u https://www.example.com/ -r
```

## 4. 实践清单

按顺序做完这五步，就能把工具从「装上」推进到「会用」：

- [ ] **1.** **装好并确认版本** —— `sudo apt install uniscan`，再执行 `uniscan --version` 2>/dev/null || `uniscan -V`
- [ ] **2.** **读官方帮助** —— `uniscan -h`，需要细节时 `man uniscan`
- [ ] **3.** **在自有靶场跑最小用例** —— 用 `uniscan -h` 里最简单的那个子命令试一次
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/uniscan/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/reconnaissance.md`](../../tools/by-attack/reconnaissance.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/uniscan/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/uniscan/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
