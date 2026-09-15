# aircrack-ng

> Wireless WEP/WPA cracking utilities aircrack-ng is an 802.11a/b/g WEP/WPA cracking program that can recover a 40-bit, 104-bit, 256-bit or 512-bit WEP key once enough encrypted packets have been gathered. Also it can attack WPA1/2 networks …

> **功能分类**：无线攻击 ｜ **Kali 包**：`aircrack-ng` ｜ **官方文档**：<https://www.kali.org/tools/aircrack-ng/>

## 1. 安装

```bash
sudo apt update
sudo apt install aircrack-ng
```

| 项目 | 内容 |
|------|------|
| 版本 | 1.7 |
| 架构 | any |
| 可执行命令 | `aircrack-ng`、`airbase-ng`、`airdecap-ng`、`airdecloak-ng`、`aireplay-ng`、`airmon-ng`、`airodump-ng`、`airodump-ng-oui-update`、`airolib-ng`、`airserv-ng`、`airtun-ng`、`airventriloquist-ng`、`besside-ng`、`besside-ng-crawler`、`buddy-ng`、`dcrack`、`easside-ng`、`ivstools`、`kstats`、`makeivs-ng`、`packetforge-ng`、`tkiptun-ng`、`wesside-ng`、`wpaclean`、`airgraph-ng`、`airodump-join` |
| 依赖 | `ethtool`、`hwloc`、`iw`、`libc6`、`libgcc-s1`、`libhwloc15`、`libnl-3-200`、`libnl-genl-3-200`、`libpcap0.8t64`、`libpcre2-8-0`、`libsqlite3-0`、`libssl3t64` 等 |
| 安装体积 | 2.47 MB |
| 官网 | <https://www.aircrack-ng.org/> |
| 源码仓库 | <https://salsa.debian.org/pkg-security-team/aircrack-ng> |
| 包追踪 | <https://pkg.kali.org/pkg/aircrack-ng> |

## 2. 官方用法示例

> 以下为 Kali 官方工具页给出的示例与输出原文。

```text
Usage Examples
WPA Wordlist Mode
Specify the wordlist to use (-w password.lst) and the path to the capture file (wpa.cap) containing at least one 4-way handshake.
root@kali:~# aircrack-ng -w password.lst wpa.cap

                               Aircrack-ng 1.5.2

      [00:00:00] 232/233 keys tested (1992.58 k/s)

      Time left: 0 seconds                                      99.57%

                           KEY FOUND! [ biscotte ]


      Master Key     : CD D7 9A 5A CF B0 70 C7 E9 D1 02 3B 87 02 85 D6
                       39 E4 30 B3 2F 31 AA 37 AC 82 5A 55 B5 55 24 EE

      Transient Key  : 33 55 0B FC 4F 24 84 F4 9A 38 B3 D0 89 83 D2 49
                       73 F9 DE 89 67 A6 6D 2B 8E 46 2C 07 47 6A CE 08
                       AD FB 65 D6 13 A9 9F 2C 65 E4 A6 08 F2 5A 67 97
                       D9 6F 76 5B 8C D3 DF 13 2F BC DA 6A 6E D9 62 CD

      EAPOL HMAC     : 28 A8 C8 95 B7 17 E5 72 27 B6 A7 EE E3 E5 34 45

Basic WEP Cracking
To have aircrack-ng conduct a WEP key attack on a capture file, pass it the filename, either in .ivs or .cap/.pcap format:
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 26 个可执行命令，下面是官方页面内嵌的帮助原文。

### `aircrack-ng`

官方给出的调用示例：`aircrack-ng -w password.lst wpa.cap`

```text
root@kali:~# aircrack-ng -w password.lst wpa.cap
                               Aircrack-ng 1.5.2
      [00:00:00] 232/233 keys tested (1992.58 k/s)
      Time left: 0 seconds                                      99.57%
                           KEY FOUND! [ biscotte ]
      Master Key     : CD D7 9A 5A CF B0 70 C7 E9 D1 02 3B 87 02 85 D6
                       39 E4 30 B3 2F 31 AA 37 AC 82 5A 55 B5 55 24 EE
      Transient Key  : 33 55 0B FC 4F 24 84 F4 9A 38 B3 D0 89 83 D2 49
                       73 F9 DE 89 67 A6 6D 2B 8E 46 2C 07 47 6A CE 08
                       AD FB 65 D6 13 A9 9F 2C 65 E4 A6 08 F2 5A 67 97
                       D9 6F 76 5B 8C D3 DF 13 2F BC DA 6A 6E D9 62 CD
      EAPOL HMAC     : 28 A8 C8 95 B7 17 E5 72 27 B6 A7 EE E3 E5 34 45
