# 第3题：制造、解决并解释一次合并冲突

**主题**：Version Control and Git

## 题目要求
在 `q03` 中从零创建 Git 仓库：
- 初始化仓库，在 main 分支创建 `config.txt`（内容 `mode=normal`）并初始提交
- 创建 `feature-a`，改为 `mode=safe` 并提交
- 从初始 main 创建 `feature-b`，改为 `mode=fast` 并提交
- 回到 main，先合并 feature-a，再合并 feature-b（产生冲突）
- 解决冲突时保留 `mode=safe`，另加一行 `note=reviewed`
- 确认工作区干净，运行 `git log --all --graph --decorate --oneline` 查看历史

## 冲突原因
feature-a 和 feature-b 都从同一初始提交分叉，且修改了 `config.txt` 的同一行，Git 无法自动调和，标记为冲突由人工解决。

## 冲突标记
```
<<<<<<< HEAD
mode=safe       # 当前分支内容
=======
mode=fast       # 被合并分支内容
>>>>>>> feature-b
```

## 结果
- 成功制造并解决合并冲突
- 最终内容：`mode=safe` + `note=reviewed`
- 工作区干净，提交历史图清晰显示分支与合并
