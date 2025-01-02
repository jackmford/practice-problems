"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # For each node, visit it and make a copy
        
        visited = set()
        m = {}

        # For every neighbor that hasn't been copied already call DFS.
        # If it has been copied, just retrieve the copy and add it to the copies neighbors.
        def dfs(root):
            if root is None:
                return None
            
            cp = Node(root.val, [])
            m[root.val] = cp

            for n in root.neighbors:
                if n.val not in m:
                    d = dfs(n)
                    if d != None:
                        cp.neighbors.append(d)
                else:
                    cp.neighbors.append(m[n.val])

            return cp

        return dfs(node)
