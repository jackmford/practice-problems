# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # Use DFS to find paths and if there is a node in the path greater than current node it is bad

        self.count = 0
        def dfs(root, maxVal):
            if root is None:
                return


            if root.val >= maxVal:
                self.count+=1
            maxVal = max(maxVal, root.val)

            dfs(root.left, maxVal)
            dfs(root.right, maxVal)
        
        dfs(root, root.val)

        return self.count

