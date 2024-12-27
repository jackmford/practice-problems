"""
Given a binary tree, determine if it is
height-balanced.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        f = True
        def dfs(root):
            nonlocal f
            if root is None:
                return 0

            left = dfs(root.left)
            right = dfs(root.right)
            if abs(left-right) > 1:
                f = False

            return max(left, right) + 1

        dfs(root)
        return f
