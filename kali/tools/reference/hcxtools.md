# hcxtools

> Tools for converting captures to use with hashcat or John the Ripper Portable solution for capturing wlan traffic and conversion to hashcat formats (recommended by hashcat) and to John the Ripper formats. hcx stands for: h = hash c = captu…

> **功能分类**：通用工具 ｜ **Kali 包**：`hcxtools` ｜ **官方文档**：<https://www.kali.org/tools/hcxtools/>

## 1. 安装

```bash
sudo apt update
sudo apt install hcxtools
```

| 项目 | 内容 |
|------|------|
| 版本 | 7.1.2 |
| 架构 | any |
| 可执行命令 | `hcxtools`、`hcxeiutool`、`hcxhash2cap`、`hcxhashtool`、`hcxpcapngtool`、`hcxpmktool`、`hcxpottool`、`hcxpsktool`、`hcxwltool`、`whoismac`、`wlancap2wpasec` |
| 依赖 | `ieee-data`、`libc6`、`libcurl4t64`、`libssl3t64`、`zlib1g`、`hcxeiutool` |
| 安装体积 | 636 KB |
| 官网 | <https://github.com/ZerBea/hcxtools> |
| 源码仓库 | <https://salsa.debian.org/pkg-security-team/hcxtools> |
| 包追踪 | <https://pkg.kali.org/pkg/hcxtools> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
hcxtools -h          # 查看用法
man hcxtools         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 11 个可执行命令，下面是官方页面内嵌的帮助原文。

### `hcxeiutool`

官方给出的调用示例：`hcxeiutool -h`

```text
root@kali:~# hcxeiutool -h
hcxeiutool 7.1.2 (C) 2026 ZeroBeat
usage:
hcxeiutool <options>
options:
-i <file> : input wordlist
-d <file> : output digit wordlist
-x <file> : output xdigit wordlist
-c <file> : output character wordlist (A-Za-z - other characters removed)
-s <file> : output character wordlist (A-Za-z - other characters replaced by 0x0a)
            recommended option for processing with rules
-h        : show this help
-v        : show version
--help           : show this help
--version        : show version
example:
$ hcxdumptool -i <interface> -w dump.pcapng
$ hcxpcapngtool -o hash.22000 -E elist dump.pcapng
$ hcxeiutool -i elist -d digitlist -x xdigitlist -c charlist -s sclist
$ cat elist digitlist xdigitlist charlist sclist > wordlisttmp
$ hashcat --stdout -r <rule> charlist >> wordlisttmp
$ hashcat --stdout -r <rule> sclist >> wordlisttmp
$ cat wordlisttmp | sort | uniq > wordlist
$ hashcat -m 22000 hash.22000 wordlist
```

### `hcxhash2cap`

官方给出的调用示例：`hcxhash2cap -h`

```text
root@kali:~# hcxhash2cap -h
hcxhash2cap 7.1.2 (C) 2026 ZeroBeat
usage:
hcxhash2cap <options>
options:
-c <file> : output cap file
            if no cap file is selected, output will be written to single cap files
            format: mac_sta.cap (mac_sta.cap_x)
-h        : show this help
-v        : show version
--pmkid-eapol=<file> : input PMKID EAPOL (22000) combi hash file
--pmkid=<file>       : input deprecated PMKID (16800) hash file
--hccapx=<file>      : input deprecated hccapx (2500) hash file
--hccap=<file>       : input ancient hccap (2500) file
--john=<file>        : input John the Ripper WPAPSK hash file
--help               : show this help
--version            : show version
Important notice:
Conversion from a dump file to a hash file is not loss less.
Hash files that contain EAPOL M3 MESSAGEs can't be converted back to a cap file.
```

### `hcxhashtool`

官方给出的调用示例：`hcxhashtool -h`

