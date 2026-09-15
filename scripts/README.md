# 脚本说明

本目录的脚本负责**从官方来源同步数据**并**生成索引文档**，让学习库的内容可以随时刷新，
而不是一次性抄写后逐渐过期。

---

## 依赖

只依赖 Python 3 标准库（`urllib`、`json`、`re`、`concurrent.futures`），**无需 pip 安装任何包**。

```bash
python3 --version    # 需要 3.10+（用到了 `X | None` 类型标注）
```

---

## 数据同步流程

```bash
cd <仓库根目录>

# ① Kali 工具元数据（约 780 个工具页面，1–2 分钟）
python3 scripts/fetch_kali_tools.py --workers 6
#    -> data/kali-tools.json

# ② Kali 工具功能分类树（16 个 ATT&CK 风格分类）
python3 scripts/fetch_kali_categories.py
#    -> data/kali-categories.json

# ③ 官方重点工具清单（Top 100 页面，用于教程覆盖度比对）
python3 scripts/fetch_kali_top100.py
#    -> data/kali-top100.json

# ④ Kali 官方文档大纲与摘要（约 270 篇，1–2 分钟）
python3 scripts/fetch_kali_docs.py --workers 6
#    -> data/kali-docs.json, kali/docs/official-index.md

# ⑤ 生成工具索引文档
python3 scripts/gen_kali_index.py
#    -> kali/tools/index.md
#    -> kali/tools/by-attack/*.md   （16 个分类）
#    -> kali/tools/catalog/*.md     （按包速查卡片）
#    -> data/kali-tools.tsv         （扁平数据，便于 grep）

# ⑥ 抓取每个工具页内嵌的官方用法示例与各命令 help 原文（约 780 个页面，1–2 分钟）
python3 scripts/fetch_kali_usage.py --workers 6
#    -> data/kali-tool-usage.json

# ⑦ 为每个工具包生成「安装 + 官方示例 + 参数 + 实践清单」参考文档
python3 scripts/gen_kali_reference.py
#    -> kali/tools/reference/*.md（约 780 篇）+ reference/README.md

# ⑧ 生成教程索引
python3 scripts/gen_tutorials_index.py
#    -> kali/tools/tutorials/README.md

# ⑨ 校验全库链接（含锚点）
python3 scripts/check_links.py --anchors
```

也可以一条命令跑完（顺序有依赖，不能并行）：

```bash
for s in fetch_kali_tools fetch_kali_categories fetch_kali_top100 fetch_kali_docs \
         fetch_kali_usage gen_kali_index gen_kali_reference gen_tutorials_index check_links; do
  echo "=== $s ==="
  python3 "scripts/$s.py" || break
done
```

---

## 脚本清单

| 脚本 | 作用 | 输出 |
|------|------|------|
| `fetch_kali_tools.py` | 抓取 <https://www.kali.org/tools/all-tools/> 全部工具包的元数据（版本、包/命令、依赖、体积、官网、源码库） | `data/kali-tools.json` |
| `fetch_kali_categories.py` | 抓取 <https://www.kali.org/tools/> 首页的功能分类树（一级分类 → 二级子类 → 命令），并附中文名与说明 | `data/kali-categories.json` |
| `fetch_kali_top100.py` | 抓取 <https://www.kali.org/tools/top-100/> 的官方重点工具清单 | `data/kali-top100.json` |
| `fetch_kali_docs.py` | 抓取 <https://www.kali.org/docs/> 全量文档的标题、内文大纲、摘要 | `data/kali-docs.json`、`kali/docs/official-index.md` |
| `fetch_kali_usage.py` | 抓取每个工具页内嵌的官方用法示例与各命令 `-h`/man 原文 | `data/kali-tool-usage.json` |
| `gen_kali_index.py` | 把结构化数据渲染成 Markdown 索引与卡片 | `kali/tools/index.md`、`by-attack/`、`catalog/`、`data/kali-tools.tsv` |
| `gen_kali_reference.py` | 为每个工具包生成参考文档（安装、官方示例、参数原文、实践清单） | `kali/tools/reference/*.md` |
| `gen_tutorials_index.py` | 扫描教程目录生成教程索引，并比对官方重点工具的教程覆盖度 | `kali/tools/tutorials/README.md` |
| `check_links.py` | 校验全库 Markdown 的相对链接与锚点，有断链时退出码为 1（可接 CI） | 终端输出 |
| `fetch_linux_kernel.sh` | 拉取 Linux 内核源码到 `kernel/src/linux` | 内核源码树 |

