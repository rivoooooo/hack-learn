#!/usr/bin/env python3
"""生成 Kali 工具目录文档。

用法:
    python3 scripts/gen_kali_index.py

依赖 data/kali-tools.json（fetch_kali_tools.py）与
     data/kali-categories.json（fetch_kali_categories.py）

产出:
    kali/tools/index.md                    功能分类总导航（ATT&CK 战术风格）
    kali/tools/by-attack/<分类>.md         各功能分类下的工具清单（命令级）
    kali/tools/catalog/<包分组>.md         按包速查卡片（全量）
    kali/tools/catalog/all-tools.md        全量 A–Z
    data/kali-tools.tsv                    扁平数据，便于 grep
"""
from __future__ import annotations

import collections
import json
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TOOLS_JSON = os.path.join(ROOT, "data", "kali-tools.json")
CATS_JSON = os.path.join(ROOT, "data", "kali-categories.json")
TOOLS_DIR = os.path.join(ROOT, "kali", "tools")
CATALOG_DIR = os.path.join(TOOLS_DIR, "catalog")
BYATTACK_DIR = os.path.join(TOOLS_DIR, "by-attack")

# 按包分组时使用的 metapackage 短名 -> 中文
GROUP_ZH = {
    "information-gathering": "信息搜集",
    "vulnerability": "漏洞分析",
    "web": "Web 应用",
    "passwords": "口令攻击",
    "wireless": "无线攻击",
    "802-11": "802.11 Wi-Fi",
    "bluetooth": "蓝牙",
    "exploitation": "漏洞利用",
    "sniffing-spoofing": "嗅探与欺骗",
    "post-exploitation": "后渗透",
    "forensics": "数字取证",
    "recover": "数据恢复",
    "reverse-engineering": "逆向工程",
    "reporting": "报告与记录",
    "social-engineering": "社会工程",
    "hardware": "硬件攻击",
    "rfid": "RFID / NFC",
    "sdr": "软件定义无线电",
    "voip": "VoIP",
    "database": "数据库",
    "fuzzing": "模糊测试",
    "crypto-stego": "密码学与隐写",
    "identify": "识别与指纹",
    "detect": "检测",
    "protect": "防护",
    "top10": "Top 10 常用",
    "respond": "事件响应",
    "windows-resources": "Windows 资源",
    "gpu": "GPU 计算",
    "utils": "通用工具",
    "Tool Documentation": "（页面标记）",
}
GROUP_ORDER = list(GROUP_ZH)


def slugify(name: str) -> str:
    s = re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")
    return s or "misc"


def load(path: str):
    with open(path, encoding="utf-8") as fh:
        return json.load(fh)


def primary_group(tool: dict) -> str:
    groups = [g for g in (tool.get("tool_groups") or []) if g != "Tool Documentation"]
    if not groups:
        return "utils"
    return min(groups, key=lambda g: GROUP_ORDER.index(g) if g in GROUP_ORDER else 999)


def card(tool: dict, zh_group: str) -> str:
    lines = [f"### {tool['name']}\n"]
    if tool.get("description"):
        lines.append(f"{tool['description']}\n")
    lines += ["| 项目 | 内容 |", "|------|------|"]
    lines.append(f"| 归入分组 | {zh_group} |")
    # 一个包常同时属于多个元包分组（如 wireshark 同时属于 web / forensics /
    # sniffing-spoofing 等）。卡片只归入其中一个文件，但把全部归属列出来，避免误导。
    all_groups = [g for g in tool.get("tool_groups") or [] if g != "Tool Documentation"]
    if len(all_groups) > 1:
        names = [GROUP_ZH.get(g, g) for g in all_groups]
        shown = "、".join(names[:8])
        if len(names) > 8:
            shown += f" 等 {len(names)} 个"
        lines.append(f"| 全部所属分组 | {shown} |")
    lines.append(f"| Kali 文档 | <{tool['url']}> |")
    if tool.get("version"):
        lines.append(f"| 版本 | {tool['version']} |")
    if tool.get("packages"):
        # 页面会同时以 Source/Package/Command 三种图标列出条目，同名会重复，这里去重保序
        pkgs = list(dict.fromkeys(tool["packages"]))
        lines.append("| 包 / 命令 | " + "、".join(f"`{p}`" for p in pkgs) + " |")
    lines.append(f"| 安装 | `{tool['install']}` |")
    if tool.get("installed_size"):
        lines.append(f"| 占用空间 | {tool['installed_size']} |")
    if tool.get("dependencies"):
        deps = tool["dependencies"][:12]
        more = " 等" if len(tool["dependencies"]) > 12 else ""
        lines.append("| 依赖 | " + "、".join(f"`{d}`" for d in deps) + more + " |")
    if tool.get("homepage"):
        lines.append(f"| 官网 | <{tool['homepage']}> |")
    if tool.get("source_repo"):
        lines.append(f"| 源码 | <{tool['source_repo']}> |")
    lines.append("")
    return "\n".join(lines)


