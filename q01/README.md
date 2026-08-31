# 第1题：含空格文件名的批量整理

**主题**：Shell 基础与文件系统

## 题目要求

在当前目录新建 `q01`，完全使用命令行完成：

- 创建 `input/docs` 和 `input/tmp` 目录
- 创建含空格文件名 `notes one.txt`、文件 `secret.txt`、空文件 `empty.txt`、日志文件 `run.log`
- 显示 `q01` 绝对路径，长格式列出 `input` 下全部项目
- 将所有 `.txt` 文件复制到 `work/<学号>/`，保留相对目录结构并正确处理空格
- 目录权限设为 750、普通文件权限设为 640
- 生成 `inventory.txt`，列出相对路径和字节数

## 关键技术点

- `mkdir -p input/{docs,tmp}` 花括号展开一次创建多个目录
- `find -print0 | tar --null -T -` 通过管道打包传输文件名，正确处理空格
- `tar -cf - ... | (cd 目标 && tar -xvf -)` 子 shell 切换目录解包，保留相对结构
- `chmod 750` / `chmod 640` 数字权限设置
- `find -printf "%P %s\n"` 生成相对路径和字节数清单

## 结果

- 3 个 txt 文件成功复制（含空格文件名 `notes one.txt` 和 `secret.txt`）
- 目录权限 750，文件权限 640
- `inventory.txt` 包含相对路径和字节数
