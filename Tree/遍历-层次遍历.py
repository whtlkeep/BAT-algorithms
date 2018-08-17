"""
一、题目
    按层次的遍历的方法打印一颗树

    例如有如下一棵树：
        5
       / \
      3   6
     / \   \
    2   4   7

    打印结果是
    5 3 6 2 4 7

二、思路
    层次遍历的步骤是：
    对于不为空的结点，先把该结点加入到队列中
    从队中拿出结点，如果该结点的左右结点不为空，就分别把左右结点加入到队列中
    重复以上操作直到队列为空

"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def hierarchical_traversal(root):
    if root is None:
        return []
    # 用一个list和一个索引index模拟队列的先进先出
    queue = []
    index = 0
    result = []
    queue.append(root)
    while len(queue) > index:
        temp = queue[index]
        index += 1
        result.append(temp.val)
        if temp.left is not None:
            queue.append(temp.left)
        if temp.right is not None:
            queue.append(temp.right)
    return result


if __name__ == '__main__':
    from Tree.tree import construct_tree

    root = construct_tree()
    print(hierarchical_traversal(root))
