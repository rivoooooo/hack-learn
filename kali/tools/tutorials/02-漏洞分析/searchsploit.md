# searchsploit（本地 Exploit-DB 检索）

> **一句话**：在本地离线的漏洞利用库（Exploit-DB，2 万+ 条）里按关键词搜索，把"服务版本"变成"可用的 EXP"。
> **分类**：漏洞分析 ｜ **Kali 包**：`exploitdb`（命令名 `searchsploit`） ｜ **官方文档**：<https://www.exploit-db.com/searchsploit>

## 1. 它解决什么问题

[nmap](../01-信息搜集/nmap.md) 给你 `vsftpd 2.3.4`、[whatweb](../01-信息搜集/whatweb.md) 给你 `phpMyAdmin 2.11.1`——但这些字符串本身没有意义。**真正的问题是：这个版本有没有公开的利用代码？**

searchsploit 就是这座桥：把本地 Exploit-DB 归档（`sudo apt install exploitdb` 装好，约 191 MB）按关键词模糊匹配，输出对应的 EXP 路径。

| 工具 | 数据来源 | 优势 |
|------|---------|------|
| **searchsploit** | 本地 Exploit-DB 归档（离线） | 极快、离线、支持 `--nmap` 自动匹配 |
| [nuclei](nuclei.md) | 在线模板库 | 直接**验证**漏洞是否存在 |
| `exploitdb` 网站 | 在线 | 内容更新，有讨论与验证状态 |
| Metasploit `search` | MSF 模块库 | 可直接 `use` 并配置 |
| `getsploit` | 多源在线 | 能直接下载 EXP |

**核心认知**：searchsploit 查的是"**存在公开 EXP**"，**不等于目标一定存在该漏洞**。EXP 需要人工阅读、适配（改 IP、改偏移、改路径），成功率参差不齐——`(PoC)`、`/dos/` 这些标注能帮你过滤掉大量没用的条目。

## 2. 工作原理

```text
   searchsploit apache 2.4.49
        │
   ┌────┴────────────────────────────────────────────────────┐
   │ ① 读取本地索引文件                                        │
   │    /usr/share/exploitdb/files_exploits.csv                 │
   │    /usr/share/exploitdb/files_shellcodes.csv               │
   │    每条记录含：EDB-ID、文件路径、描述、日期、作者、平台      │
   └────┬────────────────────────────────────────────────────┘
        │
   ┌────┴────────────────────────────────────────────────────┐
   │ ② 对每一行做匹配（默认规则）                               │
   │    - 大小写不敏感（-c 改为敏感）                           │
   │    - 多个词是 AND 关系，顺序无关                            │
   │    - 默认匹配「标题 + 文件路径」（-t 只看标题）             │
   │    - 支持"版本区间模糊匹配"：搜 3.2 会命中 "3.0 < 3.5"      │
   │      （-s 关闭这个行为，要求精确存在）                      │
   │    - 默认排除部分低价值条目（可用 -v 显示更多）             │
   └────┬────────────────────────────────────────────────────┘
        │
   ┌────┴────────────────────────────────────────────────────┐
   │ ③ 输出                                                        │
   │    默认：两栏 —— Exploit Title | Path                        │
   │    -w   ：显示 exploit-db.com 的 URL 而非本地路径             │
   │    --id ：显示 EDB-ID                                        │
   │    -j   ：JSON（配 jq 做流水线）                              │
   │    -p   ：显示完整路径（并尝试复制到剪贴板）                    │
   │    -x   ：用 $PAGER 打开 EXP 原文                             │
   │    -m   ：把 EXP 复制到当前目录                                │
   └────┬────────────────────────────────────────────────────┘
        │
   --nmap scan.xml  →  自动解析 nmap XML，对每个服务版本逐个搜索
```

关键机制：

- **模糊版本匹配**：EXP 描述里常写成 `1.0 < 1.3`（表示受影响区间）。搜索 `1.1` 会命中它。这个行为很贴心，但也带来误报——`-s` 可以关掉。
- **`-t`（只看标题）是最重要的减噪参数**：不加 `-t` 时会连同**文件路径**一起匹配，导致搜数字（版本号）时命中一堆无关内容（比如某条 EXP 恰好在 `3.2/` 这样的目录里）。
- **`--nmap` 是自动化关键**：直接吃 `nmap -sV -oX` 的输出，逐个服务去查 EXP。这是"从扫描到利用"最短的自动化路径。
- **`/dos/` 和 `(PoC)` 是警示标记**：`/dos/` 目录里的通常是拒绝服务 PoC（可能把目标打挂），`(PoC)` 表示只是概念验证、不一定能直接利用。

