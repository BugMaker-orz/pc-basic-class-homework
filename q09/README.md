# 第9题：打包 greetlab 并在干净环境安装

**主题**：Python 打包分发

## 题目要求

在 `q09` 中创建可安装的 Python 包 greetlab：

- 使用 src 布局，包内提供命令行入口 `sdt-greet`，运行 `sdt-greet --name 25020007016` 输出问候语
- 用 `python -m build` 构建 wheel 包
- 在全新的虚拟环境中只从 wheel 安装，验证入口可正常运行

## 包结构

```
q09/
├── pyproject.toml        # 构建后端 setuptools + 入口声明
└── src/greetlab/
    ├── __init__.py
    └── cli.py            # argparse 解析 --name 并输出问候语
```

`cli.py` 用 `argparse` 声明必选参数 `--name`，打印 `Hello, {name}!`；`pyproject.toml` 在 `[project.scripts]` 中注册 `sdt-greet = "greetlab.cli:main"`。

## 构建与安装验证

```bash
python3 -m build -q                    # 产出 wheel 与 sdist
python3 -m venv ~/q09-venv             # 全新虚拟环境
~/q09-venv/bin/pip install dist/greetlab_25020007016-0.1.0-py3-none-any.whl -q
~/q09-venv/bin/sdt-greet --name 25020007016
# Hello, 25020007016!
```

## 关键技术点

- **src 布局**：源码放在 `src/greetlab/` 下，构建时只打包 src 内内容，避免仓库根目录杂项混入包
- **入口脚本**：`[project.scripts]` 声明后，安装 wheel 自动生成可执行脚本
- **干净环境验证**：全新 venv 只装 wheel 后运行，证明包不依赖开发环境隐式状态
