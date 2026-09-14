# 课后练习：MIT Missing Semester

**来源**：[MIT Missing Semester 中文版](https://missing-semester-cn.github.io/)
**要求**：每次课完成 >10 个实例

## 第一周：Shell + Git（17 个实例）

### Shell（9 个，见 missing/ 目录）
1. `/tmp` 下新建 missing 文件夹
2. `man touch` 查看手册
3. `touch` 创建 semester 文件
4. 写入 shebang `#!/bin/sh` + curl 脚本
5. `./semester` 执行报 Permission denied（退出码 126）
6. `man chmod` 查看手册
7. `chmod +x` 后成功执行
8. 管道+重定向把 Last-Modified 写入 last-modified.txt
9. 从 `/sys`、`/proc` 读取系统信息

### Git（8 个，见 week1-git/）
1. 克隆课程仓库 `git clone https://github.com/missing-semester/missing-semester.git`
2. `git log --all --graph --decorate --oneline` 可视化历史
3. `git log -1 -- README.md`：最后修改者 Anish Athalye（commit 49f676c）
4. `git log -S "collections:" -- _config.yml`：commit e9ba75d
5. `~/.gitconfig` 配置 `[alias] graph = log --all --graph --decorate --oneline`
6. `git stash`：改 README → stash（工作区干净）→ stash pop（改动恢复）
7. 全局 `.gitignore_global` 忽略 `.DS_Store` 等临时文件
8. `git clone --depth 1` 浅克隆

## 第二周：Shell Tools + Debugging（11 个实例）

### Shell Tools（5 个，见 week2-shelltools/）
1. `ls -lhart --color=auto`：人类可读+按修改时间排序+彩色+含隐藏
2. `marco.sh`：marco 保存当前目录，polo cd 回去（marco/polo 函数）
3. `run_until_fail.sh`：循环跑随机脚本直到 exit 1，记录失败前次数（实测第 6 次失败）
4. `find -name '*.html' -print0 | xargs -0 zip`：含空格文件名也能正确压缩
5. `ls -lt` 按修改时间排序找最近文件

### Debugging & Profiling（6 个，见 week2-debug/）
1. `journalctl` 查看登录日志
2. `pdb` 断点调试（q07 已实际使用）
3. `shellcheck` 检查 m3u 脚本：报 5 个问题（SC2045 遍历 ls、SC2086 变量未引号、SC2062 grep 模式未引号、SC3037 echo -e、SC2016 单引号不展开），修复后清零
4. `fib.py` 递归版结果 34；加 `lru_cache(1)` 后结果一致但调用次数指数下降
5. `lsof -i :4444` 找占用端口的进程 PID
6. `stress -c 3` + `htop` 可视化 CPU 占用

## 第三周：Packaging + AI 工具 + PyTorch（课上检查题 q09~q12，均已完成）

- q09 从源码 build wheel 并在干净 venv 安装
- q10 AI 智能体修复循环（空白名 exit 2）
- q11 协作材料改写（Issue/提交信息/评审意见）
- q12 PyTorch 线性回归（zero_grad/backward/step，loss<0.001）

## 第四周：Metaprogramming + 综合（7 个实例）

### Metaprogramming（5 个，见 week4-meta/）
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
