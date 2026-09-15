# metasploit-framework

> Framework for exploit development and vulnerability research The Metasploit Framework is an open source platform that supports vulnerability research, exploit development, and the creation of custom security tools.

> **功能分类**：信息搜集 ｜ **Kali 包**：`metasploit-framework` ｜ **官方文档**：<https://www.kali.org/tools/metasploit-framework/>

## 1. 安装

```bash
sudo apt update
sudo apt install metasploit-framework
```

| 项目 | 内容 |
|------|------|
| 版本 | 6.5.3 |
| 架构 | any |
| 可执行命令 | `metasploit-framework`、`msf-egghunter`、`msf-exe2vba`、`msf-exe2vbs`、`msf-find_badchars`、`msf-halflm_second`、`msf-hmac_sha1_crack`、`msf-java_deserializer`、`msf-jsobfu`、`msf-makeiplist`、`msf-md5_lookup`、`msf-metasm_shell`、`msf-msf_irb_shell`、`msf-nasm_shell`、`msf-pattern_create`、`msf-pattern_offset`、`msf-pdf2xdp`、`msf-virustotal`、`msfconsole`、`msfd`、`msfdb`、`msfrpc`、`msfrpcd`、`msfupdate`、`msfvenom` |
| 依赖 | `bundler`、`curl`、`gcc-mingw-w64-i686-win32`、`gcc-mingw-w64-x86-64-win32`、`git`、`john`、`libc6`、`libffi8`、`libgcc-s1`、`liblzma5`、`libpcap0.8t64`、`libruby3.3` 等 |
| 安装体积 | 598.76 MB |
| 官网 | <https://www.metasploit.com/> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/metasploit-framework> |
| 包追踪 | <https://pkg.kali.org/pkg/metasploit-framework> |

## 2. 官方用法示例

> 以下为 Kali 官方工具页给出的示例与输出原文。

