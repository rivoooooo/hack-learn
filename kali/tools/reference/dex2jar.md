# dex2jar

> Tools to work with android .dex and java .class files dex2jar contains 4 compments: dex-reader is designed to read the Dalvik Executable (.dex/.odex) format. It has a light weight API similar with ASM. An example here dex-translator is des…

> **功能分类**：逆向工程 ｜ **Kali 包**：`dex2jar` ｜ **官方文档**：<https://www.kali.org/tools/dex2jar/>

## 1. 安装

```bash
sudo apt update
sudo apt install dex2jar
```

| 项目 | 内容 |
|------|------|
| 版本 | 0.0.9.15 |
| 可执行命令 | `dex2jar`、`d2j-apk-sign`、`d2j-asm-verify`、`d2j-baksmali`、`d2j-class-version-switch`、`d2j-decrypt-string`、`d2j-dex-recompute-checksum`、`d2j-dex-weaver`、`d2j-dex2jar`、`d2j-dex2smali`、`d2j-jar-access`、`d2j-jar-weaver`、`d2j-jar2dex`、`d2j-jar2jasmin`、`d2j-jasmin2jar`、`d2j-smali`、`d2j-std-apk`、`d2j_invoke`、`dex-tools` |
| 依赖 | `default-jre`、`d2j-apk-sign` |
| 安装体积 | 5.80 MB |
| 官网 | <https://github.com/pxb1988/dex2jar/tree/2.x> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/dex2jar> |
| 包追踪 | <https://pkg.kali.org/pkg/dex2jar> |

## 2. 官方用法示例

> 以下为 Kali 官方工具页给出的示例与输出原文。

```text
Usage Example
root@kali:~# d2j-dex2jar /usr/share/metasploit-framework/data/android/apk/classes.dex
dex2jar /usr/share/metasploit-framework/data/android/apk/classes.dex -> classes-dex2jar.jar

d2j-jar-remap
root@kali:~# d2j-jar-remap -h
d2j-jar-remap -- rename package/class/method/field name in a jar
usage: d2j-jar-remap [options] jar
options:
 -c,--config <config>    config file for remap, this is REQUIRED
 -f,--force              force overwrite
 -h,--help               Print this help message
 -o,--output <out-jar>   output .jar file, default is $current_dir/[jar-name]-re
                         map.jar
version: 0.0.9.15
online help: https://code.google.com/p/dex2jar/wiki/DeObfuscateJarWithDexTool

dex2jar
root@kali:~# dex2jar
this cmd is deprecated, use the d2j-dex2jar if possible
dex2jar version: translator-0.0.9.15
dex2jar file1.dexORapk file2.dexORapk ...

d2j-dex-dump
root@kali:~# d2j-dex-dump -h
Dump in.dexORapk out.dump.jar

d2j-init-deobf
root@kali:~# d2j-init-deobf -h
d2j-init-deobf -- generate an init config file for deObfuscate a jar
usage: d2j-init-deobf [options] <jar>
options:
 -f,--force                force overwrite
 -h,--help                 Print this help message
 -max,--max-length <MAX>   do the rename if the length > MIN, default is 40
 -min,--min-length <MIN>   do the rename if the length < MIN, default is 2
 -o,--output <out-file>    output .jar file, default is $current_dir/[file-name]
                           -deobf-init.txt
version: 0.0.9.15
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 19 个可执行命令，下面是官方页面内嵌的帮助原文。

### `d2j-jar-remap`

> 官方示例调用：`d2j-jar-remap -h`

```text
root@kali:~# d2j-jar-remap -h
d2j-jar-remap -- rename package/class/method/field name in a jar
usage: d2j-jar-remap [options] jar
options:
 -c,--config
    config file for remap, this is REQUIRED
 -f,--force              force overwrite
 -h,--help               Print this help message
 -o,--output
   output .jar file, default is $current_dir/[jar-name]-re
                         map.jar