```text
root@kali:~# hcxhashtool -h
hcxhashtool 7.1.2 (C) 2026 ZeroBeat
usage:
hcxhashtool <options>
options:
-i <file>   : input PMKID/EAPOL hash file
-o <file>   : output PMKID/EAPOL hash file
-E <file>   : output ESSID list (autohex enabled)
-E stdout   : output ESSID list to stdout (autohex enabled)
-L <file>   : output ESSID list (unfiltered and unsorted)
              useful in combination with hashcat -a9 option
-d          : download https://standards-oui.ieee.org/oui.txt
              and save to ~/.hcxtools/oui.txt
              internet connection required
-h          : show this help
-v          : show version
--essid-group                : convert to ESSID groups in working directory
                               full advantage of reuse of PBKDF2
                               not on old hash formats
--oui-group                  : convert to OUI groups in working directory
                               not on old hash formats
--mac-group-ap               : convert APs to MAC groups in working directory
                               not on old hash formats
--mac-group-client           : convert CLIENTs to MAC groups in working directory
                               not on old hash formats
--type=<digit>               : filter by hash type
                               bitmask:
                                1 = PMKID
                                2 = EAPOL
                               default PMKID and EAPOL (1+2=3)
--hcx-min=<digit>            : disregard hashes with occurrence lower than hcx-min/ESSID
--hcx-max=<digit>            : disregard hashes with occurrence higher than hcx-max/ESSID
--essid-len                  : filter by ESSID length
                               default ESSID length: 0...32
--essid-min                  : filter by ESSID minimum length
                               default ESSID minimum length: 0
--essid-max                  : filter by ESSID maximum length
                               default ESSID maximum length: 32
--essid=<ESSID>              : filter by ESSID
--essid-part=<part of ESSID> : filter by part of ESSID (case sensitive)
--essid-partx=<part of ESSID>: filter by part of ESSID (case insensitive)
                               locale and wide characters are ignored
--essid-list=<file>          : filter by ESSID file
--essid-regex=<regex>        : filter ESSID by regular expression
--mac-ap=<MAC>               : filter AP by MAC
                               format: 001122334455, 00:11:22:33:44:55, 00-11-22-33-44-55 (hex)
--mac-client=<MAC>           : filter CLIENT by MAC
                               format: 001122334455, 00:11:22:33:44:55, 00-11-22-33-44-55 (hex)
--mac-list=<file>            : filter by MAC file
                               format: 001122334455, 00:11:22:33:44:55, 00-11-22-33-44-55 (hex)
--mac-skiplist=<file>        : exclude MAC from file
                               format: 001122334455, 00:11:22:33:44:55, 00-11-22-33-44-55 (hex)
--oui-ap=<OUI>               : filter AP by OUI
                               format: 001122, 00:11:22, 00-11-22 (hex)
--oui-client=<OUI>           : filter CLIENT by OUI
                               format: 001122, 00:11:22, 00-11-22 (hex)
--vendor=<VENDOR>            : filter AP or CLIENT by (part of) VENDOR name
--vendor-ap=<VENDOR>         : filter AP by (part of) VENDOR name
--vendor-client=<VENDOR>     : filter CLIENT by (part of) VENDOR name
--authorized                 : filter EAPOL pairs by status authorized (M2M3, M3M4, M1M4)
--challenge                  : filter EAPOL pairs by status CHALLENGE (M1M2, M1M2ROGUE)
--rc                         : filter EAPOL pairs by replaycount status checked
--rc-not                     : filter EAPOL pairs by replaycount status not checked
--apless                     : filter EAPOL pairs by status M1M2ROGUE (M2 requested from CLIENT)
--info=<file>                : output detailed information about content of hash file
                               no filter options available
--info=stdout                : stdout output detailed information about content of hash file
                               no filter options available
--info-vendor=<file>         : output detailed information about ACCESS POINT and CLIENT VENDORs
                               no filter options available
--info-vendor-ap=<file>      : output detailed information about ACCESS POINT VENDORs
                               no filter options available
--info-vendor-client=<file>  : output detailed information about CLIENT VENDORs
                               no filter options available
--info-vendor=stdout         : stdout output detailed information about ACCESS POINT and CLIENT VENDORs
                               no filter options available
--info-vendor-ap=stdout      : stdout output detailed information about ACCESS POINT VENDORs
                               no filter options available
--info-vendor-client=stdout  : stdout output detailed information about CLIENT VENDORs
                               no filter options available
--psk=<PSK>                  : pre-shared key to test
                               due to PBKDF2 calculation this is a very slow process
                               no nonce error corrections
--pmk=<PMK>                  : plain master key to test
                               no nonce error corrections
--hccapx-in=<file>           : input deprecated hccapx file
                                MESSSAGEPAIR is taken from the hccapx source
--hccapx-out=<file>          : output to deprecated hccapx file
--hccap-in=<file>            : input ancient hccap file
--hccap-out=<file>           : output to ancient hccap file
                                MESSSAGEPAIR is calculated from the EAPOL MESSAGE
                                due to missing information, the worst case value is calculated
--hccap-single               : output to ancient hccap single files (MAC + count)
--john=<file>                : output to deprecated john file
--vendorlist                 : stdout output complete OUI list sorted by OUI
--help                       : show this help
--version                    : show version
Important notice:
hcxhashtool does not do NONCE ERROR CORRECTIONS
in case of a packet loss, you get a wrong PTK
```

