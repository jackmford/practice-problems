# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.maxDiameter = 0
        def dfs(root) -> int:
            if root is None:
                return 0
            
            left = dfs(root.left)
            right = dfs(root.right)
            if left + right > self.maxDiameter:
                self.maxDiameter = left+right

            return (max(left,right)+1)

        dfs(root)
        return self.maxDiameter
