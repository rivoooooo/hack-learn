# spike

> Network protocol fuzzer When you need to analyze a new network protocol for buffer overflows or similar weaknesses, the SPIKE is the tool of choice for professionals. While it requires a strong knowledge of C to use, it produces results se…

> **功能分类**：漏洞分析 ｜ **Kali 包**：`spike` ｜ **官方文档**：<https://www.kali.org/tools/spike/>

## 1. 安装

```bash
sudo apt update
sudo apt install spike
```

| 项目 | 内容 |
|------|------|
| 版本 | 2.9 |
| 架构 | any |
| 可执行命令 | `spike`、`citrix`、`closed_source_web_server_fuzz`、`dceoversmb`、`dltest`、`do_post`、`generic_chunked`、`generic_listen_tcp`、`generic_send_tcp`、`generic_send_udp`、`generic_web_server_fuzz`、`generic_web_server_fuzz2`、`gopherd`、`halflife`、`line_send_tcp`、`msrpcfuzz`、`msrpcfuzz_udp`、`ntlm2`、`ntlm_brute`、`pmspike`、`post_fuzz`、`post_spike`、`quake`、`quakeserver`、`sendmsrpc`、`ss_spike`、`statd_spike`、`sunrpcfuzz`、`webfuzz`、`x11_spike` |
| 依赖 | `libc6`、`citrix` |
| 安装体积 | 3.78 MB |
| 官网 | <http://www.immunitysec.com/resources-freesoftware.shtml> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/spike> |
| 包追踪 | <https://pkg.kali.org/pkg/spike> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
spike -h          # 查看用法
man spike         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 30 个可执行命令，下面是官方页面内嵌的帮助原文。

### `citrix`

> 官方示例调用：`citrix -h`

```text
root@kali:~# citrix -h
Usage: ./citrix target port
./citrix 192.168.1.101 1494
```

### `closed_source_web_server_fuzz`

> 官方示例调用：`closed_source_web_server_fuzz -h`

```text
root@kali:~# closed_source_web_server_fuzz -h
Example: ./closed localhost 80 POST /_vti_bin/ shtml .exe 0 0
Don't forget the period before the extention.
Common Extentions are: .asa .asp .cdx .cer .htw .htr .ida .idc .idq .shtm .shtml .stm .printer .jsp .jhtml .bat .exe .com .gif .jpg .mpg .rma .wma .cfm .pl .py .pike, etc
Common methods are OPTIONS, TRACE, GET, HEAD, DELETE, PUT, POST, COPY, MOVE, MKCOL, PROPFIND, PROPPATCH, LOCK, UNLOCK, SEARCH, BROWSE
Try with both existing and NON existing files. Also try .dll with .exe and vice versa
Try ALL the extentions and go into your server settings windows and try all methods and all directories as well. If it crashes, ask for a refund.
Anything that says, 500 Server Error, also indicates a buggy web server. Might even be exploitable.
Likewise to anything like Error (not 0x80040e14, which MS uses for 'not an overflow' for some reason) caught while processing query. These are signs of serious problems in the web server.
Happy bug hunting!
contact Dave Aitel if you find anything cool. :>
```

### `dceoversmb`

> 官方示例调用：`dceoversmb -h`

```text
root@kali:~# dceoversmb -h
Argc=2 not 9
Usage: ./dceoversmb target pipe GUID Version VersionMinor(usually 0) function_number number_of_tries max_number_of_random_items
Example: ./dceoversmb 10.25.25.15 \\pipe\\srvsvc e1af8308-5d1f-11c9-91a4-08002b14a0fa 3 0 2 10 3 [login password]
Read the msrpc readme when you get a chance.
```

### `dltest`

> 官方示例调用：`dltest -h`

```text
root@kali:~# dltest -h
Couldn't open file test.spk to parse with s_parse()
```

### `do_post`

> 官方示例调用：`do_post -h`

```text
root@kali:~# do_post -h
Usage: ./post_spike target port optional
```

### `generic_chunked`

> 官方示例调用：`generic_chunked -h`

```text
root@kali:~# generic_chunked -h
Usage: ./generic_web_server_fuzz target port file.spk skipvariables skipfuzzstring
Example: ./gwsf exchange1 80 owa1.spk 0 0
http://www.immunitysec.com/spike.html
```

### `generic_listen_tcp`

> 官方示例调用：`generic_listen_tcp -h`

```text
root@kali:~# generic_listen_tcp -h
argc=2
Usage: ./generic_listen_tcp port spike_script
./generic_listen_tcp 70 gopherd.spk
```

### `generic_send_tcp`

> 官方示例调用：`generic_send_tcp -h`

```text
root@kali:~# generic_send_tcp -h
argc=2
Usage: ./generic_send_tcp host port spike_script SKIPVAR SKIPSTR
./generic_send_tcp 192.168.1.100 701 something.spk 0 0
```

### `generic_send_udp`

> 官方示例调用：`generic_send_udp -h`

```text
root@kali:~# generic_send_udp -h
argc=2
Usage: ./gsu target port file.spk startvariable startfuzzstring startvariable startstring totaltosend
./gsu 192.168.1.104 80 file.spk 0 0 5000
```

### `generic_web_server_fuzz`

> 官方示例调用：`generic_web_server_fuzz -h`

```text
root@kali:~# generic_web_server_fuzz -h
Usage: ./generic_web_server_fuzz target port file.spk skipvariables skipfuzzstring
Example: ./gwsf exchange1 80 owa1.spk 0 0
http://www.immunitysec.com/spike.html
```

## 4. 实践清单

按顺序做完这五步，就能把工具从「装上」推进到「会用」：

- [ ] **1.** **装好并确认版本** —— `sudo apt install spike`，再执行 `spike --version` 2>/dev/null || `spike -V`
- [ ] **2.** **读官方帮助** —— `spike -h`，需要细节时 `man spike`
- [ ] **3.** **在自有靶场跑最小用例** —— 官方给出的调用形式是：`Usage: ./citrix target port`
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/spike/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/resource-development.md`](../../tools/by-attack/resource-development.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/spike/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/spike/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
