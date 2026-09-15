#!/usr/bin/env python3
"""为 Kali 的每一个工具包生成一份「安装 + 官方用法示例 + 命令参数 + 实践清单」文档。

用法:
    python3 scripts/gen_kali_reference.py

依赖:
    data/kali-tools.json       (fetch_kali_tools.py)
    data/kali-tool-usage.json  (fetch_kali_usage.py)
    data/kali-categories.json  (fetch_kali_categories.py)

产出:
    kali/tools/reference/README.md          索引
    kali/tools/reference/<slug>.md          每个工具包一篇（约 780 篇）

说明:
    文档正文中的「官方用法示例」与「命令与参数」两节是**官网原文**，
    由脚本从 kali.org/tools/<slug>/ 抓取并原样引用，不是二手转述。
    其余章节（安装、实践清单、相关）由脚本按统一模板生成。
"""
from __future__ import annotations

import datetime
import json
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TOOLS_JSON = os.path.join(ROOT, "data", "kali-tools.json")
USAGE_JSON = os.path.join(ROOT, "data", "kali-tool-usage.json")
CATS_JSON = os.path.join(ROOT, "data", "kali-categories.json")
OUT_DIR = os.path.join(ROOT, "kali", "tools", "reference")
TUT_DIR = os.path.join(ROOT, "kali", "tools", "tutorials")

GROUP_ZH = {
    "information-gathering": "信息搜集", "vulnerability": "漏洞分析", "web": "Web 应用",
    "passwords": "口令攻击", "wireless": "无线攻击", "802-11": "802.11 Wi-Fi",
    "bluetooth": "蓝牙", "exploitation": "漏洞利用", "sniffing-spoofing": "嗅探与欺骗",
    "post-exploitation": "后渗透", "forensics": "数字取证", "recover": "数据恢复",
    "reverse-engineering": "逆向工程", "reporting": "报告与记录", "social-engineering": "社会工程",
    "hardware": "硬件攻击", "rfid": "RFID / NFC", "sdr": "软件定义无线电", "voip": "VoIP",
    "database": "数据库", "fuzzing": "模糊测试", "crypto-stego": "密码学与隐写",
    "identify": "识别与指纹", "detect": "检测", "protect": "防护", "top10": "Top 10 常用",
    "respond": "事件响应", "windows-resources": "Windows 资源", "gpu": "GPU 计算",
    "utils": "通用工具", "Tool Documentation": "（页面标记）",
}
ORDER = list(GROUP_ZH)


def fence(text: str, lang: str = "text") -> str:
    """选用足够长的围栏，避免内容里的反引号破坏代码块。"""
    longest = max((len(m) for m in re.findall(r"`+", text)), default=0)
    bar = "`" * max(3, longest + 1)
    return f"{bar}{lang}\n{text}\n{bar}"


# 命令行块里若出现这些章节标题，说明已经越界到下一个段落
STOP_LABELS = {
    "Packages and Binaries:", "Packages & Binaries", "Installed size:",
    "How to install:", "Dependencies:", "Files:", "Comments", "Categories",
    "Metapackages", "Tools:",
}


def clean_block(text: str) -> str:
    """截断命令块中越界的页面章节噪声。"""
    lines = text.split("\n")
    out: list[str] = []
    for i, ln in enumerate(lines):
        if i > 0 and ln.strip() in STOP_LABELS:
            break
        out.append(ln)
    return "\n".join(out).rstrip()


def cmd_name(cmdline: str) -> str:
    """从完整调用中取可执行文件名，用作小节标题。"""
    parts = cmdline.split()
    return os.path.basename(parts[0]) if parts else cmdline


def brief(text: str, limit: int = 240) -> str:
    text = re.sub(r"\s+", " ", (text or "").strip())
    return text if len(text) <= limit else text[: limit - 1] + "…"


def load(path: str):
    with open(path, encoding="utf-8") as fh:
        return json.load(fh)


def primary_group(tool: dict) -> str:
    groups = [g for g in (tool.get("tool_groups") or []) if g != "Tool Documentation"]
    if not groups:
        return "utils"
    return min(groups, key=lambda g: ORDER.index(g) if g in ORDER else 999)


def find_tutorial(slug: str, packages: list[str]) -> str:
    """在本库精讲教程里找这个包/命令对应的教程，返回相对链接。"""
    if not os.path.isdir(TUT_DIR):
        return ""
    names = {slug.lower()} | {p.lower() for p in packages}
    for d in sorted(os.listdir(TUT_DIR)):
        sub = os.path.join(TUT_DIR, d)
        if not os.path.isdir(sub):
            continue
        for f in sorted(os.listdir(sub)):
            if not f.endswith(".md") or f.upper() == "README.MD":
                continue
            stem = f[:-3]
            low = stem.lower()
            if low in names or any(low == n or n.startswith(low) or low.startswith(n) for n in names):
                return f"../../tools/tutorials/{d}/{f}"
    return ""


