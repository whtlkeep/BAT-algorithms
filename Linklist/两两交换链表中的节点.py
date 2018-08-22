"""
题目：
    给定一个链表，两两交换其中相邻的节点，并返回交换后的链表

示例：
    给定 1->2->3->4, 你应该返回 2->1->4->3.
"""

from Linklist.utils import *


def swap_pairs(head):
    node = ListNode(-1)  # 交换前，在头节点前面加一个值为“-1”的节点
    node.next = head
    pre = node
    while pre.next is not None and pre.next.next is not None:
        l1 = pre.next
        l2 = pre.next.next
        l2_next = l2.next
        l1.next = l2_next
        l2.next = l1
        pre.next = l2
        pre = l1
    return node.next


if __name__ == '__main__':
    head1 = build_l([1, 2, 3, 4, 5])
    print_l(swap_pairs(head1))
