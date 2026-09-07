# 第11题：协作材料改写

**主题**：协作沟通：Issue、提交信息与评审意见

## 题目要求

在 `q11` 中围绕同一缺陷（空白 name 参数未报错），把低质量的协作材料改写成专业版本：

- 一条 Issue：可复现、带环境与命令
- 一条提交信息：符合 conventional commits 风格
- 一条评审意见：区分 Blocking 与 Suggestion
- 全文不超过 400 字

## 改写后的材料（communication.md）

- **Issue**：给出 Windows / Python 3.12 环境、复现命令 `sdt-greet --name " "`、期望（退出码 2）与实际（输出问候语、退出码 0）
- **提交信息**：`fix: 拒绝空白 name 参数并返回退出码 2`，正文说明校验逻辑与回归测试
- **评审意见**：Blocking 指出空白名仍以 0 退出违反 CLI 参数契约；Suggestion 建议输出前统一去首尾空白

## 关键技术点

- **Issue 可复现**：环境、命令、期望/实际结果三要素齐全
- **提交信息规范**：type(scope): summary 开头，正文解释动机与影响
- **评审分级**：Blocking 阻塞合并的问题与 Suggestion 可选改进分开写，避免混为一谈
