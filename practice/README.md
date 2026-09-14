# 课后练习：MIT Missing Semester 2026（计算机学生缺失的一课）

**来源**：[MIT Missing Semester 中文版 2026](https://mlbo.github.io/missing-semester-cn-2026/)
**要求**：每次课完成 >10 个实例

## 课程周次与讲次对应

| 周次 | 课程内容 | 2026 讲次 | 链接 |
|------|---------|-----------|------|
| 第1周 | 课程概览 + Shell 入门 | [课程概览与 Shell](https://mlbo.github.io/missing-semester-cn-2026/2026/course-shell/) | 1/12 |
| 第1周 | Version Control and Git | [版本控制与 Git](https://mlbo.github.io/missing-semester-cn-2026/2026/version-control/) | 1/16 |
| 第2周 | 命令行环境 | [命令行环境](https://mlbo.github.io/missing-semester-cn-2026/2026/command-line-environment/) | 1/13 |
| 第2周 | 开发环境与工具 | [开发环境与工具](https://mlbo.github.io/missing-semester-cn-2026/2026/development-environment/) | 1/14 |
| 第2周 | Debugging and Profiling | [调试与分析](https://mlbo.github.io/missing-semester-cn-2026/2026/debugging-profiling/) | 1/15 |
| 第3周 | Packaging and Shipping Code | [打包与发布代码](https://mlbo.github.io/missing-semester-cn-2026/2026/shipping-code/) | 1/20 |
| 第3周 | 智能体编程 | [代理编码](https://mlbo.github.io/missing-semester-cn-2026/2026/agentic-coding/) | 1/21 |
| 第3周 | 不止于代码 | [代码之外](https://mlbo.github.io/missing-semester-cn-2026/2026/beyond-code/) | 1/22 |
| 第4周 | 代码质量 + 元编程 | [代码质量](https://mlbo.github.io/missing-semester-cn-2026/2026/code-quality/) | 1/23 |

---

## 第1周：Shell + Git（17 个实例）

### 课程概览与 Shell（9 个，见 missing/）
讲次：https://mlbo.github.io/missing-semester-cn-2026/2026/course-shell/

1. `/tmp` 下新建 missing 文件夹
2. `man touch` 查看手册
3. `touch` 创建 semester 文件
4. 写入 shebang `#!/bin/sh` + curl 脚本
5. `./semester` 执行报 Permission denied（退出码 126）
6. `man chmod` 查看手册
7. `chmod +x` 后成功执行
8. 管道+重定向把 Last-Modified 写入 last-modified.txt
9. 从 `/sys`、`/proc` 读取系统信息

### 版本控制与 Git（8 个，见 week1-git/）
讲次：https://mlbo.github.io/missing-semester-cn-2026/2026/version-control/

1. 克隆课程仓库 `git clone https://github.com/missing-semester/missing-semester.git`
2. `git log --all --graph --decorate --oneline` 可视化历史
3. `git log -1 -- README.md`：最后修改者 Anish Athalye（commit 49f676c）
4. `git log -S "collections:" -- _config.yml`：commit e9ba75d
5. `~/.gitconfig` 配置 `[alias] graph = log --all --graph --decorate --oneline`
6. `git stash`：改 README → stash（工作区干净）→ stash pop（改动恢复）
7. 全局 `.gitignore_global` 忽略 `.DS_Store`、`.venv/`、`__pycache__/`，通过 `git config --global core.excludesfile ~/.gitignore_global` 全局生效
8. `git clone --depth 1` 浅克隆：只拉最新一次提交

---

## 第2周：命令行环境 + 开发工具 + Debugging（16 个实例）

### 命令行环境（5 个，见 week2-clenv/）
讲次：https://mlbo.github.io/missing-semester-cn-2026/2026/command-line-environment/

1. `touch -- -myfile`：`--` 之后的参数不被解析为 flag，文件名以 `-` 开头也能创建；删除用 `rm -- -myfile`
2. `diff <(printenv | sort) <(export | sort)`：printenv 输出裸 `KEY=VALUE`，export 输出 `declare -x KEY="VALUE"`，格式不同
3. 作业控制：`sleep 10000 &` 后台启动 → `pgrep -af` 找 PID → `pkill -f` 终止（注意 `-f` 会匹配命令行字符串，小心误杀）
4. `pidwait` 函数：`while kill -0 "$1" 2>/dev/null; do sleep 0.1; done` 等待指定 PID 退出
5. 别名：`alias dc=cd`；`history | awk '{$1="";print substr($0,2)}' | sort | uniq -c | sort -n | tail` 统计最常用命令
6. `tmux` 基础：`tmux new-session -d -s demo` 后台建会话，`tmux split-window -h` 水平分屏，`tmux capture-pane -p` 抓取屏幕内容，`tmux kill-session` 销毁

### 开发环境与工具（5 个，见 week2-shelltools/）
讲次：https://mlbo.github.io/missing-semester-cn-2026/2026/development-environment/

1. `ls -lhart --color=auto`：人类可读+按修改时间排序+彩色+含隐藏
2. `marco.sh`：marco 保存当前目录，polo cd 回去
3. `run_until_fail.sh`：循环跑随机脚本直到 exit 1，记录失败前次数（实测第 6 次失败）
4. `find -name '*.html' -print0 | xargs -0 zip`：含空格文件名也能正确压缩
5. `ls -lt` 按修改时间排序找最近文件

### 调试与分析（6 个，见 week2-debug/）
讲次：https://mlbo.github.io/missing-semester-cn-2026/2026/debugging-profiling/

1. `journalctl` 查看登录日志（容器无 systemd 时改看 `/var/log/`）
2. `pdb` 断点调试（q07 已实际使用）
3. `shellcheck` 检查 m3u 脚本：报 5 个问题（SC2045 遍历 ls、SC2086 变量未引号、SC2062 grep 模式未引号、SC3037 echo -e、SC2016 单引号不展开），修复后清零
4. `fib.py` 递归版结果 34；加 `lru_cache(1)` 后结果一致但调用次数指数下降
5. `lsof -i :4444` 找占用端口的进程 PID
6. `stress -c 3` + `htop` 可视化 CPU 占用
7. `cProfile` 对比插入排序 vs 快排：5000 个元素插入排序 0.391s，快排 0.006s（快 65 倍）

---

## 第3周：打包发布 + 智能体 + 代码之外（8 个实例）

### 打包与发布代码（2 个，见 week3-pkg/）
讲次：https://mlbo.github.io/missing-semester-cn-2026/2026/shipping-code/

1. `printenv | sort > before.txt` → `python -m venv .venv && source .venv/bin/activate` → `printenv | sort > after.txt` → diff：激活后 PATH 前面多了 `.venv/bin`，这就是 shell 优先用 venv 里的 python 的原因
2. 写 `pyproject.toml`（`[project]` name/version + `[build-system]` setuptools）→ 放 `demo_greet/__init__.py` → `python -m build` 产出 `.whl` 和 `.tar.gz`

### 代理编码（3 个，主观任务）
讲次：https://mlbo.github.io/missing-semester-cn-2026/2026/agentic-coding/

1. 同一任务分别手写/AI 补全/内联聊天/代理四次完成，对比体验
2. 用 AI 代理导航陌生代码库（如 opencode 的安全相关模块）
3. Vibe code 一个小应用，不手写一行代码
4. 为代理写 `AGENTS.md`：约定提交前跑 `ruff check . && pytest`，说明测试运行方式

### 代码之外（3 个，主观任务）
讲次：https://mlbo.github.io/missing-semester-cn-2026/2026/beyond-code/

1. 浏览 Redis/curl 源码，找 TODO、外部引用、"为什么不"注释的实例
2. `git log` 找一条好提交消息（解释 why）和一条弱消息（只描述 what），用问题→解决方案→影响结构重写弱消息
3. 比较三个 1000+ star 项目的 README，总结"做什么/为什么关心/怎么用/怎么装"四要素写法

---

## 第4周：代码质量 + 元编程（7 个实例）

### 代码质量（5 个，见 week4-meta/）
讲次：https://mlbo.github.io/missing-semester-cn-2026/2026/code-quality/

1. Makefile 实现 `clean` 目标并声明 `.PHONY`
2. 版本约束语法：`^`（兼容次版本）、`~`（兼容补丁号）、通配符、比较符
3. `.git/hooks/pre-commit`：提交前 `make paper.pdf`，失败则拒绝提交（实测通过）
4. GitHub Pages + GitHub Action 对 shell 文件跑 shellcheck
5. GitHub Action 对 md 文件跑 proselint/write-good

### 综合题（q13~q16，均已完成）
- q13 ruff+pytest 质量门禁
- q14 Makefile 增量构建
- q15 curl+jq 生成 Markdown 报告
- q16 修复陌生仓库 + wheel SHA-256
