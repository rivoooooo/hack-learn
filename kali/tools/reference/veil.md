# veil

> Generates payloads to bypass anti-virus solutions Veil is a tool designed to generate metasploit payloads that bypass common anti-virus solutions. It replaces the package veil-evasion.

> **功能分类**：后渗透 ｜ **Kali 包**：`veil` ｜ **官方文档**：<https://www.kali.org/tools/veil/>

## 1. 安装

```bash
sudo apt update
sudo apt install veil
```

| 项目 | 内容 |
|------|------|
| 版本 | 3.1.14 |
| 架构 | i386 |
| 可执行命令 | `veil`、`veil-catapult`、`veil-evasion` |
| 依赖 | `git`、`metasploit-framework`、`mingw-w64`、`mono-mcs`、`python3`、`python3-pycryptodome`、`ruby`、`sudo`、`unzip`、`wine` |
| 安装体积 | 871 KB |
| 官网 | <https://github.com/Veil-Framework/Veil> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/veil> |
| 包追踪 | <https://pkg.kali.org/pkg/veil> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
veil -h          # 查看用法
man veil         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 3 个可执行命令，下面是官方页面内嵌的帮助原文。

### `veil`

官方给出的调用示例：`veil -h`

```text
root@kali:~# veil -h
 ==========================================================================
                 Veil (Setup Script) | [Updated]: 2018-05-08
 ==========================================================================
     [Web]: https://www.veil-framework.com/ | [Twitter]: @VeilFramework
 ==========================================================================
                 os = kali
          osversion = 2026.3
       osmajversion = 2026
               arch = x86_64
           trueuser = kali
   userprimarygroup = kali
        userhomedir = /home/kali
            rootdir = /usr/share/veil
            veildir = /var/lib/veil
          outputdir = /var/lib/veil/output
    dependenciesdir = /var/lib/veil/setup-dependencies
            winedir = /var/lib/veil/wine
          winedrive = /var/lib/veil/wine/drive_c
            gempath = Z:\var\lib\veil\wine\drive_c\Ruby187\bin\gem
 [I] Kali Linux 2026.3 x86_64 detected...
 [?] Are you sure you wish to install Veil?
     Continue with installation? ([y]es/[s]ilent/[N]o):
```

## 4. 实践清单

按顺序做完这五步，就能把工具从「装上」推进到「会用」：

- [ ] **1.** **装好并确认版本** —— `sudo apt install veil`，再执行 `veil --version` 2>/dev/null || `veil -V`
- [ ] **2.** **读官方帮助** —— `veil -h`，需要细节时 `man veil`
- [ ] **3.** **在自有靶场跑最小用例** —— 用 `veil -h` 里最简单的那个子命令试一次
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/veil/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/defense-evasion.md`](../../tools/by-attack/defense-evasion.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/veil/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/veil/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
