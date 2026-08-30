# 系统开发工具基础 - 第一次实验

> 中国海洋大学 · 2026年秋季学期

**授课教师**：周小伟  
**学生**：丁翊君（学号：25020007016）  
**实验日期**：2026年8月30日

---

## 📄 实验报告

- **[实验报告 PDF（19页）](report/lab1_report.pdf)**
- [实验报告 LaTeX 源码](report/lab1_report.tex)

---

## 📋 实验内容

本次实验涵盖三个主题：Shell 入门、Version Control and Git、LaTeX 文档编辑。

### 课上实验（4题）

| 编号 | 题目 | 主题 | 目录 |
|------|------|------|------|
| 第1题 | 含空格文件名的批量整理 | Shell 基础与文件系统 | [q01/](q01/) |
| 第2题 | 随机访问日志统计 | Shell 管道与文本处理 | [q02/](q02/) |
| 第3题 | 制造、解决并解释一次合并冲突 | Version Control and Git | [q03/](q03/) |
| 第4题 | 修复并构建一页技术说明 | LaTeX 文档编辑 | [q04/](q04/) |

### 课后练习

来自课程参考资料 [MIT Missing Semester 第1讲](https://missing-semester-cn.github.io/2020/course-shell/)，共 9 道原题：

- 目录操作、man 手册、文件创建
- 脚本编写、权限管理、shebang 机制
- 管道与重定向、sysfs 系统信息

详见 [practice/](practice/)

---

## 🖥️ 实验环境

- **操作系统**：Ubuntu 22.04.3 LTS (Linux)
- **Shell**：GNU Bash 5.1.16
- **Git**：version 2.34.1
- **LaTeX**：XeTeX 3.141592653-2.6-0.999993
- **文本处理**：awk (mawk), sort, head, grep

---

## 📊 Git 提交记录

共 12 次分次提交（禁止单次全量提交），涵盖代码、截图、报告和文档的逐步迭代。

```
git log --oneline
```

---

## 📁 目录结构

```
.
├── README.md              # 本文件
├── .gitignore             # Git 忽略规则
├── q01/                   # 第1题：Shell 文件操作
├── q02/                   # 第2题：日志统计脚本
├── q03/                   # 第3题：Git 合并冲突
├── q04/                   # 第4题：LaTeX 文档
├── practice/              # 课后练习（Missing Semester）
├── screenshots/           # 终端截图（18张）
└── report/                # 实验报告
    ├── lab1_report.pdf    # 报告 PDF（19页）
    └── lab1_report.tex    # 报告 LaTeX 源码
```
