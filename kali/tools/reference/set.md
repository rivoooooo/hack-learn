# set

> Social-Engineer Toolkit The Social-Engineer Toolkit (SET) is an open-source Python-driven tool aimed at penetration testing around Social-Engineering.

> **功能分类**：漏洞利用 ｜ **Kali 包**：`set` ｜ **官方文档**：<https://www.kali.org/tools/set/>

## 1. 安装

```bash
sudo apt update
sudo apt install set
```

| 项目 | 内容 |
|------|------|
| 版本 | 8.1.3 |
| 架构 | all |
| 可执行命令 | `set`、`se-toolkit`、`setoolkit` |
| 依赖 | `aircrack-ng`、`dsniff`、`ettercap-common`、`kali-defaults`、`libapache2-mod-php`、`metasploit-framework`、`nginx`、`openssl`、`python3`、`python3-impacket`、`python3-openssl`、`python3-paramiko` 等 |
| 安装体积 | 30.40 MB |
| 官网 | <https://www.trustedsec.com/downloads/social-engineer-toolkit/> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/set> |
| 包追踪 | <https://pkg.kali.org/pkg/set> |

## 2. 官方用法示例

> 以下为 Kali 官方工具页给出的示例与输出原文。

```text
Usage Example
root@kali:~# setoolkit

         01011001011011110111010100100000011100
         10011001010110000101101100011011000111
         10010010000001101000011000010111011001
         10010100100000011101000110111100100000
         01101101011101010110001101101000001000
         00011101000110100101101101011001010010
         00000110111101101110001000000111100101
         10111101110101011100100010000001101000
         01100001011011100110010001110011001000
         00001110100010110100101001001000000101
         01000110100001100001011011100110101101
         11001100100000011001100110111101110010
         00100000011101010111001101101001011011
         10011001110010000001110100011010000110
         01010010000001010011011011110110001101
         10100101100001011011000010110101000101
         01101110011001110110100101101110011001
         01011001010111001000100000010101000110
         11110110111101101100011010110110100101
         11010000100000001010100110100001110101
         011001110111001100101010

[---]        The Social-Engineer Toolkit (SET)         [---]
[---]        Created by: David Kennedy (ReL1K)         [---]
                      Version: 7.7.9
                   Codename: 'Blackout'
[---]        Follow us on Twitter: @TrustedSec         [---]
[---]        Follow me on Twitter: @HackingDave        [---]
[---]       Homepage: https://www.trustedsec.com       [---]
        Welcome to the Social-Engineer Toolkit (SET).
         The one stop shop for all of your SE needs.

     Join us on irc.freenode.net in channel #setoolkit

   The Social-Engineer Toolkit is a product of TrustedSec.

           Visit: https://www.trustedsec.com

   It's easy to update using the PenTesters Framework! (PTF)
Visit https://github.com/trustedsec/ptf to update all your tools!


 Select from the menu:

   1) Social-Engineering Attacks
   2) Penetration Testing (Fast-Track)
   3) Third Party Modules
   4) Update the Social-Engineer Toolkit
   5) Update SET configuration
   6) Help, Credits, and About

  99) Exit the Social-Engineer Toolkit

set>
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 3 个可执行命令，下面是官方页面内嵌的帮助原文。

### `setoolkit`

```text
root@kali:~# setoolkit
         01011001011011110111010100100000011100
         10011001010110000101101100011011000111
         10010010000001101000011000010111011001
         10010100100000011101000110111100100000
         01101101011101010110001101101000001000
         00011101000110100101101101011001010010
         00000110111101101110001000000111100101
         10111101110101011100100010000001101000
         01100001011011100110010001110011001000
         00001110100010110100101001001000000101
         01000110100001100001011011100110101101
         11001100100000011001100110111101110010
         00100000011101010111001101101001011011
         10011001110010000001110100011010000110
         01010010000001010011011011110110001101
         10100101100001011011000010110101000101
         01101110011001110110100101101110011001
         01011001010111001000100000010101000110
         11110110111101101100011010110110100101
         11010000100000001010100110100001110101
         011001110111001100101010
