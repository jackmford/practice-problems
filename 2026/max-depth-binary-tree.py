# Assume the tree node looks like this:
# class TreeNode:
#    def __init__(self, val=0, left=None, right=None):
#        self.val = val
#        self.left = left
#        self.right = right


def max_depth(root):

    def dfs(node):
        if node is None:
            return 0

        left = dfs(node.left)
        right = dfs(node.right)

        return 1 + max(left, right)

    dfs(root)
