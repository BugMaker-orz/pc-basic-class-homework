#!/usr/bin/env bash
# 本地质量门禁：格式检查 + 静态检查 + 单元测试
set -e
echo "[1/3] ruff format --check"
ruff format --check --no-cache
echo "[2/3] ruff check"
ruff check --no-cache
echo "[3/3] pytest"
PYTHONPATH=src pytest
echo "OK: 质量门禁全部通过"
