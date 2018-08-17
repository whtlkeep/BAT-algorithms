"""
一、题目
    分行从上之下打印一颗二叉树

    例如有如下一棵树：
        5
       / \
      3   6
     / \   \
    2   4   7

    打印结果是
    5
    3 6
    2 4 7
二、思路
    在层次遍历的基础加以改进
    如何实现逐行打印，必须要知道每一行的开始和结束。如何准确地获得该信息是关键。
    核心思想：在每一层开始遍历前，队列中存储的就是该行的全部是数据，用size记录，然后一次性全部遍历。
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def print_from_top_to_bottom(root):
    if root is None:
        return []
    # 用一个list和一个索引index模拟队列的先进先出
    queue = []
    index = 0
    result = []
    queue.append(root)
    while len(queue) > index:
        size = len(queue) - index  # 新遍历一个层时，队列中存储是该层的全部数据，size记录个数
        res = []
        for i in range(size):  # 遍历size次
            temp = queue[index]
            index += 1
            res.append(temp.val)
            if temp.left is not None:
                queue.append(temp.left)
            if temp.right is not None:
                queue.append(temp.right)
        result.append(res)
    return result


if __name__ == '__main__':
    from Tree.tree import construct_tree

    root = construct_tree()
    print(print_from_top_to_bottom(root))
