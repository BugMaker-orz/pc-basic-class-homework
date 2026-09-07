with open("stats.txt") as f:
    stats = f.read().strip()

report = "# 成绩统计报告\n\n" + stats + "\n\n报告生成时间: make 增量构建\n"
with open("report.txt", "w") as f:
    f.write(report)
