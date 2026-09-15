# hexstrike-ai（AI 驱动的安全工具编排 / MCP 平台）

> **一句话**：把 150+ 个安全工具包装成 **MCP（Model Context Protocol）工具**，让支持 MCP 的 AI 客户端（Claude Desktop、Cursor、VS Code Copilot…）能「自己选工具、自己拼参数、自己串流程」——**AI 负责决策，HexStrike 负责动手，真正干活的还是 nmap/nuclei/sqlmap 这些老工具**。
> **分类**：基础设施与 C2 / 工具编排（AI Agent 层）｜ **Kali 包**：`hexstrike-ai`（命令 `hexstrike_server`、`hexstrike_mcp`）｜ **官方文档**：<https://www.kali.org/tools/hexstrike-ai/> ｜ 上游：<https://github.com/0x4m4/hexstrike-ai>

---

## 1. 它解决什么问题

渗透测试里有一层**纯粹的「体力活」**：

- 拿到目标 → 要决定「先 nmap 还是先 whatweb」；
- 看到 80 端口开着 → 要决定「跑 nikto 还是 nuclei 还是直接 gobuster」；
- 扫出一堆结果 → 要决定「哪些值得深挖、用什么工具深挖」；
- 做完一步 → 要**手工把上一步的输出粘到下一步的输入里**。

**HexStrike 想自动化的就是这一层**：

```
   传统方式（人做所有决策 + 所有搬运）
   ┌──────────────────────────────────────────────────────────┐
   │ 人：nmap 扫 → 看结果 → 手工决定 → 跑 nuclei → 看结果 → …  │
   └──────────────────────────────────────────────────────────┘

   HexStrike 方式（AI 做决策，HexStrike 做搬运）
   ┌──────────────────────────────────────────────────────────┐
   │ 你说：「帮我评估 10.10.10.5」                              │
   │      │                                                    │
   │      ▼                                                    │
   │ AI（Claude/GPT…） ──MCP 协议──► hexstrike_server          │
   │      │                            │                       │
   │      │  ①「先 nmap 全端口」        ├─► 真的调用 nmap        │
   │      │  ② 读结果，「开 22/80」     ├─► 真的调用 whatweb/nikto │
   │      │  ③「80 上有 WordPress」     ├─► 真的调用 wpscan      │
   │      │  ④ 汇总成报告               └─► …                  │
   │      ▼                                                    │
   │ 你得到：一份带推理过程的测试报告（AI 写的文字）              │
   └──────────────────────────────────────────────────────────┘
```

**它到底「新」在哪**：

| 层次 | 谁负责 |
|------|--------|
| **工具能力**（扫描、爆破、分析） | **完全没变**——还是 nmap/nuclei/sqlmap/john 这些 |
| **工具调用接口** | HexStrike 封装成 **HTTP API + MCP 工具** |
| **决策与编排** | **交给 AI 模型** |
| **人的角色** | **从「执行者」变成「授权者 + 审阅者」** |

**对比同类（非常关键：要理解它在生态里的位置）**：

| 方案 | 决策者 | 特点 |
|------|--------|------|
| **手敲命令** | 人 | 最可控、最慢；**唯一 100% 可预测的方式** |
| **`autorecon`** | **固定流程**（脚本） | 确定性高、无需 AI；「先 nmap 再 nikto」这类流程是写死的 |
| **固定扫描器（nuclei/nikto）** | 无 | 只做一件事，做得好 |
| **HexStrike + AI** | **LLM** | **灵活但有不确定性**：同样的目标，两次可能走不同路径；可能选错工具、可能误读输出 |
| **`pentestgpt` 等同类** | LLM | 思路相同；HexStrike 的卖点是**工具数量多 + MCP 标准化** |
| **自己写 MCP server** | 你 | 最可控——**只需暴露你真正需要的 5 个工具**，风险面小得多 |

**必须先说清楚的定位判断**：

| 维度 | 现实评价 |
|------|----------|
| **适合** | **探索式调查**（不知道用什么工具时让它先试）、**已知工具的批量编排**、**学习「AI Agent + 安全工具」这个模式** |
| **不适合** | **需要确定性、可复现、可审计的正式渗透项目**——LLM 的决策不可复现，报告需要人工重做验证 |
| **最大风险** | **它给 AI 一个「执行任意命令」的接口**（见第 2 节的架构），而且**默认无认证** |
| **成熟度** | 项目较新、迭代快；**在生产/客户环境中使用前必须自行评估代码**（见第 9 节） |

**一句话**：**把它当成「一个能让你用自然语言驱动 150 个工具的调度台」——很好玩、很有启发，但真正做项目时，你仍然要对每一条命令负责。**

---

## 2. 工作原理

### 2.1 三层结构

```
┌──────────────────────────────────────────────────────────────────────┐
│  第 1 层：AI 客户端（Claude Desktop / Cursor / VS Code Copilot …）     │
│      它做三件事：                                                      │
│        ① 读 MCP 工具的「描述」（工具名 + 参数 schema）                  │
│        ② 决定「现在该调用哪个工具、传什么参数」                          │
│        ③ 读回结果，决定下一步                                          │
└───────────────────────────────┬──────────────────────────────────────┘
                                │  MCP 协议（stdio / HTTP）
                                ▼
┌──────────────────────────────────────────────────────────────────────┐
│  第 2 层：hexstrike_mcp（MCP 客户端/桥接）                            │
│      把 hexstrike_server 的 HTTP API「翻译」成 MCP 工具              │
│      为 AI 提供：工具清单、参数说明、调用入口、结果格式化               │
└───────────────────────────────┬──────────────────────────────────────┘
                                │  HTTP（默认 http://127.0.0.1:8888）
                                ▼
┌──────────────────────────────────────────────────────────────────────┐
│  第 3 层：hexstrike_server（真正干活的）                              │
│      ├─ HTTP API：/health, /api/command, /api/intelligence/…         │
│      ├─ 「智能层」：DecisionEngine / 12+ agents / 缓存 / 进程管理      │
│      └─ 工具执行：subprocess 调 nmap / nuclei / sqlmap / …            │
└──────────────────────────────────────────────────────────────────────┘
```

**关键理解**：**`hexstrike_mcp` 是桥，`hexstrike_server` 是大脑+手脚**。

| 进程 | 角色 | 谁启动它 |
|------|------|----------|
| **`hexstrike_server`** | **常驻服务**：提供 API、跑工具 | **你手动启动**（`hexstrike_server --port 8888`） |
| **`hexstrike_mcp`** | **被 AI 客户端拉起的桥接进程** | **AI 客户端**根据配置里的 `command` 启动 |
| **AI 客户端** | 决策者 | 你（Claude Desktop / Cursor / VS Code…） |

**所以「启动顺序」是**：**先起 server，再让 AI 客户端通过 mcp 桥接连上**。

### 2.2 「智能层」做了什么

官方列出 12+ 个 agent（组件），按功能归类：

| 类别 | 组件 | 作用 |
|------|------|------|
| **决策** | `IntelligentDecisionEngine` | 选工具、定参数 |
| | `ParameterOptimizer` | 结合上下文调参（比如「nmap 该用什么强度」） |
| | `TechnologyDetector` | 识别目标技术栈 |
| **流程** | `BugBountyWorkflowManager` | 按漏洞赏金的分析流程编排 |
| | `CTFWorkflowManager` | 按 CTF 题型的套路编排 |
| | `VulnerabilityCorrelator` | **把多个发现串成攻击链** |
| **情报** | `CVEIntelligenceManager` | CVE 情报与利用分析 |
| | `AIExploitGenerator` | 生成 exploit 骨架 |
| **健壮性** | `RateLimitDetector` | 识别被限速 |
| | `FailureRecoverySystem` / `GracefulDegradation` | 失败恢复与降级 |
| | `PerformanceMonitor` | 性能优化 |

