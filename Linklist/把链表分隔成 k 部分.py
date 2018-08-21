"""
题目：
    把链表分隔成 k 部分，每部分的长度都应该尽可能相同，排在前面的长度应该大于等于后面的。

示例：
    Input:
    root =  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], k = 3
    Output: [[1, 2, 3, 4], [5, 6, 7], [8, 9, 10]]
"""

from Linklist.utils import *


def split_list_to_parts(root, k):
    cur = root
    count = 0  # 统计节点个数
    while cur is not None:
        count += 1
        cur = cur.next
    mod = count % k
    size = int(count / k)
    cut_way = [size] * k  # 划分成k个部分，cut_way中记录每部分的节点个数
    for i in range(mod):
        cut_way[i] += 1

    result = [None] * k
    cur = root
    i = 0
    # 按cut_way中每部分的节点个数将链表分成k断，存于result中
    while cur is not None and i < k:
        result[i] = cur
        for j in range(cut_way[i] - 1):
            cur = cur.next
        next1 = cur.next
        cur.next = None
        cur = next1
        i += 1
    return result


if __name__ == '__main__':
    head = build_l([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    for l in split_list_to_parts(head, 3):
        print_l(l)
