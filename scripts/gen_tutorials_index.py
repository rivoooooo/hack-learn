#!/usr/bin/env python3
"""扫描 kali/tools/tutorials/，生成教程索引。

用法:
    python3 scripts/gen_tutorials_index.py

产出:
    kali/tools/tutorials/README.md

说明:
    教程文件由人工/代理撰写，本脚本只负责汇总登记，保证索引与实际文件一致。
    每个教程文件的第一行注释或首个标题会被用作条目描述。
"""
from __future__ import annotations

import json
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TUT_DIR = os.path.join(ROOT, "kali", "tools", "tutorials")
TOOLS_JSON = os.path.join(ROOT, "data", "kali-tools.json")
TOP100_JSON = os.path.join(ROOT, "data", "kali-top100.json")

# 目录 -> (显示名, 说明, 建议顺序)
DIR_META = {
    "01-信息搜集": ("信息搜集", "被动/主动侦察：端口、服务、DNS、OSINT、SMB 枚举", 1),
    "02-漏洞分析": ("漏洞分析", "漏洞扫描、模糊测试与应用安全检测", 2),
    "03-Web应用": ("Web 应用", "Web 代理、目录爆破、注入与 Web 漏洞利用", 3),
    "04-口令攻击": ("口令攻击", "在线爆破、离线破解、字典生成", 4),
    "05-无线攻击": ("无线攻击", "Wi-Fi 监听、握手抓取与破解", 5),
    "06-漏洞利用": ("漏洞利用", "EXP 框架、Payload 生成与投递", 6),
    "07-嗅探与欺骗": ("嗅探与欺骗", "流量抓取、中间人与名称解析投毒", 7),
    "08-后渗透": ("后渗透", "提权、凭据获取、横向移动与隧道", 8),
    "09-数字取证": ("数字取证", "磁盘/内存/文件取证与证据分析", 9),
    "10-逆向工程": ("逆向工程", "反汇编、调试与二进制分析", 10),
    "11-社会工程与报告": ("社会工程与报告", "钓鱼演练与测试报告输出", 11),
    "12-基础设施与C2": ("基础设施与 C2", "C2 框架、重定向器与 Payload 托管", 12),
}


def first_heading(path: str) -> str:
    """取文件首个 Markdown 标题作为描述。"""
    try:
        with open(path, encoding="utf-8") as fh:
            for line in fh:
                line = line.strip()
                if line.startswith("#"):
                    return re.sub(r"^#+\s*", "", line)
                if line and not line.startswith((">", "<!--")):
                    return line[:80]
    except OSError:
        pass
    return ""


def load_top100_coverage(name2rel: dict[str, str]) -> list[tuple[str, str, str]]:
    """返回 [(包名, 描述, 教程相对链接或 '—')]，报告官方重点工具的教程覆盖情况。

    教程文件名可能是包名，也可能是包内的命令名（例如 `impacket` 教程对应
    `impacket-scripts` 包、`netexec` 对应 `netexec` 包）。这里用
    "包名 / 命令名互相包含"做匹配，避免因命名差异漏判。
    """
    if not (os.path.exists(TOOLS_JSON) and os.path.exists(TOP100_JSON)):
        return []

    with open(TOOLS_JSON, encoding="utf-8") as fh:
        tools = json.load(fh)
    with open(TOP100_JSON, encoding="utf-8") as fh:
        top = json.load(fh)

    by_slug = {t["slug"]: t for t in tools}
    cmd2pkg: dict[str, str] = {}
    for t in tools:
        for cmd in t.get("packages") or []:
            cmd2pkg.setdefault(cmd.lower(), t["slug"])

    rows: list[tuple[str, str, str]] = []
    for pkg in sorted(top.get("packages") or []):
        meta = by_slug.get(pkg, {})
        desc = (meta.get("description") or "").strip()
        desc = desc[:70] + ("…" if len(desc) > 70 else "")

        link = "—"
        for name in sorted(name2rel):
            low = name.lower()
            if (
                low == pkg
                or cmd2pkg.get(low) == pkg
                # 前缀匹配：容许 impacket ↔ impacket-scripts 这类命名差异，
                # 但不用子串匹配（否则 ettercap 会被 bettercap 误判为已覆盖）
                or low.startswith(pkg)
                or pkg.startswith(low)
            ):
                link = f"[{name}]({name2rel[name]})"
                break
        rows.append((pkg, desc, link))
    return rows


