# 第16题：修复并交付一个陌生的小型工具仓库

**主题**：综合检查：破坏—失败—修复—构建—提交

## 题目要求

复用第13题项目，在 `q16` 中完成一次 15 分钟综合检查：

- 复制 q13 为 q16 并初始化/继续使用 Git
- 临时改字面量使 check.sh 失败，确认门禁能抓住问题
- 修复后门禁通过；Makefile 提供 check / build / clean 目标
- 运行 make check / make build，校验 wheel 的 SHA-256
- 提交只包含有意义的改动（内容聚焦提交）

## 流程

```bash
git init && git add -A
git commit -m "q16: import q13 project as baseline"

# 临时把问候语改成字面量 "Hello, name!"
./check.sh          # 测试失败，门禁拦住回归

# 修复 f-string，恢复问候
make check          # 全部通过

make build          # 生成 wheel 与 sdist
sha256sum dist/*.whl
git add -A && git commit -m "fix: restore f-string greeting, add check/build/clean targets"
git log --oneline   # 两条提交：基线 + 修复
```

## 关键技术点

- **先破坏再修复**：临时引入回归并让门禁失败，验证测试确实能抓住问题
- **Makefile 三目标**：check 复用门禁脚本、build 生成可分发包、clean 清理产物
- **SHA-256 校验**：交付时凭指纹校验包完整性
- **内容聚焦提交**：.gitignore 排除 dist、egg-info、缓存，提交只含源码与构建配置
