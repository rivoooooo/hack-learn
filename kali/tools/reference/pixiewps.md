# pixiewps

> Offline WPS bruteforce tool Pixiewps is a tool written in C used to bruteforce offline the WPS pin exploiting the low or non-existing entropy of some APs (pixie dust attack). It is meant for educational purposes only.

> **功能分类**：无线攻击 ｜ **Kali 包**：`pixiewps` ｜ **官方文档**：<https://www.kali.org/tools/pixiewps/>

## 1. 安装

```bash
sudo apt update
sudo apt install pixiewps
```

| 项目 | 内容 |
|------|------|
| 版本 | 1.4.2 |
| 架构 | any |
| 可执行命令 | `pixiewps` |
| 依赖 | `libc6` |
| 安装体积 | 118 KB |
| 官网 | <https://github.com/wiire/pixiewps> |
| 源码仓库 | <https://salsa.debian.org/pkg-security-team/pixiewps> |
| 包追踪 | <https://pkg.kali.org/pkg/pixiewps> |

## 2. 官方用法示例

> 以下为 Kali 官方工具页给出的示例与输出原文。

```text
Usage Example
root@kali:~# pixiewps \
>    -a 7f:de:11:b9:69:1c:de:26:4a:21:a4:6f:eb:3d:b8:aa:aa:d7:30:09:09:32:b8:24:43:9b:e0:91:78:e7:6f:2c \
>    -e d4:38:91:0d:4e:6e:15:fe:70:f0:97:a8:70:2a:b8:94:f5:75:74:bf:64:19:9f:92:82:9b:e0:2c:c0:a3:75:48:08:8f:63:0a:82:37:0c:b7:95:42:cf:55:ca:a5:f0:f7:6c:b2:c7:5f:0e:23:18:44:f4:2d:00:f1:da:d4:94:23:56:c7:2c:b0:f6:87:c7:77:d0:cc:11:35:cf:b7:4f:bc:44:8d:ca:35:8a:78:3d:99:7f:2b:cf:44:21:d8:e2:0f:3c:7d:a4:72:c8:03:6f:77:2a:e9:fa:c1:e9:a8:2c:74:65:99:5a:e0:a5:26:d9:23:5e:4e:ec:5a:07:07:ab:80:db:3f:5f:18:7f:fa:fa:f1:57:74:b2:8d:a9:97:a6:c6:0a:a5:e0:ec:93:09:23:67:f6:3e:ec:1f:55:32:a4:5d:73:8f:ab:91:74:cf:1d:79:85:12:c1:81:f5:ea:a6:68:9d:8e:c7:c6:be:01:dc:d9:f8:68:80:11:55:d7:44:6a \
>    -r bc:ad:54:2f:88:44:7c:12:69:ef:34:31:4a:17:1c:92:b1:d7:06:4c:73:be:9f:d3:ed:87:63:74:10:46:0f:46:8c:36:b5:d4:a0:ba:af:85:9c:b2:30:42:d7:59:43:75:5a:d7:79:96:fb:ee:7b:66:db:b7:a8:f9:22:9c:a5:d3:b8:e7:c0:c4:5c:58:34:1f:56:a8:1a:41:a8:d2:e8:f6:3e:c9:3a:93:d9:9b:59:5c:a8:e0:78:84:6c:fc:05:e8:76:a3:e6:3b:33:94:4a:a9:ff:50:fb:60:fa:97:3b:6d:cc:04:f1:5e:36:24:a9:06:7a:f8:6b:00:e9:71:9d:89:be:9c:b2:9c:1f:ca:6d:d6:4d:ab:46:3d:b3:11:1f:8d:40:f7:c8:a4:39:48:c5:ca:1b:f6:30:95:7d:d9:68:41:ef:0a:37:b2:4a:37:e4:a4:b0:dd:7e:c1:af:3e:66:ea:bf:16:0a:7a:8a:05:00:01:a4:29:77:a9:d4:81:d4:0e \
>    -s 90:5f:f5:7d:93:e5:c4:3c:62:0d:26:65:dd:59:57:d5:ba:ba:f1:b7:30:91:72:7c:54:94:38:08:1e:13:35:38 \
>    -z b0:2b:07:50:28:e7:6e:5f:fa:27:1b:31:92:85:43:cb:c5:6a:ec:73:e2:27:c3:b9:80:ec:5b:ed:88:f0:1e:ec \
>    -n 00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00

 Pixiewps 1.4

 [?] Mode:     1 (RT/MT/CL)
 [*] Seed N1:  -
 [*] Seed ES1: 0x00000000
 [*] Seed ES2: 0x00000000
 [*] PSK1:     d4eb0c2a3815e1a03d70db7431eb53a3
 [*] PSK2:     d3b7e623f31d220a23ea07bb7f76658b
 [*] ES1:      00000000000000000000000000000000
 [*] ES2:      00000000000000000000000000000000
 [+] WPS pin:  04847533

 [*] Time taken: 0 s 4 ms

root@kali:~#
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### ``

```text
root@kali:~#
">
    -a 7f:de:11:b9:69:1c:de:26:4a:21:a4:6f:eb:3d:b8:aa:aa:d7:30:09:09:32:b8:24:43:9b:e0:91:78:e7:6f:2c \
