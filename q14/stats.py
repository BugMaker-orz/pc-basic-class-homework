import csv

with open("data.csv") as f:
    rows = list(csv.DictReader(f))
scores = [int(r["score"]) for r in rows]
lines = [
    f"总人数: {len(rows)}",
    f"最高分: {max(scores)}",
    f"最低分: {min(scores)}",
    f"平均分: {sum(scores) / len(scores):.2f}",
]
with open("stats.txt", "w") as f:
    f.write("\n".join(lines) + "\n")