### `hcxpcapngtool`

官方给出的调用示例：`hcxpcapngtool -h`

```text
root@kali:~# hcxpcapngtool -h
hcxpcapngtool 7.1.2 (C) 2026 ZeroBeat
convert pcapng, pcap and cap files to hash formats that hashcat and JtR use
usage:
hcxpcapngtool <options>
hcxpcapngtool <options> input.pcapng
hcxpcapngtool <options> *.pcapng
hcxpcapngtool <options> *.pcap
hcxpcapngtool <options> *.cap
hcxpcapngtool <options> *.*
short options:
-o <file> : output WPA-PBKDF2-PMKID+EAPOL hash file (hashcat -m 22000)
            get full advantage of reuse of PBKDF2 on PMKID and EAPOL
-E <file> : output wordlist (autohex enabled on non ASCII characters) to use as input wordlist for cracker
            retrieved from every frame that contain an ESSID
-R <file> : output wordlist (autohex enabled on non ASCII characters) to use as input wordlist for cracker
            retrieved from PROBEREQUEST frames only
-I <file> : output unsorted identity list to use as input wordlist for cracker
-U <file> : output unsorted username list to use as input wordlist for cracker
-D <file> : output device information list
            format MAC MANUFACTURER MODELNAME SERIALNUMBER DEVICENAME UUID ESSID
-h        : show this help
-v        : show version
long options:
--all                              : convert all possible hashes instead of only the best one
                                     that can lead to much overhead hashes
                                     use hcxhashtool to filter hashes
                                     need hashcat --nonce-error-corrections >= 8
--eapoltimeout=<digit>             : set EAPOL TIMEOUT (milliseconds)
                                   : default: 5000 ms
--nonce-error-corrections=<digit>  : set nonce error correction
                                     warning: values > 0 can lead to uncrackable handshakes
                                   : default: 0
--ignore-ie                        : do not use CIPHER and AKM information
                                     this will convert all frames regadless of
                                     CIPHER and/OR AKM information,
                                     and can lead to uncrackable hashes
--max-essids=<digit>               : maximum allowed ESSIDs
                                     default: 1 ESSID
                                     disregard ESSID changes and take ESSID with highest ranking
--eapmd5=<file>                    : output EAP MD5 CHALLENGE (hashcat -m 4800)
--eapmd5-john=<file>               : output EAP MD5 CHALLENGE (john chap)
--eapleap=<file>                   : output EAP LEAP and MSCHAPV2 CHALLENGE (hashcat -m 5500, john netntlm)
--tacacs-plus=<file>               : output TACACS PLUS v1 (hashcat -m 16100, john tacacs-plus)
--nmea-in=<file>                   : input NME 0183 file
                                     to convert gpx to NMEA 0183, use GPSBabel:
                                     gpsbabel -w -t -i gpx -f in_file.gpx -o nmea -F out_file.nmea
--nmea-out=<file>                  : output GPS data in NMEA 0183 format
                                     format: NMEA 0183 $GPGGA, $GPRMC, $GPWPL
                                     to convert it to gpx, use GPSBabel:
                                     gpsbabel -i nmea -f hcxdumptool.nmea -o gpx,gpxver=1.1 -F hcxdumptool.gpx
                                     to display the track, open file.gpx with viking
--csv=<file>                       : output ACCESS POINT information in CSV format
                                     delimiter: tabulator (0x08)
                                     columns:
                                     YYYY-MM-DD HH:MM:SS MAC_AP ESSID ENC_TYPE CIPHER AKM COUNTRY_INFO CHANNEL RSSI GPS(DM.m) GPS(D.d) GPSFIX SATCOUNT HDOP ALTITUDE UNIT
                                     GPS FIX:
                                     0 = fix not available or invalid
                                     1 = fix valid (GPS SPS mode)
                                     2 = fix valid (differential GPS SPS Mode)
                                     3 = not supported
                                     4 = not supported
                                     5 = not supported
                                     6 = fix valid (Dead Reckoning Mode)
                                     to convert it to other formats, use bash tools or scripting languages
--log=<file>                       : output logfile
--raw-out=<file>                   : output frames in HEX ASCII
                                   : format: TIMESTAMP*LINKTYPE*FRAME*CHECKSUM
--raw-in=<file>                    : input frames in HEX ASCII
                                   : format: TIMESTAMP*LINKTYPE*FRAME*CHECKSUM
--lts=<file>                       : output BSSID list to sync with external GPS data
                                     format: LINUX timestamp <tab> RSSI <tab> MAC_AP <tab> ESSID
--pmkid-client=<file>              : output WPA-(MESH/REPEATER)-PMKID hash file (hashcat -m 22000)
--pmkid=<file>                     : output deprecated PMKID file (delimiter *)
--hccapx=<file>                    : output deprecated hccapx v4 file
--hccap=<file>                     : output deprecated hccap file
--john=<file>                      : output deprecated PMKID/EAPOL (JtR wpapsk-opencl/wpapsk-pmk-opencl)
--prefix=<file>                    : convert everything to lists using this prefix (overrides single options):
                                      -o <file.22000>           : output PMKID/EAPOL hash file
                                      -E <file.essid>           : output wordlist (autohex enabled on non ASCII characters) to use as input wordlist for cracker
                                      -I <file.identity>        : output unsorted identity list to use as input wordlist for cracker
                                      -U <file.username>        : output unsorted username list to use as input wordlist for cracker
                                     --eapmd5=<file.4800>       : output EAP MD5 CHALLENGE (hashcat -m 4800)
                                     --eapleap=<file.5500>      : output EAP LEAP and MSCHAPV2 CHALLENGE (hashcat -m 5500, john netntlm)
                                     --tacacs-plus=<file.16100> : output TACACS+ (hashcat -m 16100, john tacacs-plus)
                                     --nmea=<file.nmea>         : output GPS data in NMEA 0183 format
--add-timestamp                    : add date/time and EAPOL TIME gap (time between two EAPOL MESSAGEs in nsec) to hash line
                                     this must be filtered out before feeding hashcat with the hash, e.g. by awk:
                                     cat hash.hc22000 | awk '{print $1}' > hashremovedtimestamp.hc22000
--help                             : show this help
--version                          : show version
bitmask of PMKID hash line (WPA*01) message pair field:
0: reserved
1: PMKID taken from AP
2: PMKID taken from AP possible PSKSHA256 FT using PSK
3: reserved
4: PMKID taken from CLIENT (wlan.da: possible MESH or REPEATER)
5: reserved
6: reserved
7: reserved
bitmask of EAPOL hash line (WPA*02) message pair field:
2,1,0:
 000 = M1+M2, EAPOL from M2 (challenge - ANONCE from M1)
 001 = M1+M4, EAPOL from M4 (authorized) - usable if NONCE_CLIENT is not zeroed
 010 = M2+M3, EAPOL from M2 (authorized - ANONCE from M3)
 011 = M2+M3, EAPOL from M3 (authorized) - usable by option --all
 100 = M3+M4, EAPOL from M3 (authorized) - usable by option --all
 101 = M3+M4, EAPOL from M4 (authorized) - usable if NONCE_CLIENT is not zeroed
3: reserved
4: NC (set to 1) - nonce-error-corrections deactivated on M1M2ROGUE, M2M3E3 and M3M4E3
5: LE router detected (set to 1) - nonce-error-corrections required only on LE
6: BE router detected (set to 1) - nonce-error-corrections required only on BE
7: NC (set to 1) - nonce-error-corrections activated
Do not edit, merge or convert pcapng files! This will remove optional comment fields!
Detection of bit errors does not work on cleaned dump files!
Do not use hcxpcapngtool in combination with third party cap/pcap/pcapng cleaning tools (except: tshark and/or Wireshark)!
It is much better to run gzip to compress the files. Wireshark, tshark and hcxpcapngtool will understand this.
Output is appended to existing files.
Recommended tools to show additional 802.11 fields or to decrypt WiFi traffic: Wireshark and/or tshark
Recommended tool to filter converted hash by several options: hcxhashtool
Recommended tool to get default or standard PSKs: hcxpsktool
Recommended tool to calculate wordlists based on ESSID: hcxeiutool
Recommended tools to retrieve PSK from hash: hashcat, JtR
```

