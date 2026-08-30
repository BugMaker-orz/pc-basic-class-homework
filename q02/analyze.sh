#!/usr/bin/env bash
# analyze.sh - 访问日志统计脚本
# 用法: ./analyze.sh <csv_file>

set -euo pipefail

# 检查参数
if [ $# -ne 1 ]; then
    echo "用法: $0 <csv_file>" >&2
    exit 1
fi

CSV_FILE="$1"

# 检查文件是否存在
if [ ! -f "$CSV_FILE" ]; then
    echo "错误: 文件 '$CSV_FILE' 不存在" >&2
    exit 1
fi

echo "=== HTTP 5xx 数量最多的前 2 个 path ==="

# 筛选5xx状态码，统计每个path的出现次数，按次数降序、path字典序，取前2
# 跳过表头（NR>1），第4列是status，第3列是path
awk -F',' 'NR>1 && $4 ~ /^5[0-9][0-9]$/ {count[$3]++}
END {
    for (p in count) {
        printf "%d %s\n", count[p], p
    }
}' "$CSV_FILE" | sort -k1,1nr -k2,2 | head -n 2 | awk '{print $2, $1}'

echo ""
echo "=== 全部数据行的平均 latency_ms ==="

# 计算平均latency，跳过表头，第5列是latency_ms
awk -F',' 'NR>1 {sum+=$5; count++}
END {
    if (count > 0) {
        printf "%.2f\n", sum/count
    } else {
        print "0.00"
    }
}' "$CSV_FILE"
