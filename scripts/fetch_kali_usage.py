#!/usr/bin/env python3
"""抓取每个 Kali 工具页内嵌的「官方用法示例」与各命令的 `-h`/man 原文。

用法:
    python3 scripts/fetch_kali_usage.py
    python3 scripts/fetch_kali_usage.py --workers 6 --limit 20

产出:
    data/kali-tool-usage.json

说明:
    Kali 官方工具页除了描述，还内嵌了两类实践素材：
      1. "Usage Example" —— 官方给出的典型命令与**真实输出**；
      2. 每个可执行命令的 `-h` / `man` 输出原文（页面里以 `root@kali:~#` 提示符开头）。
    这些是官网原文而非二手转述，用来为每个工具包生成可操作的参考文档。
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
UA = "Mozilla/5.0 (X11; Linux x86_64) hack-learn-study-library/1.0"
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TOOLS_JSON = os.path.join(ROOT, "data", "kali-tools.json")
OUT = os.path.join(ROOT, "data", "kali-tool-usage.json")

MAX_CMD_BLOCKS = 10      # 每个包最多保留多少个命令的使用说明
MAX_LINES_PER_CMD = 220  # 单个命令 help 最多保留多少行
MAX_EXAMPLE_CHARS = 4000  # 官方示例最多保留多少字符
PROMPT = "root@kali:~#"


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
    body = re.sub(r"<(script|style)[^>]*>.*?</\1>", "", raw_html, flags=re.S)
    text = html.unescape(re.sub(r"<[^>]+>", "\n", body))
    return [ln.rstrip() for ln in text.split("\n") if ln.strip()]


def meta_description(raw: str) -> str:
    m = re.search(r'itemprop=description content="(.*?)">', raw, re.S)
    return html.unescape(m.group(1)).strip() if m else ""


def extract_usage(tool: dict, raw: str) -> dict:
    lines = visible_lines(raw)
    packages = set(tool.get("packages") or [])
    prompt_rows = [i for i, l in enumerate(lines) if l.startswith(PROMPT)]

    blocks: list[dict] = []
    for k, i in enumerate(prompt_rows[: MAX_CMD_BLOCKS * 3]):
        end = prompt_rows[k + 1] if k + 1 < len(prompt_rows) else len(lines)
        # 不越过下一个命令段落的起点（包名行）
        for j in range(i + 1, end):
            if lines[j] in packages:
                end = j
                break
        chunk = lines[i:end][:MAX_LINES_PER_CMD]
        if not chunk:
            continue
        cmdline = chunk[0][len(PROMPT) :].strip()
        # 找出该块里的 Usage 行，作为"最小可用形式"的提示
        usage = next((l.strip() for l in chunk if l.strip().startswith("Usage")), "")
        blocks.append({"cmdline": cmdline, "usage": usage, "text": "\n".join(chunk)})
        if len(blocks) >= MAX_CMD_BLOCKS:
            break

    example = meta_description(raw)
    if "Usage Example" in example:
        example = example[example.index("Usage Example") :]
    example = example[:MAX_EXAMPLE_CHARS].strip()

    return {
        "slug": tool["slug"],
        "name": tool["name"],
        "usage_example": example,
        "commands": blocks,
        "has_prompt": bool(prompt_rows),
    }


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--workers", type=int, default=6)
    ap.add_argument("--limit", type=int, default=0)
    args = ap.parse_args()

    with open(TOOLS_JSON, encoding="utf-8") as fh:
        tools = json.load(fh)
    if args.limit:
        tools = tools[: args.limit]
    print(f"[*] 共 {len(tools)} 个工具页面待抓取", flush=True)

    results: list[dict] = []
    failed: list[str] = []

    def work(t: dict) -> dict | None:
        try:
            return extract_usage(t, get(f"{BASE}/tools/{t['slug']}/"))
        except Exception as exc:  # noqa: BLE001
            print(f"[!] {t['slug']}: {exc}", file=sys.stderr)
            failed.append(t["slug"])
            return None

    with cf.ThreadPoolExecutor(max_workers=args.workers) as pool:
        for i, r in enumerate(pool.map(work, tools), 1):
            if r:
                results.append(r)
            if i % 50 == 0:
                print(f"    进度 {i}/{len(tools)}", flush=True)

    results.sort(key=lambda r: r["slug"])
    with open(OUT, "w", encoding="utf-8") as fh:
        json.dump(results, fh, ensure_ascii=False, indent=1)

    with_example = sum(1 for r in results if r["usage_example"])
    with_cmds = sum(1 for r in results if r["commands"])
    total_cmds = sum(len(r["commands"]) for r in results)
    size_mb = os.path.getsize(OUT) / 1024 / 1024
    print(
        f"[+] 成功 {len(results)} / 失败 {len(failed)} · "
        f"含官方示例 {with_example} · 含命令说明 {with_cmds} · "
        f"命令块合计 {total_cmds} · 输出 {size_mb:.1f} MB"
    )
    if failed:
        print("[!] 失败:", ", ".join(failed[:20]))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