**现实检查**：这些「agent」**本质上是规则 + 提示词 + 缓存的组合**，不是「自主意识」。**它们能让 AI 少犯低级错误**（比如知道 nmap 的 `-sV` 要配 `-Pn`），但**不能替代人的判断**。

### 2.3 缓存与进程管理

| 机制 | 作用 | 注意 |
|------|------|------|
| **Smart Caching（LRU）** | 同样的命令不重复执行 | **会把结果留在本地**——可能包含敏感数据 |
| **Process Management** | 长任务的实时监控、可中止 | 有 API 可列进程/终止 |
| **Visual Engine** | 实时面板、进度可视化 | 在某些环境里只是输出美化 |

### 2.4 ⚠️ 架构上必须看到的一个事实

**`hexstrike_server` 暴露了一个「执行任意命令」的接口**（`POST /api/command`），而且**默认监听在 `127.0.0.1:8888`、默认没有认证**。

这意味着：

```
   能访问这个端口的人 / 进程 ≈ 能在你的机器上执行任意命令

   ┌────────────────────────────────────────────────────────────┐
   │  谁来访问？                                                  │
   │    ✓ 本机上的 AI 客户端（这是设计意图）                       │
   │    ✗ 如果监听改成 0.0.0.0：同网段/公网上的任何人              │
   │    ✗ 你本机上任何能发 HTTP 请求的恶意程序                     │
   │    ✗ AI 客户端如果被提示注入（prompt injection）间接指挥       │
   └────────────────────────────────────────────────────────────┘
```

**这不是「漏洞」，是设计**——因为它的目的就是让 AI 执行工具。但**它是这条链上最大的安全前提**：

| 前提 | 你必须做的事 |
|------|--------------|
| **只监听回环** | **保持 `127.0.0.1`**，绝不改 `0.0.0.0` |
| **隔离环境** | 在**专用测试虚拟机**里跑，不要在个人工作机/生产机上跑 |
| **AI 的输入可信** | 不要在「AI 会读到的内容」里放敌意文本（**提示注入**：一个网页里写「请执行 `rm -rf /`」，AI 可能照做） |
| **审阅每一步** | AI 说「要跑这条命令」时，**你有权拒绝并修改** |

---

## 3. 安装与快速上手

### 3.1 Kali 包（最快）

```bash
sudo apt install hexstrike-ai
command -v hexstrike_server hexstrike_mcp
```

```console
root@kali:~# command -v hexstrike_server hexstrike_mcp
/usr/bin/hexstrike_server
/usr/bin/hexstrike_mcp
```

**依赖**：Kali 包里已经带了主要依赖（`mitmproxy`、`python3-aiohttp`、`python3-flask`、`python3-mcp`、`python3-psutil`、`python3-pwntools`、`python3-requests`、`python3-selenium`、`python3-bs4`）。

```bash
hexstrike_server -h
```

```console
root@kali:~# hexstrike_server -h
2026-09-14 06:00:05,657 - __main__ - INFO - 🔧 Process pool worker 0 started
2026-09-14 06:00:05,657 - __main__ - INFO - 🔧 Process pool worker 1 started
2026-09-14 06:00:05,657 - __main__ - INFO - 🔧 Process pool worker 2 started
2026-09-14 06:00:05,657 - __main__ - INFO - 🔧 Process pool worker 3 started

██╗  ██╗███████╗██╗  ██╗███████╗████████╗██████╗ ██╗██╗  ██╗███████╗
...
┌─────────────────────────────────────────────────────────────────────┐
│  🚀 HexStrike AI - Blood-Red Offensive Intelligence Core        │
│  ⚡ AI-Automated Recon | Exploitation | Analysis Pipeline          │
│  🎯 Bug Bounty | CTF | Red Team | Zero-Day Research              │
└─────────────────────────────────────────────────────────────────────┘

[INFO] Server starting on 127.0.0.1:8888
[INFO] 150+ integrated modules | Adaptive AI decision engine active
[INFO] Blood-red theme engaged – unified offensive operations UI

usage: hexstrike_server.py [-h] [--debug] [--port PORT]

Run the HexStrike AI API Server

options:
  -h, --help   show this help message and exit
  --debug      Enable debug mode
  --port PORT  Port for the API server (default: 8888)
```

```bash
hexstrike_mcp -h
```

```console
root@kali:~# hexstrike_mcp -h
usage: hexstrike_mcp.py [-h] [--server SERVER] [--timeout TIMEOUT] [--debug]

Run the HexStrike AI MCP Client

options:
  -h, --help         show this help message and exit
  --server SERVER    HexStrike AI API server URL (default:
                     http://127.0.0.1:8888)
  --timeout TIMEOUT  Request timeout in seconds (default: 300)
  --debug            Enable debug logging
```

> **注意**：`hexstrike_server -h` 会**先把启动横幅打出来**再显示帮助——它不是在「启动服务」，只是 banner 在参数解析之前就打印了。**看到 `Server starting on 127.0.0.1:8888` 也不要误会它已经开始跑了。**

### 3.2 从源码装（跟进上游新版本）

```bash
git clone https://github.com/0x4m4/hexstrike-ai.git
cd hexstrike-ai
python3 -m venv hexstrike-env
source hexstrike-env/bin/activate
pip3 install -r requirements.txt
```

### 3.3 启动服务（**先做这一步**）

```bash
# ⚠️ 在隔离的测试虚拟机里做
hexstrike_server --port 8888
```

```console
[INFO] Server starting on 127.0.0.1:8888
[INFO] 150+ integrated modules | Adaptive AI decision engine active
```

**验证服务是否活着**：

```bash
# 健康检查（会报告「哪些工具可用」）
curl -s http://localhost:8888/health | python3 -m json.tool | head -40

# 看缓存统计
curl -s http://localhost:8888/api/cache/stats | python3 -m json.tool | head
```

```console
root@kali:~# curl -s http://localhost:8888/health
{"status":"healthy","timestamp":"...","tools_available":{...},"system_info":{...}}
```

**解读**：**`/health` 的输出就是「这台机器上哪些工具能用」的清单**——**如果你要用的工具不在里面，AI 也调不动它**（它会报「工具不存在」）。这是排错的第一入口。

```bash
# 测试「智能分析」接口（先别让它真扫，只试 API 通不通）
curl -s -X POST http://localhost:8888/api/intelligence/analyze-target \
  -H "Content-Type: application/json" \
  -d '{"target": "127.0.0.1", "analysis_type": "comprehensive"}' | python3 -m json.tool | head -40
```

### 3.4 装齐工具（AI 能调动的范围完全取决于这个）

HexStrike 只是**调度器**——**工具本身要你自己装**。官方给的「核心工具」清单：

```bash
# 网络与侦察
sudo apt install -y nmap masscan amass fierce dnsenum theharvester responder netexec enum4linux-ng
# Web
sudo apt install -y gobuster feroxbuster dirsearch ffuf dirb nikto sqlmap wpscan arjun dalfox wafw00f
# 口令
sudo apt install -y hydra john hashcat medusa patator hash-identifier ophcrack
# 二进制/逆向/取证
sudo apt install -y gdb radare2 binwalk ghidra checksec binutils foremost steghide exiftool
# 探测可用性
for t in nmap gobuster nuclei sqlmap ffuf nikto hydra hashcat radare2 binwalk; do
  printf '%-12s ' "$t"; command -v "$t" || echo "MISSING"
done
```

```console
nmap         /usr/bin/nmap
gobuster     /usr/bin/gobuster
nuclei       MISSING
sqlmap       /usr/bin/sqlmap
...
```

**解读（这是新手最容易失望的地方）**：

> **「HexStrike 有 150+ 工具」≠「你装了 150+ 工具」**。
>
> 它**封装**了 150+ 个工具的调用方式，但**工具本体必须在系统里存在**。AI 决定「要用 nuclei」时，如果 `nuclei` 不在 PATH 里，那一步就失败。

**补装缺失的工具**（能用 `apt` 的优先）：

