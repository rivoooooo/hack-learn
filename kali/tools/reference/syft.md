# syft

> CLI tool for generating a SBOM from container images and filesystems This package contains a CLI tool and Go library for generating a Software Bill of Materials (SBOM) from container images and filesystems. Exceptional for vulnerability de…

> **功能分类**：通用工具 ｜ **Kali 包**：`syft` ｜ **官方文档**：<https://www.kali.org/tools/syft/>

## 1. 安装

```bash
sudo apt update
sudo apt install syft
```

| 项目 | 内容 |
|------|------|
| 版本 | 1.51.0 |
| 架构 | any |
| 可执行命令 | `syft` |
| 依赖 | `libc6` |
| 安装体积 | 83.29 MB |
| 官网 | <https://github.com/anchore/syft> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/syft> |
| 包追踪 | <https://pkg.kali.org/pkg/syft> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
syft -h          # 查看用法
man syft         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `syft`

官方给出的调用示例：`syft -h`

```text
root@kali:~# syft -h
Generate a packaged-based Software Bill Of Materials (SBOM) from container images and filesystems
Usage:
  syft [SOURCE] [flags]
  syft [command]
Examples:
  syft scan alpine:latest                                a summary of discovered packages
  syft scan alpine:latest -o json                        show all possible cataloging details
  syft scan alpine:latest -o cyclonedx                   show a CycloneDX formatted SBOM
  syft scan alpine:latest -o cyclonedx-json              show a CycloneDX JSON formatted SBOM
  syft scan alpine:latest -o spdx                        show a SPDX 2.3 Tag-Value formatted SBOM
  syft scan alpine:latest -o
[email protected]
                    show a SPDX 2.2 Tag-Value formatted SBOM
  syft scan alpine:latest -o spdx-json                   show a SPDX 2.3 JSON formatted SBOM
  syft scan alpine:latest -o
[email protected]
               show a SPDX 2.2 JSON formatted SBOM
  syft scan alpine:latest -vv                            show verbose debug information
  syft scan alpine:latest -o template -t my_format.tmpl  show a SBOM formatted according to given template file
  Supports the following image sources:
    syft scan yourrepo/yourimage:tag     defaults to using images from a Docker daemon. If Docker is not present, the image is pulled directly from the registry.
    syft scan path/to/a/file/or/dir      a Docker tar, OCI tar, OCI directory, SIF container, or generic filesystem directory
  You can also explicitly specify the scheme to use:
    syft scan docker:yourrepo/yourimage:tag            explicitly use the Docker daemon
    syft scan podman:yourrepo/yourimage:tag            explicitly use the Podman daemon
    syft scan registry:yourrepo/yourimage:tag          pull image directly from a registry (no container runtime required)
    syft scan docker-archive:path/to/yourimage.tar     use a tarball from disk for archives created from "docker save"
    syft scan oci-archive:path/to/yourimage.tar        use a tarball from disk for OCI archives (from Skopeo or otherwise)
    syft scan oci-dir:path/to/yourimage                read directly from a path on disk for OCI layout directories (from Skopeo or otherwise)
    syft scan singularity:path/to/yourimage.sif        read directly from a Singularity Image Format (SIF) container on disk
    syft scan oci-model-registry:ai/llama3.2           scan an OCI model artifact from a registry (e.g. Docker Hub AI models)
    syft scan dir:path/to/yourproject                  read directly from a path on disk (any directory)
    syft scan file:path/to/yourproject/file            read directly from a path on disk (any single file)
Available Commands:
  attest      Generate an SBOM as an attestation for the given [SOURCE] container image
  cataloger   Show available catalogers and configuration
  completion  Generate the autocompletion script for the specified shell
  config      show the syft configuration
  convert     Convert between SBOM formats
  help        Help about any command
  login       Log in to a registry
  scan        Generate an SBOM
  version     show version information
Flags:
      --base-path string                          base directory for scanning, no links will be followed above this directory, and all paths will be reported relative to this directory
  -c, --config stringArray                        syft configuration file(s) to use
      --enrich stringArray                        enable package data enrichment from local and online sources (options: all, golang, java, javascript, python, vcpkg)
      --exclude stringArray                       exclude paths from being scanned using a glob expression
      --file string                               file to write the default report output to (default is STDOUT) (DEPRECATED: use: --output FORMAT=PATH)
      --from stringArray                          specify the source behavior to use (e.g. docker, registry, oci-dir, ...)
  -h, --help                                      help for syft
  -o, --output stringArray                        report output format (<format>=<file> to output to a file), formats=[cyclonedx-json cyclonedx-xml github-json purls spdx-json spdx-tag-value syft-json syft-table syft-text template] (default [syft-table])
      --override-default-catalogers stringArray   set the base set of catalogers to use (defaults to 'image' or 'directory' depending on the scan source)
      --parallelism int                           number of cataloger workers to run in parallel
      --platform string                           an optional platform specifier for container image sources (e.g. 'linux/arm64', 'linux/arm64/v8', 'arm64', 'linux')
      --profile stringArray                       configuration profiles to use
  -q, --quiet                                     suppress all logging output
  -s, --scope string                              selection of layers to catalog, options=[squashed all-layers deep-squashed] (default "squashed")
      --select-catalogers stringArray             add, remove, and filter the catalogers to be used
      --source-name string                        set the name of the target being analyzed
      --source-supplier string                    the organization that supplied the component, which often may be the manufacturer, distributor, or repackager
      --source-version string                     set the version of the target being analyzed
  -t, --template string                           specify the path to a Go template file
  -v, --verbose count                             increase verbosity (-v = info, -vv = debug)
      --version                                   version for syft
Use "syft [command] --help" for more information about a command.
Updated on: 2026-Aug-25
 Edit this page
subversion
tcpdump
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

- [ ] **1.** **装好并确认版本** —— `sudo apt install syft`，再执行 `syft --version` 2>/dev/null || `syft -V`
- [ ] **2.** **读官方帮助** —— `syft -h`，需要细节时 `man syft`
- [ ] **3.** **在自有靶场跑最小用例** —— 官方给出的调用形式是：`Usage:`
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/syft/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/syft/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/syft/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