```text
Usage Examples
One of the best sources of information on using the Metasploit Framework is Metasploit Unleashed, a free online course created by OffSec. Metasploit Unleashed guides you from the absolute basics of Metasploit all the way through to advanced topics.
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 25 个可执行命令，下面是官方页面内嵌的帮助原文。

### `msfrpcd`

> 官方示例调用：`msfrpcd -h`

```text
root@kali:~# msfrpcd -h
Usage: msfrpcd <options>
OPTIONS:
    -P <opt>  Specify the password to access msfrpcd
    -S        Disable SSL on the RPC socket
    -U <opt>  Specify the username to access msfrpcd
    -a <opt>  Bind to this IP address
    -f        Run the daemon in the foreground
    -h        Help banner
    -n        Disable database
    -p <opt>  Bind to this port instead of 55553
    -t <opt>  Token Timeout (default 300 seconds
    -u <opt>  URI for Web server
Metasploit-Framework Usage Examples
One of the best sources of information on using the Metasploit Framework is
Metasploit Unleashed
, a free online course created by OffSec. Metasploit Unleashed guides you from the absolute basics of Metasploit all the way through to advanced topics.
```

### `msf-egghunter`

> 官方示例调用：`msf-egghunter -h`

```text
root@kali:~# msf-egghunter -h
Usage: msf-egghunter [options]
Example: msf-egghunter -f python -e W00T
Specific options:
    -f, --format <String>            See --list-formats for a list of supported output formats
    -b, --badchars <String>          (Optional) Bad characters to avoid for the egg
    -e, --egg <String>               The egg (Please give 4 bytes)
    -p, --platform <String>          (Optional) Platform
        --startreg <String>          (Optional) The starting register
        --forward                    (Optional) To search forward
        --depreg <String>            (Optional) The DEP register
        --depdest <String>           (Optional) The DEP destination
        --depsize <Integer>          (Optional) The DEP size
        --depmethod <String>         (Optional) The DEP method to use (virtualprotect/virtualalloc/copy/copy_size)
    -a, --arch <String>              (Optional) Architecture
        --list-formats               List all supported output formats
    -v, --var-name <name>            (Optional) Specify a custom variable name to use for certain output formats
    -h, --help                       Show this message
```

### `msf-exe2vba`

> 官方示例调用：`msf-exe2vba -h`

```text
root@kali:~# msf-exe2vba -h
    Usage: msf-exe2vba [exe] [vba]
```

### `msf-exe2vbs`

> 官方示例调用：`msf-exe2vbs -h`

```text
root@kali:~# msf-exe2vbs -h
    Usage: msf-exe2vbs [exe] [vbs]
```

### `msf-find_badchars`

> 官方示例调用：`msf-find_badchars -h`

```text
root@kali:~# msf-find_badchars -h
    Usage: msf-find_badchars <options>
OPTIONS:
    -b   The list of characters to avoid: '\x00\xff'
    -h   Help banner
    -i   Read memory contents from the supplied file path
    -t   The format that the memory contents are in (empty to list)
```

### `msf-halflm_second`

> 官方示例调用：`msf-halflm_second -h`

```text
root@kali:~# msf-halflm_second -h
    Usage: msf-halflm_second <options>
OPTIONS:
    -h   Display this help information
    -n   The encrypted LM hash to crack
    -p   The decrypted LANMAN password for bytes 1-7
    -s   The server challenge (default value 1122334455667788)
```

### `msf-hmac_sha1_crack`

> 官方示例调用：`msf-hmac_sha1_crack -h`

```text
root@kali:~# msf-hmac_sha1_crack -h
Usage: msf-hmac_sha1_crack hashes.txt <wordlist | - >
The format of hash file is <identifier>:<hex-salt>:<hash>
```

### `msf-java_deserializer`

> 官方示例调用：`msf-java_deserializer -h`

```text
root@kali:~# msf-java_deserializer -h
Usage: msf-java_deserializer <file> [option]
    -a, --array=ID                   Print detailed information about content array
    -o, --object=ID                  Print detailed information about content object
    -h, --help                       Prints this help
```

### `msf-jsobfu`

> 官方示例调用：`msf-jsobfu -h`

```text
root@kali:~# msf-jsobfu -h
Usage: msf-jsobfu [options]
Specific options:
    -t, --iteration <Integer>        Number of times to obfuscate the JavaScript
    -i, --input <String>             The JavaScript file you want to obfuscate (default=1)
    -o, --output <String>            Save the obfuscated file as
    -p id1,id2,                      The identifiers to preserve
        --preserved-identifiers
    -h, --help                       Show this message
```

### `msf-md5_lookup`

> 官方示例调用：`msf-md5_lookup -h`

```text
root@kali:~# msf-md5_lookup -h
Usage: msf-md5_lookup [options]
Specific options:
    -i, --input <file>               The file that contains all the MD5 hashes (one line per hash)
    -d, --databases <names>          (Optional) Select databases: all, authsecu, i337, md5_my_addr, md5_net, md5crack, md5cracker, md5decryption, md5online, md5pass, netmd5crack, tmto (Default=all)
    -o, --out <filepath>             (Optional) Save the results to a file (Default=md5_results.txt)
    -h, --help                       Show this message
```

## 4. 实践清单

按顺序做完这五步，就能把工具从「装上」推进到「会用」：

- [ ] **1.** **装好并确认版本** —— `sudo apt install metasploit-framework`，再执行 `metasploit-framework --version` 2>/dev/null || `metasploit-framework -V`
- [ ] **2.** **读官方帮助** —— `metasploit-framework -h`，需要细节时 `man metasploit-framework`
- [ ] **3.** **在自有靶场跑最小用例** —— 官方给出的调用形式是：`Usage: msfrpcd <options>`
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/metasploit-framework/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- **精讲教程**（含原理、参数详解、靶场实操与输出解读）：[metasploit-framework](../../tools/tutorials/06-漏洞利用/metasploit-framework.md)
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/resource-development.md`](../../tools/by-attack/resource-development.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/metasploit-framework/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/metasploit-framework/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