def main() -> int:
    if not os.path.isdir(TUT_DIR):
        print(f"[!] 目录不存在: {TUT_DIR}")
        return 1

    dirs = sorted(
        d for d in os.listdir(TUT_DIR) if os.path.isdir(os.path.join(TUT_DIR, d))
    )
    total = 0
    sections: list[tuple[str, str, str, list[tuple[str, str]]]] = []

    for d in dirs:
        files = sorted(
            f
            for f in os.listdir(os.path.join(TUT_DIR, d))
            if f.endswith(".md") and f.upper() != "README.MD"
        )
        entries = [
            (f, first_heading(os.path.join(TUT_DIR, d, f))) for f in files
        ]
        total += len(entries)
        zh, desc, order = DIR_META.get(d, (d, "", 99))
        sections.append((d, zh, desc, entries))

    sections.sort(key=lambda s: DIR_META.get(s[0], ("", "", 99))[2])

    out: list[str] = [
        "# Kali 工具精讲教程\n",
        f"共 **{total}** 篇工具教程，按攻击阶段组织。每篇包含："
        "解决什么问题 → 工作原理 → 参数详解 → 靶场实操 → 输出解读 → 常见坑 → 防御视角。\n",
        "> ⚠️ 所有实操步骤仅适用于**你自己的靶场或获得授权的目标**。\n",
        "## 教程统计\n",
        "| 阶段 | 目录 | 篇数 | 说明 |",
        "|------|------|------|------|",
    ]
    for d, zh, desc, entries in sections:
        out.append(f"| {zh} | [{d}/]({d}/) | {len(entries)} | {desc} |")
    out.append("")

    out.append("## 怎么用\n")
    out.append("1. **零基础**：按上表顺序从上往下读（01 → 12），对应一次渗透测试的自然流程。")
    out.append("2. **补工具**：直接按工具名找对应的分类目录。")
    out.append("3. **查参数**：每个教程的「核心参数详解」一节可直接当速查表用。")
    out.append("4. **没写到的工具**：本目录只精讲重点工具；全部 780 个工具包的卡片在")
    out.append("   [`../catalog/`](../catalog/) 与 [`../by-attack/`](../by-attack/)，")
    out.append("   每张卡片含包名、命令、依赖、安装命令与官方文档链接。\n")

    # 官方重点工具（Top 100 页面）覆盖情况
    name2rel: dict[str, str] = {}
    for d, _zh, _desc, entries in sections:
        for fname, _title in entries:
            name2rel.setdefault(fname[:-3], f"{d}/{fname}")
    coverage = load_top100_coverage(name2rel)
    if coverage:
        hit = sum(1 for _p, _d, link in coverage if link != "—")
        out.append("## 官方重点工具覆盖情况\n")
        out.append(
            "Kali 官网 [Top 100 工具](<https://www.kali.org/tools/top-100/>) 页面收录了 "
            f"**{len(coverage)}** 个重点包。本目录的教程覆盖情况（脚本自动比对）：\n"
        )
        out.append(f"**{hit} / {len(coverage)}** 个已有深度教程。\n")
        out.append("| 包 | 说明 | 本库教程 |")
        out.append("|----|------|----------|")
        for pkg, desc, link in coverage:
            out.append(f"| `{pkg}` | {desc} | {link} |")
        out.append("")
        out.append(
            "> 没有教程的包并非没有收录——它们在 "
            "[`../catalog/`](../catalog/) 里有完整卡片（包名、命令、依赖、安装方式、官方链接）。\n"
        )

    out.append("## 工具清单\n")

    for d, zh, desc, entries in sections:
        out.append(f"### {zh}（[{d}/]({d}/)）\n")
        out.append(f"{desc}\n")
        if not entries:
            out.append("> 待补充\n")
            continue
        out.append("| 教程 | 内容 |")
        out.append("|------|------|")
        for fname, title in entries:
            name = fname[:-3]
            out.append(f"| [{name}]({d}/{fname}) | {title or '—'} |")
        out.append("")

    out.append("## 相关\n")
    out.append("- [工具总览](../index.md) —— 按攻击阶段与按包两种查法")
    out.append("- [按包速查卡片](../catalog/all-tools.md) —— 全量 780 个包")
    out.append("- [靶场搭建](../../labs/README.md) —— 练习环境")
    out.append("- [Kali 官方文档精读](../../docs/) —— 系统层知识")
    out.append("")

    dest = os.path.join(TUT_DIR, "README.md")
    with open(dest, "w", encoding="utf-8") as fh:
        fh.write("\n".join(out))

    print(f"[+] 共 {total} 篇教程，{len(sections)} 个分类 -> {dest}")
    for d, zh, _desc, entries in sections:
        print(f"    {len(entries):>3}  {zh:<16} {d}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
