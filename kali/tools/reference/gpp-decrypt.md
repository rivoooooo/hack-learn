# gpp-decrypt

> Group Policy Preferences decrypter A simple ruby script that will decrypt a given GPP encrypted string.

> **功能分类**：口令攻击 ｜ **Kali 包**：`gpp-decrypt` ｜ **官方文档**：<https://www.kali.org/tools/gpp-decrypt/>

## 1. 安装

```bash
sudo apt update
sudo apt install gpp-decrypt
```

| 项目 | 内容 |
|------|------|
| 版本 | 0.1 |
| 架构 | all |
| 可执行命令 | `gpp-decrypt` |
| 依赖 | `ruby`、`rubygems` |
| 安装体积 | 11 KB |
| 官网 | <http://carnal0wnage.attackresearch.com/2012/10/group-policy-preferences-and-getting.html> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/gpp-decrypt> |
| 包追踪 | <https://pkg.kali.org/pkg/gpp-decrypt> |

## 2. 官方用法示例

> 以下为 Kali 官方工具页给出的示例与输出原文。

```text
Usage Example
Decrypt the given Group Policy Preferences string (j1Uyj3Vx8TY9LtLZil2uAuZkFQA/4latT76ZwgdHdhw):
root@kali:~# gpp-decrypt j1Uyj3Vx8TY9LtLZil2uAuZkFQA/4latT76ZwgdHdhw
Local*P4ssword!
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `gpp-decrypt`

> 官方示例调用：`gpp-decrypt j1Uyj3Vx8TY9LtLZil2uAuZkFQA/4latT76ZwgdHdhw`

```text
root@kali:~# gpp-decrypt j1Uyj3Vx8TY9LtLZil2uAuZkFQA/4latT76ZwgdHdhw
Local*P4ssword!
```

## 4. 实践清单

按顺序做完这五步，就能把工具从「装上」推进到「会用」：

- [ ] **1.** **装好并确认版本** —— `sudo apt install gpp-decrypt`，再执行 `gpp-decrypt --version` 2>/dev/null || `gpp-decrypt -V`
- [ ] **2.** **读官方帮助** —— `gpp-decrypt -h`，需要细节时 `man gpp-decrypt`
- [ ] **3.** **在自有靶场跑最小用例** —— 用 `gpp-decrypt -h` 里最简单的那个子命令试一次
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/gpp-decrypt/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/gpp-decrypt/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/gpp-decrypt/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
