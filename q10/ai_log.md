# ai_log.md — 智能体修复循环记录

1. 提示：name 只含空白字符时 main 应以 SystemExit(2) 结束，仅改 cli.py，保持既有功能。
2. 改动：增加 strip() 空值校验（p.error → SystemExit(2)），并补 if __name__ == "__main__": main() 入口。
3. 验证：git diff 无无关改动，pytest 空白名用例通过。
