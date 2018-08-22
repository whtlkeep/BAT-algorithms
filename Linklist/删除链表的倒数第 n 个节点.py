"""
题目：
    给定一个链表，删除链表的倒数第 k 个节点，并且返回链表的头结点。

示例:
    给定一个链表: 1->2->3->4->5, 和 k = 2.
    当删除了倒数第二个节点后，链表变为 1->2->3->5.

思路:
    第一种：遍历一次，获得链表长度N，则可知 倒数第k个节点 == 顺数第N-k+1个节点，再次遍历，删除即可。 （一共需要两次遍历）
    第二种：使用快慢指针遍历，让快指针先走k步，然后快慢指针一起移动，当快指针遍历到末尾，慢指针正好在倒数第k个节点上，删除即可
"""

from Linklist.utils import *


def remove_k_th_from_end(head, k):
    fast = head
    while k > 0:
        fast = fast.next
        k -= 1
    if fast is None:
        return head.next
    slow = head
    while fast.next is not None:
        fast = fast.next
        slow = slow.next
    slow.next = slow.next.next
    return head


if __name__ == '__main__':
    head1 = build_l([1, 2, 3, 4, 5])
    print_l(remove_k_th_from_end(head1, 2))
