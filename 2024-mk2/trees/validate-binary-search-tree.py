class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(root, left, right):
            if root is None:
                return True
            if (left < root.val < right) == False:
                return False

            left = dfs(root.left, left, root.val)
            right = dfs(root.right, root.val, right)

            return left and right

        return dfs(root, float("-inf"), float("inf"))


