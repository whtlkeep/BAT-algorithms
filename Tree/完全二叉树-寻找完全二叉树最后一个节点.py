"""
一、题目
    任意给定一个完全二叉树（定义可自行 百度），寻找树的最后一个节点

    举例
          5
       /    \
      3      6
     / \    /
    2   4  7     是完全二叉树， 最后一个节点是7

        5
       / \
      3   6
     / \   \
    2   4   7    不是完全二叉树

二、思路
    * 暴力求解 O(N)
        可以采用层次遍历，将整个树遍历一遍，最后一个遍历到的节点即为所求。【层次遍历可以参考 /树/层次遍历.py】
    * 二分查找 O(logN)
        假如本题是普通二叉树，可能只有采用遍历的方法，但是题目的关键字是“完全树”，必须利用其特性来优化方法。
        值得思考的性质有如下几点：（对照上面例子中的第一棵树考虑）
            1、最后一个节点肯定是在最后一层，例如节点 7 在第 3 层
            2、最后一个节点肯定是在最后一层的最右边；
            3、完全二叉树获取树高最快的方式是从根节点（每一棵子树都有根节点）出发一直向左遍历，遍历到头，经过的节点数目就是树高。
                求树高的复杂度是O（logN）

        利用以上三点性质，讨论二分查找的思想：
            1、对于根节点，如果左右子树的树高不等，则最后一个节点在左子树中（性质2）
            2、如果左右子树的树高相等，则最后一个节点在右子树中（性质 1）
"""


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 计算一颗完全二叉树的树高
def count_height(node):
    height = 0
    while node:
        height += 1
        node = node.left
    return height


def find_last_node(root):
    if root is None:
        return
    left_count = count_height(root.left)
    right_count = count_height(root.right)
    if left_count != right_count:  # 如果左右子树的树高不等，则最后一个节点在左子树中（性质2）
        return find_last_node(root.left)
    elif left_count == right_count:
        if left_count == 0:  # 树没有孩子节点，则该根节点是最后一个节点
            return root
        elif left_count == 1:  # 有左右孩子节点，都是叶节点,右孩子是最后一个节点
            return root.right
        else:  # 如果左右子树的树高相等，则最后一个节点在右子树中
            return find_last_node(root.right)


if __name__ == '__main__':
    root = TreeNode(5)
    root.left = TreeNode(3)
    root.right = TreeNode(6)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(7)
    print(find_last_node(root).val)
