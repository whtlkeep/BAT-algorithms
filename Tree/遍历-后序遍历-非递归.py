class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def post_order_traversal(root):  # 后序
    """
    前序遍历为 root -> left -> right，后序遍历为 left -> right -> root，
    可以修改前序遍历成为 root -> right -> left，那么这个顺序就和后序遍历正好相反
    """
    result = []
    stack = []
    stack.append(root)
    while len(stack) != 0:
        node = stack.pop()
        if node is None:
            continue
        result.append(node.val)
        stack.append(node.left)
        stack.append(node.right)
    return result[::-1]
