# wordlists

> Contains the rockyou wordlist This package contains the rockyou.txt wordlist and has an installation size of 134 MB.

> **功能分类**：信息搜集 ｜ **Kali 包**：`wordlists` ｜ **官方文档**：<https://www.kali.org/tools/wordlists/>

## 1. 安装

```bash
sudo apt update
sudo apt install wordlists
```

| 项目 | 内容 |
|------|------|
| 版本 | 2026.2.0 |
| 架构 | all |
| 可执行命令 | `wordlists` |
| 依赖 | `kali-defaults`、`sudo` |
| 安装体积 | 50.90 MB |
| 官网 | <https://www.kali.org> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/wordlists> |
| 包追踪 | <https://pkg.kali.org/pkg/wordlists> |

## 2. 官方用法示例

> 以下为 Kali 官方工具页给出的示例与输出原文。

```text
Usage Examples
root@kali:~# ls -lh /usr/share/wordlists/
total 51M
lrwxrwxrwx 1 root root  25 Jan  3 13:59 dirb -> /usr/share/dirb/wordlists
lrwxrwxrwx 1 root root  30 Jan  3 13:59 dirbuster -> /usr/share/dirbuster/wordlists
lrwxrwxrwx 1 root root  35 Jan  3 13:59 dnsmap.txt -> /usr/share/dnsmap/wordlist_TLAs.txt
lrwxrwxrwx 1 root root  41 Jan  3 13:59 fasttrack.txt -> /usr/share/set/src/fasttrack/wordlist.txt
lrwxrwxrwx 1 root root  45 Jan  3 13:59 fern-wifi -> /usr/share/fern-wifi-cracker/extras/wordlists
lrwxrwxrwx 1 root root  46 Jan  3 13:59 metasploit -> /usr/share/metasploit-framework/data/wordlists
lrwxrwxrwx 1 root root  41 Jan  3 13:59 nmap.lst -> /usr/share/nmap/nselib/data/passwords.lst
-rw-r--r-- 1 root root 51M Mar  3  2013 rockyou.txt.gz
lrwxrwxrwx 1 root root  34 Jan  3 13:59 sqlmap.txt -> /usr/share/sqlmap/txt/wordlist.txt
lrwxrwxrwx 1 root root  25 Jan  3 13:59 wfuzz -> /usr/share/wfuzz/wordlist
root@kali:~#
root@kali:~# gunzip /usr/share/wordlists/rockyou.txt.gz
root@kali:~#
root@kali:~# wc -l /usr/share/wordlists/rockyou.txt; ls -lah /usr/share/wordlists/rockyou.txt
14344392 /usr/share/wordlists/rockyou.txt
-rw-r--r-- 1 root root 134M Mar  3  2013 /usr/share/wordlists/rockyou.txt
root@kali:~#
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### ``

```text
root@kali:~#
```

### `gunzip`

官方给出的调用示例：`gunzip /usr/share/wordlists/rockyou.txt.gz`

```text
root@kali:~# gunzip /usr/share/wordlists/rockyou.txt.gz
```

### `（示例）`

```text
root@kali:~#
```

### `wc`

官方给出的调用示例：`wc -l /usr/share/wordlists/rockyou.txt; ls -lah /usr/share/wordlists/rockyou.txt`

```text
root@kali:~# wc -l /usr/share/wordlists/rockyou.txt; ls -lah /usr/share/wordlists/rockyou.txt
14344392 /usr/share/wordlists/rockyou.txt
-rw-r--r-- 1 root root 134M Mar  3  2013 /usr/share/wordlists/rockyou.txt
```

### `（示例）`

```text
root@kali:~#
">
 /usr/share/dirb/wordlists