### `hcxpmktool`

官方给出的调用示例：`hcxpmktool -h`

```text
root@kali:~# hcxpmktool -h
hcxpmktool 7.1.2  (C) 2026 ZeroBeat
usage  : hcxpmktool <options>
short options:
-l <hash line> : input hashcat hash line (-m 22000)
-e <ESSID>     : input Network Name (ESSID)
-p <PSK>       : input Pre Shared Key (PSK) or Plain Master Key (PMK)
-p -           : read Pre Shared Key (PSK) from stdin
               : small lists only
long options:
--help         : show this help
--version      : show version
exit codes:
0 = PSK/PMK confirmed
1 = ERROR occurred
2 = PSK/PMK unconfirmed
Important notice:
hcxpmktool does not do NONCE ERROR CORRECTIONS
in case of a packet loss, you get a wrong PTK
```

### `hcxpottool`

官方给出的调用示例：`hcxpottool -h`

```text
root@kali:~# hcxpottool -h
hcxpottool 7.1.2  (C) 2026 ZeroBeat
usage  : hcxpottool <options>
short options:
-h                   : show this help
-v                   : show version
long options:
--hcpotin=<file>     : input potfile in hashcat pot file format
                        format: PMK*ESSID:PSK
--hcoutin=<file>     : input outfile in hashcat out file format
                        format: MIC/PMKID:MAC_AP:MAC_CLIENT:ESSID:PSK
                        verify/calculate plain master keys enabled by default
--jtrpotin=<file>    : input potfile in john pot file format
                        format: $pbkdf2-hmac-sha1$ESSID$PMK:PSK
--hcpotout=<file>    : output potfile in hashcat format
                        hexified characters < 0x20
                        hexified characters > 0x7e
                        hexified delimiter :
--hcpbkdf2out=<file> : output hashcat hash file format 12000
--jtrpbkdf2out=<file>: output john hash file format PBKDF2-HMAC-SHA1-opencl / PBKDF2-HMAC-SHA1
--tabin=<file>       : input tabulator separated file
                        format: PMK <tab> ESSID <tab> PSK
                        verify/calculate plain master keys enabled by default
--tabout=<file>      : output tabulator separated file
                        hexified characters < 0x21
                        hexified characters > 0x7e
--tabspout=<file>    : output tabulator separated file
                        hexified characters < 0x20
                        hexified characters > 0x7e
--tabnhout=<file>    : output tabulator separated file
                        hexified characters < 0x20
                        use with care
--faultyout=<file>   : output faulty lines file
--pmkoff             : disable verification/calculation of plain master keyss
--help               : show this help
--version            : show version
```