>    -e d4:38:91:0d:4e:6e:15:fe:70:f0:97:a8:70:2a:b8:94:f5:75:74:bf:64:19:9f:92:82:9b:e0:2c:c0:a3:75:48:08:8f:63:0a:82:37:0c:b7:95:42:cf:55:ca:a5:f0:f7:6c:b2:c7:5f:0e:23:18:44:f4:2d:00:f1:da:d4:94:23:56:c7:2c:b0:f6:87:c7:77:d0:cc:11:35:cf:b7:4f:bc:44:8d:ca:35:8a:78:3d:99:7f:2b:cf:44:21:d8:e2:0f:3c:7d:a4:72:c8:03:6f:77:2a:e9:fa:c1:e9:a8:2c:74:65:99:5a:e0:a5:26:d9:23:5e:4e:ec:5a:07:07:ab:80:db:3f:5f:18:7f:fa:fa:f1:57:74:b2:8d:a9:97:a6:c6:0a:a5:e0:ec:93:09:23:67:f6:3e:ec:1f:55:32:a4:5d:73:8f:ab:91:74:cf:1d:79:85:12:c1:81:f5:ea:a6:68:9d:8e:c7:c6:be:01:dc:d9:f8:68:80:11:55:d7:44:6a \
>    -r bc:ad:54:2f:88:44:7c:12:69:ef:34:31:4a:17:1c:92:b1:d7:06:4c:73:be:9f:d3:ed:87:63:74:10:46:0f:46:8c:36:b5:d4:a0:ba:af:85:9c:b2:30:42:d7:59:43:75:5a:d7:79:96:fb:ee:7b:66:db:b7:a8:f9:22:9c:a5:d3:b8:e7:c0:c4:5c:58:34:1f:56:a8:1a:41:a8:d2:e8:f6:3e:c9:3a:93:d9:9b:59:5c:a8:e0:78:84:6c:fc:05:e8:76:a3:e6:3b:33:94:4a:a9:ff:50:fb:60:fa:97:3b:6d:cc:04:f1:5e:36:24:a9:06:7a:f8:6b:00:e9:71:9d:89:be:9c:b2:9c:1f:ca:6d:d6:4d:ab:46:3d:b3:11:1f:8d:40:f7:c8:a4:39:48:c5:ca:1b:f6:30:95:7d:d9:68:41:ef:0a:37:b2:4a:37:e4:a4:b0:dd:7e:c1:af:3e:66:ea:bf:16:0a:7a:8a:05:00:01:a4:29:77:a9:d4:81:d4:0e \
>    -s 90:5f:f5:7d:93:e5:c4:3c:62:0d:26:65:dd:59:57:d5:ba:ba:f1:b7:30:91:72:7c:54:94:38:08:1e:13:35:38 \
>    -z b0:2b:07:50:28:e7:6e:5f:fa:27:1b:31:92:85:43:cb:c5:6a:ec:73:e2:27:c3:b9:80:ec:5b:ed:88:f0:1e:ec \
>    -n 00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00
 Pixiewps 1.4
 [?] Mode:     1 (RT/MT/CL)
 [*] Seed N1:  -
 [*] Seed ES1: 0x00000000
 [*] Seed ES2: 0x00000000
 [*] PSK1:     d4eb0c2a3815e1a03d70db7431eb53a3
 [*] PSK2:     d3b7e623f31d220a23ea07bb7f76658b
 [*] ES1:      00000000000000000000000000000000
 [*] ES2:      00000000000000000000000000000000
 [+] WPS pin:  04847533
 [*] Time taken: 0 s 4 ms
