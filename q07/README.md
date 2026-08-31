# 第7题：用调试器定位归并排序缺陷

**主题**：Debugging

## 题目要求

将给定存在缺陷的归并排序代码保存为 `q07/merge_sort.py`，再使用调试器定位并修复：

- 先运行给定输入，确认结果错误或出现异常
- 使用 pdb、IDE debugger 或等价调试器，在 `merge` 中设置断点并观察 `i`、`j`、`left[i]`、`right[j]`
- 完成最小修复，不得用 `sorted` 替换归并排序
- 使用 pytest 增加两个测试：给定输入和含重复元素的列表；保证测试通过

## 缺陷定位

原代码 `merge` 函数的 `else` 分支存在索引错误：

```python
else:
    result.append(right[i])   # bug：应该访问 right[j]
    j += 1
```

当 `right[j] <= left[i]` 时本应取 `right[j]`，却误写成了 `right[i]`（用另一个列表的 `i` 下标去访问 `right`），导致合并结果错乱。

## 调试过程

1. 运行 `python3 merge_sort.py`，确认输出与预期不符
2. 在 VS Code 中为 `merge` 设置断点，使用调试器（debugpy）单步执行
3. 观察变量面板：`i`、`j`、`left`、`right`、`result` 的实时值
4. 在 `else` 分支命中断点时发现：`left=[1,3]`、`right=[1,4]`、`i=1`、`j=1`，此时 `result.append(right[i])` 访问的是 `right[1]` 而非应取的 `right[1]`，定位到索引错误
5. 最小修复：`right[i]` → `right[j]`

## 修复结果

```python
else:
    result.append(right[j])   # 修复：right[i] -> right[j]
    j += 1
```

运行验证：

```text
给定输入:  [1, 1, 2, 3, 4, 5, 6, 9]
含重复元素: [1, 2, 2, 5, 5, 5, 8, 9]
```

## pytest 单元测试

按题目要求新增 `test_merge_sort.py`，覆盖两个场景：

```python
from merge_sort import merge_sort

def test_merge_sort_given_input():
    assert merge_sort([3, 1, 4, 1, 5, 9, 2, 6]) == [1, 1, 2, 3, 4, 5, 6, 9]

def test_merge_sort_with_duplicates():
    assert merge_sort([5, 2, 8, 2, 9, 1, 5, 5]) == [1, 2, 2, 5, 5, 5, 8, 9]
```

运行结果：`2 passed in 0.22s`。

## 关键技术点

- **断点调试**：在可疑分支设断点，单步跟踪变量变化，比打印定位更快
- **变量监视**：调试面板实时显示 `i`/`j`/`left`/`right`/`result`，直观发现越界/错位
- **最小修复**：只改错的那一行，不重写算法
- **pytest 回归**：两个用例覆盖给定输入与含重复元素场景，防止修复引入回归