## 3. 安装与快速上手

```bash
sudo apt install exploitdb
searchsploit -h
searchsploit --version 2>/dev/null; ls /usr/share/exploitdb | head
```

最小可用命令：

```bash
# 1) 搜产品名
searchsploit apache 2.4

# 2) 只看标题（推荐，减少假阳性）
searchsploit -t oracle windows

# 3) 用 EDB-ID 查看 EXP 内容
searchsploit -x 39446
```

## 4. 核心参数详解

### 搜索词相关

| 参数 | 作用 | 使用建议 |
|------|------|----------|
| `term1 term2 ...` | 任意多个搜索词，默认 AND、顺序无关、大小写不敏感 | 一般用 `产品名 + 版本` |
| `-c, --case` | 大小写**敏感**搜索 | 产品名有大小写含义时（如 `SQLite`） |
| `-e, --exact` | 标题**精确且顺序**匹配（隐含 `-t`） | 已经知道完整 EXP 标题时 |
| `-s, --strict` | 严格搜索：输入值必须真实存在，**关闭版本区间模糊匹配** | 想排除 `1.0 < 1.3` 这类宽泛命中时 |
| `-t, --title` | **只搜标题**（默认是标题 + 文件路径） | **强烈建议默认加上** |
| `--exclude="a\|b\|c"` | 从结果里剔除匹配这些值的条目，用 `\|` 串联 | 如 `--exclude="(PoC)\|/dos/"` |
| `--cve <CVE>` | 按 CVE 编号搜索 | **手上有 CVE 号时最直接的用法** |

### 输出控制

| 参数 | 作用 | 使用建议 |
|------|------|----------|
| `-j, --json` | JSON 输出 | 与 `jq` 组合做流水线 |
| `-o, --overflow` | 允许标题溢出列宽（完整显示） | 标题被截断时用 |
| `-p, --path <EDB-ID>` | 显示 EXP 的完整本地路径（并尝试复制到剪贴板） | 准备 `cat`/`cp` 时用 |
| `-v, --verbose` | 显示更多信息（含默认被过滤的条目） | 结果太少时用；`--nmap` 时也生效 |
| `-w, --www` | 显示 exploit-db.com 的 URL 而非本地路径 | 需要看在线版本/讨论时 |
| `--id` | 显示 EDB-ID 而非本地路径 | 想分享"编号"时 |
| `--disable-colour` | 关闭结果中的颜色高亮 | 重定向到文件时 |

### 非搜索动作

| 参数 | 作用 | 使用建议 |
|------|------|----------|
| `-m, --mirror <EDB-ID>` | **把 EXP 复制到当前目录** | 准备本地修改/编译时用 |
| `-x, --examine <EDB-ID>` | 用 `$PAGER` 打开 EXP 原文 | 快速阅读 |
| `-u, --update` | 检查并安装 exploitdb 包更新（deb / brew / git） | 定期更新（Kali 也可用 `apt update && apt install --only-upgrade exploitdb`） |
| `-h, --help` | 显示帮助 | — |

### 自动化

| 参数 | 作用 | 使用建议 |
|------|------|----------|
| `--nmap <file.xml>` | 用 nmap 的 XML 输出（含 `-sV` 版本）自动逐个匹配 | **批量从扫描到 EXP 的核心参数** |
| `--nmap <file.xml> -v` | 尝试更多关键词组合 | 漏检时用 |

## 5. 实战演练

**环境**：本地实验环境，`searchsploit` 本身**不接触目标**，只是查本地数据库，所以没有授权风险（但把 EXP 用在目标上必须有授权）。

- 靶机：Metasploitable2（`192.168.56.101`）
- 攻击机：Kali（`192.168.56.10`）

### 场景 1：从 nmap 指纹到 EXP 清单

```bash
# 第一步：拿到带版本的服务识别结果
sudo nmap -sV -oX /tmp/scan.xml 192.168.56.101

# 第二步：用 XML 自动逐个服务查 EXP
searchsploit --nmap /tmp/scan.xml
```

预期输出片段：