```

### ``

```text
root@kali:~#
">
    -a 7f:de:11:b9:69:1c:de:26:4a:21:a4:6f:eb:3d:b8:aa:aa:d7:30:09:09:32:b8:24:43:9b:e0:91:78:e7:6f:2c \
>    -e d4:38:91:0d:4e:6e:15:fe:70:f0:97:a8:70:2a:b8:94:f5:75:74:bf:64:19:9f:92:82:9b:e0:2c:c0:a3:75:48:08:8f:63:0a:82:37:0c:b7:95:42:cf:55:ca:a5:f0:f7:6c:b2:c7:5f:0e:23:18:44:f4:2d:00:f1:da:d4:94:23:56:c7:2c:b0:f6:87:c7:77:d0:cc:11:35:cf:b7:4f:bc:44:8d:ca:35:8a:78:3d:99:7f:2b:cf:44:21:d8:e2:0f:3c:7d:a4:72:c8:03:6f:77:2a:e9:fa:c1:e9:a8:2c:74:65:99:5a:e0:a5:26:d9:23:5e:4e:ec:5a:07:07:ab:80:db:3f:5f:18:7f:fa:fa:f1:57:74:b2:8d:a9:97:a6:c6:0a:a5:e0:ec:93:09:23:67:f6:3e:ec:1f:55:32:a4:5d:73:8f:ab:91:74:cf:1d:79:85:12:c1:81:f5:ea:a6:68:9d:8e:c7:c6:be:01:dc:d9:f8:68:80:11:55:d7:44:6a \
>    -r bc:ad:54:2f:88:44:7c:12:69:ef:34:31:4a:17:1c:92:b1:d7:06:4c:73:be:9f:d3:ed:87:63:74:10:46:0f:46:8c:36:b5:d4:a0:ba:af:85:9c:b2:30:42:d7:59:43:75:5a:d7:79:96:fb:ee:7b:66:db:b7:a8:f9:22:9c:a5:d3:b8:e7:c0:c4:5c:58:34:1f:56:a8:1a:41:a8:d2:e8:f6:3e:c9:3a:93:d9:9b:59:5c:a8:e0:78:84:6c:fc:05:e8:76:a3:e6:3b:33:94:4a:a9:ff:50:fb:60:fa:97:3b:6d:cc:04:f1:5e:36:24:a9:06:7a:f8:6b:00:e9:71:9d:89:be:9c:b2:9c:1f:ca:6d:d6:4d:ab:46:3d:b3:11:1f:8d:40:f7:c8:a4:39:48:c5:ca:1b:f6:30:95:7d:d9:68:41:ef:0a:37:b2:4a:37:e4:a4:b0:dd:7e:c1:af:3e:66:ea:bf:16:0a:7a:8a:05:00:01:a4:29:77:a9:d4:81:d4:0e \
>    -s 90:5f:f5:7d:93:e5:c4:3c:62:0d:26:65:dd:59:57:d5:ba:ba:f1:b7:30:91:72:7c:54:94:38:08:1e:13:35:38 \
>    -z b0:2b:07:50:28:e7:6e:5f:fa:27:1b:31:92:85:43:cb:c5:6a:ec:73:e2:27:c3:b9:80:ec:5b:ed:88:f0:1e:ec \
>    -n 00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00
 Pixiewps 1.4
 [?] Mode:     1 (RT/MT/CL)
 [*] Seed N1:  -
 [*] Seed ES1: 0x00000000
 [*] Seed ES2: 0x00000000
 [*] PSK1:     d4eb0c2a3815e1a03d70db7431eb53a3
 [*] PSK2:     d3b7e623f31d220a23ea07bb7f76658b
 [*] ES1:      00000000000000000000000000000000
 [*] ES2:      00000000000000000000000000000000
 [+] WPS pin:  04847533
 [*] Time taken: 0 s 4 ms
