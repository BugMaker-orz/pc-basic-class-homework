# 第4题：修复并构建一页技术说明

**主题**：LaTeX 文档编辑

## 题目要求
将模板保存为 `q04/report.tex`，补全内容并从命令行构建 PDF：
- 加入一个带编号和 label 的公式，在正文中使用 `\ref` 或 `\eqref` 引用
- 加入一个 2 行 2 列表格，设置 caption 和 label，在正文中引用该表
- 使用 `latexmk -pdf -halt-on-error` 或 `tectonic` 生成 `report.pdf`
- 确认 PDF 能打开，且交叉引用不显示"??"

## 关键技术点
- `\label{eq:avg}` + `\eqref{eq:avg}` 公式交叉引用
- `\caption` + `\label{tab:perm}` + `\ref{tab:perm}` 表格交叉引用
- 需编译两次：第一次写入 .aux，第二次解析引用
- `ctex` 宏包 + `xelatex` 引擎支持中文
- `-halt-on-error` 遇错即停

## 结果
- 成功生成 1 页 PDF
- 公式引用显示为"式(1)"，表格引用显示为"表 1"
- 无"??"标记，交叉引用正常
