"""
一、题目
    给定一个单链表，其中的元素按升序排序，将其转换为高度平衡的二叉搜索树。
    本题中，一个高度平衡二叉树是指一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1。

二、思路
    递归大法
    利用二分查找的思路，二分建树。
    二分的中点是根节点（相对而言的，每个子树都有根节点），左边的序列建立左子树，右边的序列建立右子树

三、本题与“从有序数组中构建二叉查找树”的整体思路是一样的
    只是单链表无法直接获得中间节点，必须通过顺序遍历才能得到mid位置的节点。
    遍历的方法是用“快慢指针”: 快指针每走两步，慢指针只走1步，这样快指针走到重点时，慢指针在中间。

    *** “快慢指针”是单链表中的重要方法，很多问题都要用到这个技巧，才能实现最优解 ***

四、同
    LeetCode-109
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 找到单链表中间节点mid的前驱
def pre_Mid(head):
    slow = head
    fast = head.next
    pre = head
    while fast is not None and fast.next is not None:
        pre = slow
        slow = slow.next
        fast = fast.next.next
    return pre


def sortedListToBST(head):
    if head is None:
        return None
    if head.next is None:
        return TreeNode(head.val)

    preMid = pre_Mid(head)
    mid = preMid.next
    preMid.next = None  # 断开链表

    t = TreeNode(mid.val)
    t.left = sortedListToBST(head)
    t.right = sortedListToBST(mid.next)
    return t