```

### ``

```text
root@kali:~#
">
    -a 7f:de:11:b9:69:1c:de:26:4a:21:a4:6f:eb:3d:b8:aa:aa:d7:30:09:09:32:b8:24:43:9b:e0:91:78:e7:6f:2c \
>    -e d4:38:91:0d:4e:6e:15:fe:70:f0:97:a8:70:2a:b8:94:f5:75:74:bf:64:19:9f:92:82:9b:e0:2c:c0:a3:75:48:08:8f:63:0a:82:37:0c:b7:95:42:cf:55:ca:a5:f0:f7:6c:b2:c7:5f:0e:23:18:44:f4:2d:00:f1:da:d4:94:23:56:c7:2c:b0:f6:87:c7:77:d0:cc:11:35:cf:b7:4f:bc:44:8d:ca:35:8a:78:3d:99:7f:2b:cf:44:21:d8:e2:0f:3c:7d:a4:72:c8:03:6f:77:2a:e9:fa:c1:e9:a8:2c:74:65:99:5a:e0:a5:26:d9:23:5e:4e:ec:5a:07:07:ab:80:db:3f:5f:18:7f:fa:fa:f1:57:74:b2:8d:a9:97:a6:c6:0a:a5:e0:ec:93:09:23:67:f6:3e:ec:1f:55:32:a4:5d:73:8f:ab:91:74:cf:1d:79:85:12:c1:81:f5:ea:a6:68:9d:8e:c7:c6:be:01:dc:d9:f8:68:80:11:55:d7:44:6a \
>    -r bc:ad:54:2f:88:44:7c:12:69:ef:34:31:4a:17:1c:92:b1:d7:06:4c:73:be:9f:d3:ed:87:63:74:10:46:0f:46:8c:36:b5:d4:a0:ba:af:85:9c:b2:30:42:d7:59:43:75:5a:d7:79:96:fb:ee:7b:66:db:b7:a8:f9:22:9c:a5:d3:b8:e7:c0:c4:5c:58:34:1f:56:a8:1a:41:a8:d2:e8:f6:3e:c9:3a:93:d9:9b:59:5c:a8:e0:78:84:6c:fc:05:e8:76:a3:e6:3b:33:94:4a:a9:ff:50:fb:60:fa:97:3b:6d:cc:04:f1:5e:36:24:a9:06:7a:f8:6b:00:e9:71:9d:89:be:9c:b2:9c:1f:ca:6d:d6:4d:ab:46:3d:b3:11:1f:8d:40:f7:c8:a4:39:48:c5:ca:1b:f6:30:95:7d:d9:68:41:ef:0a:37:b2:4a:37:e4:a4:b0:dd:7e:c1:af:3e:66:ea:bf:16:0a:7a:8a:05:00:01:a4:29:77:a9:d4:81:d4:0e \
>    -s 90:5f:f5:7d:93:e5:c4:3c:62:0d:26:65:dd:59:57:d5:ba:ba:f1:b7:30:91:72:7c:54:94:38:08:1e:13:35:38 \
>    -z b0:2b:07:50:28:e7:6e:5f:fa:27:1b:31:92:85:43:cb:c5:6a:ec:73:e2:27:c3:b9:80:ec:5b:ed:88:f0:1e:ec \
>    -n 00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00
 Pixiewps 1.4
 [?] Mode:     1 (RT/MT/CL)
 [*] Seed N1:  -
 [*] Seed ES1: 0x00000000
 [*] Seed ES2: 0x00000000
 [*] PSK1:     d4eb0c2a3815e1a03d70db7431eb53a3
 [*] PSK2:     d3b7e623f31d220a23ea07bb7f76658b
 [*] ES1:      00000000000000000000000000000000
 [*] ES2:      00000000000000000000000000000000
 [+] WPS pin:  04847533
 [*] Time taken: 0 s 4 ms
