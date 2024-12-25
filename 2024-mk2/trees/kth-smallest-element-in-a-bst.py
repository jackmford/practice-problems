class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        self.order = 0
        self.res = 0

        def dfs(root):
            if root is None:
                return

            dfs(root.left)
            
            if self.order == k-1:
                self.res = root.val
            self.order+=1
            
            dfs(root.right)

        dfs(root)

        return self.res

