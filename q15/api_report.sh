#!/usr/bin/env bash
# 拉取本地 API 数据，用 jq 筛选排序，生成 summary.md
set -e
{
  echo "# 活跃软件包报告"
  echo
  echo "| name | version | downloads |"
  echo "|------|---------|-----------|"
  curl -fsS http://127.0.0.1:8000/packages.json |
    jq -r '[.[] | select(.status == "active" and .downloads >= 100)] | sort_by(-.downloads, .name)[] | "| \(.name) | \(.version) | \(.downloads) |"'
} > summary.md
echo "summary.md 已生成"