```

### ``

```text
root@kali:~#
">
Join Free CTF
Get Kali
Blog
Documentation
Documentation Pages
Tools Documentation
Frequently Asked Questions
Known Issues
Community
Community Support
Forums
Discord
Join Newsletter
Mirror Location
Get Involved
Courses
Developers
Git Repositories
Packages
Auto Package Test
Bug Tracker
Kali NetHunter Stats
About
Kali Linux Overview
Press Pack
Wallpapers
Kali Swag Store
Meet The Kali Team
Partnerships
Contact Us
```

### `pixiewps`

> 官方示例调用：`pixiewps \`

```text
root@kali:~# pixiewps \
>    -a 7f:de:11:b9:69:1c:de:26:4a:21:a4:6f:eb:3d:b8:aa:aa:d7:30:09:09:32:b8:24:43:9b:e0:91:78:e7:6f:2c \
>    -e d4:38:91:0d:4e:6e:15:fe:70:f0:97:a8:70:2a:b8:94:f5:75:74:bf:64:19:9f:92:82:9b:e0:2c:c0:a3:75:48:08:8f:63:0a:82:37:0c:b7:95:42:cf:55:ca:a5:f0:f7:6c:b2:c7:5f:0e:23:18:44:f4:2d:00:f1:da:d4:94:23:56:c7:2c:b0:f6:87:c7:77:d0:cc:11:35:cf:b7:4f:bc:44:8d:ca:35:8a:78:3d:99:7f:2b:cf:44:21:d8:e2:0f:3c:7d:a4:72:c8:03:6f:77:2a:e9:fa:c1:e9:a8:2c:74:65:99:5a:e0:a5:26:d9:23:5e:4e:ec:5a:07:07:ab:80:db:3f:5f:18:7f:fa:fa:f1:57:74:b2:8d:a9:97:a6:c6:0a:a5:e0:ec:93:09:23:67:f6:3e:ec:1f:55:32:a4:5d:73:8f:ab:91:74:cf:1d:79:85:12:c1:81:f5:ea:a6:68:9d:8e:c7:c6:be:01:dc:d9:f8:68:80:11:55:d7:44:6a \
>    -r bc:ad:54:2f:88:44:7c:12:69:ef:34:31:4a:17:1c:92:b1:d7:06:4c:73:be:9f:d3:ed:87:63:74:10:46:0f:46:8c:36:b5:d4:a0:ba:af:85:9c:b2:30:42:d7:59:43:75:5a:d7:79:96:fb:ee:7b:66:db:b7:a8:f9:22:9c:a5:d3:b8:e7:c0:c4:5c:58:34:1f:56:a8:1a:41:a8:d2:e8:f6:3e:c9:3a:93:d9:9b:59:5c:a8:e0:78:84:6c:fc:05:e8:76:a3:e6:3b:33:94:4a:a9:ff:50:fb:60:fa:97:3b:6d:cc:04:f1:5e:36:24:a9:06:7a:f8:6b:00:e9:71:9d:89:be:9c:b2:9c:1f:ca:6d:d6:4d:ab:46:3d:b3:11:1f:8d:40:f7:c8:a4:39:48:c5:ca:1b:f6:30:95:7d:d9:68:41:ef:0a:37:b2:4a:37:e4:a4:b0:dd:7e:c1:af:3e:66:ea:bf:16:0a:7a:8a:05:00:01:a4:29:77:a9:d4:81:d4:0e \
>    -s 90:5f:f5:7d:93:e5:c4:3c:62:0d:26:65:dd:59:57:d5:ba:ba:f1:b7:30:91:72:7c:54:94:38:08:1e:13:35:38 \
>    -z b0:2b:07:50:28:e7:6e:5f:fa:27:1b:31:92:85:43:cb:c5:6a:ec:73:e2:27:c3:b9:80:ec:5b:ed:88:f0:1e:ec \
>    -n 00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00
 Pixiewps 1.4
 [?] Mode:     1 (RT/MT/CL)
 [*] Seed N1:  -
 [*] Seed ES1: 0x00000000
 [*] Seed ES2: 0x00000000
 [*] PSK1:     d4eb0c2a3815e1a03d70db7431eb53a3
 [*] PSK2:     d3b7e623f31d220a23ea07bb7f76658b
 [*] ES1:      00000000000000000000000000000000
 [*] ES2:      00000000000000000000000000000000
 [+] WPS pin:  04847533
 [*] Time taken: 0 s 4 ms
