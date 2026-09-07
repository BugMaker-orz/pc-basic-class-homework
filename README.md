# 系统开发工具基础 · 课程实验仓库

> 中国海洋大学 · 2026 年秋季学期

**授课教师**：周小伟  
**学生**：丁翊君（学号：25020007016）

本仓库收录《系统开发工具基础》四次课上实验的完整交付：代码、终端截图、LaTeX 报告与过程文档。所有内容按题分目录存放，分次提交，可逐题回放。

---

## 📄 实验报告

| 实验 | 主题 | 报告 | 页数 |
|------|------|------|------|
| 第一次 | Shell、Git、LaTeX | [lab1_report.pdf](report/lab1_report.pdf) | 19 页 |
| 第二次 | 命令行环境、调试、性能分析 | [lab2_report.pdf](report/lab2_report.pdf) | 19 页 |
| 第三次 | Python 打包与智能体编程 | [lab3_report.pdf](report/lab3_report.pdf) | 14 页 |
| 第四次 | 质量门禁、构建自动化、综合检查 | [lab4_report.pdf](report/lab4_report.pdf) | 17 页 |

> 报告 LaTeX 源码与 PDF 同目录存放（`report/labN_report.tex`），截图以 `\graphicspath{{./}}` 相对引用，重新编译即可复现。

---

## 📋 实验内容

### 第一次实验（2026-08-30）：Shell、Git、LaTeX

| 编号 | 题目 | 主题 | 目录 |
|------|------|------|------|
| 第1题 | 含空格文件名的批量整理 | Shell 基础与文件系统 | [q01/](q01/) |
| 第2题 | 随机访问日志统计 | Shell 管道与文本处理 | [q02/](q02/) |
| 第3题 | 制造、解决并解释一次合并冲突 | Version Control and Git | [q03/](q03/) |
| 第4题 | 修复并构建一页技术说明 | LaTeX 文档编辑 | [q04/](q04/) |

课后练习（MIT Missing Semester 第1讲，9 题）：见 [practice/](practice/)，截图见 [screenshots/](screenshots/)（18 张）。

### 第二次实验（2026-08-31）：命令行环境与调试

| 编号 | 题目 | 主题 | 目录 |
|------|------|------|------|
| 第5题 | 控制一个可清理的后台任务 | 进程、信号与任务控制 | [q05/](q05/) |
| 第6题 | 语义重构与本地开发反馈 | 开发环境与工具 | [q06/](q06/) |
| 第7题 | 用调试器定位归并排序缺陷 | Debugging | [q07/](q07/) |
| 第8题 | 用 cProfile 定位并消除热点 | 性能分析 | [q08/](q08/) |

截图见 [screenshots_week2/](screenshots_week2/)（12 张）。

### 第三次实验（2026-09-07）：Python 打包与智能体编程

| 编号 | 题目 | 主题 | 目录 |
|------|------|------|------|
| 第9题 | 打包 greetlab 并在干净环境安装 | Python 打包分发 | [q09/](q09/) |
| 第10题 | 智能体修复循环 | 失败测试驱动修复 | [q10/](q10/) |
| 第11题 | 协作材料改写 | Issue、提交信息与评审意见 | [q11/](q11/) |
| 第12题 | PyTorch 线性回归训练 | 基础训练循环 | [q12/](q12/) |

截图见 [screenshots_week3/](screenshots_week3/)（9 张）。

### 第四次实验（2026-09-14）：质量门禁与综合检查

| 编号 | 题目 | 主题 | 目录 |
|------|------|------|------|
| 第13题 | 本地质量门禁 | ruff + pytest | [q13/](q13/) |
| 第14题 | Makefile 增量构建 | make 目标与依赖 | [q14/](q14/) |
| 第15题 | API 数据转报告 | curl + jq 处理 | [q15/](q15/) |
| 第16题 | 修复并交付陌生小仓库 | 破坏—失败—修复—构建—提交 | [q16/](q16/) |

截图见 [screenshots_week4/](screenshots_week4/)（12 张）。

---

## 🖥️ 实验环境

前两次实验在个人电脑完成，后两次在课程云电脑完成，环境版本以各报告内的实验环境表为准：

| 项目 | 第一、二次实验（本地 PC） | 第三、四次实验（课程云电脑） |
|------|--------------------------|------------------------------|
| 操作系统 | Ubuntu 26.04.1 LTS | Ubuntu 22.04.3 LTS |
| Shell | GNU Bash 5.3.9 | GNU Bash |
| Python | 3.14.4（.venv） | 3.12.11 |
| git | 2.53.0 | git 2.x |
| 测试/检查 | pytest 9.0.2 · ruff 0.16.4 | pytest 9.1.1 · ruff 0.16.6 |
| 深度学习 | — | PyTorch 2.14.0+cpu |
| 文档排版 | XeTeX（TeX Live） | XeTeX（TeX Live） |

---

## 📊 Git 提交记录

共 **50 次分次提交**（`git rev-list --count HEAD`），遵循课程"禁止单次全量提交"要求：按 代码 → 截图 → 报告 → 文档 的顺序逐步迭代，每次提交内容聚焦、信息为祈使句。

```
git log --oneline
```

---

## 📁 目录结构

```
.
├── README.md                # 本文件
├── .gitignore               # 忽略 LaTeX 临时文件、Python 缓存与构建产物
├── docs/                    # 课程参考资料（教材、每周课上实验检查题）
├── practice/                # 课后练习（MIT Missing Semester 第1讲，9 题）
├── q01/ … q16/              # 第1–16题，每题独立目录（代码 + README + 过程文档）
├── screenshots/             # 第一周终端截图（18 张）
├── screenshots_week2/       # 第二周终端截图（12 张）
├── screenshots_week3/       # 第三周终端截图（9 张）
├── screenshots_week4/       # 第四周终端截图（12 张）
└── report/                  # 实验报告（lab1–lab4 的 PDF 与 LaTeX 源码）
```

---

## ✅ 可复现性说明

各题均可在本地复现验证，例如：

```bash
# 第10题：失败测试驱动修复（空白名应退出码 2）
cd q10 && PYTHONPATH=src pytest

# 第12题：PyTorch 线性回归（损失收敛到 0）
cd q12 && python3 train.py

# 第13题：本地质量门禁
cd q13 && bash check.sh

# 第14题：Makefile 增量构建
cd q14 && make all && make all && make clean
```
