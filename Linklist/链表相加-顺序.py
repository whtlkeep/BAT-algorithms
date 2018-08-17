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

二、思路
    题目的本质是加法运算，注意加法的进位情况，和链表的一些特性即可
    加法运算都是从个位数开始加的，注意进位
    假如是逆序表示的数据，正好可以从头向后依次相加，但本题是顺序表示。
    其实我们可以将链表逆序后，实现过程就和逆序相加一模一样了,但是需要注意的是必须将求和后的链表再次逆序
    本题：利用stack将链表逆序
"""

from Linklist.utils import build_single_list, print_single_list, ListNode


def reverse_single_list(head):
    """
    给定一个头结点，返回一个栈，存储是各个结点的数据
    :param head:
    :return: list
    """
    stack = []
    p = head
    while p:
        stack.append(p.val)
        p = p.next
    return stack


def add(l1, l2):
    l1stack = reverse_single_list(l1)
    l2stack = reverse_single_list(l2)
    carry = 0  # 进位
    l_head = ListNode(-1)  # 创建一个头结点，再运算完后需要删除
    while len(l1stack) > 0 and len(l2stack) > 0:
        value = l1stack.pop() + l2stack.pop() + carry
        carry = value // 10
        value = value % 10
        cur = ListNode(value)  # 通过不断在头结点后面插入结点，实现逆序的
        cur.next = l_head.next
        l_head.next = cur

    # 看看哪个链表比较长，继续做加法
    l3stack = None
    if len(l1stack) > 0:
        l3stack = l1stack
    else:
        l3stack = l2stack
    while len(l3stack) > 0:
        value = l3stack.pop() + carry
        carry = value // 10
        value = value % 10
        cur = ListNode(value)
        cur.next = l_head.next
        l_head.next = cur
    if carry != 0:  # 处理可能存在的进位
        cur = ListNode(carry)
        cur.next = l_head.next
        l_head.next = cur
    return l_head.next  # 跳过头结点才是正确的解


if __name__ == '__main__':
    l1 = build_single_list([9, 9, 9])
    l2 = build_single_list([1])
    print_single_list(add(l1, l2))
