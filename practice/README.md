# 课后练习：MIT Missing Semester 第1讲

**来源**：[课程概览与 Shell - Missing Semester](https://missing-semester-cn.github.io/2020/course-shell/)

## 练习列表

| 编号 | 题目 | 关键命令 |
|------|------|----------|
| 1 | 在 /tmp 下新建 missing 文件夹 | `mkdir -p` |
| 2 | 用 man 查看 touch 使用手册 | `man touch` / `touch --help` |
| 3 | 用 touch 创建 semester 文件 | `touch` |
| 4 | 写入 shebang + curl 脚本内容 | `printf`, `#!/bin/sh` |
| 5 | 尝试执行 ./semester（Permission denied） | 退出码 126，缺少 x 权限 |
| 6 | 查看 chmod 手册 | `chmod --help` |
| 7 | chmod +x 后成功执行，理解 shebang | `chmod +x` |
| 8 | 管道+重定向提取 Last-Modified 写入文件 | `| grep > file` |
| 9 | 从 /sys 获取系统信息 | `/sys/class/`, `/proc/meminfo` |

## 核心收获
- shebang（`#!/bin/sh`）告诉系统用哪个解释器执行脚本
- 文件需有执行权限（x）才能直接 `./file` 运行
- 管道 `|` 连接程序输出与输入，重定向 `>` 将输出写入文件
- `/sys` 和 `/proc` 是 Linux 内核暴露的虚拟文件系统，可读取系统信息