---

## 常用参数

```bash
# 只抓少量做调试
python3 scripts/fetch_kali_tools.py --limit 10 --workers 2

# 提高并发（对方站点可能限速，建议不超过 8）
python3 scripts/fetch_kali_tools.py --workers 8

# 指定输出路径
python3 scripts/fetch_kali_tools.py --out /tmp/test.json

# 拉取内核：浅克隆（默认）、完整历史、stable 分支
bash scripts/fetch_linux_kernel.sh
bash scripts/fetch_linux_kernel.sh --full
bash scripts/fetch_linux_kernel.sh --stable

# 校验链接：只查文件 / 同时查锚点 / 列出正常链接
python3 scripts/check_links.py
python3 scripts/check_links.py --anchors
python3 scripts/check_links.py --list-ok

# 国内网络可用镜像
export KERNEL_MIRROR=https://gitclone.com/github.com/torvalds/linux.git
bash scripts/fetch_linux_kernel.sh
```

> 💡 新增或改动文档后建议跑一次 `python3 scripts/check_links.py --anchors`，
> 它会同时校验相对路径与 `#锚点`（按 github-slugger 规则计算，与 GitHub 渲染一致）。

---

## 数据文件的用法

### `data/kali-tools.tsv`（推荐用这个来搜）

制表符分隔，字段：`slug`、`name`、`package_group`、`attack_category`、`packages`、`description`、`url`

```bash
# 搜描述里含 "sql injection" 的工具
grep -i 'sql injection' data/kali-tools.tsv | cut -f2,5

# 按功能分类筛选
awk -F'\t' '$4=="凭据访问" {print $2}' data/kali-tools.tsv

# 按包分组筛选
awk -F'\t' '$3=="web" {print $2}' data/kali-tools.tsv

# 找出全部可执行命令名（逗号分隔的 packages 字段）
cut -f5 data/kali-tools.tsv | tr ',' '\n' | sort -u | wc -l
```

### `data/kali-tools.json`

完整元数据，适合写脚本消费。单个记录形如：

```json
{
  "slug": "nmap",
  "name": "nmap",
  "url": "https://www.kali.org/tools/nmap/",
  "version": "...",
  "packages": ["nmap", "ncat", "ndiff", "nping", "zenmap"],
  "description": "...",
  "install": "sudo apt install nmap",
  "dependencies": ["..."],
  "homepage": "...",
  "source_repo": "..."
}
```

### `data/kali-categories.json`

功能分类树：

```json
{
  "categories": [
    {
      "id": "reconnaissance",
      "zh": "侦察",
      "subcategories": [
        {"name": "Host Information", "zh": "主机信息",
         "tools": [{"package": "nmap", "command": "nmap", "url": "..."}]}
      ]
    }
  ]
}
```

---

## 抓取礼仪

这些脚本抓的是**公开文档页面**，请保持礼貌：

- 默认 6 并发 + 失败退避重试，不要随意调到很高
- 全量刷新一次约 780 + 270 个请求，**不要频繁重复跑**
- 抓下来的数据已经提交进仓库，日常使用不需要重新抓
- 只有当你需要"确认官网是否有更新"时才重跑

---

## 已知限制

| 限制 | 说明 |
|------|------|
| 页面结构依赖 | 解析基于当前 HTML 结构（无官方 API）。Kali 改版后解析可能失效，届时需更新 `parse_tool()` / `TOKEN` 正则 |
| 分类覆盖 | 官网功能分类页只收录约 418 个包；其余包在 `catalog/` 的"通用工具"等分组里 |
| 个别页面 404 | 例如 `tools/submitting-tools` 在工具索引里是死链，脚本会跳过并打印警告 |
| 中文名为人工映射 | `fetch_kali_categories.py` 里的中文翻译表需要人工维护，官网新增分类时会回退显示英文名 |

---

## 排错

| 现象 | 原因 | 处理 |
|------|------|------|
| `请求失败 ... HTTP Error 404` | 该工具页在 all-tools 里被引用但实际不存在 | 属正常，脚本会跳过并统计 |
| 抓取中途大量失败 | 网络不稳或被限速 | 降低 `--workers`，重跑即可（脚本有退避重试） |
| `gen_kali_index.py` 报 `FileNotFoundError` | 还没跑 fetch 脚本 | 先按上面顺序跑 fetch |
| 生成的中文分类名显示成英文 | 该分类不在翻译表里 | 在 `fetch_kali_categories.py` 的 `SUBCATEGORY_ZH` 补充 |
