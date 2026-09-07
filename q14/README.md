# 第14题：Makefile 增量构建

**主题**：构建自动化：make 目标与依赖

## 题目要求

在 `q14` 中编写 Makefile 管理数据统计与报告生成：

- `make all` 依次执行 stats.txt 和 report.txt 两个目标
- 用 Python 脚本读取 data.csv 生成统计文件，报告依赖统计文件
- `make clean` 只删除生成文件；all、clean 声明为 .PHONY
- 验证首次构建、无改动不重建、touch 触发重建、clean 只删生成物

## Makefile

```makefile
.PHONY: all clean

all: stats.txt report.txt

stats.txt: data.csv stats.py
	python3 stats.py

report.txt: stats.txt report.py
	python3 report.py

clean:
	rm -f stats.txt report.txt
```

## 执行结果

```bash
$ make all
python3 stats.py
python3 report.py
$ make all            # 无改动，不重复执行
make: Nothing to be done for 'all'.
$ touch data.csv      # 模拟数据更新
$ make all
python3 stats.py      # 依赖变更，重建
python3 report.py
$ make clean          # 只删生成物
rm -f stats.txt report.txt
```

stats.txt 输出总人数 4、最高分 92、最低分 78、平均分 85.75。

## 关键技术点

- **目标与依赖**：make 比较目标与依赖的时间戳决定是否重建
- **.PHONY**：all、clean 不是真实文件，声明伪目标避免与同名文件冲突
- **增量构建**：只重建依赖被改动的目标；touch 修改时间戳模拟数据更新
- **clean 语义**：只删生成物，不碰 data.csv、脚本与 Makefile
