#!/usr/bin/env python3
"""抓取 kali.org/docs 全量文档的标题、正文大纲与首段摘要。

用法:
    python3 scripts/fetch_kali_docs.py
    python3 scripts/fetch_kali_docs.py --workers 6 --limit 20

产出:
    data/kali-docs.json                  结构化数据
    kali/docs/official-index.md          官方文档全量索引（按章节组织）
"""
from __future__ import annotations

import argparse
import concurrent.futures as cf
import html
import json
import os
import re
import sys
import time
import urllib.error
import urllib.request

SITEMAP = "https://www.kali.org/sitemap.xml"
UA = "Mozilla/5.0 (X11; Linux x86_64) hack-learn-study-library/1.0"
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 官方文档章节 -> 中文名与说明（顺序即官网导航顺序）
CHAPTERS: list[tuple[str, str, str]] = [
    ("introduction", "介绍", "Kali 是什么、能做什么、版本与政策"),
    ("installation", "安装", "镜像获取、安装方式、加密磁盘、USB 启动"),
    ("general-use", "常规使用", "sudo、SSH、桌面环境、软件源、Python、显卡驱动"),
    ("tools", "工具相关", "工具分类说明与 metapackage 结构"),
    ("virtualization", "虚拟化", "VirtualBox / VMware / Hyper-V / QEMU / Docker / WSL"),
    ("containers", "容器", "Docker、Podman 与容器化 Kali"),
    ("cloud", "云环境", "AWS / Azure / Linode 等云上 Kali"),
    ("wsl", "WSL", "Windows Subsystem for Linux 中的 Kali"),
    ("usb", "USB 启动", "制作启动盘、持久化存储、加密持久化"),
    ("arm", "ARM 与单板机", "树莓派、ARM 设备、chroot"),
    ("nethunter", "Kali NetHunter", "移动端渗透平台"),
    ("nethunter-pro", "NetHunter Pro", "NetHunter Pro 设备与用法"),
    ("development", "开发与打包", "Debian 打包、Kali 源码、贡献流程"),
    ("troubleshooting", "故障排查", "常见问题、显卡、网络、双系统"),
    ("policy", "政策与法律", "使用政策、商标、法律边界"),
    ("community", "社区", "论坛、Discord、参与方式"),
    ("", "根文档", "文档入口页"),
]
CHAPTER_ZH = {en: zh for en, zh, _ in CHAPTERS}
CHAPTER_DESC = {en: d for en, _, d in CHAPTERS}


def get(url: str, retries: int = 3, timeout: int = 45) -> str:
    last: Exception | None = None
    for attempt in range(retries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA})
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                return resp.read().decode("utf-8", "replace")
        except (urllib.error.URLError, TimeoutError, OSError) as exc:
            last = exc
            time.sleep(1.5 * (attempt + 1))
    raise RuntimeError(f"请求失败 {url}: {last}")


def list_docs() -> list[str]:
    raw = get(SITEMAP)
    urls = sorted(set(re.findall(r"<loc>(https://www\.kali\.org/docs/[^<]*)</loc>", raw)))
    return [u for u in urls if not u.endswith("/docs/")]


