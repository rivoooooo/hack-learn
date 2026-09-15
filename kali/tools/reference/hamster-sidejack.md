# hamster-sidejack

> Sidejacking tool Hamster is tool or “sidejacking”. It acts as a proxy server that replaces your cookies with session cookies stolen from somebody else, allowing you to hijack their sessions. Cookies are sniffed using the Ferret program. Yo…

> **功能分类**：Web 应用 ｜ **Kali 包**：`hamster-sidejack` ｜ **官方文档**：<https://www.kali.org/tools/hamster-sidejack/>

## 1. 安装

```bash
sudo apt update
sudo apt install hamster-sidejack
```

| 项目 | 内容 |
|------|------|
| 版本 | 2.0 |
| 架构 | any |
| 可执行命令 | `hamster-sidejack` |
| 依赖 | `libc6`、`libgcc-s1`、`libstdc++6` |
| 安装体积 | 154 KB |
| 官网 | <http://www.erratasec.com/research.html> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/hamster-sidejack> |
| 包追踪 | <https://pkg.kali.org/pkg/hamster-sidejack> |

## 2. 官方用法示例

> 以下为 Kali 官方工具页给出的示例与输出原文。

```text
Usage Example
root@kali:~# hamster
--- HAMPSTER 2.0 side-jacking tool ---
Set browser to use proxy http://127.0.0.1:1234
DEBUG: set_ports_option(1234)
DEBUG: mg_open_listening_port(1234)
Proxy: listening on 127.0.0.1:1234
begining thread
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `hamster`

```text
root@kali:~# hamster
--- HAMPSTER 2.0 side-jacking tool ---
Set browser to use proxy http://127.0.0.1:1234
DEBUG: set_ports_option(1234)
DEBUG: mg_open_listening_port(1234)
Proxy: listening on 127.0.0.1:1234
begining thread
```

## 4. 实践清单

按顺序做完这五步，就能把工具从「装上」推进到「会用」：

- [ ] **1.** **装好并确认版本** —— `sudo apt install hamster-sidejack`，再执行 `hamster-sidejack --version` 2>/dev/null || `hamster-sidejack -V`
- [ ] **2.** **读官方帮助** —— `hamster-sidejack -h`，需要细节时 `man hamster-sidejack`
- [ ] **3.** **在自有靶场跑最小用例** —— 用 `hamster-sidejack -h` 里最简单的那个子命令试一次
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/hamster-sidejack/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/collection.md`](../../tools/by-attack/collection.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/hamster-sidejack/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/hamster-sidejack/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
