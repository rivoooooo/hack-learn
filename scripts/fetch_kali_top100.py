#!/usr/bin/env python3
"""抓取 kali.org/tools/top-100/ 的官方重点工具清单。

用法:
    python3 scripts/fetch_kali_top100.py

产出:
    data/kali-top100.json

说明:
    该页面是 Kali 官方维护的"最常用工具"精选视图，用作教程覆盖度的基准：
    scripts/gen_tutorials_index.py 会用它比对哪些重点工具已有深度教程。
"""
from __future__ import annotations

import json
import os
import re
import urllib.request

URL = "https://www.kali.org/tools/top-100/"
UA = "Mozilla/5.0 (X11; Linux x86_64) hack-learn-study-library/1.0"
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def main() -> int:
    req = urllib.request.Request(URL, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=60) as resp:
        raw = resp.read().decode("utf-8", "replace")

    hits = re.findall(
        r"href=https://www\.kali\.org/tools/([a-z0-9._+-]+)/#([a-z0-9._+-]+)", raw
    )
    packages = sorted({p for p, _ in hits})

    out = {
        "source": URL,
        "packages": packages,
        "command_entries": len(hits),
    }
    dest = os.path.join(ROOT, "data", "kali-top100.json")
    with open(dest, "w", encoding="utf-8") as fh:
        json.dump(out, fh, ensure_ascii=False, indent=1)

    print(f"[+] 重点包 {len(packages)} 个 · 命令条目 {len(hits)} 条 -> {dest}")
    print("    " + ", ".join(packages[:20]) + (" ..." if len(packages) > 20 else ""))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
