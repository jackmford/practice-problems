# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False

        if self.dfs(root, subRoot):
            return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def dfs(self, r, s):
        if r is None and s is None:
            return True
        if r is None and s is not None:
            return False
        if r is not None and s is None:
            return False
        if r.val != s.val:
            return False

        left = self.dfs(r.left, s.left)
        right = self.dfs(r.right, s.right)

        return right and left
