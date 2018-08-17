""" 有序树
一、题目
    给定二叉查找树（有序的意思），求两个节点p,q的最近公共祖先
            _______6______
          /                \
      ___2__             ___8__
     /      \           /      \
    0        4         7        9
            /  \
           3   5
    比如：节点 2 和 8 的最近公共祖先是 6
         节点 3 和 7 的最近公共祖先是 6

二、思路
    递归大法,利用有序的性质:
        当节点p,q的值都小于root，则最近公共祖先肯定是在root的左子树中
        当节点p,q的值都大于root，则最近公共祖先肯定是在root的右子树中
        当以上两种情况都不满足，则root就是公共祖先

三、同
    LeetCode-235
"""


def lowestCommonAncestor(root, p, q):
    if root.val > p.val and root.val > q.val:
        return lowestCommonAncestor(root.left, p, q)
    if root.val < p.val and root.val < q.val:
        return lowestCommonAncestor(root.right, p, q)
    return root


"""  无序树
一、题目
    给定二叉树（无序的意思），求两个节点p,q的最近公共祖先
           _______3______
          /              \
      ___5__           ___1__
     /      \         /      \
    6        2       0        8
            /  \
           7    4
    比如：节点 5 和 1 的最近公共祖先是 3
         节点 4 和 5 的最近公共祖先是 5
         
二、思路
    递归大法:
        if 当前节点root等于None、p或者q，则该root节点就是公共祖先
        else 就在root的左右子树中分别去寻找公共祖先。
        
三、同
    LeetCode-236
"""


def lowestCommonAncestor(root, p, q):
    if root is None or root == p or root == q:
        return root
    left = lowestCommonAncestor(root.left, p, q)
    right = lowestCommonAncestor(root.right, p, q)
    if left is None:
        return right
    elif right is None:
        return left
    else:
        return root
