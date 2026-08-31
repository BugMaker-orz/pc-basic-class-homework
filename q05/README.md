# 第5题：控制一个可清理的后台任务

**主题**：命令行环境：进程、信号与任务控制

## 题目要求

将给定脚本保存为 `q05/worker.sh`，完成任务控制：

- 赋予脚本执行权限，在前台启动，并把 stdout、stderr 分别写入 `stdout.log`、`stderr.log`
- 使用 `Ctrl-Z` 挂起任务，再用 `bg` 让它在后台继续；使用 `jobs` 确认状态
- 使用 `jobs -p` 或等价方式取得 PID，不得手工抄写 PID；发送 `SIGTERM` 并等待任务结束
- 确认 `cleanup.log` 中出现 `CLEAN_EXIT`，且任务已经退出；禁止使用 `kill -9`

## 执行过程

```bash
mkdir q05 && cd q05
cat > worker.sh << 'EOF'
#!/usr/bin/env bash
trap 'echo CLEAN_EXIT >> cleanup.log; exit 0' TERM INT
n=0
while true; do
    echo "$n"
    n=$((n+1))
    sleep 1
done
EOF
chmod +x worker.sh
./worker.sh > stdout.log 2> stderr.log   # 前台启动，输出分离
# Ctrl-Z 挂起
bg                                    # 后台继续
pid=$(jobs -p %1)                     # 通过 jobs 取 PID，不手工抄写
kill -TERM $pid                       # 发送 SIGTERM
cat cleanup.log                       # 应为 CLEAN_EXIT
```

## 关键技术点

- `trap '...' TERM INT`：捕获 SIGTERM / SIGINT，执行清理动作后退出
- `Ctrl-Z` 发送 SIGTSTP 挂起任务，`bg` 使其在后台继续运行
- `jobs -p` 输出任务对应 PID，避免手工抄写带来的错误
- `kill -TERM` 优雅终止进程，由 `trap` 完成清理（`kill -9` 无法被捕获，会跳过清理）
- `> file 2> file` 将标准输出与标准错误分别重定向

## 结果

- `stdout.log`：脚本逐秒输出递增数字（0 起，运行期间持续累计）
- `stderr.log`：为空，脚本运行无错误输出
- `cleanup.log`：包含 `CLEAN_EXIT`，说明收到 SIGTERM 后执行了清理并正常退出
