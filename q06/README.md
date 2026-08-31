# 第6题：语义重构与本地开发反馈

**主题**：开发环境与工具

## 题目要求

在 `q06` 中按照给定代码创建三个 Python 文件，并使用编辑器语言服务器完成一次语义重构：

- 在已配置好 Python、pytest 和 ruff 的课程环境中打开 `q06`，并启用 Python 语言服务器
- 分别演示**跳转到定义**和**查找引用**
- 使用**重命名符号**把模块 `math_utils` 改为 `calculate_total`，保证定义和所有代码引用同步改变
- 在 `app.py` 中临时加入未使用的 `import os`，用 `ruff` 发现并删除；最后运行 `ruff` 和 `pytest` 并保证通过

## 文件说明

| 文件 | 作用 |
|------|------|
| `calculate_total.py` | 定义函数 `total_price(price, count)`，返回 `price * count`（由 `math_utils.py` 语义重构而来） |
| `app.py` | 导入并调用 `total_price(12.5, 4)`，打印结果 |
| `test_math_utils.py` | pytest 测试用例，断言 `total_price(12.5, 4) == 50.0` |

## 执行过程

1. 创建三个文件（`math_utils.py`、`app.py`、`test_math_utils.py`），启用语言服务器
2. 演示跳转到定义 / 查找引用
3. 使用 IDE 重命名符号：模块 `math_utils` → `calculate_total`，所有 `import` 引用同步更新
4. 在 `app.py` 临时加入 `import os`，运行 `ruff check`：
   - `I001`：导入块未排序 / 未格式化
   - `F401`：`os` 已导入但未使用
5. 按 ruff 提示删除未使用的 `import os`，再次 `ruff check` 通过
6. 安装 pytest 依赖后运行 `pytest`，1 个测试用例通过

## 关键技术点

- **Python 语言服务器**：IDE 基于语言服务器提供跳转、引用、重命名等语义能力
- **重命名符号（Shift+F6）**：一次操作同步更新定义与所有引用，避免手改遗漏
- **ruff**：轻量 Python 静态检查工具，`F401` 检查未使用导入，`I001` 检查导入块格式
- **pytest**：单元测试框架，`test_` 前缀函数自动收集并执行

## 结果

- `calculate_total.py` 定义 `total_price`，`app.py` 与 `test_math_utils.py` 的 import 全部同步更新
- `ruff check` 通过（无 `F401` / `I001` 告警）
- `pytest` 通过：`1 passed in 0.01s`
