# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
    # Is this BFS and mark the nodes that we see when we only have one item in the queue? 
        queue = []
        queue.append(root)
        res = []

        while queue:
            farthestRight = None
            # Get the length of each level
            lengthOfQ = len(queue)

            # This goes through each level at once, instead of one node at a time in normal BFS
            for i in range(lengthOfQ):
                cur = queue[0]
                queue = queue[1:]
                
                if cur:
                    farthestRight = cur
                    queue.append(cur.left)
                    queue.append(cur.right)
            
            if farthestRight:
                res.append(farthestRight.val)

        return res

