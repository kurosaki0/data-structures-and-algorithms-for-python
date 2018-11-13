# coding: utf-8

"""
给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。

leetcode 236
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if not root or root == p or root == q:
            return root

        # 分别在左右子树中找p，q
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left and right:
            # 若左右子树不为空，说明p，q分别在左右子树两侧，那么p，q的最近公共祖先就是root
            return root
        else:
            # 若left或者right有一个为空，说明p，q在在左右子树同侧，那么p，q的最近公共祖先就是不为空的那个
            return left if left else right


if __name__ == '__main__':
    binary = [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]

    a = TreeNode(3)
    b = TreeNode(5)
    c = TreeNode(1)
    d = TreeNode(6)
    e = TreeNode(2)
    f = TreeNode(0)
    g = TreeNode(8)
    h = TreeNode(None)
    i = TreeNode(None)
    j = TreeNode(7)
    k = TreeNode(4)

    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.left = f
    c.right = g
    d.left = h
    d.right = i
    e.left = j
    e.right = k

    obj = Solution()
    print(obj.lowestCommonAncestor(a, b, c))
