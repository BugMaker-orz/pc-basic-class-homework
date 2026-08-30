# 第2题：随机访问日志统计

**主题**：Shell 管道与文本处理

## 题目要求
在 `q02` 中创建 `access.csv`，编写 `analyze.sh`：
- 接收一个 CSV 文件路径，文件不存在时将错误写入 stderr 并返回非零退出码
- 使用 Shell 管道及 awk、sort、head 等工具，输出 HTTP 5xx 数量最多的前 2 个 path（按次数降序，次数相同按 path 字典序）
- 输出全部数据行的平均 `latency_ms`，保留两位小数（表头不计入）
- 分别对 `access.csv` 和不存在的文件运行脚本，不得使用 Python

## 关键技术点
- `set -euo pipefail` 脚本健壮性
- `echo "..." >&2` 标准错误输出
- `exit 1` 非零退出码
- awk 关联数组 `count[$3]++` 统计
- `sort -k1,1nr -k2,2` 多字段排序
- `NR>1` 跳过表头

## 结果
- 5xx Top2：`/api/orders` (3次)、`/api/users` (2次)
- 平均延迟：193.75 ms
- 不存在文件时输出错误到 stderr，退出码 1