[---]        The Social-Engineer Toolkit (SET)         [---]
[---]        Created by: David Kennedy (ReL1K)         [---]
                      Version: 7.7.9
                   Codename: 'Blackout'
[---]        Follow us on Twitter: @TrustedSec         [---]
[---]        Follow me on Twitter: @HackingDave        [---]
[---]       Homepage: https://www.trustedsec.com       [---]
        Welcome to the Social-Engineer Toolkit (SET).
         The one stop shop for all of your SE needs.
     Join us on irc.freenode.net in channel #setoolkit
   The Social-Engineer Toolkit is a product of TrustedSec.
           Visit: https://www.trustedsec.com
   It's easy to update using the PenTesters Framework! (PTF)
Visit https://github.com/trustedsec/ptf to update all your tools!
 Select from the menu:
   1) Social-Engineering Attacks
   2) Penetration Testing (Fast-Track)
   3) Third Party Modules
   4) Update the Social-Engineer Toolkit
   5) Update SET configuration
   6) Help, Credits, and About
  99) Exit the Social-Engineer Toolkit
set>
```

### `se-toolkit`

官方给出的调用示例：`se-toolkit -h`

```text
root@kali:~# se-toolkit -h
┏━(Message from Kali developers)
┃
┃ The command se-toolkit is deprecated. Please use setoolkit instead.
┃
┗━
```

### `setoolkit（示例）`

官方给出的调用示例：`setoolkit -h`

```text
root@kali:~# setoolkit -h
[-] New set.config.py file generated on: 2026-09-14 07:53:58.021268
[-] Verifying configuration update...
[*] Update verified, config timestamp is: 2026-09-14 07:53:58.021268
[*] SET is using the new config, no need to restart
Copyright 2020, The Social-Engineer Toolkit (SET) by TrustedSec, LLC
All rights reserved.
Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:
    * Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.
    * Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.
    * Neither the name of Social-Engineer Toolkit nor the names of its contributors may be used to endorse or promote products derived from this software without specific prior written permission.
THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY  THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
The above licensing was taken from the BSD licensing and is applied to Social-Engineer Toolkit as well.
Note that the Social-Engineer Toolkit is provided as is, and is a royalty free open-source application.
Feel free to modify, use, change, market, do whatever you want with it as long as you give the appropriate credit where credit is due (which means giving the authors the credit they deserve for writing it).
Also note that by using this software, if you ever see the creator of SET in a bar, you should (optional) give him a hug and should (optional) buy him a beer (or bourbon - hopefully bourbon). Author has the option to refuse the hug (most likely will never happen) or the beer or bourbon (also most likely will never happen). Also by using this tool (these are all optional of course!), you should try to make this industry better, try to stay positive, try to help others, try to learn from one another, try stay out of drama, try offer free hugs when possible (and make sure recipient agrees to mutual hug), and try to do everything you can to be awesome.
The Social-Engineer Toolkit is designed purely for good and not evil. If you are planning on using this tool for malicious purposes that are not authorized by the company you are performing assessments for, you are violating the terms of service and license of this toolset. By hitting yes (only one time), you agree to the terms of service and that you will only use this tool for lawful purposes only.
Do you agree to the terms of service [y/n]:
Updated on: 2026-Aug-25
 Edit this page
sdrangel
sfuzz
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install set`，再执行 `set --version` 2>/dev/null || `set -V`
- [ ] **2.** **读官方帮助** —— `set -h`，需要细节时 `man set`
- [ ] **3.** **在自有靶场跑最小用例** —— 用 `set -h` 里最简单的那个子命令试一次
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/set/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- **精讲教程**（含原理、参数详解、靶场实操与输出解读）：[set](../../tools/tutorials/11-社会工程与报告/set.md)
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/initial-access.md`](../../tools/by-attack/initial-access.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/set/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/set/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
