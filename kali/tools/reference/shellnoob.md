# shellnoob

> Shellcode writing toolkit Features: * convert shellcode between different formats and sources. Formats currently supported: asm, bin, hex, obj, exe, C, Python, ruby, pretty, safeasm, completec, shellstorm. (All details in the “Formats desc…

> **功能分类**：漏洞利用 ｜ **Kali 包**：`shellnoob` ｜ **官方文档**：<https://www.kali.org/tools/shellnoob/>

## 1. 安装

```bash
sudo apt update
sudo apt install shellnoob
```

| 项目 | 内容 |
|------|------|
| 版本 | 2.1 |
| 架构 | amd64 |
| 可执行命令 | `shellnoob` |
| 依赖 | `python3` |
| 安装体积 | 96 KB |
| 官网 | <https://github.com/reyammer/shellnoob> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/shellnoob> |
| 包追踪 | <https://pkg.kali.org/pkg/shellnoob> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
shellnoob -h          # 查看用法
man shellnoob         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `shellnoob`

> 官方示例调用：`shellnoob -i --to-opcode`

```text
root@kali:~# shellnoob -i --to-opcode
asm_to_opcode selected (type "quit" or ^C to end)
>> xchg %eax, %esp
xchg %eax, %esp ~> 94
>> ret
ret ~> c3
>>
```

### `shellnoob -h`

> 官方示例调用：`shellnoob -h`

```text
root@kali:~# shellnoob -h
shellnoob.py [--from-INPUT] (input_file_path | - ) [--to-OUTPUT] [output_file_path | - ]
shellnoob.py -c (prepend a breakpoint (Warning: only few platforms/OS are supported!)
shellnoob.py --64 (64 bits mode, default: 32 bits)
shellnoob.py --intel (intel syntax mode, default: att)
shellnoob.py -q (quite mode)
shellnoob.py -v (or -vv, -vvv)
shellnoob.py --to-strace (compiles it & run strace)
shellnoob.py --to-gdb (compiles it & run gdb & set breakpoint on entrypoint)
Standalone "plugins"
shellnoob.py -i [--to-asm | --to-opcode ] (for interactive mode)
shellnoob.py --get-const <const>
shellnoob.py --get-sysnum <sysnum>
shellnoob.py --get-strerror <errno>
shellnoob.py --file-patch <exe_fp> <file_offset> <data> (in hex). (Warning: tested only on x86/x86_64)
shellnoob.py --vm-patch <exe_fp> <vm_address> <data> (in hex). (Warning: tested only on x86/x86_64)
shellnoob.py --fork-nopper <exe_fp> (this nops out the calls to fork(). Warning: tested only on x86/x86_64)
"Installation"
shellnoob.py --install [--force] (this just copies the script in a convinient position)
shellnoob.py --uninstall [--force]
Supported INPUT format: asm, obj, bin, hex, c, shellstorm
Supported OUTPUT format: asm, obj, exe, bin, hex, c, completec, python, bash, ruby, pretty, safeasm
All combinations from INPUT to OUTPUT are supported!
Check out the README file for more info.
Updated on: 2025-Dec-09
 Edit this page
shed
sipcrack
LIGHT
DARK
Links
Home
Download / Get Kali
Blog
OS Documentation
Tool Documentation
System Status
Archived Releases
Partnerships
Platforms
ARM (SBC)
NetHunter (Mobile)
Amazon AWS
Docker
Linode
Microsoft Azure
Microsoft Store (WSL)
Vagrant
Development
Bug Tracker
Continuous Integration
Network Mirror
Package Tracker
GitLab
Community
Discord
Support Forum
PeerTube
Follow Us
Bluesky
Facebook
Instagram
Mastodon
Substack
X
Newsletter
RSS
Policies
Cookie Policy
Privacy Policy
Trademark Policy
© OffSec Services Limited 2026. All rights reserved.
Kali Linux is part of OffSec's Community Projects
Learn more about OffSec's free, open-source penetration testing tools for cybersecurity professionals
```

## 4. 实践清单

按顺序做完这五步，就能把工具从「装上」推进到「会用」：

- [ ] **1.** **装好并确认版本** —— `sudo apt install shellnoob`，再执行 `shellnoob --version` 2>/dev/null || `shellnoob -V`
- [ ] **2.** **读官方帮助** —— `shellnoob -h`，需要细节时 `man shellnoob`
- [ ] **3.** **在自有靶场跑最小用例** —— 用 `shellnoob -h` 里最简单的那个子命令试一次
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/shellnoob/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/resource-development.md`](../../tools/by-attack/resource-development.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/shellnoob/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/shellnoob/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
