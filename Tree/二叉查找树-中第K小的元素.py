"""
一、题目
    给定一个二叉搜索树，编写一个函数 kthSmallest 来查找其中第 k 个最小的元素。

二、思路
    本题要充分利用二叉搜索树有序的性质。一个节点的左子树上的节点都比该节点小，右子树上的节点都比该节点大；
    因此我们可以求当前节点左子树的个数left_count:
        * 如果 left_count == k-1, 则该节点就是第k小的元素；
        * 如果 left_count < k-1, 则第K小的数在右子树中，而且在右子树中变成了第 k - left_count - 1 小的数了
        * 如果 left_count > k-1, 则第k小的数在左子树中，而且还是第k小的元素

三、同
    LeetCode-230
"""


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 采用递归的思路求一棵树的节点个数
def count(node):
    if node is None:
        return 0
    return count(node.left) + count(node.right) + 1


def kthSmallest(root, k):
    leftc = count(root.left)
    if leftc == k - 1:
        return root.val
    if leftc > k - 1:
        return kthSmallest(root.left, k)
    return kthSmallest(root.right, k - leftc - 1)
