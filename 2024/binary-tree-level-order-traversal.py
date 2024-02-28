# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        q = []
        q.append(root)
        res = []
        visited = []
        
        #res.append([root.val])
        while q:
            qLen = len(q)
            level = []
            for i in range(qLen):
                cur = q.pop(0)   
                if cur:
                    level.append(cur.val)
                    q.append(cur.left)
                    q.append(cur.right)
            if level:
                res.append(level)
        
        return res