# 第10题：智能体修复循环

**主题**：智能体编程：失败测试驱动修复

## 题目要求

在 `q10` 中模拟一次智能体协作修复：

- 以 q09 为基线建立仓库，编写一个**失败测试**：`--name` 只含空白字符时，程序应退出码 2
- 运行 pytest 复现失败（基线程序对空白名不校验，退出码 0）
- 让智能体修复实现，人工用 `git diff` 检查改动范围后确认
- 记录修复过程的 `ai_log.md`，不超过 5 行

## 缺陷与修复

基线 `cli.py` 只做 `argparse` 必选检查，`--name " "` 会原样输出、退出码 0。失败测试断言退出码 2：

```python
def test_blank_name_exits_2():
    r = subprocess.run(
        [sys.executable, "-m", "greetlab.cli", "--name", " "],
        capture_output=True, text=True,
    )
    assert r.returncode == 2
```

修复后在 `main()` 中增加 `if not a.name.strip(): p.error(...)`，使空白名触发 `SystemExit(2)`；同时补 `if __name__ == "__main__": main()`，保证 `python -m` 也能执行。

## 修复日志（ai_log.md，3 行）

1. 提示：name 只含空白字符时 main 应以 SystemExit(2) 结束，仅改 cli.py
2. 改动：增加 strip() 空值校验（p.error → SystemExit(2)），补 `__main__` 入口
3. 验证：git diff 无无关改动，pytest 1 个用例通过

## 关键技术点

- **失败测试先行**：先写断言再改实现，测试能复现缺陷才谈得上修复
- **diff 审查**：人工确认改动只涉及目标文件，防止智能体顺手改无关代码
- **隐藏缺陷**：缺 `__main__` 时 `python -m` 无法执行，`-m` 场景测试才能暴露
