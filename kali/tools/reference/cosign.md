# cosign

> Code signing/transparency for containers and binaries (program) Signing OCI containers (and other artifacts) using Sigstore Cosign supports: “Keyless signing” with the Sigstore public good Fulcio certificate authority and Rekor transparenc…

> **功能分类**：通用工具 ｜ **Kali 包**：`cosign` ｜ **官方文档**：<https://www.kali.org/tools/cosign/>

## 1. 安装

```bash
sudo apt update
sudo apt install cosign
```

| 项目 | 内容 |
|------|------|
| 版本 | 3.1.1 |
| 架构 | any |
| 可执行命令 | `cosign`、`golang-github-sigstore-cosign-dev` |
| 依赖 | `libc6` |
| 安装体积 | 84.77 MB |
| 官网 | <https://github.com/sigstore/cosign> |
| 源码仓库 | <https://salsa.debian.org/go-team/packages/cosign> |
| 包追踪 | <https://pkg.kali.org/pkg/cosign> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
cosign -h          # 查看用法
man cosign         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 2 个可执行命令，下面是官方页面内嵌的帮助原文。

### `cosign`

官方给出的调用示例：`cosign -h`

```text
root@kali:~# cosign -h
A tool for Container Signing, Verification and Storage in an OCI registry.
Usage:
cosign [command]
Available Commands:
attest                  Attest the supplied container image.
attest-blob             Attest the supplied blob.
bundle                  Interact with a Sigstore protobuf bundle
clean                   Remove all signatures from an image.
completion              Generate completion script
download                Provides utilities for downloading artifacts and attached artifacts in a registry
env                     Prints Cosign environment variables
generate-key-pair       Generates a key-pair.
help                    Help about any command
import-key-pair         Imports a PEM-encoded RSA or EC private key.
initialize              Initializes SigStore root to retrieve trusted certificate and key targets for verification.
load                    Load a signed image on disk to a remote registry
login                   Log in to a registry
public-key              Gets a public key from the key-pair.
save                    Save the container image and associated signatures to disk at the specified directory.
sign                    Sign the supplied container image.
sign-blob               Sign the supplied blob, outputting the base64-encoded signature to stdout.
signing-config          Interact with a Sigstore protobuf signing config
tree                    Display supply chain security related artifacts for an image such as signatures, SBOMs and attestations
trusted-root            Interact with a Sigstore protobuf trusted root
verify                  Verify a signature on the supplied container image
verify-attestation      Verify an attestation on the supplied container image
verify-blob             Verify a signature on the supplied blob
verify-blob-attestation Verify an attestation on the supplied blob
version                 Prints the version
Flags:
    -h, --help=false:
	help for cosign
    --output-file='':
	log output to a file
    -t, --timeout=3m0s:
	timeout for commands
    -d, --verbose=false:
	log debug output
Additional help topics:
cosign piv-tool                This cosign was not built with piv-tool support!
cosign pkcs11-tool             This cosign was not built with pkcs11-tool support!
Use "cosign [command] --help" for more information about a command.
```

## 4. 实践清单

按顺序做完这五步，就能把工具从「装上」推进到「会用」：

- [ ] **1.** **装好并确认版本** —— `sudo apt install cosign`，再执行 `cosign --version` 2>/dev/null || `cosign -V`
- [ ] **2.** **读官方帮助** —— `cosign -h`，需要细节时 `man cosign`
- [ ] **3.** **在自有靶场跑最小用例** —— 官方给出的调用形式是：`Usage:`
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/cosign/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/cosign/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/cosign/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
