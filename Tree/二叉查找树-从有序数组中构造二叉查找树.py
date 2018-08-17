"""
一、题目
    将一个按照升序排列的有序数组，转换为一棵高度平衡二叉搜索树。
    本题中，一个高度平衡二叉树是指一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1。

二、思路
    递归大法
    利用二分查找的思路，二分建树。
    二分的中点是根节点（相对而言的，每个子树都有根节点），左边的序列建立左子树，右边的序列建立右子树

三、同
    LeetCode-108
"""


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def to_BST(nums, start, end):
    if start > end:
        return None
    middle = (start + end) >> 1
    root = TreeNode(nums[middle])
    root.left = to_BST(nums, start, middle - 1)
    root.right = to_BST(nums, middle + 1, end)
    return root


def sortedArrayToBST(nums):
    return to_BST(nums, 0, len(nums) - 1)