```

### ``

```text
root@kali:~#
```

### `pixiewps --help`

> 官方示例调用：`pixiewps --help`

```text
root@kali:~# pixiewps --help
 Pixiewps 1.4 WPS pixie-dust attack tool
 Copyright (c) 2015-2017, wiire <
[email protected]
>
 Description of arguments:
 -e, --pke
     Enrollee's DH public key, found in M1.
 -r, --pkr
     Registrar's DH public key, found in M2.
 -s, --e-hash1
     Enrollee hash-1, found in M3. It's the hash of the first half of the PIN.
 -z, --e-hash2
     Enrollee hash-2, found in M3. It's the hash of the second half of the PIN.
 -a, --authkey
     Authentication session key. Although for this parameter a modified version of Reaver or Bully is needed, it can be avoided by specifying small Diffie-Hellman keys in both Reaver and Pixiewps and supplying --e-nonce, --r-nonce and --e-bssid.
 [?] pixiewps -e <pke> -s <e-hash1> -z <e-hash2> -S -n <e-nonce> -m <r-nonce> -b <e-bssid>
 -n, --e-nonce
     Enrollee's nonce, found in M1.
 -m, --r-nonce
     Registrar's nonce, found in M2. Used with other parameters to compute the session keys.
 -b, --e-bssid
     Enrollee's BSSID. Used with other parameters to compute the session keys.
 -S, --dh-small (deprecated)
     Small Diffie-Hellman keys. The same option must be specified in Reaver too. Some Access Points seem to be buggy and don't behave correctly with this option. Avoid using it with Reaver when possible
 --mode N[,... N]
     Select modes, comma separated (experimental modes are not used unless specified):
         1 (RT/MT/CL)
         2 (eCos simple)
         3 (RTL819x)
         4 (eCos simplest) [Experimental]
         5 (eCos Knuth)    [Experimental]
 --start [mm/]yyyy
 --end   [mm/]yyyy
     Starting and ending dates for mode 3. They are interchangeable. If only one is specified, the current time will be used for the other. The earliest possible date is 01/1970, corresponding to 0 (Unix epoch time), the latest is 02/2038, corresponding to 0x7FFFFFFF. If --force is used then pixiewps will start from the current time and go back all the way to 0.
 -7, --m7-enc
     Encrypted settings, found in M7. Recover Enrollee's WPA-PSK and secret nonce 2. This feature only works on some Access Points vulnerable to mode 3.
 [?] pixiewps -e <pke> -r <pkr> -n <e-nonce> -m <r-nonce> -b <e-bssid> -7 <enc7> --mode 3
 -5, --m5-enc
     Encrypted settings, found in M5. Recover Enrollee's secret nonce 1. This option must be used in conjunction with --m7-enc. If --e-hash1 and --e-hash2 are also specified, pixiewps will also recover the WPS PIN.
 [?] pixiewps -e <pke> -r <pkr> -n <e-nonce> -m <r-nonce> -b <e-bssid> -7 <enc7> -5 <enc5> --mode 3
 [?] pixiewps -e <pke> -r <pkr> -n <e-nonce> -m <r-nonce> -b <e-bssid> -7 <enc7> -5 <enc5> -s <e-hash1> -z <e-hash2> --mode 3
Learn more with
OffSec
Want to learn more about pixiewps? get access to in-depth training and hands-on labs:
PEN-210: 8.3. Attacking WPS Networks: WPS Attack
PEN-210 course
Updated on: 2025-Dec-09
 Edit this page
pipal
polenum
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install pixiewps`，再执行 `pixiewps --version` 2>/dev/null || `pixiewps -V`
- [ ] **2.** **读官方帮助** —— `pixiewps -h`，需要细节时 `man pixiewps`
- [ ] **3.** **在自有靶场跑最小用例** —— 用 `pixiewps -h` 里最简单的那个子命令试一次
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/pixiewps/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/credential-access.md`](../../tools/by-attack/credential-access.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/pixiewps/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/pixiewps/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
