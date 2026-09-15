# distorm3

> Powerful disassembler library for x86/AMD64 binary streams (runtime) diStorm3 is a binary stream disassembler library project. With diStorm3, no more parsing strings is needed. diStorm3 is really a decomposer, which means it takes an instr…

> **功能分类**：数字取证 ｜ **Kali 包**：`distorm3` ｜ **官方文档**：<https://www.kali.org/tools/distorm3/>

## 1. 安装

```bash
sudo apt update
sudo apt install libdistorm3-3
```

| 项目 | 内容 |
|------|------|
| 版本 | 3.5.2b |
| 架构 | any |
| 可执行命令 | `libdistorm3-3`、`libdistorm3-dev`、`python3-distorm3` |
| 依赖 | `libc6`、`libdistorm3-dev` |
| 安装体积 | 89 KB |
| 官网 | <https://github.com/gdabah/distorm> |
| 源码仓库 | <https://salsa.debian.org/debian/distorm3> |
| 包追踪 | <https://pkg.kali.org/pkg/distorm3> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
libdistorm3-3 -h          # 查看用法
man libdistorm3-3         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 3 个可执行命令，下面是官方页面内嵌的帮助原文。

### `python`

```text
root@kali:~# python
Python 2.7.3 (default, Mar 13 2014, 11:03:55)
[GCC 4.7.2] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> from distorm3 import Decode, Decode16Bits, Decode32Bits, Decode64Bits
>>> l = Decode(0x100, open("stagedrev.bin", "rb").read(), Decode16Bits)
>>> for i in l:
...  print "0x%08x (%02x) %-20s %s" % (i[0],  i[1],  i[3],  i[2])
...
0x00000100 (02) 7f45                 JG 0x147
0x00000102 (01) 4c                   DEC SP
0x00000103 (01) 46                   INC SI
0x00000104 (02) 0101                 ADD [BX+DI], AX
0x00000106 (02) 0100                 ADD [BX+SI], AX
0x00000108 (02) 0000                 ADD [BX+SI], AL
0x0000010a (02) 0000                 ADD [BX+SI], AL
0x0000010c (02) 0000                 ADD [BX+SI], AL
0x0000010e (02) 0000                 ADD [BX+SI], AL
0x00000110 (02) 0200                 ADD AL, [BX+SI]
0x00000112 (02) 0300                 ADD AX, [BX+SI]
0x00000114 (02) 0100                 ADD [BX+SI], AX
0x00000116 (02) 0000                 ADD [BX+SI], AL
0x00000118 (01) 54                   PUSH SP
0x00000119 (03) 800408               ADD BYTE [SI], 0x8
```

## 4. 实践清单

按顺序做完这五步，就能把工具从「装上」推进到「会用」：

- [ ] **1.** **装好并确认版本** —— `sudo apt install libdistorm3-3`，再执行 `libdistorm3-3 --version` 2>/dev/null || `libdistorm3-3 -V`
- [ ] **2.** **读官方帮助** —— `libdistorm3-3 -h`，需要细节时 `man libdistorm3-3`
- [ ] **3.** **在自有靶场跑最小用例** —— 用 `libdistorm3-3 -h` 里最简单的那个子命令试一次
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/distorm3/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/distorm3/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/distorm3/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
