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


def max_depth(root):
    if root is None:
        return 0
    return max(max_depth(root.left) + 1, max_depth(root.right) + 1)


if __name__ == '__main__':
    from Tree.tree import construct_tree

    root = construct_tree()
    print(max_depth(root))
