"""
Given the roots of two binary trees p and q, return true if the trees are equivalent, otherwise return false.

Two binary trees are considered equivalent if they share the exact same structure and the nodes have the same values.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        self.res = True

        def dfs(proot, qroot):
            if proot == None or qroot == None:
                self.res = False
                return
            if proot.val != qroot.val:
                self.res = False
            dfs(proot.left, qroot.left)
            dfs(proot.right, qroot.right)
            return

        dfs(p, q)
        return self.res
