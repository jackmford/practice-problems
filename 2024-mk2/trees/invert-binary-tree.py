# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        # Write a function to switch the left and right children of any node

        def dfs(root):
            if root is None:
                return
            
            left = dfs(root.left)
            right = dfs(root.right)

            tmp = left
            root.left = right
            root.right = tmp

            return root

        return dfs(root)
