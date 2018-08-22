"""
一、题目
    将一个链表进行逆序
    如： 1->2->3 逆序得到 3->2->1

二、思路
    * 递归大法
        可以将链表任意一个链表看成由 一个节点和一串节点 组成的，将其进行交换即可。
        如： 1  - >  2 - > 3 -> 4                 2 - > 3 -> 4  ->  1
            ---     --------------   交换         ------------     ---
            一个         一串                         一串         一个
        对上面的一串再进行同样的递归操作，最后得到的便是逆序的

    * 头插法
        新建一个头结点，遍历单链表，将每个结点插入到该头结点后面，即可实现逆序
"""
from Linklist.utils import *


# 递归实现
def reverse_list(head):
    if head is None or head.next is None:
        return head
    right = head.next
    new_head = reverse_list(right)
    right.next = head
    head.next = None
    return new_head


# 头插法逆序
def reverse_list(head):
    new_head = ListNode(-1)  # 头结点
    while head:
        next = head.next
        head.next = new_head.next
        new_head.next = head
        head = next
    return new_head.next


if __name__ == '__main__':
    head1 = build_l([1, 2, 3, 4])
    print_l(reverse_list(head1))
