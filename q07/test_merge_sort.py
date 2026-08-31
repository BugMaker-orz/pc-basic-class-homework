"""第7题 pytest 单元测试：给定输入 + 含重复元素的列表。"""
from merge_sort import merge_sort


def test_merge_sort_given_input():
    # 给定输入
    assert merge_sort([3, 1, 4, 1, 5, 9, 2, 6]) == [1, 1, 2, 3, 4, 5, 6, 9]


def test_merge_sort_with_duplicates():
    # 含重复元素
    assert merge_sort([5, 2, 8, 2, 9, 1, 5, 5]) == [1, 2, 2, 5, 5, 5, 8, 9]