def build(tool: dict, usage: dict, cat_of: dict, date: str) -> str:
    slug = tool["slug"]
    name = tool.get("name") or slug
    packages = list(dict.fromkeys(tool.get("packages") or []))
    group = primary_group(tool)
    zh = GROUP_ZH.get(group, group)
    first_pkg = packages[0] if packages else slug

    out: list[str] = []
    out.append(f"# {name}\n")
    if tool.get("description"):
        out.append(f"> {brief(tool['description'])}\n")
    out.append(
        f"> **功能分类**：{zh} ｜ **Kali 包**：`{slug}` ｜ "
        f"**官方文档**：<{tool['url']}>\n"
    )

    # 1. 安装
    out.append("## 1. 安装\n")
    out.append(fence(f"sudo apt update\n{tool.get('install') or f'sudo apt install {slug}'}", "bash") + "\n")
    rows = [("版本", tool.get("version")), ("架构", (tool.get("arch") or "").split()[0] if tool.get("arch") else "")]
    if packages:
        rows.append(("可执行命令", "、".join(f"`{p}`" for p in packages)))
    deps_all = [d for d in (tool.get("dependencies") or []) if d != slug]
    if deps_all:
        deps = deps_all[:12]
        more = " 等" if len(deps_all) > 12 else ""
        rows.append(("依赖", "、".join(f"`{d}`" for d in deps) + more))
    rows += [
        ("安装体积", tool.get("installed_size")),
        ("官网", f"<{tool['homepage']}>" if tool.get("homepage") else ""),
        ("源码仓库", f"<{tool['source_repo']}>" if tool.get("source_repo") else ""),
        ("包追踪", f"<{tool['package_tracker']}>" if tool.get("package_tracker") else ""),
    ]
    out.append("| 项目 | 内容 |")
    out.append("|------|------|")
    for k, v in rows:
        if v:
            out.append(f"| {k} | {v} |")
    out.append("")

    # 2. 官方用法示例
    out.append("## 2. 官方用法示例\n")
    example = (usage or {}).get("usage_example") or ""
    if example:
        out.append("> 以下为 Kali 官方工具页给出的示例与输出原文。\n")
        out.append(fence(example) + "\n")
    else:
        out.append("> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。\n")
        out.append("```bash")
        out.append(f"{first_pkg} -h          # 查看用法")
        out.append(f"man {first_pkg}         # 查看手册")
        out.append("```\n")

    # 3. 命令与参数
    cmds = (usage or {}).get("commands") or []
    out.append("## 3. 命令与参数（官方 help / man 原文）\n")
    if cmds:
        out.append(f"本包提供 {len(packages)} 个可执行命令，下面是官方页面内嵌的帮助原文。\n")
        seen_cmd: set[str] = set()
        for c in cmds:
            cname = cmd_name(c["cmdline"])
            full = c["cmdline"]
            if cname not in seen_cmd:
                seen_cmd.add(cname)
                title = cname
            else:
                title = full if len(full) <= 60 else full[:57] + "…"
            out.append(f"### `{title}`\n")
            if len(full.split()) > 1:
                out.append(f"> 官方示例调用：`{full}`\n")
            out.append(fence(clean_block(c["text"])) + "\n")
    else:
        out.append("> 官方页面未内嵌该工具的 help 原文，请在本机执行：\n")
        out.append(fence("\n".join(f"{p} -h" for p in packages) or f"{slug} -h", "bash") + "\n")

    # 4. 实践清单
    out.append("## 4. 实践清单\n")
    out.append("按顺序做完这五步，就能把工具从「装上」推进到「会用」：\n")
    usage_hint = next((c["usage"] for c in cmds if c.get("usage")), "")
    steps = [
        f"**装好并确认版本** —— `{tool.get('install') or f'sudo apt install {slug}'}`，再执行 `"
        f"{first_pkg} --version` 2>/dev/null || `{first_pkg} -V`",
        f"**读官方帮助** —— `{first_pkg} -h`，需要细节时 `man {first_pkg}`",
        "**在自有靶场跑最小用例** —— "
        + (f"官方给出的调用形式是：`{usage_hint}`" if usage_hint else f"用 `{first_pkg} -h` 里最简单的那个子命令试一次"),
        f"**对照官方文档确认参数语义** —— <{tool['url']}>，重点核对上一步用到的每个参数",
        "**记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」",
    ]
    for i, s in enumerate(steps, 1):
        out.append(f"- [ ] **{i}.** {s}")
    out.append("")
    out.append(
        "> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。\n"
        "> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。\n"
    )

    # 5. 相关
    out.append("## 5. 相关\n")
    tut = find_tutorial(slug, packages)
    if tut:
        out.append(f"- **精讲教程**（含原理、参数详解、靶场实操与输出解读）：[{tut.split('/')[-1][:-3]}]({tut})")
    else:
        out.append(
            "- 精讲教程：本工具暂无专篇，可在 "
            "[`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具"
        )
    cat = cat_of.get(slug)
    if cat:
        out.append(f"- 按攻击阶段浏览同类工具：[`../../tools/by-attack/{cat}.md`](../../tools/by-attack/{cat}.md)")
    out.append(f"- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)")
    out.append(f"- Kali 官方工具页：<{tool['url']}>")
    out.append("")

    out.append("---\n")
    out.append("## 来源\n")
    out.append(f"- 工具元数据与用法示例、help 原文均抓取自 <{tool['url']}>（同步日期：{date}）")
    out.append("- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`")
    out.append("")
    return "\n".join(out)