lrwxrwxrwx 1 root root  30 Jan  3 13:59 dirbuster -> /usr/share/dirbuster/wordlists
lrwxrwxrwx 1 root root  35 Jan  3 13:59 dnsmap.txt -> /usr/share/dnsmap/wordlist_TLAs.txt
lrwxrwxrwx 1 root root  41 Jan  3 13:59 fasttrack.txt -> /usr/share/set/src/fasttrack/wordlist.txt
lrwxrwxrwx 1 root root  45 Jan  3 13:59 fern-wifi -> /usr/share/fern-wifi-cracker/extras/wordlists
lrwxrwxrwx 1 root root  46 Jan  3 13:59 metasploit -> /usr/share/metasploit-framework/data/wordlists
lrwxrwxrwx 1 root root  41 Jan  3 13:59 nmap.lst -> /usr/share/nmap/nselib/data/passwords.lst
-rw-r--r-- 1 root root 51M Mar  3  2013 rockyou.txt.gz
lrwxrwxrwx 1 root root  34 Jan  3 13:59 sqlmap.txt -> /usr/share/sqlmap/txt/wordlist.txt
lrwxrwxrwx 1 root root  25 Jan  3 13:59 wfuzz -> /usr/share/wfuzz/wordlist
```

### `（示例）`

```text
root@kali:~#
```

### `gunzip（示例）`

官方给出的调用示例：`gunzip /usr/share/wordlists/rockyou.txt.gz`

```text
root@kali:~# gunzip /usr/share/wordlists/rockyou.txt.gz
```

### `（示例）`

```text
root@kali:~#
```

### `wc（示例）`

官方给出的调用示例：`wc -l /usr/share/wordlists/rockyou.txt; ls -lah /usr/share/wordlists/rockyou.txt`

```text
root@kali:~# wc -l /usr/share/wordlists/rockyou.txt; ls -lah /usr/share/wordlists/rockyou.txt
14344392 /usr/share/wordlists/rockyou.txt
-rw-r--r-- 1 root root 134M Mar  3  2013 /usr/share/wordlists/rockyou.txt
```

### `（示例）`

```text
root@kali:~#
">
 /usr/share/dirb/wordlists
lrwxrwxrwx 1 root root  30 Jan  3 13:59 dirbuster -> /usr/share/dirbuster/wordlists
lrwxrwxrwx 1 root root  35 Jan  3 13:59 dnsmap.txt -> /usr/share/dnsmap/wordlist_TLAs.txt
lrwxrwxrwx 1 root root  41 Jan  3 13:59 fasttrack.txt -> /usr/share/set/src/fasttrack/wordlist.txt
lrwxrwxrwx 1 root root  45 Jan  3 13:59 fern-wifi -> /usr/share/fern-wifi-cracker/extras/wordlists
lrwxrwxrwx 1 root root  46 Jan  3 13:59 metasploit -> /usr/share/metasploit-framework/data/wordlists
lrwxrwxrwx 1 root root  41 Jan  3 13:59 nmap.lst -> /usr/share/nmap/nselib/data/passwords.lst
-rw-r--r-- 1 root root 51M Mar  3  2013 rockyou.txt.gz
lrwxrwxrwx 1 root root  34 Jan  3 13:59 sqlmap.txt -> /usr/share/sqlmap/txt/wordlist.txt
lrwxrwxrwx 1 root root  25 Jan  3 13:59 wfuzz -> /usr/share/wfuzz/wordlist
```

## 4. 实践清单

按顺序做完这五步，就能把工具从「装上」推进到「会用」：

- [ ] **1.** **装好并确认版本** —— `sudo apt install wordlists`，再执行 `wordlists --version` 2>/dev/null || `wordlists -V`
- [ ] **2.** **读官方帮助** —— `wordlists -h`，需要细节时 `man wordlists`
- [ ] **3.** **在自有靶场跑最小用例** —— 用 `wordlists -h` 里最简单的那个子命令试一次
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/wordlists/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- **精讲教程**（含原理、参数详解、靶场实操与输出解读）：[wordlists](../../tools/tutorials/04-口令攻击/wordlists.md)
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/credential-access.md`](../../tools/by-attack/credential-access.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/wordlists/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/wordlists/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