version: 0.0.9.15
online help: https://code.google.com/p/dex2jar/wiki/DeObfuscateJarWithDexTool
```

### `dex2jar`

```text
root@kali:~# dex2jar
this cmd is deprecated, use the d2j-dex2jar if possible
dex2jar version: translator-0.0.9.15
dex2jar file1.dexORapk file2.dexORapk ...
d2j-dex-dump
```

### `d2j-dex-dump`

> 官方示例调用：`d2j-dex-dump -h`

```text
root@kali:~# d2j-dex-dump -h
Dump in.dexORapk out.dump.jar
d2j-init-deobf
```

### `d2j-init-deobf`

> 官方示例调用：`d2j-init-deobf -h`

```text
root@kali:~# d2j-init-deobf -h
d2j-init-deobf -- generate an init config file for deObfuscate a jar
usage: d2j-init-deobf [options]
options:
 -f,--force                force overwrite
 -h,--help                 Print this help message
 -max,--max-length
   do the rename if the length > MIN, default is 40
 -min,--min-length
   do the rename if the length
    output .jar file, default is $current_dir/[file-name]
                           -deobf-init.txt
version: 0.0.9.15
">
 classes-dex2jar.jar
d2j-jar-remap
```

### `d2j-jar-remap -h`

> 官方示例调用：`d2j-jar-remap -h`

```text
root@kali:~# d2j-jar-remap -h
d2j-jar-remap -- rename package/class/method/field name in a jar
usage: d2j-jar-remap [options] jar
options:
 -c,--config
    config file for remap, this is REQUIRED
 -f,--force              force overwrite
 -h,--help               Print this help message
 -o,--output
   output .jar file, default is $current_dir/[jar-name]-re
                         map.jar
version: 0.0.9.15
online help: https://code.google.com/p/dex2jar/wiki/DeObfuscateJarWithDexTool
```

### `dex2jar`

```text
root@kali:~# dex2jar
this cmd is deprecated, use the d2j-dex2jar if possible
dex2jar version: translator-0.0.9.15
dex2jar file1.dexORapk file2.dexORapk ...
d2j-dex-dump
```

### `d2j-dex-dump -h`

> 官方示例调用：`d2j-dex-dump -h`

```text
root@kali:~# d2j-dex-dump -h
Dump in.dexORapk out.dump.jar
d2j-init-deobf
```

### `d2j-init-deobf -h`

> 官方示例调用：`d2j-init-deobf -h`

```text
root@kali:~# d2j-init-deobf -h
d2j-init-deobf -- generate an init config file for deObfuscate a jar
usage: d2j-init-deobf [options]
options:
 -f,--force                force overwrite
 -h,--help                 Print this help message
 -max,--max-length
   do the rename if the length > MIN, default is 40
 -min,--min-length
   do the rename if the length
    output .jar file, default is $current_dir/[file-name]
                           -deobf-init.txt
version: 0.0.9.15
">
 classes-dex2jar.jar
d2j-jar-remap
```

### `d2j-jar-remap -h`

> 官方示例调用：`d2j-jar-remap -h`

```text
root@kali:~# d2j-jar-remap -h
d2j-jar-remap -- rename package/class/method/field name in a jar
usage: d2j-jar-remap [options] jar
options:
 -c,--config
    config file for remap, this is REQUIRED
 -f,--force              force overwrite
 -h,--help               Print this help message
 -o,--output
   output .jar file, default is $current_dir/[jar-name]-re
                         map.jar
version: 0.0.9.15
online help: https://code.google.com/p/dex2jar/wiki/DeObfuscateJarWithDexTool
```

### `dex2jar`

```text
root@kali:~# dex2jar
this cmd is deprecated, use the d2j-dex2jar if possible
dex2jar version: translator-0.0.9.15
dex2jar file1.dexORapk file2.dexORapk ...
d2j-dex-dump
```

## 4. 实践清单

按顺序做完这五步，就能把工具从「装上」推进到「会用」：

- [ ] **1.** **装好并确认版本** —— `sudo apt install dex2jar`，再执行 `dex2jar --version` 2>/dev/null || `dex2jar -V`
- [ ] **2.** **读官方帮助** —— `dex2jar -h`，需要细节时 `man dex2jar`
- [ ] **3.** **在自有靶场跑最小用例** —— 用 `dex2jar -h` 里最简单的那个子命令试一次
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/dex2jar/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- **精讲教程**（含原理、参数详解、靶场实操与输出解读）：[dex2jar](../../tools/tutorials/10-逆向工程/dex2jar.md)
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/resource-development.md`](../../tools/by-attack/resource-development.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/dex2jar/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/dex2jar/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
