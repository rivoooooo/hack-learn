#!/usr/bin/env bash
# 拉取 Linux 内核源码到 kernel/src/linux
#
# 用法:
#   bash scripts/fetch_linux_kernel.sh              # 浅克隆主线（约 1.5 GB，推荐）
#   bash scripts/fetch_linux_kernel.sh --full       # 完整历史（约 5 GB+，含 git log/blame）
#   bash scripts/fetch_linux_kernel.sh --stable     # 拉取最新 stable 分支
#
# 说明:
#   - 学习内核结构用 --depth 1 即可；需要追溯某行代码的历史时再改用 --full。
#   - 国内网络可先设置镜像：
#       export KERNEL_MIRROR=https://gitclone.com/github.com/torvalds/linux.git
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
DEST="$ROOT/kernel/src/linux"
MIRROR="${KERNEL_MIRROR:-https://github.com/torvalds/linux.git}"

MODE="shallow"
BRANCH="master"
for arg in "$@"; do
  case "$arg" in
    --full)   MODE="full" ;;
    --stable) BRANCH="linux-6.12.y"; MIRROR="https://git.kernel.org/pub/scm/linux/kernel/git/stable/linux.git" ;;
    *) echo "未知参数: $arg" >&2; exit 1 ;;
  esac
done

echo "[*] 仓库: $MIRROR"
echo "[*] 分支: $BRANCH"
echo "[*] 目标: $DEST"
echo "[*] 模式: $MODE"

mkdir -p "$ROOT/kernel/src"

if [ -d "$DEST/.git" ]; then
  echo "[=] 已存在仓库，执行增量更新 ..."
  git -C "$DEST" fetch --all --tags
  git -C "$DEST" checkout "$BRANCH"
  git -C "$DEST" pull --ff-only || echo "[!] 拉取失败，请手动检查"
else
  if [ "$MODE" = "full" ]; then
    git clone --branch "$BRANCH" "$MIRROR" "$DEST"
  else
    git clone --depth 1 --branch "$BRANCH" "$MIRROR" "$DEST"
  fi
fi

echo
echo "[+] 完成。内核版本："
make -s -C "$DEST" kernelversion 2>/dev/null || git -C "$DEST" describe --tags 2>/dev/null || true
echo
echo "下一步："
echo "  cd kernel/src/linux"
echo "  make defconfig          # 生成默认配置"
echo "  make -j\$(nproc)          # 编译（首次约 10-30 分钟）"
echo "  详见 kernel/docs/01-内核构建与调试.md"
