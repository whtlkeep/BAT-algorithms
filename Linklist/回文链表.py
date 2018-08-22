"""
题目：
    判断一个链表是否为回文链表

示例：
    1->2 False
    1->2->2->1 True

思路：
    step1:通过快慢指针找到链表中间节点
    step2:将链表切分成两个子链表
    step3:将第二个链表逆序
    step4:逐个判断链表元素是否相同

    注意：要考虑链表节点个数的奇偶性
"""
from Linklist.utils import *


def is_palindrome(head):
    if head is None or head.next is None:
        return True
    slow = head
    fast = slow.next
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
    if fast is not None:  # 链表共偶数个节点，让 slow 指向下一个节点
        slow = slow.next
    cut(head, slow)
    return is_equal(head, reverse_list(slow))


def reverse_list(head):
    new_head = ListNode(-1)  # 头结点
    while head:
        next = head.next
        head.next = new_head.next
        new_head.next = head
        head = next
    return new_head.next


def cut(head, cut_node):
    while head.next != cut_node:
        head = head.next
    head.next = None


def is_equal(head1, head2):
    while head1 is not None and head2 is not None:
        if head1.val != head2.val:
            return False
        head1 = head1.next
        head2 = head2.next
    return True


if __name__ == '__main__':
    print("----------test 1-------------")
    l1 = build_l([1, 2, 3, 2, 1])
    print_l(l1, p_type="SINGLE")
    print(is_palindrome(l1))
    print("----------test 2-------------")
    l2 = build_l([1, 2, 3])
    print_l(l2, p_type="SINGLE")
    print(is_palindrome(l2))