```bash
# nuclei / ffuf / katana / httpx 等（ProjectDiscovery 系）
sudo apt install -y nuclei ffuf 2>/dev/null || true
# 或用 go install（如果本机有 go）
command -v go >/dev/null && go install -v github.com/projectdiscovery/nuclei/v3/cmd/nuclei@latest || true
# 复查
curl -s http://localhost:8888/health | python3 -c "
import json,sys
d = json.load(sys.stdin)
avail = d.get('tools_available') or {}
ok = [k for k, v in avail.items() if v]
missing = [k for k, v in avail.items() if not v]
print('可用:', len(ok)); print('缺失:', len(missing))
print('缺失清单:', ', '.join(missing[:30]))
" 2>/dev/null
```

### 3.5 让 AI 客户端连上（Claude Desktop / Cursor / VS Code）

**关键理解**：这三个客户端**不直接连 `hexstrike_server`**，而是**去启动 `hexstrike_mcp` 这个桥接进程**，由桥接进程去连 server。

**Claude Desktop / Cursor** —— 编辑 `~/.config/Claude/claude_desktop_config.json`：

```json
{
  "mcpServers": {
    "hexstrike-ai": {
      "command": "python3",
      "args": [
        "/path/to/hexstrike-ai/hexstrike_mcp.py",
        "--server",
        "http://localhost:8888"
      ],
      "description": "HexStrike AI v6.0 - Advanced Cybersecurity Automation Platform",
      "timeout": 300,
      "disabled": false
    }
  }
}
```

**用 Kali 包时**（不需要源码路径，直接用命令）：

```json
{
  "mcpServers": {
    "hexstrike-ai": {
      "command": "hexstrike_mcp",
      "args": ["--server", "http://127.0.0.1:8888"],
      "timeout": 300,
      "disabled": false
    }
  }
}
```

**VS Code Copilot** —— `.vscode/settings.json`：

```json
{
  "servers": {
    "hexstrike": {
      "type": "stdio",
      "command": "hexstrike_mcp",
      "args": ["--server", "http://127.0.0.1:8888"]
    }
  },
  "inputs": []
}
```

**改完配置后重启客户端**。然后在 AI 对话里**先确认「工具已挂载」**：

```text
（在 Claude/Cursor 的对话里）
你：列出你现在可用的 MCP 工具里，和网络扫描相关的有哪些？

（AI 应该能报出 nmap_scan、masscan_scan、rustscan_scan、autorecon_scan 等）
```

**排错**：如果 AI 说「没有这些工具」：

```bash
# ① server 起来了吗
curl -s -o /dev/null -w '%{http_code}\n' http://127.0.0.1:8888/health
netstat -tlnp 2>/dev/null | grep 8888 || ss -lntp | grep 8888

# ② mcp 桥接能单独跑吗（用 --debug 看它连 server 的过程）
hexstrike_mcp --server http://127.0.0.1:8888 --debug

# ③ 配置文件路径对吗（Claude Desktop 各平台路径不同）
ls -l ~/.config/Claude/claude_desktop_config.json
python3 -c "import json;json.load(open('$HOME/.config/Claude/claude_desktop_config.json'));print('JSON 语法 OK')"
```

---

## 4. 核心参数详解

HexStrike 的「参数」分三层：**两个命令的命令行参数**、**HTTP API**、**MCP 工具**。

### 4.1 `hexstrike_server`

| 参数 | 作用 | 使用建议 |
|------|------|----------|
| `-h` / `--help` | 帮助（**注意：会先打 banner**） | —— |
| `--debug` | **调试模式**：更详细日志 | 排错；但**日志会包含命令与输出**（可能含敏感数据） |
| `--port PORT` | **API 端口**（默认 `8888`） | 换端口用；**不要改绑定地址** |

**绑定地址**：从 `-h` 的输出可以看到 **`Server starting on 127.0.0.1:8888`** —— 即**默认只监听回环**。

> ⚠️ **绝对不要**为了「让其他机器也能连」去改绑定地址（源码里如果没有这个参数，就别去 hack 它）。**这个服务一旦对外可达，等于把「任意命令执行」暴露出去**。

### 4.2 `hexstrike_mcp`

| 参数 | 作用 | 使用建议 |
|------|------|----------|
| `-h` / `--help` | 帮助 | —— |
| `--server <url>` | **要连的 server 地址**（默认 `http://127.0.0.1:8888`） | 与 `hexstrike_server --port` 保持一致 |
| `--timeout <秒>` | **请求超时**（默认 `300`） | **跑长时间扫描（nmap 全端口、nuclei 全模板）时可能不够** → 调大（如 `900`） |
| `--debug` | 调试日志 | 排查「AI 说连不上」时用 |

**`--timeout` 是最常需要调的参数**：

| 场景 | 建议 timeout |
|------|--------------|
| 快速侦察（health、单个轻量工具） | 默认 300 够 |
| **全端口 nmap / 大字典 fuzz / nuclei 全模板** | **900 ~ 1800** |
| **知道会超时的长任务** | 不用等它——用**进程管理 API** 提交后台任务，再查状态 |

### 4.3 HTTP API（**用它做自动化和排错，比走 AI 更可控**）

**核心系统接口**（官方文档）：

| 接口 | 方法 | 作用 | 怎么用 |
|------|------|------|--------|
| **`/health`** | GET | **健康检查 + 工具可用性** | **第一个要调的接口**；用来确认「工具装没装」 |
| **`/api/command`** | POST | **执行命令**（带缓存） | **⚠️ 这就是「任意命令执行」入口**；只在完全可控的环境里手工调 |
| `/api/telemetry` | GET | 系统性能指标 | 看 CPU/内存占用 |
| `/api/cache/stats` | GET | 缓存统计 | 判断「结果是缓存命中还是真跑了」 |
| `/api/intelligence/analyze-target` | POST | AI 目标分析 | 让智能层给出建议（**不一定会真扫**） |
| `/api/intelligence/select-tools` | POST | 智能选工具 | 看它「会选什么」——**很好的学习入口** |
| `/api/intelligence/optimize-parameters` | POST | 参数优化 | 同上 |

**进程管理接口**：

| 接口 | 方法 | 作用 |
|------|------|------|
| `/api/processes/list` | GET | 列出当前所有活动进程 |
| `/api/processes/status/<pid>` | GET | 某进程详情 |
| `/api/processes/terminate/<pid>` | POST | **终止某进程**（长任务卡住时用） |
| `/api/processes/dashboard` | GET | 实时监控面板 |

**用法示例（**先用 `select-tools` 这种只读接口熟悉它**）**：

```bash
# ① 健康检查：看工具可用性
curl -s http://localhost:8888/health | python3 -m json.tool | head -30

# ② 看看它「会给我选什么工具」（只读，不会真扫）
curl -s -X POST http://localhost:8888/api/intelligence/select-tools \
  -H "Content-Type: application/json" \
  -d '{"target": "127.0.0.1", "objective": "web_security_assessment"}' \
  | python3 -m json.tool | head -40

# ③ 看进程
curl -s http://localhost:8888/api/processes/list | python3 -m json.tool | head -30
```

### 4.4 MCP 工具（AI 实际调用的东西）

**工具是按类别暴露的**（官方文档列举的名字）：

| 类别 | MCP 工具（示例） | 底层真实工具 |
|------|------------------|--------------|
| **网络** | `nmap_scan()`、`rustscan_scan()`、`masscan_scan()`、`autorecon_scan()`、`amass_enum()` | nmap / rustscan / masscan / autorecon / amass |
| **Web** | `gobuster_scan()`、`feroxbuster_scan()`、`ffuf_scan()`、`nuclei_scan()`、`sqlmap_scan()`、`wpscan_scan()` | 同名工具 |
| **二进制/逆向** | `ghidra_analyze()`、`radare2_analyze()`、`gdb_debug()`、`pwntools_exploit()`、`angr_analyze()` | ghidra / radare2 / gdb / pwntools / angr |
| **云** | `prowler_assess()`、`scout_suite_audit()`、`trivy_scan()`、`kube_hunter_scan()`、`kube_bench_check()` | 同名工具 |