Basic WEP Cracking
To have aircrack-ng conduct a WEP key attack on a capture file, pass it the filename, either in .ivs or .cap/.pcap format:
```

### `aircrack-ng（示例）`

官方给出的调用示例：`aircrack-ng all-ivs.ivs`

```text
root@kali:~# aircrack-ng all-ivs.ivs
                                   Aircrack-ng 1.4
                   [00:00:00] Tested 1514 keys (got 30566 IVs)
   KB    depth   byte(vote)
    0    0/  9   1F(39680) 4E(38400) 14(37376) 5C(37376) 9D(37376)
    1    7/  9   64(36608) 3E(36352) 34(36096) 46(36096) BA(36096)
    2    0/  1   1F(46592) 6E(38400) 81(37376) 79(36864) AD(36864)
    3    0/  3   1F(40960) 15(38656) 7B(38400) BB(37888) 5C(37632)
    4    0/  7   1F(39168) 23(38144) 97(37120) 59(36608) 13(36352)
                         KEY FOUND! [ 1F:1F:1F:1F:1F ]
    Decrypted correctly: 100%
airgraph-ng Usage Examples
CAPR graph
Specify the input file to use (
-i dump-01.csv
), the output file to generate (
-o capr.png
) and the graph type (
-g CAPR
):
```

### `airgraph-ng`

官方给出的调用示例：`airgraph-ng -i dump-01.csv -o capr.png -g CAPR`

```text
root@kali:~# airgraph-ng -i dump-01.csv -o capr.png -g CAPR
**** WARNING Images can be large, up to 12 Feet by 12 Feet****
Creating your Graph using, dump-01.csv and writing to, capr.png
Depending on your system this can take a bit. Please standby......
CPG graph
Specify the input file to use (
-i dump-01.csv
), the output file to generate (
-o cpg.png
) and the graph type (
-g CAG
):
```

### `airgraph-ng（示例）`

官方给出的调用示例：`airgraph-ng -i dump-01.csv -o cpg.png -g CPG`

```text
root@kali:~# airgraph-ng -i dump-01.csv -o cpg.png -g CPG
**** WARNING Images can be large, up to 12 Feet by 12 Feet****
Creating your Graph using, dump-01.csv and writing to, cpg.png
Depending on your system this can take a bit. Please standby......
wpaclean Usage Example
Parse the provided capture files (
wpa-psk-linksys.cap wpa.cap
) and save any 4-way handshakes to a new file (
/root/handshakes.cap
):
root@kali:/usr/share/doc/aircrack-ng/examples# wpaclean /root/handshakes.cap wpa-psk-linksys.cap wpa.cap
Pwning wpa-psk-linksys.cap (1/2 50%)
Net 00:0b:86:c2:a4:85 linksys
Pwning wpa.cap (2/2 100%)
Net 00:0d:93:eb:b0:8c test
Done
wesside-ng Usage Example
Use the specified monitor mode interface (
-i wlan0mon
) and target a single BSSID (
-v de:ad:be:ef:ca:fe
):
```

### `wesside-ng`

官方给出的调用示例：`wesside-ng -i wlan0mon -v de:ad:be:ef:ca:fe`

```text
root@kali:~# wesside-ng -i wlan0mon -v de:ad:be:ef:ca:fe
[18:31:52] Using mac 3C:46:D8:4E:EF:AA
[18:31:52] Looking for a victim...
[18:32:13] Chan 04 -
makeivs-ng Usage Example
Specify a BSSID (
-b de:ad:be:ef:ca:fe
), WEP key (
-k 123456789ABCDEF123456789AB
), and output filename (
-w makeivs.ivs
):
```

### `makeivs-ng`

官方给出的调用示例：`makeivs-ng -b de:ad:be:ef:ca:fe -k 123456789ABCDEF123456789AB -w makeivs.ivs`

```text
root@kali:~# makeivs-ng -b de:ad:be:ef:ca:fe -k 123456789ABCDEF123456789AB -w makeivs.ivs
Creating 100000 IVs with 16 bytes of keystream each.
Estimated filesize: 2.29 MB
Using fake BSSID DE:AD:BE:EF:CA:FE
Done.
```

### `aircrack-ng（示例）`

官方给出的调用示例：`aircrack-ng makeivs.ivs`

```text
root@kali:~# aircrack-ng makeivs.ivs
Opening makeivs.ivs
Read 100001 packets.
   #  BSSID              ESSID                     Encryption
   1  DE:AD:BE:EF:CA:FE                            WEP (100000 IVs)
