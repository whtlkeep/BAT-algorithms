"""
题目:
    给定一个排序链表，删除所有重复的元素，使得每个元素只出现一次。

示例:
    输入: 1->1->2->3->3
    输出: 1->2->3

思路：
    递归大法
    先对后n-1个节点进行去重，得头节点temp，再比较第一个节点和temp,
    若值相同，直接返回temp;
    若值不同，则把temp接在第一个节点后面，返回第一个节点
"""
from Linklist.utils import *


def delete_duplicates(head):
    if head is None or head.next is None:
        return head
    head.next = delete_duplicates(head.next)
    if head.val == head.next.val:
        return head.next
    else:
        return head


if __name__ == '__main__':
    head1 = build_l([1, 1, 1, 2, 2, 3, 10, 12])
    print_l(delete_duplicates(head1))