def main() -> int:
    tools = load(TOOLS_JSON)
    cats = load(CATS_JSON)
    by_slug = {t["slug"]: t for t in tools}

    os.makedirs(CATALOG_DIR, exist_ok=True)
    os.makedirs(BYATTACK_DIR, exist_ok=True)

    # ---------- 1) 按包分组速查卡片 ----------
    buckets: dict[str, list[dict]] = collections.defaultdict(list)
    for t in tools:
        buckets[primary_group(t)].append(t)

    catalog_files: list[tuple[str, str, int]] = []
    for group, items in buckets.items():
        items.sort(key=lambda t: t["name"].lower())
        zh = GROUP_ZH.get(group, group)
        fname = f"{slugify(group)}.md"
        body = [
            f"# 按包速查：{zh}（{group}）\n",
            f"> 共 **{len(items)}** 个包 · 数据来源 <https://www.kali.org/tools/all-tools/>\n",
            "返回 [工具总览](../index.md) · [全量清单](all-tools.md) · "
            "[按功能分类](../index.md#功能分类导航)\n",
            "---\n",
        ]
        body += [card(t, zh) for t in items]
        with open(os.path.join(CATALOG_DIR, fname), "w", encoding="utf-8") as fh:
            fh.write("\n".join(body))
        catalog_files.append((group, fname, len(items)))

    # ---------- 2) 全量 A–Z ----------
    all_body = [
        "# Kali 全量工具清单（A–Z）\n",
        f"> 共 **{len(tools)}** 个包 · 数据来源 <https://www.kali.org/tools/all-tools/>\n",
        "返回 [工具总览](../index.md)\n",
        "---\n",
    ]
    for t in sorted(tools, key=lambda x: x["slug"]):
        grp = GROUP_ZH.get(primary_group(t), primary_group(t))
        pkgs = "、".join(f"`{p}`" for p in dict.fromkeys(t.get("packages") or [])) or "-"
        line = (
            f"- **[{t['name']}](<{t['url']}>)** · `{grp}` · "
            f"{t.get('description') or '（无描述）'}\n"
            f"  - 包/命令：{pkgs} · 安装：`{t['install']}`"
        )
        if t.get("homepage"):
            line += f" · 官网：<{t['homepage']}>"
        all_body.append(line)
    with open(os.path.join(CATALOG_DIR, "all-tools.md"), "w", encoding="utf-8") as fh:
        fh.write("\n".join(all_body))

    # ---------- 3) 扁平 TSV ----------
    with open(os.path.join(ROOT, "data", "kali-tools.tsv"), "w", encoding="utf-8") as fh:
        fh.write("slug\tname\tpackage_group\tattack_category\tpackages\tdescription\turl\n")
        attack_of: dict[str, str] = {}
        for c in cats["categories"]:
            for s in c["subcategories"]:
                for t in s["tools"]:
                    attack_of.setdefault(t["package"], c["zh"] or c["name"])
        for t in sorted(tools, key=lambda x: x["slug"]):
            fh.write(
                "\t".join(
                    [
                        t["slug"],
                        t["name"],
                        primary_group(t),
                        attack_of.get(t["slug"], ""),
                        ",".join(t.get("packages") or []),
                        (t.get("description") or "").replace("\t", " "),
                        t["url"],
                    ]
                )
                + "\n"
            )

    # ---------- 4) 按功能分类（ATT&CK 战术风格）----------
    stats = cats["stats"]
    covered: set[str] = set()
    cat_files: list[tuple[dict, str, int]] = []
    for c in cats["categories"]:
        zh = c["zh"] or c["name"]
        fname = f"{slugify(c['id'])}.md"
        ncmds = sum(len(s["tools"]) for s in c["subcategories"])
        body = [
            f"# {zh}（{c['name']}）\n",
            f"> {c.get('description', '')}\n",
            f"> 子类别 **{len(c['subcategories'])}** 个 · 命令 **{ncmds}** 条 · "
            "来源 <https://www.kali.org/tools/>\n",
            "返回 [工具总览](../index.md)\n",
            "---\n",
        ]
        for s in c["subcategories"]:
            szh = s["zh"] or s["name"]
            body.append(f"## {szh}（{s['name']}）\n")
            body.append("| 命令 | 所属包 | 说明 | 链接 |")
            body.append("|------|--------|------|------|")
            for t in sorted(s["tools"], key=lambda x: x["command"].lower()):
                pkg = t["package"]
                covered.add(pkg)
                meta = by_slug.get(pkg, {})
                desc = (meta.get("description") or "").strip()
                if len(desc) > 90:
                    desc = desc[:87] + "…"
                desc = desc.replace("|", "\\|")
                body.append(
                    f"| `{t['command']}` | [{pkg}](<{meta.get('url', t['url'])}>) "
                    f"| {desc} | [官方](<{t['url']}>) |"
                )
            body.append("")
        with open(os.path.join(BYATTACK_DIR, fname), "w", encoding="utf-8") as fh:
            fh.write("\n".join(body))
        cat_files.append((c, fname, ncmds))

    # ---------- 5) 总导航 ----------
    idx: list[str] = []
    idx.append("# Kali 工具库总览\n")
    idx.append(
        f"收录 Kali Linux 官方工具文档中的 **{len(tools)}** 个工具包、"
        f"**{stats['command_entries']}** 条命令级条目，覆盖 **{stats['categories']}** "
        "个功能分类。全部数据由脚本从官网同步，可随时复核。\n"
    )
    idx.append("## 两种查法\n")
    idx.append("| 你想做什么 | 去哪查 |")
    idx.append("|------------|--------|")
    idx.append("| 按**攻击阶段**找工具（先侦察？要提权？） | [按功能分类](#功能分类导航) |")
    idx.append("| 按**包名/命令名**找细节 | [catalog/ 按包速查](catalog/all-tools.md) |")
    idx.append(
        "| **从零开始用一个工具**（安装 → 官方示例 → 参数 → 实践清单） "
        "| [reference/ 工具参考文档](reference/README.md) |"
    )
    idx.append("| 学重点工具的完整用法（原理 + 靶场实操） | [tutorials/](tutorials/README.md) |")
    idx.append("| 直接搜索 | `grep -i '关键词' data/kali-tools.tsv` |\n")

    idx.append("## 功能分类导航\n")
    idx.append(
        "Kali 官方按**攻击/防御阶段**组织工具（命名参考 MITRE ATT&CK 战术）。"
        "下表按官方顺序排列：\n"
    )
    idx.append("| 分类 | 子类 | 命令数 | 说明 | 目录 |")
    idx.append("|------|------|--------|------|------|")
    for c, fname, ncmds in cat_files:
        zh = c["zh"] or c["name"]
        idx.append(
            f"| **{zh}** | {len(c['subcategories'])} | {ncmds} "
            f"| {c.get('description', '')} | [{c['name']}](by-attack/{fname}) |"
        )
    idx.append("")
    idx.append("## 按包速查（全量）\n")
    idx.append("| 分组 | 包数 | 目录 |")
    idx.append("|------|------|------|")
    for group, fname, count in sorted(
        catalog_files, key=lambda x: GROUP_ORDER.index(x[0]) if x[0] in GROUP_ORDER else 999
    ):
        idx.append(f"| {GROUP_ZH.get(group, group)} | {count} | [catalog/{fname}](catalog/{fname}) |")
    idx.append(f"\n全量 A–Z 清单：▶ [catalog/all-tools.md](catalog/all-tools.md)\n")

    idx.append("## 使用示例\n")
    idx.append("```bash")
    idx.append("# 找所有口令攻击类工具")
    idx.append("awk -F'\\t' '$3==\"passwords\" {print $2, \"|\", $6}' data/kali-tools.tsv")
    idx.append("")
    idx.append("# 按 ATT&CK 分类名过滤")
    idx.append("awk -F'\\t' '$4==\"凭据访问\" {print $2}' data/kali-tools.tsv")
    idx.append("")
    idx.append("# 搜索描述里含 SQL 注入的工具")
    idx.append("grep -i 'sql injection' data/kali-tools.tsv | cut -f1,2")
    idx.append("```\n")

    idx.append("## 数据来源与维护\n")
    idx.append("```bash")
    idx.append("# 重新同步工具元数据（约 800 个页面，1–2 分钟）")
    idx.append("python3 scripts/fetch_kali_tools.py --workers 6")
    idx.append("# 重新同步功能分类树")
    idx.append("python3 scripts/fetch_kali_categories.py")
    idx.append("# 重新生成本目录")
    idx.append("python3 scripts/gen_kali_index.py")
    idx.append("```\n")
    idx.append("- 工具元数据：<https://www.kali.org/tools/all-tools/>")
    idx.append("- 功能分类树：<https://www.kali.org/tools/>")
    idx.append(f"- 未被功能分类收录的包：{len(tools) - len(covered)} 个（多为依赖库或元包）\n")

    with open(os.path.join(TOOLS_DIR, "index.md"), "w", encoding="utf-8") as fh:
        fh.write("\n".join(idx))

    print(f"[+] 工具包 {len(tools)} 个 · 功能分类 {len(cat_files)} 个 · 包分组 {len(catalog_files)} 个")
    print(f"[+] 分类文档 -> kali/tools/by-attack/")
    print(f"[+] 包卡片   -> kali/tools/catalog/")
    print(f"[+] 导航     -> kali/tools/index.md")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
