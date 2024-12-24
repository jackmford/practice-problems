# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Level Order Traversal
        queue = []
        queue.append(root)
        res = []

        while queue:
            qLen = len(queue)
            tmp = []
            for i in range(qLen):
                cur = queue[0]
                queue = queue[1:]

                if cur:
                    tmp.append(cur.val)
                    queue.append(cur.left)
                    queue.append(cur.right)
            if len(tmp) > 0:
                res.append(tmp)
        return res
