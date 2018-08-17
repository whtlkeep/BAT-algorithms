"""
    链表相加的题目一共两种：
        1、数字用链表逆序存储，例如 123 用链表表示是 3 -> 2 -> 1
        2、数字用链表顺序存储，例如 123 用链表表示是 1 -> 2 -> 3

    以链表为基础做加法运算
"""

"""
一、题目
    数字用链表逆序存储，计算任意给定的两个非负整数。
    如：输入 2 -> 4 -> 3, 5 -> 6 -> 4, 得到 7 -> 0 -> 8.
                342     +     465       =      807

二、思路
    题目的本质是加法运算，注意加法的进位情况，和链表的一些特性即可
    加法运算都是从个位数开始加的，注意进位
    逆序表示的数据，正好可以从头向后依次相加
"""
from Linklist.utils import build_single_list, print_single_list, ListNode


def add(l1, l2):
    carry = 0  # 进位
    l_head = ListNode(-1)  # 创建一个头结点，再运算完后需要删除
    l_Tail = l_head
    while l1 and l2:
        value = l1.val + l2.val + carry
        carry = value // 10
        value = value % 10
        l_Tail.next = ListNode(value)
        l_Tail = l_Tail.next
        l1 = l1.next
        l2 = l2.next

    # 看看哪个链表比较长，继续做加法
    l3 = None
    if l1:
        l3 = l1
    else:
        l3 = l2
    while l3:
        value = l3.val + carry
        carry = value // 10
        value = value % 10
        l_Tail.next = ListNode(value)
        l_Tail = l_Tail.next
        l3 = l3.next
    if carry != 0:  # 处理可能存在的进位
        l_Tail.next = ListNode(carry)
    return l_head.next  # 跳过头结点才是正确的解


if __name__ == '__main__':
    # 创建一个单链表l1    4 -> 9 -> 0 -> 4 -> 7 -> 1
    l1 = build_single_list([9, 9, 9])
    # 创建一个单链表l2    1 -> 7 -> 1 -> 5 -> 5 -> 4 -> 2 -> 8
    l2 = build_single_list([1])
    print_single_list(head=add(l1, l2), pType="SINGLE")