### `hcxpsktool`

官方给出的调用示例：`hcxpsktool -h`

```text
root@kali:~# hcxpsktool -h
hcxpsktool 7.1.2 (C) 2026 ZeroBeat
usage:
hcxpsktool <options>
options:
-c <file>   : input PMKID/EAPOL hash file (hashcat -m 22000/22001)
-i <file>   : input EAPOL hash file (hashcat -m 2500/2501)
-j <file>   : input EAPOL hash file (john)
-z <file>   : input PMKID hash file (hashcat -m 16800/16801 and john)
-e <char>   : input ESSID
-b <xdigit> : input MAC access point
              format: 112233445566
-o <file>   : output PSK file
              default: stdout
              output list must be sorted unique!
-h          : show this help
-v          : show version
--maconly           : print only candidates based on ACCESS POINT MAC
--noessidcombination: exclude ESSID combinations
--netgear           : include weak NETGEAR / ORBI / NTGR_VMB / ARLO_VMB / FoxtelHub candidates
--spectrum          : include weak MySpectrumWiFi / SpectrumSetup / MyCharterWiFi candidates
                      list will be > 3.3GB
--digit10           : include weak 10 digit candidates (INFINITUM, ALHN, INEA, VodafoneNet, VIVACOM)
                      list will be > 1GB
--phome             : include weak PEGATRON / Vantiva candidates (CBCI, HOME, [SP/XF]SETUP)
                      list will be > 2.9GB
--tenda             : include weak Tenda / NOVA / NOVE / BrosTrend candidates
--ee                : include weak 5GHz-EE / BrightBox / EE / EE-BrightBox candidates
                      list will be > 1.4GB
--eeupper           : include weak EE-Hub candidates
                      list will be > 4.0GB
--alticeoptimum     : include weak Altice/Optimum candidates (MyAltice, MyOptimum)
                      list will be > 6.3GB
--asus              : include weak ASUS RT-AC candidates (ASUS_XX, RT-AC)
--weakpass          : include weak password candidates
--eudate            : include complete european dates
--usdate            : include complete american dates
--wpskeys           : include complete WPS keys
--egn               : include Bulgarian EGN
--simple            : include simple pattern
--help              : show this help
--version           : show version
if hcxpsktool recovered your password, you should change it immediately!
```

