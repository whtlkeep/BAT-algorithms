"""
题目：
    编写一个程序，找到两个单链表相交的起始节点。

示例：
    A:         a1 → a2
                       ↘
                         c1 → c2 → c3
                       ↗
    B:    b1 → b2 → b3
    A和B相较于c1节点

思路：
    设 A 的长度为 a + c，B 的长度为 b + c，其中 c 为尾部公共部分长度，可知 a + c + b = b + c + a。
    当访问 A 链表的指针访问到链表尾部时，令它从链表 B 的头部开始访问链表 B；
    同样地，当访问 B 链表的指针访问到链表尾部时，令它从链表 A 的头部开始访问链表 A。
    这样就能控制访问 A 和 B 两个链表的指针能同时访问到交点。

    图解：
    a1 -> a2 -> c1 -> c2 -> c3 -> b1 -> b2 -> b3 -> c1 -> c2 -> c3  访问A的指针，先访问A，再访问B
    b1 -> b2 -> b3 -> c1 -> c2 -> c3 -> a1 -> a2 -> c1 -> c2 -> c3  访问B的指针，先访问B，再访问A
                                                 同时到达交点c1

"""


def get_intersection_node(head1, head2):
    cur1, cur2 = head1, head2
    while cur1 != cur2:
        cur1 = head2 if cur1 is None else cur1.next
        cur2 = head1 if cur2 is None else cur2.next
    return cur1