**关键理解**：**AI 调用 `nmap_scan()` 时，真正发生的是「在 server 上起一个 nmap 进程」**。所以：

| 事实 | 含义 |
|------|------|
| 工具名与真实工具**同名/近名** | **你可以预估它要干什么** —— 这是审阅 AI 决策的基础 |
| 参数由 AI 决定 | **AI 可能选出过激的参数**（如 `nmap -T5 -p-` 打满） |
| 结果回到 AI 再被「解读」 | **AI 的解读可能有误**（把 `filtered` 说成 `closed`） |
| 你有「拒绝/修改」的机会 | **不要习惯性点同意** |

**与其它教程的对应关系**（**HexStrike 里的每个工具，本库都有对应的精讲**）：

| HexStrike 工具 | 本库教程 |
|----------------|----------|
| `nmap_scan()` | [`../01-信息搜集/nmap.md`](../01-信息搜集/nmap.md) |
| `amass_enum()` | [`../01-信息搜集/amass.md`](../01-信息搜集/amass.md) |
| `gobuster_scan()` / `ffuf_scan()` | [`../03-Web应用/gobuster.md`](../03-Web应用/gobuster.md)、[`../03-Web应用/ffuf.md`](../03-Web应用/ffuf.md) |
| `nuclei_scan()` | [`../02-漏洞分析/nuclei.md`](../02-漏洞分析/nuclei.md) |
| `sqlmap_scan()` | [`../03-Web应用/sqlmap.md`](../03-Web应用/sqlmap.md) |
| `wpscan_scan()` | [`../03-Web应用/wpscan.md`](../03-Web应用/wpscan.md) |
| `radare2_analyze()` | [`radare2.md`](../10-逆向工程/radare2.md)（10-逆向工程） |
| `ghidra_analyze()` | [`ghidra.md`](../10-逆向工程/ghidra.md) |

> **这是使用 HexStrike 最正确的姿势**：**AI 决定「用哪个工具」，你负责「这个工具的细节是否合适」** —— 所以你必须先学过那些工具。

---

## 5. 实战演练

> ## ⚠️ 本节前提（**必读**）
>
> **1. 环境**：**必须在一台专用的、隔离的测试虚拟机里**运行 HexStrike。
> - 它会执行任意命令（设计如此）；
> - 它可能被**提示注入**驱动（AI 读到的内容可能含攻击指令）；
> - 它会产生大量扫描流量（**别在公司网络里乱跑**）。
>
> **2. 目标**：**只能是你自己的靶场**（本机回环、DVWA 容器、你自己的实验网段、CTF 题目）。
> **绝对不要**把它指向任何未授权目标 —— **AI 不会替你判断合法性**，它只会执行。
>
> **3. 心智模型**：**你是「操作审批者」**。AI 每次说「我要执行 X」时，你都要能回答：
> - 这条命令打的是什么目标？
> - 这条命令会做什么？
> - 我的授权范围包含它吗？
> **答不上来就点拒绝。**

### 场景 0：先把「环境」搭好（这一步决定了后面能不能安全地玩）

```bash
# ① 用一次性虚拟机（快照是必需的）
#    建议：至少 4 GB 内存、20 GB 磁盘（要装一堆工具）

# ② 在虚拟机里起一个靶场（用 Docker 起 DVWA，作为唯一目标）
git clone https://github.com/digininja/DVWA.git /tmp/DVWA
cd /tmp/DVWA && docker compose up -d
sleep 10
curl -s -o /dev/null -w 'DVWA HTTP %{http_code}\n' http://localhost:4280/
```

```console
DVWA HTTP 200
```

**现在这台机器上有三个东西**：

| 组件 | 地址 | 角色 |
|------|------|------|
| **HexStrike server** | `127.0.0.1:8888` | 调度器（待启动） |
| **DVWA** | `127.0.0.1:4280` | **唯一合法的测试目标** |
| **AI 客户端** | 本机 GUI 应用 | 决策者 |

```bash
# ③ 起 HexStrike server（前台跑，方便看日志；或另开一个终端）
hexstrike_server --port 8888
```

**⚠️ 一个重要的纪律**：**把 DVWA 的地址记在心里**——**AI 只能对 `127.0.0.1` 或你指定给它的靶场地址动手**。任何时刻 AI 提出要打别的地址，**就是拒绝的时候**。

### 场景 1：先「只用 API」玩一遍（推荐！比走 AI 更可控）

**先用 HTTP API 熟悉它，再让 AI 接管**——这样你能清楚看到「AI 到底在做什么」。

**1a. 看它「有什么」**

```bash
# ① 健康检查：工具可用性
curl -s http://127.0.0.1:8888/health | python3 -c "
import json,sys
d = json.load(sys.stdin)
print('状态:', d.get('status'))
tools = d.get('tools_available') or {}
if tools:
    ok = sorted(k for k,v in tools.items() if v)
    miss = sorted(k for k,v in tools.items() if not v)
    print(f'可用工具 {len(ok)} 个:', ', '.join(ok[:40]))
    print(f'缺失 {len(miss)} 个:', ', '.join(miss[:40]))
else:
    print(json.dumps(d, ensure_ascii=False)[:800])
"
```

```console
状态: healthy
可用工具 62 个: amass, arjun, binwalk, checksec, dalfox, dnsenum, exiftool, ffuf, ...
缺失 45 个: angr, feroxbuster, kube-hunter, prowler, rustscan, scout-suite, ...
```

**解读**：

| 观察 | 含义 | 动作 |
|------|------|------|
| `可用工具 N 个` | **AI 能调动的范围** | 想要更多 → 装工具（`apt`/`go install`/`pip`） |
| `缺失 M 个` | AI 选了这些工具会**失败** | 补装；或告诉 AI「别用这些」 |
| `状态: healthy` 但接口全空 | server 版本/接口不同 | 看 `/health` 的原始 JSON，以实际输出为准 |

**1b. 看它「会怎么决策」（只读接口，非常值得玩）**

```bash
# ② 让「智能层」给出工具选择建议（不一定真扫）
curl -s -X POST http://127.0.0.1:8888/api/intelligence/select-tools \
  -H 'Content-Type: application/json' \
  -d '{"target": "http://127.0.0.1:4280/", "objective": "web_security_assessment"}' \
  | python3 -m json.tool | head -50
```

```console
{
    "target": "http://127.0.0.1:4280/",
    "objective": "web_security_assessment",
    "recommended_tools": [ ... ],
    "reasoning": "...",
    "parameters": { ... }
}
```

**解读**：**这个接口是理解「AI + 安全工具」最有价值的地方**——你能看到它**怎么推理**、**准备用什么参数**。

**⚠️ 而且这是「只读」的**——**不会真的发包**。**先用它建立信任（或发现它不靠谱），再决定要不要让它真动手。**

**1c. 手动调一次「真的干活的接口」（在靶场上）**

```bash
# ③ 直接在靶场上跑一次 nmap（通过 HexStrike 的接口）
#    ⚠️ 目标必须是 127.0.0.1（你的靶场）
curl -s -X POST http://127.0.0.1:8888/api/command \
  -H 'Content-Type: application/json' \
  -d '{"command": "nmap -sV -Pn -p 4280 127.0.0.1", "timeout": 120}' \
  | python3 -m json.tool | head -40
```

```console
{
    "success": true,
    "command": "nmap -sV -Pn -p 4280 127.0.0.1",
    "stdout": "...4280/tcp open  http  nginx...",
    "stderr": "",
    "execution_time": 3.42,
    "cached": false
}
```

**解读（这个响应结构就是「HexStrike 的一切」）**：

