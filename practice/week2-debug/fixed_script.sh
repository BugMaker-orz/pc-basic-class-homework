#!/bin/sh
# 修复: 用 for glob 代替 ls; 变量加引号; 避免 -e 与 \\ 转义
for f in *.m3u; do
  [ -e "$f" ] || continue
  if grep -qi 'hq.*mp3' "$f"; then
    printf 'Playlist %s contains a HQ file in mp3 format\n' "$f"
  fi
done
