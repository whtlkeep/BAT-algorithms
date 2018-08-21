"""
题目：
    给定一个单链表，把所有的奇数节点和偶数节点分别排在一起。
    请注意，这里的奇数节点和偶数节点指的是节点编号的奇偶性，而不是节点的值的奇偶性。
    请尝试使用原地算法完成。你的算法的空间复杂度应为 O(1)，时间复杂度应为 O(nodes)，nodes 为节点总数。

示例：
    输入: 2->1->3->5->6->4->7->NULL
    输出: 2->3->6->7->1->5->4->NULL

思路：
    将奇数位置的节点连接起来，将偶数位置的节点连接起来，再拼接起来即可
"""
from Linklist.utils import *


def odd_even_list(head):
    if head is None:
        return head
    odd = head
    even = head.next
    even_head = even
    while even is not None and even.next is not None:
        odd.next = odd.next.next
        odd = odd.next
        even.next = even.next.next
        even = even.next
    odd.next = even_head
    return head


if __name__ == '__main__':
    head1 = build_l([2, 1, 3, 5, 6, 4, 7])
    print_l(odd_even_list(head1))