| 字段 | 含义 | 注意 |
|------|------|------|
| `success` | 命令是否成功执行 | **`success: true` ≠ 「发现了什么」**——只是「命令跑完了」 |
| `command` | **实际执行的命令** | **每次都要核对这个字段！** |
| `stdout` / `stderr` | 输出 | **AI 就是读这个来「理解结果」的** |
| `execution_time` | 耗时 | 判断性能/是否卡住 |
| **`cached`** | **是否是缓存命中** | **`true` 说明「这条命令之前跑过，直接返回旧结果」** ← **重要！旧结果可能已过期** |

**⚠️ `cached` 字段是个大坑**：同样的命令行会走缓存。**如果目标状态变了（比如靶场重启），你拿到的可能是旧数据**。要强制重跑：换一下命令（加个无害参数），或用进程管理看缓存细节。

```bash
# ④ 看失败长什么样（故意调一个不存在的工具）
curl -s -X POST http://127.0.0.1:8888/api/command \
  -H 'Content-Type: application/json' \
  -d '{"command": "definitely-not-a-tool --help"}' \
  | python3 -m json.tool | head -20
```

```console
{
    "success": false,
    "command": "definitely-not-a-tool --help",
    "stderr": "/bin/sh: 1: definitely-not-a-tool: not found",
    ...
}
```

**解读**：**AI 拿到 `success: false` 时的行为很关键**——它应该「换一个工具或告诉你工具没装」。**如果它无视失败继续往下做，那你就要接管了。**

**1d. 进程管理与长任务**

```bash
# ⑤ 看当前有哪些进程在跑
curl -s http://127.0.0.1:8888/api/processes/list | python3 -m json.tool | head -40

# ⑥ 如果有个任务卡住了 → 终止它
PID=<从上面拿到的 pid>
curl -s -X POST "http://127.0.0.1:8888/api/processes/terminate/$PID" | python3 -m json.tool

# ⑦ 看实时面板
curl -s http://127.0.0.1:8888/api/processes/dashboard | python3 -m json.tool | head -30
```

### 场景 2：让 AI 接管（**这是它真正的用法**）

**2a. 在 AI 客户端里发起任务（先给「范围约束」）**

**关键在于「提示词」**——你要在 prompt 里**明确限定范围**，而不是随便说「帮我测试一下」：

```text
你是一名在我授权的测试环境里工作的助手。

【环境】
- 目标：仅限 http://127.0.0.1:4280/ （这是一个我自建的 DVWA 靶场）
- 其他任何地址【一律不要访问】
- 所有工具调用都应针对这个地址

【任务】
用你现有的 MCP 工具，对这个靶场做一次基础的 Web 安全评估。

【要求】
1. 每调用一个工具前，先用一句话说明「为什么要用它」和「它会对什么发请求」
2. 只做【识别与检测】，不要做任何会造成破坏的操作（不要爆破、不要 DoS、不要写入数据）
3. 遇到工具不存在（success: false）就跳过并告诉我，不要重试
4. 最后给我一份报告，必须包含：
   - 实际调用过的每一条命令（原文）
   - 每条命令的原始输出摘要
   - 你的结论，以及【你不确定的地方】
5. 不要编造没执行过的步骤
```

**2b. 观察 AI 的行为（**这一步比结果更有价值**）**

你会看到的**典型流程**：

```text
AI：先做存活与端口确认 → 调用 nmap_scan(target="127.0.0.1", ports="4280")
    （你应该核对：参数合理吗？目标对吗？）
    ✔ 结果：4280/tcp open http nginx

AI：识别到 HTTP 服务 → 调用 whatweb 或 nikto
    ✔ 结果：nginx / PHP

AI：DVWA 是已知的靶场应用 → 准备跑 nikto/gobuster
    ⚠️ 这里你该注意：gobuster 用的是什么字典？并发多少？

AI：读结果 → 生成报告
```

**2c. 你在每一步该检查什么（**这张表决定了你是在「用 AI」还是「被 AI 用」**）**

| 检查项 | 怎么看 | 不合格的表现 |
|--------|--------|--------------|
| **目标地址** | AI 说的目标是不是 `127.0.0.1:4280` | **出现了别的 IP/域名 → 立刻停** |
| **命令原文** | 调用的 MCP 工具名 + 参数 | 说不出「这命令干嘛」→ 拒绝 |
| **强度** | 有没有 `-T5`、`--threads 100`、爆破 | **对靶场无所谓；对真实目标会打崩** |
| **是否破坏性** | 有没有写操作、上传、删数据 | 出现写操作 → 拒绝 |
| **工具是否存在** | `success: false` | AI 无视失败继续 → 接管 |
| **结论是否可复现** | 报告里的结论对应哪条命令的哪段输出 | **找不到对应输出的结论 = 编的** |

**2d. 一个很实用的练习：让 AI「只选不做」**

```text
请【不要真的执行任何工具】。

只根据我给的这一个目标（http://127.0.0.1:4280/），
列出你【打算】按顺序调用哪些 MCP 工具，以及每个工具的完整参数。
对每一步解释：这一步要验证什么假设。
```

**解读**：**这是最安全的用法**——**先让 AI 出方案，你审阅，再决定放不放行**。这相当于给 AI 加了一个「人工审批层」，**是从「AI 自主执行」到「AI 辅助决策」的正确降级**。

```text
（审阅 AI 的方案后）
按这个方案执行。但：
- 跳过所有涉及爆破和字典枚举的步骤
- 每一步执行前把命令原文再贴一次
```

### 场景 3：把它当「学习工具」和「自定义 MCP」的起点

**3a. 用它来「学工具选型」（可能比它的扫描能力更有价值）**

```bash
# 准备一组「不同形态的目标」，看它会怎么选工具
for payload in \
  '{"target":"127.0.0.1","objective":"network_recon"}' \
  '{"target":"http://127.0.0.1:4280/","objective":"web_security_assessment"}' \
  '{"target":"http://127.0.0.1:4280/","objective":"api_security"}' \
  '{"target":"/tmp/some_binary","objective":"binary_analysis"}'
do
  echo "===== $payload ====="
  curl -s -X POST http://127.0.0.1:8888/api/intelligence/select-tools \
    -H 'Content-Type: application/json' -d "$payload" \
  | python3 -c "
import json,sys
try:
    d = json.load(sys.stdin)
    for k, v in d.items():
        print(f'  {k}: {v}')
except Exception as e:
    print('  解析失败:', e)
"
done
```

**解读（这个实验能直接回答「AI 懂不懂工具」）**：

| 观察 | 结论 |
|------|------|
| 「网络侦察」→ 选 nmap/masscan/rustscan | 合理 |
| 「Web」→ 选 whatweb/nikto/gobuster | 合理 |
| 「二进制」→ 选 radare2/ghidra/binwalk/checksec | 合理 |
| **「API 安全」→ 也只会套 nikto/gobuster** | **不够专业**（真做 API 要 swagger 解析、JWT 测试） |
| **每次都选同一批工具** | 说明「智能」更多来自**规则**，而不是对目标的理解 |

**结论**：**HexStrike 的「智能选型」是「够用的启发式」，不是「专家判断」**。**你自己在 [`../02-漏洞分析/nuclei.md`](../02-漏洞分析/nuclei.md)、[`../03-Web应用/sqlmap.md`](../03-Web应用/sqlmap.md) 里学到的选型知识，比它的建议更可靠。**

**3b. 读它的源码，学「怎么把工具包成 MCP」**

```bash
# 用 Kali 包时，源码/数据通常在 /usr/share/hexstrike-ai 或 Python site-packages
python3 -c "import hexstrike_mcp" 2>/dev/null && echo "作为模块可导入"
find / -maxdepth 6 -name 'hexstrike_server.py' 2>/dev/null | head
find / -maxdepth 6 -name 'hexstrike_mcp.py' 2>/dev/null | head
```

