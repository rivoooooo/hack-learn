#!/usr/bin/env python3
"""抓取 kali.org/tools 全部工具元数据，输出 data/kali-tools.json。

用法:
    python3 scripts/fetch_kali_tools.py             # 抓取全部工具
    python3 scripts/fetch_kali_tools.py --limit 20  # 只抓 20 个（调试）
    python3 scripts/fetch_kali_tools.py --workers 6

数据来源: https://www.kali.org/tools/all-tools/
仅做公开页面抓取，默认 6 并发 + 重试退避，请勿高频请求。
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

BASE = "https://www.kali.org"
ALL_TOOLS = f"{BASE}/tools/all-tools/"
UA = "Mozilla/5.0 (X11; Linux x86_64) hack-learn-study-library/1.0"
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "data", "kali-tools.json")

SKIP_SLUGS = {"all-tools", "top-100", "index", "pages"}
UI_NOISE = {"LIGHT", "DARK", "Home", "Back to top"}
# 合法包名形态，用于过滤页面导航噪声混入依赖/包列表
PKG_RE = re.compile(r"^[a-z0-9][a-z0-9.+_-]*$")


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


def visible_lines(raw_html: str) -> list[str]:
    """把 HTML 转成去掉标签后的可见文本行。"""
    body = re.sub(r"<(script|style)[^>]*>.*?</\1>", "", raw_html, flags=re.S)
    text = html.unescape(re.sub(r"<[^>]+>", "\n", body))
    return [ln.strip() for ln in text.split("\n") if ln.strip()]


def list_slugs() -> list[str]:
    raw = get(ALL_TOOLS)
    slugs = set(re.findall(r"/tools/([a-z0-9][a-z0-9._+-]*)/", raw))
    slugs -= SKIP_SLUGS
    return sorted(slugs)


def parse_tool(slug: str, raw: str) -> dict:
    lines = visible_lines(raw)
    try:
        start = next(i for i, l in enumerate(lines) if l.startswith("version:"))
    except StopIteration:
        start = 0

    # 显示名优先取 <title>（形如 "dex2jar | Kali Linux Tools"），避免抓到相邻行噪声
    name = slug
    m = re.search(r"<title[^>]*>(.*?)</title>", raw, re.S)
    if m:
        candidate = html.unescape(re.sub(r"\s+", " ", m.group(1))).strip()
        candidate = re.sub(r"\s*\|\s*Kali Linux Tools\s*$", "", candidate)
        if candidate:
            name = candidate
    body = lines[start:]

    labels = {
        "Categories",
        "Metapackages",
        "Tools:",
        "Packages & Binaries",
        "Packages and Binaries:",
        "Files:",
        "Installed size:",
        "How to install:",
        "Dependencies:",
        "Comments",
    }

    def collect(label: str, extra_stop: set[str] | None = None) -> list[str]:
        """收集 label 之后、遇到下一个章节标题/UI 噪声为止的行。"""
        try:
            i = body.index(label)
        except ValueError:
            return []
        stop = labels | UI_NOISE | (extra_stop or set())
        out: list[str] = []
        for ln in body[i + 1 :]:
            if ln in stop or (ln.endswith(":") and len(ln) < 40):
                break
            out.append(ln)
        return out

    def collect_packages(label: str, extra_stop: set[str] | None = None) -> list[str]:
        """包/命令列表：只接受形如包名的行，遇到噪声立即停止。"""
        out: list[str] = []
        for ln in collect(label, extra_stop):
            if not PKG_RE.match(ln):
                break
            out.append(ln)
        return out

    version = arch = ""
    for ln in body[:6]:
        if ln.startswith("version:"):
            version = ln.split(":", 1)[1].strip()
        elif ln.startswith("arch:"):
            arch = ln.split(":", 1)[1].strip()

    categories = collect("Categories")
    metapackages = collect_packages("Metapackages")
    tool_groups = collect("Tools:")
    packages = collect_packages("Packages & Binaries")
    files = collect("Files:")

    # 一个工具页面里可能依次列出多个包（如 nmap 页含 ncat、ndiff…）。
    # 先定位与 slug 同名的那一段，后续的「描述 / 体积 / 安装 / 依赖」都从这一段里取，
    # 否则会拿到相邻包的信息（曾导致 wireshark 的安装命令被解析成 libwireshark-data）。
    seg_start = 0
    if "Packages and Binaries:" in body:
        base = body.index("Packages and Binaries:")
        seg_start = base + 1
        for j in range(base + 1, len(body)):
            if body[j] == slug:
                seg_start = j
                break

    def find_after(label: str) -> int:
        """返回 label 在 slug 所属段落之后的首次出现位置，找不到返回 -1。"""
        try:
            return seg_start + body[seg_start:].index(label)
        except ValueError:
            return -1

    installed_size = ""
    i = find_after("Installed size:")
    if i >= 0 and i + 1 < len(body):
        installed_size = body[i + 1]

    install_cmd = ""
    i = find_after("How to install:")
    if i >= 0 and i + 1 < len(body):
        install_cmd = body[i + 1]

    # 依赖：只收集形如包名的行，遇到第一个非包名行即停止
    deps: list[str] = []
    i = find_after("Dependencies:")
    if i >= 0:
        for ln in body[i + 1 :]:
            if not PKG_RE.match(ln):
                break
            deps.append(ln)

    # 描述：slug 段落的包名之后到下一个章节标题之间的文字
    description = ""
    start = seg_start + 1 if seg_start else 0
    buf: list[str] = []
    for ln in body[start:]:
        if ln in labels or ln in ("Installed size:", "How to install:"):
            break
        if buf and ln in packages:
            break
        if len(buf) >= 6:
            break
        buf.append(ln)
    description = " ".join(buf).strip()

    # 官网 / 源码 / 包追踪（注意 Kali 用无引号 href，图标标签夹在中间）
    link = r'<a href="?(https?://[^" >]+)"?[^>]*>(?:<[^>]+></[^>]+>)?\s*[^<]*'
    homepage = source = tracker = ""
    m = re.search(link + "Homepage", raw)
    if m:
        homepage = m.group(1)
    m = re.search(link + "Source Code Repository", raw)
    if m:
        source = m.group(1)
    m = re.search(link + "Package Tracker", raw)
    if m:
        tracker = m.group(1)

    return {
        "slug": slug,
        "name": name,
        "url": f"{BASE}/tools/{slug}/",
        "version": version,
        "arch": arch,
        "categories": categories,
        "tool_groups": tool_groups,
        "metapackages": metapackages,
        "packages": packages,
        "files": files,
        "description": description,
        "installed_size": installed_size,
        "install": install_cmd or f"sudo apt install {slug}",
        "dependencies": deps,
        "homepage": homepage,
        "source_repo": source,
        "package_tracker": tracker,
    }


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--workers", type=int, default=6)
    ap.add_argument("--out", default=OUT)
    args = ap.parse_args()

    print("[*] 获取工具清单 ...", flush=True)
    slugs = list_slugs()
    if args.limit:
        slugs = slugs[: args.limit]
    print(f"[*] 共 {len(slugs)} 个工具页面待抓取", flush=True)

    results: list[dict] = []
    failed: list[str] = []

    def work(s: str) -> dict | None:
        try:
            return parse_tool(s, get(f"{BASE}/tools/{s}/"))
        except Exception as exc:  # noqa: BLE001
            print(f"[!] {s}: {exc}", file=sys.stderr)
            failed.append(s)
            return None

    with cf.ThreadPoolExecutor(max_workers=args.workers) as pool:
        for i, res in enumerate(pool.map(work, slugs), 1):
            if res:
                results.append(res)
            if i % 50 == 0:
                print(f"    进度 {i}/{len(slugs)}", flush=True)

    results.sort(key=lambda r: r["slug"])
    os.makedirs(os.path.dirname(args.out), exist_ok=True)
    with open(args.out, "w", encoding="utf-8") as fh:
        json.dump(results, fh, ensure_ascii=False, indent=1)

    print(f"[+] 成功 {len(results)} / 失败 {len(failed)} -> {args.out}")
    if failed:
        print("[!] 失败列表:", ", ".join(failed[:40]))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
