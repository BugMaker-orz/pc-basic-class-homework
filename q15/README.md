# 第15题：API 数据转报告

**主题**：HTTP 服务 + curl + jq 数据处理

## 题目要求

在 `q15` 中把本地 API 数据转换为可读报告：

- 保存 packages.json，在 q15 目录运行 `python -m http.server 8000`
- 用 `curl -fsS` 获取 JSON 数据
- 用 jq 筛选 `status == "active"` 且 `downloads >= 100`，按 downloads 降序、name 升序排列
- 编写 api_report.sh 生成 summary.md，包含标题和 name/version/downloads 三列表格

## 数据与筛选

packages.json 含 5 条记录。筛选后保留 3 条：delta(450)、gamma(450)、alpha(120)；epsilon 因 downloads=80 被排除，beta 因 inactive 被排除。

```bash
curl -fsS http://127.0.0.1:8000/packages.json |
  jq -r '[.[] | select(.status == "active" and .downloads >= 100)] | sort_by(-.downloads, .name)[] | "| \(.name) | \(.version) | \(.downloads) |"'
```

## 生成的 summary.md

| name | version | downloads |
|------|---------|-----------|
| delta | 0.9.0 | 450 |
| gamma | 1.5.1 | 450 |
| alpha | 1.2.0 | 120 |

## 关键技术点

- **curl -fsS**：-f 在 HTTP 错误时失败退出，-sS 静默但保留错误信息
- **jq 筛选排序**：`select()` 过滤 + `sort_by(-.downloads, .name)` 先降序再按名称升序
- **脚本化**：固定流程写进 api_report.sh（set -e），重复执行结果一致
