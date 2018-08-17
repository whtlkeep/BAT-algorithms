class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def in_order_traversal(root):  # 中序
    res = []
    stack = []
    if root is None:
        return res
    cur = root
    while len(stack) != 0 or cur is not None:
        while cur is not None:
            stack.append(cur)
            cur = cur.left
        node = stack.pop()
        res.append(node.val)
        cur = node.right
    return res