```text
[i] SearchSploit - Exploit Database Archive Search
[i] Reading: /tmp/scan.xml
[i] Target: 192.168.56.101

[i] Service: ftp vsftpd 2.3.4
  Exploit Title                                                        |  Path
  -------------------------------------------------------------------- |  -----
  vsftpd 2.3.4 - Backdoor Command Execution                            | unix/remote/17491.rb

[i] Service: ssh OpenSSH 4.7p1
  Exploit Title                                                        |  Path
  -------------------------------------------------------------------- |  -----
  OpenSSH 2.3 < 7.7 - Username Enumeration                             | linux/remote/45233.py

[i] Service: http Apache httpd 2.2.8
  Exploit Title                                                        |  Path
  -------------------------------------------------------------------- |  -----
  Apache 2.2.x - Multiple Vulnerabilities                              | multiple/remote/...
```

解读：这一步把"扫描结果"直接翻译成"候选 EXP 列表"。`vsftpd 2.3.4 - Backdoor Command Execution` 对应 Metasploit 的 `exploit/unix/ftp/vsftpd_234_backdoor`。

### 场景 2：精细搜索与减噪

```bash
# 只看标题，并排除只是 PoC 和 DoS 的条目
searchsploit -t linux kernel 3.2 --exclude="(PoC)|/dos/"

# 严格模式：不要"版本区间"这种宽泛匹配
searchsploit -t -s "openssh 7.7"

# 有 CVE 号时直接查（最精确）
searchsploit --cve 2021-44228

# JSON 输出 + jq 整理
searchsploit -t --json "apache 2.4.49" | jq -r '.RESULTS_EXPLOIT[] | [.EDB_ID, .Title, .Path] | @tsv'
```

预期输出片段（JSON 整理后）：

```text
50383	Apache HTTP Server 2.4.49 - Path Traversal and Remote Code Execution	webapps/50383.sh
```

解读：
- `--exclude="(PoC)|/dos/"` 是实战必备——它过滤掉"只证明概念"和"只能把目标打挂"的条目，让你专注在可利用的 EXP 上。
- `--cve` 是最精确的入口。有了 CVE 号就不需要猜关键词了。
- JSON + `jq` 让 searchsploit 可以嵌入自动化流程。

### 场景 3：查看、复制与本地化 EXP

```bash
# 用 EDB-ID 直接查看
searchsploit -x 50383

# 看完整本地路径
searchsploit -p 50383

# 把 EXP 复制到当前工作目录（准备修改/编译）
mkdir -p ~/exploits/cve-2021-41773 && cd ~/exploits/cve-2021-41773
searchsploit -m 50383
ls -l
head -30 50383.sh
```

预期输出片段：

```text
  Exploit: Apache HTTP Server 2.4.49 - Path Traversal and Remote Code Execution
      URL: https://www.exploit-db.com/exploits/50383
     Path: /usr/share/exploitdb/exploits/webapps/50383.sh
File Type: Bash script, ASCII text executable

Copied to: /root/exploits/cve-2021-41773/50383.sh
```

解读：`-m`（mirror）是标准工作流——**永远复制到自己的工作目录再改，不要直接改系统的 EXPLOITDB 目录**（`apt upgrade` 会覆盖掉你的修改）。复制后 `head` 看用法、看要不要改参数。

### 场景 4（进阶）：用在线链接核对 + 定期更新数据库

```bash
# 输出 exploit-db.com 的 URL（去看是否有验证状态、评论区反馈）
searchsploit -w -t "vsftpd 2.3.4"

# 输出 EDB-ID（方便在报告里引用编号）
searchsploit --id -t "vsftpd 2.3.4"

# 更新本地数据库
sudo searchsploit -u
# 或走 Kali 包管理
sudo apt update && sudo apt install --only-upgrade exploitdb
```

解读：
- `-w` 给出在线链接，**去 exploit-db.com 看那条 EXP 的"Verified"标记与评论**——这能帮你判断"这条 EXP 到底靠不靠谱"。
- `--id` 在报告里引用编号比引用文件路径更清晰。
- Exploit-DB 更新很频繁，**定期 `-u`**；新出的 CVE 往往先有 [nuclei](nuclei.md) 模板验证，再有 EXP。

### 场景 5：把 searchsploit 嵌进自动化流程

```bash
#!/bin/bash
# 从 nmap XML 提取服务，逐个查 EXP 并汇总成表
sudo nmap -sV -oX /tmp/scan.xml 192.168.56.101
searchsploit --nmap /tmp/scan.xml -v -j > /tmp/sploits.json

jq -r '.RESULTS_EXPLOIT[] | [.EDB_ID, .Title, .Path] | @tsv' /tmp/sploits.json \
  | sort -u > /tmp/exploits.tsv
column -t -s $'\t' /tmp/exploits.tsv
```