def extract(url: str, raw: str) -> dict:
    title = ""
    m = re.search(r"<title[^>]*>(.*?)</title>", raw, re.S)
    if m:
        title = html.unescape(re.sub(r"\s+", " ", m.group(1))).strip()
        title = re.sub(r"\s*\|\s*Kali Linux Documentation\s*$", "", title)

    # 正文容器
    i = raw.find("<div id=content")
    if i == -1:
        i = raw.find('<div id="content"')
    j = raw.find("<div id=pagination", i if i > 0 else 0)
    body_html = raw[i:j] if i > 0 and j > i else raw

    headings = [
        (int(lvl), html.unescape(re.sub(r"<[^>]+>", "", txt)).strip())
        for lvl, txt in re.findall(r"<h([1-3])[^>]*>(.*?)</h\1>", body_html, re.S)
    ]
    headings = [(l, t) for l, t in headings if t and len(t) < 120]

    text = html.unescape(re.sub(r"<[^>]+>", " ", body_html))
    text = re.sub(r"\s+", " ", text).strip()
    summary = text[:300]

    parts = url.replace("https://www.kali.org/docs/", "").strip("/").split("/")
    chapter = parts[0] if len(parts) > 1 else ""
    slug = parts[-1]

    return {
        "url": url,
        "title": title,
        "chapter": chapter,
        "chapter_zh": CHAPTER_ZH.get(chapter, chapter),
        "slug": slug,
        "headings": [{"level": l, "text": t} for l, t in headings],
        "summary": summary,
    }


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--workers", type=int, default=6)
    ap.add_argument("--limit", type=int, default=0)
    args = ap.parse_args()

    print("[*] 读取 sitemap ...", flush=True)
    urls = list_docs()
    if args.limit:
        urls = urls[: args.limit]
    print(f"[*] 共 {len(urls)} 篇官方文档", flush=True)

    results: list[dict] = []
    failed: list[str] = []

    def work(u: str) -> dict | None:
        try:
            return extract(u, get(u))
        except Exception as exc:  # noqa: BLE001
            print(f"[!] {u}: {exc}", file=sys.stderr)
            failed.append(u)
            return None

    with cf.ThreadPoolExecutor(max_workers=args.workers) as pool:
        for i, r in enumerate(pool.map(work, urls), 1):
            if r:
                results.append(r)
            if i % 50 == 0:
                print(f"    进度 {i}/{len(urls)}", flush=True)

    results.sort(key=lambda r: (r["chapter"], r["slug"]))
    with open(os.path.join(ROOT, "data", "kali-docs.json"), "w", encoding="utf-8") as fh:
        json.dump(results, fh, ensure_ascii=False, indent=1)

    # 生成官方文档全量索引
    grouped: dict[str, list[dict]] = {}
    for r in results:
        grouped.setdefault(r["chapter"], []).append(r)

    out = [
        "# Kali 官方文档全量索引\n",
        f"从 <https://www.kali.org/docs/> 同步的 **{len(results)}** 篇官方文档，"
        "按官方章节组织。每篇给出标题、原文链接与内文标题大纲，便于定位。\n",
        "> 本文件由 `scripts/fetch_kali_docs.py` 自动生成。"
        "配套的中文精读笔记见本目录其余 `NN-*.md` 文件。\n",
        "## 章节速览\n",
        "| 章节 | 中文 | 篇数 | 说明 |",
        "|------|------|------|------|",
    ]
    for en, zh, desc in CHAPTERS:
        n = len(grouped.get(en, []))
        if n == 0:
            continue
        anchor = en or "root"
        out.append(f"| [{en or '(根)'}](#{anchor}) | {zh} | {n} | {desc} |")
    out.append("")

    for en, zh, desc in CHAPTERS:
        items = grouped.get(en)
        if not items:
            continue
        out.append(f"## {zh}（`{en or 'docs'}`）\n")
        out.append(f"{desc} · 共 **{len(items)}** 篇\n")
        for r in sorted(items, key=lambda x: x["title"].lower()):
            out.append(f"### [{r['title']}](<{r['url']}>)\n")
            subs = [h["text"] for h in r["headings"] if h["level"] >= 2][:12]
            if subs:
                out.append("内文小节：" + " · ".join(f"`{s}`" for s in subs) + "\n")
            if r["summary"]:
                out.append(f"摘要：{r['summary'][:200]}…\n")
        out.append("")

    with open(os.path.join(ROOT, "kali", "docs", "official-index.md"), "w", encoding="utf-8") as fh:
        fh.write("\n".join(out))

    print(f"[+] 成功 {len(results)} / 失败 {len(failed)}")
    if failed:
        print("[!] 失败:", ", ".join(failed[:20]))
    print("[+] -> data/kali-docs.json, kali/docs/official-index.md")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
