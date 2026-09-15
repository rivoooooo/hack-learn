# phpggc

> Generate payloads that exploit unsafe object deserialization PHPGGC is a library of payloads exploiting unsafe object deserialization. It also provides a command-line tool to generate them.

> **功能分类**：通用工具 ｜ **Kali 包**：`phpggc` ｜ **官方文档**：<https://www.kali.org/tools/phpggc/>

## 1. 安装

```bash
sudo apt update
sudo apt install phpggc
```

| 项目 | 内容 |
|------|------|
| 版本 | 0.20230428 |
| 架构 | all |
| 可执行命令 | `phpggc` |
| 依赖 | `php-cli` |
| 安装体积 | 650 KB |
| 官网 | <https://github.com/ambionics/phpggc> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/phpggc> |
| 包追踪 | <https://pkg.kali.org/pkg/phpggc> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
phpggc -h          # 查看用法
man phpggc         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `phpggc`

官方给出的调用示例：`phpggc -h`

```text
root@kali:~# phpggc -h
PHPGGC: PHP Generic Gadget Chains
---------------------------------
USAGE
  ./phpggc [-h|-l|-i|...] <GadgetChain> [arguments]
INFORMATION
  -h, --help Displays help
  -l, --list [filter] Lists available gadget chains
  -i, --information
     Displays information about a gadget chain
OUTPUT
  -o, --output <file>
     Outputs the payload to a file instead of standard output
PHAR
  -p, --phar <tar|zip|phar>
     Creates a PHAR file of the given format
  -pj, --phar-jpeg <file>
     Creates a polyglot JPEG/PHAR file from given image
  -pp, --phar-prefix <file>
     Sets the PHAR prefix as the contents of the given file.
     Generally used with -p phar to control the beginning of the generated file.
  -pf, --phar-filename <filename>
     Defines the name of the file contained in the generated PHAR (default: test.txt)
ENHANCEMENTS
  -f, --fast-destruct
     Applies the fast-destruct technique, so that the object is destroyed
     right after the unserialize() call, as opposed to at the end of the
     script
  -a, --ascii-strings
     Uses the 'S' serialization format instead of the standard 's' for non-printable chars.
     This replaces every non-ASCII value to an hexadecimal representation:
       s:5:"A<null_byte>B<cr><lf>"; -> S:5:"A\00B\09\0D";
     This is experimental and it might not work in some cases.
  -A, --armor-strings
     Uses the 'S' serialization format instead of the standard 's' for every char.
     This replaces every character to an hexadecimal representation:
       s:5:"A<null_byte>B<cr><lf>"; -> S:5:"\41\00\42\09\0D";
     This is experimental and it might not work in some cases.
     Note: Since strings grow by a factor of 3 using this option, the payload can get
     really long.
  -n, --plus-numbers <types>
     Adds a + symbol in front of every number symbol of the given type.
     For instance, -n iO adds a + in front of every int and object name size:
     O:3:"Abc":1:{s:1:"x";i:3;} -> O:+3:"Abc":1:{s:1:"x";i:+3;}
     Note: Since PHP 7.2, only i and d (float) types can have a +
  -w, --wrapper <wrapper>
     Specifies a file containing at least one wrapper functions:
       - process_parameters(array $parameters): called right before object is created
       - process_object(object $object): called right before the payload is serialized
       - process_serialized(string $serialized): called right after the payload is serialized
ENCODING
  -s, --soft   Soft URLencode
  -u, --url    URLencodes the payload
  -b, --base64 Converts the output into base64
  -j, --json   Converts the output into json
  Encoders can be chained, for instance -b -u -u base64s the payload,
  then URLencodes it twice
CREATION
  -N, --new <framework> <type>
    Creates the file structure for a new gadgetchain for given framework
    Example: ./phpggc -N Drupal RCE
  --test-payload
    Instead of displaying or storing the payload, includes vendor/autoload.php and unserializes the payload.
    The test script can only deserialize __destruct, __wakeup, __toString and PHAR payloads.
    Warning: This will run the payload on YOUR system !
EXAMPLES
  ./phpggc -l
  ./phpggc -l drupal
  ./phpggc Laravel/RCE1 system id
  ./phpggc SwiftMailer/FW1 /var/www/html/shell.php /path/to/local/shell.php
Updated on: 2025-Dec-09
 Edit this page
photon
phpsploit
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install phpggc`，再执行 `phpggc --version` 2>/dev/null || `phpggc -V`
- [ ] **2.** **读官方帮助** —— `phpggc -h`，需要细节时 `man phpggc`
- [ ] **3.** **在自有靶场跑最小用例** —— 用 `phpggc -h` 里最简单的那个子命令试一次
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/phpggc/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/persistence.md`](../../tools/by-attack/persistence.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/phpggc/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/phpggc/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
