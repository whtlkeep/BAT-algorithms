"""
    链表相加的题目一共两种：
        1、数字用链表逆序存储，例如 123 用链表表示是 3 -> 2 -> 1
        2、数字用链表顺序存储，例如 123 用链表表示是 1 -> 2 -> 3

    以链表为基础做加法运算
"""
# ---------------------- 建议先看链表相加-逆序篇--------------------
"""
一、题目
    数字用链表顺序存储，计算任意给定的两个非负整数。
    如：(7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4) 得到: 7 -> 8 -> 0 -> 7

二、思路 同其他几种"加法"
    题目的本质是加法运算，注意加法的进位情况，和链表的一些特性即可
    加法运算都是从个位数开始加的，注意进位
    注意，将顺序链表进行逆序操作，可以得到逆序表示，这样就可以从左到右进行逐位计算
    
    下面的循环的结构是任何加法运算（二进制、字符串、链表）的通用结构，值得仔细品味
"""

from Linklist.utils import *


def reverse_list(head):
    new_head = ListNode(-1)  # 头结点
    while head:
        next = head.next
        head.next = new_head.next
        new_head.next = head
        head = next
    return new_head.next


def add(head1, head2):
    # 先将链表逆序
    head1 = reverse_list(head1)
    head2 = reverse_list(head2)
    # 以下操作同逆序链表相加
    cur1 = head1
    cur2 = head2
    carry = 0
    new_head = ListNode(-1)
    while carry > 0 or cur1 is not None or cur2 is not None:
        if cur1 is not None:
            carry += cur1.val
            cur1 = cur1.next
        if cur2 is not None:
            carry += cur2.val
            cur2 = cur2.next
        # 将求和结果利用“头插法”，得到顺序链表
        cur = ListNode(carry % 10)
        cur.next = new_head.next
        new_head.next = cur
        carry = int(carry / 10)
    return new_head.next


if __name__ == '__main__':
    l1 = build_l([8, 9, 9])
    l2 = build_l([9, 0, 1])
    print_l(add(l1, l2))