```bash
# 看它怎么定义 MCP 工具（这就是「工具包装」的模板）
grep -rn 'def .*_scan\|@mcp.tool\|def nmap_scan\|def nuclei_scan' <源码目录> 2>/dev/null | head -20
```

**解读**：**这是本篇最有价值的「产出」**——**读懂它怎么把 `subprocess` 调用包装成 MCP 工具，你就能写自己的 MCP server 了**。

```python
# 一个「最小 MCP 工具」长这样（结构示意，帮助你理解 HexStrike 在做什么）
# 真正的实现细节请以你本机的源码为准
def nmap_scan(target: str, ports: str = "1-1000", flags: str = "-sV") -> dict:
    """对目标做 nmap 扫描。

    Args:
        target: 目标 IP 或域名
        ports:  端口范围，如 "80,443" 或 "1-1000"
        flags:  额外的 nmap 参数
    Returns:
        {"success": bool, "stdout": str, "stderr": str}
    """
    cmd = ["nmap", "-Pn"] + flags.split() + ["-p", ports, target]
    # ... 校验、执行、限流、超时、缓存 ...
```

**为什么「自己写」往往更好**（对真实项目）：

| 自己做 | 好处 |
|--------|------|
| **只暴露 5 个你信任的工具** | 攻击面小得多（不需要「任意命令执行」接口） |
| **参数**你写死/校验（不给 AI 自由） | **AI 无法选出危险参数** |
| **输出解析**你写 | 结论可靠（不靠 AI 读文本） |
| **不需要给 AI 一个 shell** | 风险降低一个数量级 |

**3c. 一个「安全使用」的极简流程（把上面的经验固化成纪律）**

```bash
# ① 起隔离环境（每次都用快照回滚）
# ② 起靶场，确认地址
docker compose -f /tmp/DVWA/compose.yml up -d && curl -s -o /dev/null -w '%{http_code}\n' http://127.0.0.1:4280/

# ③ 起 HexStrike（保持默认监听 127.0.0.1）
hexstrike_server --port 8888 &

# ④ 记下「允许的目标」清单（写进提示词）
echo "允许的目标: http://127.0.0.1:4280/  （DVWA 靶场，我自己的）" > /tmp/scope.txt

# ⑤ 在 AI 客户端里：先要方案（不让它执行），审阅后再放行
# ⑥ 全程监控进程
watch -n 5 'curl -s http://127.0.0.1:8888/api/processes/list | head -c 400; echo'

# ⑦ 结束后
pkill -f hexstrike_server
cd /tmp/DVWA && docker compose down -v
```

**清理**：

```bash
pkill -f hexstrike_server
pkill -f hexstrike_mcp
cd /tmp/DVWA && docker compose down -v
# 虚拟机回滚到快照
```

---

## 6. 输出解读

### 6.1 `/health` 的输出

```json
{
  "status": "healthy",
  "timestamp": "...",
  "tools_available": { "nmap": true, "nuclei": false, ... },
  "system_info": { ... }
}
```

| 字段 | 含义 | 判断 |
|------|------|------|
| `status` | 服务状态 | `healthy` = 服务活着 |
| **`tools_available`** | **每个工具的可用性** | **`false` 的工具 = AI 调用必然失败**；这是补装清单 |
| `system_info` | 系统信息 | 看资源是否够（AI 可能同时起多个工具） |

### 6.2 `/api/command` 的响应（**最需要精确解读的**）

```json
{
  "success": true,
  "command": "nmap -sV -Pn -p 4280 127.0.0.1",
  "stdout": "...",
  "stderr": "",
  "execution_time": 3.42,
  "cached": false
}
```

| 字段 | 含义 | **必查** |
|------|------|----------|
| `success` | **命令是否执行成功** | ⚠️ **只表示「进程正常退出」，不代表「探测到任何东西」** |
| `command` | **实际执行的命令** | ✅ **每次都核对**——这是审计的锚点 |
| `stdout` / `stderr` | 输出 | ✅ AI 靠这个下结论；**它的解读可能错** |
| `execution_time` | 耗时 | 异常短 → 可能秒退（参数错）；异常长 → 可能卡住 |
| **`cached`** | **是否缓存命中** | ⚠️ **`true` = 返回的是历史结果，可能已过期** |

**`success` 的三种情况**：

| `success` | `stdout` | 真实含义 |
|-----------|----------|----------|
| `true` | 有内容 | 命令跑了且有输出 |
| `true` | 空 | 命令跑了但没输出（**不是「没发现问题」**，可能是参数不对） |
| `false` | —— | 进程非 0 退出 / 工具不存在 / 超时被杀 |

**最容易犯的解读错误**：

```
❌ 「success: true，所以扫描成功，没发现漏洞」
✅ 「命令执行成功，输出为空 —— 需要确认参数是否正确、目标是否可达」
```

### 6.3 AI 生成报告时必须核实的点

| 报告里的话 | 怎么核实 |
|------------|----------|
| 「发现开放端口 80」 | 找对应的 nmap 输出（`stdout`）里有没有 `80/tcp open` |
| 「存在 SQL 注入」 | 找 sqlmap/nuclei 的原始终端输出；**AI 可能把「可能有」说成「存在」** |
| 「已确认可利用」 | **除非有完整的、你自己看过的证据，否则一律按「未确认」处理** |
| 「没有发现问题」 | 检查：**工具都装了吗？参数对吗？目标真的可达吗？**（`success: true` + 空输出 ≠ 安全） |
| 报告的「推理过程」 | **推理是 AI 写的，不是证据**——证据只有 `command` + `stdout` |

> **一条纪律**：**AI 的报告只能当「待核实的草稿」**。正式交付的报告必须**基于你自己看过的原始输出**重写。

### 6.4 判断「这次用得成不成功」

| 观察 | 结论 |
|------|------|
| AI 的每一步都能对应到一条**具体命令** | ✅ 用得好 |
| 报告里有**你无法追溯来源**的结论 | ❌ **那是 AI 编的**，删掉 |
| `tools_available` 里大部分是 `false` | ⚠️ 工具没装够，AI 能力被限制 |
| 大量 `cached: true` | ⚠️ 可能拿到过期结果 |
| AI 无视 `success: false` 继续推进 | ❌ **立即接管** |
| AI 的目标跑出了你给的地址 | ❌ **立即停止**（见第 9 节的合规要求） |

---

## 7. 与其他工具配合

```
                        ┌──────────────────────────────────────┐
   你的意图（自然语言）   │  AI 客户端（Claude/Cursor/Copilot…）  │
                        └───────────────┬──────────────────────┘
                                        │ MCP
                        ┌───────────────▼──────────────────────┐
                        │      hexstrike_mcp（桥接）            │
                        └───────────────┬──────────────────────┘
                                        │ HTTP :8888
                        ┌───────────────▼──────────────────────┐
                        │   hexstrike_server（调度 + 执行）     │
                        └───────────────┬──────────────────────┘
                                        │ subprocess
        ┌───────────────┬───────────────┼───────────────┬───────────────┐
        ▼               ▼               ▼               ▼               ▼
     侦察类          Web 类          口令类         逆向类          云/容器
   nmap/amass     nuclei/sqlmap    hydra/john    radare2/ghidra  prowler/trivy
   ../01-信息搜集/  ../03-Web应用/   ../04-口令攻击/ 10-逆向工程/     （本库未覆盖）

   重要的「旁路」工具（不经过 AI，你自己用）：
   ┌─────────────────────────────────────────────────────────────────┐
   │ 概念验证与复测：手动跑一遍 AI 说它跑过的命令                        │
   │   nmap / nuclei / sqlmap / ffuf  ← 本库都有精讲，见上表            │
   │ 流量观察：tcpdump / wireshark / mitmproxy   → 07-嗅探与欺骗/      │
   │ 流量检测：snort（看 AI 的扫描会不会被检出） → 02-漏洞分析/snort.md │
   │ 报告整理：cherrytree / dradis               → 11-社会工程与报告/   │
   └─────────────────────────────────────────────────────────────────┘
```