解读：`--nmap ... -j` 组合把"扫描 → 匹配 → 结构化输出"串成一条线。配合 `jq` 就能直接生成待验证的 EXP 清单，然后**逐条手工验证**——searchsploit 只负责生成候选列表，验证是人的工作。

## 6. 输出解读

### 默认两栏输出

```text
 Exploit Title                                     |  Path
 ------------------------------------------------- |  ----
 vsftpd 2.3.4 - Backdoor Command Execution         | unix/remote/17491.rb
```

| 部分 | 含义 | 用途 |
|------|------|------|
| Exploit Title | EXP 描述，通常含产品 + 版本 + 漏洞类型 | 判断是否匹配 |
| Path | 本地相对路径（在 `/usr/share/exploitdb/exploits/` 下） | 定位文件 |

`Path` 的目录结构本身就携带信息：

| 路径片段 | 含义 |
|---------|------|
| `unix/remote/` | Unix 远程利用 |
| `unix/local/` | Unix 本地提权 |
| `windows/remote/` | Windows 远程利用 |
| `windows/local/` | Windows 本地提权 |
| `webapps/` | Web 应用类的 EXP（多为脚本） |
| `multiple/` | 跨平台 |
| `dos/` | **拒绝服务 PoC** |
| `hardware/`、`local/` | 硬件/本地 |
| 文件名后缀 `.rb` | Metasploit 模块（可直接被 MSF 使用） |
| `.py`、`.sh`、`.pl`、`.c` | 需要自己跑/编译的 PoC |

### 标题里的警示标记

| 标记 | 含义 | 处理 |
|------|------|------|
| `(PoC)` | 概念验证，不一定能实际利用 | 需人工评估 |
| `(DoS)` 或路径含 `/dos/` | 拒绝服务，可能打挂目标 | **生产环境慎用** |
| `(Metasploit)` / `.rb` | 有对应的 MSF 模块 | 优先用 MSF（更省事） |
| `(未验证)` / 无标记 | 未经验证或状态未知 | 去 exploit-db.com 查 Verified 状态 |

### JSON 字段（`-j`）

| 字段 | 含义 |
|------|------|
| `.RESULTS_EXPLOIT[].EDB_ID` | Exploit-DB 编号 |
| `.RESULTS_EXPLOIT[].Title` | 标题 |
| `.RESULTS_EXPLOIT[].Path` | 路径 |
| `.RESULTS_EXPLOIT[].Date` | 日期 |
| `.RESULTS_EXPLOIT[].Author` | 作者 |
| `.RESULTS_EXPLOIT[].Type` | 类型 |
| `.RESULTS_EXPLOIT[].Platform` | 平台 |
| `.RESULTS_SHELLCODE[]` | shellcode 类结果 |

### 判断要点

1. **"有 EXP" ≠ "有漏洞"**。searchsploit 是离线关键字匹配，无法知道目标是否真的受影响。
2. **版本号必须精确**：搜 `apache 2.4` 会返回一大片，搜 `apache 2.4.49` 才有针对性。
3. **优先 Metasploit 模块**：`.rb` 结尾的条目在 MSF 里通常已经处理好了参数与稳定性，比裸 PoC 可靠得多。
4. **验证顺序建议**：先 [nuclei](nuclei.md) 模板确认，再考虑 EXP；能不动 EXP 就不动。

## 7. 与其他工具配合

```bash
# ★ 最核心的流水线：nmap -sV -oX -> searchsploit --nmap
sudo nmap -sV -oX scan.xml 192.168.56.101
searchsploit --nmap scan.xml
# 有对应的 .rb 时，交给 Metasploit
msfconsole -q -x 'search vsftpd; use exploit/unix/ftp/vsftpd_234_backdoor; show options'

# whatweb 指纹 -> searchsploit
whatweb -a 1 http://192.168.56.101 | tr ',' '\n' | grep -oP '\w+\[\K[^\]]+' | sort -u > svc.txt
while read -r s; do echo "=== $s ==="; searchsploit -t "$s" | head -5; done < svc.txt

# nuclei 命中 CVE -> searchsploit 找 EXP
nuclei -u http://192.168.56.101 -jsonl -je n.jsonl -silent
jq -r '.info.classification["cve-id"][]?' n.jsonl | sort -u | while read -r cve; do
  echo "=== $cve ==="; searchsploit --cve "${cve#CVE-}"
done

# searchsploit -> 本地工作区（改 EXP 不要动系统目录）
searchsploit -m 50383 && vim 50383.sh
```

## 8. 常见坑与排错

