# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(root, left, right):
            if root is None:
                return True
            if left >= root.val or right <= root.val:
                return False

            left = dfs(root.left, left, root.val)
            right = dfs(root.right, root.val, right)

            return left and right

        return dfs(root, float("-inf"), float("inf"))

            

