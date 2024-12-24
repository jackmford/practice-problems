# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # DFS and count edges on the left side and edges on the right side?
        # But you need to do it at each level

        # Base case, if both children are none, return 0
        # Keep a max variable
        self.m = 0
        def dfs(root):
            if root is None:
                return 0
            
            left = dfs(root.left)
            right = dfs(root.right)

            self.m = max(self.m, left+right)

            return max(left, right)+1
        
        dfs(root)
        return self.m

