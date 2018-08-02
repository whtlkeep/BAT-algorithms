"""
一、题目
    给定一个二叉树，找出其最大的深度

二、思路
    用递归的思路，求左孩子的高度，求右孩子的高度，哪个大，就加1

三、同
    leetcode-104
"""


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def maxDepth(root):
    """
    :type root: TreeNode
    :rtype: int
    """
    if root == None:
        return 0
    return max(maxDepth(root.left) + 1, maxDepth(root.right) + 1)
