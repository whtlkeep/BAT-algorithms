"""
一、题目
    给定一个二叉搜索树和一个目标结果，如果 BST 中存在两个元素且它们的和等于给定的目标结果，则返回 true。

二、案例
    输入:
        5
       / \
      3   6
     / \   \
    2   4   7

    Target = 9

    输出: True（因为存在 2 + 7 = 9）

三、思路
    使用中序遍历得到有序数组之后，再利用双指针对数组进行查找。
    应该注意到，这一题不能用分别在左右子树两部分来处理这种思想，因为两个待求的节点可能分别在左右子树中。
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 中序遍历 非递归实现
def inorder_traversal(root, nums):
    stack = []
    cur = root
    if root is None:
        return nums
    while len(stack) != 0 or cur is not None:
        while cur is not None:
            stack.append(cur)
            cur = cur.left
        node = stack.pop()
        nums.append(node.val)
        cur = node.right


def findTarget(root, k):
    """
    :type root: TreeNode
    :type k: int
    :rtype: bool
    """
    nums = []
    inorder_traversal(root, nums)
    start = 0
    end = len(nums) - 1
    while start < end:
        if nums[start] + nums[end] == k:
            return True
        elif nums[start] + nums[end] < k:
            start += 1
        else:
            end -= 1
    return False


if __name__ == '__main__':
    from Tree.tree import construct_tree

    root = construct_tree()
    print(findTarget(root, 9))