def main() -> int:
    tools = load(TOOLS_JSON)
    usage_list = load(USAGE_JSON)
    cats = load(CATS_JSON)
    usage_of = {u["slug"]: u for u in usage_list}
    date = datetime.date.today().isoformat()

    cat_of: dict[str, str] = {}
    for c in cats["categories"]:
        for s in c["subcategories"]:
            for t in s["tools"]:
                cat_of.setdefault(t["package"], c["id"])

    os.makedirs(OUT_DIR, exist_ok=True)
    written = 0
    with_example = 0
    with_help = 0

    for tool in tools:
        u = usage_of.get(tool["slug"], {})
        if u.get("usage_example"):
            with_example += 1
        if u.get("commands"):
            with_help += 1
        body = build(tool, u, cat_of, date)
        with open(os.path.join(OUT_DIR, f"{tool['slug']}.md"), "w", encoding="utf-8") as fh:
            fh.write(body)
        written += 1

    # 索引
    by_group: dict[str, list[dict]] = {}
    for t in tools:
        by_group.setdefault(primary_group(t), []).append(t)
    ordered = sorted(by_group.items(), key=lambda kv: ORDER.index(kv[0]) if kv[0] in ORDER else 999)

    idx = [
        "# 工具参考文档（全量 780 个工具包）\n",
        "本目录为**每一个 Kali 工具包**提供一份参考文档，由脚本从官网同步生成，内容包含：\n",
        "1. **安装**：包名、可执行命令、依赖、体积、官网与源码仓库",
        "2. **官方用法示例**：Kali 官方工具页给出的典型命令与**真实输出**原文",
        "3. **命令与参数**：该包每个可执行命令的 `-h` / man 输出原文",
        "4. **实践清单**：五步走的动手路径（装好 → 读帮助 → 靶场最小用例 → 核对参数 → 记录解读）",
        "5. **相关**：精讲教程、按攻击阶段的同类工具、官方文档\n",
        f"> 共 **{written}** 篇 · 其中含官方示例 **{with_example}** 篇、"
        f"含 help 原文 **{with_help}** 篇 · 同步日期 {date}\n",
        "## 三种查法的分工\n",
        "| 目录 | 粒度 | 适合 |",
        "|------|------|------|",
        "| `by-attack/` | 16 个攻击阶段 → 501 条命令 | 「我现在要做侦察/提权，有哪些工具」 |",
        "| `catalog/` | 780 个包 → 速查卡片 | 「这个包是什么、装了有什么命令」 |",
        "| `reference/`（本目录） | 780 个包 → 完整参考文档 | 「我要开始用这个工具，从哪下手」 |",
        "| `tutorials/` | 108 篇深度教程 | 「我要把这个重点工具学透」 |\n",
        "## 按分组浏览\n",
        "| 分组 | 包数 | 包名 |",
        "|------|------|------|",
    ]
    for group, items in ordered:
        zh = GROUP_ZH.get(group, group)
        names = "、".join(
            f"[{i['slug']}]({i['slug']}.md)" for i in sorted(items, key=lambda x: x["slug"])
        )
        idx.append(f"| **{zh}** | {len(items)} | {names} |")
    idx.append("")
    idx.append("## 常用入口\n")
    idx.append("- 全量 A–Z：[`../catalog/all-tools.md`](../catalog/all-tools.md)")
    idx.append("- 25 个最常用包：`grep -c . <(ls *.md)` 之后按需查；官方精选见 <https://www.kali.org/tools/top-100/>")
    idx.append("- 搜索工具：`grep -i '关键词' ../../../data/kali-tools.tsv`")
    idx.append("")
    with open(os.path.join(OUT_DIR, "README.md"), "w", encoding="utf-8") as fh:
        fh.write("\n".join(idx))

    print(f"[+] 生成 {written} 篇参考文档（官方示例 {with_example} · help 原文 {with_help}）")
    print(f"[+] -> {OUT_DIR}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
