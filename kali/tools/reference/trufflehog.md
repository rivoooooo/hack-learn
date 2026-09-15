# trufflehog

> Searches through git repositories for secrets This package contains a utitlity to search through git repositories for secrets, digging deep into commit history and branches. This is effective at finding secrets accidentally committed.

> **功能分类**：通用工具 ｜ **Kali 包**：`trufflehog` ｜ **官方文档**：<https://www.kali.org/tools/trufflehog/>

## 1. 安装

```bash
sudo apt update
sudo apt install trufflehog
```

| 项目 | 内容 |
|------|------|
| 版本 | 3.94.3 |
| 架构 | amd64 |
| 可执行命令 | `trufflehog` |
| 依赖 | `libc6` |
| 安装体积 | 118.50 MB |
| 官网 | <https://github.com/trufflesecurity/truffleHog> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/trufflehog> |
| 包追踪 | <https://pkg.kali.org/pkg/trufflehog> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
trufflehog -h          # 查看用法
man trufflehog         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `trufflehog`

> 官方示例调用：`trufflehog -h`

```text
root@kali:~# trufflehog -h
usage: TruffleHog [<flags>] <command> [<args> ...]
TruffleHog is a tool for finding credentials.
Flags:
  -h, --[no-]help                Show context-sensitive help (also try
                                 --help-long and --help-man).
      --log-level=0              Logging verbosity on a scale of 0 (info) to 5
                                 (trace). Can be disabled with "-1".
      --[no-]profile             Enables profiling and sets a pprof and fgprof
                                 server on :18066.
  -j, --[no-]json                Output in JSON format.
      --[no-]json-legacy         Use the pre-v3.0 JSON format. Only works with
                                 git, gitlab, and github sources.
      --[no-]github-actions      Output in GitHub Actions format.
      --concurrency=6            Number of concurrent workers.
      --[no-]no-verification     Don't verify the results.
      --results=RESULTS          Specifies which type(s) of results to output:
                                 verified (confirmed valid by API),
                                 unknown (verification failed due to error),
                                 unverified (detected but not verified),
                                 filtered_unverified (unverified but would
                                 have been filtered out). Defaults to
                                 verified,unverified,unknown.
      --[no-]no-color            Disable colorized output
      --[no-]allow-verification-overlap
                                 Allow verification of similar credentials
                                 across detectors
      --[no-]filter-unverified   Only output first unverified result per
                                 chunk per detector if there are more than one
                                 results.
      --filter-entropy=FILTER-ENTROPY
                                 Filter unverified results with Shannon entropy.
                                 Start with 3.0.
      --max-decode-depth=5       Maximum depth of iterative decoding.
                                 Each decoder's output is fed back through all
                                 decoders, up to this limit. 1 = single pass, 2+
                                 = chained decoding (e.g., base64 inside utf16).
      --config=CONFIG            Path to configuration file.
      --[no-]print-avg-detector-time
                                 Print the average time spent on each detector.
      --[no-]no-update           Don't check for updates.
      --[no-]fail                Exit with code 183 if results are found.
      --[no-]fail-on-scan-errors
                                 Exit with non-zero error code if an error
                                 occurs during the scan.
      --verifier=VERIFIER ...    Set custom verification endpoints.
      --[no-]custom-verifiers-only
                                 Only use custom verification endpoints.
      --detector-timeout=DETECTOR-TIMEOUT
                                 Maximum time to spend scanning chunks per
                                 detector (e.g., 30s).
      --archive-max-size=ARCHIVE-MAX-SIZE
                                 Maximum size of archive to scan. (Byte units
                                 eg. 512B, 2KB, 4MB)
      --archive-max-depth=ARCHIVE-MAX-DEPTH
                                 Maximum depth of archive to scan.
      --archive-timeout=ARCHIVE-TIMEOUT
                                 Maximum time to spend extracting an archive.
      --include-detectors="all"  Comma separated list of detector types to
                                 include. Protobuf name or IDs may be used,
                                 as well as ranges.
      --exclude-detectors=EXCLUDE-DETECTORS
                                 Comma separated list of detector types to
                                 exclude. Protobuf name or IDs may be used,
                                 as well as ranges. IDs defined here take
                                 precedence over the include list.
      --[no-]no-verification-cache
                                 Disable verification caching
      --[no-]force-skip-binaries
                                 Force skipping binaries.
      --[no-]force-skip-archives
                                 Force skipping archives.
      --[no-]skip-additional-refs
                                 Skip additional references.
      --user-agent-suffix=USER-AGENT-SUFFIX
                                 Suffix to add to User-Agent.
      --[no-]version             Show application version.
Commands:
help [<command>...]
    Show help.
git [<flags>] <uri>
    Find credentials in git repositories.
github [<flags>]
    Find credentials in GitHub repositories.
github-experimental --repo=REPO [<flags>]
    Run an experimental GitHub scan. Must specify at least one experimental
    sub-module to run: object-discovery.
gitlab --token=TOKEN [<flags>]
    Find credentials in GitLab repositories.
filesystem [<flags>] [<path>...]
    Find credentials in a filesystem.
s3 [<flags>]
    Find credentials in S3 buckets.
gcs [<flags>]
    Find credentials in GCS buckets.
syslog --format=FORMAT [<flags>]
    Scan syslog
circleci --token=TOKEN
    Scan CircleCI
docker [<flags>]
    Scan Docker Image
travisci --token=TOKEN
    Scan TravisCI
postman [<flags>]
    Scan Postman
elasticsearch [<flags>]
    Scan Elasticsearch
jenkins --url=URL [<flags>]
    Scan Jenkins
huggingface [<flags>]
    Find credentials in HuggingFace datasets, models and spaces.
stdin
    Find credentials from stdin.
multi-scan
    Find credentials in multiple sources defined in configuration.
json-enumerator [<path>...]
    Find credentials from a JSON enumerator input.
analyze
    Analyze API keys for fine-grained permissions information.
Updated on: 2026-May-25
 Edit this page
tree
twofi
LIGHT
DARK
Links
Home
Download / Get Kali
Blog
OS Documentation
Tool Documentation
System Status
Archived Releases
Partnerships
Platforms
ARM (SBC)
NetHunter (Mobile)
Amazon AWS
Docker
Linode
Microsoft Azure
Microsoft Store (WSL)
Vagrant
Development
Bug Tracker
Continuous Integration
Network Mirror
Package Tracker
GitLab
Community
Discord
Support Forum
PeerTube
Follow Us
Bluesky
Facebook
Instagram
Mastodon
Substack
X
Newsletter
RSS
Policies
Cookie Policy
Privacy Policy
Trademark Policy
© OffSec Services Limited 2026. All rights reserved.
Kali Linux is part of OffSec's Community Projects
Learn more about OffSec's free, open-source penetration testing tools for cybersecurity professionals
```

## 4. 实践清单

按顺序做完这五步，就能把工具从「装上」推进到「会用」：

- [ ] **1.** **装好并确认版本** —— `sudo apt install trufflehog`，再执行 `trufflehog --version` 2>/dev/null || `trufflehog -V`
- [ ] **2.** **读官方帮助** —— `trufflehog -h`，需要细节时 `man trufflehog`
- [ ] **3.** **在自有靶场跑最小用例** —— 用 `trufflehog -h` 里最简单的那个子命令试一次
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/trufflehog/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/credential-access.md`](../../tools/by-attack/credential-access.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/trufflehog/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/trufflehog/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
