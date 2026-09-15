# dnschef

> DNS proxy for penetration testers DNSChef is a highly configurable DNS proxy for Penetration Testers and Malware Analysts. A DNS proxy (aka “Fake DNS”) is a tool used for application network traffic analysis among other uses. For example, …

> **功能分类**：嗅探与欺骗 ｜ **Kali 包**：`dnschef` ｜ **官方文档**：<https://www.kali.org/tools/dnschef/>

## 1. 安装

```bash
sudo apt update
sudo apt install dnschef
```

| 项目 | 内容 |
|------|------|
| 版本 | 0.4 |
| 架构 | all |
| 可执行命令 | `dnschef` |
| 依赖 | `python3`、`python3-dnslib` |
| 安装体积 | 51 KB |
| 官网 | <https://github.com/iphelix/dnschef> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/dnschef> |
| 包追踪 | <https://pkg.kali.org/pkg/dnschef> |

## 2. 官方用法示例

> 以下为 Kali 官方工具页给出的示例与输出原文。

```text
Usage Example
root@kali:~# dnschef
          _                _          __
         | | version 0.1  | |        / _|
       __| |_ __  ___  ___| |__   ___| |_
      / _` | '_ \/ __|/ __| '_ \ / _ \  _|
     | (_| | | | \__ \ (__| | | |  __/ |
      \__,_|_| |_|___/\___|_| |_|\___|_|
                   iphelix@thesprawl.org

[*] DNS Chef started on interface: 127.0.0.1
[*] Using the following nameservers: 8.8.8.8
[*] No parameters were specified. Running in full proxy mode
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `dnschef`

```text
root@kali:~# dnschef
          _                _          __
         | | version 0.1  | |        / _|
       __| |_ __  ___  ___| |__   ___| |_
      / _` | '_ \/ __|/ __| '_ \ / _ \  _|
     | (_| | | | \__ \ (__| | | |  __/ |
      \__,_|_| |_|___/\___|_| |_|\___|_|
[email protected]
[*] DNS Chef started on interface: 127.0.0.1
[*] Using the following nameservers: 8.8.8.8
[*] No parameters were specified. Running in full proxy mode
```

### `dnschef -h`

> 官方示例调用：`dnschef -h`

```text
root@kali:~# dnschef -h
usage: dnschef [options]:
          _                _          __
         | | version 0.4  | |        / _|
       __| |_ __  ___  ___| |__   ___| |_
      / _` | '_ \/ __|/ __| '_ \ / _ \  _|
     | (_| | | | \__ \ (__| | | |  __/ |
      \__,_|_| |_|___/\___|_| |_|\___|_|
[email protected]
DNSChef is a highly configurable DNS Proxy for Penetration Testers and Malware
Analysts. It is capable of fine configuration of which DNS replies to modify
or to simply proxy with real responses. In order to take advantage of the tool
you must either manually configure or poison DNS server entry to point to
DNSChef. The tool requires root privileges to run on privileged ports.
options:
  -h, --help            show this help message and exit
  --fakedomains thesprawl.org,google.com
                        A comma separated list of domain names which will be
                        resolved to FAKE values specified in the the above
                        parameters. All other domain names will be resolved to
                        their true values.
  --truedomains thesprawl.org,google.com
                        A comma separated list of domain names which will be
                        resolved to their TRUE values. All other domain names
                        will be resolved to fake values specified in the above
                        parameters.
Fake DNS records::
  --fakeip 192.0.2.1    IP address to use for matching DNS queries. If you use
                        this parameter without specifying domain names, then
                        all 'A' queries will be spoofed. Consider using --file
                        argument if you need to define more than one IP
                        address.
  --fakeipv6 2001:db8::1
                        IPv6 address to use for matching DNS queries. If you
                        use this parameter without specifying domain names,
                        then all 'AAAA' queries will be spoofed. Consider
                        using --file argument if you need to define more than
                        one IPv6 address.
  --fakemail mail.fake.com
                        MX name to use for matching DNS queries. If you use
                        this parameter without specifying domain names, then
                        all 'MX' queries will be spoofed. Consider using
                        --file argument if you need to define more than one MX
                        record.
  --fakealias www.fake.com
                        CNAME name to use for matching DNS queries. If you use
                        this parameter without specifying domain names, then
                        all 'CNAME' queries will be spoofed. Consider using
                        --file argument if you need to define more than one
                        CNAME record.
  --fakens ns.fake.com  NS name to use for matching DNS queries. If you use
                        this parameter without specifying domain names, then
                        all 'NS' queries will be spoofed. Consider using
                        --file argument if you need to define more than one NS
                        record.
  --file FILE           Specify a file containing a list of DOMAIN=IP pairs
                        (one pair per line) used for DNS responses. For
                        example: google.com=1.1.1.1 will force all queries to
                        'google.com' to be resolved to '1.1.1.1'. IPv6
                        addresses will be automatically detected. You can be
                        even more specific by combining --file with other
                        arguments. However, data obtained from the file will
                        take precedence over others.
Optional runtime parameters.:
  --logfile FILE        Specify a log file to record all activity
  --nameservers 8.8.8.8#53 or 4.2.2.1#53#tcp or 2001:4860:4860::8888
                        A comma separated list of alternative DNS servers to
                        use with proxied requests. Nameservers can have either
                        IP or IP#PORT format. A randomly selected server from
                        the list will be used for proxy requests when provided
                        with multiple servers. By default, the tool uses
                        Google's public DNS server 8.8.8.8 when running in
                        IPv4 mode and 2001:4860:4860::8888 when running in
                        IPv6 mode.
  -i, --interface 127.0.0.1 or ::1
                        Define an interface to use for the DNS listener. By
                        default, the tool uses 127.0.0.1 for IPv4 mode and ::1
                        for IPv6 mode.
  -t, --tcp             Use TCP DNS proxy instead of the default UDP.
  -6, --ipv6            Run in IPv6 mode.
  -p, --port 53         Port number to listen for DNS requests.
  -q, --quiet           Don't show headers.
Updated on: 2025-Dec-09
 Edit this page
dns2tcp
dnsenum
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install dnschef`，再执行 `dnschef --version` 2>/dev/null || `dnschef -V`
- [ ] **2.** **读官方帮助** —— `dnschef -h`，需要细节时 `man dnschef`
- [ ] **3.** **在自有靶场跑最小用例** —— 用 `dnschef -h` 里最简单的那个子命令试一次
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/dnschef/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/discovery.md`](../../tools/by-attack/discovery.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/dnschef/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/dnschef/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