### `hcxwltool`

官方给出的调用示例：`hcxwltool -h`

```text
root@kali:~# hcxwltool -h
hcxwltool 7.1.2 (C) 2026 ZeroBeat
usage:
hcxwltool <options>
options:
-i <file> : input wordlist
-o <file> : output wordlist to file
-h        : show this help
-v        : show version
--straight       : output format untouched
--digit          : output format only digits
--xdigit         : output format only xdigits
--lower          : output format only lower
--upper          : output format only upper
--capital        : output format only capital
--length=<digit> : password length (8...32)
--help           : show this help
--version        : show version
examples:
hcxwltool -i wordlist --straight | sort | uniq | hashcat -m 22000 hashfile.hc22000
hcxwltool -i wordlist --digit --length=10 | sort | uniq | hashcat -m 22000 hashfile.hc22000
hcxwltool -i wordlist --digit | sort | uniq | hashcat -m 22000 hashfile.hc22000
hcxwltool -i wordlist --xdigit | sort | uniq | john --stdin --format=wpapsk-opencl john.hashfile
```

### `whoismac`

官方给出的调用示例：`whoismac -h`

```text
root@kali:~# whoismac -h
whoismac 7.1.2 (C) 2026 ZeroBeat
usage: whoismac <options>
options:
-d            : download https://standards-oui.ieee.org/oui/oui.txt
              : and save to ~/.hcxtools/oui.txt
              : internet connection required
-m <mac>      : mac (six bytes of mac addr) or
              : oui (fist three bytes of mac addr)
-p <hashline> : input PMKID and/or EAPOL hashline (hashmode 22000 or 16800)
-P <hashline> : input EAPOL hashline from potfile (hashcat <= 5.1.0)
-e <ESSID>    : input ESSID
-x <xdigit>   : input ESSID in hex
-v <vendor>   : vendor name
-h            : this help screen
```

### `wlancap2wpasec`

官方给出的调用示例：`wlancap2wpasec -h`

```text
root@kali:~# wlancap2wpasec -h
wlancap2wpasec 7.1.2 (C) 2026 ZeroBeat
usage: wlancap2wpasec <options>  [input.pcapng] [input.pcap] [input.cap] [input.pcapng.gz]...
       wlancap2wpasec <options> *.pcapng
       wlancap2wpasec <options> *.gz
       wlancap2wpasec <options> *.*
options:
-k <key>           : wpa-sec user key
-u <url>           : set user defined URL
                     default = https://wpa-sec.stanev.org
-t <seconds>       : set connection timeout
                     default = 30 seconds
-e <email address> : set email address, if required
-R                 : remove cap if upload was successful
-h                 : this help
-v                 : show version
Do not merge different cap files to a single cap file.
This will lead to unexpected behaviour on ESSID changes
or different link layer types.
To remove unnecessary packets, run tshark:
tshark -r input.cap -R "(wlan.fc.type_subtype == 0x00 || wlan.fc.type_subtype == 0x02 || wlan.fc.type_subtype == 0x04 || wlan.fc.type_subtype == 0x05 || wlan.fc.type_subtype == 0x08 || eapol)" -2 -F pcapng -w output.pcapng
To reduce the size of the cap file, compress it with gzip:
gzip capture.pcapng
Learn more with
OffSec
Want to learn more about hcxtools? get access to in-depth training and hands-on labs:
PEN-210: 7.3.5. Cracking Authentication Hashes: Passphrase Cracking with Hashcat
PEN-210 course
Updated on: 2026-Aug-25
 Edit this page
gvm
heartleech
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install hcxtools`，再执行 `hcxtools --version` 2>/dev/null || `hcxtools -V`
- [ ] **2.** **读官方帮助** —— `hcxtools -h`，需要细节时 `man hcxtools`
- [ ] **3.** **在自有靶场跑最小用例** —— 用 `hcxtools -h` 里最简单的那个子命令试一次
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/hcxtools/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/hcxtools/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/hcxtools/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
