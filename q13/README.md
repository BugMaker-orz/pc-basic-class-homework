# 第13题：本地质量门禁

**主题**：代码质量：ruff + pytest 门禁

## 题目要求

复用第10题项目，在 `q13` 中搭建本地质量门禁：

- 在 pyproject.toml 中加入 ruff 与 pytest 的最小配置
- 补充正常姓名与空白姓名两个测试，每个包含有效断言
- 运行 ruff format、ruff check 和 pytest，修复全部问题，**不得全局忽略规则**
- 编写 check.sh 依次执行三步检查，运行后返回 0

## 配置（pyproject.toml 追加）

```toml
[tool.ruff]
line-length = 100

[tool.pytest.ini_options]
testpaths = ["."]
```

## 质量检查与修复

初次 `ruff check` 报 3 个错误：

- `I001` import 块未排序格式化（ruff format 可自动修复）
- 两处 `PLW1510`：`subprocess.run` 未显式指定 `check` 参数

修复方式：为测试中的 `subprocess.run` 补 `check=False`（测试自行断言退出码，无需子进程抛异常），随后 `ruff format` 规范化，再次检查全部通过。

## check.sh（门禁脚本）

```bash
#!/usr/bin/env bash
set -e
ruff format --check --no-cache
ruff check --no-cache
PYTHONPATH=src pytest
```

运行输出三步全部通过，退出码 0。

## 关键技术点

- **三层门禁**：格式（format --check）、静态（ruff check）、行为（pytest）各管一层
- **PLW1510**：`check=False` 显式表达"故意不检查，由测试断言退出码"
- **set -e**：任一步非零退出即终止，失败不被后续命令掩盖
- **不全局忽略规则**：靠修代码解决问题，而不是在配置里关闭规则
