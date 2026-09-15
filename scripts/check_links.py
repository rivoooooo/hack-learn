#!/usr/bin/env python3
"""校验仓库内 Markdown 的相对链接是否指向真实存在的文件。

用法:
    python3 scripts/check_links.py              # 只报断链
    python3 scripts/check_links.py --anchors     # 同时校验 #锚点
    python3 scripts/check_links.py --list-ok     # 也列出正常链接

退出码: 有断链时返回 1，便于接入 CI。
"""
from __future__ import annotations

import argparse
import os
import re
import sys
import urllib.parse

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 跳过这些目录
SKIP_DIRS = {".git", "node_modules", "__pycache__", "src"}
# 匹配 Markdown 链接与图片：[文本](目标) / ![alt](目标)
LINK_RE = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
# 匹配标题，用于锚点校验
HEADING_RE = re.compile(r"^#{1,6}\s+(.*)$", re.M)


def slugify_heading(text: str) -> str:
    """按 github-slugger 的规则生成锚点。

    规则：转小写 → 去掉行内代码/链接的标记 → 移除非字母数字（保留中文、`_`、`-`、空格）
    → 把每个空格替换为 `-`（**不压缩连续空格**，因此 "a + b" 会得到 "a--b"）。
    """
    s = text.strip().lower()
    s = re.sub(r"`([^`]*)`", r"\1", s)
    s = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", s)
    s = re.sub(r"[^\w\u4e00-\u9fff\s-]", "", s)
    return s.replace(" ", "-")


def iter_links(text: str):
    """产出 (行号, 链接目标)，跳过 fenced code block 内的内容。

    代码块里的 `[xx](+yy)` 这类文本不会被渲染成链接（例如 safecopy 的 help 原文里
    就有进度指示符 `[xx](+yy)`），必须排除，否则会产生误报。
    """
    in_fence = False
    fence_marker = ""
    for lineno, line in enumerate(text.split("\n"), 1):
        stripped = line.lstrip()
        m = re.match(r"(`{3,}|~{3,})", stripped)
        if m:
            marker = m.group(1)
            if not in_fence:
                in_fence, fence_marker = True, marker[0] * len(marker)
            elif marker[0] == fence_marker[0] and len(marker) >= len(fence_marker):
                in_fence, fence_marker = False, ""
            continue
        if in_fence:
            continue
        for target in LINK_RE.findall(line):
            yield lineno, target


def collect_headings(path: str) -> set[str]:
    try:
        with open(path, encoding="utf-8") as fh:
            text = fh.read()
    except OSError:
        return set()
    out = {slugify_heading(m) for m in HEADING_RE.findall(text)}
    return out


def iter_md_files() -> list[str]:
    files = []
    for dirpath, dirnames, filenames in os.walk(ROOT):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
        for f in filenames:
            if f.endswith((".md", ".markdown")):
                files.append(os.path.join(dirpath, f))
    return sorted(files)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--anchors", action="store_true", help="同时校验锚点")
    ap.add_argument("--list-ok", action="store_true", help="列出正常链接")
    args = ap.parse_args()

    files = iter_md_files()
    broken: list[tuple[str, str, str]] = []
    checked = 0
    external = 0
    heading_cache: dict[str, set[str]] = {}

    for path in files:
        rel_src = os.path.relpath(path, ROOT)
        try:
            with open(path, encoding="utf-8") as fh:
                text = fh.read()
        except OSError as exc:
            print(f"[!] 无法读取 {rel_src}: {exc}", file=sys.stderr)
            continue

        for lineno, target in iter_links(text):
            target = target.strip()
            # 去掉 CommonMark 的可选尖括号包裹，再判断类型
            if target.startswith("<") and target.endswith(">"):
                target = target[1:-1].strip()
            if not target:
                continue
            if target.startswith(("http://", "https://", "mailto:")):
                external += 1
                continue
            if target.startswith("#"):
                continue

            raw_path, _, anchor = target.partition("#")
            raw_path = urllib.parse.unquote(raw_path)
            checked += 1

            if raw_path.startswith("/"):
                dest = os.path.join(ROOT, raw_path.lstrip("/"))
            else:
                dest = os.path.normpath(os.path.join(os.path.dirname(path), raw_path))

            exists_file = os.path.exists(dest)
            if not exists_file:
                broken.append((f"{rel_src}:{lineno}", target, "文件不存在"))
                continue

            if args.anchors and anchor and os.path.isfile(dest):
                if dest not in heading_cache:
                    heading_cache[dest] = collect_headings(dest)
                if anchor.lower() not in heading_cache[dest]:
                    broken.append((f"{rel_src}:{lineno}", target, "锚点不存在"))
            elif args.list_ok:
                print(f"[ok] {rel_src}:{lineno} -> {target}")

    print()
    print(f"扫描 {len(files)} 个 Markdown 文件")
    print(f"  内部链接检查 {checked} 条，外部链接 {external} 条（未检查）")
    if broken:
        print(f"\n[!] 发现 {len(broken)} 条断链：\n")
        for src, target, reason in broken:
            print(f"  {src}\n      -> {target}   [{reason}]")
        return 1

    print("\n[+] 未发现断链")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
