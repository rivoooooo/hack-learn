#!/usr/bin/env python3
"""抓取 kali.org/tools/ 首页的功能分类树（ATT&CK 战术 → 子类别 → 工具命令）。

用法:
    python3 scripts/fetch_kali_categories.py

产出:
    data/kali-categories.json

说明:
    Kali 工具首页用「一级分类（ATT&CK 战术风格）→ 二级子类别 → 命令」组织工具，
    比按包名平铺更适合作为学习导航。本脚本输出该层次结构并附中文名。
"""
from __future__ import annotations

import json
import os
import re
import urllib.request

URL = "https://www.kali.org/tools/"
UA = "Mozilla/5.0 (X11; Linux x86_64) hack-learn-study-library/1.0"
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

CATEGORY_ZH = {
    "reconnaissance": "侦察",
    "resource-development": "资源开发",
    "initial-access": "初始访问",
    "execution": "执行",
    "persistence": "持久化",
    "privilege-escalation": "权限提升",
    "defense-evasion": "防御规避",
    "credential-access": "凭据访问",
    "discovery": "发现",
    "lateral-movement": "横向移动",
    "collection": "收集",
    "command-and-control": "命令与控制",
    "exfiltration": "数据外泄",
    "impact": "影响",
    "forensics": "数字取证",
    "services-and-other-tools": "服务与其它工具",
}

CATEGORY_DESC = {
    "reconnaissance": "在动手之前尽可能了解目标：主机、身份、网络与 Web 面。",
    "resource-development": "搭建攻击基础设施：C2 服务器、重定向器、Payload 托管。",
    "initial-access": "打进第一台机器：Web 漏洞、口令、钓鱼、暴露服务。",
    "execution": "在目标上运行代码：命令执行、脚本宿主、宏与解释器滥用。",
    "persistence": "维持访问：账号、服务、计划任务、后门与 rootkit。",
    "privilege-escalation": "从普通用户到 root/SYSTEM：内核漏洞、配置错误、令牌滥用。",
    "defense-evasion": "绕过检测：混淆、加壳、日志清除、免杀与白利用。",
    "credential-access": "拿凭据：内存转储、哈希、Kerberos 攻击、口令破解。",
    "discovery": "摸清内网：主机、账户、共享、进程与服务发现。",
    "lateral-movement": "横向扩散：远程执行、凭据复用、协议隧道。",
    "collection": "收集高价值数据：文件、屏幕、键盘、邮件与数据库。",
    "command-and-control": "建立稳定通道：C2 框架、隧道、隐蔽协议。",
    "exfiltration": "把数据带出去：通道选择、分块与伪装。",
    "impact": "造成影响：破坏、加密（勒索）、服务中断与擦除（红队演练中仅作演示）。",
    "forensics": "事后取证：镜像、雕复、时间线、内存与日志分析。",
    "services-and-other-tools": "系统服务、开发与通用工具。",
}

SUBCATEGORY_ZH = {
    "Host Information": "主机信息",
    "Identity Information": "身份信息",
    "Network Information": "网络信息",
    "Network Information: DNS": "网络信息：DNS",
    "Web Scanning": "Web 扫描",
    "Vulnerability Scanning": "漏洞扫描",
    "Web Vulnerability Scanning": "Web 漏洞扫描",
    "Radio Frequency": "射频",
    "OS Credential Dumping": "操作系统凭据转储",
    "Hash Identification": "哈希识别",
    "Password Profiling & Wordlists": "口令画像与字典",
    "Brute Force": "暴力破解",
    "Password Cracking": "口令破解",
    "Unsecured Credentials": "未受保护的凭据",
    "WiFi Credential Access": "Wi-Fi 凭据获取",
    "VoIP Credential Access": "VoIP 凭据获取",
    "Network Service Discovery": "网络服务发现",
    "SSL / TLS": "SSL / TLS 分析",
    "Network Sniffing": "网络嗅探",
    "Remote System Discovery": "远程系统发现",
    "Account Discovery": "账户发现",
    "Network Share Discovery": "网络共享发现",
    "Process Discovery": "进程发现",
    "System Network Configuration Discovery": "系统网络配置发现",
    "Network Security Appliances": "网络安全设备",
    "Cisco Tools": "Cisco 工具",
    "Active Directory": "活动目录",
    "Application Layer Protocol": "应用层协议",
    "Non-Application Layer Protocol": "非应用层协议",
    "Protocol Tunneling": "协议隧道",
    "Digital Forensics": "数字取证",
    "Forensic Carving Tools": "取证雕复工具",
    "Forensic Imaging Tools": "取证镜像工具",
    "PDF Forensics Tools": "PDF 取证工具",
    "Sleuth Kit Suite": "Sleuth Kit 套件",
    "Reporting Tools": "报告工具",
    "System Services": "系统服务",
}

# 匹配顺序敏感：h3 分类 → span 子类 → 工具命令链接
TOKEN = re.compile(
    r"<h3 id=([a-z0-9-]+)>"
    r"|<span title=\"([^\"]+)\" id=([a-z0-9-]+)>"
    r"|href=https://www\.kali\.org/tools/([a-z0-9._+-]+)/#([a-z0-9._+-]+)",
    re.I,
)


def main() -> int:
    req = urllib.request.Request(URL, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=60) as resp:
        raw = resp.read().decode("utf-8", "replace")

    categories: list[dict] = []
    cur_cat: dict | None = None
    cur_sub: dict | None = None
    seen: set[tuple[str, str]] = set()

    for m in TOKEN.finditer(raw):
        h3, span_title, _span_id, pkg, cmd = m.groups()
        if h3:
            cur_cat = {
                "id": h3,
                "name": h3.replace("-", " ").title(),
                "zh": CATEGORY_ZH.get(h3, ""),
                "description": CATEGORY_DESC.get(h3, ""),
                "subcategories": [],
            }
            categories.append(cur_cat)
            cur_sub = None
        elif span_title:
            if cur_cat is None:
                continue
            cur_sub = {
                "name": span_title,
                "zh": SUBCATEGORY_ZH.get(span_title, ""),
                "tools": [],
            }
            cur_cat["subcategories"].append(cur_sub)
        elif pkg:
            if cur_cat is None:
                continue
            if cur_sub is None:
                # 该分类下有些工具直接挂在分类上，没有二级子类别
                cur_sub = {"name": "(direct)", "zh": "本类直属工具", "tools": []}
                cur_cat["subcategories"].append(cur_sub)
            key = (pkg, cmd)
            if key in seen:
                continue
            seen.add(key)
            cur_sub["tools"].append(
                {"package": pkg, "command": cmd, "url": f"https://www.kali.org/tools/{pkg}/#{cmd}"}
            )

    out = {
        "source": URL,
        "categories": categories,
        "stats": {
            "categories": len(categories),
            "subcategories": sum(len(c["subcategories"]) for c in categories),
            "command_entries": len(seen),
            "unique_packages": len({p for p, _ in seen}),
        },
    }

    dest = os.path.join(ROOT, "data", "kali-categories.json")
    with open(dest, "w", encoding="utf-8") as fh:
        json.dump(out, fh, ensure_ascii=False, indent=1)

    print("[+] 分类树：", out["stats"])
    for c in categories:
        print(f"  {c['zh'] or c['name']:<12} 子类 {len(c['subcategories']):>2} · "
              f"命令 {sum(len(s['tools']) for s in c['subcategories']):>3}")
    print(f"[+] -> {dest}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