**配合要点**：

| 组合 | 怎么做 |
|------|--------|
| **HexStrike + 本库工具教程** | **最关键的配合**：AI 说「用 nuclei 扫」，你要能判断「该用什么模板、什么强度」。**HexStrike 让你少打字，但不让你少懂** |
| **HexStrike + `tcpdump`/`wireshark`** | **验证 AI 到底发了什么包**（[`../07-嗅探与欺骗/tcpdump.md`](../07-嗅探与欺骗/tcpdump.md)）——比看日志更可信 |
| **HexStrike + `snort`** | 把 AI 的扫描流量**喂给 IDS**，看它会不会被检出（[`../02-漏洞分析/snort.md`](../02-漏洞分析/snort.md)）——**理解「扫描有多显眼」** |
| **HexStrike + `autorecon`** | 需要**确定性流程**时用 autorecon（脚本化、可复现），不要用 AI |
| **HexStrike + 靶场（DVWA 等）** | **唯一安全的练法**（[`../03-Web应用/dvwa.md`](../03-Web应用/dvwa.md)） |
| **HexStrike + 报告工具** | AI 出草稿 → 你核实 → 用 cherrytree/dradis 整理（[`../11-社会工程与报告/`](../11-社会工程与报告/)） |

**「什么时候不该用 HexStrike」**（很重要）：

| 情况 | 用什么 |
|------|--------|
| **正式客户项目 / 需要可复现** | **手动跑 + autorecon** —— AI 的决策不可复现，报告站不住 |
| **只需一个明确任务**（跑个 nuclei） | 直接跑 nuclei，**不要在中间加一层 AI** |
| **需要精确的参数控制** | 手动（AI 会「优化」掉你要的参数） |
| **生产环境 / 敏感数据** | **绝对不用**（有任意命令执行接口 + 结果会进 AI 上下文） |
| **想学工具本身** | **直接学工具**（本库的教程），HexStrike 学不到细节 |
| **想在 CI 里跑** | 用固定命令/脚本，**不用 AI** |

---

## 8. 常见坑与排错

| 报错/现象 | 原因 | 解决 |
|-----------|------|------|
| AI 说「没有 hexstrike 工具」 | **配置文件路径/内容不对**；或客户端没重启 | 检查 `claude_desktop_config.json` 的 JSON 语法（`python3 -c "import json;json.load(...)"`）；**重启客户端** |
| `hexstrike_mcp` 连不上 server | **server 没起**；或 `--server` 地址/端口不一致 | `curl http://127.0.0.1:8888/health`；`ss -lntp \| grep 8888` |
| **`hexstrike_server -h` 打完 banner 就没反应** | 这是**帮助输出**，不是启动 | 不带 `-h` 才是启动：`hexstrike_server --port 8888` |
| 端口 8888 被占用 | 别的服务占了 | `hexstrike_server --port 8899`（同时改 `--server` 参数和客户端配置） |
| AI 调工具总是 `success: false` | **工具没装**；或不在 PATH | `curl /health` 看 `tools_available`；补装；`command -v <tool>` |
| AI 说「扫描完成，没有发现问题」但 `stdout` 是空的 | **空输出 ≠ 没发现问题** | 核对参数、目标可达性、工具是否真的存在 |
| 长任务超时 | `hexstrike_mcp --timeout` 默认 300 秒不够 | 调大 `--timeout`；或用进程管理 API 提交后台任务 |
| 结果看起来是「旧数据」 | **`cached: true`**（缓存命中） | 换一下命令绕过缓存；或重启 server |
| 进程卡住/无法停止 | 长任务 | `GET /api/processes/list` → `POST /api/processes/terminate/<pid>` |
| 内存/CPU 被吃满 | server 起了多个工具进程 | 看 `/api/telemetry`；terminate 多余进程；**降低并发** |
| AI 的报告里有「没执行过的步骤」 | **AI 幻觉** | **只以 `command` + `stdout` 为准**；报告必须自己重写 |
| AI 擅自换了目标地址 | 提示词没约束好；或它「自作聪明」 | **提示词里明确「只允许 X」**；发现越界立即停止并复盘 |
| 结果里出现敏感信息（凭据/数据） | 工具真的扫到了 | **这些内容会进 AI 上下文**（可能被发送到模型服务商）→ **不要在真实目标上这么干** |
| 工具版本引起的参数不兼容 | HexStrike 封装的是某个版本的工具参数 | 以 `/api/command` 返回的 `stderr` 为准；**必要时退回手动调用该工具** |
| Kali 包的版本比上游旧 | 打包滞后 | 需要新功能就**从源码装**（虚拟环境） |
| 想让它扫公网 IP | —— | **停下**。除非那是你的、且你已确认授权 |

---

## 9. 防御视角（蓝队）

HexStrike 对蓝队有两重意义：**①它是「AI 自动化攻击」的一个现实样本，要能识别；②它是「AI + 安全」的一个学习样本，值得研究其风险模式。**

### 9.1 「AI 驱动的自动化扫描」的检测特征

**好消息**：**HexStrike 本身不隐藏流量**——它调用的还是 nmap/nuclei/sqlmap 这些**特征明显的工具**。

| 检测维度 | 特征 | 对策 |
|----------|------|------|
| **流量特征** | **与工具本体一致的指纹**（nmap 的探测模式、nuclei 的模板流量） | 已有的 WAF/IDS 规则**通常就能覆盖**（见 [`../02-漏洞分析/snort.md`](../02-漏洞分析/snort.md)） |
| **时序特征** | AI 的调用是**串行的、有思考间隔**（不像自动化脚本那么齐整） | 行为分析：**「有条理但不机械」的扫描节奏** |
| **来源** | 通常来自**云主机 / 新出现的 IP** | IP 信誉、地理异常 |
| **User-Agent** | 底层工具的原生 UA（nuclei/sqlmap 特征） | WAF 规则 |
| **覆盖面** | 往往**先广后深**（AI 会先「了解一下」） | 侦察阶段的探测告警 |

**关于「AI 会不会让它更隐蔽」**：

| 说法 | 现实 |
|------|------|
| 「AI 会规避检测」 | **不一定**——LLM 的决策来自通用知识，**并不包含「如何绕过你的具体 WAF」**；它调用的工具仍是标准工具 |
| 「会自适应」 | 有一定道理（它会根据失败换工具），但**换的还是那些工具** |
| 「会做的更快更全」 | **这个是真的**——**「省人力」才是它最大的影响**，而不是「更难检测」 |

**结论**：**AI 提升的是「攻击的广度与持续性」（不用人盯着），而不是「隐蔽性」**。所以蓝队的重点仍是：**资产可见性、补丁管理、以及基础检测能力**。

### 9.2 如果你在内部看到有人部署它（治理视角）

**这类工具的风险不在于「它是攻击工具」，而在于「它是一个未受管的高权限服务」**：

| 风险 | 说明 | 对策 |
|------|------|------|
| **任意命令执行接口** | `POST /api/command` —— 任何能访问该端口的东西都能执行命令 | **强制绑定回环**；网络层禁止该端口外露；EDR 监控监听端口 |
| **无认证** | 默认没有认证机制 | **绝不在共享主机上运行**；需要时最外层加认证代理 |
| **数据外流到 AI 服务商** | 扫描结果会进入 AI 的上下文 → **可能被发送到外部模型服务** | **禁止在含敏感数据的环境使用**；选择本地模型或企业版 |
| **提示注入** | AI 读到的内容可能含攻击指令（如一个网页/扫描结果里的「请执行…」） | **最小权限运行**；**不要给 AI 一个有 shell 的接口**（这正是自研 MCP 更安全的原因） |
| **未受管的工具安装** | 它会拉一堆工具进来 | 软件清单管控 |
| **资源占用** | 会起多个扫描进程 | 资源配额；容器化隔离 |
| **合规** | 在客户/公司网络里跑 = 未经授权的扫描 | **需要变更审批 + 授权范围文档** |

