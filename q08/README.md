# 第8题：先测量，再优化慢速词频程序

**主题**：Profiling

## 题目要求

在 `q08` 中创建可重复生成的词表和故意低效的去重程序，再使用性能分析工具优化：

- 生成 `words.txt`，使用 `time` 运行原程序 2 次并记录耗时
- 使用 `cProfile -s cumulative` 运行一次，找出主要耗时位置
- 在不改变最终 count 的前提下优化程序；不得写死 1000
- 使用相同输入再运行 2 次，计算优化前后中位数和加速比

## 原始程序（O(n²) 去重）

`wordfreq.py` 使用列表 + `in` 线性扫描去重，每次判断都要遍历已收集的唯一词：

```python
words = open("words.txt", encoding="utf-8").read().split()
unique = []
for word in words:
    if word not in unique:      # O(n) 线性扫描，整体 O(n²)
        unique.append(word)
print("count=", len(unique))
```

`generate_words.py` 用固定 seed（20260831）生成 30000 个词（词表 1000），保证可重复。

## cProfile 定位

```bash
python3 -m cProfile -s cumulative wordfreq.py
```

输出显示主要耗时集中在模块级代码（`wordfreq.py:1(<module>)`，cumtime 0.082s），其中 `for` 循环内的 `if word not in unique` 列表线性扫描是瓶颈——30000 次迭代，每次平均扫描数百个元素。

## 优化（set 去重，O(n)）

将列表替换为 `set`，哈希查找 O(1)，整体降为 O(n)：

```python
words = open("words.txt", encoding="utf-8").read().split()
unique = set(words)
print("count=", len(unique))
```

最终 count 由程序算出（与优化前完全一致，均为 1000），未写死。

## 性能对比

| 轮次 | 优化前 | 优化后 |
| --- | --- | --- |
| 第 1 次 | 0.091s | 0.022s |
| 第 2 次 | 0.092s | 0.016s |
| **中位数** | **0.0915s** | **0.0190s** |
| **count** | 1000 | 1000 |
| **加速比** | — | **4.82x** |

## 关键技术点

- **先测量再优化**：用 `time` 量化基线，用 `cProfile -s cumulative` 定位真正瓶颈，不凭直觉改代码
- **数据结构选择**：列表 `in` 是 O(n) 线性扫描，set 是 O(1) 哈希查找；去重场景 set 是正确选择
- **可重复实验**：固定 random seed，保证优化前后输入完全一致，对比才有意义
- **正确性验证**：优化前后 count 必须一致（均为 1000），加速比才有意义