Choosing first network as target.
Opening makeivs.ivs
Attack will be restarted every 5000 captured ivs.
Starting PTW attack with 100000 ivs.
                                   Aircrack-ng 1.2 rc4
                   [00:00:00] Tested 621 keys (got 100000 IVs)
   KB    depth   byte(vote)
    0    1/  2   76(113152) 1E(111104) 48(109824) 1C(109568) A6(109568)
    1    1/  3   F5(112640) 06(111616) 33(111616) F4(111616) 05(111104)
    2    0/  2   31(137216) F9(113664) 76(113152) DC(110336) B9(109568)
    3   10/  3   E1(108800) 0A(108544) 34(108032) 3E(108032) 48(108032)
    4    9/  4   7D(109312) BA(109056) 5E(108800) D6(108800) 11(108288)
             KEY FOUND! [ 12:34:56:78:9A:BC:DE:F1:23:45:67:89:AB ]
    Decrypted correctly: 100%
ivstools Usage Examples
Strip out the initialization vectors of the provided .pcap capture and save them to a new file:
```

### `ivstools`

官方给出的调用示例：`ivstools --convert wep_64_ptw.cap out.ivs`

```text
root@kali:~# ivstools --convert wep_64_ptw.cap out.ivs
Opening wep_64_ptw.cap
Creating out.ivs
Read 65282 packets.
Written 30566 IVs.
Merge all .ivs files into one file.
```

### `ivstools（示例）`

官方给出的调用示例：`ivstools --merge *.ivs /root/all-ivs.ivs`

```text
root@kali:~# ivstools --merge *.ivs /root/all-ivs.ivs
Creating /root/all-ivs.ivs
Opening out.ivs
916996 bytes written
Opening out2.ivs
1374748 bytes written
easside-ng Usage Example
First, run buddy-ng, then launch the Easside-ng attack, specifying as many of the options as you can.
```

### `buddy-ng`

```text
root@kali:~# buddy-ng
Waiting for connexion
```

## 4. 实践清单

按顺序做完这五步，就能把工具从「装上」推进到「会用」：

- [ ] **1.** **装好并确认版本** —— `sudo apt install aircrack-ng`，再执行 `aircrack-ng --version` 2>/dev/null || `aircrack-ng -V`
- [ ] **2.** **读官方帮助** —— `aircrack-ng -h`，需要细节时 `man aircrack-ng`
- [ ] **3.** **在自有靶场跑最小用例** —— 用 `aircrack-ng -h` 里最简单的那个子命令试一次
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/aircrack-ng/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- **精讲教程**（含原理、参数详解、靶场实操与输出解读）：[aircrack-ng](../../tools/tutorials/05-无线攻击/aircrack-ng.md)
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/credential-access.md`](../../tools/by-attack/credential-access.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/aircrack-ng/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/aircrack-ng/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