### 9.3 蓝队能主动做的（也是给自家团队的建议）

1. **先自研、再引进**：如果只想让 AI 做「选工具 + 解析结果」，**自己写一个只暴露 5 个只读工具的 MCP server**，比引入一个「任意命令执行平台」安全得多；
2. **沙盒化**：如果一定要用，**在一次性容器/VM 里跑**，网络策略限制其只能访问靶场网段；
3. **审计每一层**：`/api/command` 的 `command` 字段、server 日志、EDR 的进程树——**这三者要能对上**；
4. **控制输出**：**别让敏感目标的扫描结果进入外部 AI 服务**；
5. **把它的行为当训练素材**：**用 HexStrike 打你的靶场，看你的检测规则能不能抓到** —— **这是 AI 时代红队/蓝队演练的一个新课题**；
6. **对「AI 说的结论」保持怀疑**：**AI 的报告不是证据**。这条对攻击方和防守方同样适用——**也会有人拿 AI 生成的「漏洞报告」来找你要钱，先验证再处理**。

**一个值得警惕的新场景**：

```
收到一份「AI 生成的漏洞报告」声称你的系统有洞
              │
              ▼
先做三件事：
   ① 报告里的每个「结论」能不能对应到一条具体命令与输出？
   ② 那些命令真的跑过吗（看你的日志里有没有对应的流量）？
   ③ 报告里的目标地址是不是你的资产？
              │
              ▼
三者缺一，就很可能是【AI 幻觉产物】或【敲诈尝试】
```

---

## 10. 参考

- Kali 工具页（含 `hexstrike_mcp -h`、`hexstrike_server -h` 原文）：<https://www.kali.org/tools/hexstrike-ai/>
- 上游仓库（含架构、安装、API 参考、排查、安全说明）：<https://github.com/0x4m4/hexstrike-ai>
- Kali 包跟踪：<https://pkg.kali.org/pkg/hexstrike-ai>
- 本地命令与接口：`hexstrike_server -h`、`hexstrike_mcp -h`、`curl http://127.0.0.1:8888/health`、`curl http://127.0.0.1:8888/api/cache/stats`
- MCP（Model Context Protocol）规范（理解「工具是怎么暴露给 AI 的」）：<https://modelcontextprotocol.io/>
- 配套教程（**HexStrike 调用的每个工具，本库都有精讲——用它们来审阅 AI 的决策**）：
  - 侦察：[`../01-信息搜集/nmap.md`](../01-信息搜集/nmap.md)、[`../01-信息搜集/amass.md`](../01-信息搜集/amass.md)、[`../01-信息搜集/masscan.md`](../01-信息搜集/masscan.md)
  - 漏洞分析：[`../02-漏洞分析/nuclei.md`](../02-漏洞分析/nuclei.md)、[`../02-漏洞分析/nikto.md`](../02-漏洞分析/nikto.md)、[`../02-漏洞分析/snort.md`](../02-漏洞分析/snort.md)
  - Web：[`../03-Web应用/sqlmap.md`](../03-Web应用/sqlmap.md)、[`../03-Web应用/gobuster.md`](../03-Web应用/gobuster.md)、[`../03-Web应用/ffuf.md`](../03-Web应用/ffuf.md)、[`../03-Web应用/wpscan.md`](../03-Web应用/wpscan.md)、[`../03-Web应用/dvwa.md`](../03-Web应用/dvwa.md)
  - 口令：[`../04-口令攻击/hydra.md`](../04-口令攻击/hydra.md)、[`../04-口令攻击/hashcat.md`](../04-口令攻击/hashcat.md)、[`../04-口令攻击/john.md`](../04-口令攻击/john.md)
  - 逆向：[`radare2.md`](../10-逆向工程/radare2.md)、[`ghidra.md`](../10-逆向工程/ghidra.md)、[`gdb.md`](../10-逆向工程/gdb.md)
  - 抓包验证：[`../07-嗅探与欺骗/tcpdump.md`](../07-嗅探与欺骗/tcpdump.md)

## ⚠️ 法律与伦理

**HexStrike 是本教程里「最需要谨慎」的一篇**——因为它的设计目的就是**把强大的工具交给一个「不会判断合法性」的执行者（AI）**，而**AI 不会替你读授权书**。

**① 核心风险：AI 不做合法性判断**

```
   你说「帮我测试一下」                    AI 会：
        │                                   ① 猜一个它认为合理的范围
        ▼                                   ② 开始调工具
   AI 的理解可能是：                         ③ 遇到失败就换工具
   「测试一切它认为相关的目标」               ④ 生成一份「看起来很专业」的报告
        │
        ▼
   ⚠️ 它【不会】问：「这个 IP 是你的吗？」
   ⚠️ 它【不会】问：「你的授权书里有这个网段吗？」
   ⚠️ 它【不会】停：「我已经打到别人的系统上了」
```

**所以「谁对 AI 的行为负责」的答案是明确的**：**是你**。AI 不是责任主体。

| 行为 | 法律后果 |
|------|----------|
| 让 AI 对**未授权目标**做扫描 | 《网络安全法》第 27 条（非法侵入/干扰他人网络）；**《刑法》第 285 条**（非法获取计算机信息系统数据）；《刑法》第 286 条 |
| 让 AI 做**爆破 / 注入 / 利用** | 同上，且可能构成**第 286 条（破坏计算机信息系统）** |
| 用它在**工作中扫描公司网络** | **违反内部制度 + 可能违法**（除非有书面授权） |
| **把结果发到外部 AI 服务商** | 可能导致**数据泄露**（《个人信息保护法》《数据安全法》）；涉密数据可能触犯《保守国家秘密法》 |
| **分享「用 AI 打某站」的成果** | 可能构成《刑法》第 285 条之三（**提供侵入、非法控制计算机信息系统的程序、工具**）或教唆 |

**② 「AI 说的」不是「事实」——这对合法性和技术结论都成立**

- AI 可能**编造**「我扫了这个目标」「发现了这个漏洞」——**报告必须能追溯到具体命令与原始输出**；
- 如果你把 AI 生成的报告**当成事实交付给客户**，可能构成**虚假报告 / 欺诈**；
- 同理，**收到别人给的「AI 漏洞报告」时，先验证再处理**。

**③ 合法使用的边界**

| 场景 | 是否允许 |
|------|----------|
| 在**你自有的靶场**（DVWA、本地 VM）上练 | ✅ |
| **CTF** 中按比赛规则使用 | ✅ |
| **获得书面授权**的渗透测试（授权范围明确） | ✅ **但要在授权范围内，且你自己对每一步负责** |
| 用 AI 帮你**整理/解释你自己跑出来的输出** | ✅（结果不外泄的前提下） |
| 对**任何未授权目标**运行 | ❌ **违法** |
| 在**公司生产网络**做未报备的扫描 | ❌ 违规且可能违法 |
| 把**客户数据的扫描结果**送进外部 AI 服务 | ❌ **数据泄露风险** |

**必须遵守**：

1. **HexStrike 只在隔离的、你自己的测试环境里运行**（专用 VM + 快照 + 只连靶场网段）；
2. **保持默认的 `127.0.0.1` 监听**，**绝不**把它暴露到网络；
3. **绝不在含真实敏感数据的机器上运行**——扫描结果会进入 AI 上下文并可能被发送到外部模型服务；
4. **AI 的每一个动作都要审阅**（看 `command` 字段），**越界立即终止**；
5. **AI 的报告只能当草稿**——正式交付必须基于你亲自核实的**原始输出**；
6. **CTF / 靶场 / 书面授权**是唯一合规的使用场景；**「我只是想试试」不是理由**；
7. **不要分享**以它为主体的「自动化打靶/打站」教程与成果（可能构成提供工具或教唆）；
8. 任何情况下，**你都是行为的责任人**——**不要说「是 AI 做的」**。