| 现象 | 原因 | 解决 |
|------|------|------|
| `searchsploit: command not found` | 只装了 `exploitdb` 但路径未生效 | `sudo apt install exploitdb`；确认 `/usr/bin/searchsploit` 存在 |
| 搜索数字（版本号）时结果泛滥 | 默认匹配标题**+文件路径**，路径里含相同数字 | 加 `-t`（只看标题） |
| 搜 `1.1` 命中了 `1.0 < 1.3` 之类的条目 | 默认启用版本区间模糊匹配 | 加 `-s`（strict） |
| 结果里有大量无用的 DoS/PoC | 未过滤 | `--exclude="(PoC)\|/dos/"` |
| 刚发布的 CVE 搜不到 | 本地库未更新 | `sudo searchsploit -u` 或 `apt install --only-upgrade exploitdb` |
| `-x` 打开报 `$PAGER` 相关错误 | 环境没有设置分页器 | `export PAGER=less`，或直接 `cat` 路径 |
| `-m` 复制后修改，升级后丢失 | 直接改了系统目录 | 用 `-m` 复制到自己的工作目录再改 |
| `--nmap` 报解析失败 | XML 不是 nmap 生成的，或没带 `-sV` | 用 `nmap -sV -oX` 重新生成 |
| `--nmap` 漏掉很多服务 | 关键词组合不够 | 加 `-v` 让 searchsploit 尝试更多组合 |
| JSON 输出配 `jq` 报错 | 键名大小写或结构不对 | 先 `searchsploit -j <term> | head -30` 看实际结构 |
| 颜色转义符污染输出文件 | ANSI 颜色 | `--disable-colour` |
| 磁盘占用大（191 MB 起） | exploitdb 包本身很大 | 不需要时 `apt remove exploitdb`；也可只装 `exploitdb-bin-sploits` 之类 |

## 9. 防御视角（蓝队）

searchsploit 本身**不发任何网络流量**（纯本地查询），所以"检测"不适用。防御的重点是**让查询结果变得没用**。

- **核心思路：让"版本"无法被确定**。
  - 隐藏服务 banner：`ServerTokens Prod`（Apache）、`server_tokens off`（nginx）、`expose_php = Off`（PHP）、修改 SSH banner。
  - **版本号是 searchsploit 的输入。没有版本号，这个工具就退化成了"猜"**。
- **减少"有 EXP 的版本"的存活时间**：
  - 建立补丁管理流程。searchsploit 的命中率直接反映你的**补丁延迟**。
  - 定期自查：用 [nmap](../01-信息搜集/nmap.md) `-sV` 扫自己 + `searchsploit --nmap` 查自己的服务——这应该是一个例行的"暴露面核查"流程。
- **配置层面的针对性加固**（对应 EXP 高发区）：
  - VSFTPD 2.3.4 后门 → 升级 vsftpd；不要用来源不明的软件包。
  - Apache 2.4.49/2.4.50 路径穿越 → 及时打补丁；这是被 EXP 覆盖最广的一类。
  - 旧版 phpMyAdmin / Tomcat / Struts → 这些是 EXP 数量的高地，优先升级或下架。
- **纵深防御**：即使版本有对应 EXP，也不代表一定能打通。
  - WAF 虚拟补丁（对已知 EXP 的 payload 做特征拦截）。
  - 最小权限运行服务、容器隔离、只读文件系统。
  - 出网限制（很多 EXP 需要反弹 shell 或下载二段载荷）。
- **蓝队可用性**：`searchsploit --nmap` 同样适合蓝队做**漏洞管理优先级排序**——把你资产扫描结果和 EXP 库对照，快速识别"有哪些服务存在公开可用的攻击代码"，优先修这些。

## 10. 参考

- Exploit-DB 官网：<https://www.exploit-db.com/>
- SearchSploit 手册：<https://www.exploit-db.com/searchsploit>
- 官方仓库（含 `searchsploit` 脚本与数据库）：<https://gitlab.com/exploit-database/exploitdb>
- Kali 工具页（包归属 `exploitdb`）：<https://www.kali.org/tools/exploitdb/>
- man page：`man searchsploit`
- 用法核实：本教程参数取自 `exploitdb` 包 man page（`searchsploit 3.8.8`）与上游 `searchsploit` 脚本 `usage()` 的实际选项定义

---

**相关教程**：[nuclei](nuclei.md) ｜ [nikto](nikto.md) ｜ [lynis](lynis.md) ｜ [openssl](openssl.md) ｜ [nmap](../01-信息搜集/nmap.md) ｜ [whatweb](../01-信息搜集/whatweb.md)
