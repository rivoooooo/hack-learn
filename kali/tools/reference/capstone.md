# capstone

> Lightweight multi-architecture disassembly framework - command line tool Capstone is a lightweight multi-platform, multi-architecture disassembly framework. This package contains cstool, a command-line tool to disassemble hexadecimal strin…

> **功能分类**：数字取证 ｜ **Kali 包**：`capstone` ｜ **官方文档**：<https://www.kali.org/tools/capstone/>

## 1. 安装

```bash
sudo apt update
sudo apt install capstone-tool
```

| 项目 | 内容 |
|------|------|
| 版本 | 5.0.9 |
| 架构 | any |
| 可执行命令 | `capstone-tool`、`cstool`、`libcapstone-dev`、`libcapstone5`、`python3-capstone` |
| 依赖 | `libc6`、`cstool` |
| 安装体积 | 8.97 MB |
| 官网 | <https://www.capstone-engine.org/> |
| 源码仓库 | <https://salsa.debian.org/pkg-security-team/capstone> |
| 包追踪 | <https://pkg.kali.org/pkg/capstone> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
capstone-tool -h          # 查看用法
man capstone-tool         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 5 个可执行命令，下面是官方页面内嵌的帮助原文。

### `cstool`

官方给出的调用示例：`cstool -h`

```text
root@kali:~# cstool -h
Cstool for Capstone Disassembler Engine v5.0.9
Syntax: cstool [-d|-s|-u|-v] <arch+mode> <assembly-hexstring> [start-address-in-hex-format]
The following <arch+mode> options are supported:
        x16         16-bit mode (X86)
        x32         32-bit mode (X86)
        x64         64-bit mode (X86)
        x16att      16-bit mode (X86), syntax AT&T
        x32att      32-bit mode (X86), syntax AT&T
        x64att      64-bit mode (X86), syntax AT&T
        arm         arm
        armbe       arm + big endian
        thumb       thumb mode
        thumbbe     thumb + big endian
        cortexm     thumb + cortex-m extensions
        armv8       arm v8
        thumbv8     thumb v8
        armv8be     arm v8 + big endian
        thumbv8be   thumb v8 + big endian
        arm64       aarch64 mode
        arm64be     aarch64 + big endian
        mips        mips32 + little endian
        mipsbe      mips32 + big endian
        mips64      mips64 + little endian
        mips64be    mips64 + big endian
        ppc32       ppc32 + little endian
        ppc32be     ppc32 + big endian
        ppc32qpx    ppc32 + qpx + little endian
        ppc32beqpx  ppc32 + qpx + big endian
        ppc32ps     ppc32 + ps + little endian
        ppc32beps   ppc32 + ps + big endian
        ppc64       ppc64 + little endian
        ppc64be     ppc64 + big endian
        ppc64qpx    ppc64 + qpx + little endian
        ppc64beqpx  ppc64 + qpx + big endian
        sparc       sparc
        systemz     systemz (s390x)
        xcore       xcore
        m68k        m68k + big endian
        m68k40      m68k_040
        tms320c64x  TMS320C64x
        m6800       M6800/2
        m6801       M6801/3
        m6805       M6805
        m6808       M68HC08
        m6809       M6809
        m6811       M68HC11
        cpu12       M68HC12/HCS12
        hd6301      HD6301/3
        hd6309      HD6309
        hcs08       HCS08
        evm         Ethereum Virtual Machine
        6502        MOS 6502
        65c02       WDC 65c02
        w65c02      WDC w65c02
        65816       WDC 65816 (long m/x)
        wasm:       Web Assembly
        bpf         Classic BPF
        bpfbe       Classic BPF + big endian
        ebpf        Extended BPF
        ebpfbe      Extended BPF + big endian
        riscv32     riscv32
        riscv64     riscv64
        sh          superh SH1
        sh2         superh SH2
        sh2e        superh SH2E
        sh2dsp      superh SH2-DSP
        sh2a        superh SH2A
        sh2afpu     superh SH2A-FPU
        sh3         superh SH3
        sh3be       superh SH3 big endian
        sh3e        superh SH3E
        sh3ebe      superh SH3E big endian
        sh3-dsp     superh SH3-DSP
        sh3-dspbe   superh SH3-DSP big endian
        sh4         superh SH4
        sh4be       superh SH4 big endian
        sh4a        superh SH4A
        sh4abe      superh SH4A big endian
        sh4al-dsp   superh SH4AL-DSP
        sh4al-dspbe superh SH4AL-DSP big endian
        tc110       tricore V1.1
        tc120       tricore V1.2
        tc130       tricore V1.3
        tc131       tricore V1.3.1
        tc160       tricore V1.6
        tc161       tricore V1.6.1
        tc162       tricore V1.6.2
Extra options:
        -d show detailed information of the instructions
        -s decode in SKIPDATA mode
        -u show immediates as unsigned
        -v show version & Capstone core build info
```

## 4. 实践清单

按顺序做完这五步，就能把工具从「装上」推进到「会用」：

- [ ] **1.** **装好并确认版本** —— `sudo apt install capstone-tool`，再执行 `capstone-tool --version` 2>/dev/null || `capstone-tool -V`
- [ ] **2.** **读官方帮助** —— `capstone-tool -h`，需要细节时 `man capstone-tool`
- [ ] **3.** **在自有靶场跑最小用例** —— 用 `capstone-tool -h` 里最简单的那个子命令试一次
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/capstone/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/resource-development.md`](../../tools/by-attack/resource-development.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/capstone/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/capstone/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
